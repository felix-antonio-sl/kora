---
_manifest:
  urn: urn:hi:kb:atomic-codex-asclepius-ai-healthcare-04
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/ia med.md — atomizacion Codex
      Asclepius (AI for Improving Healthcare); output de /atomize 2026-04-10
version: 1.0.0
status: borrador
tags:
- atomic
- ai
- healthcare
- codex-asclepius
- hi
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 53
      producer: urn:kora:artefacto:atomize
      source_corpus: Codex Asclepius — AI for Improving Healthcare
      segmented: true
      segment_role: segment
      hand_edited: true
      segment_index: 4
      segment_count: 4
---

# Codex Asclepius - Segmento 04

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/ia med.md`
- Proposiciones: `53`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `04/04`
- Rango: `P601-P653`

## Indice de fuentes

- `S01` · [ia med.md](../../INBOX/hi/ia med.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 04 del corpus atomizado.

- **P601** · `requirement` · When buying AI tools, thorough understanding of underlying data and quality essential to appraise limitations/benefits; when developing models, high-quality data = key determinant of success · [src:S01](../../INBOX/hi/ia med.md)
- **P602** · `fact` · Interoperability embraces technical aspects (protocols), semantic aspects (terminology/coding), data model aspects (properties, structure, interrelationships) · [src:S01](../../INBOX/hi/ia med.md)
- **P603** · `fact` · Data biases cause invalid AI models and exacerbate health disparities; result from incorrect, inconsistent, irrelevant data, meaningless variables, missing data · [src:S01](../../INBOX/hi/ia med.md)
- **P604** · `fact` · In supervised learning, human expert data labeling is cumbersome and error-prone; biases must be accompanied by metadata describing provenance/formation · [src:S01](../../INBOX/hi/ia med.md)
- **P605** · `obligation` · Healthcare professionals must evolve from passive consumers to active participants in data evaluation; liability for diagnostic/treatment/care decisions puts them in "driver's seat" · [src:S01](../../INBOX/hi/ia med.md)
- **P606** · `fact` · When non-anonymized data processed, informed consent required by law in many countries (absent legal base for processing); data protection laws directly impact opportunities for AI model training · [src:S01](../../INBOX/hi/ia med.md)
- **P607** · `tension` · Breakneck speed of AI developments often exceeds time needed for ethical discourses and laws to be put in place · [src:S01](../../INBOX/hi/ia med.md)

### The Nature of Medical and Health Data
- **P608** · `rule` · "More data → better models" demonstrated outside healthcare; routine patient data different due to sensitivity restrictions limiting sheer number · [src:S01](../../INBOX/hi/ia med.md)
- **P609** · `constraint` · EU GDPR: access to non-anonymized personal data only permitted by law or via patient informed consent; data use beyond original purpose requires patient permission · [src:S01](../../INBOX/hi/ia med.md)
- **P610** · `constraint` · US HIPAA protects patient health information in corresponding way to GDPR · [src:S01](../../INBOX/hi/ia med.md)
- **P611** · `fact` · Rare diseases inherently limit available data volume; manual expert labeling costs/time can also lead to small datasets · [src:S01](../../INBOX/hi/ia med.md)
- **P612** · `definition` · Overfitting (small dataset problem) = learning from noise/details specific to dataset → poor performance on new unseen data · [src:S01](../../INBOX/hi/ia med.md)
- **P613** · `definition` · Lack of generalization (small dataset problem) = model does not capture diversity/variability of underlying data distribution → less effective in real-world applications · [src:S01](../../INBOX/hi/ia med.md)
- **P614** · `definition` · Bias in dataset (small dataset problem) = skewed/discriminatory models → poor performance on new/unseen data · [src:S01](../../INBOX/hi/ia med.md)
- **P615** · `definition` · Limited feature representation (small dataset problem) = important features/patterns missing → incomplete models · [src:S01](../../INBOX/hi/ia med.md)
- **P616** · `definition` · Unreliable evaluation metrics (small dataset problem) = standard metrics (accuracy, loss) may not reliably reflect actual model performance → unclear performance · [src:S01](../../INBOX/hi/ia med.md)
- **P617** · `fact` · Mitigation methods for small datasets: transfer learning (pre-training on large general datasets like ImageNet), data augmentation including synthetic data, cross-validation · [src:S01](../../INBOX/hi/ia med.md)
- **P618** · `fact` · Data spread across departments/institutions/regions/countries not interoperable = additional cause of small effective datasets · [src:S01](../../INBOX/hi/ia med.md)
- **P619** · `fact` · Common international health IT standards: HL7 FHIR, openEHR; terminologies: SNOMED CT · [src:S01](../../INBOX/hi/ia med.md)
- **P620** · `definition` · OMOP = Observational Medical Outcomes Partnership; aims to standardize healthcare data for large-scale observational studies by creating consistent format from diverse sources (EHRs, claims, registries) · [src:S01](../../INBOX/hi/ia med.md)
- **P621** · `definition` · OMOP CDM = Common Data Model defining standardized structure for healthcare data: tables for conditions, drugs, procedures, measurements, observations, devices, specimens, visits, provider · [src:S01](../../INBOX/hi/ia med.md)
- **P622** · `fact` · OMOP CDM comprises: standardized clinical data, standardized health system, standardized health economics, standardized vocabulary, standardized derived data, standardized metadata, results schema · [src:S01](../../INBOX/hi/ia med.md)
- **P623** · `fact` · OMOP employs standardized vocabularies: SNOMED CT for clinical terms, LOINC for laboratory tests · [src:S01](../../INBOX/hi/ia med.md)
- **P624** · `fact` · Once OMOP CDM-compliant data available, open-source tools for data quality/characterization can be applied for exploratory and hypothesis-driven analyses · [src:S01](../../INBOX/hi/ia med.md)
- **P625** · `definition` · FAIR = Findable, Accessible, Interoperable, Reusable; principles for standardization, interoperability, good organization of data · [src:S01](../../INBOX/hi/ia med.md)
- **P626** · `definition` · Findable = datasets registered with unique identifiers and indexed in searchable databases; example: DRYAD repository · [src:S01](../../INBOX/hi/ia med.md)
- **P627** · `definition` · Accessible = crucial health data available when needed while respecting privacy/security regulations; example: HIPAA/GDPR implementations · [src:S01](../../INBOX/hi/ia med.md)
- **P628** · `definition` · Interoperable = implementing standardized data formats and healthcare communication protocols; example: HL7 FHIR, SNOMED CT · [src:S01](../../INBOX/hi/ia med.md)
- **P629** · `definition` · Reusable = datasets under open licenses with detailed documentation/metadata on collection methods and context; example: DRYAD repository · [src:S01](../../INBOX/hi/ia med.md)
- **P630** · `fact` · FAIRification process = centerpiece of research data management; applies to metadata, data, supporting infrastructures (e.g., search engines) · [src:S01](../../INBOX/hi/ia med.md)
- **P631** · `fact` · Findability/accessibility implemented at metadata level; interoperability/reuse requirements address data level · [src:S01](../../INBOX/hi/ia med.md)

### Data Quality Is First
- **P632** · `definition` · Accuracy = degree data correctly describes real-world object/event; expressed as structural accuracy (syntactic + semantic) and time-related accuracy (currency, volatility, timeliness) · [src:S01](../../INBOX/hi/ia med.md)
- **P633** · `fact` · Accuracy metric: percentage of data entries without errors · [src:S01](../../INBOX/hi/ia med.md)
- **P634** · `definition` · Completeness = extent data are of sufficient breadth, depth, scope for task at hand; missing values/tuples/attributes/relations; temporal dimension = completability · [src:S01](../../INBOX/hi/ia med.md)
- **P635** · `fact` · Completeness metric: ratio of filled data fields vs total fields or percentage of missing values; completability measured by growth rate of completeness over time · [src:S01](../../INBOX/hi/ia med.md)
- **P636** · `definition` · Accessibility (data quality) = ease with which data can be obtained and used legally/ethically · [src:S01](../../INBOX/hi/ia med.md)
- **P637** · `fact` · Accessibility metric: subjective ease of access or amount of effort/time to retrieve data · [src:S01](../../INBOX/hi/ia med.md)
- **P638** · `definition` · Consistency = compliance with semantic rules defined over data items; absence of contradictions within dataset or among different datasets · [src:S01](../../INBOX/hi/ia med.md)
- **P639** · `fact` · Consistency metric: rate of data entries without logical/matched consistency with related data fields or datasets · [src:S01](../../INBOX/hi/ia med.md)
- **P640** · `fact` · Additional data quality characteristics: redundancy (minimality, conciseness, normalization), readability (comprehensibility, clarity), usefulness (user advantages), trust (reliability, data security) · [src:S01](../../INBOX/hi/ia med.md)
- **P641** · `rule` · Data quality not free nor pure technical task; ensuring/improving it = critical organizational and leadership task relying on data governance policies · [src:S01](../../INBOX/hi/ia med.md)
- **P642** · `fact` · Data governance policies should draw on FAIR principles and OMOP CDM; embrace data quality culture, assessment/auditing, documentation, monitoring · [src:S01](../../INBOX/hi/ia med.md)
- **P643** · `definition` · Data stewards = role embracing structural/procedural aspects of data management: acquisition, storage, aggregation, de-identification, data provision; conceptualized in data governance policies · [src:S01](../../INBOX/hi/ia med.md)
- **P644** · `fact` · Data steward role gaining increasing relevance with advent of data-driven AI and large data volumes; some recommendations speak of "FAIR data steward" · [src:S01](../../INBOX/hi/ia med.md)
- **P645** · `fact` · Clinical experts produce/collect/label data for AI training, perform quality control with analytical software, do plausibility checks of AI output with critical datasets · [src:S01](../../INBOX/hi/ia med.md)

### Conclusions and Outlook
- **P646** · `fact` · Medical/healthcare datasets can be rather small vs other domains; inherent reasons (rare diseases) + changeable reasons (lack of interoperability) · [src:S01](../../INBOX/hi/ia med.md)
- **P647** · `definition` · EHDS (European Health Data Space) = EU initiative for use/exchange of electronic health data across EU; stimulates primary use (healthcare delivery, cross-border sharing) and secondary use (research, innovation, AI) · [src:S01](../../INBOX/hi/ia med.md)
- **P648** · `deadline` · EHDS Regulation entered into force March 2025 · [src:S01](../../INBOX/hi/ia med.md)
- **P649** · `deadline` · EHDS primary use scenarios implementation planned for 2029 · [src:S01](../../INBOX/hi/ia med.md)
- **P650** · `deadline` · EHDS secondary use scenarios implementation planned for 2031 · [src:S01](../../INBOX/hi/ia med.md)
- **P651** · `fact` · EHDS regards individuals as gatekeepers for access, control, sharing of their electronic health data · [src:S01](../../INBOX/hi/ia med.md)
- **P652** · `fact` · EHDS = example of opening health data on very large scale in trustworthy manner, offering opportunities for AI based on truly big data · [src:S01](../../INBOX/hi/ia med.md)
- **P653** · `fact` · Data in dual role as representatives of real world and fuel for AI constitute bridge between artificial intelligence and human intelligence · [src:S01](../../INBOX/hi/ia med.md)
