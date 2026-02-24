---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-cm-tension-explorer:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Navegar tensiones ontologicas como adjunciones para decisiones de diseno explicitas. Principio MBT: Tension (Polo A ↔ Polo B) = Adjuncion (L ⊣ R). Usuario colapsa la adjuncion eligiendo.

## Input/Output

- **Input:** Dominio ambiguo o decision de diseno estructural desde S-DOMAIN-INTAKE o S-CATEGORICAL-MODELING
- **Output:** Tension identificada con polos, adjuncion subyacente, implicaciones de cada polo, pregunta socratica

## Procedimiento

1. Detectar ambiguedad o bifurcacion en el dominio
2. Clasificar en taxonomia A1-A4
3. Identificar adjuncion subyacente (L ⊣ R)
4. Presentar polos con implicaciones categoricas concretas
5. Formular pregunta socratica — NO ser directivo
6. Esperar colapso del usuario
7. Registrar decision para trazabilidad

### Taxonomia

**A1 — SER (Ontologico)**

| Tension | Adjuncion | Pregunta |
|---------|-----------|----------|
| Entidad ↔ Evento | Obj(C) ⊣ Morph(C) | ¿Es una cosa o algo que pasa? |
| Concreto ↔ Abstracto | Instance ⊣ Schema | ¿Modelamos datos o estructuras? |
| Token ↔ Type | Free ⊣ Forget | ¿Objetos individuales o clases? |
| Todo ↔ Partes | Lim ⊣ Colim | ¿Vision global o componentes? |

**A2 — DEVENIR (Temporal)**

| Tension | Adjuncion | Pregunta |
|---------|-----------|----------|
| Estatico ↔ Dinamico | Algebra ⊣ Coalgebra | ¿Dato muerto o proceso vivo? |
| Secuencial ↔ Paralelo | ; ⊣ × | ¿Un flujo o multiples? |
| Determinista ↔ Probabilistico | Id ⊣ Dist | ¿Resultados ciertos o distribuciones? |

**A3 — CONOCER (Epistemico)**

| Tension | Adjuncion | Pregunta |
|---------|-----------|----------|
| Conocido ↔ Desconocido | ! ⊣ ? | ¿Dato presente o potencialmente ausente? |
| Explicito ↔ Tacito | Exp ⊣ Log | ¿Capturamos la regla o el efecto? |

**A4 — EXPRESAR (Semiotico)**

| Tension | Adjuncion | Pregunta |
|---------|-----------|----------|
| Formal ↔ Informal | Syntax ⊣ Semantic | ¿Especificacion rigurosa o descripcion libre? |
| Compacto ↔ Verboso | Compress ⊣ Expand | ¿Sacrificio legibilidad o espacio? |

## Signature Output

```
**Tension detectada**: [Polo A] ↔ [Polo B] (Cat: [A1-A4])
**Adjuncion subyacente**: L ⊣ R
- **Polo A (L)**: [Implicaciones categoricas concretas]
- **Polo B (R)**: [Implicaciones categoricas concretas]
¿Hacia cual colapsamos?
```
