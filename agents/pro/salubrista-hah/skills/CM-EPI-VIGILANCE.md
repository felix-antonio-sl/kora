---
_manifest:
  urn: "urn:pro:skill:salubrista-hah-epi-vigilance:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-EPI-VIGILANCE

## Propósito
Conducir vigilancia epidemiológica activa: detección temprana de riesgos, evaluación de brotes, aplicación del RSI 2005 y gestión de resistencia antimicrobiana. El profesional actúa como guardián de la seguridad sanitaria. Integra obligaciones internacionales (RSI 2005, vinculante para 196 países/194 EM OMS) con acción territorial.

## I/O

- **Input:** señal: string (alerta, caso, brote, patrón epidemiológico), contexto: object (territorio, población, sistema de salud disponible)
- **Output:** VigilanceReport { tipo_amenaza, evaluacion_riesgo, clasificacion_RSI, acciones_inmediatas, notificacion_requerida, recomendaciones_largo_plazo }

## Procedimiento

1. RECIBIR SEÑAL: caracterizar evento — ¿cuándo? ¿dónde? ¿cuántos casos? ¿cuál es el agente probable? ¿cuál es la vía de transmisión?
2. CLASIFICAR TIPO DE AMENAZA:
   - Inteligencia epidémica: zoonosis, brote infeccioso, clúster inusual
   - Amenaza química o radiológica: evento de origen no biológico
   - Salud ocupacional: riesgo en trabajadores de salud (base de resiliencia del sistema)
   - Resistencia antimicrobiana: patrón RAM, falla terapéutica, necesidad PROA
3. EVALUAR RIESGO: gravedad del evento × probabilidad de propagación × capacidad de respuesta disponible.
   - Herramientas: árbol de decisión RSI 2005 (Anexo 2) — 4 preguntas: ¿impacto grave en salud pública? ¿inusual o inesperado? ¿riesgo significativo difusión internacional? ¿riesgo restricciones viaje/comercio?
4. CLASIFICAR SEGÚN RSI 2005:
   - IF ≥ 2 criterios positivos en árbol de decisión → potencial PHEIC (Public Health Emergency of International Concern)
   - IF PHEIC probable → notificación a OMS < 24h desde evaluación (obligación de Estado)
   - IF no PHEIC → gestión nivel local/nacional con reporte periódico
5. MODELADO EPI (si aplica → handoff a CM-FIRS-REASONER Dim II Rama B):
   - ¿Se requiere modelo compartimental para proyectar magnitud? → estimar R₀, tasa ataque, pico esperado, capacidad hospitalaria requerida
6. ACCIONES INMEDIATAS: contención, investigación epidemiológica de campo, medidas de control por vía de transmisión, protección trabajadores de salud.
7. RESISTENCIA ANTIMICROBIANA / PROA (si aplica):
   - Implementar Programa de Optimización de Antibióticos (PROA)
   - Identificar antibióticos críticos (OMS: Watch, Reserve), restricción de uso
   - Vigilancia microbiológica activa, reporte a sistema nacional/OMS si corresponde
8. SALUD OCUPACIONAL: ¿trabajadores de salud expuestos? → evaluar EPP, protocolo post-exposición, vigilancia activa del personal (resiliencia del sistema depende de integridad del equipo).
9. RECOMENDACIONES LARGO PLAZO: sistemas de alerta temprana, capacidad laboratorial, fortalecimiento RRHH, gobernanza intersectorial (salud + agricultura + comercio + educación).
10. IF web_search requerido para datos de situación epidemiológica actual → ejecutar, citar fuente.

## Signature Output

| Campo | Tipo | Descripción |
|-------|------|-------------|
| tipo_amenaza | string | Infecciosa / Química / Radiológica / RAM / Ocupacional |
| evaluacion_riesgo | string | Gravedad × propagación × respuesta disponible |
| clasificacion_rsi | string | PHEIC probable / Gestión nacional / Vigilancia rutinaria |
| notificacion_requerida | bool | True si PHEIC probable → OMS < 24h |
| acciones_inmediatas | string[] | Contención, investigación, control, protección |
| modelo_epi_requerido | bool | True si necesita CM-FIRS-REASONER Dim II |
| recomendaciones_largo_plazo | string[] | Sistemas, capacidades, gobernanza |
| trazabilidad | string[] | RSI 2005, OMS, guías internacionales citadas |
