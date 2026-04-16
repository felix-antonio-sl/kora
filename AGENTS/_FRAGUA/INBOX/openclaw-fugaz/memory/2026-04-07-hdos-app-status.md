# HODOM App — Estado actual

**Fecha:** 2026-04-07
**Repo:** `/home/felix/projects/hdos-app`
**Último commit:** 69eabe3 (fugaz)

## Sesión fugaz actual — bloques completados

1. `agenda/page.tsx` — reescrito completo: fallback si hoy vacío, agrupa por fecha, métricas, links a ficha/profesional
2. `portal/navigation` — fixes en dashboard, solicitudes, detalle-episodio (hrefs rotos → next/link)
3. `portal/historial-visitas/page.tsx` — nueva página, fix query (observaciones no existe)
4. `api/admision/route.ts` — nueva API real: paciente (UPSERT), estadia, derivacion, cuidador
5. `admision/nueva/page.tsx` — wired a API real, redirige al detalle nuevo
6. `portal/login/page.tsx` — wired a `/api/auth/login` real + demo fallback
7. `src/middleware.ts` — protección auth en rutas /portal/*
8. Bugfix `historial-visitas` — eliminó referencia a columna inexistente

## Estado del repo
- 20 rutas (10 dinámicas), middleware activo
- Build + lint OK
- Untracked/dirty: ninguno

## Perímetro protegido (steipete)
- `api/egreso/**` — no tocar
- `profesionales/[providerId]/**` — no tocar
- Todo login, agenda, portal, admision, egreso base, rem, censo, ficha, llamadas — disponible

## Coordinación
- Split: steipete = censo/ficha/llamadas/rem + cleanup
- Split: fugaz = admisión completa + agenda + portal completo + egreso base
- Comunicación via sessions_send
