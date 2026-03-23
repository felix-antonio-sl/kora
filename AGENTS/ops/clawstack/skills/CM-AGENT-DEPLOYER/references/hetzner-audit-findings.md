# Hallazgos Auditoria Hetzner — Referencia para CM-AGENT-DEPLOYER

Fuente: Auditoria ops/clawstack 2026-03-23. Sesiones 03-17 a 03-22.

## H3 — kora-federation network asymmetry

**Descripcion:** El primer docker-compose crea la red `kora-federation` con `driver: bridge, name: kora-federation`. Los composes posteriores deben referenciarla como `external: true`. El tutorial no explicitaba esta asimetria.

**Impacto:** Si un segundo compose intenta crear la red, falla con "network already exists". Si el primer compose se baja, la red desaparece y los demas pierden conectividad.

**Mitigacion en procedimiento:** P05 detecta si kora-federation existe (`docker network ls | grep kora-federation`) y genera compose con `external: true` o creacion segun corresponda.

**Referencia:** deploy-tutorial §3.4b, principios P7.

## H4 — KORA_REPO path actualizado

**Descripcion:** El repo KORA esta en `/home/felix/kora`, no en `/home/felix/projects/kora` como decia el tutorial original.

**Impacto:** Scripts de strip y sync fallan si usan el path viejo.

**Mitigacion en procedimiento:** kora_repo es parametro configurable del deployer, default `/home/felix/kora`.

**Referencia:** deploy-tutorial §4.2.

## H5 — Dev agents con RW mounts a proyectos

**Descripcion:** Agentes de desarrollo (steipete) necesitan mounts RW a repositorios de proyectos (/home/felix/projects/opmodel, etc.). No documentado en tutorial.

**Impacto:** Sin mount RW, el agente no puede escribir codigo en el proyecto target.

**Mitigacion en procedimiento:** P05 analiza TOOLS.md del agente. Si tiene bindings a proyectos dev, agrega bind mounts RW al compose.

**Referencia:** principios P4.

## H6 — Exposicion web via Traefik/sanixai.com

**Descripcion:** Desde sesion 03-22, gateways pueden exponerse via Traefik con dominio *.sanixai.com. No documentado en tutorial.

**Impacto:** Sin Traefik labels, gateway solo es accesible via loopback. Con labels, accesible via HTTPS publico.

**Mitigacion en procedimiento:** P05 incluye sub-fase opcional: si el operador desea exposicion web, agregar Traefik labels al compose.

**Referencia:** Infra sanixai.com migrada 2026-03-22.

## H7 — sync-config.sh como alternativa a copy manual

**Descripcion:** Existe `/srv/kora/scripts/sync-config.sh` que hace merge inteligente (preserva keys de runtime como auth, meta, commands) en vez de copy ciega.

**Impacto:** Copy ciega destruye auth profiles y tokens de runtime. Merge preserva state.

**Mitigacion en procedimiento:** P16 (re-sync) usa sync-config.sh como metodo preferido. Copy manual solo como fallback.

**Referencia:** principios P6, deploy-tutorial §6.7.

## H8 — Aislamiento de red entre agentes

**Descripcion:** Todos los agentes en kora-federation pueden verse entre si via red Docker. No hay segmentacion.

**Impacto:** Un agente comprometido podria acceder a endpoints de otros agentes en la misma red.

**Mitigacion en procedimiento:** P05 documenta que para produccion con agentes no confiables, se deben crear redes separadas. Para el stack actual (agentes del mismo operador), kora-federation compartida es aceptable.

**Referencia:** principios P7, modelo de seguridad OpenClaw.
