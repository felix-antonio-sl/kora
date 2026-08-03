# AGENTS.md

## Estatuto

Este repositorio es la encarnación KORA legada, “la bestia”. Su ley y realización histórica permanecen congeladas; la doctrina y autoría futuras viven en `../kora-pneuma`.

## Modo de sesión

Actúa como conservador del legado: recupera evidencia, corrige solo errores de verdad autorizados y evita bifurcar el régimen vigente. Esta postura operativa de Codex no convierte la sesión en un artefacto KORA ni amplía su autoridad.

## Entrada y autoridad

- Lee `README.md`, `docs/README.md` y la documentación exacta del subsistema afectado.
- Antes de desarrollar doctrina, agentes o skills, consulta `../kora-pneuma/artefactos/conocimiento/kora/regimen-de-ley.md`.
- Usa este repositorio como autoridad solo para corpus aún no migrado o para la procedencia histórica que pneuma indique.

## Reglas

- Migrar significa reescribir en pneuma con la ley vigente, no copiar ni modernizar aquí.
- No edites salidas generadas, índices o instalaciones runtime como fuente.
- Conserva URN, hashes, lifecycle y trazabilidad.
- No ejecutes despliegues o instalaciones por una tarea de lectura o mantenimiento documental.
- En hosts primary/secondary, determina el rol con el comando de la toolchain antes de cualquier operación sensible.

## Verificación

Usa los comandos documentados por `toolchain/kora` para el frente exacto. Para cambios autorizados del núcleo, ejecuta el check estricto y la suite vigente; para documentación, `git diff --check` y revisión de referencias bastan. Declara cualquier runtime o paridad no observados como `NOT_RUN`.
