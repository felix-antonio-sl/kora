# Toolchain KORA

- `python3 toolchain/kora` es el unico entrypoint soportado.
- `toolchain/kora_lib/` contiene la implementacion viva de la CLI.
- `toolchain/kora.bat` y `toolchain/kora.ps1` son wrappers de conveniencia.
- `toolchain/legacy_migration/` concentra one-shots y migradores historicos.
- `toolchain/sync_openclaw_docs_mirror.py` sigue soportado como excepcion operativa puntual.

Regla: si un flujo debe vivir institucionalmente, entra por `toolchain/kora`, deja logica reusable en `toolchain/kora_lib/` y gana cobertura en `tests/`.

Si no cumple eso, tratalo como legado o soporte acotado.
