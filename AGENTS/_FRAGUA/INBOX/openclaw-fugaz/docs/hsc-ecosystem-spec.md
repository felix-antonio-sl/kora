# HSC Ecosystem — Spec integrada desde los sueños del urgencista

Date: 2026-04-02
Status: spec viva derivada del sueño operativo + estado real del producto
Scope: los tres repos del ecosistema clínico HSC

---

## 1. Visión del ecosistema

El operador clínico (Dr. Félix Sanhueza) trabaja turnos de urgencia de 12+ horas con 8-15 pacientes simultáneos en el Hospital de San Carlos. Su flujo real es:

1. Llega a turno → necesita panorama instantáneo
2. Recibe paciente → necesita contexto longitudinal completo en segundos
3. Atiende → dicta hallazgos, necesita documentación telegráfica
4. Sigue labs → necesita diff/trend, no valores aislados
5. Cambia turno → necesita handoff estructurado en 30 segundos, no 30 minutos

El principio rector del ecosistema es:

> **El operador piensa en el paciente. El sistema piensa en los sistemas.**

---

## 2. Arquitectura de tres capas

```
hsc-cli (h)    → manos: acceso atómico a DAU/SGH/LAB
     ↓ datos
hsc-store      → memoria: cache, índice, diff, herramientas
     ↓ datos + estado
hsc-agent      → cerebro: razonamiento, generación, alertas, interpretación
```

### hsc-cli (`/home/felix/projects/hsc-cli`)
Binario Go `h`. JSON-first. Un comando = un dato atómico.
No piensa, no genera, no persiste. Solo lee y escribe contra sistemas hospitalarios.

### hsc-store (`/home/felix/projects/hsc-store`)
SQLite local. Cache, índice de pacientes, estado para diff/alertas, herramientas complementarias (CIE-10, fármacos).
No habla con sistemas hospitalarios directamente — se alimenta del CLI.

### hsc-agent (`/home/felix/projects/hsc-agent`)
Agente OpenClaw. Razonamiento clínico, generación de documentos, interpretación de imágenes, alertas proactivas, búsqueda semántica, voz.
Consume datos del CLI y del store. Actúa a través del CLI para escritura.

---

## 3. Spec del CLI (`hsc-cli`) — actualizada con sueños

La spec canónica vigente está en `/home/felix/projects/hsc-cli/docs/product-spec.md`.
Lo siguiente integra los gaps identificados desde el sueño del urgencista.

### 3.1 Gaps confirmados que el CLI debe cerrar

#### 3.1.1 Paciente sin episodio activo
Hoy `h ctx` depende de tener un `atencion_id` DAU activo. Cuando el paciente no tiene episodio urgencia activo (ej: consulta HODOM, paciente hospitalizado, paciente externo), el comando pierde mucho poder.

**Necesidad**: un modo que funcione puramente desde SGH + LIS cuando no hay DAU activo. Puede ser `h ctx --longitudinal` o un comando separado `h patient`.

**Estructura JSON objetivo** (del sueño):
```json
{
  "identidad": {},
  "alergias": [],
  "hospitalizaciones": [],
  "urgencias_previas": [],
  "ultima_epicrisis": {},
  "ultimas_evoluciones": [],
  "medicacion_activa": [],
  "ultimo_lab": {},
  "en_curso": {}
}
```

#### 3.1.2 Búsqueda por nombre
`h who` acepta RUT y atencion_id pero no nombre. Necesita aceptar nombre parcial como input y manejar múltiples resultados.

#### 3.1.3 Labs inteligentes en el CLI
Hoy `h lis` y `h lis-detail` existen pero son atómicos. El CLI necesita:
- `--altered` para filtrar solo alterados
- `--since` para filtrar por fecha
- `--last` para último panel solamente

El diff/trend/watch son más apropiados para hsc-store, pero el CLI podría exponerlos si el store existe.

#### 3.1.4 Buscador CIE-10
No existe. Endpoint `buscar_cie10` existe en arqueología. Implementación directa, blast radius bajo, valor alto. Cada alta requiere CIE-10.

#### 3.1.5 SGH más granular
- Recetas como comando dedicado (hoy solo sale dentro de `hx --deep`)
- `--last N` en evoluciones
- `--servicio` como filtro en camas
- `--active` en hospitalizaciones

#### 3.1.6 Medicación longitudinal
No existe como concepto unificado. Las fuentes están dispersas:
- `h rx` → meds del episodio DAU activo
- recetas SGH → dentro de enrichment
- APS → launcher roto

Necesita un comando que cruce todas las fuentes disponibles.

#### 3.1.7 Compilación de materia prima para documentos
`h ctx --deep` compila parcialmente. Falta un modo explícito orientado a "dame todo lo que necesito para escribir una epicrisis/alta/IC de este paciente", consolidado y ordenado.

#### 3.1.8 Output universal
Hoy solo JSON. El sueño pide:
- `--text`: texto plano telegráfico (para pegar en DAU/Telegram)
- `--table`: tabla ASCII
- `--brief`: una línea

Implementable como capa en `internal/output`.

#### 3.1.9 DAU read consolidado
Un `h dau read <cod_atencion>` que devuelva todos los campos de la atención en un solo JSON (anamnesis, EF, hipótesis, obs, indicaciones, CIE-10, SV). Hoy eso requiere llamar 6 comandos.

### 3.2 Lo que el CLI ya cubre bien del sueño

| Sección del sueño | Cobertura |
|---|---|
| Auth invisible | 90% |
| Identidad por RUT | 85% |
| DAU turno (box, cola, triage) | 95% |
| DAU lectura individual | 90% |
| DAU escritura con guardrails | 90% |
| SGH hospitalizaciones/evoluciones | 80% |
| Handoff generación | 70% |
| Documentos hospitalarios (epi, ing, alt) | 90% |
| DAU históricos | 95% |
| Documentos OSIRIS ambulatorios | 95% (nuevo) |

---

## 4. Spec del store (`hsc-store`) — desde los sueños

Documento de ideas detallado en `/home/felix/projects/hsc-store/IDEAS.md`.

### 4.1 Capacidades core

#### Cache con TTL
- Demográficos: 24h
- Antecedentes: 1h
- Labs: 15min
- SV/episodio: 2min o sin cache
- Flag `--fresh` para bypass

#### Lab diff / trend / watch
La feature más pedida del sueño que no existe en ninguna parte:
- **diff**: comparación entre paneles → delta con flechas
- **trend**: serie temporal de un parámetro
- **watch**: filtrar solo keys de interés

#### Índice de pacientes atendidos
Cada interacción con un paciente se indexa automáticamente. Búsqueda por nombre/RUT/fecha.

#### Buscador CIE-10 local
~14,000 códigos en SQLite. Búsqueda por texto libre o código.

#### Base de fármacos de emergencia
Fichas técnicas de preparación/dilución/infusión para fármacos de emergencia frecuentes.

#### Estado previo para alertas
Tabla que registra último valor conocido de parámetros clínicos por paciente, para que el motor de alertas del agente pueda comparar.

#### Modo offline
Sync explícito de datos críticos. Fallback a cache cuando no hay red. Indicador de freshness.

### 4.2 Priorización
1. Cache con TTL (impacto inmediato en performance)
2. Lab diff/trend (impacto clínico directo)
3. CIE-10 buscador (impacto en cada alta)

---

## 5. Spec del agente (`hsc-agent`) — desde los sueños

Documento de ideas detallado en `/home/felix/projects/hsc-agent/IDEAS.md`.

### 5.1 Capacidades core

#### Dashboard de inicio de turno
Un trigger que compone: box + cola priorizada + HODOM + alertas.
Consume múltiples comandos del CLI, enriquece con reglas clínicas, formatea para Telegram.

#### Alertas proactivas
Motor de reglas clínicas (14 combinaciones ya diseñadas) evaluado periódicamente via polling del CLI.
Notifica por OpenClaw cuando algo requiere atención sin que el operador pregunte.

#### Generación de documentos clínicos
Templates para: alta, epicrisis, IC, ingreso, contrarreferencia.
El CLI compila materia prima. El agente genera texto clínico telegráfico. El operador revisa y aprueba.

#### Handoff assume
Brief instantáneo de cada paciente heredado al recibir turno. Composición multi-comando del CLI.

#### Interpretación de imágenes con contexto
Imagen (ECG/Rx/TAC) + contexto del paciente via CLI → modelo de visión → hallazgos correlacionados.

#### Voz y dictado
Audio → STT → texto clínico telegráfico → `h w nota`. Elimina un paso completo del flujo.

#### Contexto cruzado con memoria
Búsqueda que cruza SGH/DAU (CLI) + archivos locales + sesiones previas + memoria OpenClaw.

#### Búsqueda clínica transversal
Queries semánticas sobre la base de pacientes/episodios del store.

### 5.2 Priorización
1. Dashboard de inicio de turno (30 segundos para arrancar)
2. Generación de documentos (80% del tiempo del agente)
3. Handoff assume (momento de mayor riesgo)

---

## 6. Frontera entre capas

### Principio de separación
- Si la operación es **un request HTTP contra un sistema hospitalario** → CLI
- Si la operación requiere **comparar con estado previo o persistir** → Store
- Si la operación requiere **razonar, generar texto, o decidir** → Agente

### Ejemplos concretos

| Operación | Capa |
|---|---|
| Leer labs del episodio | CLI |
| Comparar labs de hoy vs ayer | Store (diff) |
| Alertar que el potasio subió a 6.5 | Agente (regla + notificación) |
| Extraer epicrisis PDF | CLI |
| Ordenar todas las epicrisis cronológicamente | Store (o CLI con store) |
| Generar borrador de epicrisis de egreso | Agente |
| Escribir nota en DAU | CLI |
| Decidir si la nota está lista para escribir | Agente |
| Transcribir audio de dictado | Agente |
| Buscar CIE-10 por texto | Store |
| Interpretar ECG con contexto clínico | Agente |

### Flujo de escritura (siempre)
```
Agente genera borrador → operador revisa → operador confirma → CLI escribe
```
Nunca se salta al operador.

---

## 7. Relación con specs previas

### product-spec.md (CLI)
Sigue vigente como spec canónica del binario `h`. Esta spec de ecosistema la **extiende** con los gaps del sueño y la sitúa en el contexto de las tres capas.

### write-guardrails.md
Sigue vigente. Aplica al CLI y al agente: la política de escritura no cambia por agregar capas.

### endpoint-priority-matrix.md
Sigue vigente como mapa de endpoints. Los gaps funcionales del sueño (CIE-10, medicación longitudinal, etc.) se pueden agregar como filas nuevas.

### Arqueología (historias usuario v2, primer, aterrizaje)
Siguen siendo referencia histórica. Muchas de las historias de usuario del sueño del urgencista son evolución natural de las 48 historias originales. La continuidad es real.

---

## 8. Qué no es parte de este ecosistema

- UI web o app móvil (existió `urgencista-app` en arqueología, hoy no es prioridad)
- Base de datos hospitalaria directa (MySQL no accesible, todo es via web scraping)
- Multi-usuario o multi-hospital (producto para un operador en un hospital)
- Reemplazo del sistema institucional (complemento, no sustituto)

---

## 9. Resumen ejecutivo

El ecosistema HSC tiene tres capas con responsabilidades claras:

**CLI** = acceso atómico, ya sólido (~75% del sueño que le compete), gaps cerrables.

**Store** = persistencia y herramientas, no existe aún, prioridades claras: cache, lab diff, CIE-10.

**Agente** = inteligencia clínica, no existe como producto separado, prioridades claras: dashboard, generación de docs, handoff assume.

El sueño del urgencista se cubre **~60-70% con lo que existe hoy** si contamos solo el CLI. Con las tres capas implementadas, la cobertura sería **~90%+**.

Lo que falta no es misterio. Es ingeniería con dirección clara.
