# Configuración de Correo — Modo Procesamiento Korax

## Cuentas
| Cuenta | Propósito |
|--------|-----------|
| `felixsanhuezaluna@gmail.com` | Principal — donde llega TODO |
| `koraxfx@gmail.com` | Cuenta Korax — aquí recibiré y procesaré los correos |

## Estado Actual
- **Forwarding:** Configurado (copia sin eliminar en origen)
- **Acceso Korax:** gog conectado a koraxfx@gmail.com

## Flujo de Procesamiento — Pipeline de 3 Tiers

### Tier 1: Clasificación Instantánea (hook)
- **Trigger:** Gmail push notification → Pub/Sub → gog-gmail-watch → OpenClaw webhook
- **Modelo:** haiku (rápido, barato)
- **Acción:** Clasifica email en tiempo real con reglas hardcoded en messageTemplate
- **Output:** Notificación Telegram con emoji de urgencia (🔴🟡🔵⚪🗑️)
- **Latencia:** <5 segundos desde recepción

### Tier 2: Micro-check Batch (cierre vespertino)
- **Trigger:** heartbeat_evening (21:00) → S_CLOSE → skill close → paso 3
- **Modelo:** sonnet (default session)
- **Acción:** Ejecuta skill email-clasificador batch sobre todos los no leídos
- **Consulta:** Corpus de patrones via memory_search (email-patterns.md)
- **Output:** Resumen consolidado en cierre del día
- **Skill:** `skills/email-clasificador/SKILL.md`

### Tier 3: Corpus de Patrones (aprendizaje continuo)
- **Ubicación:** `docs/activa/email-patterns.md` (indexado por memory search)
- **Contenido:** Reglas de dominio, ruido, heurísticas de contenido, patrones aprendidos
- **Actualización:** Por feedback del operador (corregir clasificación → patrón se registra)
- **Revisión:** Semanal (Sunday 20:00, integrado a /sync)
- **Cap:** max 20 reglas hardcoded por sección

## Criterios de Clasificación

| Emoji | Nivel | Acción |
|---|---|---|
| 🔴 | Inmediato | Leer ahora, posiblemente responder |
| 🟡 | Hoy | Revisar en el día |
| 🔵 | Semana | Revisar cuando haya tiempo |
| ⚪ | Algún día | Baja prioridad |
| 🗑️ | Ruido | Descartado automáticamente |

Dominios: trabajo (GORE), hospital, digital, personal, finanzas, desconocido.

## Configuración Técnica
- **gog account:** koraxfx@gmail.com
- **Lectura:** `gog gmail messages search`
- **Notificación:** Hook Gmail configurado en OpenClaw

*Última actualización: 2026-02-28*
