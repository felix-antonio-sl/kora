---
_manifest:
  urn: urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol
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
---

# Protocolo de Auditoría Ontológica 360° (Gist)

## Propósito y Alcance

Ctx: Auditoría ontológica 360° (propósito/estructura/semántica/sintaxis). SPARQL/OWL/SHACL. Foco: Gist como ontología upper/patrones reutilizables.
XRef_Required: `urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol`
Src: `staging/d.md`

Evaluar ontologías end-to-end: validez + utilidad + sostenibilidad. Objetivos: (1) calibrar severidad por nivel de madurez (L1–L4); (2) auditar 4 cuadrantes: pragmático/estructural/semántico/sintáctico; (3) producir checklist, evidencias (SPARQL/OWL/SHACL) y reporte accionable.

## Matriz de Madurez (MMO)

| Nivel | Nombre | Descripción |
|---|---|---|
| L1 | Prototipo | Exploración inicial; tolerancia alta a inconsistencias |
| L2 | Desarrollo | Modelo en construcción; requiere consistencia básica |
| L3 | Producción | Modelo operativo; requiere conformidad estricta |
| L4 | Federado | Modelo publicado para integración externa; máximo rigor |

## Cuadrante 1: Pragmático

Foco: propósito, alcance, gobernanza, audiencia.

### Competency Questions (CQs) y Requisitos Funcionales

Criterios:

| ID | Criterio | Peso | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|---|
| P1.1 | Existencia de CQs documentadas | Alto | ○ | ● | ● | ● |
| P1.2 | CQs traducibles a SPARQL | Alto | ○ | ○ | ● | ● |
| P1.3 | Cobertura CQs vs clases/propiedades | Medio | ○ | ○ | ● | ● |
| P1.4 | Trazabilidad CQ ↔ Stakeholder | Bajo | ○ | ○ | ○ | ● |

Preguntas: (1) ¿Existe documento que liste CQs? (2) Para cada CQ, ¿existe SPARQL que la responda? (3) ¿Cada clase/propiedad justificada por ≥1 CQ? (4) ¿Hay CQs que el modelo no puede responder? (Gap Analysis)

Anti-patrones:

| Anti-patrón | Síntoma | Impacto |
|---|---|---|
| CQ-less Ontology | Sin CQs documentadas | Imposible validar utilidad |
| Orphan Concepts | Clases sin CQ | Complejidad innecesaria |
| Scope Creep | CQs fuera del dominio | Modelo inmanejable |

Técnica — detección de clases sin instancias ni uso:

```sparql
SELECT ?class (COUNT(?s) AS ?instances) (COUNT(?usage) AS ?usages)
WHERE {
  ?class a owl:Class .
  OPTIONAL { ?s a ?class }
  OPTIONAL { ?usage ?p ?class }
}
GROUP BY ?class
HAVING (COUNT(?s) = 0 && COUNT(?usage) = 0)
```

### Alineación de Alcance y Minimalismo

| ID | Criterio | Descripción |
|---|---|---|
| P2.1 | Ratio Clase/CQ | Idealmente ≤3 clases por CQ cubierta |
| P2.2 | Índice de Reuso | % propiedades reutilizadas vs. ad-hoc |
| P2.3 | Densidad Axiomática | Axiomas por clase (ideal: 2–5 para L3) |

Preguntas: ¿Puede eliminarse alguna clase sin perder respuesta a CQs? ¿Nivel de detalle apropiado? ¿Límites del dominio claros? ¿Qué explícitamente NO se modela?

Checklist de gobernanza de alcance: Scope Statement documentado (máx 3 párrafos); lista explícita de Out of Scope; versión y fecha de vigencia; proceso de Change Request definido; responsable de gobernanza identificado.

### Audiencia y Usabilidad Humana

| ID | Criterio | Verificación |
|---|---|---|
| P3.1 | Legibilidad de Labels | ¿rdfs:label en lenguaje natural, sin camelCase técnico? |
| P3.2 | Completitud de Definiciones | ¿100% de clases tienen skos:definition o rdfs:comment? |
| P3.3 | Ejemplos | ¿Clases complejas tienen skos:example? |
| P3.4 | Multilingüismo | ¿Labels en idiomas requeridos con @lang tags? |

Anti-patrones:

| Anti-patrón | Ejemplo | Corrección |
|---|---|---|
| CamelCase Labels | rdfs:label "hasEmploymentRelation" | rdfs:label "tiene relación de empleo"@es |
| Definition-less Classes | Clase sin rdfs:comment | Añadir definición de 1–2 oraciones |
| Jargon Overload | "RDF reification pattern for n-ary" | "Representa relación con múltiples participantes" |

### Gobernanza y Ciclo de Vida

| ID | Criterio | Preguntas |
|---|---|---|
| P4.1 | Versionamiento | ¿Existe owl:versionInfo y política de deprecación? |
| P4.2 | Provenance | ¿Documentado creador, fecha, licencia? |
| P4.3 | Change Management | ¿Proceso para proponer cambios? |
| P4.4 | Deprecation Policy | ¿Cómo se marcan términos obsoletos? (owl:deprecated) |

Metadatos requeridos L3+:

```turtle
<https://example.org/ontology/domain> a owl:Ontology ;
    owl:versionInfo "1.2.0" ;
    owl:versionIRI <https://example.org/ontology/domain/1.2.0> ;
    owl:priorVersion <https://example.org/ontology/domain/1.1.0> ;
    dc:title "Domain Ontology"@en ;
    dc:creator "Knowledge Team" ;
    dc:created "2025-01-15"^^xsd:date ;
    dc:modified "2026-01-23"^^xsd:date ;
    dc:license <https://creativecommons.org/licenses/by/4.0/> ;
    rdfs:comment "Ontología para modelar..."@es .
```

Trade-off semiótico: perfección lógica puede degradar utilidad pragmática si el modelo es demasiado complejo para consultar. Priorizar claridad operable; si `gist:Category` resuelve, evitar OWL complejo por pureza.

## Cuadrante 2: Estructural

Foco: taxonomía, arquitectura, propiedades, namespaces, patrones y reuso.

### Higiene Taxonómica

**Análisis de jerarquía de clases:**

| ID | Verificación | Método |
|---|---|---|
| S1.1 | Ciclos en subClassOf | Query SPARQL o razonador |
| S1.2 | Profundidad máxima | Contar niveles (recomendado: ≤7) |
| S1.3 | Anchura promedio | Subclases directas por clase (recomendado: 3–7) |
| S1.4 | Clases huérfanas | Sin superclase (excepto owl:Thing) |
| S1.5 | Herencia múltiple | Detectar y validar si intencional |

```sparql
SELECT ?class (COUNT(?parent) AS ?parentCount)
WHERE {
  ?class rdfs:subClassOf ?parent .
  FILTER(?parent != owl:Thing)
}
GROUP BY ?class
HAVING (COUNT(?parent) > 1)
```

**Distinción Class / Instance / Category:**

| Patrón | Usar Cuando | Ejemplo Correcto | Anti-patrón |
|---|---|---|---|
| owl:Class | Tipos con axiomas formales, estables | ex:Employee rdfs:subClassOf gist:Person | Crear clase por cada variante |
| Instance | Individuos específicos | ex:_Person_JuanPerez a gist:Person | ex:JuanPerez a owl:Class |
| gist:Category | Taxonomías flexibles, sin axiomas | ex:_EmployeeType_Permanent a gist:Category | Clase para tipos administrativos |

Preguntas: ¿Hay clases que deberían ser instancias? (ej: ChileCountry como clase). ¿Hay instancias que deberían ser clases? ¿Se usa `gist:Category` para taxonomías administradas por no-técnicos?

### Higiene de Propiedades

**Object Properties:**

| ID | Verificación | Criterio |
|---|---|---|
| S2.1 | Inversa declarada | ¿Propiedades navegables tienen inversa? |
| S2.2 | Dominio/Rango | ¿Declarados pero no excesivamente restrictivos? |
| S2.3 | Características | ¿Funcional, transitiva, simétrica correctamente aplicadas? |
| S2.4 | Naming consistency | ¿Verbos para object properties (hasX, isXOf)? |

```sparql
SELECT ?prop WHERE {
  ?prop a owl:ObjectProperty .
  FILTER NOT EXISTS { ?prop owl:inverseOf ?inv }
  FILTER NOT EXISTS { ?inv owl:inverseOf ?prop }
}
```

**Datatype Properties:**

| ID | Verificación | Criterio |
|---|---|---|
| S2.5 | Tipo de dato explícito | ¿rdfs:range con xsd: datatype? |
| S2.6 | Magnitudes con unidad | ¿Valores medibles usan gist:Magnitude pattern? |
| S2.7 | Fechas | ¿Usan xsd:date, xsd:dateTime consistentemente? |

Anti-patrones de propiedades:

| Anti-patrón | Ejemplo | Corrección |
|---|---|---|
| Stringly-typed | ex:employeeId "12345" sin tipo | Usar xsd:integer o IRI |
| Direct Measurement | ex:weight "75.5"^^xsd:decimal | gist:Magnitude con UoM |
| Embedded Semantics | ex:billingAddress, ex:shippingAddress separadas | gist:Address + gist:AddressUsageType |

### Higiene de Namespaces e IRIs

| ID | Criterio | Verificación |
|---|---|---|
| S3.1 | No Namespace Squatting | ¿No se definen términos en gist:, foaf:, schema:? |
| S3.2 | Consistencia de Prefijos | ¿Un solo prefijo por namespace? |
| S3.3 | Dereferenciabilidad | ¿IRIs resuelven a documentación o son opacos? |
| S3.4 | Patrón de IRI | ¿Consistente para clases, propiedades, instancias? |

Patrones de IRI recomendados:

```
https://org.example/ontology/domain/         # TBox (clases, propiedades)
https://org.example/data/domain/             # ABox (instancias)
https://org.example/data/domain/_Person_abc123   # Instancias (prefijo "_")
https://org.example/refdata/Country_CL        # Reference Data
```

### Patrones de Modelado y Reuso

**Evaluación de patrones Gist:**

| Patrón | Aplica Cuando | Verificar |
|---|---|---|
| TemporalRelation | Relaciones con contexto temporal | ¿Empleo, membresía, propiedad modelados como relación? |
| Magnitude + UoM | Valores medibles | ¿Peso, precio, distancia usan el patrón? |
| Category | Taxonomías flexibles | ¿Tipos administrativos son categorías? |
| Address | Direcciones físicas/electrónicas | ¿Se usa containedText + refersTo? |
| Agreement/Commitment | Contratos, obligaciones | ¿Estructura para partes y términos? |

**Métricas de reuso:**

```sparql
SELECT
  (COUNT(DISTINCT ?imported) AS ?importedProps)
  (COUNT(DISTINCT ?custom) AS ?customProps)
  (COUNT(DISTINCT ?imported) * 100.0 /
   (COUNT(DISTINCT ?imported) + COUNT(DISTINCT ?custom)) AS ?reusePercent)
WHERE {
  { ?imported a owl:ObjectProperty . FILTER(STRSTARTS(STR(?imported), "https://w3id.org/semanticarts/")) }
  UNION
  { ?custom a owl:ObjectProperty . FILTER(!STRSTARTS(STR(?custom), "https://w3id.org/semanticarts/")) }
}
# Objetivo L3+: reusePercent >= 40%
```

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
│   ├── temporal.ttl
│   └── spatial.ttl
├── reference-data/
│   ├── countries.ttl
│   └── currencies.ttl
└── bundle.ttl
```

### Testing y Validación Automatizada

Ejemplo SHACL shapes:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <https://example.org/ns/> .

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
| Cuadrante   | Score    | Estado          |
|-------------|----------|-----------------|
| Pragmático  | X/10     | RED/YELLOW/GREEN |
| Estructural | X/10     | RED/YELLOW/GREEN |
| Semántico   | X/10     | RED/YELLOW/GREEN |
| Sintáctico  | X/10     | RED/YELLOW/GREEN |
| **Total**   | **X/40** |                 |

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
