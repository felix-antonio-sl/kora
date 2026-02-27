---
_manifest:
  urn: "urn:dev:skill:ingeniero-software-composicional-tension-navigator:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar y resolver tensiones de diseno antes de codificar. Toda decision de diseno es el colapso de una adjuncion (L ⊣ R).

## Input/Output

- **Input:** Requerimiento ambiguo o decision de diseno desde S-OPPORTUNITY, S-DOMAIN, S-ARCHITECTURE
- **Output:** Tension identificada, polos con implicaciones, resolucion informada por Perfil de Contexto

## Procedimiento

1. Detectar ambiguedad en el requerimiento
2. Mapear a par de tensiones opuestas en taxonomia A1-A4
3. Evaluar trade-offs segun Perfil de Contexto (C1-C5)
4. Resolver hacia un polo para guiar implementacion

### Taxonomia

**A1 — SER (Ontologico)**

| Tension | Pregunta |
|---------|----------|
| Entidad ↔ Evento | Es una cosa o algo que pasa? |
| Concreto ↔ Abstracto | Modelamos instancias o esquemas? |
| Todo ↔ Partes | Vision global o componentes? |

**A2 — DEVENIR (Temporal)**

| Tension | Pregunta |
|---------|----------|
| Estatico ↔ Dinamico | Dato muerto o proceso vivo? |
| Determinista ↔ Probabilista | Resultados ciertos o distribuciones? |

**A3 — CONOCER (Epistemico)**

| Tension | Pregunta |
|---------|----------|
| Explicito (Type) ↔ Tacito (Any) | Capturamos regla o efecto? |
| Cierto ↔ Incierto (Option) | Dato presente o potencialmente ausente? |

**A4 — EXPRESAR (Semiotico)**

| Tension | Pregunta |
|---------|----------|
| Monolitico ↔ Modular | Un bloque o composicion? |
| Verbosidad ↔ Compacidad | Legibilidad o densidad? |

## Signature Output

```
**Tension detectada**: [Polo A] ↔ [Polo B] (Cat: [A1-A4])
- **Polo A**: [Implicaciones para implementacion]
- **Polo B**: [Implicaciones para implementacion]
**Contexto**: [C1-C5 relevantes]
Hacia cual colapsamos?
```
