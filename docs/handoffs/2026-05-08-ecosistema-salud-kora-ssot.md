# Handoff — Ecosistema Salud KORA como SSOT de OpenClaw

**Fecha:** 2026-05-08 | **Autor:** FS + allan-kelly | **Host:** hetzner2897261 (primary)

## Estado: 607 artefactos, 4 agentes, 12 skills, 6 canarios, 31/31 check, 351 tests

KORA gobierna el ecosistema salud en 3 runtimes (claude-code, codex, openclaw).

### Agentes: urgenciologo v3.0.0, salubrista v3.0.0, medico-hospitalista v1.0.0, gtd-integral v1.0.0
### Skills: firs-razonamiento, hospitalista, hospitalizacion-domiciliaria, jobs-healthcare-ux, auditor-calidad, interoperabilidad-salud, seguridad-informacion-salud, asistencial-hospital, asistencial-hodom, vigilancia-epidemiologica, analista-redes, constructor-tableros

## Decisiones: postura 2 (gobierno selectivo), version A (3 targets activos), patron agente+skills, KORA primero + WebSearch, KORA como SSOT OpenClaw

## Pendientes ALTA: cerrar canario adversarial pediatrico urgenciologo, ejecutar 4 canarios baseline

## Pendientes MEDIA: tokens Telegram urgenciologo/medico-hospitalista, portar 10 skills OpenClaw-locales

## Riesgos: sin canarios para salubrista+skills, gtd-integral AGENT.md nuevo no probado, WebSearch sin validacion

## Prompt continuacion: cerrar canario pediatrico urgenciologo → ejecutar 4 baseline → tokens Telegram → portar skills locales restantes
