---
_manifest:
  urn: urn:pro:skill:salubrista-hah-firs-reasoner:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-FIRS-REASONER

## Proposito
Aplicar el framework FIRS para razonamiento clínico individual (Dim I) o inferencia epidemiológica/poblacional (Dim II). Garantiza segregación de niveles, uso correcto de herramientas y mediación obligatoria cuando se cruzan dimensiones.

## Input/Output
- **Input:** dim: "I"|"II", problema: string, contexto: object (datos clínicos o epidemiológicos disponibles)
- **Output:** ReasoningResult { análisis: string, herramientas_aplicadas: string[], conclusiones: string[], incertidumbre_residual: string, puente_requerido: bool, dim_destino_puente: string? }

## Procedimiento
### Ruta Dim I — Cognición Clínica Individual

1. POSICIONAR: nivel = individuo. Objeto: razonamiento clínico frente al paciente.
2. ESTIMAR PROBABILIDAD PRE-TEST: prevalencia poblacional × antecedentes individuales. Requiere input epidemiológico → IF no disponible, solicitar o estimar con datos del modelo + declarar incertidumbre.
3. ACTIVAR DUAL-PROCESS:
   - Sistema 1: ¿existe illness script que active reconocimiento de patrón inmediato? Declararlo.
   - Sistema 2: construir lista diferencial hipotético-deductiva. Mínimo 3 diagnósticos.
4. VERIFICAR SESGOS (checklist):
   - Anclaje/cierre prematuro: ¿primera hipótesis bloquea reevaluación? → considerar alternativos post-cierre
   - Disponibilidad: ¿sobrepondero diagnóstico reciente/memorable? → calibrar con prevalencia real
   - Confirmación: ¿busco solo datos que validan hipótesis activa? → buscar activamente evidencia refutatoria
   - Momentum diagnóstico: ¿propago etiqueta acrítica de interfaz anterior? → verificar diagnóstico en cada transición
   - Sesgos implícitos: ¿fenotipo, socioeconómico, género influyen? → protocolo estándar
5. APLICAR BAYES: calcular o estimar probabilidad post-test con hallazgos disponibles. Identificar LR+ y LR- de hallazgos clave. ¿Cruzamos umbral de prueba? ¿Umbral de tratamiento?
6. DIAGNOSTIC STEWARDSHIP (si test requerido):
   - Pre-analítica: ¿test altera conducta? ¿probabilidad pre-test justifica? ¿existe sobre-diagnóstico?
   - Analítica: fidelidad metrológica del test considerada
   - Post-analítica: integración post-test probability sin silos informativos
7. METACOGNICIÓN: ¿diagnostic time-out necesario? ¿switching S1→S2 justificado?
8. CO-INDUCCIÓN: ¿estoy cruzando de nivel clínico → poblacional sin mediación? → IF sí → activar puente clinical epi (Dim II input requerido)
9. OUTPUT: análisis con hipótesis diferencial, Bayes aplicado, sesgos identificados, conclusión provisional, incertidumbre residual declarada.

### Ruta Dim II — Inferencia Epidemiológica

1. POSICIONAR: nivel = población/grupo. Objeto: estimar efectos causales o modelar dinámica de transmisión.
2. CLASIFICAR pregunta:
   - ¿Inferencia causal? (¿X causa Y?) → Rama A
   - ¿Dinámica de transmisión/brote? → Rama B
3. RAMA A — Inferencia causal:
   - Construir DAG: identificar variables, flechas causales, confounders, colliders
   - Identificar sesgo de selección, confusión, error de medición
   - Seleccionar estrategia: estandarización, IPW, target trial emulation, mediación
   - Modelo Rothman-Greenland si aplica: causas suficientes/componentes
   - Resultado: estimado de efecto + IC + limitaciones causales declaradas
4. RAMA B — Dinámica de transmisión:
   - Seleccionar modelo compartimental adecuado (SIR, SEIR, SEIR+edad, Neural-SEIR)
   - Estimar parámetros disponibles: β, σ, γ, N → calcular R₀ = β/γ
   - Proyectar: pico de saturación hospitalaria, horizonte temporal
   - Extensiones si necesario: estructura por edad, vacunación, estocasticidad
5. FALACIA ECOLÓGICA: verificar antes de cualquier traslación a nivel individual. IF riesgo → agregar mediación explícita: "datos de nivel poblacional; para aplicar a decisión individual requiere clinical epidemiology (Dim I↔II puente)"
6. CLINICAL EPIDEMIOLOGY (puente Dim I↔II): si el output debe alimentar decisión clínica individual → traducir via probabilidades pre-test, likelihood ratios, appraisal crítico de evidencia
7. OUTPUT: análisis epi con rama identificada, herramientas aplicadas, resultado/estimado, riesgo de falacia ecológica evaluado, puente a Dim I si requerido.

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| dim_aplicada | string | "I" o "II" |
| hipotesis_diferenciales | string[] | Solo Dim I: lista de diagnósticos con probabilidad estimada |
| herramientas_aplicadas | string[] | Bayes, DAG, SIR, etc. |
| sesgos_verificados | string[] | Solo Dim I: sesgos revisados |
| estimado_efecto | string | Solo Dim II Rama A: estimado causal + IC |
| R0_estimado | float? | Solo Dim II Rama B |
| conclusiones | string[] | Conclusiones provisionalescon nivel de certeza |
| incertidumbre_residual | string | Declaración explícita de incertidumbre |
| puente_requerido | bool | True si se necesita mediación inter-dimensional |
| dim_destino_puente | string? | "I" o "III" si puente necesario |
