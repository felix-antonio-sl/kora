---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:medico-urgencias-tools:1.1.0"
  type: "bootstrap_tools"
---

## parse_clinical_input

- **Firma:** xml_tags: string -> ClinicalData{historia_antigua, derivacion, informacion_atencion, imagenes_clinicas, tipo_output}
- **Cuando usar:** Al recibir info paciente en etiquetas XML. Primer paso en S-RECEPTOR.
- **Cuando NO usar:** Si datos ya parseados en turno actual.
- **Notas:** Acepta texto e imagenes en <imagenes_clinicas>. Si imagenes presentes, invocar skill CM-interpretador-imagenes.

## analyze_image

- **Firma:** image_or_report: string|image -> PivoteImagenologico{modalidad, hallazgos_relevantes, correlacion_clinica, red_flags, urgencia}
- **Cuando usar:** Cuando <imagenes_clinicas> contiene informe radiologico o imagen directa (Rx, ECO, TAC). Requiere capacidad multimodal para imagenes directas.
- **Cuando NO usar:** Si no hay datos imagenologicos. Si imagen no es clinica.
- **Notas:** Parsimonia: omitir hallazgos incidentales, descripciones normales, detalles tecnicos, variantes anatomicas sin relevancia.
