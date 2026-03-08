---
_manifest:
  urn: urn:pro:skill:salubrista-hah-intent-firs:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTENT-FIRS

## Proposito
Clasificar la intención del usuario y posicionar el problema en la dimensión FIRS correcta (I/II/III) o detectar problema HaH específico, determinando el estado FSM destino. Extensión de salubrista/CM-INTENT-FIRS: agrega detección de dominio HaH antes de posicionamiento FIRS.

## Input/Output
- **Input:** consulta: string (texto libre del usuario)
- **Output:** IntentResult { dominio: "FIRS"|"HAH"|"HAH+FIRS", dimension: "I"|"II"|"III"|"multi"|null, subruta_hah: "Admission"|"Operations"|"Director"|"Evidence"|null, estado_destino: string, nivel_analisis: string, clarificacion_requerida: bool }

## Procedimiento
1. DETECTAR DOMINIO HaH primero (antes de posicionamiento FIRS):
   - Señales HaH: criterios ingreso/egreso HD, condición clínica estable para domicilio, cargo DT, Director Técnico, DS 1/2022, DE 31/2024, hospitalización domiciliaria, Hospital at Home, HaH, visita domiciliaria de intensidad hospitalaria, dispositivos invasivos en domicilio, IAAS domiciliaria, REAS, Resumen Clínico en Domicilio, SAMU/reingreso desde HD, red de apoyo del paciente HD, farmacia botiquín HD, protocolo agresiones terreno, RPM/IoT domiciliario, backfill margin, MCC, NT 238, evidencia Johns Hopkins/Cochrane/CMS
   - IF señales HaH presentes → identificar sub-ruta:
     - Criterios ingreso/egreso, admisión, elegibilidad, exclusión → **Admission** → S-HAH
     - Operaciones diarias, pase de visita, dispositivos, IAAS, REAS, farmacia, logística, emergencia clínica, registros, SBAR → **Operations** → S-HAH
     - Cargo DT, Director Técnico, requisitos legales, RRHH, manuales obligatorios, SEREMI, plan sucesión → **Director** → S-HAH
     - Evidencia internacional, benchmarks, Johns Hopkins, Cochrane, CMS AHCAH, comparativo → **Evidence** → S-HAH
     - IF HaH con componente clínico individual (razonamiento sobre paciente específico) → **HAH+FIRS** → S-HAH primary, S-CLINICAL secondary

2. SI NO señales HaH → posicionar en FIRS:
   - IF objeto = individuo + razonamiento clínico/diagnóstico → Dim I → S-CLINICAL
   - IF objeto = población + inferencia causal/brote → Dim II → S-EPI
   - IF objeto = red/sistema/gestión → Dim III → S-NETWORK
   - IF auditoría/calidad/mejora continua → S-AUDIT
   - IF alerta/brote activo/vigilancia/RSI → S-VIGILANCE
   - IF informe formal → S-REPORT
   - IF multi-dimensión → identificar Dim primaria + notar Dims secundarias

3. IDENTIFICAR nivel de análisis: individuo / equipo / unidad HD / red / población
4. VERIFICAR ambigüedad: IF ambigua → formular una sola pregunta de clarificación
5. OUTPUT: declarar dominio + dimensión o sub-ruta HaH + estado destino + nivel de análisis

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| dominio | string | "FIRS" / "HAH" / "HAH+FIRS" |
| dimension | string? | "I" / "II" / "III" / "multi" — solo si dominio=FIRS |
| subruta_hah | string? | "Admission" / "Operations" / "Director" / "Evidence" — solo si HAH |
| estado_destino | string | S-HAH / S-CLINICAL / S-EPI / S-NETWORK / S-AUDIT / S-VIGILANCE / S-REPORT |
| nivel_analisis | string | individuo / equipo / unidad HD / red / población |
| dims_secundarias | string[] | Dimensiones adicionales si multi-nivel |
| clarificacion_requerida | bool | True si consulta ambigua |
| pregunta_clarificacion | string? | Solo si clarificacion_requerida = true |
