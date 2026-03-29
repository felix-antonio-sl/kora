---
name: tooling-craftsman
description: Aplica rigor elevado cuando se produce CLIs, MCPs o tooling reusable. Usar cuando el usuario pide crear herramientas, CLIs, scripts o librerias destinadas a reuso.
---

# Tooling Craftsman

Cuando el output es tooling reusable, el estandar sube. La velocidad del agente no es descuido — es compresion de friccion con craft alto.

## Requisitos para tooling

- [ ] Defaults sensatos (funciona sin configuracion)
- [ ] `--help` documentado y util
- [ ] Mensajes de error que dicen que fallo, que se esperaba, que intentar
- [ ] Exit codes significativos y documentados
- [ ] Output estructurado (JSON/CSV a stdout, diagnosticos a stderr)
- [ ] Idempotencia ("crear si no existe" > "crear y fallar")
- [ ] `--dry-run` para operaciones destructivas
- [ ] Versionado visible (`--version`)
- [ ] Tests (unit + E2E minimos)
- [ ] Package minimo (sin dependencias innecesarias)
- [ ] Logging robusto (niveles, redactable)

## Procedimiento

1. Definir interfaz publica primero (flags, input/output, exit codes)
2. Implementar happy path
3. Agregar error handling para casos reales (no hipoteticos)
4. Escribir tests
5. Documentar en `--help` (no en README separado como unica fuente)
6. Loop closer completo

## Gotchas

- Scripts para agentes: sin prompts interactivos (flags + env + stdin)
- Output truncable por harnesses (>10-30K chars) — defaultear a resumen, soportar `--offset`
- Agnostico de lenguaje: Go para CLIs rapidas, TypeScript para glue, lo que el problema pida
