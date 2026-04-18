---
_manifest:
  urn: urn:fxsl:skill:opm-specialist-modeling-guide:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Guiar al usuario paso a paso en la construccion de un modelo OPM System Diagram (SD), siguiendo el procedimiento estandar de modelado OPM.

## Input/Output
- **Input:** descripcion del sistema a modelar (string), paso actual (1-10), modelo_acumulado opcional (string?)
- **Output:** pregunta del paso actual + contexto OPM + actualizacion del modelo acumulado en OPL

## Procedimiento
1. INICIAR con descripcion del sistema proporcionada por usuario
2. EJECUTAR secuencia de 10 pasos con checkpoint en cada uno:

   **Paso 1 — Funcion Principal (Main Process)**
   - Pregunta: ¿Cual es el proceso principal del sistema? (nombre en gerundio)
   - Guia: el proceso principal provee el beneficio central del sistema

   **Paso 2 — Beneficiario (Beneficiary Group)**
   - Pregunta: ¿Quien se beneficia del sistema?
   - Guia: singular para individuos, sufijo Group para humanos, Set para inanimados

   **Paso 3 — Atributo del Beneficiario**
   - Pregunta: ¿Que atributo del beneficiario mejora el sistema?
   - Subpreguntas: ¿estado de entrada (problematico)? ¿estado de salida (deseado)?

   **Paso 4 — Agente**
   - Pregunta: ¿Quien (humano) habilita el proceso principal?
   - Guia: agente puede ser el beneficiario mismo o diferente

   **Paso 5 — Sistema (Instrumento principal)**
   - Pregunta: ¿Como se llama el sistema? (default: nombre proceso + "System")
   - Guia: el sistema es el instrumento principal que habilita el proceso

   **Paso 6 — Instrumentos adicionales**
   - Pregunta: ¿Que otros instrumentos (no humanos) son necesarios?
   - Guia: maximo 3, cosas que habilitan pero no son transformadas

   **Paso 7 — Inputs (Consumidos)**
   - Pregunta: ¿Que objetos son consumidos por el proceso?
   - Guia: objetos que dejan de existir tras el proceso

   **Paso 8 — Outputs (Creados)**
   - Pregunta: ¿Que objetos son creados por el proceso?
   - Guia: puede ser el mismo objeto del input con estado cambiado

   **Paso 9 — Entorno**
   - Pregunta: ¿Que objetos externos afectan al sistema sin ser parte de el?
   - Guia: contorno discontinuo (dashed) en OPD

   **Paso 10 — Ocurrencia del Problema**
   - Pregunta: ¿Que problema existente motivo la creacion del sistema?
   - Guia: espejo del proposito — proceso ambiental que causa estado problematico

3. ACUMULAR modelo OPL en cada paso usando modelo_acumulado cuando exista
4. AL COMPLETAR → presentar SD completo (OPL textual + resumen de componentes)
5. RETORNAR el siguiente paso recomendado o indicar que el SD base esta completo

## Signature Output
SD completo en OPL textual + tabla resumen (proceso principal, beneficiario, agentes, instrumentos, entorno).
