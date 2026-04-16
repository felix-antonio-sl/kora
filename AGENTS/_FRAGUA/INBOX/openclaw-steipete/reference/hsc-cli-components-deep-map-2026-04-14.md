# hsc-cli — Deep Component Map

Fecha: 2026-04-14

Objetivo: inventariar los componentes granulares que ya salen realmente de los parsers/comandos actuales y distinguirlos de las superficies latentes que existen en los endpoints pero aún no están expuestas en la CLI.

## Regla de lectura

- `extraído`: ya sale de parser/comando vivo.
- `latente`: el endpoint existe y la semántica es útil, pero aún no está productizada.
- `débil`: existe, pero hoy sale con forma pobre o ambigua.

## Componentes extraídos hoy

| Sistema | Endpoint | Superficie actual | Componente | Campos reales | Calidad |
|---|---|---|---|---|---|
| DAU | `atencion/index.php` | `who`, `patient`, `ctx`, `tri` | `event_meta.current_urgency` | `atencion_id`, `codAdmision`, `codPacie`, `run_paciente`, `dv_paciente` | fuerte |
| DAU | `triageprueba/listadoTriage.php` | `tri`, `ctx`, `alx` | `triage` | `fecha`, `categoria`, `motivo_consulta`, `antecedentes`, `alergias`, `profesional`, `raw` | fuerte |
| DAU | `triageprueba/listadoTriage.php` | `tri`, `ctx` | `vitals.initial` | `timestamp`, `pa_sys`, `pa_dia`, `fc`, `sat`, `hgt`, `fr`, `temp`, `glasgow`, `source=triage` | fuerte |
| DAU | `atencion/obtener_listado_signos_vitales.php` | `sv`, `ctx` | `vitals.serial` | `timestamp`, `pa_sys`, `pa_dia`, `fc`, `temp`, `fr`, `sat`, `hgt`, `source/profesional` | fuerte |
| DAU | `obtener_anamnesis.php` | `nota`, `ctx` | `anamnesis` | `detalle_id`, `timestamp`, `profesional`, `texto` | fuerte |
| DAU | `obtener_examen_fisico.php` | `nota`, `ctx` | `physical_exam` | `detalle_id`, `timestamp`, `profesional`, `texto` | fuerte |
| DAU | `obtener_hipotesis.php` | `nota`, `ctx` | `hypothesis` | `detalle_id`, `timestamp`, `profesional`, `texto` | fuerte |
| DAU | merge de los 3 anteriores | `nota`, `ctx` | `clinical_note` | `detalle_id`, `timestamp`, `profesional`, `origen`, `anamnesis`, `examen_fisico`, `hipotesis` | fuerte |
| DAU | `atencion/obtener_cie.php` | `dx`, `ctx` | `diagnosis` | `codigo`, `descripcion` | fuerte |
| DAU | `atencion/obtener_lista_sic.php` | `obs`, `ctx --deep` | `observation` | `timestamp`, `texto`, `profesional` | media |
| DAU | `atencion/obtener_lista_exa_laboratorio.php` | `labs`, `ctx` | `lab_order` | `fecha`, `examen`, `estado` | media |
| DAU | `atencion/obtener_lista_indicaciones.php` | `rx`, `ctx` | `indication/medication_visible` | `timestamp`, `nombre`, `profesional`, `estado` | media |
| DAU | `listadoPacientesBox/listadoPacientesBox.php` | `box`, `who <nombre>` | `operational_patient_box` | `atencion_id`, `nombre`, `edad`, `box`, `categoria`, `tiempo`, `servicio`, `tratante`, `alergias`, `background` | fuerte |
| DAU | `llamar/listadoPacientesBox.php` | `cola`, `who <nombre>` | `operational_patient_queue` | `nombre`, `edad`, `tiempo_espera` y columnas variables por tabla | media |
| DAU | `atencion/dau_p.php` | `dau`, `hx --deep`, `ctx --deep` | `document.dau_print` | `cod_atencion`, `texto_resumen`, y secciones heurísticas: `anamnesis`, `examen_fisico`, `hipotesis`, `indicaciones`, `diagnosticos[]` | media |
| SGH | `ingreso/obt_paciente.php` | `who`, `patient`, `ctx` | `identity.base` | `nombre`, `rut`, `cp`, `ingreso_id`, `fecha_ingreso` | media |
| SGH | `funciones/busqueda/buscar_datos_paciente.php` | `who`, `patient` | `identity.demographics` | `nombre`, `rut`, `edad`, `comuna`, `domicilio` | fuerte |
| SGH | `ingreso/ver_paciente.php` | `hx`, `ctx`, `patient` | `event.hospitalization` | `ingreso_id`, `estado`, `diagnostico`, `establecimiento`, `servicio`, `fecha` | fuerte |
| SGH | `ingreso/atenciones_previas.php` | `hx`, `ctx` | `event.urgency_history` | `fecha`, `diagnostico`, `establecimiento`, `atencion_id` | fuerte |
| SGH | `ingreso/cargar_historial_evolucion.php` | `evo`, `hx --deep`, `ctx --deep` | `evolution.list` | variante simple: `id`, `fecha`, `profesional`; variante rica: además `tipo`, `diagnosticos`, `historia`, `evolucion`, `plan`, `indicaciones`, `farmacos`, `examenes`, `info_familiar`, `info_traslado` | fuerte |
| SGH | `ingreso/cargar_detalle_evolucion.php` | `evo detail`, `hx --deep` | `evolution.detail` | `historia`, `evolucion`, `plan`, `indicaciones`, `farmacos`, `examenes`, `info_familiar`, `info_traslado` | fuerte |
| SGH | `ingreso/actualizar_diagnostico_egreso.php` | `hx --deep` | `discharge_diagnosis` | `codigo`, `descripcion`, `tipo` | fuerte |
| SGH | `funciones/listado/listado_intervenciones_egreso.php` | `hx --deep` | `procedure/intervention` | `fecha`, `procedimiento`, `cirujano`, `servicio` | fuerte |
| SGH | `ingreso/ver_pdf.php?form=ing|sol|epi|con|alt` | `docs`, `doc`, `hx --deep`, `ctx --deep` | `document.sgh_pdf` | `type`, `label`, `format`, `size`, `text` | fuerte |
| SGH | `ingreso/atenciones_previas_ambulatorias.php` | `amb`, `ctx --deep` | `event.ambulatory_cae` | `establecimiento`, `fecha`, `especialidad`, `diagnostico`, `modalidad`, `cod_cita`, `cod_inst`, `cod_pacie`, `has_docs` | fuerte |
| SGH/OSIRIS | `ingreso/osiris/listadoDocumentos.php` | `amb-doc` | `document.osiris_index` | `cod_doc`, `cod_tipo`, `tipo`, `problema`, `cie10`, `fecha` | fuerte |
| SGH/OSIRIS | varios PDFs `atencion_pdf.php`, `alta_pdf.php`, etc | `amb-doc` | `document.osiris_pdf` | `format`, `size`, `text`, `error` | fuerte |
| SGH | `ingreso/atenciones_previas_aps.php` | `aps` | `event.aps` | `fecha`, `cesfam`, `motivo`, `profesional` | débil |
| LAB | `resultadoseleccion.php` | `lis`, `ctx --deep` | `event.lis_order` | `id`, `fecha`, `rut`, `nombre`, `procedencia`, `examenes`, `url_detalle`, `estado` | fuerte |
| LAB | `detalleexamenes.php` PDF | `lis-detail`, `lis --last`, `lis --altered`, `ctx --deep` | `document.lis_pdf` | `orden`, `fecha`, `muestra`, `seccion`, `resultados[]` | media |
| LAB | parsed from LIS PDF | same | `lab_result` | `examen`, `resultado`, `unidad`, `referencia`, `alterado` | media |
| SGH | `estructura/data.php` | `camas` | `ops.bed_dashboard` | agregados por estado de camas/ocupación | fuerte |
| SGH | `funciones/listado/listado_datos_camas_pacientes.php` | `sala` | `ops.room_occupancy` | tabla de camas y pacientes por sala | fuerte |

## Superficies latentes valiosas no expuestas o no canónicas aún

| Sistema | Endpoint | Tipo | Valor | Estado |
|---|---|---|---|---|
| SGH | `ingreso/cargar_ubicacion_paciente.php` | `component.current_location` | Resolver hospitalizado actual con ubicación real | latente |
| SGH | `ingreso/obt_paciente_cp.php` | `identity.lookup_by_cp` | Lookup robusto por CP | latente |
| SGH | `ingreso/cargar_historia_ingreso.php` | `component.admission_history` | Historia del ingreso actual, separada de evoluciones | latente |
| SGH | `ingreso/buscar_ultima_evolucion.php` | `component.latest_evolution_ref` | Shortcut limpio a última evolución | latente |
| SGH | `ingreso/verificarUltimaEvolucion.php` | `component.latest_evolution_id` | Resolve id de la última evolución del día | latente |
| SGH | `ingreso/cargar_complementos_evolucion.php` | `component.evolution_complements_count` | Conteos de procedimientos/IIH/exámenes/intervenciones | latente |
| SGH | `ingreso/data_diagnostico_principal.php` | `component.principal_diagnosis` | Dx principal estructurado | latente, con incidentes históricos |
| SGH | `funciones/listado/listado_recetas_evolucion.php` | `component.prescriptions_inpatient` | Recetas del ingreso | latente |
| SGH | `funciones/listado/listado_recetas_espera_tab.php` | `component.prescriptions_longitudinal` | Historial de recetas | latente |
| SGH | `ingreso/cargar_receta_seleccionada.php` | `document/prescription_detail` | Receta específica | latente |
| SGH | `ingreso/detalleReceta.php` | `component.active_prescription_table` | Tabla activa de medicación | latente |
| SGH | `ingreso/lista_espera.php` | `event.future_appointment_or_waitlist` | Más cercano a agenda/citas reales | latente |
| SGH | `ingreso/datosCate.php` | `component.categorization_index` | Barthel/SIC y categorizaciones | latente |
| SGH | `categorizaciones/barthel_encuesta_cargar.php` | `component.barthel` | Dependencia funcional detallada | latente |
| SGH | `categorizaciones/categorizacion_encuesta_cargar.php` | `component.sic_categorization` | Categorización clínica detallada | latente |
| SGH | `tab interconsultas` + `guardar_sic.php` + `ver_sic_nuevo.php` | `component.interconsult` | Interconsultas longitudinales | latente |
| SGH | `ingreso/osiris/documentosGes/*.php` | `document.osiris_ges_*` | Documentos GES con valor documental alto | parcialmente usado como fallback de tipo, no canónico |
| DAU | `atencion/datos_ingreso.php` | `identity+event_meta` | Nombre, sexo, previsión, fecha admisión, teléfono, parte de identidad fuerte | parcialmente usado en fallback, no canónico |
| DAU | `obtener_indicaciones_alta.php` | `component.discharge_indications` | Cierre/documento de alta del episodio | latente |
| DAU | `obtener_examen_observacion.php` | `component.exam_observation` | Notas densas pegadas a exámenes/observación | latente importante |
| DAU | `obtener_lista_recetas.php` | `component.recipes_dau` | Recetas del episodio | latente |
| DAU | `obtener_destino_consultante.php` | `component.disposition` | Destino/disposición del episodio | latente |
| DAU | `obtener_destino_pertinencia.php` | `component.pertinence` | Pertinencia / disposición | latente |
| DAU | `s_guarda_alcoholemia_grado_lesion_dev.php` | `document.alcoholemia` | Módulo médico-legal | latente |
| DAU | `s_guarda_muestra_toxicologica.php` | `component.toxicology_sample` | Muestra toxicológica | latente |
| DAU | `obtener_del_sex.php` | `component.sexual_assault` | Módulo delito sexual | latente |
| DAU | `busca_uego.php` | `component.uego` | Gineco-obstetricia UEGO | latente |
| DAU | `obtener_visor_aps.php` | `document.viewer_aps` | Visor APS desde DAU | latente/inestable |
| DAU | `obtener_visor_atencion_ambulatoria_osiris.php` | `document.viewer_osiris` | Visor OSIRIS desde DAU | latente |

## Qué debería pasar a `event-components` primero

### current_urgency

Componentes mínimos:

- `event_meta`
- `triage`
- `vitals.initial`
- `vitals.serial`
- `anamnesis`
- `physical_exam`
- `hypothesis`
- `diagnosis`
- `observation`
- `lab_order`
- `image_order`
- `indication`
- `allergy`
- `disposition` cuando se mapee

### urgency history

Componentes mínimos:

- `event_meta`
- `document.dau_print`
- `anamnesis` heurística desde DAU printable
- `physical_exam` heurística desde DAU printable
- `hypothesis` heurística desde DAU printable
- `diagnosis` heurística desde DAU printable
- `indication` heurística desde DAU printable

### hospitalization

Componentes mínimos:

- `event_meta`
- `document.sgh_ingreso`
- `document.sgh_epicrisis`
- `document.sgh_alta`
- `evolution.list`
- `evolution.detail`
- `principal_diagnosis` cuando se aisle bien
- `discharge_diagnosis`
- `procedure`
- `current_location` cuando se exponga

### ambulatory_cae

Componentes mínimos:

- `event_meta`
- `document.osiris_index`
- `document.osiris_pdf`
- `document_text`
- `diagnosis` extraíble luego desde texto o índice documental

### lis_order

Componentes mínimos:

- `event_meta`
- `document.lis_pdf`
- `lab_result`

## Qué está sobrecargado hoy y conviene partir

### `ClinicalNote`

Hoy mezcla:

- `anamnesis`
- `examen_fisico`
- `hipotesis`
- potencialmente `observacion`
- potencialmente `indicaciones`

En V2 conviene que siga existiendo como agregado, pero que también se puedan pedir sus subcomponentes.

### `Medication`

En DAU hoy `Medication` está reutilizado para indicaciones y se usa `Via` para guardar `estado`. Eso funciona para pantalla, pero semánticamente está torcido. Conviene partir en:

- `indication`
- `medication_visible`

### `LabResult` DAU

En DAU hoy `LabResult` es casi una orden/resumen, no un resultado cuantitativo. Conviene separar:

- `lab_order` para DAU
- `lab_result` para LIS/PDFs cuantitativos

## Deuda de modelo detectada

1. `Patient` todavía carga demasiada semántica transversal y mezcla identidad con estado actual.
2. `Medication`, `LabResult` y parte de `Observation` están siendo usados como contenedores reutilizados, no como modelos exactos.
3. El parser `ParseSGHPatientSearch` promete `cama/servicio` pero no los entrega; eso contamina la intuición de la capa canónica.
4. Parte del valor documental más fuerte sigue encapsulado en texto libre de PDFs; hace falta `doc-components` para extraer sin resumir.

## Prioridad de exposición siguiente

1. `current_location` SGH desde `cargar_ubicacion_paciente.php`
2. `future_appointments/waitlist` desde `lista_espera.php`
3. `prescriptions_longitudinal` SGH
4. `interconsults` SGH
5. `exam_observation` DAU
6. `disposition` y `discharge_indications` DAU
7. módulos médico-legales DAU

## Conclusión

La granularidad real ya está bastante avanzada. El problema no es ausencia total de datos sino falta de una ontología estable para:

- nombrar correctamente cada ingrediente
- separar órdenes de resultados
- separar documento de componente
- separar identidad de presencia actual

Con esta base, `event-components` puede implementarse mayormente como reencuadre y composición de parsers ya existentes, no como greenfield.