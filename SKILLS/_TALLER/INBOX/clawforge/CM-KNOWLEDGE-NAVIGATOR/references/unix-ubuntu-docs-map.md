---
title: Unix Ubuntu Docs Map
status: internal
lang: es
source_policy: official_docs_only
---

# Unix/Ubuntu Docs Map

Usar este mapa para consultas de host Unix/Ubuntu. Citar siempre el documento oficial indicado, no este archivo.

## Routing

| Tema | Documento oficial | URL |
|------|-------------------|-----|
| SSH, acceso remoto, hardening base de `sshd` | OpenSSH Server | https://documentation.ubuntu.com/server/_sources/how-to/security/openssh-server.md.txt |
| Firewall host-based y UFW | Firewalls | https://documentation.ubuntu.com/server/_sources/how-to/security/firewalls.md.txt |
| Seguridad de host, AppArmor, baseline hardening | Security | https://documentation.ubuntu.com/server/_sources/how-to/security.md.txt |
| APT, actualizaciones automaticas, `unattended-upgrades` | Automatic updates | https://documentation.ubuntu.com/server/_sources/how-to/software/automatic-updates.md.txt |
| Networking base, Netplan, DNS, routing | Introduction to networking | https://documentation.ubuntu.com/server/explanation/intro-to/networking/ |
| Sincronizacion horaria del host | Synchronize time using timedatectl and timesyncd | https://documentation.ubuntu.com/server/how-to/networking/timedatectl-and-timesyncd/ |
| Estrategia segura de actualizacion antes de promover cambios | Advance testing of updates in best-practice server deployments | https://documentation.ubuntu.com/server/explanation/software/advance-testing-of-updates-in-best-practice-server-deployments/ |
| Drift en archivos gestionados por paquetes | Changing package files | https://documentation.ubuntu.com/server/explanation/software/changing-package-files/ |

## Reglas de uso

- Seleccionar primero una fila del mapa y citar el documento oficial asociado.
- Si un tema no calza claramente en el mapa, declararlo como gap de referencia en vez de afirmarlo como hecho cerrado.
- Cuando una respuesta combine varios planos (ej: SSH + firewall + updates), citar cada documento oficial relevante por separado.
