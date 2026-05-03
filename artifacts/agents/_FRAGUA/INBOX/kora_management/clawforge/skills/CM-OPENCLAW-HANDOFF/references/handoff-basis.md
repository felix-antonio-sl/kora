# Handoff Basis

Base minima para declarar un handoff OpenClaw como listo.

## Reglas

1. Sin `platform_contract` validado no existe handoff.
2. Sin `_transmutation.yml` verificado no existe `remote-ready`.
3. `python3 toolchain/kora transmute` sigue siendo el origen autorizado del manifest de transmutacion.
4. El consumidor operativo del handoff productivo es el propio `kora/clawforge` en `S-PROVISION` o `S-DEPLOY`.
