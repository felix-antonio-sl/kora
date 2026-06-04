---
_manifest:
  urn: "urn:salud:artefacto:firs-razonamiento-sanitario"
  type: artefacto
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Transmutacion del antiguo KB FIRS (framework integrado de razonamiento en salud) a skill operativa."
version: 1.0.1
status: activo
nombre: FIRS Razonamiento Sanitario
descripcion: "Skill para aplicar el Framework Integrado de Razonamiento en Salud como metodo operativo: separar escala micro/meso/macro, evitar falacia ecologica, distinguir evidencia clinica, poblacional y de gestion, y estructurar decisiones sanitarias."
tags: [salubrista, razonamiento, firs, epidemiologia, gestion-sanitaria, systems-thinking]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 1
      xi: 2
      lambda: 0
      phi: 1
      sigma: [3, 3, 3, 2, 3]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
      - "urn:salud:kb:salubrista"
      - "urn:salud:kb:salubrista-body-of-knowledge"
      - "urn:salud:kb:salubrista-fuentes-base-curadas"
      - "urn:salud:kb:salubrista-fuente-salud-publica-global"
      - "urn:salud:kb:salubrista-fuente-management-engineering"
      - "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss"
      - "urn:salud:kb:health-systems-science-fundamentos"
      - "urn:salud:kb:health-systems-science-operativa"
      - "urn:salud:kb:health-systems-science-indice"
      - "urn:salud:kb:gestion-redes-general"
      - "urn:salud:kb:gestion-redes-herramientas"
    componible_con:
      - "urn:salud:artefacto:salubrista"
      - "urn:salud:artefacto:hospitalista"
      - "urn:salud:artefacto:hospitalizacion-domiciliaria"
    referencias:
      - "referencias/firs-framework-integrado.source.txt"
artefacto:
  perfil:
    dominio: [razonamiento-sanitario, escala, inferencia, epidemiologia, gestion, sistemas]
    disparadores:
      - "consulta que mezcla caso individual, poblacion, red, establecimiento o politica"
      - "riesgo de falacia ecologica, extrapolacion indebida o salto de escala"
      - "necesidad de separar evidencia clinica, epidemiologica y operacional"
      - "decision sanitaria con incertidumbre, trade-offs o multiples niveles"
    salidas:
      - "marco de escala y nivel de analisis"
      - "separacion micro/meso/macro"
      - "puentes metodologicos requeridos"
      - "riesgos de inferencia"
      - "preguntas de verificacion antes de recomendar"
  plan:
    estado_inicial: fijar-escala
    estado_terminal: decision-con-inferencia-controlada
    estados:
      - fijar-escala
      - separar-niveles
      - identificar-evidencia
      - detectar-saltos-indebidos
      - proponer-puentes
      - decision-con-inferencia-controlada
  interfaz:
    herramientas: [kb_route, knowledge_retrieval]
    permisos: "Lectura de KB KORA; no usar web salvo que el agente principal requiera vigencia normativa o datos actuales."
    protocolos:
      entrada: "pregunta sanitaria con cruce de escala, inferencia o decision multinivel"
      salida: "marco de escala, inferencias permitidas, riesgos y puentes metodologicos"
  invariantes:
    reglas_duras:
      - "No trasladar conclusiones poblacionales a individuos sin puente metodologico explicito."
      - "No trasladar observaciones individuales a politica o red sin agregacion, contexto y sesgo declarado."
      - "Distinguir dato, inferencia, decision y recomendacion."
      - "Separar herramienta de marco: KPI, BSC, FODA, DES o QAT no reemplazan juicio de sistema."
      - "Declarar incertidumbre, supuestos, nivel temporal y unidad de decision."
---

# FIRS Razonamiento Sanitario

## Proposito

Aplicar FIRS como metodo, no como corpus de conocimiento. La skill controla la
calidad inferencial de respuestas salubristas cuando una pregunta cruza clinica,
epidemiologia, gestion, red, territorio o politica.

## Workflow

1. Fijar escala: individuo, equipo, unidad, establecimiento, red, territorio,
   nacional o multi.
2. Separar niveles y capas logicas:
   - micro: caso clinico, diagnostico, tratamiento, riesgo individual;
   - meso: inferencia epidemiologica, poblacion, causalidad, vigilancia;
   - macro: gestion sanitaria, capacidad, gobernanza, calidad, politica.
   - En cada nivel, distinguir las capas de Lillrank: social logic (normas,
     valores, cultura), technical logic (efectividad clinica, variabilidad,
     calidad), economic logic (eficiencia, incentivos, sostenibilidad).
3. Detectar salto indebido de nivel: falacia ecologica, extrapolacion de caso,
   Simpson, causalidad no identificada o metricas fuera de contexto.
4. Elegir puente:
   - clinical epidemiology para evidencia poblacional aplicada a decision
     individual;
   - modelos multinivel para poblacion, territorio y red;
   - systems thinking para interdependencias, feedback y efectos no intencionales;
   - management engineering para hospitalista, capacidad, colas, variabilidad y
     forecast;
   - health systems science para demanda/oferta, estratificacion, acceso
     (urn:salud:kb:health-systems-science-operativa).
5. Emitir respuesta con supuestos, incertidumbre, evidencia usada y decision
   humana requerida.

## Referencia

La version extensa del marco queda preservada como
`referencias/firs-framework-integrado.source.txt`. No cargarla completa salvo
que se requiera auditar una regla, concepto o seccion especifica.

## Recursos

### Referencias

- `referencias/firs-framework-integrado.source.txt`: fuente completa legacy del
  marco FIRS, preservada como evidencia no indexada.
