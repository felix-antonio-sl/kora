# Caso aplicado canonico: Asto / Besto / Resto

Procedimiento original del operador (2026-06-03) del cual esta skill es la
generalizacion. Se conserva como ejemplo vivo de convocatoria de panel.

## Panel

| Alias | Identidad (que encarna) | Capacidades (que posee) |
|-------|--------------------------|--------------------------|
| Asto | agente `salud/salubrista` (AGENT.md productivo en KORA) | skill `hospitalizacion-domiciliaria` (build claude-code) |
| Besto | skill encarnable `mente-omega` (Pentamotor) | skill `cat-thinking` (pensamiento categorial) |
| Resto | persona deployada `dov-dori` (~/.claude/agents/dov-dori.md) | skill `modelamiento-opm` |

Observaciones de diseno que este panel ilustra:

- La **identidad** no tiene una sola forma material: Asto encarna un AGENT.md,
  Besto encarna una skill de razonamiento, Resto encarna una persona ya
  transmutada al runtime. Las tres son identidades legitimas.
- La **diversidad epistemica** esta garantizada por construccion: salud
  publica/clinica (Asto), razonamiento estructural-discursivo (Besto),
  modelado conceptual de sistemas (Resto). Ninguno es clon de otro.
- Las **capacidades** son skills que el experto ejerce dentro de su turno:
  Resto puede emitir un modelo OPM como parte de su propuesta; Asto puede
  aplicar criterios HODOM; Besto puede auditar la estructura del argumento.

## Procedimiento original (texto del operador)

> Asto, Besto y Resto deben resolver el problema mediante consenso critico.
>
> Cada uno formulara una propuesta inicial breve con tesis, argumentos,
> supuestos y riesgos. Luego cada uno criticara las propuestas de los otros,
> limitandose a objeciones sustantivas. Con esas criticas construiran una
> sintesis comun. Despues intentaran refutar esa sintesis como adversarios
> externos. Si aparecen objeciones criticas, corregiran la sintesis y
> repetiran el ciclo hasta que no queden objeciones relevantes.
>
> El consenso solo puede declararse cuando los tres acepten que la sintesis
> es la mejor version disponible, que no pueden mejorarla materialmente con
> nuevos argumentos y que las discrepancias restantes son menores.
>
> La salida debe incluir: sintesis final, razonamiento consolidado, aportes
> de Asto/Besto/Resto, supuestos aceptados, riesgos pendientes,
> incertidumbres y nivel de confianza de cada experto.

## Mapeo al protocolo de la skill

| Fragmento del procedimiento | Estado de la skill |
|------------------------------|--------------------|
| definicion del panel con identidades + capacidades | `convocar` |
| "propuesta inicial breve con tesis, argumentos, supuestos y riesgos" | `proponer` |
| "criticara las propuestas de los otros, limitandose a objeciones sustantivas" | `criticar` |
| "con esas criticas construiran una sintesis comun" | `sintetizar` |
| "intentaran refutar esa sintesis como adversarios externos" | `refutar` |
| "si aparecen objeciones criticas, corregiran la sintesis y repetiran el ciclo" | `corregir` (loop con `refutar`) |
| "el consenso solo puede declararse cuando los tres acepten..." (triple aceptacion) | `declarar` |
| "la salida debe incluir: sintesis final, ..." | `entregar` |

Lo que la skill agrega sobre el procedimiento original:

- **max_ciclos** con salida de disenso estructurado + HITL (el original no
  define que pasa si el ciclo no converge).
- **Gate de diversidad** en `convocar` (el original la logra por construccion;
  la skill la exige para cualquier panel).
- **Modos de realizacion declarados** (encarnacion vs orquestacion) con
  registro auditable en la salida.
- **Catalogo de degeneracion** y reglas anti consenso-de-cortesia.
