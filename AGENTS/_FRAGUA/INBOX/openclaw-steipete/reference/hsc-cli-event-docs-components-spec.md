# hsc-cli — Event / Docs / Components Specification

Status: proposed canonical extraction spec
Date: 2026-04-14
Product: `h` CLI in `/home/felix/projects/hsc-cli`

This document defines the next semantic center of `hsc-cli`.

The CLI is no longer framed primarily around:
- patient summaries
- clinical context bundles
- narrative history outputs

The CLI is framed around:
- `identity`
- `event`
- `document`
- `component`

The product role is:
- fetch real system data
- normalize identifiers
- extract granular ingredients cleanly
- attach dense documentary payloads where available
- stop before clinical interpretation

Short version:
- `h` is the supermarket
- another actor cooks

---

## 1. Mission shift

The CLI should produce:
- raw but well-extracted data
- stable JSON shapes
- event-centric documentary payloads
- granular components derived from source systems and PDFs

The CLI should not produce:
- clinical summaries
- longitudinal narratives as a final product
- diagnostic prioritization
- treatment recommendations
- handoff prose as the main semantic center

Those belong to the downstream clinical agent.

---

## 2. Core ontology

## Identity
Canonical patient resolution and runtime keys.

Identity is responsible for:
- resolving `RUT`
- resolving `CP`
- resolving `atencion_id`
- resolving `ingreso_id`
- exposing current active references when available

Identity is not itself clinical knowledge.

## Event
A longitudinal or runtime occurrence involving the patient.

Examples:
- current urgency episode
- prior urgency encounter
- hospitalization
- ambulatory CAE visit
- APS visit
- LIS order

An event is:
- a bounded occurrence
- tied to one or more source identifiers
- optionally associated with one or more documents
- optionally decomposable into granular components

## Document
A dense payload associated with an event.

Examples:
- DAU printable record
- SGH epicrisis
- SGH admission note
- SGH discharge document
- SGH consent
- SGH solicitud
- OSIRIS ambulatory documents
- LIS order PDF

A document is:
- denser than the row/table that points to it
- often the best compression surface in the whole system
- parseable into components

## Component
A granular extracted part from an event or document.

Examples:
- anamnesis
- motivo de consulta
- vital signs row
- diagnosis item
- plan
- indication
- lab result item
- intervention
- discharge diagnosis
- document metadata

Components are:
- low-interpretation
- source-traceable
- reusable by other actors

---

## 3. Source systems and their natural products

## DAU
Natural products:
- current urgent runtime
- triage
- vital signs
- note fragments
- indications
- observations
- current order surfaces
- historical DAU printable artifact

Natural question:
- what happened in this urgency episode?

## SGH
Natural products:
- longitudinal event rows
- hospitalization shell
- evolutions
- dense hospitalization documents
- ambulatory CAE visits
- OSIRIS documentary layer
- occupancy and active hospitalization state

Natural question:
- what events and documents exist across time?

## OSIRIS
Natural products:
- ambulatory documentary payloads tied to CAE visits

Natural question:
- what documentary artifact exists for this ambulatory encounter?

## LIS
Natural products:
- lab orders
- validated result PDFs
- parsed analyte-level results

Natural question:
- what analyte facts exist for this laboratory order?

---

## 4. Canonical contracts

## 4.1 Identity contract

```json
{
  "identity_id": "rut:7708189-5",
  "rut": "7708189-5",
  "cp": 176365,
  "nombre": "NOMBRE PACIENTE",
  "edad": 44,
  "sexo": "Masculino",
  "fecha_nac": "",
  "prevision": "",
  "domicilio": "",
  "telefono": "",
  "comuna": "",
  "active_refs": {
    "atencion_id": 4000607,
    "ingreso_id": 12345,
    "servicio": "",
    "cama": "",
    "fecha_ingreso": "",
    "dx_ingreso": ""
  }
}
```

Notes:
- `active_refs` exposes runtime pivots.
- This object stays factual and non-interpretive.

## 4.2 Event contract

```json
{
  "event_id": "hospitalization:sgh:12345",
  "kind": "hospitalization",
  "source": "sgh",
  "identity_ref": {
    "rut": "7708189-5",
    "cp": 176365
  },
  "refs": {
    "atencion_id": 0,
    "ingreso_id": 12345,
    "cod_cita": "",
    "cod_inst": "",
    "cod_pacie": "",
    "lis_order_id": ""
  },
  "meta": {
    "fecha": "01-04-2026",
    "estado": "egresado",
    "diagnostico": "texto crudo",
    "establecimiento": "HSC",
    "servicio": "Medicina"
  },
  "documents": [],
  "components": []
}
```

Rules:
- every event must have a stable `event_id`
- every event must expose its raw source refs
- `documents` lists dense payloads tied to this event
- `components` contains granular extracted ingredients

## 4.3 Document contract

```json
{
  "doc_id": "sgh:epi:12345",
  "event_id": "hospitalization:sgh:12345",
  "type": "epicrisis",
  "source": "sgh",
  "format": "pdf",
  "size": 0,
  "metadata": {
    "fecha": "",
    "label": "epicrisis"
  },
  "raw_text": "",
  "components": [],
  "error": ""
}
```

Rules:
- documents remain directly inspectable
- raw extracted text should be preserved
- downstream agents can ignore `components` and parse `raw_text` if needed
- `components` are a convenience layer, not the only truth

## 4.4 Component contract

```json
{
  "component_id": "diag:principal:1",
  "kind": "diagnosis",
  "source": "sgh_epicrisis_pdf",
  "event_id": "hospitalization:sgh:12345",
  "doc_id": "sgh:epi:12345",
  "data": {
    "codigo": "J18.9",
    "descripcion": "Neumonía, no especificada",
    "tipo": "principal"
  }
}
```

Rules:
- components should be small and typed
- keep provenance in the component
- no clinical interpretation layer is added here

---

## 5. Event kinds supported by the current repo mapping

## 5.1 `current_urgency`

Meaning:
- active DAU urgent encounter

Base mapping:
- `DAU atencion/index.php`
- `DAU triageprueba/listadoTriage.php`
- `DAU atencion/obtener_listado_signos_vitales.php`
- `DAU atencion/obtener_anamnesis.php`
- `DAU atencion/obtener_examen_fisico.php`
- `DAU atencion/obtener_hipotesis.php`
- `DAU atencion/obtener_cie.php`
- `DAU atencion/obtener_lista_sic.php`
- `DAU atencion/obtener_lista_exa_laboratorio.php`
- `DAU atencion/obtener_lista_exa_rayo.php`
- `DAU atencion/obtener_lista_exa_scanner.php`
- `DAU atencion/obtener_lista_indicaciones.php`

Primary refs:
- `atencion_id`
- `codAdmision`
- `codPacie`

Documents:
- none as primary row payload
- may attach current `dau_p.php` only when that surface is confirmed meaningful for active episode

Components:
- triage
- allergies
- vital_signs
- anamnesis
- physical_exam
- diagnostic_hypothesis
- diagnosis
- observation
- lab_order
- image_order
- indication

Current code:
- `h tri`
- `h sv`
- `h nota`
- `h dx`
- `h obs`
- `h labs`
- `h img`
- `h rx`
- `h alx`
- `h dau read`

## 5.2 `urgency`

Meaning:
- prior urgent encounter surfaced in SGH

Base mapping:
- `SGH ingreso/atenciones_previas.php`

Document bridge:
- `DAU atencion/dau_p.php` using extracted `cod_atencion`

Primary refs:
- `atencion_id`

Documents:
- `dau`

Components:
- event row metadata
- DAU print text
- anamnesis
- physical_exam
- diagnostic_hypothesis
- indications
- diagnosis list

Current code:
- `h hx`
- `h hx --deep`
- `h dau <cod_atencion>`

## 5.3 `hospitalization`

Meaning:
- inpatient encounter in SGH

Base mapping:
- `SGH ingreso/ver_paciente.php`

Enrichment:
- `SGH ingreso/cargar_historial_evolucion.php`
- `SGH ingreso/cargar_detalle_evolucion.php`
- `SGH ingreso/ver_pdf.php`
- `SGH ingreso/actualizar_diagnostico_egreso.php`
- `SGH funciones/listado/listado_intervenciones_egreso.php`

Primary refs:
- `ingreso_id`

Documents:
- `ing`
- `sol`
- `epi`
- `con`
- `alt`

Components:
- event row metadata
- evolution entry
- evolution detail
- discharge diagnosis
- intervention
- document text

Current code:
- `h hx`
- `h hx --deep`
- `h evo`
- `h evo detail`
- `h docs`
- `h doc`

## 5.4 `ambulatory_cae`

Meaning:
- SGH/OSIRIS ambulatory specialty care event

Base mapping:
- `SGH ingreso/atenciones_previas_ambulatorias.php`

Document bridge:
- `SGH ingreso/osiris/listadoDocumentos.php`
- OSIRIS PDF endpoints (`atencion_pdf.php`, `alta_pdf.php`, etc.)

Primary refs:
- `cod_cita`
- `cod_inst`
- `cod_pacie`
- `modalidad`

Documents:
- OSIRIS documents returned by `listadoDocumentos.php`

Components:
- ambulatory visit metadata
- document list rows
- parsed OSIRIS text once fetched

Current code:
- `h amb`
- `h amb-doc`

Gap:
- event and document layers are not yet unified under one event envelope

## 5.5 `aps`

Meaning:
- APS event surfaced through SGH legacy launcher

Base mapping:
- `SGH ingreso/atenciones_previas_aps.php`

Current status:
- parser exists
- launcher semantics remain unstable

Rule:
- do not treat APS as a strong canonical event family until launcher failure vs real empty data is modeled explicitly

## 5.6 `lis_order`

Meaning:
- laboratory order/result document from LIS

Base mapping:
- `LAB resultadoseleccion.php`

Document bridge:
- `LAB detalleexamenes.php`

Primary refs:
- `order_id`

Documents:
- LIS result PDF

Components:
- section
- analyte result
- unit
- reference range
- altered flag

Current code:
- `h lis`
- `h lis-detail`

---

## 6. Document kinds supported by the current repo mapping

| Type | Source | Current extraction path | Current state |
|---|---|---|---|
| `dau` | DAU | `atencion/dau_p.php` | works |
| `ingreso` | SGH | `ingreso/ver_pdf.php?form=ing` | works |
| `solicitud` | SGH | `ingreso/ver_pdf.php?form=sol` | works |
| `epicrisis` | SGH | `ingreso/ver_pdf.php?form=epi` | works |
| `consentimiento` | SGH | `ingreso/ver_pdf.php?form=con` | works |
| `alta` | SGH | `ingreso/ver_pdf.php?form=alt` | works |
| `osiris_document` | OSIRIS | `osiris/listadoDocumentos.php` + PDF fetch | partial, split across commands |
| `lis_result_pdf` | LIS | `detalleexamenes.php` | works |

Rule:
- if a row points to a document, the event layer should attach it
- if a document exists, the CLI should parse it eagerly in deep mode

---

## 7. Canonical component kinds

The CLI should standardize component types independent of source system naming.

Canonical kinds:
- `triage`
- `allergy`
- `vital_sign`
- `anamnesis`
- `physical_exam`
- `diagnostic_hypothesis`
- `diagnosis`
- `observation`
- `indication`
- `lab_order`
- `image_order`
- `lab_result`
- `evolution`
- `evolution_detail`
- `discharge_diagnosis`
- `intervention`
- `document_text`
- `document_metadata`

Rule:
- same semantic kind across systems should reuse the same component kind when possible
- source-specific differences remain in `source` and `data`

---

## 8. Recommended command surface V2

This is the target semantic surface.

## Identity
- `h identity <id>`

## Events
- `h events <id>`
- `h event <event_id>`
- `h event-docs <event_id>`
- `h event-components <event_id>`

## Documents
- `h doc get <doc_id>`
- `h doc components <doc_id>`

## Current urgency primitives
- `h urgency <id>`
- `h triage <id>`
- `h vitals <id>`
- `h note <id>`
- `h dx <id>`
- `h obs <id>`
- `h lab-orders <id>`
- `h image-orders <id>`
- `h indications <id>`
- `h allergies <id>`

## LIS primitives
- `h lis-orders <id>`
- `h lis-order <order_id>`

Compatibility guidance:
- existing commands remain initially as compatibility aliases
- `ctx`, `patient`, `handoff`, and draft surfaces become explicitly secondary

---

## 9. Existing commands mapped into the new ontology

| Existing command | Event/docs/components role |
|---|---|
| `h who` | identity |
| `h box` | current urgency board |
| `h cola` | current urgency board |
| `h tri` | component extraction |
| `h sv` | component extraction |
| `h nota` | component extraction |
| `h dx` | component extraction |
| `h obs` | component extraction |
| `h labs` | component extraction for DAU orders |
| `h img` | component extraction for image orders |
| `h rx` | component extraction for indications |
| `h alx` | component extraction |
| `h dau read` | current urgency composite, legacy |
| `h hx` | event listing composite, legacy |
| `h hx --deep` | event deep enrich, legacy |
| `h evo` | hospitalization component extraction |
| `h docs` / `h doc` | document retrieval |
| `h amb` | ambulatory event listing |
| `h amb-doc` | ambulatory document retrieval |
| `h aps` | APS event listing, unstable |
| `h lis` | LIS order listing |
| `h lis-detail` | LIS document + analyte components |
| `h patient` | patient-centered composite, legacy |
| `h ctx` | cross-system composite, legacy |
| `h handoff` | shift-oriented composite, legacy |

---

## 10. Implementation rules

## Rule 1
Every event row should be able to expose:
- its raw refs
- its associated docs
- its extracted components

## Rule 2
Document parsing should happen close to retrieval.

Do not force downstream agents to rediscover:
- which PDF belongs to which row
- which endpoint to call next
- which IDs are required to fetch the dense artifact

## Rule 3
Components should stay factual.

Bad:
- "probable sepsis"

Good:
- diagnosis component
- triage component
- altered lactate lab result
- hypotension vital signs row

## Rule 4
Deep mode should mean:
- fetch event
- fetch all mapped documents
- parse all mapped documents
- extract granular components

It should not mean:
- synthesize a clinical narrative

## Rule 5
Legacy composite commands remain allowed, but they stop being the primary semantic model.

Primary semantic model becomes:
- `identity`
- `events`
- `docs`
- `components`

---

## 11. Immediate execution order

1. Introduce stable `event_id` and `doc_id` generation for mapped event families.
2. Refactor `hx --deep` internals into reusable `events` / `event` builders.
3. Unify SGH hospitalization docs and DAU historical docs under one document contract.
4. Unify `amb` + `amb-doc` under ambulatory event deep retrieval.
5. Promote LIS order detail into first-class event/document/component semantics.
6. Expose `event-docs` and `event-components`.
7. Only after that, decide whether `ctx` and `patient` should survive as compatibility helpers.

---

## 12. Strategic conclusion

`hsc-cli` should stop centering:
- history as prose
- context as interpretation
- patient summary as a product

`hsc-cli` should center:
- events as bounded occurrences
- documents as dense payloads
- components as reusable clinical ingredients

This keeps the CLI:
- extractive
- agent-friendly
- reusable across multiple downstream actors
- honest about its role in the stack

The CLI buys and cleans ingredients.
Another actor cooks.
