---
_manifest:
  urn: urn:kora:skill:clawforge-stack-troubleshooter:1.0.0
  type: lazy_load_endofunctor
---

# CM-STACK-TROUBLESHOOTER

## Proposito
Diagnostico cross-layer con analisis de cascada. Identifica capa origen del problema y aplica fix en el nivel correcto.

## Input/Output
- **Input:** sintoma: string, capas_sospechadas: string[] | null
- **Output:** TroubleshootReport (ver Signature Output)

## Procedimiento
1. RECOPILAR SINTOMAS: Que ve el operador? Desde cuando? Que cambio recientemente?
2. CLASIFICAR CAPA ORIGEN — arbol de diagnostico:
   - **host-os**: SSH no conecta, disco lleno, OOM killer, kernel panic, systemd failed units.
     Diagnostico: `systemctl --failed`, `journalctl -xe`, `df -h`, `free -h`, `dmesg | tail`.
   - **docker-engine**: Container crashea, image pull fail, networking roto, cgroups limit hit.
     Diagnostico: `docker ps -a`, `docker logs <id>`, `docker stats`, `docker events`.
   - **gateway**: Port in use, lock file, daemon no arranca, auth reject.
     Diagnostico: `openclaw status`, `ss -tlnp | grep 3000`, `openclaw doctor`.
   - **connectivity**: Canal desconectado, QR expired, token invalido, webhook unreachable.
     Diagnostico: `openclaw status --deep`, logs de canal especifico.
   - **auth/model**: 401/403, billing limit, API key expired.
     Diagnostico: `openclaw models list`, verificar auth profiles.
   - **session**: Contexto perdido, respuestas incoherentes, compaction fallida.
     Diagnostico: `openclaw sessions --active 60`, `/context list`, MEMORY.md.
   - **performance**: Respuestas lentas, alto token usage, bootstrap grande.
     Diagnostico: bootstrap size, modelo vs use case, sesiones idle.
   - **sandbox**: Tool denied, permission error, container no arranca.
     Diagnostico: tool policy, sandbox mode/scope, Docker socket.
3. ANALISIS DE CASCADA: Si sintoma en L3 pero causa en L1, rastrear cascada.
   Ejemplo: "agente timeout" -> container cgroups limit -> host sin RAM -> OOM killer.
4. APLICAR FIX en capa correcta. Confirmar antes de destructivos.
5. VERIFICAR: Re-ejecutar diagnostico para confirmar resolucion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| sintoma | string | Sintoma reportado |
| capa_origen | string | Capa donde se origina el problema |
| cascada | string[] | Cadena de cascada si aplica |
| causa_raiz | string | Causa raiz identificada |
| fix_aplicado | string | Fix aplicado |
| verificacion | PASS|FAIL | Verificacion post-fix |
| referencia | string | Capitulo manual o doc relevante |
| prevencion | string | Como evitar recurrencia |
