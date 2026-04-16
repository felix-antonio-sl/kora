# hsc-cli — Estudio de Sesiones y Cookies

Fecha: 2026-04-14

Objetivo: entender la capa real de autenticación de `hsc-cli` para evitar fallos por entrada, salida, expiración o cambio de sesión en DAU, SGH y LIS.

Base principal:

- `/home/felix/projects/hsc-cli/internal/transport/session.go`
- arqueología de incidentes en `arqueologia/cli-hsc/`

## Estado actual del transporte

`internal/transport/session.go` implementa:

- `cookiejar` en memoria
- un `http.Client` único por `Session`
- tres marcas temporales:
  - `dauAuthed`
  - `sghAuthed`
  - `labAuthed`
- `ensureAuth(sys)` basado solo en TTL lógico

No implementa hoy:

- persistencia real de cookies
- validación de sesión viva por respuesta
- renovación automática homogénea al detectar login HTML
- separación entre “cookie existe” y “sesión sirve”
- manejo explícito de cambio de hospital/sede/servicio en SGH

## Flujo actual por sistema

### DAU

Login:

- POST a `autenticacion.php`
- éxito si el jar recibe `PHPSESSID`

Lectura:

- `Get/Post` llaman `ensureAuth(DAU)`
- si `dauAuthed < 4h`, se asume sesión válida

Riesgo:

- la sesión real puede haber expirado antes
- el código no inspecciona si la respuesta es HTML de login

### SGH

Login:

- POST a `funciones/autenticacion.php`
- éxito si hay `PHPSESSID` y la respuesta no contiene `id="login_form"`

Lectura:

- `ensureAuth(SGH)` usa TTL lógico de 5h

Riesgo:

- la arqueología reporta expiración real alrededor de 6h
- algunos endpoints devuelven template vacío o comportamiento degradado aunque la sesión “parezca viva”
- `curl` directo con cookies llegó a fallar para evoluciones, mientras la CLI unificada funcionaba mejor

### LIS

Login:

- POST a `autenticacion.php`
- éxito si hay `PHPSESSID`

Lectura:

- igual que los otros sistemas, por TTL lógico
- solo `cmd/h/ctx.go` tiene una defensa explícita: si `resultadoseleccion.php` parece formulario de login, hace re-login y retry una vez

Riesgo:

- la detección de sesión vencida en LIS está duplicada en capa de comando, no en transporte

## Hallazgos concretos

### 1. Las cookies no se persisten realmente

`Logout()` borra `~/.h/cookies`, pero `NewSession()` nunca carga ni escribe cookies persistidas. Hoy el jar es solo en memoria. Eso implica:

- cada nueva ejecución del CLI vuelve a loguear
- no hay “continuidad de sesión” entre invocaciones
- borrar `~/.h/cookies` hoy tiene efecto semántico menor o nulo

### 2. `IsAuthed` no significa “sesión válida”

Hoy significa solo:

- “yo recuerdo haber hecho login hace menos de N horas”

No significa:

- “el servidor sigue aceptando la sesión”
- “este endpoint no me está devolviendo el login form”
- “esta sede/hospital/contexto sigue siendo el mismo”

### 3. Falta detector transversal de sesión expirada

El sistema necesita reconocer al menos estos patrones:

- HTML de login explícito
- redirección hacia login
- respuesta vacía/template vacío cuando el endpoint normalmente trae datos
- pérdida de cookie `PHPSESSID`
- cambio de hospital o contexto SGH que invalida la navegación

Hoy eso está:

- parcialmente en `loginSGH()` por `id="login_form"`
- parcialmente en `ctx.go` para LIS
- ausente en el resto

### 4. SGH tiene degradaciones más sutiles que DAU

La arqueología muestra:

- expiración SGH en ~6h
- `cargar_historial_evolucion.php` puede devolver template vacío
- `curl` directo con cookies “correctas” igual falló en algunos casos

Eso sugiere que el problema no es solo cookie válida/no válida. También puede haber:

- dependencia de headers o flujo previo
- estado de sesión en servidor más fino
- navegación acoplada a secuencia de páginas

### 5. DAU y SGH no deben compartir la misma estrategia mental

La propia arqueología lo dice:

- DAU write es más stateless en algunos casos
- SGH write depende mucho más de sesión activa

Eso obliga a un diseño diferenciado:

- `read` DAU: reauth barato y frecuente
- `write` SGH: sesión viva, chequeada y defendida

## Incidentes relevantes ya documentados

### DAU

- cookie DAU expira durante el turno y vuelve HTML de login
- `dau_p.php` puede apuntar a atención histórica y no debe usarse para identidad actual

### SGH

- sesión SGH expira en ~6h
- evoluciones vacías con `curl` directo y mejor comportamiento a través de la CLI
- algunos endpoints devuelven vacío si la sesión o el flujo no están bien establecidos

### LIS

- falta endurecimiento general; solo `ctx.go` hace stale-session retry explícito

## Riesgos operativos actuales

### Riesgo 1: falso positivo de autenticación

El CLI puede creer que está autenticado porque `AuthAge < TTL`, pero el backend ya expuso login form o sesión vencida.

Impacto:

- lecturas silenciosamente incorrectas
- listas vacías interpretadas como “no hay datos”
- mayor riesgo clínico que un fallo duro

### Riesgo 2: lógica de retry dispersa

La recuperación de sesión vencida no está centralizada en `transport`.

Impacto:

- algunos comandos se recuperan
- otros fallan o devuelven basura
- comportamiento inconsistente por sistema y por comando

### Riesgo 3: continuidad falsa entre invocaciones

La sesión no persiste entre procesos, aunque algunas rutas del código sugieren lo contrario.

Impacto:

- costo extra de login
- expectativa equivocada del operador
- diseño confuso del `DataDir/cookies`

### Riesgo 4: cambios de contexto no modelados

SGH tiene endpoints de cambio de hospital/sede (`vistas/cambiar_hospital.php`) y múltiples módulos conectados. El transporte hoy no modela:

- hospital actual
- módulo actual
- pivote previo útil para navegación
- contexto de usuario/sede con que se abrió el flujo

Impacto:

- lecturas inconsistentes en escenarios multi-hospital o multi-contexto
- dificultad para depurar respuestas vacías

## Endurecimiento recomendado

## 1. Separar `auth freshness` de `auth validity`

La sesión debe tener dos nociones:

- `fresh`: cuándo hice login
- `valid`: si el último response útil confirma que sigo dentro

`IsAuthed` debería dejar de ser criterio único.

## 2. Centralizar stale-session detection en transporte

Agregar en `transport` inspectores por sistema:

- `looksLikeDAULogin(body, resp)`
- `looksLikeSGHLogin(body, resp)`
- `looksLikeLABLogin(body, resp)`
- `looksLikeEmptyTemplate(sys, path, body)`

Luego envolver `Get/Post` así:

1. asegurar login si hace falta
2. hacer request
3. inspeccionar respuesta
4. si parece sesión vencida:
   - re-login una vez
   - repetir request una vez
5. si sigue igual:
   - devolver error explícito de autenticación/sesión degradada

## 3. Convertir “vacío sospechoso” en error fuerte cuando aplique

Ejemplos:

- `cargar_historial_evolucion.php` devolviendo solo template sin filas
- `resultadoseleccion.php` devolviendo formulario
- endpoints DAU devolviendo login form o shell vacío

No siempre debe interpretarse como “no hay datos”. Debe haber heurística por endpoint.

## 4. Decidir explícitamente si habrá persistencia de cookies

Hay dos caminos válidos:

### Opción A: no persistir cookies

Ventajas:

- menos estado oculto
- menos problemas por cookies corruptas o viejas
- más predecible en CLI corta

Costo:

- re-login frecuente

### Opción B: persistir cookies de verdad

Requisitos:

- serialización segura del jar por sistema
- invalidación por expiración
- detección de corrupción
- comando explícito de `logout/clear-session`

Mi lectura: para este CLI, la opción A es mejor salvo que throughput real demuestre dolor fuerte por logins repetidos.

## 5. Agregar `AuthProbe` por sistema

Cada sistema debería tener una lectura barata para verificar sesión:

- DAU: una URL pequeña que delate login vencido
- SGH: una URL mínima que confirme shell autenticado
- LIS: una lectura mínima de formulario protegido

Esto permitiría:

- `h auth-status`
- health checks reales
- reauth anticipado sin ensuciar comandos clínicos

## 6. Modelar “contexto de sesión” para SGH

La sesión SGH no es solo cookie.

Hace falta poder registrar:

- hospital actual
- módulo actual
- último pivote abierto
- CP/ingreso/usuario con que se abrió el flujo

Aunque no se use al principio, conviene dejar la estructura para depurar cambios de contexto.

## Recomendación concreta de implementación

### Fase 1

- mover el retry LIS desde `ctx.go` al transporte
- agregar inspectores de login form para DAU/SGH/LIS
- devolver errores explícitos de sesión degradada

### Fase 2

- agregar detectores endpoint-specific de template vacío sospechoso
- introducir `AuthProbe`
- unificar logging de login, retry, stale-session y relogin

### Fase 3

- decidir persistencia o no persistencia real de cookies
- si se persiste, implementarlo de verdad
- si no, remover la falsa pista de `DataDir/cookies`

## Superficie sugerida

- `h auth status`
- `h auth login dau|sgh|lis`
- `h auth logout`
- `h auth probe dau|sgh|lis`

Y en output de debug de cualquier comando:

- `system`
- `session_fresh`
- `session_validated`
- `relogin_attempted`
- `retry_count`

## Conclusión

La deuda de sesión/cookies no es cosmética. Es estructural.

Hoy el transporte funciona razonablemente para happy path corto, pero no ofrece garantías fuertes contra:

- sesión vencida silenciosa
- respuestas vacías engañosas
- divergencia entre sistemas
- ambigüedad entre login reciente y sesión realmente válida

Si `hsc-cli` va a convertirse en supermercado confiable de ingredientes clínicos, esta capa debe endurecerse antes de ampliar mucho más la superficie V2.
