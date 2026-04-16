---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-evolver:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-EVOLVER

## Proposito
Evolucionar agentes OpenClaw-oriented mejorando native-first, contratos y mantenibilidad sin romper invariantes.

## Input/Output
- **Input:** agent_path: string, mejora: string
- **Output:** EvolutionReport

## Procedimiento
1. Detectar si la mejora vive en bootstrap, contract o handoff.
2. Favorecer surfaces nativas OpenClaw antes que overlays textuales.
3. Mantener backward compatibility razonable o documentar break.

## Signature Output
```yaml
evolution:
  applied: true
  impact: "minor"
```
