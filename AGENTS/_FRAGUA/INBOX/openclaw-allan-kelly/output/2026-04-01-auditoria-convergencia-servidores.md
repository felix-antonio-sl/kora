# Auditoría de convergencia de proyectos y recomendación de concentración en servidor de 3ª generación

Fecha: 2026-04-01
Autor: Allan Kelly

## Propósito

Evaluar el portafolio distribuido entre:
- servidor BPS remoto (`clawdbot@157.180.121.173:/home/clawdbot/projects`)
- servidor actual/local de 3ª generación (`/home/felix/projects`)

para decidir cómo **concentrar y converger en un solo servidor**, asumiendo como destino operativo preferente el servidor donde ya vive la 3ª generación de agentes y donde deben quedar los proyectos en desarrollo.

> Nota de genealogía: la memoria operativa disponible clasifica `157.180.121.173` como host legacy de 1ª generación (`clawdbot-hetzner`), no 2ª. La 2ª generación `kora` figura en `138.201.53.205` como deprecada. Source: `MEMORY.md#L1-L42`

---

## Decisión propuesta

### Decisión principal

**Sí: concentrar el desarrollo activo en el servidor de 3ª generación.**

### Traducción operativa

- El servidor remoto BPS debe pasar de ser **superficie de desarrollo viva** a ser **fuente de legado, referencia y extracción controlada**.
- El servidor de 3ª generación debe convertirse en la **única superficie canónica de proyectos en desarrollo**.
- Ningún proyecto debe seguir viviendo en dos lugares como “semiactivo” sin una decisión explícita de migración o archivo.

### Razón

Hoy hay una mezcla de:
- capacidades útiles aún vivas en el BPS,
- proyectos estratégicos reconstruidos en el servidor actual,
- y líneas donde el linaje existe pero la absorción todavía no se ha cerrado.

El coste real ya no es solo infraestructura duplicada. Es **ambigüedad de ownership, drift de conocimiento y pago doble de mantenimiento cognitivo**.

---

## Inventario comparado

### Servidor remoto BPS

Proyectos detectados:
- `air-bridge`
- `dashboard-korax`
- `downloads-scout`
- `hodom`
- `hsc-clinical`
- `kora`
- `korax-briefing`
- `leychile-sdk`
- `opcloud-oss`
- `sgh-tools`
- `urgencista-app`

### Servidor actual / 3ª generación

Proyectos detectados:
- `docker-stacks`
- `hdos`
- `hsc-cli`
- `kora-panel`
- `opcloud-reports`
- `openclaw`
- `opmodel`
- `pca`

---

## Lectura estratégica

## Qué representa el BPS remoto

No es solo “legacy”. Contiene cuatro tipos de activos:

1. **Utilitarios operativos pequeños pero valiosos**
   - `air-bridge`
   - `downloads-scout`
   - `korax-briefing`

2. **Repositorios de aprendizaje duro del dominio clínico**
   - `hsc-clinical`
   - `sgh-tools`
   - `urgencista-app`

3. **Marcos de intención / programa de dominio**
   - `hodom`
   - `kora`
   - `opcloud-oss`

4. **Vestigios o líneas laterales**
   - `dashboard-korax`

## Qué representa el servidor actual

Contiene menos proyectos, pero con más peso de plataforma:
- `openclaw`
- `opmodel`
- `hsc-cli`
- `pca`
- `hdos`
- `docker-stacks`

Es decir: menos utilitarios sueltos y más núcleos de producto o infraestructura.

---

## Auditoría por proyecto remoto

## 1. air-bridge

### Propósito real
Sincroniza `INBOX.md` del VPS hacia Obsidian en Mac vía nodo `air`.

### Estado observable
- README claro
- propósito único
- superficie pequeña
- cronizable

### Valor
**Alto valor operativo personal.** Resuelve una fricción concreta de captura y traspaso.

### Relación con 3ª generación
No tiene reemplazo explícito como proyecto. Su capacidad podría vivir mejor dentro de OpenClaw + cron + nodes.

### Decisión sugerida
**Absorber como capacidad, no mantener como proyecto estratégico independiente.**

### Acción
- migrar lógica útil al servidor de 3ª generación
- dejar el repo remoto solo como referencia temporal hasta validar reemplazo

---

## 2. downloads-scout

### Propósito real
Monitorea una carpeta de descargas en el Mac y captura archivos nuevos al `INBOX.md` del VPS.

### Estado observable
- README claro
- ciclo funcional concreto
- utilidad puntual

### Valor
**Alto valor GTD / ingestión personal.**

### Relación con 3ª generación
No tiene reemplazo claro actual, pero conceptualmente encaja como capacidad de nodes + cron.

### Decisión sugerida
**Absorber como capability operativa en 3ª generación.**

### Acción
- portar al servidor actual si la capacidad sigue siendo útil
- no dejarlo como isla eterna en BPS

---

## 3. korax-briefing

### Propósito real
Generador de brief matutino GTD a Telegram.

### Estado observable
- simple
- cronizable
- claro

### Valor
**Medio-alto**, por utilidad diaria y síntesis operacional.

### Relación con 3ª generación
Puede y probablemente debe migrar a cron/agente en OpenClaw actual.

### Decisión sugerida
**Migrar como job/capability, no como proyecto central.**

---

## 4. hodom

### Propósito real
Programa de transformación de la unidad HODOM-HSC:
- normativa
- diagnóstico
- diseño target
- implementación
- KPIs

### Estado observable
Más programa/documentación que software. Está en Fase 1.

### Valor
**Muy alto valor de dominio e intención.**

### Relación con 3ª generación
Se reparte conceptualmente entre:
- `hdos` — demo/prototipo operativo
- `opmodel` — modelamiento del sistema real HODOM HSC
- `hsc-cli` — tooling clínico longitudinal posible

### Riesgo
Perder el repo `hodom` no rompe software, pero sí rompe el **marco de intención y trazabilidad del programa**.

### Decisión sugerida
**Migrar o reflejar como corpus de referencia viva dentro del entorno de 3ª generación.**

### Acción
- no tratarlo como software a “ejecutar”
- tratarlo como base de contexto y programa director del dominio

---

## 5. hsc-clinical

### Propósito real
Acceso clínico Python a DAU/SGH/labs/documentos/historia.

### Estado observable
- actividad reciente
- 19 tests visibles
- pyproject claro
- mucho aprendizaje acumulado
- dependiente de entorno remoto no completamente preparado (`pytest` no disponible en host base)

### Valor
**Altísimo como activo de conocimiento y oráculo de migración.**

### Relación con 3ª generación
Linaje directo con:
- `hsc-cli/arqueologia/cli-hsc/hsc-clinical`
- `hsc-cli` (Go) como sucesor estratégico

### Juicio
No es el futuro como producto principal, pero sí una fuente crítica del pasado reciente.

### Decisión sugerida
**Congelar como repo de referencia / oracle, no como superficie principal.**

### Acción
- mantenerlo accesible
- no seguir desarrollando allí salvo fixes de preservación extrema
- usarlo para certificar paridad en migraciones hacia `hsc-cli`

---

## 6. kora

### Propósito real
Monorepo doctrinal y operacional con specs, knowledge, agents, toolchain, schemas y tests.

### Estado observable
- repo grande y vivo
- 185 tests via `unittest`
- 184 pasan, 1 falla
- alto peso normativo

### Valor
**Muy alto valor epistemológico y estructural.**

### Riesgo
Quedar como sistema madre doctrinal sin loop closure suficiente con la generación actual.

### Relación con 3ª generación
No tiene reemplazo 1:1. Su descendencia doctrinal parece distribuida entre:
- workspaces OpenClaw
- memoria operativa
- skills
- agentes actuales

### Decisión sugerida
**No migrarlo por reflejo como “otro proyecto en desarrollo”, sino decidir si queda como repositorio de referencia o si se absorbe selectivamente.**

### Acción
- evitar una migración mecánica completa sin objetivo
- extraer lo que todavía gobierna decisiones reales
- archivar con claridad lo que ya no manda

---

## 7. leychile-sdk

### Propósito real
SDK Python para Ley Chile.

### Estado observable
- README sólido
- tests presentes
- propósito claro
- producto bien delimitado

### Valor
**Alto valor específico.** Es de los proyectos más nítidos del BPS.

### Relación con 3ª generación
No tiene equivalente local directo.

### Decisión sugerida
**Migrar íntegro al servidor de 3ª generación si sigue siendo parte del portafolio activo.**

### Acción
- mantenerlo como proyecto independiente si sigue teniendo uso real
- si no, archivarlo con dignidad, pero no dejarlo huérfano en BPS por inercia

---

## 8. opcloud-oss

### Propósito real
Spec de ingeniería inversa de OPCloud y propuesta de clon open-source.

### Estado observable
Artefacto de spec, no producto.

### Relación con 3ª generación
Muy vinculado a `opmodel`.

### Decisión sugerida
**No migrar como proyecto vivo. Absorber como referencia histórica/conceptual de `opmodel`.**

---

## 9. sgh-tools

### Propósito real
Tooling shell / bootstrap táctico para sistemas clínicos HSC.

### Estado observable
Pequeño, táctico, precursor.

### Relación con 3ª generación
Ancestro funcional de `hsc-clinical` y `hsc-cli`.

### Decisión sugerida
**Archivo de referencia, no línea de producto.**

---

## 10. urgencista-app

### Propósito real
App clínica Next.js.

### Estado observable
- package moderno
- commits recientes
- propósito opaco por README genérico

### Valor
Potencial, pero hoy poco visible desde fuera.

### Relación con 3ª generación
Sin equivalente top-level actual, pero relacionada conceptualmente con tooling clínico asistido.

### Decisión sugerida
**Exigir decisión explícita: migrar y clarificar propósito, o archivar.**

---

## 11. dashboard-korax

### Propósito real
Dashboard Flask + alertas Telegram.

### Estado observable
Marcado como archived.

### Relación con 3ª generación
Parentesco funcional probable con `kora-panel`.

### Decisión sugerida
**Dejar archivado.**

---

## Auditoría de proyectos actuales / 3ª generación

## 1. openclaw

### Estado
Proyecto más maduro y central.

### Valor
Máximo. Plataforma principal.

### Rol en convergencia
Debe ser el **ancla** de la concentración.

---

## 2. opmodel

### Estado
Motor potente con valor real, pero baseline aún no cerrada.

### Valor
Muy alto.

### Rol en convergencia
Debe absorber o referenciar explícitamente activos de modelamiento hoy dispersos (`opcloud-oss`, parte de `hodom`).

---

## 3. hsc-cli

### Estado
Proyecto estratégico en Go para CLI clínico. Alto valor potencial, consumibilidad aún por cerrar.

### Rol en convergencia
Es el **sucesor directo** de la línea clínica dispersa del BPS:
- `hsc-clinical`
- `sgh-tools`
- parte de `urgencista-app`

### Condición
No debe convivir indefinidamente con desarrollo semiactivo en el Python anterior.

---

## 4. hdos

### Estado
Demo funcional. Build local observado OK.

### Rol en convergencia
Representa la materialización UX/demo del programa `hodom`.

### Riesgo
Inflarse como demo brillante sin cierre operacional.

---

## 5. pca

### Estado
Proyecto pequeño y sano. 98 tests observados en verde.

### Rol en convergencia
No parece depender del legado BPS. Puede quedarse como proyecto independiente bien contenido.

---

## 6. docker-stacks

### Estado
Infraestructura operativa útil.

### Rol en convergencia
Soporte de despliegue, no producto.

---

## 7. kora-panel

### Estado
Temprano, sin cierre observable suficiente.

### Relación
Puede ser heredero funcional parcial de `dashboard-korax`.

### Decisión sugerida
Exigir prueba de valor antes de seguir construyendo.

---

## 8. opcloud-reports

### Estado
Artefacto puntual, no producto.

### Decisión sugerida
No tratar como proyecto estratégico.

---

## Mapa de convergencia

### Capacidades del BPS que deben converger al servidor de 3ª generación

#### Absorber como capability operativa
- `air-bridge`
- `downloads-scout`
- `korax-briefing`

#### Migrar como conocimiento/oráculo de transición
- `hsc-clinical`
- `sgh-tools`
- `hodom`
- `opcloud-oss`

#### Migrar como proyecto si sigue activo
- `leychile-sdk`

#### Exigir decisión explícita
- `urgencista-app`

#### Archivar definitivamente
- `dashboard-korax`

---

## Riesgos de no converger

1. **Drift de conocimiento**
   - el contexto relevante sigue repartido entre hosts

2. **Duplicación semántica**
   - dos repos para una misma capacidad o linaje

3. **Ambigüedad de ownership**
   - no queda claro cuál es la superficie canónica

4. **Pago cognitivo doble**
   - mantener localización mental del portfolio distribuido

5. **Falsos activos vivos**
   - proyectos que parecen activos solo porque siguen existiendo en el BPS

---

## Criterio de convergencia

Para cada repo del BPS, aplicar solo una de estas salidas:

- **MIGRAR** → proyecto seguirá vivo en 3ª generación
- **ABSORBER** → deja de existir como repo protagonista y pasa a capability interna
- **CONGELAR** → queda como oracle / referencia histórica de migración
- **ARCHIVAR** → se declara cerrado

Regla: **ningún repo queda en estado “semi-vivo” en dos hosts**.

---

## Recomendación final por proyecto remoto

| Proyecto BPS | Decisión | Destino en 3ª generación | Prioridad |
|---|---|---|---|
| air-bridge | ABSORBER | OpenClaw cron/nodes/capability | Alta |
| downloads-scout | ABSORBER | OpenClaw cron/nodes/capability | Alta |
| korax-briefing | ABSORBER | OpenClaw cron/job de briefing | Media |
| hodom | CONGELAR + REFERENCIAR | corpus de dominio para `hdos`/`opmodel`/`hsc-cli` | Alta |
| hsc-clinical | CONGELAR como oracle | referencia para `hsc-cli` | Muy alta |
| kora | DECISIÓN ESTRATÉGICA EXPLÍCITA | extraer/absorber selectivamente | Muy alta |
| leychile-sdk | MIGRAR o ARCHIVAR | proyecto independiente si sigue activo | Media-alta |
| opcloud-oss | CONGELAR | referencia de `opmodel` | Media |
| sgh-tools | ARCHIVAR como ancestro | referencia menor para `hsc-cli` | Media |
| urgencista-app | DECIDIR | migrar con propósito claro o archivar | Alta |
| dashboard-korax | ARCHIVAR | ninguno | Baja |

---

## Plan incremental de convergencia

## Lote 1 — cerrar superficies canónicas

Objetivo: decidir de manera explícita qué vive en 3ª generación.

1. Declarar el servidor de 3ª generación como **único locus de desarrollo activo**.
2. Marcar el BPS como **legado / referencia / extracción**.
3. Etiquetar cada repo remoto con una salida: migrar / absorber / congelar / archivar.

## Lote 2 — migrar capacidades pequeñas y útiles

1. `air-bridge`
2. `downloads-scout`
3. `korax-briefing`

Éxito: esas capacidades ya operan desde el stack actual o quedan descartadas explícitamente.

## Lote 3 — cerrar el linaje clínico

1. `hsc-clinical` queda formalmente como oracle, no como superficie principal.
2. `hsc-cli` queda reconocido como sucesor único.
3. `sgh-tools` pasa a archivo.
4. decidir destino de `urgencista-app`.

## Lote 4 — cerrar el linaje de modelamiento/HODOM

1. `hodom` queda como corpus de intención y dominio.
2. `opmodel` absorbe el modelamiento real.
3. `hdos` queda claramente delimitado como demo/prototipo o se recalibra.
4. `opcloud-oss` pasa a referencia histórica.

## Lote 5 — decidir KORA

Este lote no debe hacerse por inercia.

Preguntas de decisión:
- ¿Qué parte de `kora` sigue gobernando decisiones reales hoy?
- ¿Qué parte ya fue absorbida por OpenClaw/workspaces/skills?
- ¿Qué parte puede archivarse sin pérdida de capacidad?

---

## Juicio final

La convergencia en un solo servidor **sí es la dirección correcta**.

Pero el objetivo no es copiar carpetas.
El objetivo es:
- **concentrar desarrollo activo**,
- **cerrar superficies canónicas**,
- **reducir duplicación semántica**,
- **y podar el legado sin perder sus aprendizajes**.

Compresión doctrinal:

> El BPS no debe seguir siendo un segundo cerebro operativo. Debe pasar a ser, en el mejor de los casos, una cantera de legado bien clasificado. El servidor de 3ª generación debe ser el único lugar donde el futuro del sistema se escribe.
