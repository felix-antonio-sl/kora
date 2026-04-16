# Memory — kora/salubrista-hah

## Contexto Clínico

_Registrar aquí contexto relevante del paciente y plan de cuidados._

## Decisiones

_Decisiones clínicas y operativas tomadas._

## Hallazgos Pendientes

_Items abiertos que requieren seguimiento._

## Evolución

_Registro de evolución y cambios observados._

## Coordinación

- **Korax disponible vía hook cross-gateway** (`kora-personal:18789/hooks/agent`) para apoyo de estructuración, priorización, síntesis, foco, realismo operativo y reducción de carga cognitiva de Félix.
- Cuando convenga derivar trabajo a Korax, enviar insumo idealmente distinguiendo: hechos, hipótesis, problemas, riesgos, propuestas y pendientes; además objetivo, audiencia, plazo, formato esperado, restricciones, material base y decisiones a tomar.

## Notas

### 2026-03-24 — Reorganización de workspace (clawforge)

Estructura aplicada:
- `corpus/hah/` → corpus-hah-completo.md, corpus-hah-nuclear-23.md
- `output/hodom-hsc/` → 9 documentos del proyecto HODOM HSC (análisis, checklist normativo, historias usuario, inventario, plan capacitación, presentación DT, propuesta ideal, protocolos clínicos, specs sistema web)
- `output/operacional/` → plan-90-dias-dt.md, formato-briefing-matinal.md
- `sources/` → PDFs y textos extraídos de evidencia HaH
- `skills/` → 9 skills con SKILL.md
- Raíz limpia: archivos core OpenClaw (AGENTS, SOUL, TOOLS, USER, IDENTITY, MEMORY, BOOTSTRAP, HEARTBEAT)

**Convención de output:** documentos nuevos generados van en `output/<proyecto>/`. Material de referencia en `corpus/<tema>/`.

### 2026-03-25 — Consolidado estratégico DT HODOM HSC

Se consolidó en un documento madre todo el trabajo preparatorio para la primera reunión del nuevo Director Técnico HODOM HSC, incluyendo:
- diagnóstico integral del dispositivo
- marco estratégico de 3 horizontes
- narrativa diplomática y política para el equipo
- brechas normativas y operativas prioritarias
- rol dual DT + médico regulador
- enfoque de baja carga cognitiva como criterio de diseño
- prototipos web inmediatos (panel general, registro móvil, regulación clínica, georreferenciación, alta/contrarreferencia)
- consideración del repositorio histórico de Google Drive como activo de rediseño
- categoría de artefactos rectores (normativa, protocolo, BIP, acuerdos, enlace APS)
- necesidad de integrar catastro de pacientes/rutas históricas geolocalizadas
- inventario de RRHH, vehículos, insumos, medicamentos y equipamiento
- prioridad de reactivar sueroterapia y oxigenoterapia (3 concentradores disponibles)

Documentos clave:
- `output/hodom-hsc/consolidado-estrategico-dt-hodom-hsc-2026-03-25.md`
- `memory/2026-03-25-hodom-dt-consolidado.md`
