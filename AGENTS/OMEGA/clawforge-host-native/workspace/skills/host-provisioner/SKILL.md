---
name: host-provisioner
description: >-
  Provision a fresh host server for running OpenClaw: install Node.js, install
  OpenClaw, configure firewall, and set up daemon. Use when the user has a fresh
  server and wants to set it up for OpenClaw from scratch.
---

## Alcance

Aprovisionamiento completo de un servidor nuevo para ejecutar OpenClaw.
Desde OS base hasta gateway funcionando como daemon.

## Procedimiento

### 1. Verificar OS y acceso

```bash
uname -a                     # confirmar OS
whoami                       # confirmar usuario
sudo -v                      # confirmar acceso sudo
```

Requisitos minimos: 1 CPU, 1 GB RAM, 10 GB disco, acceso SSH con sudo.

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
npm install -g @anthropic-ai/openclaw
openclaw --version
```

### 5. Configurar firewall

**UFW (Ubuntu/Debian):**
```bash
sudo ufw allow OpenSSH
sudo ufw allow 3000/tcp      # puerto gateway (ajustar si es diferente)
sudo ufw enable
sudo ufw status
```

Solo abrir puertos estrictamente necesarios. El puerto 3000 es el default del gateway.

### 6. Onboarding

```bash
openclaw onboard
```

Seguir el wizard: configurar API key, directorio de agentes, preferencias iniciales.

### 7. Instalar daemon

```bash
openclaw daemon install
sudo systemctl enable openclaw && sudo systemctl start openclaw
```

### 8. Verificar instalacion completa

```bash
sudo systemctl status openclaw   # debe mostrar active (running)
openclaw doctor                  # cero errores
openclaw status                  # gateway healthy
```

## Notas

- Usar nvm permite upgrades de Node.js sin sudo y sin afectar el sistema.
- Guardar la API key en variable de entorno o en el store seguro de OpenClaw, no en archivos planos.
- Despues del provisioning, usar el skill `operator` para gestion continua.
