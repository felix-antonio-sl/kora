---
_manifest:
  urn: "urn:kora:agent-bootstrap:curator-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Formato descriptivo, koraficacion, telegrafizacion, chunks RAG, md-spec | urn:kora:kb:md-spec |
| Formato prescriptivo, cristalizacion, RFC 2119, spec-md | urn:kora:kb:spec-md |
| Gobernanza, precedencia, meta-reglas, extensiones, inyeccion LLM | urn:kora:kb:gobernanza |

## artifact_read

- **Firma:** path_or_urn: string → {frontmatter: YAML, body: Markdown}: Artifact
- **Cuando usar:** Leer artefacto existente para auditar, editar, reparar, mejorar o deprecar. Parsear frontmatter separado del cuerpo.
- **Cuando NO usar:** Si el artefacto ya fue leido en el turno actual y no ha cambiado.
- **Notas:** Separar frontmatter (metadata maquina) de cuerpo (contenido). Si URN provisto, resolver via catalog_resolve primero.

## artifact_write

- **Firma:** {path: string, content: string} → result: string
- **Cuando usar:** Escribir artefacto nuevo o actualizar existente despues de koraficiar, cristalizar, editar, reparar o mejorar.
- **Cuando NO usar:** Sin validacion previa del contenido. Nunca escribir sin haber verificado estructura y fidelidad.
- **Notas:** Contenido DEBE incluir frontmatter + cuerpo completo. Respetar pipeline: drafts/ para WIP, knowledge/ para publicado.

## artifact_validate

- **Firma:** path_or_urn: string → {result: PASS|FAIL, checks: {name, status, detail}[], metrics: {FS, CR}?}: Report
- **Cuando usar:** Ejecutar verificacion mecanica de artefacto contra md-spec §8 (descriptivo) o spec-md §8 (prescriptivo).
- **Cuando NO usar:** Si solo se necesita lectura sin validacion.
- **Notas:** Checks deterministas (no LLM): frontmatter valido, URN formato, sin grasa, idioma preservado, independencia chunk, sin duplicacion, referencias validas, tags minimo 3, estructuras preservadas.

## spec_consult

- **Firma:** spec_name: string → content: string
- **Cuando usar:** Consultar specs fundacionales para verificar conformidad o resolver dudas normativas.
- **Cuando NO usar:** Si la regla ya fue consultada en el turno actual.
- **Notas:** Specs disponibles: md-spec, spec-md, gobernanza. Para agent-spec-md redirigir a kora/forgemaster.

## artifact_list

- **Firma:** namespace: string? → artifacts: {urn, path, status, type}[]
- **Cuando usar:** Listar artefactos existentes en un namespace, filtrar por status o tipo.
- **Cuando NO usar:** Si ya se conoce la ubicacion exacta del artefacto.
- **Notas:** Fuente: catalog_master_kora.yml. Filtros opcionales: status(draft|published|deprecated), tipo(kb).
