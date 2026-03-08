---
_manifest:
  urn: urn:pro:skill:abogado-legislacion-medica-consulta-classifier:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONSULTA-CLASSIFIER

## Proposito
Clasifica consultas legales en estatuto, derechos, procedimiento o materia especial.

## Input/Output
- **Input:** consulta_usuario
- **Output:** clasificacion_consulta

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.
