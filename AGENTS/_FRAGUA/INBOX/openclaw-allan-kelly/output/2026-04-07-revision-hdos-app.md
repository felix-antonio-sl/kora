# Revisión rápida — `hdos-app`

Fecha: 2026-04-07
Objeto revisado: `/home/felix/projects/hdos-app`
Método: lectura estática de rutas App Router, auth, DB access, offline, REM y README

---

## Veredicto ejecutivo

`hdos-app` **ya se parece a un producto HODOM real**, no a un prototipo vacío.

Tiene buena alineación con el dominio:
- censo
- admisión
- agenda
- ficha
- llamadas
- REM
- exportación
- offline parcial
- conexión a BD viva

Pero **no está listo para producción clínica todavía**.

El cuello de botella no es UX ni modelo de datos. Es **seguridad y control de acceso**.

---

## 1. Lo que está bien

### 1.1 Alineación fuerte con el diseño HODOM
El app refleja bastante bien el paquete de diseño:

| Diseño esperado | Estado en `hdos-app` |
|---|---|
| Censo / tablero | Sí |
| Admisión | Sí |
| Agenda | Sí |
| Ficha del episodio | Sí |
| Registro de llamadas | Sí |
| REM A21 | Sí |
| Exportación REM | Sí |
| Offline-first parcial | Sí |

No veo desalineación conceptual grave. El app entiende el dominio.

### 1.2 Usa la BD viva, no una BD paralela inventada
README indica PostgreSQL existente, con 101+ tablas, 19 vistas y funciones REM.
Eso es correcto como estrategia: **converger sobre una base viva** y no duplicar fuentes.

### 1.3 La ficha clínica está bien orientada
La ruta `src/app/(app)/ficha/[stayId]/page.tsx` consume:
- estadía
- paciente
- domicilio
- cuidador
- signos vitales
- visitas
- timeline clínico
- llamadas
- alertas

Eso es clínicamente sensato. La unidad estructural sigue siendo el episodio/estadia.

### 1.4 REM está conectado a funciones reales
`/rem` y `/api/rem/export` llaman:
- `reporting.fn_rem_personas_atendidas`
- `reporting.fn_rem_visitas`
- `reporting.fn_rem_origen_derivacion`
- `reporting.fn_ocupacion_dia`

Eso cierra bien la idea de **REM derivado desde operación**, no digitado aparte.

### 1.5 Hay una primera capa real de offline
Existe:
- `PrepararOfflineButton`
- `/api/offline/fichas`
- `offline-store.ts` con IndexedDB
- cola de sync (`pending-sync`)

No es offline-first completo, pero **sí es un comienzo legítimo**.

---

## 2. Hallazgos críticos

## C1 — Login roto por contrato frontend/backend inconsistente

### Evidencia
Frontend (`src/app/(app)/login/page.tsx`) envía:
```json
{ "email": "...", "password": "..." }
```

Backend (`src/app/api/auth/login/route.ts`) espera:
```json
{ "nombre": "...", "rut": "..." }
```

### Impacto
El login actual probablemente falla siempre o de forma errática.

### Juicio
**Crítico.** El sistema no puede operar bien si el acceso base ya está inconsistente.

---

## C2 — La “contraseña” no autentica nada

### Evidencia
El backend no valida password. Solo busca profesional por RUT o nombre y crea sesión.

### Impacto
Cualquier persona que conozca un nombre o RUT válido podría entrar.

### Juicio
**Crítico clínico y legal.** Inaceptable para datos sensibles.

---

## C3 — Secret JWT inseguro por fallback hardcoded

### Evidencia
En `src/lib/auth.ts`:
```ts
process.env.NEXTAUTH_SECRET || process.env.JWT_SECRET || "hdos-dev-secret-change-in-production"
```

### Impacto
Si falta variable de entorno en deploy, el sistema usa un secreto conocido.

### Juicio
**Crítico.** Riesgo de secuestro de sesión.

---

## C4 — Acceso a páginas clínicas sin enforcement consistente

### Evidencia
- `dashboard/page.tsx` sí exige sesión (`getSession()` + redirect)
- `api/rem/export` sí exige sesión
- varias páginas clínicas (`censo`, `admision`, `agenda`, `llamadas`, `ficha`, `rem`) no muestran enforcement equivalente en lo leído
- no encontré `middleware.ts`

### Impacto
Dependiendo de la configuración real de rutas, podrías tener acceso directo a datos clínicos sin auth consistente.

### Juicio
**Crítico.** Hay deuda de perímetro.

---

## C5 — RBAC demasiado débil para entorno clínico

### Evidencia
`checkPermission()` usa `profesion` como proxy de rol. Además:
- si una acción no está listada, queda permitida por defecto
- no vi filtro por episodio asignado
- no vi segregación fuerte entre clínico / administrativo / coordinación / auditoría

### Impacto
Permisos insuficientemente controlados para confidencialidad, mínimo privilegio y trazabilidad.

### Juicio
**Crítico funcional-regulatorio.**

---

## 3. Hallazgos importantes, no críticos

## I1 — `admision/page.tsx` usa datos demo si no hay postulaciones

### Evidencia
Si no hay pendientes, renderiza pacientes ficticios (`Juan Pérez`, `Ana Torres`, etc.).

### Impacto
En ambiente real puede confundir, contaminar demos y erosionar confianza.

### Juicio
**Importante.** En producción clínica no debe existir fallback demo visible.

---

## I2 — Offline API hace N+1 queries y expone mucha ficha

### Evidencia
`/api/offline/fichas` itera `stayIds` uno por uno y por cada uno consulta episodio + paciente + signos + alertas + indicaciones.

### Impacto
- rendimiento subóptimo
- superficie de exposición alta
- falta control fino por episodio asignado

### Juicio
**Importante.** No bloquea MVP, pero hay que endurecerlo.

---

## I3 — Rate limit en memoria

### Evidencia
`rate-limit.ts` usa `Map` en proceso.

### Impacto
Sirve en single-instance MVP, pero no en despliegue serio con reinicios o múltiples instancias.

### Juicio
**Importante, no urgente.**

---

## I4 — Navegación y superficie algo inconsistentes

### Evidencia
- root redirige a `/dashboard`
- sidebar prioriza `/censo`
- README organiza por módulos HODOM, pero la superficie visible mezcla tablero y censo como entradas separadas

### Impacto
No rompe, pero muestra falta de criterio final de IA/superficie.

### Juicio
**Menor**, pero conviene ordenar.

---

## 4. Lectura de madurez

| Dimensión | Estado |
|---|---|
| Modelo dominio | Bueno |
| Integración con BD real | Bueno |
| Cobertura funcional MVP | Buena |
| UX operativa | Prometedora |
| REM automático | Bien encaminado |
| Offline | Inicial pero real |
| Seguridad | Débil |
| RBAC | Débil |
| Cumplimiento clínico | Parcial |
| Listo para producción | No aún |

---

## 5. Prioridades correctas

## P0 — Antes de cualquier despliegue clínico real

1. **Arreglar login frontend/backend**
   - unificar payload
   - eliminar campos inconsistentes

2. **Implementar autenticación real**
   - password real o SSO institucional
   - no login solo por nombre/RUT

3. **Eliminar secret hardcoded fallback**
   - fail-fast si no existe JWT_SECRET/NEXTAUTH_SECRET

4. **Cerrar perímetro de acceso**
   - middleware o guard central
   - toda ruta clínica requiere sesión

5. **Endurecer RBAC**
   - deny by default
   - roles explícitos
   - filtro por episodio asignado

## P1 — Para operar sin deuda peligrosa

6. eliminar demo fallback en admisión
7. limitar payload offline y revisar permisos
8. agregar auditoría explícita por lectura/escritura sensible
9. validar export REM contra casos reales cerrados

## P2 — Mejora estructural

10. unificar dashboard vs censo
11. revisar performance de queries pesadas
12. formalizar portal/cuidador si existe realmente en rutas

---

## 6. Recomendación

`hdos-app` **sí merece seguir vivo**. No lo podaría.

Pero lo correcto no es decir “ya está”.
Lo correcto es decir:

> **el producto está bien encaminado en dominio y operación, pero todavía no cruza el umbral mínimo de seguridad y gobernanza para uso clínico real**.

En lenguaje de célula:
- **valor**: sí, ya aparece
- **autonomía**: todavía mal cercada
- **eval**: falta endurecer seguridad y acceso
- **rollback**: no desplegar clínicamente hasta cerrar P0

---

## 7. Veredicto final

### ¿`hdos-app` entiende HODOM?
**Sí.**

### ¿Está bien orientado para MVP?
**Sí.**

### ¿Está listo para uso clínico real?
**No.**

### ¿Qué lo bloquea?
**No el dominio, sino seguridad, autenticación y control de acceso.**
