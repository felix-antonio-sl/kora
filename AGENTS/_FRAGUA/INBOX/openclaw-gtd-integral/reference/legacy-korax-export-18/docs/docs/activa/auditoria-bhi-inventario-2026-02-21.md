# Auditoría Técnica — BHI Inventario
## Sistema de Gestión de Inventario Bravo Hair Institute

---

**Documento:** Informe de Auditoría Técnica
**Aplicación:** https://inventario.bhi.cl
**Fecha de auditoría:** 21 de febrero de 2026
**Elaborado por:** Korax (agente de Korvo / Félix Sanhueza)
**Solicitado por:** Félix Sanhueza Luna
**Desarrollador de la aplicación:** Ariel Sanhueza (asanlu.dev)
**Versión del informe:** 1.0
**Clasificación:** Interno — uso restringido

---

## 1. Resumen Ejecutivo

Se realizó una auditoría técnica no intrusiva de la aplicación web BHI Inventario, desarrollada por Ariel Sanhueza para Bravo Hair Institute. La auditoría incluyó navegación completa de todos los módulos disponibles, análisis del stack tecnológico, revisión de headers HTTP y detección de problemas funcionales, de seguridad y de arquitectura.

La aplicación se encuentra en un estado funcional sólido para una versión inicial (v1), con un diseño de flujos de trabajo apropiado para el dominio clínico-quirúrgico. Se identificaron **3 hallazgos de seguridad** (2 críticos, 1 medio), **2 bugs funcionales** y **4 oportunidades de mejora técnica**.

Los problemas críticos identificados son todos de configuración de servidor y pueden ser resueltos en menos de una hora sin tocar el código de la aplicación.

---

## 2. Alcance y Metodología

### 2.1 Alcance

| Ítem | Detalle |
|------|---------|
| URL auditada | https://inventario.bhi.cl |
| Credenciales utilizadas | administracion@bhi.cl (rol: Administrador) |
| Fecha y hora | 21-02-2026, 17:00–17:10 UTC |
| Tipo de auditoría | Caja gris — acceso con credenciales, sin acceso a código fuente ni servidor |
| Herramienta | Playwright (Chromium headless) + análisis de headers HTTP |

### 2.2 Metodología

1. Navegación completa de todos los módulos del menú lateral
2. Extracción de estructura HTML: encabezados, tablas, formularios, enlaces internos
3. Detección de framework JS por inspección de variables globales y atributos DOM
4. Análisis de headers HTTP de respuesta
5. Recolección de errores de consola y fallos de red durante la sesión

### 2.3 Exclusiones

- No se realizaron pruebas de penetración activas
- No se intentó acceso a rutas no vinculadas desde la UI
- No se modificó ningún dato del sistema

---

## 3. Stack Tecnológico

### 3.1 Frontend

| Componente | Detección | Observaciones |
|-----------|-----------|---------------|
| Framework JS | No identificable externamente | SPA compilada/minificada. Probable React, Vue o Svelte |
| CSS | **Tailwind CSS** | Detección positiva por clases utilitarias en DOM |
| Bundle | `index-BCUBLQfa.js` (único) | Sin code splitting. Todo el código en un archivo |
| Empaquetador | Probable **Vite** | El hash en el nombre de archivo (`BCUBLQfa`) es característico de Vite |

### 3.2 Backend / Infraestructura

| Componente | Valor |
|-----------|-------|
| Web server | **nginx/1.24.0 (Ubuntu)** |
| Protocolo | HTTPS (TLS activo) |
| Autenticación | Session cookie |
| Content-Encoding | gzip |

### 3.3 Meta información

```
Title pattern: "BHI Inventario - Bravo Hair Institute"
Footer: "Copyright © 2026 Bravo Hair Institute. Todos los derechos reservados. By asanlu.dev"
```

---

## 4. Módulos Relevados

| # | Módulo | URL | Estado | Descripción |
|---|--------|-----|--------|-------------|
| 1 | Dashboard | /dashboard | ✅ Operativo | KPIs principales, movimientos recientes, alertas de stock |
| 2 | Catálogo | /catalogo | ✅ Operativo | 139 productos, 44+ categorías, carga masiva, CRUD |
| 3 | Stock | /stock | ✅ Operativo | Control por área, ingreso/egreso/transferencia |
| 4 | Solicitudes | /solicitudes | ✅ Operativo | Flujo en 4 etapas: Mis → Revisión → Aprobación → Historial |
| 5 | Compras | /compras | ✅ Operativo | Solicitudes → Cotizaciones → OC → Recepciones |
| 6 | Proveedores | /proveedores | ✅ Operativo | 9 proveedores registrados con RUT, giro, condición de pago |
| 7 | Procedimientos | /procedimientos | 🚧 En construcción | Módulo no implementado |
| 8 | Reportes | /reportes | 🚧 En construcción | Módulo no implementado |
| 9 | Configuración | /configuracion | ✅ Operativo | Datos empresa, gestión de usuarios |
| 10 | Movimientos | /movimientos | ⚠️ Roto | Redirige a /stock en lugar de mostrar log de movimientos |

---

## 5. Hallazgos de Seguridad

### 5.1 [CRÍTICO] Headers HTTP de seguridad ausentes

**Descripción:**
El servidor nginx no envía ningún header de seguridad estándar en sus respuestas HTTP.

**Headers faltantes:**

| Header | Riesgo | Descripción |
|--------|--------|-------------|
| `X-Frame-Options` | Clickjacking | Permite que la app sea embebida en iframes maliciosos |
| `X-Content-Type-Options` | MIME sniffing | El browser puede interpretar respuestas como tipos diferentes |
| `Content-Security-Policy` | XSS | Sin política declarativa de fuentes de contenido confiables |
| `Strict-Transport-Security` | Downgrade HTTP | Sin HSTS, posible degradación de HTTPS a HTTP |
| `Referrer-Policy` | Data leakage | La URL con datos puede filtrarse en headers Referer |

**Headers observados en respuesta:**
```http
content-encoding: gzip
content-type: text/html
date: Sat, 21 Feb 2026 17:05:33 GMT
etag: W/"6998a404-1e4"
last-modified: Fri, 20 Feb 2026 18:12:20 GMT
server: nginx/1.24.0 (Ubuntu)
```

**Remediación recomendada (nginx):**
```nginx
# Agregar en el bloque server{} del sitio
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';" always;
```

**Esfuerzo estimado:** 30 minutos
**Requiere reinicio:** `nginx -s reload`

---

### 5.2 [CRÍTICO] Versión de servidor expuesta

**Descripción:**
El header `server: nginx/1.24.0 (Ubuntu)` revela la versión exacta del servidor web y el sistema operativo. Esta información facilita ataques dirigidos a vulnerabilidades conocidas de esa versión específica.

**Remediación:**
```nginx
# En nginx.conf, dentro del bloque http{}
server_tokens off;
```

**Esfuerzo estimado:** 5 minutos

---

### 5.3 [MEDIO] Sin rate limiting en endpoint de login

**Descripción:**
No se detectó ningún mecanismo de protección ante intentos repetidos de autenticación (brute force). Un atacante podría intentar contraseñas de forma automatizada sin restricción.

**Remediación recomendada (nginx):**
```nginx
# Definir zona de límite (en bloque http{})
limit_req_zone $binary_remote_addr zone=login:10m rate=5r/m;

# Aplicar en el location del login
location /login {
    limit_req zone=login burst=3 nodelay;
    # ... resto de configuración
}
```

**Alternativa:** Implementar límite en la capa de aplicación (backend API).

---

## 6. Bugs Funcionales

### 6.1 Ruta /movimientos rota

**Descripción:**
El dashboard muestra un enlace "Ver todo →" en la sección "Últimos Movimientos" que apunta a `/movimientos`. Al navegar a esa URL, el sistema redirige automáticamente a `/stock` en lugar de mostrar un log de movimientos históricos.

**Comportamiento esperado:** Página con historial de entradas, salidas y transferencias de inventario
**Comportamiento actual:** Redirección a `/stock`
**Impacto:** El usuario no puede acceder al historial completo de movimientos desde el dashboard

---

### 6.2 Formulario de login con method="get"

**Descripción:**
El HTML del formulario de login tiene `method="get"` en lugar de `method="post"`. Aunque el submit es interceptado por JavaScript (comportamiento SPA), esto constituye una mala práctica: si el JS falla por cualquier razón, las credenciales serían enviadas como parámetros en la URL, quedando expuestas en:
- Logs del servidor nginx
- Historial del navegador
- Headers Referer de solicitudes posteriores

**Remediación:** Cambiar `method="get"` a `method="post"` en el formulario HTML del login.

---

## 7. Problemas de Datos

### 7.1 Productos críticos sin mínimos configurados

**Descripción:**
En el módulo de Stock se observan múltiples productos marcados con criticidad `CRIT` (alta criticidad clínica/quirúrgica) que tienen `stock=0` y `mínimo=0`, siendo mostrados con estado **"OK"**. El sistema calcula el estado en función del stock actual versus el mínimo definido, por lo que un mínimo de 0 impide que el sistema genere alertas de desabastecimiento.

**Ejemplos identificados:**
- Bisturí N°11 — área Quirúrgica — stock: 0, mínimo: 0 → OK
- Bisturí N°15 — área Quirúrgica — stock: 0, mínimo: 0 → OK
- Bupivacaína 0,5% — área Quirúrgica — stock: 0, mínimo: 0 → OK
- Bata quirúrgica estéril (L, S, XL) — área Quirúrgica — stock: 0, mínimo: 0 → OK

**Impacto:** Las alertas de stock crítico son inoperativas para estos productos, que por definición son los de mayor impacto en caso de desabastecimiento.

**Recomendación:** Campaña de configuración de mínimos para todos los productos marcados como CRIT. Considerar agregar validación en el sistema que alerte cuando un producto CRIT tenga mínimo=0.

---

### 7.2 Precios de referencia no registrados

**Descripción:**
La columna "Precio Ref." en el catálogo muestra `—` para la mayoría de los productos.

**Impacto:** Imposibilita:
- Valorización del inventario actual
- Estimación de costos en órdenes de compra
- Reportería financiera del módulo (cuando se implemente)

---

## 8. Oportunidades de Mejora Técnica

### 8.1 Code splitting (performance)

**Situación actual:** Toda la aplicación está compilada en un único archivo JavaScript. El usuario que accede al formulario de login descarga el código de configuración, reportes, proveedores, etc.

**Recomendación:** Implementar lazy loading por ruta con Vite + React Router (o equivalente). Ejemplo:
```javascript
// En lugar de importar directo:
const Reportes = lazy(() => import('./pages/Reportes'));
const Configuracion = lazy(() => import('./pages/Configuracion'));
```
Esto reduce significativamente el tiempo de carga inicial.

---

### 8.2 Cache headers para assets estáticos

**Situación actual:** Los assets en `/assets/` no tienen `Cache-Control` explícito.

**Recomendación:**
```nginx
location /assets/ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```
El hash en el nombre del archivo (`index-BCUBLQfa.js`) garantiza cache busting automático al deployar nueva versión.

---

### 8.3 Upload de logo en lugar de ruta manual

**Situación actual:** En Configuración, el logo se ingresa como texto con la ruta del archivo en el servidor (ej: `/logo-bhi.png`). Requiere acceso al servidor para actualizar el logo.

**Recomendación:** Implementar un input de tipo `file` con upload al servidor y almacenamiento en directorio público.

---

### 8.4 Meta tags SEO/accesibilidad

**Situación actual:** La app solo tiene el meta `viewport`. Sin `description`, sin `og:` tags, sin `lang` en el HTML.

**Recomendación mínima:**
```html
<html lang="es">
<meta name="description" content="Sistema de inventario Bravo Hair Institute">
<meta name="robots" content="noindex, nofollow"> <!-- si es interno -->
```

---

## 9. Aspectos Positivos

Los siguientes elementos reflejan buenas decisiones de diseño y desarrollo:

- **Flujo de solicitudes bien modelado:** El proceso Mis Solicitudes → Bandeja de Revisión → Bandeja de Aprobación → Historial refleja fielmente un flujo de aprobación organizacional real.
- **Nomenclatura de productos consistente:** El sistema de códigos (`QUI-AGU-005`, `MED-ANE-003`) sigue una convención área-categoría-correlativo coherente.
- **Separación por áreas:** La gestión de stock por área (Administrativa, Aseo/Operativo, Clínica, Quirúrgica) es apropiada para el contexto de una clínica.
- **HTTPS activo:** Las comunicaciones están cifradas.
- **0 errores de consola JavaScript:** La aplicación no genera errores en el browser durante la navegación normal.
- **Dashboard funcional:** KPIs relevantes (total productos, stock crítico, solicitudes pendientes) presentados de forma clara.

---

## 10. Resumen de Hallazgos

| # | Categoría | Severidad | Descripción | Esfuerzo |
|---|-----------|-----------|-------------|----------|
| 1 | Seguridad | 🔴 Crítico | Headers HTTP de seguridad ausentes | 30 min |
| 2 | Seguridad | 🔴 Crítico | Versión de nginx expuesta | 5 min |
| 3 | Seguridad | 🟠 Medio | Sin rate limiting en login | 1h |
| 4 | Funcional | 🟠 Medio | Ruta /movimientos rota | Bajo |
| 5 | Funcional | 🟠 Medio | Form login method="get" | Bajo |
| 6 | Datos | 🟡 Bajo | Productos CRIT sin mínimos configurados | Datos |
| 7 | Datos | 🟡 Bajo | Precios de referencia vacíos | Datos |
| 8 | Performance | 🔵 Mejora | Bundle único sin code splitting | Medio |
| 9 | Performance | 🔵 Mejora | Sin cache headers para assets | 15 min |
| 10 | UX | 🔵 Mejora | Logo por ruta en lugar de upload | Medio |
| 11 | SEO/Acceso | 🔵 Mejora | Meta tags mínimos ausentes | 15 min |

---

## 11. Plan de Remediación Sugerido

### Fase 1 — Inmediata (< 1 hora, solo configuración de servidor)
1. Agregar headers de seguridad en nginx
2. Desactivar `server_tokens`
3. Agregar cache headers para `/assets/`

### Fase 2 — Corto plazo (próximo sprint)
4. Corregir ruta `/movimientos`
5. Cambiar `method` del form de login a `post`
6. Agregar rate limiting en endpoint de login
7. Configurar mínimos de stock para productos CRIT

### Fase 3 — Mediano plazo
8. Implementar code splitting por ruta
9. Upload real para logo en Configuración
10. Completar módulos Procedimientos y Reportes
11. Agregar meta tags básicos

---

*Informe generado automáticamente por Korax (OpenClaw v2026.2.20) · Auditoría no intrusiva · Sin modificaciones al sistema auditado*
