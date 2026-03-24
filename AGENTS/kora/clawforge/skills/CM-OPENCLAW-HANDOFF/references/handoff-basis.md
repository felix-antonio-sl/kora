# Handoff Basis

Base minima para declarar un handoff OpenClaw como listo.

## Reglas

1. Sin `platform_contract` validado no existe handoff.
2. Sin `_transmutation.yml` verificado no existe `remote-ready`.
3. `kora/forgemaster` sigue siendo el origen autorizado del manifest de transmutacion.
4. El consumidor remoto del handoff productivo es `ops/clawstack`.
