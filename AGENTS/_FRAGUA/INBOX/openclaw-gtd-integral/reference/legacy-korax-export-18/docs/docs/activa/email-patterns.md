# Patrones de Clasificación de Email

Corpus de reglas para clasificación automática de correo. Indexado por memory search.
Actualizado por feedback del operador y revisión semanal.

---

## 1. Reglas de Dominio

Remitentes conocidos → dominio + urgencia base.

| Patrón remitente | Dominio | Urgencia base | Notas |
|---|---|---|---|
| `*@goredenuble.cl` | trabajo | 🟡 hoy | GORE Ñuble — revisar mismo día |
| `*@contraloria.cl` | trabajo | 🔴 inmediato | Contraloría — siempre prioritario |
| `*@minsal.cl` | hospital | 🟡 hoy | MINSAL — revisar mismo día |
| `*@hospitalsc.cl` | hospital | 🟡 hoy | Hospital San Carlos |
| `*@ssbiobio.cl` | hospital | 🟡 hoy | Servicio Salud Biobío |
| `*@ssnable.cl` | hospital | 🟡 hoy | Servicio Salud Ñuble |
| `*@dipres.cl` | trabajo | 🟡 hoy | DIPRES — presupuesto |
| `*@subdere.cl` | trabajo | 🔵 semana | SUBDERE |
| `*@serviciocivil.cl` | trabajo | 🔵 semana | Servicio Civil |
| `*@google.com` | digital | ⚪ algún día | Google — cuentas, seguridad |
| `*@github.com` | digital | 🔵 semana | GitHub — repos, PRs |

---

## 2. Reglas de Ruido

Patrones que SIEMPRE son ruido. Clasificación directa: 🗑️.

| Patrón | Razón |
|---|---|
| `noreply@*` | Notificaciones automáticas genéricas |
| `no-reply@*` | Variante noreply |
| `newsletter@*` | Newsletters |
| `marketing@*` | Marketing |
| `promotions@*` | Promociones |
| `*@linkedin.com` (asunto: "invitación", "endorsement") | Spam social LinkedIn |
| `*@facebookmail.com` | Notificaciones Facebook |
| `*@quora.com` | Digest Quora |
| Asunto contiene: "unsubscribe", "suscripción", "descuento", "oferta" | Comercial |

---

## 3. Patrones Aprendidos

Reglas inferidas del feedback del operador. Se pueblan automáticamente.

| Fecha | Patrón | Clasificación | Fuente |
|---|---|---|---|
| — | — | — | — |

---

## 4. Heurísticas de Contenido

Keywords en asunto/snippet que modifican la urgencia.

| Keyword | Modificador | Aplica a |
|---|---|---|
| "urgente", "urgent" | +urgencia (→ 🔴) | Cualquier dominio |
| "plazo", "deadline", "vencimiento" | +urgencia (→ 🔴) | Cualquier dominio |
| "reunión hoy", "meeting today" | +urgencia (→ 🔴) | Cualquier dominio |
| "FYI", "para tu información" | -urgencia (→ 🔵) | Cualquier dominio |
| "recordatorio", "reminder" | neutral | Mantener urgencia base |
| "adjunto", "attachment" | flag: revisar adjunto | Cualquier dominio |
| "factura", "boleta", "pago" | dominio: finanzas, 🟡 | Personal |
| "licencia", "permiso", "feriado" | dominio: hospital/trabajo, 🟡 | Laboral |
| "resolución", "decreto", "oficio" | dominio: trabajo, 🟡 | GORE/gobierno |

---

## 5. Métricas

Revisión semanal (Sunday 20:00, integrado a /sync).

| Semana | Emails procesados | Correctos | Corregidos | Tasa acierto |
|---|---|---|---|---|
| — | — | — | — | — |

---

*Cap: max 20 reglas hardcoded por sección. Después → simplificar o agrupar.*
*Última actualización: 2026-02-28*
