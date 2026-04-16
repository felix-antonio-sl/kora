# Sistema de Vigilancia Epidemiológica de Chile

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes**: Decreto 7/2019; Código Sanitario; RSI 2005; MINSAL Depto. Epidemiología

---

## 1. Marco legal

### 1.1 Base constitucional y legal

- **Código Sanitario (DFL 725/1967)**: Faculta a la autoridad sanitaria para vigilar enfermedades transmisibles y establecer medidas de control
- **DFL 1/2005**: Atribuye a la Subsecretaría de Salud Pública la función de vigilancia epidemiológica
- **Ley 19.937 (2004)**: SEREMI de Salud como autoridad sanitaria regional con función de vigilancia
- **Reglamento Sanitario Internacional (RSI 2005)**: Compromisos internacionales vinculantes (OMS)

### 1.2 Decreto 7/2019 — Enfermedades de Notificación Obligatoria (ENO)

**Instrumento central del sistema de vigilancia.**

Establece:
- Lista de enfermedades de notificación obligatoria
- Modalidades de notificación
- Plazos
- Responsables
- Sanciones por incumplimiento

[VERIFICAR] Puede haber actualizaciones posteriores al Decreto 7/2019

---

## 2. Estructura del sistema de vigilancia

### 2.1 Niveles

```
┌─────────────────────────────────────┐
│     NIVEL CENTRAL                   │
│  Depto. Epidemiología MINSAL        │
│  Subsecretaría de Salud Pública     │
│  ISP (laboratorio de referencia)    │
├─────────────────────────────────────┤
│     NIVEL REGIONAL                  │
│  SEREMI de Salud                    │
│  Unidad de Epidemiología regional   │
├─────────────────────────────────────┤
│     NIVEL LOCAL                     │
│  Establecimientos de salud          │
│  (hospitales, APS, laboratorios)    │
│  Médico tratante → notificación     │
└─────────────────────────────────────┘
```

### 2.2 Flujo de notificación

1. **Médico tratante** detecta caso sospechoso o confirmado
2. **Notifica** a la SEREMI de Salud correspondiente vía EPIVIGILA
3. **SEREMI** investiga, confirma, aplica medidas de control
4. **SEREMI** reporta al nivel central (Depto. Epidemiología MINSAL)
5. **ISP** confirma por laboratorio (cuando corresponde)
6. **MINSAL** consolida, analiza, publica informes, notifica internacionalmente (RSI)

### 2.3 Roles institucionales

| Institución | Función en vigilancia |
|---|---|
| **Depto. Epidemiología MINSAL** | Rectoría, normativa, análisis nacional, informes, RSI |
| **SEREMI de Salud** | Vigilancia regional, investigación de brotes, medidas de control |
| **ISP** | Laboratorio de referencia, confirmación diagnóstica, tipificación |
| **Establecimientos** | Notificación, toma de muestras, tratamiento |
| **DEIS** | Estadísticas vitales, egresos hospitalarios, bases de datos |

---

## 3. Modalidades de vigilancia

### 3.1 Vigilancia universal (pasiva)

- Toda ocurrencia de una ENO debe ser notificada por el médico tratante
- Base del sistema: depende de la sospecha clínica y la notificación

### 3.2 Vigilancia centinela

- Establecimientos o unidades seleccionadas que vigilan activamente condiciones específicas
- Ejemplos:
  - Vigilancia centinela de influenza y virus respiratorios
  - Vigilancia centinela de enfermedades diarreicas agudas
  - Vigilancia centinela de ETS
- No busca captar todos los casos sino estimar tendencias

### 3.3 Vigilancia de laboratorio

- ISP como laboratorio de referencia nacional
- Redes de laboratorio regionales
- Confirmación diagnóstica de: meningococo, salmonella, tuberculosis, VIH, influenza, COVID-19, etc.
- Tipificación molecular y resistencia antimicrobiana
- Vigilancia genómica (incorporada post-COVID)

### 3.4 Vigilancia ambiental

- Calidad del agua, alimentos, vectores
- SEREMI como autoridad fiscalizadora
- Integrada con vigilancia epidemiológica para detección de brotes de fuente común

### 3.5 Vigilancia sindrómica

- Monitoreo de síndromes (respiratorio, diarreico, febril, neurológico)
- Útil para detección temprana de eventos inusuales
- Implementada parcialmente; se fortaleció post-COVID

---

## 4. EPIVIGILA

**Sistema informático oficial de vigilancia epidemiológica de Chile.**

### 4.1 Características

- Plataforma web para la notificación y gestión de casos ENO
- Permite: notificación, investigación epidemiológica, seguimiento, cierre de caso
- Genera alertas automáticas por umbrales
- Conectado con ISP para resultados de laboratorio
- Acceso según perfil: notificador, epidemiólogo SEREMI, nivel central

### 4.2 Proceso en EPIVIGILA

1. Notificación del caso (datos clínicos, demográficos, factores de riesgo)
2. Clasificación: sospechoso → probable → confirmado (o descartado)
3. Investigación epidemiológica: contactos, fuente de exposición
4. Medidas de control: aislamiento, quimioprofilaxis, vacunación de bloqueo
5. Cierre del caso con clasificación final

---

## 5. Clasificación de ENO por modalidad de notificación

### 5.1 Notificación inmediata (dentro de 24 horas)

Enfermedades de alta gravedad o potencial epidémico:
- Cólera
- Peste
- Fiebre amarilla
- Ébola y otras fiebres hemorrágicas
- Influenza por nuevo subtipo
- SARS / MERS / COVID-19 [VERIFICAR categorización actual]
- Meningitis bacteriana / Enfermedad meningocócica
- Poliomielitis / Parálisis flácida aguda
- Sarampión
- Difteria
- Rabia humana
- Botulismo
- Ántrax
- Brote de cualquier enfermedad
- Evento de importancia en salud pública (RSI)

### 5.2 Notificación diaria

- Hepatitis viral (A, B, C, E)
- Tuberculosis
- VIH/SIDA
- Sífilis (todas las formas)
- Gonorrea
- Coqueluche
- Fiebre tifoidea y paratifoidea
- Enfermedad de Chagas
- Hantavirus
- Leptospirosis
- Dengue
- Malaria
- Otros [VERIFICAR lista completa actualizada del Decreto 7]

### 5.3 Notificación semanal/consolidada

- Varicela
- Parotiditis
- Influenza (centinela)
- Otros según normativa

### 5.4 Notificación por resultado de laboratorio (ISP)

- Agentes de importancia en salud pública confirmados por ISP
- Resistencia antimicrobiana

---

## 6. Investigación de brotes

### 6.1 Definición

**Brote**: Ocurrencia de casos de una enfermedad en número mayor al esperado, en un lugar y tiempo definidos.

### 6.2 Pasos de la investigación (CDC/OMS adaptado a Chile)

1. **Confirmar la existencia del brote**: Verificar diagnósticos, comparar con línea de base
2. **Establecer definición de caso**: Clínica + epidemiológica + laboratorio
3. **Buscar y contar casos**: Búsqueda activa
4. **Caracterizar el brote**: Tiempo (curva epidémica), lugar (mapeo), persona (edad, sexo, exposiciones)
5. **Generar hipótesis**: Fuente, modo de transmisión, vehículo
6. **Evaluar hipótesis**: Estudio analítico (caso-control, cohorte retrospectiva) si es necesario
7. **Implementar medidas de control**: No esperar a confirmar hipótesis
8. **Comunicar hallazgos**: Informe, retroalimentación, comunicación de riesgo
9. **Seguimiento y evaluación de las medidas**

### 6.3 Responsable

- SEREMI de Salud lidera la investigación en su territorio
- Apoyada por el Depto. de Epidemiología MINSAL cuando es necesario
- ISP provee apoyo de laboratorio

---

## 7. Reglamento Sanitario Internacional (RSI 2005)

### 7.1 Obligaciones de Chile

- Notificar a la OMS eventos que constituyan una **Emergencia de Salud Pública de Importancia Internacional (ESPII)**
- Mantener capacidades básicas de vigilancia y respuesta en puertos, aeropuertos y pasos fronterizos
- Designar un **Punto Focal Nacional RSI** (en el Depto. Epidemiología MINSAL)
- Evaluar todo evento mediante el **Instrumento de Decisión del Anexo 2 del RSI**

### 7.2 Capacidades básicas RSI

- Detectar eventos inusuales en el territorio
- Evaluar y notificar al nivel central dentro de 48 horas
- Notificar a la OMS dentro de 24 horas (si aplica)
- Responder con medidas de contención
- Mantener capacidades en puntos de entrada internacionales

---

## 8. Vigilancia ESAVI

**ESAVI**: Evento Supuestamente Atribuido a Vacunación o Inmunización.

- Sistema de vigilancia pasiva y activa post-vacunación
- Notificación obligatoria de eventos graves
- Investigación de causalidad (clasificación OMS)
- ISP participa en la investigación de lotes
- Comité asesor de ESAVI [VERIFICAR estructura actual]
- Fortalecido significativamente durante la vacunación COVID-19

---

## 9. Productos de la vigilancia

| Producto | Periodicidad | Contenido |
|---|---|---|
| Informe epidemiológico semanal | Semanal | Situación de ENO, brotes, alertas |
| Boletín epidemiológico trimestral | Trimestral | Análisis de tendencias |
| Informe de vigilancia de VIH/SIDA | Anual | Situación VIH |
| Informe de vigilancia de TBC | Anual | Situación tuberculosis |
| Informe de vigilancia de influenza | Estacional | Circulación viral, cepas |
| Informe situación COVID-19 | [VERIFICAR frecuencia actual] | Casos, hospitalización, variantes |
| Estadísticas vitales (DEIS) | Anual | Mortalidad, natalidad |

---

## 10. Fuentes

- Chile. Decreto 7/2019. Enfermedades de Notificación Obligatoria.
- Chile. Código Sanitario (DFL 725/1967).
- OMS. Reglamento Sanitario Internacional (2005). 3ª edición, 2016.
- MINSAL. Departamento de Epidemiología. epi.minsal.cl
- ISP. Instituto de Salud Pública. www.ispch.cl
- MINSAL. Norma técnica de vigilancia de enfermedades transmisibles.
- CDC. Principles of Epidemiology in Public Health Practice. 3rd ed, 2012.
