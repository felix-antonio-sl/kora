---
title: "Manual de uso botón ClaveÚnica"
url: "https://wikiguias.digital.gob.cl/Manuales/Bot%C3%B3nCU"
category: "Plataformas Compartidas/Manuales de Uso"
tags: [{'tag': 'clave única', 'title': 'clave única'}, {'tag': 'cómo usar', 'title': 'cómo usar'}, {'tag': 'manuales', 'title': 'manuales'}, {'tag': 'integración', 'title': 'integración'}]
description: "¿Cómo implementar el botón de ClaveÚnica?, guía visual de anatomía y código. Puedes revisar el código HTML y su respectivo CSS."
updated_at: "2025-10-07T23:02:14.543Z"
---

ClaveÚnica es el mecanismo oficial de autenticación para personas naturales, que permite a millones de ciudadanos acceder a cientos de trámites y servicios que provee el Estado a través de sus plataformas electrónicas.

### [¶](#anatomía-del-botón-estándar) Anatomía del botón estándar

Se compone del isotipo ClaveÚnica acompañado de un texto y un fondo de color con espaciados que mejoran la accesibilidad y la percepción de botón para web.

![Estructura del botón ClaveÚnica](/imagenes/standarcu.png)

> **1 Icono ClaveÚnica:** Altura 24px, ancho 24px, color #FFFFF
>
> **2 Texto:** Tipografía Roboto, tamaño 1rem, peso: Bold, color #FFFFF
>
> **3 Contenedor:** color #0F69C4, bordes curvos 0

[¶](#dimensiones-del-botón-estándar) Dimensiones del botón estándar
-------------------------------------------------------------------

![Dimensiones en pixeles del botón](/imagenes/dimensionescu.png)

### [¶](#código-base) Código base

Se utiliza para acceder a una sesión que requiera una autenticación con ClaveÚnica donde sea el único método de autenticación del sitio web o plataforma. Para textos alternativos se recomienda `aria-label=`”Iniciar sesión con ClaveÚnica”.

- Elementos en Anchor
- Elementos en button
- Alternativas y recomendaciones
- Modo alto contraste
- Ancho Flexible
- CSS

Código tipo “Iniciar Sesión”

```
<!-- Código para visualizar botón oficial iniciar sesión con ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto"aria-hidden="true">Iniciar sesión</span>
                    </a>
```

Código tipo “ClaveÚnica”

```
  <!-- Código para visualizar botón oficial ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
                    <!--./ fin botón-->
```

Elementos para visualizar el botón oficial

```
<!-- Código con elemento button para visualizar botón oficial ClaveÚnica-->
                    <button class="btn-cu btn-m btn-color-estandar" type="button" id="#" aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </button>
                    <!--./ fin botón-->

                    <!-- Código con elemento button para visualizar botón oficial iniciar sesión con ClaveÚnica-->
                    <button class="btn-cu btn-m btn-color-estandar" type="button" id="#" aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </button>
                    <!--./ fin botón-->
```

Esquinas redondeadas 0

```
 <!-- Código para visualizar botón sin curvas iniciar sesión con ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-none" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </a>
                    <!--./ fin botón-->
                        
                    <!-- Código para visualizar botón sin curvas ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-none" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
                    <!--./ fin botón-->
```

Esquinas redondeadas medio

```
 <!-- Código para visualizar botón redondeado medio iniciar sesión con ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-middle" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </a>
                    <!--./ fin botón-->
                        
                    <!-- Código para visualizar botón redondeado medio ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-middle" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
                    <!--./ fin botón-->
```

Esquinas redondeadas full

```
<!-- Código para visualizar botón redondeado full iniciar sesión con ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-full" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </a>
                    <!--./ fin botón-->
                        
                    <!-- Código para visualizar botón redondeado full ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar rounded-full" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
                    <!--./ fin botón-->
```

```
<!-- Código para visualizar botón altoContraste iniciar sesión con ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-highContrast" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </a>
                    <!--./ fin botón-->
                        
                    <!-- Código para visualizar botón altoContraste ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-highContrast" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
                    <!--./ fin botón-->
```

```
<a class="btn-cu btn-m  btn-color-estandar btn-fw" href="#"
                        aria-label="Iniciar sesión con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">Iniciar sesión</span>
                    </a>
                    <!--./ fin botón-->
                </div>
                <div class="d-flex align-items-center">     
                    <!-- Código para visualizar botón altoContraste ClaveÚnica-->
                    <a class="btn-cu btn-m  btn-color-estandar btn-fw" href="#"
                        aria-label="Continuar con ClaveÚnica">
                        <span class="cl-claveunica" aria-hidden="true"></span>
                        <span class="texto" aria-hidden="true">ClaveÚnica</span>
                    </a>
```

Estilos gráficos para el botón de ClaveÚnica.V 2.0

```
/* Boton estilo de base */
.btn-cu {
    display: flex;
    justify-content: center;
    font-family: "Roboto", sans-serif;
    font-weight:bold;
    text-align: center;
    text-decoration:none;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border-radius: 0;
    border:0;
}
.btn-cu:hover{
    text-decoration: none;
}

/*Icono ClaveÚnica*/
.btn-cu .cl-claveunica {
    text-indent: -9999px;
    background: url(../icon/cu-blanco.svg);
    /* Esta URL debe ser modificada según donde 
        quede disponible el archivo */
}
/*Texto ClaveÚnica*/
.btn-cu .text {
    padding-left: 4px;
    text-decoration:none;
    font-size: 1rem;
    text-rendering:geometricPrecision;
}
/*si no tienes disponible unidades rem usa px*/
.btn-cu .text-px{
    font-size: 16px;
    text-decoration: none;
    padding-left:4px;
    text-rendering: optimizeLegibility;
}
/* Color Estandar */
.btn-cu.btn-color-estandar {
    background-color: #0F69C4;
    color: #FFF;
}
.btn-cu.btn-color-estandar:hover {
    background-color: #0B4E91;
    color: #FFF;
}

.btn-cu.btn-color-estandar:active {
    background-color: #07305A;
    color: #FFF;
}

.btn-cu.btn-color-estandar:focus {
    background-color: #0B4E91;
    color: #FFF;
    outline: 4px solid #FFBE5C;
    outline-offset: 0;
}

/* Tamaño M */
.btn-cu.btn-m {
    width:fit-content;
    min-height:48x;
    padding: 8px 14px 8px 14px !important;
    font-size: 16px;
    line-height:2rem;
}

.btn-cu.btn-m .cl-claveunica {
    width: 24px;
    height: 24px;
    background-size: 24px 24px;
    margin:auto 4px auto 0px;
}

/*Bordes redondeados*/
.btn-cu.rounded-none{
    border-radius: 0%;
}
.btn-cu.rounded-middle{
    border-radius: 4px 4px;
}
.btn-cu.rounded-full{
    border-radius:99px 99px;
}

/*Alto contraste o dark mode*/
.btn-cu.btn-color-highContrast {
    background-color: #625AF6;
    color: #FFF;
}
.btn-cu.btn-color-highContrast:hover {
    background-color: #4943B6;
    color: #FFF;
}

.btn-cu.btn-color-highContrast:active {
    background-color: #2D2971;
    color: #FFF;
}

.btn-cu.btn-color-highContrast:focus {
    background-color: #4943B6;
    color: #FFF;
    outline: 4px solid rgba(216,215,250,1);
    outline-offset: 0;
}

/* Tamaño fluid-width */
.btn-cu.btn-fw {
    max-width: 550px;
    width: 100%;
    display: flex;
    justify-content: center;
}
```

[¶](#consideraciones-generales) Consideraciones generales
---------------------------------------------------------

> **Recomendaciones**  
> Se recomienda implementar un sólo boton de ClaveÚnica en los accesos principales a un sitio web.  
> El botón de autenticación de ClaveÚnica no debería repetirse con el boton de Call to Action del sitio

#### [¶](#usa-correctamente-la-marca-claveúnica) Usa correctamente la marca ClaveÚnica

Debe ir con mayúscula las letras C y U  
ClaveÚnica siempre va junto, es una marca registrada

![correcto001.png](/imagenes/correcto001.png)

### [¶](#redundancia-de-contenidos) Redundancia de contenidos

Evita usar textos "ingresa con tu ClaveÚnica", acompañado del botón que dice "ClaveÚnica". En estos casos deberías usar el texto "Inicia sesión"  
![correcto002.png](/imagenes/correcto002.png)

[¶](#restricciones-de-uso) Restricciones de uso
-----------------------------------------------

> Además de las restricciones visuales, el botón **no debe enlazar** a otros tipos de autenticación que no sea ClaveÚnica, si tu sitio o servicio tiene diferentes accesos, puedes utilizar un menú secundario que tenga los enlaces de autenticación

#### [¶](#diseños-incorrectos) Diseños incorrectos

![incorrecto001_cu.png](/imagenes/incorrecto001_cu.png)

#### [¶](#uso-incorrecto-de-espaciados) Uso incorrecto de espaciados

![incorrecto_espaciado.png](/imagenes/incorrecto_espaciado.png)

[¶](#canal-de-youtube) Canal de Youtube
---------------------------------------

También te recomendamos visitar nuestro canal de [Youtube](https://www.youtube.com/watch?v=2D5XAiEveqc&list=PLUwB5Xct9D9cvDscnrC14cm8P1qrV2MI6)