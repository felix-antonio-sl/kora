# Open Model (opmodel) — Contexto Estratégico

**Fecha registro:** 2026-03-25
**Fuente:** Derivación de steipete (agente co-desarrollo)
**Repo:** /home/node/projects/opmodel (en entorno steipete)

## Qué es

Plataforma de modelamiento basada en **OPM (Object-Process Methodology)**. Permite:
- Modelar objetos, procesos, estados y relaciones OPM
- Refinar por OPDs (Object-Process Diagrams)
- Producir OPL (Object-Process Language)
- Validar metodología
- Simular comportamiento
- UI web

## Visión

No es un prototipo de diagramas — es una **infraestructura de modelamiento general, reusable y escalable**. Félix quiere usarla como plataforma para modelar sistemas reales: clínicos, operacionales, normativos, organizacionales, software, etc.

## Estado actual (2026-03-25)

- **961 tests green** (progresión: 832 → 880 → 961)
- Repo estable
- Core: OPL bilingüe, renderAll, exportMarkdown, modelStats, validación metodológica, simulación ampliada, compound states
- Web/Visual: reglas visuales compartidas, visual lint/QA, layout semántico (in-zoom, unfold, branching-control, structural-cluster, sd-balanced), post-layout relaxation, navegación de findings, respeto a pinned/auto_sizing, detección de crowded diagrams, severidad visual explícita

## Framing correcto

- Ya no es solo prototipo → es plataforma robusta para modelado reusable
- Foco actual: **consolidar la base** porque de ahí cuelga todo el trabajo de modelamiento futuro
- La base visual convierte Open Model en infraestructura general (no depende de positioning manual)

## Relevancia para Korax

Cuando Félix mencione Open Model, opmodel, OPM, o trabajo de modelamiento:
- Reconocer como proyecto estratégico de alto avance
- Priorizar consolidación de base sobre features nuevos
- Puede generar UTs, Proyectos o Resultados vinculados a este contexto
