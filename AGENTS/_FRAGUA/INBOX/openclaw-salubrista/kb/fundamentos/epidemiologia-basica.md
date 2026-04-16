# Epidemiología Básica — Conceptos Fundamentales

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes**: Gordis (Epidemiology, 6th ed); Rothman (Modern Epidemiology, 3rd ed); Bonita R et al (Epidemiología básica, OMS, 2008)

---

## 1. Medidas de frecuencia

### 1.1 Prevalencia

- **Prevalencia puntual**: Proporción de individuos con la enfermedad en un momento dado
  - P = Casos existentes / Población total en ese momento
  - No tiene unidades de tiempo; es una proporción (0-1)
- **Prevalencia de período**: Proporción que tuvo la enfermedad en algún momento durante un período
- **Relación con incidencia**: P ≈ Incidencia × Duración (cuando la prevalencia es baja y la población es estable)
- **Uso**: Planificación de servicios, carga de enfermedad

### 1.2 Incidencia

#### Incidencia acumulada (riesgo)
- IA = Casos nuevos durante un período / Población en riesgo al inicio del período
- Proporción (0-1); requiere definir período
- Interpretación: Probabilidad de enfermar en ese período
- Sinónimo: Riesgo, proporción de incidencia

#### Tasa de incidencia (densidad de incidencia)
- TI = Casos nuevos / Personas-tiempo en riesgo
- Unidades: Personas-tiempo⁻¹ (ej: por 1.000 personas-año)
- Permite periodos de seguimiento desiguales
- No es una proporción; es una tasa instantánea

#### Tasa de ataque
- Incidencia acumulada en contexto de brote
- TA = Enfermos / Expuestos

### 1.3 Tasas de mortalidad

| Tasa | Numerador | Denominador |
|---|---|---|
| Mortalidad bruta | Total defunciones | Población total |
| Mortalidad específica por edad | Defunciones en grupo etario | Población en ese grupo |
| Mortalidad específica por causa | Defunciones por causa X | Población total |
| Mortalidad infantil | Defunciones <1 año | Nacidos vivos |
| Mortalidad neonatal | Defunciones <28 días | Nacidos vivos |
| Mortalidad materna | Muertes maternas | Nacidos vivos (×100.000) |
| Letalidad | Defunciones por enfermedad X | Casos de enfermedad X |

### 1.4 Estandarización

#### Estandarización directa
- Aplica las tasas específicas por edad de la población estudiada a una población estándar
- Requiere: Tasas específicas por edad de la población estudiada + distribución etaria de la población estándar
- Resultado: Tasa estandarizada (ajustada) — comparable entre poblaciones

#### Estandarización indirecta
- Aplica las tasas de una población de referencia a la estructura etaria de la población estudiada
- Resultado: SMR (Razón de Mortalidad Estandarizada) = Muertes observadas / Muertes esperadas
- SMR > 1: exceso de mortalidad; SMR < 1: mortalidad menor que la referencia
- Útil cuando no se dispone de tasas específicas por edad

---

## 2. Medidas de asociación

### 2.1 Riesgo Relativo (RR)

- RR = Incidencia en expuestos / Incidencia en no expuestos
- Interpretación: Cuántas veces más riesgo tienen los expuestos
- RR = 1: no asociación; RR > 1: factor de riesgo; RR < 1: factor protector
- Obtenible en: Estudios de cohorte, ensayos clínicos

### 2.2 Odds Ratio (OR)

- OR = (a × d) / (b × c) en tabla 2×2
- Interpretación: Aproximación al RR cuando la enfermedad es rara (<10%)
- Obtenible en: Estudios de caso-control (única medida de asociación posible)
- También calculable en cohortes y transversales

### 2.3 Riesgo Atribuible (RA) / Diferencia de riesgo

- RA = Incidencia en expuestos − Incidencia en no expuestos
- Interpretación: Exceso de riesgo atribuible a la exposición
- Fracción atribuible en expuestos (FAE) = RA / Incidencia en expuestos
- Fracción atribuible poblacional (FAP) = (Incidencia total − Incidencia en no expuestos) / Incidencia total

### 2.4 Número Necesario a Tratar (NNT)

- NNT = 1 / Reducción absoluta del riesgo (RAR)
- RAR = Riesgo en grupo control − Riesgo en grupo tratamiento
- Interpretación: Número de pacientes que hay que tratar para evitar un evento adverso
- NNT bajo = tratamiento más efectivo
- NND (Número Necesario para Dañar): análogo para efectos adversos

---

## 3. Diseños de estudio epidemiológico

### 3.1 Estudios descriptivos

| Diseño | Características | Utilidad |
|---|---|---|
| **Reporte de caso** | Descripción de 1 caso inusual | Generar hipótesis |
| **Serie de casos** | Descripción de varios casos | Identificar patrones |
| **Ecológico (correlacional)** | Unidad de análisis = grupo/población | Comparar poblaciones; falacia ecológica |
| **Transversal (prevalencia)** | Medición simultánea de exposición y enfermedad | Prevalencia; no establece temporalidad |

### 3.2 Estudios analíticos observacionales

| Diseño | Dirección | Medida de asociación | Ventajas | Limitaciones |
|---|---|---|---|---|
| **Caso-control** | Enfermedad → Exposición (retrospectivo) | OR | Eficiente para enfermedades raras; rápido; económico | No mide incidencia; sesgo de recuerdo; selección de controles |
| **Cohorte prospectiva** | Exposición → Enfermedad (hacia adelante) | RR, TI, RA | Establece temporalidad; mide incidencia; múltiples desenlaces | Costoso; largo; pérdida de seguimiento |
| **Cohorte retrospectiva** | Registros pasados → Desenlace | RR | Más rápido que prospectivo | Depende de calidad de registros |

### 3.3 Estudios experimentales

| Diseño | Características | Estándar |
|---|---|---|
| **Ensayo clínico aleatorizado (ECA)** | Asignación aleatoria de intervención; grupo control | Gold standard para causalidad |
| **Ensayo comunitario** | Intervención a nivel de comunidad | Evaluación de políticas/programas |
| **Ensayo de campo** | Intervención en población sana (ej: vacunas) | Eficacia de vacunas |

### 3.4 Jerarquía de evidencia

```
1. Revisiones sistemáticas / Meta-análisis de ECA
2. ECA individuales
3. Estudios de cohorte
4. Estudios de caso-control
5. Series de casos
6. Opinión de expertos
```

---

## 4. Sesgos

### 4.1 Sesgo de selección

- Error en la selección de participantes que distorsiona la asociación
- Tipos:
  - **Sesgo de Berkson**: Casos hospitalarios no representan la población
  - **Sesgo del voluntario**: Autoselección de participantes
  - **Sesgo de sobrevivencia**: Solo se estudia a los que sobrevivieron
  - **Sesgo de detección**: Mayor vigilancia en expuestos
  - **Pérdida de seguimiento diferencial**: En cohortes

### 4.2 Sesgo de información (medición)

- Error en la medición de exposición o desenlace
- Tipos:
  - **Sesgo de recuerdo (recall bias)**: Casos recuerdan más exposiciones que controles
  - **Sesgo del entrevistador**: Diferencial según conocimiento del estado de caso/control
  - **Sesgo de clasificación**: No diferencial (hacia el nulo) o diferencial (en cualquier dirección)
  - **Sesgo de reporte**: Deseabilidad social

### 4.3 Confusión

- Variable que está asociada tanto con la exposición como con el desenlace, y no es un paso intermedio en la cadena causal
- Distorsiona la verdadera asociación
- **Control de confusión**:
  - En diseño: Aleatorización, restricción, pareamiento
  - En análisis: Estratificación (Mantel-Haenszel), ajuste multivariado, propensity score

---

## 5. Causalidad

### 5.1 Criterios de Hill (1965)

1. **Fuerza de la asociación**: Mayor RR/OR → más probable causalidad
2. **Consistencia**: Replicación en diferentes estudios y poblaciones
3. **Especificidad**: Una causa → un efecto (débil; multicausalidad es la norma)
4. **Temporalidad**: La exposición precede al efecto (**único criterio necesario**)
5. **Gradiente biológico (dosis-respuesta)**: Mayor exposición → mayor efecto
6. **Plausibilidad biológica**: Mecanismo biológico conocido
7. **Coherencia**: Compatible con la historia natural de la enfermedad
8. **Evidencia experimental**: Si existe, fortalece
9. **Analogía**: Causas similares producen efectos similares

### 5.2 Modelo contrafactual

- Causalidad = diferencia entre lo observado y lo que habría ocurrido sin la exposición
- Base teórica del ECA: el grupo control representa el contrafactual
- Fundamento de la inferencia causal moderna (Rubin, Pearl)

---

## 6. Tablas de vida

### 6.1 Tabla de vida de cohorte (generacional)

- Sigue una cohorte real desde el nacimiento hasta la muerte
- Requiere décadas de seguimiento
- Rara vez factible

### 6.2 Tabla de vida actual (de período)

- Usa tasas de mortalidad específicas por edad en un período dado
- Asume que las tasas actuales se mantienen (población estacionaria hipotética)
- Producto: **Esperanza de vida al nacer** y a distintas edades
- Componentes: qx (probabilidad de muerte), lx (sobrevivientes), dx (muertes), Lx (años vividos), Tx (años vividos acumulados), ex (esperanza de vida)

### 6.3 Método de Kaplan-Meier

- Estimación no paramétrica de la función de supervivencia
- Maneja censura (pérdida de seguimiento, fin del estudio)
- Curva de supervivencia
- Comparación entre grupos: Log-rank test

---

## 7. Fuentes

- Gordis L. Epidemiology. 6th ed. Philadelphia: Elsevier, 2019.
- Rothman KJ, Greenland S, Lash TL. Modern Epidemiology. 3rd ed. Philadelphia: Lippincott, 2008.
- Bonita R, Beaglehole R, Kjellström T. Epidemiología básica. 2ª ed. Washington: OPS, 2008.
- Hill AB. The environment and disease: association or causation? Proc R Soc Med 1965;58:295-300.
- Szklo M, Nieto FJ. Epidemiology: Beyond the Basics. 4th ed. Burlington: Jones & Bartlett, 2019.
