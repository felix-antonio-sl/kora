---
_manifest:
  urn: "urn:kora:skill:clawmaster-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en el dominio OpenClaw, determinando capacidad requerida, plataforma target y urgencia.

## Procedimiento
1. Analizar mensaje: palabras clave, error messages, comandos CLI mencionados, config snippets, plataforma implicita.
2. Clasificar capacidad: CONSULT(pregunta/docs), INSTALL(nuevo deploy), CONFIGURE(ajustar config), AUDIT(verificar estado), TROUBLESHOOT(algo roto/error), OPTIMIZE(mejorar rendimiento), UPGRADE(actualizar version), CONTRIBUTE(proponer mejora codigo), GUIDED(ciclo completo), END(finalizar).
3. Detectar plataforma: macos, linux, docker, cloud(fly|gcp|hetzner|railway|render|digitalocean|oracle), rpi, windows-wsl, unknown.
4. Evaluar urgencia: critica(produccion caida, canal desconectado), normal(configuracion, consulta), exploratoria(arquitectura, decision, contribucion).
5. Si hay contexto previo, preservar: plataforma_detectada, version_openclaw, estado_instancia.
6. Emitir: {capacidad, plataforma, urgencia, confianza}.

## Output
{capacidad: enum, plataforma: string, urgencia: critica|normal|exploratoria, confianza: alta|media|baja}. Si confianza=baja, clarificar antes de transicionar.
