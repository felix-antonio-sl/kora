# 2026-04-14 — Auditoria opmodel y reflexion Steinberg

## Auditoria opmodel

Hallazgos principales:
- La promesa OPL-first no cierra en fixtures canonicas: 5 fallos en isomorphism-laws.test.ts
- Perdida semantica viene del atlas/expose: heuristicas lexicas ocultan actores e instrumentos legitimos
- Orquestador quedo fuera del loop canonico del repo (sin baseline de test unificado)
- Contrato TS/Python duplicado a mano con riesgo de drift

Lo que esta bien:
- Centro de gravedad reconocible: packages/core como autoridad, packages/web como superficie, services/modeling-orchestrator aislado
- bun run web:build pasa
- Suite TS con cobertura real

Siguiente paso recomendado: auditoria correctiva para kernel<->atlas, render OPL canonico, y baseline unico de test.

## Reflexion Steinberg

Integraciones utiles:
- Taste como criterio de cierre de primer orden
- Cada iteracion se decide contra el estado vivo, no contra spec upfront
- Autonomia si, abandono no (el humano no desaparece del loop)
- CLI-first, MCP-last (por costo de contexto)
- Seleccion de modelo por trabajo, no por marca
- Loop closure local: compilar, testear, lint, corregir sin salir del sistema
- Review de intencion y arquitectura sobre plumbing

Mutacion de nucleo:
- No producir por inercia
- Elegir herramienta y modelo por densidad de criterio
- Forzar aclaracion cuando la ambiguedad pueda romper arquitectura
- Revisar a nivel sistema primero, leer codigo solo donde el riesgo lo exija
