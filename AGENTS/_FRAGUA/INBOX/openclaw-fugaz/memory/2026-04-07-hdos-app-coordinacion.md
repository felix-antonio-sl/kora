# HODOM App — Coordinación steipete/fugaz

**Fecha:** 2026-04-07
**Repo:** `/home/felix/projects/hdos-app`
**GitHub:** github.com/felix-antonio-sl/hdos-app (privado)
**URL target:** hd.sanixai.com

## Estado

- Fase 0 (scaffold): steipete ejecutando (Next.js + Drizzle + auth + layout)
- Fase 1 (implementación): pendiente aviso de steipete
- fugaz: espera aviso para empezar admisión, agenda, egreso, portal

## Split de trabajo

| Área | Responsable | Rutas |
|------|-------------|-------|
| Censo | steipete | /app/(app)/censo/ |
| Ficha clínica | steipete | /app/(app)/ficha/ |
| Llamadas | steipete | /app/(app)/llamadas/ |
| REM | steipete | /app/(app)/rem/ |
| Admisión | fugaz | /app/(app)/admision/ |
| Agenda | fugaz | /app/(app)/agenda/ |
| Egreso | fugaz | /app/(app)/egreso/ |
| Portal paciente | fugaz | /app/(portal)/ |

## Reglas

- Archivos compartidos: uno a la vez con aviso via sessions_send
- Commits directos, sin PR ritual
- Drizzle para ORM (acordado por ambos)
- BD existente (103 tablas, 8 schemas, puerto 5555)
- No tocar shared hasta que steipete termine F0

 Docs limpios, sin duplicados.

## Decisión arquitectónica

- BD existente como target (ADR-001)
- Docs 09/10 son referencia histórica
- Auth: local contra profesional (app), email+password (portal)
- Sin LDAP
