---
_manifest:
  urn: urn:kora:artefacto:ifml
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Diseno desde 0 sobre corpus IFML koraficado en artifacts/knowledge/fxsl/ifml/
      (9 URNs publicadas en v1.0.0).
version: 1.0.1
status: activo
nombre: ifml
descripcion: Skill horizontal para diagnosticar, diseñar y aplicar soluciones IFML
  (Interaction Flow Modeling Language, OMG) durante el desarrollo de aplicaciones
  interactivas web/desktop/mobile/multiscreen.
tags:
- ifml
- omg
- mda
- frontend
- ux
- modelado-interaccion
- navegacion
- view-design
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma:
      - 1
      - 1
      - 3
      - 1
      - 0
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:fxsl:kb:ifml-corpus-index
    - urn:fxsl:kb:ifml-fundamentos
    - urn:fxsl:kb:ifml-view-containers
    - urn:fxsl:kb:ifml-view-components
    - urn:fxsl:kb:ifml-actions-events
    - urn:fxsl:kb:ifml-extensiones-desktop
    - urn:fxsl:kb:ifml-extensiones-web
    - urn:fxsl:kb:ifml-extensiones-mobile
    - urn:fxsl:kb:ifml-patrones
    componible_con:
    - urn:kora:artefacto:modelamiento-opm
    - urn:kora:artefacto:jointjs-open-source
artefacto:
  perfil:
    dominio:
    - ifml
    - frontend
    - ux
    - modelado-interaccion
    - omg
    - mda
    - navegacion
    - view-design
    disparadores:
    - solicitud explicita de modelar interaccion frontend con IFML
    - diseño de navegacion entre paginas, ventanas o contenedores
    - diagnostico estructural de una UI existente (vista, contenido, eventos, transiciones)
    - aplicacion de patron IFML cifrado a un problema concreto de UX
    - validacion de un Interaction Flow Diagram contra el estandar OMG
    - seleccion de patron apropiado para una tarea de interaccion (busqueda, data
      entry, master detail, faceted search, etc.)
    - decision sobre extensiones desktop/web/mobile aplicables a un escenario
    - diseño de adaptacion contextual de UI (Context, ContextDimension, ViewPoint)
    salidas:
    - modelo IFML tipado (ViewContainer/ViewComponent/Event/NavigationFlow/Action)
      con anidamiento conjuntivo o XOR coherente
    - cita del patron aplicado con codigo oficial XY-Z (ej. CN-MD, OW-MFE, DE-WIZ)
    - reporte de validacion estructural contra reglas del estandar
    - ParameterBinding y ParameterBindingGroup explicitos cuando hay dependencia I/O
    - (opcional) hook a herramienta de render visual cuando se solicite
  plan:
    estado_inicial: triaje
    estado_terminal: entregar
    estados:
    - triaje
    - encuadrar-aplicacion
    - seleccionar-patrones
    - modelar-composicion
    - modelar-contenido
    - modelar-eventos-acciones
    - aplicar-extensiones
    - validar-modelo
    - entregar
  interfaz:
    herramientas:
    - Read
    - Grep
    - Glob
    permisos: lectura-corpus
    protocolos:
      entrada: descripcion de la aplicacion o flujo a modelar (string), o IFD existente
        (estructura serializada), o peticion dirigida (validar X, sugerir patron para
        Y)
      salida: modelo IFML estructurado + patrones citados + reporte de validacion
        + (opcional) hook a render
  invariantes:
    reglas_duras:
    - 'Constructos solo del estandar OMG: usar exclusivamente las primitivas y extensiones
      documentadas en el corpus IFML. Sin atajos visuales ni semanticas inventadas.'
    - Conservar nombres en ingles para constructos IFML (ViewContainer, NavigationFlow,
      ParameterBinding, Action, etc.); traducir solo prosa explicativa.
    - 'Todo Event que dispare interaccion debe tener salida explicita: NavigationFlow,
      DataFlow, o flujo a Action. Sin eventos colgados.'
    - ParameterBinding obligatorio cuando el destino requiere input del origen para
      computar contenido; ParameterBindingGroup cuando son varios parametros simultaneos.
    - 'Anidamiento conjuntivo (default) vs XOR debe corresponder a la realidad operativa:
      simultaneo = conjuntivo; mutually exclusive = XOR. No usar XOR como decoracion.'
    - Window con stereotype Modal o Modeless solo cuando la semantica de bloqueo del
      fondo importa; sino usar ViewContainer plano.
    - Action es referencia a logica externa, no encapsula la logica. Detallar el behavior
      en modelo separado (UML sequence, BPMN, activity).
    - Patron citado con codigo oficial XY-Z. Si no calza ninguno del catalogo, declarar
      el desvio explicitamente y nombrar la combinacion de constructos base.
    - 'DataFlow vs NavigationFlow: DataFlow para paso de parametros sin interaccion
      del usuario; NavigationFlow para paso disparado por evento del usuario.'
    - Page/Area/SiteView (web) y MapView/Marker/Path (mobile) solo cuando la dimension
      de plataforma justifica la extension; preferir core IFML cuando alcance.
    - Context + ViewPoint solo paga su prima si la aplicacion realmente cambia composicion
      en runtime; para variantes estaticas basta ActivationExpression sobre elementos.
    - 'No invadir dominio: la skill modela estructura de interaccion, no semantica
      de negocio ni decisiones de presentacion grafica (look & feel).'
    compromisos_eticos:
      transparency: Alta; cada decision de modelado cita la URN del archivo del corpus
        IFML correspondiente y el patron aplicado por codigo XY-Z.
      accountability: Alta; ante ambiguedad declara el supuesto del modelador antes
        de continuar; emite borrador trazable a las URNs del corpus.
---

# IFML

## Proposito

Skill horizontal para **diagnosticar, diseñar y aplicar soluciones IFML** durante el desarrollo de aplicaciones interactivas. Provee la capacidad de tomar una descripcion de aplicacion (web, desktop, mobile, multiscreen) y producir un Interaction Flow Diagram tipado, validado contra el estandar OMG, con citas de los patrones aplicables.

La skill es **estructural**: trabaja la sintaxis y semantica del lenguaje IFML, no la decision de diseño grafico ni la logica de negocio. El conocimiento de dominio lo aporta el agente que invoca la skill.

Anclaje canonico: las nueve capas del corpus IFML v1.0.0:

| Capa | URN | Rol en la skill |
|------|-----|-----------------|
| Indice | `urn:fxsl:kb:ifml-corpus-index` | Mapa del corpus |
| Fundamentos | `urn:fxsl:kb:ifml-fundamentos` | MVC, principios, ciclo de desarrollo, ejemplo Bookstore |
| Composicion UI | `urn:fxsl:kb:ifml-view-containers` | ViewContainer, anidamiento, Window, Context, ViewPoint, patrones O-* |
| Contenido y nav | `urn:fxsl:kb:ifml-view-components` | ViewComponent, DataBinding, ParameterBinding, Form, patrones CN/DE/CS |
| Acciones y eventos | `urn:fxsl:kb:ifml-actions-events` | Action, ActionEvent, SystemEvent, patrones CM-* |
| Ext. desktop | `urn:fxsl:kb:ifml-extensiones-desktop` | OnFocusLost, drag/drop, Tree, Table, EditableSelectionField |
| Ext. web | `urn:fxsl:kb:ifml-extensiones-web` | Page, Area, SiteView, WebNavigationFlow, List variants |
| Ext. mobile | `urn:fxsl:kb:ifml-extensiones-mobile` | Context dims, MapView, gestos, multiscreen |
| Patrones | `urn:fxsl:kb:ifml-patrones` | Catalogo cifrado XY-Z (~80 patrones) |

## Cuando Usar

- modelar la interaccion frontend de una aplicacion desde requirements o use cases.
- diseñar la jerarquia de ViewContainer y la navegacion entre vistas.
- diagnosticar una UI existente para verificar consistencia estructural antes de implementar cambios.
- elegir un patron IFML aplicable a un problema concreto (master detail, faceted search, multistep wizard, etc.).
- validar que parameter bindings, eventos y flujos respetan las reglas del estandar.
- decidir entre extensiones desktop, web o mobile cuando la plataforma importa.
- modelar adaptacion contextual de la interfaz (multi-rol, multi-device, multi-screen).

## Cuando NO Usar

- diseñar **presentacion grafica** (look & feel, layouts pixel-perfect): IFML lo delega; usar herramientas de UX/UI dedicadas.
- modelar **logica de negocio interna** de una accion: IFML referencia, no encapsula. Usar UML sequence/activity, BPMN, BPEL.
- modelar el **domain model** (entidades, atributos, asociaciones): IFML referencia el modelo de contenido pero no lo construye. Usar UML class diagram, ERD, ontologia.
- modelar interaccion entre sistemas no humanos (B2B, microservicios): IFML modela interfaces para usuarios humanos.
- decidir entre arquitecturas backend (PIM/PSM, deployment): orthogonal a IFML.
- consultoria de dominio (medicina, legal, gobierno): delegar al agente especializado.

Si la pregunta es sobre **navegacion entre vistas**, **estructura de pantallas**, **flujo de datos en formularios**, **eventos de UI**, o **patrones de interfaz**: IFML aplica. Si es sobre **estilo visual**, **logica de negocio interna**, o **estructura de datos persistentes**: IFML no aplica directamente.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud para decidir el siguiente estado:

| Input del usuario | Siguiente estado |
|-------------------|------------------|
| "modelar la app X con IFML" / "diseñar la interaccion de Y" | `encuadrar-aplicacion` |
| "que patron sirve para Z?" / "como hago un wizard / faceted search?" | `seleccionar-patrones` |
| "validar este IFD" / "este modelo cumple IFML?" | `validar-modelo` |
| "que extensiones desktop/web/mobile aplican aqui?" | `aplicar-extensiones` |
| "como modelo el contexto X (rol/device/posicion)?" | `aplicar-extensiones` (rama context) |

Antes de avanzar, verificar que el problema es **estructural de interaccion frontend**. Si es presentacion grafica pura, logica de negocio o dominio: abortar con sugerencia de herramienta correcta.

### `encuadrar-aplicacion`: clasificar el espacio de diseño

Determinar caracteristicas que condicionan el modelo:

| Dimension | Pregunta | Lleva a |
|-----------|----------|---------|
| Plataforma | desktop / web / mobile / multiscreen / hibrido | extensiones especificas (`ifml-extensiones-*`) |
| Roles | uno / varios / publicos vs autenticados | `Context`, `UserRole`, `ViewPoint`, `OW-MFE` |
| Adaptacion | estatica / dinamica (device, posicion, network) | `ContextDimension` + `ActivationExpression` |
| Tareas dominantes | navegacion, busqueda, data entry, gestion contenido | familia de patrones aplicable (CN, CS, DE, CM) |

Salida: ficha de encuadre con plataforma elegida, conjunto inicial de roles, dimensiones contextuales relevantes, y familias de patrones probables.

### `seleccionar-patrones`: elegir patrones del catalogo

Consultar `urn:fxsl:kb:ifml-patrones` para mapear cada tarea/problema a un patron cifrado:

- problemas de organizacion -> `O*` (`OD-SWA`, `OW-LWSA`, `OM-MSL`, etc.)
- problemas de contenido y navegacion -> `CN-*` (`CN-MD`, `CN-MLMD`, `CN-DEF`, etc.)
- problemas de data entry -> `DE-*` (`DE-FRM`, `DE-WIZ`, `DE-CSF`, etc.)
- problemas de busqueda -> `CS-*` (`CS-SRC`, `CS-MCS`, `CS-FSR`)
- problemas de gestion -> `CM-*` (`CM-OCR`, `CM-ODL`, `CM-AM`, `CM-NOTIF`, etc.)
- problemas de identidad/auth -> `IA-*`
- problemas de sesion -> `SES-*`
- problemas sociales -> `SOC-*`
- problemas geo -> `GEO-*`

Si ningun patron del catalogo calza: declarar el desvio, nombrar la combinacion de constructos base que se va a usar, y dejar la deuda como nota.

### `modelar-composicion`: ViewContainer y anidamiento

Aplicar `urn:fxsl:kb:ifml-view-containers`:

1. Definir `ViewContainer` top-level (uno o varios segun plataforma).
2. Decidir anidamiento conjuntivo (simultaneo) vs XOR (mutually exclusive) por subcontainer.
3. Marcar `Default` el que se muestra por defecto al acceder al padre disyuntivo.
4. Marcar `Landmark` los alcanzables desde todos los hermanos (reduce flechas explicitas).
5. Si requiere ventanas modales/modeless: usar stereotype `Window`/`Modal`/`Modeless`.

### `modelar-contenido`: ViewComponent y bindings

Aplicar `urn:fxsl:kb:ifml-view-components`:

1. Por cada `ViewContainer`, identificar `ViewComponent` (Lists, Details, Forms, MultiChoiceLists).
2. Para cada componente con contenido del domain: especificar `DataBinding` (clase + ConditionalExpression OCL + VisualizationAttributes + OrderBy).
3. Para componentes con contenido operacional: usar `DynamicBehavior` referenciando UMLBehavior.
4. Identificar dependencias I/O entre componentes: `ParameterBinding` + `ParameterBindingGroup` cuando varios.
5. Decidir si paso de parametros requiere interaccion (`NavigationFlow`) o no (`DataFlow`, flecha discontinua).

### `modelar-eventos-acciones`: Events, Actions, SystemEvents

Aplicar `urn:fxsl:kb:ifml-actions-events`:

1. Por cada `ViewComponent` interactivo, asociar `Event` (`SelectEvent`, `SubmitEvent`, etc.).
2. Cada `Event` debe tener salida: `NavigationFlow` a `ViewContainer`/`ViewComponent`, o flujo a `Action`.
3. Las `Action` se modelan como hexagono con normal/exceptional `ActionEvent`. La logica interna se delega a modelos externos.
4. Para notificaciones generadas por sistema/servicios externos: `SystemEvent` + `SystemFlow` + `TriggeringExpression` opcional.
5. Para CRUD del domain: aplicar patrones `CM-*` con sus mecanicas estandar.

### `aplicar-extensiones`: especializaciones por plataforma o contexto

Decidir cuando aplica:

| Necesidad | Extension |
|-----------|-----------|
| events sofisticados de desktop (focus loss, drag/drop, edicion en tabla) | `ifml-extensiones-desktop`: `OnFocusLost`, `OnDragStart`, `OnDrop`, `Tree`, `Table` |
| URLs, RBAC web, links con propiedades hypertext | `ifml-extensiones-web`: `Page`, `Area`, `SiteView`, `WebNavigationFlow` |
| listas avanzadas web (sort dinamico, paging, nested) | `ifml-extensiones-web`: `DynamicSortedList`, `ScrollableList`, `NestedList` |
| sensors, mapas, gestos, multiscreen | `ifml-extensiones-mobile`: `MapView`, `Marker`, `Path`, gestos como event types, multiscreen via `ActivationExpression` |
| adaptacion contextual fuerte (rol, device, network, posicion) | `Context`, `ContextDimension`, `ContextVariable`, `ActivationExpression`, `ViewPoint` |

Regla de parsimonia: usar core IFML cuando alcance. Las extensiones pagan prima cuando la dimension de plataforma o contexto realmente justifica el constructo especializado.

### `validar-modelo`: verificar invariantes

Tres niveles:

1. **Estructurales** (corpus core):
   - todo `ViewContainer` no-XOR no necesita default; uno XOR si o si necesita uno.
   - `Landmark` solo dentro del enclosing comun.
   - todo `Event` interactivo tiene `NavigationFlow` o `Action` saliente.
   - `ParameterBinding` cuando hay dependencia I/O explicita.
   - `DataFlow` con flecha discontinua, `NavigationFlow` con flecha continua.

2. **Semanticas** (corpus core):
   - `Action` es referencia a logica externa, no logica encapsulada.
   - `SystemEvent` no depende de interaccion del usuario.
   - distinguir `ActionEvent` normal vs exceptional cuando aplique.

3. **Catalogo de patrones**:
   - patrones citados con codigo `XY-Z` exacto.
   - extensiones consistentes con la plataforma declarada.

Salida: reporte pass/fail con cita de la regla violada y URN del archivo del corpus.

Si falla → volver al estado correspondiente con el fix sugerido.
Si pasa → avanzar a `entregar`.

### `entregar`: paquete final

Salida coherente al agente invocador:

- estructura tipada del modelo: lista de `ViewContainer`, `ViewComponent`, `Event`, `NavigationFlow`, `Action` con sus propiedades.
- patrones aplicados con codigo `XY-Z` y referencia a la URN del corpus.
- reporte de validacion estructural.
- (opcional) hook a `urn:kora:artefacto:jointjs-open-source` si se solicito render visual del IFD.

## Reglas Duras

1. **Constructos del estandar**: usar exclusivamente primitivas y extensiones del corpus IFML. Sin invenciones.
2. **Idioma**: nombres de constructos en ingles (ViewContainer, NavigationFlow, etc.); prosa explicativa en español.
3. **Eventos con salida**: ningun `Event` interactivo queda colgado. `NavigationFlow`, `DataFlow` o `Action` siempre.
4. **Parameter binding obligatorio cuando el destino depende del origen** para computar contenido.
5. **Anidamiento coherente con realidad operativa**: XOR = mutually exclusive real; conjuntivo = simultaneo real.
6. **Window/Modal/Modeless** solo cuando la semantica de bloqueo de fondo importa.
7. **Action es referencia, no encapsula logica**. Detallar behavior en modelo externo.
8. **Patrones citados con codigo oficial** `XY-Z` o desvio declarado.
9. **DataFlow vs NavigationFlow** segun haya o no interaccion explicita del usuario.
10. **Extensiones cuando justifiquen**, no como decoracion. Core IFML cuando alcance.
11. **Context + ViewPoint solo si la composicion cambia en runtime**, sino `ActivationExpression` sobre elementos individuales.
12. **No invadir dominio**: la skill modela estructura de interaccion, no semantica de negocio ni look & feel.

## Composicion con otras skills

### Con `modelamiento-opm`

OPM y IFML son complementarios:

- OPM modela el **sistema** (objetos, procesos, transformaciones, funcion). Capa conceptual del dominio.
- IFML modela la **interaccion del usuario con el sistema** (vistas, navegacion, eventos). Capa de interfaz.

Composicion tipica:

1. `modelamiento-opm` produce el OPM model del sistema; identifica los procesos visibles al usuario.
2. IFML modela el front-end que expone esos procesos como `Action` triggered by user events.
3. `Action` IFML referencia al proceso OPM correspondiente como su DynamicBehavior.

### Con `jointjs-open-source`

Para render visual del Interaction Flow Diagram cuando el invocador pide diagrama:

- IFML produce la estructura tipada (containers, components, events, flows con sus propiedades).
- `jointjs-open-source` realiza el render concreto (SVG, interactivo).

IFML conserva la responsabilidad del modelo correcto; jointjs la del render.

## Recursos

### Scripts

`scripts/` reservado para validacion sintactica de IFML expressions (OCL en ConditionalExpression, ActivationExpression, TriggeringExpression). En v1.0.0 esta vacio; se implementa cuando exista demanda real.

### Referencias

En v1.0.0 las referencias se delegan al corpus directo (las 9 URNs publicadas en `artifacts/knowledge/fxsl/ifml/`). No hay archivos de referencias internas en este momento. Si futuras iteraciones requieren material destilado mas alla del corpus (ej. arboles de decision para seleccion de patrones), se agregan en `referencias/` como resumenes operativos curados — nunca como SSOT alternativo al corpus.

### Recursos

`recursos/` reservado para ejemplos didacticos minimos del estandar (ej. modelo IFML del Bookstore presente en `ifml-fundamentos`). En v1.0.0 los ejemplos estan en el corpus mismo; no se duplican aqui.
