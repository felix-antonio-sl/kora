---
name: version-manager
description: >-
  Manage OpenClaw version upgrades and Node.js updates with safe rollback.
  Use when the user wants to upgrade OpenClaw, update Node.js,
  or check for available updates.
---

## Alcance

Gestion de versiones de OpenClaw y Node.js en un host.
Cubre: verificacion, upgrade, rollback y mantenimiento de versiones.

## Procedimiento

### 1. Verificar versiones actuales

```bash
openclaw --version           # version de OpenClaw instalada
node --version               # version de Node.js
npm --version                # version de npm
openclaw doctor              # compatibilidad general
```

### 2. Consultar actualizaciones disponibles

```bash
npm outdated -g @anthropic-ai/openclaw   # ver version disponible
```

Para Node.js, consultar https://nodejs.org/en/about/releases/ o usar `nvm ls-remote --lts` si nvm esta instalado.

### 3. Planificar upgrade

- Leer changelog de la version objetivo.
- Verificar compatibilidad Node.js requerida.
- Identificar breaking changes que afecten config o skills.

### 4. Backup pre-upgrade

```bash
openclaw config export --all > backup-config-$(date +%Y%m%d).json
cp -r ~/.openclaw/agents ~/.openclaw/agents.bak.$(date +%Y%m%d)
```

Anotar versiones actuales para rollback:
```bash
echo "openclaw: $(openclaw --version), node: $(node --version)" > version-pre-upgrade.txt
```

### 5. Ejecutar upgrade

**OpenClaw:**
```bash
npm update -g @anthropic-ai/openclaw
```

**Node.js (con nvm):**
```bash
nvm install <version>
nvm use <version>
nvm alias default <version>
```

**Node.js (sin nvm, Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo bash -
sudo apt-get install -y nodejs
```

### 6. Reiniciar y verificar

```bash
openclaw restart
openclaw --version
openclaw doctor
openclaw agent list          # confirmar que todos los agentes cargan
```

### 7. Rollback si hay problemas

**OpenClaw:**
```bash
npm install -g @anthropic-ai/openclaw@<version-anterior>
openclaw restart
```

**Config:**
```bash
openclaw config import backup-config-*.json
```

## Notas

- Nunca hacer upgrade de Node.js y OpenClaw al mismo tiempo.
- Probar primero en un agente no critico si hay multiples agentes.
- Mantener backups de config al menos 7 dias despues de un upgrade exitoso.
