# hsc-cli — Remapeo Canónico Corregido

Fecha: 2026-04-14

Objetivo: redefinir `hsc-cli` como supermercado de ingredientes clínicos extraídos, no como capa de síntesis clínica. Este remapeo se basa en el código vivo de `/home/felix/projects/hsc-cli` y en la arqueología operativa del repo.

## Regla de producto

- `h` no cocina.
- `h` extrae, limpia, empaqueta y referencia ingredientes.
- La síntesis clínica queda fuera del CLI.
- La unidad semántica principal deja de ser `ctx` o `hx`; pasa a ser `identity`, `event`, `document`, `component`.

## Capacidad real actual

| Capacidad | Endpoint real | Comando actual | Estado | Observación |
|---|---|---|---|---|
| Resolver identidad por RUT | `SGH ingreso/obt_paciente.php` + `funciones/busqueda/buscar_datos_paciente.php` | `h who`, `h patient`, `h ctx` | yes | Buena base para `rut`, `cp`, `ingreso_id`, demografía |
| Resolver identidad desde atención DAU | `DAU atencion/index.php` | `h who`, `h patient`, `h ctx` | yes | Extrae `codPacie`, `run_paciente`, `codAdmision` |
| Detectar urgencia activa | `DAU atencion/index.php` | `h who`, `h patient` | yes | Si hay `atencion_id`, la urgencia actual queda resuelta |
| Detectar hospitalización activa | `SGH ingreso/obt_paciente.php` | `h who`, `h patient` | partial | `ingreso_id` sí; `servicio/cama` no quedan bien extraídos en parser canónico |
| Ver todos los pacientes en box | `DAU listadoPacientesBox/listadoPacientesBox.php` | `h box`, `h handoff` | yes | Estado operativo fuerte de urgencia |
| Ver cola de espera urgencia | `DAU llamar/listadoPacientesBox.php` | `h cola` | yes | Buena superficie operacional pre-box |
| Triage actual | `DAU triageprueba/listadoTriage.php` | `h tri`, `h ctx` | yes | Fuente fuerte para MC, alergias, clasificación, SV iniciales |
| Signos vitales evolutivos | `DAU atencion/obtener_listado_signos_vitales.php` | `h sv`, `h ctx` | yes | Serie cruda con timestamps |
| Nota médica actual | `DAU obtener_anamnesis.php`, `obtener_examen_fisico.php`, `obtener_hipotesis.php` | `h nota`, `h ctx` | yes | Ya existe como trío granular usable |
| Diagnósticos actuales | `DAU atencion/obtener_cie.php` | `h dx`, `h ctx` | yes | CIE-10 estructurado |
| Observaciones / SIC | `DAU atencion/obtener_lista_sic.php` | `h obs`, `h ctx --deep` | yes | La semántica exacta es mixta, pero la lectura existe |
| Laboratorio DAU del episodio | `DAU atencion/obtener_lista_exa_laboratorio.php` | `h labs`, `h ctx` | yes | Más bien órdenes/resultados de episodio que LIS longitudinal |
| Imagenología del episodio | `DAU atencion/obtener_lista_exa_rayo.php`, `obtener_lista_exa_scanner.php` | `h img` | yes | Superficie operativa útil |
| Indicaciones / terapéutica | `DAU atencion/obtener_lista_indicaciones.php` | `h rx`, `h ctx` | yes | Ingrediente fuerte del episodio |
| Alergias | `DAU triageprueba/listadoTriage.php` | `h alx` | yes | Hoy sale aislando triage |
| DAU imprimible de evento | `DAU atencion/dau_p.php` | `h dau`, `h hx --deep`, `h ctx --deep` | yes | Artefacto documental denso; no usar para identidad actual |
| Urgencias previas longitudinales | `SGH ingreso/atenciones_previas.php` | `h hx`, `h ctx` | yes | Incluye puente hacia `cod_atencion` DAU previo |
| Hospitalizaciones previas | `SGH ingreso/ver_paciente.php` | `h hx`, `h ctx` | yes | Parser útil para ingreso, estado, diagnóstico, servicio, fecha |
| Evoluciones de hospitalización | `SGH ingreso/cargar_historial_evolucion.php` | `h evo`, `h hx --deep`, `h ctx --deep` | yes | Hay dos variantes de parser: tabla y accordion rico |
| Detalle de evolución | `SGH ingreso/cargar_detalle_evolucion.php` | `h evo detail`, `h hx --deep` | yes | JSON rico |
| Diagnósticos de egreso | `SGH ingreso/actualizar_diagnostico_egreso.php` | `h hx --deep` | yes | Ya se usa como enriquecimiento |
| Intervenciones / procedimientos | `SGH funciones/listado/listado_intervenciones_egreso.php` | `h hx --deep` | yes | Útil para componentes procedimentales |
| Documentos SGH hospitalización | `SGH ingreso/ver_pdf.php` con `ing|sol|epi|con|alt` | `h docs`, `h doc`, `h hx --deep`, `h ctx --deep` | yes | PDFs ya convertidos a texto con `pdftotext` |
| Ambulatorias previas CAE / OSIRIS | `SGH ingreso/atenciones_previas_ambulatorias.php` | `h amb`, `h ctx --deep` | yes | Historial ambulatorio real, no agenda futura |
| Documentos OSIRIS ambulatorios | `SGH ingreso/osiris/listadoDocumentos.php` + PDFs OSIRIS | `h amb-doc` | yes | Una de las superficies más valiosas ya implementadas |
| APS previas | `SGH ingreso/atenciones_previas_aps.php` | `h aps` | partial | Parser existe, pero endpoint a menudo devuelve `error` por Rayen externo |
| Órdenes LIS por RUT | `LAB resultadoseleccion.php` | `h lis`, `h ctx --deep` | yes | Buen listado de órdenes recientes |
| Detalle de orden LIS | `LAB detalleexamenes.php` | `h lis-detail`, `h lis --last`, `h lis --altered` | yes | PDF parseado localmente |
| Dashboard camas | `SGH estructura/data.php` | `h camas` | yes | Vista operacional hospitalaria |
| Pacientes por sala/cama | `SGH funciones/listado/listado_datos_camas_pacientes.php` | `h sala` | yes | Responde la pregunta servicio/cama aunque no desde identidad canónica |
| Mapa unidades/salas | `internal/sgh/units.go` + SGH room ids | `h unidades`, `h sala` | yes | Alias humanos resueltos localmente |
| Buscar por nombre en urgencia | DAU box + cola | `h who <nombre>` | yes | Usa box/cola, no búsqueda global longitudinal |

## Correcciones duras al modelo previo

### 1. Hospitalización actual: sí/no sí, servicio/cama no

`internal/parser/sgh.go` documenta que extrae `cama` y `servicio`, pero hoy no lo hace. La identidad canónica actual es suficiente para:

- `ingreso_id`
- `fecha_ingreso`
- `cp`
- `rut`

No es suficiente hoy para:

- `servicio_actual`
- `sala_actual`
- `cama_actual`

Eso existe, pero en superficies operacionales de SGH (`h sala`, `h camas`), no en el parser canónico de identidad.

### 2. CAE / ambulatorio actual no es agenda futura

`h amb` y `atenciones_previas_ambulatorias.php` entregan historial ambulatorio hospitalario. No vi evidencia de agenda futura formal en la capa actual. El endpoint SGH más cercano es `ingreso/lista_espera.php`, hoy no expuesto por `h`.

### 3. OSIRIS documental ya está más maduro de lo que parecía

`h amb-doc`:

- lista visitas ambulatorias
- resuelve `cod_cita`, `cod_inst`, `cod_pacie`, `modalidad`
- llama `osiris/listadoDocumentos.php`
- resuelve PDF correcto según `cod_tipo`
- descarga el PDF
- ejecuta `pdftotext`

Eso ya es una base real para `event-docs` ambulatorio.

## Ontología V2 recomendada

### Identity

Unidad canónica de resolución mínima:

- `rut`
- `cp`
- `nombre`
- `sexo`
- `fecha_nac`
- `edad`
- `comuna`
- `domicilio`
- `telefono`
- `active_refs`

`active_refs` debería separar:

- `dau.atencion_id`
- `dau.cod_admision`
- `sgh.ingreso_id`

### Event

Evento longitudinal o activo.

Tipos mínimos:

- `current_urgency`
- `urgency`
- `hospitalization`
- `ambulatory_cae`
- `aps`
- `lis_order`

ID canónico recomendado:

- `current_urgency:dau:<atencion_id>`
- `urgency:dau:<atencion_id>`
- `hospitalization:sgh:<ingreso_id>`
- `ambulatory:osiris:<cod_cita>`
- `aps:sgh:<fecha|hash>`
- `lis:order:<id>`

### Document

Artefacto documental asociado a evento.

Tipos reales ya visibles:

- `dau_print`
- `sgh_ingreso`
- `sgh_epicrisis`
- `sgh_alta`
- `sgh_consentimiento`
- `osiris_atencion`
- `osiris_alta`
- `osiris_no_alta`
- `osiris_ges_ipd`
- `osiris_ges_excepcion`
- `osiris_ges_cierre`
- `osiris_interconsulta`
- `osiris_receta`
- `lis_pdf`

### Component

Fragmento granular extraído de un evento o documento.

Familias mínimas:

- `identity`
- `event_meta`
- `triage`
- `vitals`
- `anamnesis`
- `physical_exam`
- `hypothesis`
- `diagnosis`
- `indication`
- `medication`
- `lab_order`
- `lab_result`
- `image_order`
- `observation`
- `allergy`
- `evolution`
- `discharge_diagnosis`
- `procedure`
- `interconsult`
- `document_text`

## Superficie V2 sugerida

### Identity y presencia actual

- `h identity <id>`
- `h active-events <id>`
- `h current-urgency <id>`
- `h current-hospitalization <id>`

### Eventos

- `h events <id>`
- `h event <event_ref>`
- `h event-docs <event_ref>`
- `h event-components <event_ref>`

### Documentos

- `h doc <doc_ref>`
- `h doc-text <doc_ref>`
- `h doc-components <doc_ref>`

### Componentes DAU

- `h triage <id>`
- `h vitals <id>`
- `h note <id>`
- `h dx <id>`
- `h obs <id>`
- `h lab-orders <id>`
- `h image-orders <id>`
- `h indications <id>`
- `h allergies <id>`

### Componentes longitudinales SGH/OSIRIS/LIS

- `h hospitalizations <id>`
- `h urgencies-history <id>`
- `h evolutions <ingreso|id>`
- `h evolution-detail <evo_id>`
- `h ambulatory-events <id>`
- `h ambulatory-docs <id|event_ref>`
- `h aps-events <id>`
- `h lis-orders <id>`
- `h lis-order <order_id>`

## Gaps reales todavía abiertos

### Gaps funcionales

- `servicio/cama` en identidad canónica actual
- agenda/citas futuras CAE realmente expuesta en CLI
- interconsultas SGH como superficie propia canónica
- recetas SGH longitudinales expuestas como ingrediente
- categorizaciones/Barthel/SIC hospitalario expuestas como componente
- ubicación actual SGH vía `cargar_ubicacion_paciente.php`
- labs externos/red SSÑ e imagenología externa como ingredientes directos

### Gaps de extracción

- PDFs SGH que a veces salen como imagen o texto pobre
- APS depende de Rayen y falla remoto
- parte del DAU médico-legal / alcoholemia / toxicológico aún no está productizado en `h`

## Orden de implementación sugerido

1. Separar la capa canónica `identity/events/docs/components` sin borrar aún los comandos legacy.
2. Crear `active-events` y `current-hospitalization` con resolución explícita de ubicación.
3. Promover `amb-doc` a `ambulatory-event-docs` canónico.
4. Crear `events` como timeline unificado con refs estables.
5. Reencuadrar `h docs`, `h dau`, `h lis-detail` como `document fetchers`.
6. Sacar `ctx`, `patient`, `hx`, `handoff` de la superficie primaria y dejarlos como compuestos/legacy.

## Conclusión

El repo ya tiene mucho más de lo necesario para pasar a un modelo de supermercado. Lo que falta no es “más contexto clínico” sino:

- renombrar semánticamente la superficie
- consolidar IDs y tipos
- separar presencia actual de longitudinal
- endurecer la extracción documental y la capa de sesión

La mayor deuda estructural no está en DAU u OSIRIS documental. Está en la capa canónica de identidad/eventos y en el manejo de sesiones/cookies.
