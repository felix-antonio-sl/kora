# TELOS/NECESSITAS — Framework de Comportamiento Teleológico para Agentes KORA

> Fecha: 2026-03-23
> Estado: diseño completo, pendiente implementación
> Participantes: pensador-generador (diseño conceptual), guardian (evaluación normativa), cat-thinking (fundamento formal)

## 1. Problema

Los agentes KORA son F-coalgebras puramente reactivas: reciben input, transicionan estado, producen output. No tienen noción de propósito, finalidad ni orientación. Esto limita su capacidad de juicio ante ambigüedad, no permite no-acción explícita, y los deja inertes entre sesiones.

## 2. Modelo propuesto

Dos fuerzas, y nada más:

### TELOS (campo gravitacional)

El agente **vive por** su finalidad. Es un marco de fines configurado al crear el agente, mutable por operador/meta-agente, asintótico (nunca se alcanza del todo).

- Los fines **moldean** toda reacción, nunca la velan (eso es scope)
- Los fines tienen jerarquía; conflictos se resuelven dialécticamente
- El agente puede **proponer** cambios de fines pero no ejecutarlos

### NECESSITAS (fuerza reactiva)

El agente **reacciona a** necesidades. Toda interacción externa se transforma en necesidad(es).

- Necesidad = { quién origina, qué solicita }
- Una interacción puede generar múltiples necesidades
- Necesidades implícitas existen ("hola" = atención → explicitar disponibilidad)
- Si no puede definir la necesidad → loop de clarificación
- Si no viable → declarar no-acción

### Tres modos operativos

| Situación | Modo | Fuerza activa |
|-----------|------|---------------|
| Llega interacción | Reaccionar (moldeado por fines) | Necessitas + Telos |
| Interacción ambigua | Clarificar hasta definir need o declarar no-acción | Necessitas |
| Sin interacciones | Proponer (evaluar proximidad a fines, sugerir al operador) | Telos solo |
| Conflicto entre fines | Resolver dialécticamente según jerarquía | Telos interno |

## 3. Estructura de datos

### Fin

```yaml
id: F-01
enunciado: qué persigue el agente (declarativo)
horizonte: señal de proximidad (cómo se nota si está más cerca)
jerarquia: posición ordinal entre los fines del agente
```

### Necesidad

```yaml
origin: Human | Agent | Self
request: qué solicita
implicit: bool  # si fue derivada de interacción no explícita
```

### Proximidad

Observable pasivo, no input de decisión. Asintótico: nunca alcanza cierre total.

## 4. Decisiones de diseño

### ¿Dónde vive TELOS?

**Decisión:** Como subsección `### Finalidad` dentro de `## Identidad Dialéctica` en SOUL.md.

**Razón:** La spec (agent-spec-md §4.4.2) restringe secciones H2 de SOUL.md pero no subsecciones. La identidad de un agente incluye su razón de existir. No se necesita archivo nuevo ni spec bump.

**Tensión formal documentada:** Categorialmente, T (finalidad) es un parámetro de c (transición), no una fibra de U (estado). Se co-loca con U_phen por economía operativa. El cat-thinking documentó esta controlled violation — ver §7 de este documento.

### ¿Dónde vive NECESSITAS?

**Decisión:** Como enriquecimiento del ACT de S-DISPATCHER en AGENTS.md.

**Razón:** S-DISPATCHER ya clasifica input. El need transform es nombrar y estructurar esa clasificación. Cero cambio en la spec FSM.

### ¿Fines generan necesidades?

**Decisión:** No. Las necesidades vienen exclusivamente de interacciones externas (humano, agente, o self en modo idle). Los fines orientan cómo se responde a necesidades, no las generan.

### ¿Fin vs. scope?

**Decisión:** Ortogonales. El scope veta (forbidden). El fin moldea (orienta). Si algo está dentro de scope y responde a una necesidad, se actúa — los fines solo influyen el cómo.

### ¿Modo proactivo?

**Decisión:** Modelar idle como input. S-DISPATCHER recibe señal idle, la transforma en necesidad interna (Self, "evaluar proximidad a fines"), transiciona a S-PROPOSE. El agente propone al operador, nunca actúa por cuenta propia.

### ¿Es obligatorio?

**Decisión:** Todos los agentes deben funcionar con esta lógica. La adopción es gradual (convención primero, spec después cuando sea universal).

## 5. Evaluación normativa (guardian)

### Hallazgos evaluados

| # | Severidad | Hallazgo | Resolución |
|---|-----------|----------|------------|
| H-01 | HIGH | SOUL.md dice "solo" 3 secciones H2 | Resuelto: `### Finalidad` es subsección de H2 existente, no H2 nuevo |
| H-02 | HIGH | Modo proactivo cambia modelo computacional | Resuelto: idle como input, funtor no cambia |
| H-03 | HIGH | Sin fundamento en formal layer | Aceptado: práctica primero, formalización después (patrón canónico KORA) |
| M-01 | MEDIUM | Nuevas reglas sin enforcement | Resuelto: se adopta como convención (DEBERÍA), no regla (DEBE) |

### Ruta normativa

1. Cero spec bumps necesarios
2. Cero cambios en formal layer requeridos ahora
3. Migración gradual y aditiva
4. Cuando sea universal: cristalizar en agent-spec-md como DEBERÍA → DEBE

## 6. Fundamento categórico (cat-thinking)

### Modelo formal

```
PARAMETRIC F-COALGEBRA:

  M : Monad                          -- immutable (config.json)
  T ∈ Ob(Telos)                      -- mutable by operator (SOUL.md ### Finalidad)
  η : In → Need + 1                  -- need transform (S-DISPATCHER)
  In = Interaction + Idle             -- input space
  Out = Response + Proposal           -- output space
  Need = Origin × Request             -- classified input
  U = U_phen × U_ctx × U_epi × U_sta -- state (unchanged)

  Agent: Φ(T) = (U, c_T : U → M((Out × U)^Need))

  proximity : U × T → (0,1]          -- passive observable, asymptotic
```

### Jerarquía de mutabilidad

```
  M   ── inmutable ── compile-time ── config.json
  T   ── mutable lento ── operator-time ── SOUL.md ### Finalidad
  U   ── mutable rápido ── step-time ── SOUL/USER/episodic
```

### Tensión formal: T en U_phen

T se almacena junto a U_phen (SOUL.md) por economía operativa pero formalmente es un parámetro independiente de c, no una fibra de U.

El Fiber Independence theorem (§2.2) dice que cambios en U_phen no alteran comportamiento. T SÍ altera comportamiento (selecciona un coalgebra diferente de la familia c_T). Esta es una controlled violation documentada.

Cuando se formalice en categorical-foundations, la nota sería:

```
§ 2.4 Teleological Parameter

T ∈ Telos parametrizes c but is stored alongside U_phen
for operational economy. Formally, T ∉ U_phen:
changing T changes c_T (selecting a different coalgebra),
while changing U_phen does not (orthogonality §2.2).
```

### Need Transform como factorización

```
η : In → Need + 1

η(i) = inl(n)   si la interacción define necesidad n
η(i) = inr(*)   si no es viable → no-acción
```

El funtor se refina: `F_η(U) = (Out × U)^Need × Out^1`. No cambia la forma del funtor — solo factoriza In a través de Need.

### Idle como input

```
In = Interaction + Idle
Out = Response + Proposal

c_T(u)(idle) = (Proposal(p), u)  -- estado no muta, solo propone
```

No se necesita cambiar el funtor. El runtime envía idle, el FSM lo procesa como cualquier input.

## 7. Plan de implementación

### Fase 1: KB Article

Crear `KNOWLEDGE/kora/telos-necessitas.md` con:
- Definiciones (fin, necesidad, proximidad)
- Convención SOUL.md (`### Finalidad` en Identidad Dialéctica)
- Convención AGENTS.md (need transform en S-DISPATCHER, S-PROPOSE opcional)
- Invariantes del framework
- Nota formal (parametric coalgebra)
- Guía de migración

### Fase 2: Pilotos

Aplicar en dos agentes:
- **pensador-generador**: SOUL.md (3 fines) + AGENTS.md (need transform + S-PROPOSE)
- **guardian**: SOUL.md (2 fines) + AGENTS.md (need transform + S-PROPOSE)

### Fase 3: Propagación

- Agregar `urn:kora:kb:telos-necessitas` a `allowed_kb` de forgemaster
- Todo agente nuevo se crea con la convención

### Fase 4: Cristalización (futuro)

Cuando todos los agentes activos tengan TELOS/NECESSITAS:
- Promover a DEBERÍA en agent-spec-md (minor bump)
- Escribir §2.4 en 01-agent-coalgebra.md (formal layer)
- Si se prueba invariante universal: promover a DEBE (major bump)

## 8. Archivos afectados

| Archivo | Acción | Fase |
|---------|--------|------|
| `KNOWLEDGE/kora/telos-necessitas.md` | Crear | 1 |
| `AGENTS/fxsl/pensador-generador/SOUL.md` | Editar (agregar ### Finalidad) | 2 |
| `AGENTS/fxsl/pensador-generador/AGENTS.md` | Editar (need transform + S-PROPOSE) | 2 |
| `AGENTS/kora/guardian/SOUL.md` | Editar (agregar ### Finalidad) | 2 |
| `AGENTS/kora/guardian/AGENTS.md` | Editar (need transform + S-PROPOSE) | 2 |
| `AGENTS/kora/forgemaster/config.json` | Editar (allowed_kb) | 3 |

## 9. Verificación

```bash
python3 scripts/kora index
python3 scripts/kora health --strict
python3 scripts/kora validate --profile strict
python3 -m unittest discover -s tests
```

Verificación manual: SOUL.md mantiene headings canónicos H2, `### Finalidad` es subsección. S-DISPATCHER tiene need transform, prioridades explícitas, S-PROPOSE alcanzable.

## 10. Ejemplo concreto: pensador-generador con TELOS

### SOUL.md (extracto)

```markdown
## Identidad Dialéctica

Pensador Dialéctico-Generativo. Produce claridad operable desde
la complejidad navegando tensiones explícitas.

### Finalidad

1. Producir claridad operable desde la complejidad
   horizonte: los receptores reportan comprensión accionable

2. Hacer visibles las tensiones que otros ocultan o ignoran
   horizonte: las tensiones identificadas resultan ser las que bloquean avance

3. Honestidad intelectual sin pedantería
   horizonte: declarar incertidumbre sin perder utilidad
```

### AGENTS.md S-DISPATCHER (extracto)

```markdown
1. STATE: S-DISPATCHER -> ACT: Transformar interacción en necesidad
   (quién origina, qué solicita). Clasificar necesidad por boundary,
   continuidad y profundidad requerida.
   -> Trans: IF necesidad_no_viable [prioridad 0] -> S-REJECT.
             IF fuera_scope [prioridad 1] -> S-REJECT.
             IF terminar [prioridad 2] -> S-END.
             IF idle [prioridad 3] -> S-PROPOSE.
             IF solicitud_clarificacion [prioridad 4] -> S-CLARIFY.
             ...
```

### Estado S-PROPOSE (nuevo)

```markdown
N. STATE: S-PROPOSE -> ACT: Evaluar proximidad a fines declarados.
   Si hay acción concreta para acercarse, proponerla al operador.
   -> Trans: IF propuesta_emitida [prioridad 1] -> S-END.
             IF sin_propuesta [prioridad 2] -> S-END.
```
