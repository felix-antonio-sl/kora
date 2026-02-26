---
_manifest:
  urn: "urn:tde:kb:manual-claveunica-boton"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/Bot%C3%B3nCU"
version: 1.0.0
status: published
tags: [tde, plataforma, claveunica, botón, diseño, ui, accesibilidad, css, html]
lang: es
---

# Manual de uso botón ClaveÚnica

ClaveÚnica = mecanismo oficial de autenticación para personas naturales. Permite acceder a cientos de trámites y servicios del Estado vía plataformas electrónicas.

## Anatomía del botón estándar

Composición: isotipo ClaveÚnica + texto + fondo de color con espaciados de accesibilidad.

| Elemento | Especificación |
|----------|---------------|
| Icono ClaveÚnica | 24×24 px, color `#FFFFFF` |
| Texto | Tipografía Roboto, 1rem, Bold, color `#FFFFFF` |
| Contenedor | Color `#0F69C4`, bordes curvos 0 |

## Código base

Botón para autenticación donde ClaveÚnica es el único método. `aria-label="Iniciar sesión con ClaveÚnica"` recomendado para textos alternativos.

### Variante "Iniciar Sesión" (anchor)

```html
<a class="btn-cu btn-m btn-color-estandar" href="#"
   aria-label="Iniciar sesión con ClaveÚnica">
  <span class="cl-claveunica" aria-hidden="true"></span>
  <span class="texto" aria-hidden="true">Iniciar sesión</span>
</a>
```

### Variante "ClaveÚnica" (anchor)

```html
<a class="btn-cu btn-m btn-color-estandar" href="#"
   aria-label="Continuar con ClaveÚnica">
  <span class="cl-claveunica" aria-hidden="true"></span>
  <span class="texto" aria-hidden="true">ClaveÚnica</span>
</a>
```

### Variante button

```html
<button class="btn-cu btn-m btn-color-estandar" type="button" id="#"
        aria-label="Continuar con ClaveÚnica">
  <span class="cl-claveunica" aria-hidden="true"></span>
  <span class="texto" aria-hidden="true">ClaveÚnica</span>
</button>
```

## Variantes de esquinas

| Variante | Clase CSS adicional |
|----------|-------------------|
| Sin curvas (default) | `rounded-none` |
| Redondeado medio | `rounded-middle` |
| Redondeado full | `rounded-full` |

## Alto contraste / dark mode

Clase: `btn-color-highContrast`

| Estado | Color fondo |
|--------|------------|
| Default | `#625AF6` |
| Hover | `#4943B6` |
| Active | `#2D2971` |
| Focus | `#4943B6` + outline `rgba(216,215,250,1)` |

## Ancho flexible

Clase: `btn-fw` → `max-width: 550px; width: 100%`

## CSS completo (v2.0)

```css
/* Base */
.btn-cu {
  display: flex;
  justify-content: center;
  font-family: "Roboto", sans-serif;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  user-select: none;
  border-radius: 0;
  border: 0;
}
.btn-cu:hover { text-decoration: none; }

/* Icono */
.btn-cu .cl-claveunica {
  text-indent: -9999px;
  background: url(../icon/cu-blanco.svg);
  /* URL debe modificarse según ubicación del archivo */
}

/* Texto */
.btn-cu .text {
  padding-left: 4px;
  text-decoration: none;
  font-size: 1rem;
  text-rendering: geometricPrecision;
}
.btn-cu .text-px {
  font-size: 16px;
  text-decoration: none;
  padding-left: 4px;
  text-rendering: optimizeLegibility;
}

/* Color estándar */
.btn-cu.btn-color-estandar { background-color: #0F69C4; color: #FFF; }
.btn-cu.btn-color-estandar:hover { background-color: #0B4E91; color: #FFF; }
.btn-cu.btn-color-estandar:active { background-color: #07305A; color: #FFF; }
.btn-cu.btn-color-estandar:focus {
  background-color: #0B4E91; color: #FFF;
  outline: 4px solid #FFBE5C; outline-offset: 0;
}

/* Tamaño M */
.btn-cu.btn-m {
  width: fit-content;
  min-height: 48px;
  padding: 8px 14px !important;
  font-size: 16px;
  line-height: 2rem;
}
.btn-cu.btn-m .cl-claveunica {
  width: 24px; height: 24px;
  background-size: 24px 24px;
  margin: auto 4px auto 0px;
}

/* Esquinas */
.btn-cu.rounded-none { border-radius: 0%; }
.btn-cu.rounded-middle { border-radius: 4px; }
.btn-cu.rounded-full { border-radius: 99px; }

/* Alto contraste */
.btn-cu.btn-color-highContrast { background-color: #625AF6; color: #FFF; }
.btn-cu.btn-color-highContrast:hover { background-color: #4943B6; color: #FFF; }
.btn-cu.btn-color-highContrast:active { background-color: #2D2971; color: #FFF; }
.btn-cu.btn-color-highContrast:focus {
  background-color: #4943B6; color: #FFF;
  outline: 4px solid rgba(216,215,250,1); outline-offset: 0;
}

/* Ancho flexible */
.btn-cu.btn-fw {
  max-width: 550px; width: 100%;
  display: flex; justify-content: center;
}
```

## Consideraciones generales

### Recomendaciones

- Implementar un solo botón ClaveÚnica en accesos principales del sitio web
- No repetir botón ClaveÚnica con botón Call to Action del sitio

### Uso correcto de marca

- Mayúsculas en C y U: **ClaveÚnica** (siempre junto, marca registrada)

### Redundancia de contenidos

- Evitar texto "ingresa con tu ClaveÚnica" acompañado de botón que dice "ClaveÚnica"
- En esos casos usar texto "Inicia sesión"

## Restricciones de uso

- Botón NO DEBE enlazar a otros tipos de autenticación que no sea ClaveÚnica
- Si el sitio tiene diferentes accesos → menú secundario con enlaces de autenticación

### Diseños incorrectos

- No modificar colores, tipografía ni proporciones del botón estándar
- No alterar espaciados definidos

## Recursos

- [Canal YouTube ClaveÚnica](https://www.youtube.com/watch?v=2D5XAiEveqc&list=PLUwB5Xct9D9cvDscnrC14cm8P1qrV2MI6)
