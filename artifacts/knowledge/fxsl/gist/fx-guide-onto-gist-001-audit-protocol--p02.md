---
_manifest:
  urn: urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol-p02
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 1.0.0
status: published
tags:
- ontology
- audit
- gist
- sparql
- owl
- shacl
- governance
- fxsl
lang: es
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol
---

# Protocolo de Auditoría Ontológica 360° (Gist) - Parte 02

## Cuadrante 3: Semántico

Foco: lógica, inferencia, restricciones, identidad, perfiles OWL.

### Consistencia Lógica

| Herramienta | Perfil | Uso |
|---|---|---|
| HermiT | OWL 2 DL | Consistencia, clasificación |
| Pellet | OWL 2 DL | Consistencia, explicaciones |
| ELK | OWL 2 EL | Alto rendimiento, ontologías grandes |
| RDFox | OWL 2 RL | Materialización, consultas |

Checklist: carga sin errores en Protégé; razonador sin timeout (<60s para L3); sin clases insatisfacibles; sin inconsistencias; inferencias esperadas (spot check).

Detección de clases insatisfacibles (después de clasificación):

```sparql
SELECT ?class WHERE {
 ?class owl:equivalentClass owl:Nothing .
}
```

Causas comunes: restricciones contradictorias (ej: `hasPart min 1` y `hasPart max 0`); disjointness con superclase; rangos incompatibles en cadena de propiedades.

### Rigor en Restricciones

| Escenario | Recomendación |
|---|---|
| Propiedad general | No declarar domain/range (hereda de superpropiedad) |
| Propiedad específica | Domain/Range en clase más general aplicable |
| Múltiples dominios posibles | Usar owl:unionOf o no declarar |

Anti-patrón sobre-restringido:

```turtle
# Incorrecto: demasiado restrictivo
ex:hasPet rdfs:domain ex:Person ; rdfs:range ex:Dog .

# Correcto: flexible
ex:hasPet rdfs:domain ex:Person ; rdfs:range ex:Animal .
# O mejor: heredar de gist:hasMember sin restricciones adicionales
```

**Disjointness:**

| ID | Verificación | Impacto |
|---|---|---|
| L1.1 | Disjointness explícita | ¿Clases hermanas son disjuntas? |
| L1.2 | Covering axioms | ¿Unión de subclases = superclase? |
| L1.3 | Completitud | ¿CWA o OWA apropiadamente aplicados? |

```turtle
# Patrón recomendado: hermanos disjuntos
ex:Employee rdfs:subClassOf ex:Person .
ex:Customer rdfs:subClassOf ex:Person .
ex:Employee owl:disjointWith ex:Customer .

# O con DisjointUnion (OWL 2)
ex:Person owl:disjointUnionOf (ex:Employee ex:Customer ex:Prospect) .
```

### Manejo de Identidad

| Característica | Uso | Verificar |
|---|---|---|
| owl:FunctionalProperty | Valor único por sujeto | ¿hasBirthDate es funcional? |
| owl:InverseFunctionalProperty | Identifica unívocamente | ¿hasSSN es IFP? |
| owl:hasKey | Clave compuesta | ¿Clases tienen claves definidas? |

Anti-patrón de enlace por string:

```turtle
# Incorrecto: enlace por string (typos rompen integridad)
ex:_Order_123 ex:customerName "Acme Corp" .
ex:_Invoice_456 ex:customerName "Acme Corp" .

# Correcto: enlace por IRI
ex:_Order_123 ex:hasCustomer ex:_Organization_AcmeCorp .
ex:_Invoice_456 ex:hasCustomer ex:_Organization_AcmeCorp .
```

### Perfiles OWL y Complejidad Computacional

| Perfil | Complejidad | Uso Típico |
|---|---|---|
| OWL 2 Full | Indecidible | Evitar |
| OWL 2 DL | 2-NEXPTIME | Ontologías medianas (default) |
| OWL 2 EL | PTIME | Ontologías grandes (SNOMED) |
| OWL 2 QL | AC0 | Query answering |
| OWL 2 RL | PTIME | Reglas de inferencia |

Verificación: Protégé → Ontology → Ontology Metrics → OWL Profile.

## Cuadrante 4: Sintáctico

Foco: calidad del artefacto — parseo, estilo, anotaciones, modularización, tests, CI.

### Validación Sintáctica

| Verificación | Herramienta | Comando |
|---|---|---|
| Turtle válido | rapper | rapper -i turtle -c ontology.ttl |
| RDF/XML válido | xmllint + rapper | Validar XML + RDF |
| Prefijos declarados | Parser | Sin warnings de prefijos desconocidos |
| IRIs válidas | Parser | Sin caracteres ilegales |

Checklist de estilo: indentación consistente (2 espacios); orden subject-ordered luego predicate-ordered; blank lines entre entidades; comentarios Turtle por sección (#=== CLASSES ===); prefijos ordenados alfabéticamente; un archivo por módulo.

### Anotaciones y Documentación Inline

| Anotación | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| rdfs:label | ● | ● | ● | ● |
| rdfs:comment | ○ | ● | ● | ● |
| skos:definition | ○ | ○ | ● | ● |
| skos:example | ○ | ○ | ○ | ● |
| skos:scopeNote | ○ | ○ | ○ | ● |
| dc:source | ○ | ○ | ○ | ● |

Query de completitud de anotaciones:

```sparql
SELECT ?entity
 (BOUND(?label) AS ?hasLabel)
 (BOUND(?comment) AS ?hasComment)
 (BOUND(?definition) AS ?hasDefinition)
WHERE {
 { ?entity a owl:Class } UNION { ?entity a owl:ObjectProperty } UNION { ?entity a owl:DatatypeProperty }
 OPTIONAL { ?entity rdfs:label ?label }
 OPTIONAL { ?entity rdfs:comment ?comment }
 OPTIONAL { ?entity skos:definition ?definition }
}
HAVING (!BOUND(?label) || !BOUND(?comment))
```

### Modularización y Dependencias

| ID | Criterio | Verificación |
|---|---|---|
| M1 | Separación TBox/ABox | ¿Ontología separada de datos de instancia? |
| M2 | Módulos por dominio | ¿Subdominios en archivos separados? |
| M3 | Imports explícitos | ¿owl:imports para dependencias? |
| M4 | Versiones de imports | ¿IRIs versionados para imports críticos? |

Patrón de modularización:

```
ontology/
├── core.ttl
├── extensions/
│ ├── temporal.ttl
│ └── spatial.ttl
├── reference-data/
│ ├── countries.ttl
│ └── currencies.ttl
└── bundle.ttl
```

### Testing y Validación Automatizada

Ejemplo SHACL shapes:

```turtle
@prefix sh: http://www.w3.org/ns/shacl# .
@prefix ex: https://example.org/ns/ .

ex:PersonShape a sh:NodeShape ;
 sh:targetClass ex:Person ;
 sh:property [
 sh:path ex:hasName ;
 sh:minCount 1 ;
 sh:maxCount 1 ;
 sh:datatype xsd:string ;
 sh:message "Toda persona debe tener exactamente un nombre"@es
 ] ;
 sh:property [
 sh:path ex:hasBirthDate ;
 sh:maxCount 1 ;
 sh:datatype xsd:date ;
 sh:lessThan ex:hasDeathDate ;
 sh:message "Fecha de nacimiento debe ser anterior a fecha de muerte"@es
 ] .
```

Pipeline CI/CD ejemplo (GitHub Actions):

```yaml
ontology-validation:
 steps:
 - name: Syntax Check
 run: rapper -i turtle -c *.ttl
 - name: Consistency Check
 run: java -jar HermiT.jar -c ontology.ttl
 - name: SHACL Validation
 run: shacl validate -s shapes.ttl -d data.ttl
 - name: Metrics Report
 run: python ontology_metrics.py > report.md
```

## Checklist Consolidado

**Preparación**: identificar nivel de madurez L1–L4; obtener CQs y alcance; identificar stakeholders; configurar ambiente (Protégé, razonador, SHACL processor).

**Auditoría Pragmática (C1)**: verificar existencia y calidad de CQs; validar cobertura CQ ↔ Modelo; evaluar minimalismo y alcance; revisar legibilidad labels/definiciones; verificar metadatos de gobernanza.

**Auditoría Estructural (C2)**: analizar jerarquía de clases (ciclos, profundidad, anchura); validar distinción Class/Instance/Category; revisar propiedades (inversas, características); verificar higiene de namespaces; evaluar reuso de patrones estándar.

**Auditoría Semántica (C3)**: ejecutar razonador (consistencia); verificar clases insatisfacibles; analizar restricciones domain/range; validar disjointness; revisar manejo de identidad; confirmar perfil OWL.

**Auditoría Sintáctica (C4)**: validar parsing sin errores; verificar estilo y formato; evaluar completitud de anotaciones; revisar modularización; verificar dependencias (imports); evaluar existencia de tests (SHACL).

**Reporte y Recomendaciones**: clasificar hallazgos por severidad (Critical/Major/Minor/Info); proporcionar ejemplos de corrección; priorizar acciones correctivas; documentar trade-offs de diseño; generar métricas comparativas.

## Plantilla de Reporte

```markdown
# Reporte de Auditoría Ontológica
**Ontología**: [Nombre]
**Versión**: [X.Y.Z]
**Fecha**: [YYYY-MM-DD]
**Auditor**: [Nombre/Agente]
**Nivel Objetivo**: [L1-L4]

## Resumen Ejecutivo
| Cuadrante | Score | Estado |
|-------------|----------|-----------------|
| Pragmático | X/10 | RED/YELLOW/GREEN |
| Estructural | X/10 | RED/YELLOW/GREEN |
| Semántico | X/10 | RED/YELLOW/GREEN |
| Sintáctico | X/10 | RED/YELLOW/GREEN |
| **Total** | **X/40** | |

## Hallazgos Críticos
1. [Hallazgo con impacto y corrección]

## Hallazgos Mayores
1. [Hallazgo con impacto y corrección]

## Hallazgos Menores
1. [Hallazgo con impacto y corrección]

## Métricas
- Total Clases: X
- Total Propiedades: X (Object: Y, Datatype: Z)
- Total Instancias: X
- Índice de Reuso: X%
- Densidad Axiomática: X axiomas/clase
- Cobertura de Anotaciones: X%

## Recomendaciones Priorizadas
1. [Acción] — Urgencia: Alta/Media/Baja
```
