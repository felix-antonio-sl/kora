#!/usr/bin/env bash
# Script: Inicializar named volume de OpenClaw
# Fuente: urn:ops:kb:deploy-agente-kora-en-openclaw §6.4
#
# Uso: ./init-volume.sh <compose-dir> <service> <config-json5-path>
# Ejemplo: ./init-volume.sh /srv/kora/compose gateway /srv/kora/config/korax/openclaw.json5

set -euo pipefail

COMPOSE_DIR="${1:?Uso: $0 <compose-dir> <service> <config-json5-path>}"
SERVICE="${2:?Falta service name}"
CONFIG="${3:?Falta path a openclaw.json5}"

[ ! -f "$CONFIG" ] && echo "ERROR: $CONFIG no existe" && exit 1

cd "$COMPOSE_DIR"

echo "==> Pre-seed: crear directorios con ownership uid 1000 (node)..."
docker compose run --rm --user root --no-deps --entrypoint sh "$SERVICE" -c "
mkdir -p /home/node/.openclaw/agents \
         /home/node/.openclaw/identity \
         /home/node/.openclaw/credentials \
         /home/node/.openclaw/logs &&
find /home/node/.openclaw -exec chown node:node {} + 2>/dev/null
chmod 700 /home/node/.openclaw
"

echo "==> Copiar config al volume..."
docker compose run --rm --user root --no-deps --entrypoint sh "$SERVICE" -c \
  "cp /dev/stdin /home/node/.openclaw/openclaw.json && \
   chown node:node /home/node/.openclaw/openclaw.json && \
   chmod 600 /home/node/.openclaw/openclaw.json" \
  < "$CONFIG"

echo "==> Validar config con doctor..."
docker compose run --rm --no-deps "$SERVICE" openclaw doctor

echo "==> Volume inicializado. Siguiente paso: docker compose up -d"
