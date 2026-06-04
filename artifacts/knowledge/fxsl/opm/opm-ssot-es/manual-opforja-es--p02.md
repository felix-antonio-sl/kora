---
_manifest:
  urn: urn:fxsl:kb:manual-opforja-es-p02
  provenance:
    created_by: deep-opm-pro/codex + custodio KORA
    created_at: '2026-06-04'
    source: Manual operativo derivado del corpus OPM/Forja SSOT ES vigente. Parte
      desde reglas-opm-estrictas-es v1.2.1, metodologia-forja-es v1.4.4, spec-forja-opd-es
      v1.0.3, spec-forja-opl-es v1.1.3, opm-categorial-es v1.2.4 y modelamiento-opm
      v1.5.0. Iniciado en REVIEW y promovido a productivo como manual v0.1.0 con
      secciones de estabilidad editorial explícita porque la implementación de opforja/deep-opm-pro
      sigue evolucionando.
version: 0.1.0
status: publicado
source_base: reglas-opm-estrictas-es.md v1.2.1; metodologia-forja-es.md v1.4.4; spec-forja-opd-es.md
  v1.0.3; spec-forja-opl-es.md v1.1.3; opm-categorial-es.md v1.2.4; modelamiento-opm
  v1.5.0.
derived_from:
- urn:fxsl:kb:reglas-opm-estrictas-es
- urn:fxsl:kb:metodologia-forja-opm-es
- urn:fxsl:kb:spec-forja-opd-es
- urn:fxsl:kb:spec-forja-opl-es
- urn:fxsl:kb:opm-categorial-es
scope: Manual operativo de uso de opforja para modeladores, agentes y mantenedores.
  Enseña flujo, criterio, lectura de OPD/OPL, validación y uso práctico sin duplicar
  el canon prescriptivo ni las specs modales. Las secciones dependientes de interfaz
  se tratan como borrador vivo hasta estabilizar la app.
tags:
- opm
- opforja
- manual
- guia-operativa
- modelamiento
- opd
- opl
- deep-opm-pro
- ssot-forja
lang: es
extensions:
  kora:
    family: note
    lifecycle_note: publicado v0.1.0; mantener secciones dependientes de interfaz como vivo o pendiente de evidencia hasta sincronización con la app.
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:manual-opforja-es
relations:
  depends:
  - urn:fxsl:kb:reglas-opm-estrictas-es
  - urn:fxsl:kb:metodologia-forja-opm-es
  - urn:fxsl:kb:spec-forja-opd-es
  - urn:fxsl:kb:spec-forja-opl-es
  cites:
  - urn:fxsl:kb:opm-categorial-es
  - urn:fxsl:kb:opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
  - urn:fxsl:kb:manual-metodologico-opm-es
---

# Manual de opforja - Parte 02

## 5. Refinar sin romper el modelo

**Estado:** estable.

Refinar es hacer visible una estructura interna que ya estaba implicada por el
modelo, no cambiar la función sin decirlo. Cada refinamiento debe declarar:

- qué cosa o proceso se refina,
- qué pregunta responde,
- qué frontera conserva,
- qué enlaces se distribuyen,
- qué hechos se expresan o se suprimen,
- qué OPL confirma la equivalencia.

### 5.1 In-zoom y frontera

Al descomponer un proceso, los subprocesos deben explicar cómo se realiza el
proceso padre. La firma de frontera del proceso abstracto se preserva. Si el
hijo necesita un nuevo input o produce un nuevo output neto, revisar si el padre
estaba incompleto o si se está modelando otra función.

### 5.2 Unfold y estructura

Al desplegar una cosa, las partes, rasgos, especializaciones o instancias deben
usar el enlace estructural correcto. No todo detalle interno es parte; algunos
son atributos exhibidos, tipos especializados o instancias clasificadas.

### 5.3 Estados expresados y suprimidos

La supresión de estados es una decisión de vista, no una eliminación del modelo.
Debe mantenerse claro qué estados existen canónicamente y cuáles están ocultos
en una aparición para controlar altitud.

## 6. Reglas prácticas de OPD

**Estado:** estable como criterio; vivo en detalles visuales.

El OPD comunica con geometría. Los detalles exactos de glifos, marcadores y
tokens visuales viven en `spec-forja-opd-es`; este manual conserva solo la
lectura práctica.

| Elemento | Lectura práctica |
| --- | --- |
| Rectángulo | Objeto. Existe y puede portar estados. |
| Elipse | Proceso. Transforma y puede refinarse por in-zoom. |
| Rountangle interno | Estado de un objeto. |
| Sombra | Esencia física cuando está visible. |
| Contorno discontinuo | Afiliación ambiental. |
| Enlace transformador | El proceso consume, produce o cambia algo. |
| Piruleta | Habilitación: agente o instrumento. |
| Triángulo estructural | Agregación, exhibición, generalización o clasificación según glifo. |
| Rayo | Invocación entre procesos. |
| `e` / `c` | Evento o condición sobre enlace permitido. |

Regla de lectura: si un elemento visual no puedes traducirlo a una oración OPL
clara, no lo trates como hecho terminado.

## 7. Reglas prácticas de OPL

**Estado:** estable como criterio; vivo en parser/edición.

OPL-ES es lenguaje natural controlado. Su valor está en ser legible por humanos
y suficientemente formal para roundtrip.

Principios prácticos:

- una oración atómica expresa un hecho,
- los nombres canónicos deben ser singulares y específicos,
- esencia y afiliación son declaraciones de cosa,
- consumo, resultado y efecto no son sinónimos,
- agente e instrumento usan predicados distintos,
- la prosa compuesta solo coordina hechos elegibles,
- una oración no parseable puede servir como comentario humano, pero no como
 hecho canónico importable.

El parser no es corrector literario. Si el operador escribe una frase ambigua,
opforja debe rechazarla, suspenderla o pedir aclaración según la política de la
spec OPL; no debe inventar el hecho.

## 8. Validación y diagnóstico

**Estado:** estable.

Validar en opforja combina reglas, método y lectura humana:

1. Correr validación de hechos y severidades.
2. Revisar checklist OPD<->OPL.
3. Leer el OPL completo con el operador.
4. Revisar frontera y firma de procesos refinados.
5. Revisar densidad y legibilidad de cada OPD.
6. Separar errores de modelo, advertencias, deuda de herramienta y brechas de
 canon.
7. Declarar si el modelo está bien formado, representa y sirve.

### 8.1 Diagnóstico honesto

Un diagnóstico debe decir qué se rompe y en qué plano:

- **Validez:** regla estricta violada.
- **Modalidad OPD:** realización visual incorrecta.
- **Modalidad OPL:** oración, parseo o roundtrip incorrecto.
- **Método:** modelo conforme pero mal construido o insuficiente.
- **Herramienta:** capacidad no implementada, UI transitoria o GAP.
- **Dominio:** falta evidencia del operador.

## 9. Patrones de modelado

**Estado:** pendiente de evidencia para catálogo completo.

Esta sección reunirá patrones probados que ya existen como lecciones Forja o
como apéndices OPL. En v0.1 se conserva el índice de patrones candidatos:

- sistemas sociotécnicos,
- agente, rol y autoridad,
- decisión y supervisión humana,
- interfaz crítica,
- control loop,
- estados ortogonales,
- composición por interfaz,
- configuración y tradeoffs,
- digital twin y simulación conceptual.

Cada patrón publicable debe incluir: intención, cuándo usarlo, cuándo no usarlo,
OPD mínimo, OPL esperado, reglas propietarias, brechas conocidas y ejemplo.

## 10. Ejemplo end-to-end

**Estado:** pendiente de evidencia.

El ejemplo principal debe ser pequeño, completo y verificable. Debe recorrer:

1. enunciado inicial,
2. detección de barro,
3. preguntas de aclaración,
4. SD inicial,
5. OPL atómica,
6. refinamiento,
7. validación tripartita,
8. export o bundle,
9. errores intencionales y correcciones.

El ejemplo no debe depender de conocimiento experto de dominio. Su función es
enseñar opforja, no enseñar medicina, logística o software.

## 11. Apéndices

**Estado:** pendiente de expansión.

### Apéndice A — Glosario opforja

Debe contener términos de uso operativo que no dupliquen el glosario OPM base:
barro, firma de frontera, realización hermana, aparición, display-vs-canónico,
bundle, roundtrip, gate, GAP.

### Apéndice B — Cheatsheet OPD

Resumen de lectura visual con enlaces a `spec-forja-opd-es`.

### Apéndice C — Cheatsheet OPL

Resumen de plantillas frecuentes con enlaces a `spec-forja-opl-es`.

### Apéndice D — Mapa de reglas a specs canónicas

Tabla de routing: si el problema es de validez, método, OPD, OPL, formal o app.

### Apéndice E — Índice de detectores/checkers

Índice operativo de validadores y severidades cuando la implementación los
exponga de forma estable.

## Bitácora del manual

| Fecha | Versión | Cambio |
| --- | --- | --- |
| 2026-06-04 | 0.1.0 | Creación, promoción a productivo y particionado en dos shards. Fija contrato editorial, TOC, capítulos estables iniciales, secciones vivas y ranuras para evidencia UI/casos. |
