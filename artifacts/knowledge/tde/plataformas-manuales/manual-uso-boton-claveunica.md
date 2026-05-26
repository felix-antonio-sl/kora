---
_manifest:
  urn: urn:tde:kb:manual-uso-boton-claveunica
  provenance:
    source: https://wikiguias.digital.gob.cl/Manuales/Bot%C3%B3nCU
version: 1.0.0
status: published
tags:
- tde
- plataformas-manuales
- clave-única
- cómo-usar
- manuales
- integración
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:manual-uso-boton-claveunica
---

# Manual de uso: Botón ClaveÚnica

## Anatomía del botón estándar

Componentes:

| Elemento | Especificación |
|----------|---------------|
| Icono ClaveÚnica | 24×24px, color `#FFFFFF` |
| Texto | Tipografía Roboto, 1rem, Bold, color `#FFFFFF` |
| Contenedor | Color `#0F69C4`, bordes curvos 0 |

## Código base

Uso: autenticación exclusiva con ClaveÚnica. Atributo recomendado: `aria-label="Iniciar sesión con ClaveÚnica"`.

### Elemento `<a>` — tipo "Iniciar Sesión"

```html
<a class="btn-cu btn-m btn-color-estandar" href="#"
 aria-label="Iniciar sesión con ClaveÚnica">
 <span class="cl-claveunica" aria-hidden="true"></span>
 <span class="texto" aria-hidden="true">Iniciar sesión</span>
</a>
```

### Elemento `<a>` — tipo "ClaveÚnica"

```html
<a class="btn-cu btn-m btn-color-estandar" href="#"
 aria-label="Continuar con ClaveÚnica">
 <span class="cl-claveunica" aria-hidden="true"></span>
 <span class="texto" aria-hidden="true">ClaveÚnica</span>
</a>
```

### Elemento `<button>`

```html
<button class="btn-cu btn-m btn-color-estandar" type="button" id="#"
 aria-label="Continuar con ClaveÚnica">
 <span class="cl-claveunica" aria-hidden="true"></span>
 <span class="texto" aria-hidden="true">ClaveÚnica</span>
</button>
```

### Variantes de bordes

| Variante | Clase adicional |
|----------|----------------|
| Sin curvas | `rounded-none` |
| Redondeado medio | `rounded-middle` |
| Redondeado full | `rounded-full` |

### Alto contraste / dark mode

Reemplazar `btn-color-estandar` por `btn-color-highContrast`.

### Ancho flexible

Agregar clase `btn-fw` (max-width: 550px, width: 100%).

## CSS completo (v2.0)

```css
/* Base */
.btn-cu {
 display: flex;
 justify-content: center;
 font-family: "Roboto", sans-serif;
 font-weight: bold;
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
 /* Ajustar URL según ubicación del archivo */
}

/* Texto */
.btn-cu .text {
 padding-left: 4px;
 font-size: 1rem;
 text-rendering: geometricPrecision;
}
.btn-cu .text-px {
 font-size: 16px;
 padding-left: 4px;
 text-rendering: optimizeLegibility;
}

/* Color estándar */
.btn-cu.btn-color-estandar { background-color: #0F69C4; color: #FFF; }
.btn-cu.btn-color-estandar:hover { background-color: #0B4E91; color: #FFF; }
.btn-cu.btn-color-estandar:active { background-color: #07305A; color: #FFF; }
.btn-cu.btn-color-estandar:focus { background-color: #0B4E91; color: #FFF;
 outline: 4px solid #FFBE5C; outline-offset: 0; }

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
 margin: auto 4px auto 0;
}

/* Bordes redondeados */
.btn-cu.rounded-none { border-radius: 0; }
.btn-cu.rounded-middle { border-radius: 4px; }
.btn-cu.rounded-full { border-radius: 99px; }

/* Alto contraste */
.btn-cu.btn-color-highContrast { background-color: #625AF6; color: #FFF; }
.btn-cu.btn-color-highContrast:hover { background-color: #4943B6; color: #FFF; }
.btn-cu.btn-color-highContrast:active { background-color: #2D2971; color: #FFF; }
.btn-cu.btn-color-highContrast:focus { background-color: #4943B6; color: #FFF;
 outline: 4px solid rgba(216,215,250,1); outline-offset: 0; }

/* Ancho flexible */
.btn-cu.btn-fw { max-width: 550px; width: 100%; display: flex; justify-content: center; }
```

## Consideraciones generales

- Implementar un solo botón ClaveÚnica por acceso principal al sitio.
- El botón de autenticación no debe duplicarse con el Call to Action del sitio.
- Escritura correcta de la marca: **ClaveÚnica** (C y U en mayúscula, siempre junto).
- Evitar texto redundante: si el botón dice "ClaveÚnica", no agregar "ingresa con tu ClaveÚnica"; usar "Inicia sesión" en su lugar.

## Restricciones de uso

- El botón **no debe enlazar** a métodos de autenticación distintos de ClaveÚnica.
- Si el sitio tiene múltiples accesos, usar un menú secundario con los enlaces de autenticación.
- Prohibido: espaciados incorrectos, modificación del isotipo, mezcla visual con otros métodos de acceso en el mismo botón.
