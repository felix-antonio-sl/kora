---
_manifest:
  urn: "urn:kora:skill:curator-crystallizer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CRYSTALLIZER

## Proposito
Ejecuta el Funtor G: {Decisiones + Practicas + Restricciones} → KORA/Spec-MD conforme a spec-md §1.2. Cristaliza conocimiento prescriptivo en documentos formales con reglas univocas.

## Procedimiento

### Fase 1: Elicitacion
1. Identificar inputs: decisiones de diseno (explicitas/tacitas), practicas existentes (convenciones informales), restricciones (tecnicas, organizacionales, legales).
2. Clasificar cada input: regla candidata, definicion candidata, ejemplo candidato, contexto.
3. Priorizar: obligaciones(DEBE) > prohibiciones(NO DEBE) > recomendaciones(DEBERIA) > opciones(PUEDE).

### Fase 2: Cristalizacion
1. Convertir decisiones implicitas → reglas explicitas con keyword RFC 2119.
2. Cada regla: exactamente una lectura posible.
3. Keywords en **negrita** siempre.
4. Version castellana de keywords (DEBE, NO DEBE, DEBERIA, NO DEBERIA, PUEDE).
5. Equivalencia inglesa solo en primera mencion, nunca repetida.

### Fase 3: Desambiguacion
1. Revisar cada regla: ¿admite multiples interpretaciones?
2. Si ambigua → reescribir hasta lograr exactamente una lectura.
3. Eliminar hedging ("probablemente", "en general", "suele").
4. Eliminar ambiguedad pronominal ("esto", "eso", "lo anterior").

### Fase 4: Ejemplificacion
1. Toda regla con complejidad semantica o riesgo ambiguedad → par Correcto/Incorrecto.
2. Formato inline: `**Correcto:** \`ejemplo\`` / `**Incorrecto:** \`ejemplo\``
3. Formato bloque para multilínea con fenced code blocks.
4. Ejemplos DEBEN anclar interpretacion, no decorar.

### Fase 5: Estructuracion (template spec-md §10)
1. Organizar en esqueleto: §1 Definicion, §2 Definiciones, §3-N Secciones normativas, §N+1 Invariantes, §N+2 Validacion, §N+3 Ejemplo(opcional).
2. Secciones ## numeradas secuencialmente.
3. Headings descriptivos del contenido normativo.
4. Toda prosa cumple funcion normativa: racionalizar, desambiguar, clarificar, contextualizar.
5. Prosa que no cumple funcion normativa → eliminar.

### Fase 6: Inyeccion Frontmatter
1. Agregar bloque YAML: _manifest(urn, provenance), version, status, tags(min 3), lang.
2. Schema conforme a spec-md §3.1.

### Fase 7: Verificacion
Checks spec-md §8:
- Frontmatter valido
- Numeracion secuencial de ##
- Keywords RFC 2119 en negrita
- Headings descriptivos (no genericos)
- Sin ambiguedad (cada regla una lectura)
- Ejemplos presentes (reglas complejas)
- Sin prosa innecesaria
- Consistencia interna (sin contradicciones)
- No-circularidad
- Definiciones completas (§2)
- Anglicismos controlados (§7.3)
- Referencias validas
- Auto-suficiencia

## Output
Artefacto KORA/Spec-MD completo (frontmatter + cuerpo). Reporte de conformidad contra spec-md §8.
