---
name: host-provisioner
description: Aprovisionar un servidor nuevo para ejecutar OpenClaw — instalar Node.js, instalar OpenClaw, configurar firewall, e instalar el daemon. Usar cuando el usuario tiene un servidor nuevo y quiere dejarlo listo para OpenClaw desde cero.
---

## Alcance

Aprovisionamiento completo de un servidor nuevo para ejecutar OpenClaw.
Desde OS base hasta gateway funcionando como daemon systemd.

## Procedimiento

### 1. Verificar OS y acceso

```bash
uname -a                     # confirmar OS
whoami                       # confirmar usuario
sudo -v                      # confirmar acceso sudo
```

Requisitos minimos: 1 CPU, 1 GB RAM, 10 GB disco, acceso SSH.

### 2. Actualizar sistema

```bash
# Ubuntu/Debian:
sudo apt-get update && sudo apt-get upgrade -y
# RHEL/Fedora: sudo dnf update -y
```

### 3. Instalar Node.js 24+

**Opcion A: nvm (recomendado)**
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install 24
nvm alias default 24
```

**Opcion B: NodeSource (Ubuntu/Debian)**
```bash
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo bash -
sudo apt-get install -y nodejs
```

Verificar: `node --version` debe mostrar v24.x+.

### 4. Instalar OpenClaw

```bash
npm install -g openclaw@latest
openclaw --version
```

### 5. Configurar firewall

**UFW (Ubuntu/Debian):**
```bash
sudo ufw allow OpenSSH
# No abrir el puerto del gateway al exterior por defecto — el gateway es interno
# Si se necesita acceso externo, usar reverse proxy (nginx/Caddy) sobre puerto 443
sudo ufw enable
sudo ufw status
```

El gateway escucha en `localhost:18789` por defecto. No exponer directamente a internet.

### 6. Onboarding

```bash
openclaw onboard
```

Seguir el wizard: configurar API key, directorio de agentes, preferencias iniciales.

### 7. Instalar daemon

```bash
openclaw gateway install     # instala user-level systemd service (sin sudo)
```

Verificar:
```bash
systemctl --user status openclaw-gateway   # debe mostrar active (running)
openclaw doctor                            # cero errores
openclaw status                            # gateway healthy
```

## Notas

- Usar nvm permite upgrades de Node.js sin sudo y sin afectar el sistema.
- `openclaw gateway install` instala el daemon como user-level systemd service, no system-level. No requiere sudo.
- Guardar la API key en variable de entorno o en el store seguro de OpenClaw, no en archivos planos.
- Despues del provisioning, usar el skill `operator` para gestion continua.
