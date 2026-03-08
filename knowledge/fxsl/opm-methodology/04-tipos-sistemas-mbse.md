---
_manifest:
  urn: "urn:fxsl:kb:opm-tipos-sistemas-mbse"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-06"
    source: "opm_youtube.md + OPM version felix.md + ISO 19450"
version: "1.0.1"
status: published
tags: [opm, iso19450, mbse, tipos-sistemas, artificial, natural, social, sociotecnico, pdr, integracion-virtual]
lang: es
---

# OPM — Tipos de Sistemas y MBSE

Clasificacion de sistemas modelables con OPM y su integracion en Ingenieria de Sistemas Basada en Modelos.

---

## Comparacion de Tipos de Sistemas

| Componente SD | Artificial | Natural | Social | Socio-tecnico |
|---------------|-----------|---------|--------|---------------|
| Proposito | Si (beneficiarios + beneficio) | No (→ Resultado/Outcome) | Si | Si |
| Funcion principal | Si | Si | Si | Si |
| Habilitadores | Agentes + Instrumentos | Solo Instrumentos (si no hay personas) | Agentes + Instrumentos | Agentes + Instrumentos |
| Entorno | Si | Si | Si | Si |
| Ocurrencia del problema | Si | No | Si | Si |

---

## Sistemas Artificiales (Tecnologicos)

Diseñados por humanos para resolver un problema especifico.
5 componentes SD. Proposito siempre presente. Ocurrencia del problema siempre presente.

**Ejemplos:** sistema de fabricacion de cafe, coche electrico, sistema de control de trafico aereo, sistema de compra de boletos de avion, sistema de fabricacion de coches electricos basado en robotica, sistema de gestion de equipaje.

**Patron SD:**
- Proceso principal → verbo gerundio que describe transformacion central.
- Objeto principal (operando) → objeto cuyo estado cambia de problematico a satisfactorio.
- Beneficiarios → quienes obtienen valor del estado satisfactorio.
- Ocurrencia del problema → proceso ambiental que causa estado problematico inicial.

---

## Sistemas Naturales

No diseñados por humanos. Sin intencion ni proposito de diseno.
SD con 3 componentes: Resultado (Outcome), Funcion Principal, Habilitadores.

**Resultado (Outcome):** puede ser beneficioso o perjudicial (detrimental) para grupo afectado. No es "proposito" — no hay intencion.

**Ejemplos:** sistema de tormenta tropical, crecimiento de arbol.

**Patron SD tormenta:**
- Proceso principal: `Storm Forming`.
- Objeto principal: `Surrounding Atmosphere` cambia de `dry` a `rainy`.
- Instrumento: `Warm Ocean Water` (habilita formacion sin ser transformado).
- Entorno: `Ocean`, `Earth's Atmosphere`.
- Sin agentes (si no hay personas involucradas).
- Sin ocurrencia del problema.

---

## Sistemas Sociales

Subcategoria de artificiales. Creados por humanos con proposito social.
SD con 5 componentes (igual que artificiales).

**Agentes:** personas con roles especificos (organizador, ujier, participante).
**Instrumentos:** equipamiento (mesas, sillas, equipo audiovisual, plataformas digitales).
**Entorno:** puede incluir clima, condiciones externas.

**Ejemplo SD conferencia:**
- Proceso: `Conference Managing`.
- Beneficiario: `Company Stakeholder Group` (propietarios, inversores, proveedores, clientes, trabajadores).
- Proposito: mejorar `Business Success` de `problematic` a `improved`.
- Agentes: `Organizer`, `Usher Group`.
- Instrumentos: `Meeting Equipment Set`.
- Ocurrencia del problema: proceso ambiental `Business Decline`.

---

## Sistemas Socio-Tecnicos

Artificiales que integran aspectos tecnologicos y sociales.
SD con 5 componentes.

**Ejemplo SD gestion identidad profesional online:**
- Proceso: `Professional Identity Managing`.
- Beneficiario: `User` → atributo `Professional Success` de `current` a `improved`.
- Instrumento: `Professional Identity Management System`.
- Instrumento ambiental: `Internet Connection`.
- Agentes: `User`, `Other Users Group`.
- Ocurrencia del problema: gestion de identidad solo offline ya no viable.

---

## Sistemas Socio-Tecnicos Complejos

Multitud de componentes que interactuan de formas multiples. Requieren colaboracion de personas con experticia diversa.
Modelado OPM obligatorio para evitar sistemas "desordenados, incompletos o poco claros".

**Ejemplos:** transporte, comunicacion, educacion, defensa, smartphone (desarrollado por decenas de miles de personas en cientos de empresas).

---

## Aplicaciones Reportadas de OPM

Dominios de uso explicitamente mencionados en el corpus fuente:
- Electrodomesticos de proxima generacion (refrigeradores, lavavajillas).
- Sistemas de aeronaves comerciales.
- Gestion del conocimiento en procesos de negocio.
- Control vehicular end-to-end en industria automotriz.
- Diseño y operacion de brazos roboticos para la Estacion Espacial Internacional.
- Diseño de nuevos productos de seguros.
- Investigacion en biologia molecular.

---

## MBSE — Model-Based Systems Engineering

**Proposito:** usar modelos conceptuales para disenar y desarrollar sistemas complejos. Mejor control del proceso de ingenieria.

**Ventajas sobre enfoque tradicional (texto):**
- Visualizacion y comprension del sistema.
- Prevencion de errores y omisiones.
- Consenso dentro del equipo de ingenieria.
- Verificacion y validacion formal.

**Limitaciones del enfoque tradicional:** basado en texto, sin lenguaje estandarizado, sin caracteristicas avanzadas de modelado → verificacion/validacion formal imposible → valor entregado potencialmente disminuido.

**Integracion OPM + OPCloud en MBSE:** sirven como infraestructura y herramientas para creacion de modelos en el proceso de ingenieria de sistemas.

---

## Generacion de Conceptos de Solucion Alternativos

Minimo 3 modelos conceptuales distintos, cada uno con nivel adicional de detalle al modelo de requisitos.

**Elementos requeridos:**
1. **Pensamiento creativo:** perspectiva holistica, no enfrascarse en detalles.
2. **Destilacion del concepto central:** principio fisico o logico que subyace a la arquitectura. Ej. para cruzar un rio: "pasar por encima" (puente, teleferico) vs "pasar a traves" (ferry, submarino).
3. **Explicitar supuestos implicitos:** cuestionar lo que se da por sentado. Ej. ¿Es necesario cruzar directamente? ¿Es necesario cruzar en absoluto?

**Concepto:** idea basada en principio fisico o logico que subyace a arquitectura de sistema de solucion.

---

## PDR — Preliminary Design Review

Revision de diseno tras modelado conceptual y diseno de alto nivel del sistema seleccionado.

| Seccion PDR | Contenido |
|-------------|-----------|
| Portada | Autores, afiliaciones, nombre e imagen del sistema |
| Problema | Necesidad del sistema con modelo de problema |
| Proposito | Funcion principal con OPD de nivel superior |
| Supuestos y restricciones | Del sistema y de su desarrollo |
| Soluciones alternativas | Conceptos, modelos, criterios de evaluacion y comparacion |
| Solucion seleccionada y justificada | Con modelo OPM completo |
| Estimaciones de costos | Todo el ciclo de vida (concepto → retiro) |
| Cronograma | Hitos, fechas, pagos del proyecto |
| Riesgos y mitigacion | Modos de falla, prevencion y recuperacion (monitoreo, redundancia) |

**Analisis de riesgos basado en modelos:** identificar modos de falla e incluirlos en el modelo OPM con mecanismos de prevencion/recuperacion y sus costos.

---

## OPM como Blueprint Comun

En diseno detallado de sistemas complejos multi-disciplinarios, el modelo OPM sirve como especificacion neutral y plan comun.
- Contiene especificaciones de interfaces en lenguaje independiente de disciplina.
- Permite que todas las areas se relacionen y confien en el.
- Modelos detallados tipicamente: 5-10 niveles de detalle.

---

## Integracion Virtual

Integracion de modelos conceptuales de componentes hardware con modulos de software ejecutables.
- Hardware: permanece como modelos conceptuales OPM.
- Software: codigo ejecutable real (generado manual o automaticamente).
- En integracion virtual: modulos de software controlan virtualmente modelos de hardware via simulacion → prueba de software real con modelos de componentes hardware.
