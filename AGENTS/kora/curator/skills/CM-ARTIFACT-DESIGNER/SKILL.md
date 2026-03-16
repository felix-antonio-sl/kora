---
_manifest:
  urn: urn:kora:skill:curator-artifact-designer:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - spec_consult
        - artifact_list
      requires: []
      references:
        - references/design-basis.md
      assets:
        - assets/frontmatter-examples.md
        - assets/design-checklist.md
---

# CM-ARTIFACT-DESIGNER

## Proposito
Planifica la estructura de un nuevo artefacto de conocimiento KORA: determina tipo, namespace, fuente, jerarquia de headings y metadatos, apoyandose en la base normativa del pipeline, familias documentales y ejemplos de frontmatter ya existentes en el repo.

## Input/Output
- **Input:** intencion: IntentClassification (del CM-INTENT-CLASSIFIER), fuentes: Document[] | null (documentos fuente si existen)
- **Output:** ArtifactPlan (ver Signature Output)

## Procedimiento
1. Cargar `references/design-basis.md` para fijar:
   - eleccion de funtor
   - pipeline `inbox -> source -> drafts -> knowledge`
   - familias documentales y sus invariantes
2. Usar `assets/design-checklist.md` para recorrer el diseno antes de emitir el plan.
3. ELICITAR DOMINIO: ¿Que conocimiento captura? ¿Descriptivo(hechos) o prescriptivo(reglas)? ¿En que namespace vive? ¿Que fuentes tiene?
4. DETERMINAR TIPO:
   - Descriptivo (KORA/MD): hechos, datos, procedimientos, leyes, manuales → spec rectora: md-spec
   - Prescriptivo (KORA/Spec-MD): reglas, specs, protocolos, workflows, guias operativas → spec rectora: spec-md
5. DEFINIR URN: formato urn:{namespace}:kb:{id}. ID en kebab-case, semanticamente expresivo.
6. EVALUAR INPUT (si hay documento fuente):
   - Largo: <5K tokens(directo), 5K-15K(segmentado), >15K(segmentado + verificacion de fidelidad reforzada)
   - Estructura: headings claros(segmentar por headings) vs prosa monolitica(segmentar por temas ~1-2K tokens)
   - Contenido numerico: alto(verificacion mecanica obligatoria) vs bajo(verificacion opcional)
   - Familia documental: persistirla luego en `extensions.kora.family` cuando aplique
7. PLANIFICAR ESTRUCTURA: headings principales(##), sub-headings(###), elementos clave(tablas, listas).
8. DEFINIR FRONTMATTER usando `assets/frontmatter-examples.md`: urn, provenance(author, date, source), version(1.0.0), status(draft), tags(min 3), lang.
9. Presentar plan al usuario: tabla con tipo, namespace, URN, estructura propuesta, fuentes, estrategia de ejecucion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo | enum(descriptivo\|prescriptivo) | Tipo de artefacto determinado |
| namespace | string | Namespace KORA destino |
| urn | string | URN asignado al artefacto |
| fuente | string | Identificacion de fuente(s) |
| largo_estimado | string | Estimacion de tokens del input |
| estrategia | enum(directa\|segmentada\|segmentada+fidelidad-reforzada) | Estrategia de ejecucion |
| estructura_propuesta | string[] | Headings planificados |
| frontmatter | object | Metadata YAML planificada |
