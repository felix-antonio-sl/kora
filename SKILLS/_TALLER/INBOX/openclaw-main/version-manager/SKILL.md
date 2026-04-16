---
name: version-manager
description: Gestionar upgrades de OpenClaw y Node.js con rollback seguro. Usar cuando el usuario quiere actualizar OpenClaw, actualizar Node.js, o verificar versiones disponibles.
---

## Alcance

Gestion de versiones de OpenClaw y Node.js en un host.
Cubre: verificacion, upgrade, rollback y mantenimiento de versiones.

## Procedimiento

### 1. Verificar versiones actuales

```bash
openclaw --version           # version de OpenClaw instalada
node --version               # version de Node.js
openclaw doctor              # compatibilidad general
```

### 2. Consultar actualizaciones disponibles

```bash
openclaw update --dry-run    # ver que cambiaria antes de aplicar
```

Para Node.js: revisar https://nodejs.org/en/about/releases/ o `nvm ls-remote --lts` si nvm esta instalado.

### 3. Planificar upgrade

- Leer changelog de la version objetivo (disponible via `openclaw update --dry-run`).
- Verificar compatibilidad Node.js requerida.
- Identificar breaking changes que afecten config o skills.

### 4. Backup pre-upgrade

```bash
openclaw backup create       # backup canonico de config y estado
```

Anotar versiones actuales para referencia:
```bash
echo "openclaw: $(openclaw --version), node: $(node --version)" > version-pre-upgrade.txt
```

### 5. Ejecutar upgrade

**OpenClaw:**
```bash
openclaw update              # upgrade canonico (actualiza runtime + valida config)
```

**Node.js (con nvm):**
```bash
nvm install 24
nvm use 24
nvm alias default 24
```

**Node.js (sin nvm, Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo bash -
sudo apt-get install -y nodejs
```

### 6. Reiniciar y verificar

```bash
openclaw gateway restart
openclaw --version
openclaw doctor
openclaw agents list         # confirmar que todos los agentes cargan
```

### 7. Rollback si hay problemas

**OpenClaw:**
```bash
npm install -g openclaw@<version-anterior>
openclaw gateway restart
```

**Config (si openclaw update corrompio algo):**
```bash
openclaw backup restore <backup-id>
```

## Notas

- Nunca hacer upgrade de Node.js y OpenClaw al mismo tiempo.
- `openclaw update` internamente corre `openclaw doctor` y puede modificar `openclaw.json` — es el mecanismo canonico, no npm directo.
- Mantener backups de config al menos 7 dias despues de un upgrade exitoso.
