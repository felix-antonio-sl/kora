# Herramientas permitidas

## kb_route

Firma: `topic: string -> urn: string`

Uso:
- primer paso semantico para resolver el corpus rector
- obligatorio antes de `knowledge_retrieval`

## knowledge_retrieval

Firma: `urn: string -> content: string`

Uso:
- recuperar el corpus inmediatamente despues de `kb_route`

## web_search

Firma: `query: string -> SearchResult[]`

Uso:
- complementar o verificar vigencia del corpus
- nunca reemplazar el corpus como fuente primaria

## Disciplina

- KB_FIRST es obligatorio
- si el corpus ya cubre el tema, no usar web
- solo usar herramientas declaradas aqui
