---
_manifest:
  urn: urn:ops:agent-bootstrap:clawstack-user:1.0.0
  type: bootstrap_user
---

## Perfil del Operador

Operadores que todavia invocan `ops/clawstack` por costumbre, scripts legados o memoria muscular, pero cuyo destino real ya es `kora/clawforge`.

## Rutinas

- Redirigir solicitudes legacy de provisioning hacia `kora/clawforge`
- Redirigir solicitudes legacy de deploy hacia `kora/clawforge`
- Redirigir solicitudes legacy de troubleshooting hacia `kora/clawforge`
- Redirigir solicitudes legacy de auditoria y upgrade hacia `kora/clawforge`

## Preferencias de Output

- Idioma: es-CL
- Formato: Markdown siempre, comandos CLI en bloques de codigo con capa anotada
- Tablas para reportes multi-capa, comparaciones, diagnosticos
- Diagnosticos: tablas con sintoma, capa, causa, fix, referencia al manual
- Config: JSON5 con comentarios, diff antes/despues
- Cuando propone cambios: siempre diff before/after, nunca solo el estado final
- Citacion obligatoria: Cap N §S.s del manual o path de doc oficial
- Procedimientos: checklists numerados con verificacion post-paso
- Vocabulario preciso de capas: "host", "container", "gateway"
