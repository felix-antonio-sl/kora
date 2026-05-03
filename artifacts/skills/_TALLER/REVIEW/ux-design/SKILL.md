---
_manifest:
  urn: "urn:kora:artefacto:ux-design"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "Migracion desde artifacts/skills/_TALLER/INBOX/ux-design/SKILL.md (legacy skill-overlay v1) a shape unified autoria-spec v1.2"
version: "1.0.0"
status: borrador
nombre: ux-design
descripcion: "Evalua y mejora la experiencia de usuario aplicando heuristicas de Nielsen, flujos de tarea, accesibilidad WCAG 2.2 AA, arquitectura de informacion y patrones UX institucionales. Usar al auditar UX, disenar formularios, mejorar navegacion o revisar accesibilidad."
tags: [ux, usabilidad, accesibilidad, wcag, disciplina]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 2, 2, 1, 0]
    presentacion: estado-primario
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, gemini]
    nivel_prescripcion: medio
    conocimiento_permitido: []
    componible_con: []
artefacto:
  perfil:
    descripcion: "Habilidad UX para auditar y disenar flujos, formularios, navegacion y accesibilidad usando heuristicas y patrones verificables."
    dominio:
      - experiencia de usuario
      - accesibilidad WCAG
      - arquitectura de informacion
    salidas:
      - auditorias UX
      - flujos de usuario
      - recomendaciones accionables por componente
  interfaz:
    herramientas: []
    permisos:
      allow: []
      deny: []
---

# UX Design

Skill para evaluar, disenar y mejorar la experiencia de usuario en interfaces web. Aplica principios de usabilidad, accesibilidad y arquitectura de informacion con enfoque en aplicaciones institucionales y gobierno digital.

## Objetivo

Producir audits UX con hallazgos trazables a heuristicas formales (Nielsen, WCAG 2.2 AA, ley de Hick, ley de Fitts) y entregar mejoras accionables por componente.

## Cuando Usar

- Auditar UX de pagina o componente existente.
- Disenar formularios, flujos de tarea o navegacion.
- Revisar accesibilidad WCAG 2.2 AA.
- Evaluar carga cognitiva, densidad de informacion o estados vacios.
- Crear user flows o mapas de interaccion.

### Distincion con skills relacionadas

| Esta skill (ux-design) | graphic-design | frontend-design |
|-------------------------|-----------------|-----------------|
| Como se USA | QUE se ve (sistema visual) | COMO se implementa |
| Flujos, tareas, errores | Identidad, tokens | Componentes, codigo |
| WCAG, heuristicas, IA | Operadores visuales | Motion, hooks, states |

## Workflow

### Modo auditoria

1. Leer HTML/JSX del componente o pagina a auditar.
2. Aplicar las 10 heuristicas de Nielsen como checklist.
3. Validar WCAG 2.2 AA contra la lista de §Accesibilidad.
4. Medir densidad de informacion y carga cognitiva por region.
5. Clasificar hallazgos por severidad: critico, alto, medio, bajo.
6. Entregar reporte con tabla `heuristica | hallazgo | evidencia | severidad | correccion`.

### Modo diseno

1. Capturar tarea objetivo y audiencia del usuario.
2. Elegir patron UX segun tipo de interfaz (formulario, tabla, dashboard, wizard).
3. Mapear flujo de tarea con puntos de decision, errores y recuperacion.
4. Definir jerarquia visual, agrupacion semantica y affordances.
5. Producir wireframe textual o componente JSX/HTML.
6. Validar contra heuristicas antes de entregar.

## Heuristicas de Nielsen

| # | Heuristica | Pregunta clave |
|---|-----------|----------------|
| H1 | Visibilidad del estado | El usuario sabe donde esta y que pasa? |
| H2 | Correspondencia mundo real | Usa lenguaje del dominio, no tecnico? |
| H3 | Control del usuario | Puede deshacer, cancelar, volver? |
| H4 | Consistencia y estandares | Sigue patrones establecidos en la app? |
| H5 | Prevencion de errores | Evita errores antes de que ocurran? |
| H6 | Reconocer vs recordar | La info necesaria esta visible? |
| H7 | Flexibilidad y eficiencia | Hay atajos para expertos? |
| H8 | Diseno minimalista | Solo muestra lo necesario? |
| H9 | Recuperacion de errores | Los mensajes son claros y accionables? |
| H10 | Ayuda y documentacion | Hay tooltips, placeholders, guias contextuales? |

## Checklist WCAG 2.2 AA

- Contraste texto: >= 4.5:1 (normal), >= 3:1 (grande/bold).
- Contraste UI: >= 3:1 (bordes, iconos, controles).
- Focus visible en todos los interactivos (outline o ring).
- Orden de tab logico (izq -> der, arriba -> abajo).
- Labels en todos los inputs (`<label for>` o `aria-label`).
- Roles ARIA correctos (`dialog`, `alert`, `navigation`, etc.).
- `alt` text en imagenes informativas.
- Estados (`disabled`, `error`, `loading`) comunicados a screen readers.
- No depender solo del color para transmitir significado.
- Target size minimo 24x24 px (WCAG 2.2 Target Size).
- Reduccion de movimiento respetada (`prefers-reduced-motion`).
- Errores de formulario: identificar campo + descripcion del error.

## Patrones UX por tipo de interfaz

### Formularios

- Agrupar campos relacionados con `fieldset` semantico.
- Labels siempre visibles (NO solo placeholder).
- Validacion inline al salir del campo (`onBlur`), NO al escribir.
- Errores: rojo + icono + texto bajo el campo.
- Boton primario a la derecha, secundario (cancelar) a la izquierda.
- Indicar campos obligatorios (asterisco o texto).
- Progress indicator para formularios multi-paso.

### Tablas de datos

- Encabezados sticky en scroll.
- Alinear texto a la izquierda, numeros a la derecha, estados al centro.
- Filas clickeables con hover state.
- Empty state contextual (NO "No hay datos").
- Paginacion o virtual scroll para > 100 filas.
- Filtros por columna y busqueda global.

### Dashboards

- Jerarquia Z: lo critico arriba-izquierda.
- Grupos de tarjetas con proximidad visual.
- Alertas criticas destacadas con color + icono + texto.
- Acciones primarias fijas, secundarias al alcance.

### Wizards multi-paso

- Stepper visible con paso actual.
- Permitir ir atras sin perder datos.
- Confirmacion antes de enviar.
- Resumen previo al submit final.

## Invariantes

- Un hallazgo UX **DEBE** trazar a una heuristica o criterio WCAG concreto.
- Una recomendacion **DEBE** ser accionable en codigo: nombre el componente afectado, el cambio exacto, y la severidad.
- No usar hedging ("podria mejorar", "seria bueno"); usar RFC 2119 cuando aplique.
- Accesibilidad NO es feature opcional: los criterios WCAG 2.2 AA son piso, no techo.

## Salida Esperada

Reporte en Markdown con:

1. Tabla de hallazgos con columnas `id | heuristica | hallazgo | evidencia | severidad | correccion`.
2. Lista de criterios WCAG violados con referencia al criterio (e.g. `SC 1.4.3`).
3. Recomendaciones priorizadas por severidad.
4. Ejemplos de correccion en HTML/JSX cuando aplique.
