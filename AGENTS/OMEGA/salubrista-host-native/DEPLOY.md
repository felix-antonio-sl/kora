# Deploy — Salubrista host-nativo

## Que es

Paquete de agente OpenClaw para `salubrista`: copiloto tecnico de salud publica y sistemas sanitarios complejos.

## Contenido

```text
salubrista-host-native/
├── DEPLOY.md
├── config/
│   └── openclaw.json
└── workspace/
    ├── IDENTITY.md
    ├── SOUL.md
    ├── AGENTS.md
    ├── USER.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── MEMORY.md
    ├── memory/
    └── skills/
        ├── intent-salubrista/
        ├── epi-analyst/
        ├── epi-vigilance/
        ├── network-analyst/
        ├── implementation-planner/
        ├── quality-auditor/
        ├── product-builder/
        └── report-builder/
```

## Pre-requisitos

1. Node.js 22.14+ o superior
2. OpenClaw instalado: `npm install -g openclaw@latest`
3. Credenciales de modelo configuradas en el host
4. Token de gateway: `openssl rand -hex 32`

## Deploy

### 1. Copiar workspace

```bash
cp -a workspace/ ~/.openclaw/workspace-salubrista/
```

### 2. Copiar config

```bash
cp config/openclaw.json ~/.openclaw/openclaw.json
```

Reemplazar:

- `__REPLACE_GATEWAY_TOKEN__`

### 3. Verificar

```bash
openclaw config validate
openclaw doctor
openclaw skills list --eligible
```

### 4. Arrancar

```bash
openclaw gateway
```

## Notas

- El heartbeat queda deshabilitado por defecto.
- No hay canales ni automatizacion activa en esta base.
- El bundle prioriza seguridad: sandbox `all`, `workspaceAccess: ro`, sin `exec`, sin escritura y sin cron.
