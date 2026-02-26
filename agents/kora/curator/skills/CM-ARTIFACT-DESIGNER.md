---
_manifest:
  urn: "urn:kora:skill:curator-artifact-designer:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-ARTIFACT-DESIGNER

## Proposito
Planifica la estructura de un nuevo artefacto de conocimiento KORA: determina tipo, namespace, fuente, jerarquia de headings y metadatos.

## I/O

- **Input:** intencion: IntentClassification (del CM-INTENT-CLASSIFIER), fuentes: Document[] | null (documentos fuente si existen)
- **Output:** ArtifactPlan (ver Signature Output)

## Procedimiento
1. ELICITAR DOMINIO: ¿Que conocimiento captura? ¿Descriptivo(hechos) o prescriptivo(reglas)? ¿En que namespace vive? ¿Que fuentes tiene?
2. DETERMINAR TIPO:
   - Descriptivo (KORA/MD): hechos, datos, procedimientos, leyes, manuales → spec rectora: md-spec
   - Prescriptivo (KORA/Spec-MD): reglas, specs, protocolos, workflows, guias operativas → spec rectora: spec-md
3. DEFINIR URN: formato urn:{namespace}:kb:{id}. ID en kebab-case, semanticamente expresivo.
4. EVALUAR INPUT (si hay documento fuente):
   - Largo: <5K tokens(directo), 5K-15K(segmentado), >15K(segmentado + verificacion adversarial)
   - Estructura: headings claros(segmentar por headings) vs prosa monolitica(segmentar por temas ~1-2K tokens)
   - Contenido numerico: alto(verificacion mecanica obligatoria) vs bajo(verificacion opcional)
5. PLANIFICAR ESTRUCTURA: headings principales(##), sub-headings(###), elementos clave(tablas, listas).
6. DEFINIR FRONTMATTER: urn, provenance(author, date, source), version(1.0.0), status(draft), tags(min 3), lang.
7. Presentar plan al usuario: tabla con tipo, namespace, URN, estructura propuesta, fuentes, estrategia de ejecucion.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo | enum(descriptivo\|prescriptivo) | Tipo de artefacto determinado |
| namespace | string | Namespace KORA destino |
| urn | string | URN asignado al artefacto |
| fuente | string | Identificacion de fuente(s) |
| largo_estimado | string | Estimacion de tokens del input |
| estrategia | enum(directa\|segmentada\|segmentada+adversarial) | Estrategia de ejecucion |
| estructura_propuesta | string[] | Headings planificados |
| frontmatter | object | Metadata YAML planificada |
