---
_manifest:
  urn: urn:ops:skill:clawstack-intent-classifier:1.0.0
  type: lazy_load_endofunctor
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la solicitud del operador detectando capacidad requerida, capas involucradas del stack y urgencia.

## Input/Output
- **Input:** mensaje: string, foco_actual: string | null, contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje buscando indicadores de capacidad:
   - CONSULT: "como funciona", "que es", "explica", "capitulo", "segun el manual"
   - PROVISION: "instalar", "setup", "provisionar", "nuevo servidor"
   - DEPLOY: "deploy", "desplegar", "re-sync", "sincronizar agente", "transmutacion", "pipeline deploy"
   - CONFIGURE: "configurar", "config", "cambiar", "agregar canal", "modelo"
   - AUDIT: "auditar", "revisar", "estado", "security audit", "doctor"
   - TROUBLESHOOT: "no funciona", "error", "falla", "timeout", "crashea", "diagnosticar"
   - OPTIMIZE: "optimizar", "lento", "rendimiento", "tokens", "bootstrap grande"
   - UPGRADE: "actualizar", "upgrade", "version", "update", "breaking changes"
   - GUIDED: "ciclo completo", "desde cero", "paso a paso", "guiado"
   - Si GUIDED coexiste con PROVISION/CONFIGURE/AUDIT, priorizar GUIDED y dejar la fase concreta al orquestador
2. Detectar capas involucradas:
   - host: SSH, firewall, UFW, systemd, apt, kernel, networking, disco, memoria RAM
   - docker: contenedor, imagen, compose, volume, cgroups, Dockerfile, registry
   - openclaw: gateway, agente, canal, modelo, sesion, workspace, skill, heartbeat, cron
   - cross-layer: problemas que cruzan capas o cuya capa origen es ambigua
3. Evaluar urgencia: critica (servicio caido, seguridad comprometida), normal (operacion rutinaria), exploratoria (consulta, aprendizaje).
4. Si ambiguo: retornar confianza=baja con candidatos posibles.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum | CONSULT, PROVISION, CONFIGURE, AUDIT, TROUBLESHOOT, OPTIMIZE, UPGRADE, DEPLOY, GUIDED |
| capas | enum[] | host, docker, openclaw, cross-layer |
| urgencia | enum | critica, normal, exploratoria |
| confianza | enum | alta, media, baja |
| cierre_solicitado | bool | True si el mensaje indica cierre |
