# Deploy — Clawforge host-nativo

## Que es

Clawforge es una fragua de agentes OpenClaw. Diseña, despliega, opera, audita, repara y evoluciona agentes. Este paquete contiene todo lo necesario para encarnarlo como gateway OpenClaw nativo sobre un host Unix.

## Contenido

```
clawforge-host-native/
├── DEPLOY.md            ← esta guia
├── config/
│   └── openclaw.json    ← config (placeholders marcados)
└── workspace/
    ├── IDENTITY.md
    ├── SOUL.md
    ├── AGENTS.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── BOOT.md
    ├── MEMORY.md
    ├── memory/
    └── skills/          ← 32 skills
```

## Pre-requisitos

1. **Node.js 24+** (o 22.14+ minimo)
2. **OpenClaw** instalado: `npm install -g openclaw@latest`
3. **Credenciales**:
   - `ANTHROPIC_API_KEY`
   - `GEMINI_API_KEY` (embeddings)
   - Token de bot Telegram
   - Token de gateway (generar con `openssl rand -hex 32`)

## Deploy

### 1. Copiar workspace

```bash
cp -a workspace/ ~/.openclaw/workspace/
```

### 2. Copiar y completar config

```bash
cp config/openclaw.json ~/.openclaw/openclaw.json
```

Reemplazar placeholders:

| Placeholder | Valor |
|---|---|
| `__REPLACE_GATEWAY_TOKEN__` | `openssl rand -hex 32` |
| `__TELEGRAM_USER_ID__` | ID numerico Telegram del operador |

### 3. Configurar credenciales

```bash
# Variables de entorno
cat > ~/.openclaw/.env << 'EOF'
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AI...
TELEGRAM_BOT_TOKEN=123456:ABC...
EOF

# O via wizard
openclaw onboard
```

### 4. Verificar

```bash
openclaw doctor
```

### 5. Arrancar

```bash
# Como daemon (produccion)
openclaw gateway install
openclaw daemon start

# O manual (debug)
openclaw gateway
```

### 6. Confirmar

```bash
openclaw health --json
openclaw status --deep
openclaw skills list --eligible
```

## Acceso remoto

```bash
# SSH tunnel (preferido)
ssh -N -L 18789:127.0.0.1:18789 user@servidor

# Tailscale Serve (alternativa)
# En config: gateway.tailscale.mode: "serve"
```

## Upgrade

```bash
npm update -g openclaw
openclaw --version
openclaw gateway restart
openclaw doctor
```

## Agregar mas agentes al mismo gateway

```bash
openclaw agents add <id>
# Editar ~/.openclaw/openclaw.json: agents.list, bindings
openclaw gateway restart
```

## Notas

- No hay secrets en este paquete. Todo marcado con placeholders.
- Los 32 skills se portaron intactos. Pueden requerir adaptacion progresiva.
- Sandbox para tools riesgosas es opcional (requiere Docker en el host).
- Control UI accesible en `http://127.0.0.1:18789/`.
