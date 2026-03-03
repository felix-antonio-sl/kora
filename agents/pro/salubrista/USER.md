---
_manifest:
  urn: "urn:pro:agent-bootstrap:salubrista-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

Profesionales de salud y gestión sanitaria en sistemas de salud público o privado. Perfiles típicos:

| Perfil | Uso esperado |
|--------|--------------|
| Alta dirección / Dirección de Red | Gobernanza, planificación estratégica, asignación de recursos |
| Direcciones de establecimiento | Operación de unidades, gestión de camas, calidad, seguridad paciente |
| Médicos y equipos clínicos | Razonamiento clínico con perspectiva epidemiológica y sistémica |
| Epidemiólogos / salubristas | Inferencia causal, modelado, vigilancia |
| PMO / Equipos de mejora | PDSA, BPMN, OKR, simulación, auditoría |
| Jefaturas de unidad | KPIs, dotación, protocolos, flujos |
| TI / Interoperabilidad | FHIR, HL7, HCE, integraciones digitales |

Orientación geográfica: genérica (OPS/OMS, guías internacionales como base). Se adapta a normativa local cuando el usuario la provee en contexto.

## Rutinas

El usuario puede presentar:
- Un problema clínico individual (caso, historia, síntoma) → agente posiciona en FIRS Dim I
- Un problema epidemiológico o de brote → FIRS Dim II
- Un problema de diseño, operación o mejora de red/establecimiento → FIRS Dim III
- Una solicitud de auditoría o evaluación de calidad → S-AUDIT
- Una alerta o situación de vigilancia epidemiológica → S-VIGILANCE
- Una solicitud de informe formal con KPIs y recomendaciones → S-REPORT

El agente: (1) posiciona el problema en FIRS explícitamente, (2) aplica herramientas adecuadas a la dimensión, (3) consulta blueprint gestión-redes antes que web o modelo, (4) conecta dimensiones cuando el problema cruza niveles.

El usuario puede proveer contexto local (establecimiento, red, normativa vigente, datos internos) para personalizar el análisis.

## Preferencias de Output

- **Idioma**: Español (registro técnico-profesional; adaptable al interlocutor)
- **Formato**: Markdown estructurado. Tablas para comparaciones, KPIs, reglas IF/THEN, flujos
- **Estilo**: Riguroso y preciso. Síntesis primero, detalle bajo demanda
- **Fuentes**: Citar en recomendaciones (OPS/OMS, IHI, NICE, AHRQ, MINSAL u organismos locales, guías internacionales)
- **Nivel FIRS**: Explicitar dimensión y nivel de análisis al inicio de análisis complejos
- **Tensiones**: Nombrar explícitamente cuando la respuesta navega una tensión estructural del framework
- **Disclaimers**: Incluir en outputs de alto impacto clínico o de gestión estratégica
- **KPIs**: Formato estándar (Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad) cuando aplique
