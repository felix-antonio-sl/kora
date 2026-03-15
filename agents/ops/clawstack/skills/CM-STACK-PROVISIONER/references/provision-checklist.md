---
title: Provision Checklist
status: internal
lang: es
---

# Provision Checklist

## Host Unix
- [ ] OS actualizado (kernel + userspace)
- [ ] SSH: solo key auth, root login disabled, puerto custom
- [ ] Firewall UFW: default deny, solo puertos necesarios
- [ ] Chrony: sincronizacion horaria activa
- [ ] Swap configurado si memoria limitada
- [ ] Unattended-upgrades habilitado para seguridad

## Docker
- [ ] Docker Engine instalado (repo oficial)
- [ ] Docker Compose v2 disponible
- [ ] daemon.json: log rotation, storage driver actualizado
- [ ] Usuario en grupo docker (o rootless mode)
- [ ] Sin Docker socket expuesto a contenedores

## OpenClaw
- [ ] Node.js >= 22.12.0
- [ ] OpenClaw instalado y onboarded
- [ ] Gateway en loopback (127.0.0.1)
- [ ] Auth configurado
- [ ] Al menos un canal conectado
- [ ] openclaw doctor: sin errores
- [ ] Daemon persistente (systemd unit o launchd)

## Cross-layer
- [ ] Firewall permite solo puertos de canales necesarios
- [ ] Docker networking no expone puertos innecesarios
- [ ] Secrets en variables de entorno o SecretRef, no en archivos
- [ ] Backup strategy definida
