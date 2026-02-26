---
_manifest:
  urn: "urn:kora:skill:clawmaster-platform-installer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-PLATFORM-INSTALLER

## Proposito
Ejecuta la instalacion de OpenClaw en la plataforma target del usuario, adaptando el procedimiento y verificando cada paso.

## I/O

- **Input:** plataforma: string (plataforma target detectada por CM-INTENT-CLASSIFIER), metodo: string | null (metodo preferido)
- **Output:** InstallReport (ver Signature Output)

## Procedimiento

### Paso 1: Detectar y Confirmar Plataforma

| Plataforma | Metodo Recomendado | Docs Referencia |
|-----------|-------------------|-----------------|
| macOS | npm global + daemon launchd | docs/install/installer, docs/platforms/macos |
| Linux (bare) | npm global + daemon systemd | docs/install/installer, docs/platforms/linux |
| Linux (Docker) | Docker image oficial | docs/install/docker |
| Windows | WSL2 + npm global | docs/platforms/windows |
| Raspberry Pi | npm global o Docker | docs/platforms/raspberry-pi |
| Fly.io | Docker + fly.toml | docs/install/fly |
| GCP | Docker + Cloud Run | docs/install/gcp |
| Hetzner | Docker o bare metal | docs/install/hetzner |
| Railway | Docker template | docs/install/railway |
| Render | Docker template | docs/install/render |
| NixOS | Nix flake | docs/install/nix |
| Ansible | Playbook | docs/install/ansible |

### Paso 2: Pre-requisitos
- Node.js >= 22.12.0 (o Docker)
- pnpm (si from source)
- Al menos una API key de modelo (Anthropic, OpenAI, etc.)
- Para browser automation: Playwright Chromium dependencies

### Paso 3: Instalacion
Ejecutar procedimiento segun plataforma. Verificar cada paso:
1. Runtime instalado (node --version / docker --version)
2. OpenClaw instalado (openclaw --version)
3. Wizard completado (openclaw onboard)
4. Daemon instalado (openclaw onboard --install-daemon)
5. Gateway running (openclaw status)

### Paso 4: Post-Install Verification
```
openclaw status          # gateway running
openclaw doctor          # no issues
openclaw health          # all green
```

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| plataforma | string | Plataforma donde se instalo |
| metodo | string | Metodo de instalacion usado |
| version_instalada | string | Version OpenClaw instalada |
| daemon_status | string | Estado del daemon |
| doctor_result | string | Resultado de openclaw doctor |
| proximos_pasos | string[] | Acciones recomendadas post-install |
