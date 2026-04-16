# Epidemiología Aplicada

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes**: CDC Field Epidemiology Manual; OMS; Gregg (Field Epidemiology, 3rd ed)

---

## 1. Investigación de brotes

### 1.1 Los 10 pasos (CDC)

1. **Prepararse para el trabajo de campo**: Equipo, logística, permisos, EPP
2. **Verificar el diagnóstico**: Confirmar casos clínica y/o laboratorialmente
3. **Confirmar la existencia del brote**: Comparar con la línea de base esperada
4. **Definir e identificar casos**: Crear definición de caso (sospechoso, probable, confirmado)
5. **Describir los datos**: Caracterizar por tiempo, lugar y persona
6. **Desarrollar hipótesis**: Sobre fuente, modo de transmisión, vehículo
7. **Evaluar hipótesis**: Estudio analítico si es necesario (caso-control, cohorte)
8. **Refinar hipótesis y ejecutar estudios adicionales**: Laboratorio, ambiental
9. **Implementar medidas de prevención y control**: Desde el inicio, no esperar
10. **Comunicar hallazgos**: Informe escrito, retroalimentación, publicación

### 1.2 Curva epidémica

**Histograma de casos por fecha de inicio de síntomas.**

| Patrón | Interpretación |
|---|---|
| **Fuente común puntual** | Pico agudo, una exposición | 
| **Fuente común continua** | Meseta prolongada |
| **Fuente propagada** | Picos sucesivos (persona a persona) |
| **Mixta** | Fuente común + propagación secundaria |

**Análisis de la curva**:
- Período de incubación: Desde la exposición al primer caso
- Pico: Período de incubación mediano desde la exposición
- Cola: Casos secundarios o exposición prolongada
- Retro-cálculo: Estimar fecha de exposición restando período de incubación

### 1.3 Estudios analíticos en brotes

#### Estudio de cohorte retrospectivo
- Cuando la población expuesta es conocida y acotada (ej: banquete)
- Tabla de ataque por alimento/exposición
- RR por exposición

#### Estudio de caso-control
- Cuando la población en riesgo es grande o desconocida
- Casos: enfermos; Controles: no enfermos de la misma población
- OR por exposición

### 1.4 Medidas de control

| Nivel | Medidas |
|---|---|
| **Fuente** | Retirar alimento contaminado, tratar casos, cerrar fuente |
| **Transmisión** | Cuarentena, aislamiento, desinfección, control de vectores |
| **Susceptibles** | Vacunación de bloqueo, quimioprofilaxis, educación |

---

## 2. Análisis de Situación de Salud (ASIS)

### 2.1 Definición

Proceso analítico-sintético que permite caracterizar, medir y explicar el perfil de salud-enfermedad de una población, incluyendo los daños, los riesgos y los determinantes, para identificar necesidades y prioridades, y orientar intervenciones.

### 2.2 Componentes del ASIS

1. **Contexto demográfico**: Estructura etaria, pirámide poblacional, crecimiento, migración
2. **Contexto socioeconómico**: Pobreza, educación, empleo, vivienda, saneamiento
3. **Perfil de mortalidad**: Causas principales, tasas específicas, tendencias, AVPP
4. **Perfil de morbilidad**: Prevalencia de ENT, transmisibles, salud mental, factores de riesgo
5. **Carga de enfermedad**: AVISA/DALY
6. **Respuesta del sistema**: Oferta de servicios, cobertura, acceso, calidad
7. **Determinantes sociales**: Gradientes, inequidades territoriales y socioeconómicas
8. **Priorización**: Métodos de priorización (Hanlon, CENDES, matriz de priorización)

### 2.3 Sala de situación (Room of Situation)

- Espacio físico y/o virtual con información epidemiológica actualizada
- Indicadores clave desplegados en tableros
- Monitoreo de tendencias, alertas, brotes
- Herramienta de gestión para toma de decisiones
- Componentes: mapas, gráficos de tendencia, indicadores semáforo, reportes

---

## 3. Vigilancia epidemiológica — conceptos técnicos

### 3.1 Tipos de vigilancia

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Pasiva** | Depende de notificación espontánea del médico | ENO habitual |
| **Activa** | Búsqueda sistemática de casos por el sistema de vigilancia | Parálisis flácida aguda, sarampión |
| **Centinela** | Sitios seleccionados vigilan condiciones específicas | Influenza centinela |
| **Sindrómica** | Monitoreo de síndromes (no diagnósticos específicos) | IRA, EDA, síndrome febril |
| **Laboratorial** | Basada en resultados de laboratorio | Resistencia antimicrobiana |
| **Basada en eventos** | Captura de señales de fuentes no tradicionales (medios, redes) | EIOS (OMS) |

### 3.2 Indicadores de vigilancia

| Indicador | Definición |
|---|---|
| **Sensibilidad** | Proporción de casos reales que el sistema detecta |
| **Especificidad** | Proporción de no-casos correctamente excluidos |
| **Valor predictivo positivo** | Proporción de notificaciones que son casos reales |
| **Oportunidad** | Tiempo entre el evento y la notificación/respuesta |
| **Representatividad** | Si los datos reflejan la distribución real en la población |
| **Simplicidad** | Facilidad de operación |
| **Flexibilidad** | Capacidad de adaptarse a cambios |
| **Aceptabilidad** | Disposición de los notificadores a participar |

### 3.3 Evaluación de sistemas de vigilancia (CDC)

Marco para evaluar sistemas de vigilancia: utilidad, atributos (los indicadores de arriba), costo, y recomendaciones de mejora.

---

## 4. Evaluación de pruebas diagnósticas

### 4.1 Tabla 2×2

```
                Enfermedad
              +         -
Prueba  +    VP        FP      → VPP = VP/(VP+FP)
        -    FN        VN      → VPN = VN/(FN+VN)
             ↓         ↓
          Sens       Espec
         VP/(VP+FN)  VN/(VN+FP)
```

### 4.2 Medidas

| Medida | Fórmula | Interpretación |
|---|---|---|
| **Sensibilidad** | VP / (VP + FN) | Capacidad de detectar enfermos (pocos FN) |
| **Especificidad** | VN / (VN + FP) | Capacidad de descartar sanos (pocos FP) |
| **VPP** | VP / (VP + FP) | Probabilidad de estar enfermo si prueba + |
| **VPN** | VN / (VN + FN) | Probabilidad de estar sano si prueba - |
| **LR+** | Sens / (1 - Espec) | Cuánto aumenta la probabilidad post-test |
| **LR-** | (1 - Sens) / Espec | Cuánto disminuye la probabilidad post-test |
| **Exactitud** | (VP + VN) / Total | Proporción de clasificaciones correctas |

### 4.3 Efecto de la prevalencia

- **VPP aumenta** con mayor prevalencia (más enfermos → menos FP relativos)
- **VPN aumenta** con menor prevalencia
- Sensibilidad y especificidad son intrínsecas a la prueba y no cambian con la prevalencia (en teoría)

### 4.4 Curva ROC

- Gráfico de Sensibilidad (eje Y) vs 1-Especificidad (eje X) para distintos puntos de corte
- **AUC (Área Bajo la Curva)**: Medida global de discriminación
  - AUC = 0.5: no discrimina (azar)
  - AUC = 1.0: discriminación perfecta
  - AUC > 0.8: generalmente considerado bueno
- Permite elegir el punto de corte óptimo según contexto clínico

### 4.5 Pruebas en paralelo y en serie

| Estrategia | Efecto | Uso |
|---|---|---|
| **En paralelo** (cualquiera +) | ↑ Sensibilidad, ↓ Especificidad | Tamizaje, urgencia |
| **En serie** (ambas +) | ↓ Sensibilidad, ↑ Especificidad | Confirmación diagnóstica |

---

## 5. Tamizaje poblacional

### 5.1 Criterios de Wilson y Jungner (OMS, 1968)

1. La enfermedad debe ser un problema de salud importante
2. Debe existir un tratamiento aceptado para los casos detectados
3. Deben existir medios para el diagnóstico y tratamiento
4. Debe haber una fase latente o presintomática reconocible
5. Debe existir una prueba de tamizaje adecuada
6. La prueba debe ser aceptable para la población
7. Se debe conocer la historia natural de la enfermedad
8. Debe existir una política consensuada sobre a quién tratar
9. El costo del programa debe ser equilibrado con el gasto total en salud
10. El tamizaje debe ser un proceso continuo, no puntual

### 5.2 Sesgos del tamizaje

| Sesgo | Descripción |
|---|---|
| **Lead time bias** | Aparente aumento de sobrevida por diagnóstico más temprano (sin cambio real) |
| **Length time bias** | El tamizaje detecta preferentemente casos de progresión lenta |
| **Overdiagnosis bias** | Detección de condiciones que nunca habrían causado síntomas o muerte |
| **Sesgo del voluntario** | Los que participan son más sanos |

### 5.3 Evaluación de programas de tamizaje

- Medida ideal: Reducción de mortalidad específica en ECA
- Indicadores de proceso: Cobertura, tasa de detección, VPP, tasa de referencia
- Balance beneficio/daño: Sobrediagnóstico, falsos positivos, ansiedad, procedimientos innecesarios

---

## 6. Fuentes

- CDC. Principles of Epidemiology in Public Health Practice. 3rd ed. Atlanta, 2012.
- Gregg MB (ed). Field Epidemiology. 3rd ed. Oxford University Press, 2008.
- OMS. Evaluación de sistemas de vigilancia. Guía práctica.
- Wilson JMG, Jungner G. Principles and practice of screening for disease. WHO Public Health Papers 34. Geneva, 1968.
- Sackett DL et al. Clinical Epidemiology: A Basic Science for Clinical Medicine. 2nd ed, 1991.
- OPS. Módulos de principios de epidemiología para el control de enfermedades (MOPECE). 2ª ed, 2011.
