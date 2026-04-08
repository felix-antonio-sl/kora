---
name: ux-design
description: Evalua y mejora la experiencia de usuario aplicando heuristicas de usabilidad, flujos de tarea, accesibilidad WCAG 2.2, arquitectura de informacion y patrones UX institucionales. Usar cuando se necesite auditar UX, disenar formularios, mejorar navegacion, o revisar accesibilidad.
allowed-tools: [Read, Write, Edit, Grep, Glob, Bash, Agent, WebFetch, WebSearch]
---

# UX Design

Skill para evaluar, disenar y mejorar la experiencia de usuario en interfaces web. Aplica principios de usabilidad, accesibilidad y arquitectura de informacion con enfoque en aplicaciones institucionales y gobierno digital.

## Cuando usar esta skill

- Al auditar la UX de una pagina o componente existente
- Al disenar formularios, flujos de tarea o navegacion
- Al revisar accesibilidad (WCAG 2.2 AA)
- Al evaluar carga cognitiva, densidad de informacion o estados vacios
- Al crear user flows o mapas de interaccion
- Cuando el usuario dice "mejorar la UX", "revisar usabilidad", "audit UX", "accesibilidad"

## Distincion con frontend-design

| Esta skill (ux-design) | frontend-design |
|-------------------------|-----------------|
| Como se USA | Como se VE |
| Flujos, tareas, errores | Tipografia, color, motion |
| WCAG, heuristicas, IA | Estetica, composicion |
| Mide eficacia/eficiencia | Mide impacto visual |

Ambas se complementan. Usa `ux-design` primero para definir QUE necesita el usuario, luego `frontend-design` para el COMO visual.

## Framework de Evaluacion

### 1. Heuristicas de Nielsen (aplicar siempre)

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
| H9 | Recuperacion de errores | Los mensajes de error son claros y accionables? |
| H10 | Ayuda y documentacion | Hay tooltips, placeholders, guias contextuales? |

### 2. Checklist de Accesibilidad (WCAG 2.2 AA)

```
[ ] Contraste texto: >= 4.5:1 (normal), >= 3:1 (grande/bold)
[ ] Contraste UI: >= 3:1 (bordes, iconos, controles)
[ ] Focus visible en todos los interactivos (outline o ring)
[ ] Orden de tab logico (izq→der, arriba→abajo)
[ ] Labels en todos los inputs (<label for> o aria-label)
[ ] Roles ARIA correctos (dialog, alert, navigation, etc.)
[ ] Alt text en imagenes informativas
[ ] Estados (disabled, error, loading) comunicados a screen readers
[ ] No depender solo del color para transmitir significado
[ ] Target size minimo 24x24px (WCAG 2.2 Target Size)
[ ] Reduccion de movimiento respetada (prefers-reduced-motion)
[ ] Errores de formulario: identificar campo + descripcion del error
```

### 3. Patrones UX por Tipo de Interfaz

#### Formularios
- Agrupar campos relacionados (fieldset semantico)
- Labels siempre visibles (NO solo placeholder)
- Validacion inline al salir del campo (onBlur), NO al escribir
- Errores: rojo + icono + texto debajo del campo
- Boton primario a la derecha, secundario (cancelar) a la izquierda
- Indicar campos obligatorios (asterisco o texto)
- Progress indicator para formularios multi-paso

#### Tablas de datos (DataTable)
- Encabezados sticky en scroll
- Columnas alineadas: texto izq, numeros der, estados centro
- Filas clickeables con hover state
- Empty state contextual (no "No hay datos")
- Paginacion o virtual scroll para >50 filas
- Filtros visibles, no ocultos en menus

#### Navegacion
- Breadcrumbs en paginas de detalle
- Sidebar colapsable con indicador de seccion activa
- Max 7+-2 items por nivel de navegacion (Miller)
- Responsive: bottom nav o hamburger en mobile

#### Modales y Drawers
- Titulo claro de la accion
- Focus trap (tab no sale del modal)
- Escape cierra el modal
- Overlay clickeable para cerrar (excepto destructivos)
- Acciones destructivas requieren confirmacion explicita

#### Estados vacios
- Ilustracion o icono contextual
- Mensaje que explica POR QUE esta vacio
- CTA principal para resolver (ej: "Crear primer registro")
- Tono constructivo, nunca culpabilizante

#### Carga y skeleton
- Skeleton que refleja el layout real (no spinner generico)
- Skeleton en 200-300ms delay (evitar flash)
- Estados de carga parcial (tabla con skeleton en filas nuevas)
- Optimistic UI para acciones rapidas (toggle, like)

### 4. Metricas UX (para auditorias)

| Metrica | Que mide | Como evaluar |
|---------|----------|--------------|
| Tiempo a primera accion | Orientacion | El usuario encuentra el CTA en <5s? |
| Clics para completar tarea | Eficiencia | Se puede reducir pasos? |
| Tasa de error de formulario | Prevencion | Cuantos submit fallan? |
| Recuperabilidad | Resiliencia | El usuario puede volver de un error? |
| Densidad de informacion | Carga cognitiva | Cuantos datos ve a la vez? |

### 5. UX para Gobierno Digital (Chile)

- **Lenguaje claro**: Nivel lectura 8vo basico. Evitar jerga legal sin contexto.
- **Accesibilidad obligatoria**: NCh-ISO 40500 (WCAG 2.0 AA) es norma chilena.
- **Bilingue conceptual**: Nombres oficiales en espanol, codigos tecnicos en ingles.
- **Roles multiples**: Un mismo usuario puede tener diferentes niveles de expertiz digital. Priorizar claridad sobre eficiencia.
- **Sesiones largas**: Usuarios institucionales trabajan 8h en la app. Reducir fatiga visual: contraste suave, densidad controlada, descansos visuales.

## Flujo de Trabajo

### Auditoria UX (evaluacion de pagina existente)

```
1. LEER la pagina/componente completo
2. EVALUAR contra las 10 heuristicas de Nielsen
3. VERIFICAR checklist de accesibilidad
4. IDENTIFICAR patron de interfaz y comparar con mejores practicas
5. CLASIFICAR hallazgos por severidad:
   - CRITICO: Bloquea tarea o excluye usuarios
   - ALTO: Causa errores frecuentes o frustracion
   - MEDIO: Reduccion de eficiencia o inconsistencia
   - BAJO: Mejora nice-to-have
6. PROPONER soluciones concretas (codigo, no solo texto)
```

### Diseno UX (nueva interfaz)

```
1. DEFINIR: Quien es el usuario? Que tarea cumple?
2. FLUJO: Dibujar el happy path + 2 caminos de error
3. WIREFRAME: Estructura de informacion (que va donde)
4. INTERACCION: Definir estados (vacio, cargando, error, exito, lleno)
5. ACCESIBILIDAD: Validar checklist antes de implementar
6. IMPLEMENTAR: Codigo con los patrones de la seccion 3
7. VALIDAR: Re-evaluar contra heuristicas post-implementacion
```

### Formato de Reporte

Al completar una evaluacion, presentar asi:

```markdown
## Auditoria UX: [Nombre de pagina]

### Resumen
- Hallazgos: X criticos, Y altos, Z medios
- Score heuristico: N/10
- Accesibilidad: AA cumple / no cumple

### Hallazgos

#### [SEVERIDAD] H#: Titulo corto
- **Problema**: Descripcion concisa
- **Impacto**: A quien afecta y como
- **Solucion**: Codigo o cambio especifico
- **Esfuerzo**: Bajo/Medio/Alto

### Accesibilidad
[Checklist con estado por item]
```

## Recursos

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Nielsen Heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- GOB.cl Guia Digital: https://www.guiadigital.gob.cl/
- NCh-ISO 40500: Norma chilena de accesibilidad web
