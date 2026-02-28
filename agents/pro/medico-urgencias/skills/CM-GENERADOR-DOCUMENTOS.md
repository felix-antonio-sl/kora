---
_manifest:
  urn: "urn:pro:skill:medico-urgencias-generador-documentos:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Generar documentos clinicos telegraficos parametrizados por tipo_output. Unifica logica de generacion para sintesis, alta, hospitalizacion, interconsulta y epicrisis. Aplica filtro parsimonia como paso final.

## I/O

- **Input:** RAZONAMIENTO_CLINICO + ClinicalData + tipo_output (sintesis|alta|hospitalizacion|interconsulta|epicrisis)
- **Output:** Documento clinico telegrafico en wrapper XML <respuesta></respuesta>

## Procedimiento

### Paso 1: Seleccion plantilla por tipo_output

**sintesis:**
- Campos: dx_activos, signos_alarma, complicaciones, lab_alterados (valor numerico), medicamentos_relevantes, enfermedad_actual_breve, sospecha_dx + dx_diferencial, plan_manejo_inmediato
- Limites: sin limite chars fijo, priorizar brevedad maxima

**alta:**
- Campos: ANAMNESIS (edad, antec relevantes, motivo, duracion, sin articulos, max 800 chars), EX FISICO (solo hallazgos positivos, SV solo si alterados, max 800 chars), PRECISION DX (razonamiento minimo, max 800 chars), CIE-10 (codigo + descripcion), INDICACIONES (tto, reposo, control, alarmas, lista no numerada, max 800 chars)
- Limites: 800 chars por campo

**hospitalizacion:**
- Campos: antec + med habituales relevantes, enfermedad actual telegrafica, lab/imagenes solo alterados valores numericos, dx principal CIE10 + secundarios, justificacion hospitalizacion (1-2 lineas), indicaciones telegraficas (farmaco + dosis + via + frecuencia)
- Limites: 800 chars por campo

**interconsulta:**
- Campos: especialidad, resumen minimo (antec, cuadro, estudios relevantes), pregunta especifica, urgencia
- Limites: minimo necesario para pregunta clara

**epicrisis:**
- Campos requeridos: dx principal egreso (CIE-10), comentarios evolucion
- Campos opcionales (solo si aportan valor): dx secundarios, precision dx, resumen hospitalizacion, examenes y resultados, indicaciones alta, plan manejo, observaciones
- Limites: incluir solo campos que aporten valor clinico

### Paso 2: Poblacion de campos

1. Extraer datos de ClinicalData segun campos requeridos por plantilla.
2. Integrar resultados de RAZONAMIENTO_CLINICO (sospecha_dx, red_flags, conducta).
3. Si PIVOTE_IMAGENOLOGICO disponible, integrar hallazgos relevantes.
4. Marcar campos con datos insuficientes -> trigger S-CLARIFICADOR si criticos.

### Paso 3: Formateo telegrafico

- Eliminar articulos (el, la, los, las, un, una, unos, unas)
- Eliminar conectores innecesarios (que, de, por, para cuando redundantes)
- Usar abreviaturas medicas estandar (antec, bilat, c/, dx, ev, hrs, HTA, DM, IRC, SV, tto, vo)
- Sin markdown
- Sin listas numeradas en indicaciones
- Valores lab: solo numero sin unidad

### Paso 4: Filtro parsimonia

Verificar cada dato incluido:
1. Cambia conducta clinica? Si no -> eliminar
2. Imprescindible para diagnostico? Si no -> evaluar eliminacion
3. Afecta pronostico o riesgo? Si no -> evaluar eliminacion
4. Requerido legalmente? Si no -> evaluar eliminacion
5. Redundante con otro campo? Si si -> eliminar de seccion menos relevante

### Paso 5: Wrapper output

Envolver en XML:
- Si razonamiento necesario: <razonamiento>[breve]</razonamiento>
- Siempre: <respuesta>[documento telegrafico]</respuesta>

## Signature Output

```
<respuesta>
[Documento clinico telegrafico segun plantilla tipo_output]
[Campos poblados, filtrados por parsimonia]
[Estilo telegrafico sin relleno]
</respuesta>
```
