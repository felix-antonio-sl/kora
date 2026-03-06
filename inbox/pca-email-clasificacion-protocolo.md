# Protocolo de Clasificación Prospectiva de Email para PCA v3.0

**Autor:** Claude Opus 4.6, en colaboración con Korvo
**Fecha:** 2026-02-27
**Estado:** Propuesta — pendiente revisión y triaje
**Contexto:** Sesión de diseño Claude Code, análisis profundo de PCA v3.0 + FSM Korax + arquitectura OpenClaw

---

## 1. El problema

Korax recibe todos los correos de todas las cuentas de Korvo:

| Cuenta | Dominio | Naturaleza |
|---|---|---|
| felixsanhuezaluna@gmail.com | Personal principal | Vida, finanzas, suscripciones, familia |
| felixsanhueza@me.com | iCloud | Redundante/legacy, notificaciones Apple |
| felix.sanhueza@goredenuble.cl | GORE Ñuble | Institucional, regulatorio, coordinación |

Las tres reenvían a `koraxfx@gmail.com`. El pipeline actual es un pass-through ciego:

```
Gmail → GCP Pub/Sub → gog-gmail-watch → /hooks/gmail → haiku → Telegram
```

Cada email genera una notificación idéntica: emoji genérico, remitente, asunto, snippet. Sin clasificación, sin filtrado, sin scoring. Un email de Contraloría con plazo de 48 horas tiene el mismo peso visual que una newsletter de LinkedIn.

**Esto viola P1 directamente.** La atención de Korvo — el recurso soberano del PCA — se fragmenta en evaluar cada notificación manualmente. El sistema que debería proteger la atención la está erosionando.

### 1.1 Dimensión del problema

Estimación conservadora del volumen diario:

- 5-10 emails institucionales (@goredenuble.cl, reguladores, SUBDERE, DIPRES)
- 5-15 emails personales (servicios, notificaciones, familia)
- 10-30 emails de ruido (newsletters, marketing, noreply, GitHub notifications)

Total: ~20-55 emails/día. De estos, quizás 3-5 requieren acción real. El ratio señal/ruido es ~10%. Korvo está gastando atención en el 90% que no importa.

### 1.2 Lo que NO es el problema

No es un problema de spam. Gmail ya filtra el spam duro. El problema es el **ruido legítimo**: emails que no son spam pero tampoco requieren la atención del operador. Newsletters que sí se suscribió, notificaciones de servicios que sí usa, CCs institucionales donde no es el destinatario primario.

---

## 2. Visión: El email como flujo atencional, no como bandeja

### 2.1 Cambio de paradigma

El email no debería ser una lista plana de mensajes esperando evaluación humana. Debería ser un **flujo atencional clasificado** donde:

1. Lo urgente interrumpe (con justificación)
2. Lo relevante espera su momento (agrupado por dominio y modo energético)
3. Lo irrelevante se archiva en silencio (con opción de auditoría)

Esto es exactamente lo que el PCA v3.0 ya hace con las capturas GTD — pero el email quedó fuera del sistema. Este protocolo cierra esa brecha.

### 2.2 Principio rector: Subsidiariedad progresiva

Korax opera bajo el principio de subsidiariedad (A2 de SOUL.md): actúa solo donde el operador no puede o no debería gastar atención. La clasificación de email es el caso perfecto para subsidiariedad:

- **Día 1:** Korax clasifica y presenta. Korvo decide.
- **Día 30:** Korax clasifica con patrones aprendidos del feedback de Korvo. Las decisiones del operador informan las del agente.
- **Día 90:** Con delegación explícita (`/delegar triage`), Korax puede archivar ruido y pre-clasificar automáticamente, reportando sus decisiones en el próximo contacto.
- **Día 180:** El clasificador es una extensión calibrada del juicio de Korvo. Las correcciones son raras. El sistema desaparece.

Este es el arco de maduración: de herramienta a exoesqueleto. No es automatización — es cognición distribuida.

### 2.3 Alineación con los 4 principios del PCA

| Principio | Cómo se alinea | Riesgo si no se alinea |
|---|---|---|
| **P1** (Atención soberana) | Reduce evaluación manual de 55 emails a 3-5 relevantes. El ruido se silencia o compacta. | Si la clasificación es mala, genera doble trabajo: leer la notificación + verificar si es correcta |
| **P2** (Separar captura de triaje) | La clasificación de email ocurre en Tier 1 (hook, automático). La decisión de capturar al GTD ocurre solo si el operador lo solicita en CM-CLOSE | Si la clasificación captura automáticamente al GTD, mezcla captura con triaje |
| **P3** (Navegar por energía) | Cada email clasificado lleva dominio (@trabajo, @hospital, @digital, @casa) y modo implícito (DEEP/SHALLOW). En S_PLAN, Korax puede decir "hay 2 emails @trabajo que requieren bloque SHALLOW de 15 min" | Si no lleva dominio, el operador no puede filtrar por energía disponible |
| **P4** (Empezar simple) | Tier 1 es una modificación de messageTemplate (0 código nuevo). Tier 2 es un paso adicional en CM-CLOSE. No hay nuevo estado FSM | Si arrancamos con Lobster pipelines, transform modules, y cron dedicados, la complejidad mata la adopción |

---

## 3. Arquitectura de 3 tiers

### 3.1 Visión general

```
TIER 1 — Instant (hook, cada email)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gmail → Pub/Sub → gog-watch → /hooks/gmail
                                  │
                                  ▼
                          haiku + instrucciones de clasificación
                          (messageTemplate mejorado)
                                  │
                                  ▼
                          Telegram: notificación con tag
                          🔴 @trabajo | Contraloría
                          Plazo informe: 48h
                          → Responder

                          🗑️ newsletter@medium.com — Weekly Digest


TIER 2 — Batch (CM-CLOSE, 21:00)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
heartbeat_evening → S_CLOSE → CM-CLOSE (paso 2b)
                                  │
                                  ▼
                          gog gmail search "in:inbox is:unread after:{today}"
                          + memory_search("email-patterns.md")
                                  │
                                  ▼
                          Resumen: "12 emails hoy. 2 urgentes sin atender.
                          ¿Capturar al GTD?"


TIER 3 — Learning (continuo, sesión main)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feedback explícito ("ese era basura")     ─┐
Feedback captura (email → /inbox)          ├──→ email-patterns.md
Feedback ignorado (sin acción en 48h)      │    (indexado por memory search)
Feedback respondido (operador respondió)  ─┘
          │
          ▼
   Patrón con confianza alta (≥3 ocurrencias)
          │
          ▼
   Promover a regla determinística
   (sección 1 o 2 de email-patterns.md)
          │
          ▼
   Incorporar al messageTemplate de Tier 1
   (próxima iteración del protocolo)
```

### 3.2 Tier 1: Clasificación instantánea en el hook

**Mecanismo:** Modificar el `messageTemplate` del mapping gmail en `openclaw.json`. El hook ya corre un agent turn con haiku — solo necesitamos darle mejores instrucciones.

**Qué cambia:**

Antes:
```
📧 Nuevo email de John Doe <john@example.com>
Asunto: Meeting tomorrow

Hey, just wanted to confirm...
```

Después:
```
🟡 @trabajo | John Doe <john@goredenuble.cl>
Meeting tomorrow
→ Responder
```

O para ruido:
```
🗑️ newsletter@medium.com — Your Weekly Digest
```

**Dimensiones de clasificación:**

| Dimensión | Valores | Señal visual |
|---|---|---|
| Urgencia | immediate / today / this_week / someday / noise | 🔴 🟡 🔵 ⚪ 🗑️ |
| Dominio | @trabajo / @hospital / @digital / @casa | Tag texto |
| Acción sugerida | Responder / Leer / Capturar GTD / Archivar | Flecha → |
| Relevancia | high / medium / low | Implícita en el formato (compacto para low) |

**Reglas hardcodeadas en el template (Tier 0 determinístico):**

```
GORE Ñuble (*@goredenuble.cl) → 🟡 @trabajo
Contraloría (*@contraloria.cl) → 🔴 @trabajo
MINSAL (*@minsal.cl) → 🟡 @hospital
Hospital San Carlos (*@hospitalsc.cl) → 🟡 @hospital
DIPRES, SUBDERE → 🔵 @trabajo
noreply@, no-reply@, newsletter, marketing → 🗑️
LinkedIn, Medium, GitHub notifications → 🗑️
```

Estas reglas se evalúan por haiku como parte de su razonamiento. No son código — son instrucciones en lenguaje natural dentro del template. Haiku las sigue con alta fidelidad para patrones explícitos.

**Costo:** Cero adicional. Haiku ya corre en cada email. Solo cambia el prompt.

### 3.3 Tier 2: Revisión batch en CM-CLOSE

**Mecanismo:** Nuevo paso 2b en CM-CLOSE.md, invocando CM-EMAIL-CLASIFICADOR como sub-procedimiento.

**Qué hace:**

1. Lee emails no leídos del día vía `gog gmail search`
2. Consulta email-patterns.md vía memory search para patrones conocidos
3. Presenta resumen compacto:

```
🌙 Cierre del día.
📧 Emails: 23 total | 🔴 1 | 🟡 3 | 🔵 5 | ⚪ 4 | 🗑️ 10
⚠️ 1 urgente sin atender:
  - Contraloría: Plazo informe ERD (vence mañana)
¿Capturar al GTD?
```

4. Si el operador quiere capturar → usa `/inbox` (sin metadatos, INV-06)
5. Si el operador corrige una clasificación → registra feedback

**Ventaja sobre Tier 1:** CM-CLOSE corre en la sesión main, que SÍ tiene acceso a memory search y al corpus de patrones. Puede hacer clasificación más sofisticada que haiku en el hook aislado.

**Duración:** <2 minutos. Si no hay urgentes, una línea de resumen y continúa el cierre.

### 3.4 Tier 3: Aprendizaje prospectivo

Este es el corazón del sistema. La clasificación no es estática — evoluciona con cada interacción.

**Corpus: `email-patterns.md`**

Archivo de conocimiento en `docs/activa/` (indexado automáticamente por memory search vía `extraPaths`). Estructura:

```
Sección 1: Reglas de dominio (determinísticas, alta confianza)
  → Tabla: patrón remitente → dominio + urgencia default

Sección 2: Reglas de ruido (determinísticas, alta confianza)
  → Tabla: patrón → tipo → acción

Sección 3: Patrones aprendidos (del feedback del operador)
  → Tabla: fecha | patrón | clasificación anterior → correcta | tipo feedback | confianza

Sección 4: Heurísticas de contenido
  → Keywords que modifican urgencia/relevancia

Sección 5: Métricas de rendimiento
  → Accuracy estimada, falsos positivos/negativos por período
```

**4 canales de feedback:**

| Canal | Señal | Confianza | Mecanismo |
|---|---|---|---|
| Explícito | Operador corrige: "ese era basura" | Alta | Korax en sesión main registra corrección en sección 3 |
| Captura | Email capturado al GTD vía /inbox | Media | Si el /inbox menciona un email reciente, inferir relevancia |
| Ignorado | Email notificado, sin acción en 48h | Baja | CM-CLOSE detecta en micro-check del día siguiente |
| Respondido | Operador respondió al email | Media | Detectable por gog gmail si el thread tiene respuesta saliente |

**Ciclo de maduración de un patrón:**

```
Día 1:  Email de X clasificado como 🔵 (this_week)
Día 1:  Korvo dice "eso es ruido"
        → Registro: X | 🔵 → 🗑️ | explícito | media (1 ocurrencia)

Día 5:  Otro email de X, clasificado como 🔵 (Tier 1 no sabe aún)
Día 5:  CM-CLOSE consulta patterns → encuentra corrección previa
        → Presenta como 🗑️ en el resumen batch (Tier 2 corregido)

Día 12: Tercer email de X, Korvo no reacciona (ignorado)
        → Registro: X | _ → 🗑️ | ignorado | baja
        → Confianza acumulada: 2 explícito/captura + 1 implícito = alta

Día 13: Patrón promovido a Sección 2 (ruido determinístico)
        → En próxima iteración del messageTemplate, X se incluye como ruido
        → Tier 1 ahora clasifica X como 🗑️ sin necesitar Tier 2
```

**Esto es lo que significa "prospectivamente mejorando":** cada interacción de Korvo con el email —incluso la no-interacción— es una señal de entrenamiento. El sistema no necesita un pipeline de ML. Necesita un corpus estructurado, una heurística de confianza, y un ciclo de promoción.

---

## 4. Integración con la FSM de Korax

### 4.1 Decisión: No crear nuevo estado

La FSM de Korax tiene 13 estados y 49 transiciones. Agregar S_EMAIL_TRIAGE requeriría:
- Un nuevo estado en AGENTS.md
- Al menos 3 nuevas transiciones (entrada, salida normal, salida por urgente)
- Un cron job dedicado
- Un CM dedicado para ese estado

Esto viola P4 (start simple). La clasificación de email se integra en estados existentes:

| Estado existente | Cómo se integra el email |
|---|---|
| **S_IDLE** (hook) | Tier 1: notificación clasificada vía messageTemplate |
| **S_CLOSE** (21:00) | Tier 2: micro-check batch en paso 2b |
| **S_PLAN** (08:00) | Extensión futura: "hay 2 emails @trabajo urgentes de anoche" |
| **S_SYNC** (quincenal) | Extensión futura: métricas de clasificación en revisión |

### 4.2 Skill: CM-EMAIL-CLASIFICADOR

Skill degenerado (CM-only) per skill-spec-md v2.0.0. No es un skill independiente que necesite su propio estado — es un sub-procedimiento invocado por CM-CLOSE.

**Frontmatter:**
```yaml
_manifest:
  urn: "urn:korvo:skill:korax-email-clasificador:1.0.0"
  type: "lazy_load_endofunctor"
```

**Las 4 secciones obligatorias:**

1. **Propósito:** Protocolo de revisión batch de emails del día. Sub-procedimiento de CM-CLOSE (paso 2b).

2. **I/O:**
   - Input: `date, emails_unread: Email[], patterns: PatternCorpus`
   - Output: `review: {total, by_urgency, unhandled_urgent[], capturas_sugeridas[], patterns_nuevos[]}`

3. **Procedimiento:** Obtener emails → consultar patrones → clasificar → presentar resumen → captura condicional → registrar feedback

4. **Signature Output:** Formato compacto de resumen (total + desglose + urgentes sin atender)

### 4.3 Modificaciones a la álgebra cerrada (TOOLS.md)

Agregar `gog_gmail_search` con firma completa:

```
gog_gmail_search(query: string, limit?: number) → Email[]
- Solo lectura
- Permitido en: S_CLOSE, S_ADVISE, S_SOLVE, S_IDLE
- Prohibido en: S_CAPTURE, S_TRIAGE, S_PLAN, S_EXECUTE, S_CHAOS
```

Agregar a `config.json` → `tools.allow`.

### 4.4 Invariantes respetados

| Invariante | Cómo se preserva |
|---|---|
| INV-01 (<5s captura) | Si se captura email, va por `/inbox` estándar |
| INV-02 (no sugerir destino sin delegación) | Solo lista urgentes. No dice "esto va a NEXT @trabajo" |
| INV-06 (captura sin metadatos) | El item capturado es texto plano del asunto, sin tags de clasificación |
| INV-10 (sistema ≤10% tiempo) | Tier 1 = 0 costo. Tier 2 = <2 min en cierre nocturno |
| INV-12 (micro-check Waiting) | Se mantiene intacto en CM-CLOSE paso 3 |
| INV-13 (registrar decisiones autónomas) | Toda clasificación es auditable en el log de sesión hook |
| INV-15 (TTL delegación 7 días) | Si se usa `/delegar triage` para email, misma mecánica |
| INV-16 (no capturar sin solicitud) | CM-EMAIL-CLASIFICADOR pregunta, no captura solo |

---

## 5. El modelo de aprendizaje

### 5.1 Por qué no ML

Un clasificador de ML necesita:
- Corpus de entrenamiento etiquetado (no existe)
- Pipeline de training/inference (complejidad operativa)
- Modelo desplegado (costo computacional)
- Reentrenamiento periódico (mantenimiento)

Para ~30-55 emails/día de un solo operador, esto es ingeniería para un problema que no lo justifica. El enfoque correcto es **heurísticas curadas + feedback loop + memoria semántica**.

### 5.2 La memoria semántica como clasificador

OpenClaw ya tiene un motor de búsqueda híbrido:
- 70% vector (OpenAI text-embedding-3-small, 1536 dims)
- 30% BM25 (keyword matching)
- MMR (lambda 0.7, diversidad)
- Temporal decay (half-life 30 días)

Cuando CM-CLOSE evalúa un email, puede buscar en memory search:
- "email de Contraloría clasificación" → encuentra patrones previos en email-patterns.md
- "newsletter medium ruido" → encuentra regla de ruido
- "felix.sanhueza urgente gore" → encuentra contexto del operador

El corpus de patrones, al estar en `docs/activa/` (indexado por `extraPaths`), es automáticamente searchable. No necesitamos un clasificador separado — la memoria semántica **es** el clasificador.

### 5.3 Heurística de confianza

Cada patrón aprendido tiene un nivel de confianza que determina su comportamiento:

| Confianza | Criterio | Comportamiento |
|---|---|---|
| **Baja** | 1 señal implícita (ignorado) | Solo informa en Tier 2 batch. No afecta Tier 1 |
| **Media** | 1-2 señales explícitas o de captura | Informa en Tier 2 con sugerencia suave |
| **Alta** | ≥3 señales consistentes del mismo patrón | Promover a regla determinística (sección 1/2). Incluir en Tier 1 |

**Regla de decadencia:** Un patrón sin refuerzo en 90 días pierde un nivel de confianza. Si llega a 0, se archiva (no se borra — puede reactivarse).

**Regla de contradicción:** Si un patrón con confianza alta recibe una corrección explícita, baja a media inmediatamente. Dos correcciones consecutivas → baja a baja. Esto previene que un patrón mal aprendido se perpetúe.

### 5.4 Promoción de patrones a Tier 1

Cuando un patrón alcanza confianza alta, el ciclo es:

1. Korax lo identifica en CM-SINCRONIZACION (quincenal) o CM-CLOSE
2. Lo mueve de sección 3 (aprendidos) a sección 1 (dominio) o 2 (ruido)
3. En la siguiente revisión del messageTemplate (manual, no automática), se incorpora como regla hardcodeada en las instrucciones de haiku

**Esto es intencional:** la promoción a Tier 1 requiere un paso manual (editar openclaw.json). Esto previene que patrones erróneos se propaguen automáticamente al nivel más visible del sistema. Es un circuit breaker humano en el loop de aprendizaje.

---

## 6. Comportamiento bajo delegación

### 6.1 Sin delegación (default)

```
Tier 1:  Notificación clasificada → Telegram (informativa)
Tier 2:  Resumen en CM-CLOSE → "¿Capturar algo?" (subsidiario)
Tier 3:  Feedback registrado → patrones actualizados (pasivo)
```

Korax presenta. Korvo decide. Todo.

### 6.2 Con `/delegar triage`

```
Tier 1:  Notificación clasificada → Telegram (informativa)
         + Ruido archivado automáticamente (si confianza alta)
Tier 2:  Emails relevantes capturados al GTD automáticamente
         + Reporte de decisiones en próximo contacto
Tier 3:  Feedback registrado → patrones actualizados (activo)
```

Korax actúa dentro del scope delegado. Toda decisión autónoma se loguea (INV-13) y se presenta al operador en el próximo contacto con opción de revertir.

### 6.3 Con `/delegar full`

```
Tier 1:  Notificación clasificada → solo urgentes a Telegram
         + Relevantes agrupados en digest diario
         + Ruido archivado en silencio
Tier 2:  Emails relevantes capturados y triados automáticamente
         + Asignados a contextos GTD (@trabajo, @hospital, etc.)
Tier 3:  Patrones promovidos automáticamente cuando alcanzan confianza alta
```

Este nivel requiere que el sistema lleve semanas operando con alta accuracy. Es el estado final del arco de maduración.

---

## 7. Escenarios concretos

### 7.1 Email urgente de Contraloría (lunes 10:30)

```
Tier 1 (instant):
  🔴 @trabajo | Contraloría General
  Plazo informe Programa Mejoramiento Gestión - vence miércoles
  → Responder

Tier 2 (21:00, si no se atendió):
  ⚠️ 1 urgente sin atender:
  - Contraloría: Plazo informe PMG (vence en 2 días)
  ¿Capturar al GTD?

Korvo: "sí, captura"
  → /inbox "Responder informe PMG Contraloría - plazo miércoles"
```

### 7.2 Newsletter de Medium (martes 14:00)

```
Tier 1 (instant):
  🗑️ newsletter@medium.com — Your Weekly Digest

Tier 2 (21:00):
  (no aparece en urgentes — solo en conteo de 🗑️)

Tier 3:
  Si Korvo nunca interactúa con emails de Medium en 30 días:
  Patrón "newsletter@medium.com → noise" sube a confianza alta
  → Promover a sección 2 (ruido determinístico)
```

### 7.3 Email ambiguo de colega GORE (miércoles 16:00)

```
Tier 1 (instant):
  🟡 @trabajo | María Pérez <maria.perez@goredenuble.cl>
  Consulta sobre disponibilidad reunión equipo TI
  → Responder

Tier 2 (21:00):
  (aparece en conteo de 🟡, no como urgente)

Korvo: "eso era más bien @digital, no @trabajo"
  → Feedback explícito: maria.perez@goredenuble.cl + "reunión equipo TI"
    clasificación 🟡 @trabajo → 🟡 @digital
    tipo: explícito, confianza: media
```

### 7.4 Email de hospital a las 23:30 (fuera de horas activas)

```
Tier 1:
  El heartbeat está inactivo (23:00-08:00).
  Pero el hook de gmail NO respeta horas activas — siempre corre.
  → Notificación Telegram: 🟡 @hospital | Hospital San Carlos
    Cambio turno urgencias sábado
    → Leer

  Pregunta: ¿Debería el hook respetar horas activas para emails no-immediate?
  Propuesta: Sí. Emails 🔵/⚪/🗑️ fuera de horas → queued para resumen matutino.
  Solo 🔴 immediate interrumpe fuera de horas.
```

---

## 8. Implementación por fases

### Fase 0: Prerrequisitos (antes de todo)

- [ ] Restaurar auth de gog: `gog auth login --account koraxfx@gmail.com`
- [ ] Renovar watch GCP Pub/Sub: `gog gmail watch renew --account koraxfx@gmail.com`
- [ ] Verificar que el hook de gmail está funcionando (enviar email de prueba)

### Fase 1: Tier 1 — Clasificación instant (1 sesión de trabajo)

**Archivos:**
1. Modificar `~/.openclaw/openclaw.json` — messageTemplate del mapping gmail
2. Reiniciar gateway: `sudo systemctl restart openclaw-gateway`

**Validación:** Enviar email de prueba → verificar notificación Telegram con formato clasificado.

**Riesgo:** Bajo. Es un cambio de prompt, reversible en segundos.

### Fase 2: Tier 2 — Batch en CM-CLOSE (1 sesión de trabajo)

**Archivos:**
1. Crear `docs/activa/email-patterns.md` — corpus de patrones
2. Crear `agents/korvo/korax/skills/CM-EMAIL-CLASIFICADOR.md` — skill cognitivo
3. Modificar `agents/korvo/korax/TOOLS.md` — agregar gog_gmail_search
4. Modificar `agents/korvo/korax/config.json` — agregar tool a allow
5. Modificar `agents/korvo/korax/skills/CM-CLOSE.md` — agregar paso 2b
6. Ejecutar `scripts/kora index` — registrar nuevo skill

**Validación:** Esperar heartbeat_evening o simular → verificar que CM-CLOSE ejecuta micro-check email.

**Riesgo:** Medio. Requiere que gog gmail funcione y que el heartbeat evening esté activo. Si falla, CM-CLOSE sigue funcionando sin el paso 2b.

### Fase 3: Tier 3 — Learning activo (emerge con uso)

No requiere implementación separada. El corpus de patrones se puebla naturalmente cuando:
- Korvo corrige una clasificación en la sesión main
- Korvo captura un email al GTD
- CM-CLOSE detecta emails ignorados

**Validación:** Después de 2 semanas, revisar email-patterns.md → debería tener 10-20 patrones aprendidos.

### Fase 4: Extensiones (solo si Fase 1-3 funcionan estable)

- [ ] Agregar micro-check email a CM-PLANIFICACION (mañana)
- [ ] Agregar métricas de clasificación a CM-SINCRONIZACION (quincenal)
- [ ] Evaluar si el volumen justifica horas activas diferenciadas para el hook
- [ ] Evaluar si el volumen justifica un Lobster pipeline para triage batch

---

## 9. Qué NO hacer

1. **No crear un estado S_EMAIL_TRIAGE.** 13 estados ya son muchos. El email se integra en estados existentes.

2. **No usar transform modules TypeScript.** La documentación dice que son funciones puras sin acceso a tools. El messageTemplate instruido es más simple y logra lo mismo.

3. **No automatizar captura al GTD sin delegación explícita.** Viola P2 y INV-16. El sistema clasifica; el operador captura.

4. **No entrenar un modelo de ML.** Para 30-55 emails/día de un operador, heurísticas curadas + memory search > ML pipeline.

5. **No silenciar ruido completamente en Fase 1.** El operador necesita ver las clasificaciones para dar feedback y calibrar su confianza en el sistema. Silenciar viene después, con delegación.

6. **No tocar la FSM de Korax para esto.** Si en 30 días el sistema necesita más estructura, entonces cristalizar. No antes.

---

## 10. Métricas de éxito

| Métrica | Baseline (hoy) | Target (30 días) | Target (90 días) |
|---|---|---|---|
| Emails que requieren evaluación manual | ~100% | <30% | <10% |
| Falsos negativos (urgente clasificado como no-urgente) | N/A | 0 | 0 |
| Falsos positivos (ruido clasificado como urgente) | N/A | <5/semana | <1/semana |
| Patrones aprendidos en corpus | 0 | 15-25 | 50+ |
| Correcciones explícitas del operador | N/A | 5-10/semana | <2/semana |
| Tiempo del operador en email | ~15 min/día estimado | <5 min/día | <2 min/día |
| Emails capturados al GTD vía sistema | 0 | 3-5/semana | Automático con delegación |

**La métrica definitiva:** si después de 90 días Korvo deja de pensar en "revisar email" como una tarea y simplemente reacciona a las notificaciones clasificadas, el protocolo está funcionando. El sistema debe desaparecer en el uso.

---

## 11. Relación con el ecosistema KORA

Este protocolo es un caso de uso concreto que valida varias abstracciones del framework KORA:

- **Segregación:** La clasificación (behavior) no contamina la personalidad (SOUL) ni el contexto del operador (USER). El CM-EMAIL-CLASIFICADOR es puro procedimiento.
- **Lazy evaluation:** El skill solo se carga cuando CM-CLOSE lo necesita. No paga costo de tokens en cada turn.
- **Closed algebra:** gog_gmail_search se declara formalmente en TOOLS.md antes de usarse. No hay herramientas fantasma.
- **Subsidiariedad → delegación:** El arco de maduración (presentar → sugerir → actuar) es exactamente el modelo de CM-DELEGACION.
- **Traces to:** Las invariantes respetadas (INV-01 a INV-16) tienen trazabilidad formal a los teoremas categóricos del Formal Layer.

Si este protocolo funciona bien, establece un patrón replicable para otros flujos atencionales: calendario, mensajes de Slack, notificaciones de sistema.

---

*Documento para triaje. Procesar según cadencia PCA v3.0.*
