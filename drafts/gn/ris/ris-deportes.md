---
_manifest:
  urn: urn:gn:kb:ris-deportes
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- deportes
- infraestructura
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml: 5989871f8a4ad10e44d060d4f8547ae81b9b4f9a7e9ad5c54891275b83fbcf1f
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.01
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 2
    meat_count: 90
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-deportes.md.json
---

# RIS Infraestructura Deportiva (SNI 2024)
## Source
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf

## RIS Deportes 2024
### Fuente URL
https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf
### Prop Doc
Establecer requisitos y criterios de evaluación para proyectos de infraestructura deportiva.
### Alcance
#### Proyectos Deportivos
Edificación para práctica física y deportiva.
#### Evaluacion Metodologia
Metodología de Formulación y Evaluación de Proyectos de Infraestructura Deportiva.
#### Modalidades Deportivas
- Modalidad-1: Deporte formativo.
- Modalidad-2: Deporte recreativo.
- Modalidad-3: Deporte competitivo.
- Modalidad-4: Deporte de alto rendimiento.
- Nota-Clasificacion: Un proyecto puede atender varias modalidades. Se clasifica por tamaño/estándar o costo.
#### Proyectos Formacion Educacional
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Integrados en establecimientos educacionales. |
| Req-2 | Req-2: Deben ser abiertos a la comunidad. |
| Req-3 | Req-3: Operables de forma autónoma (administración, financiamiento, accesos propios a vía pública). |
#### Def Aumento Oferta
- Criterio: Incremento en número de deportistas atendidos simultáneamente.
- Exclusion: No se considera aumento si solo mejora confort (ej: iluminación, camarines) sin intensificar uso.
### Orientaciones Sectoriales
#### Componentes Instalaciones Deportivas
#### Areas Uso Deportivo
#### Componentes Esenciales
- Espacios de juego (dimensiones, altura requerida).
- Equipos, equipamientos, instalaciones accesorias (camarines, baños, áreas de ejercicios, bodegas, oficinas, primeros auxilios, accesos, circulaciones, estacionamientos).
#### Componentes Opcionales Alto Rendimiento
- Habitaciones, alimentación, lavandería, estudios, entretención, atención especializada física/psicológica.
#### Areas Espectadores
#### Uso Presencial
- Accesos, graderías, circulaciones, boleterías, puntos de venta, baños, estacionamientos.
#### Uso Transmision
- Espacios para trabajo radial, televisivo, periodístico (puntos de prensa, salas especializadas, ascensores especiales).
#### Areas Mixtas
- Administración, seguridad, iluminación, urbanización, muros, losas, estacionamientos.
#### Desglose Presupuestos Prorrateo
#### Paso A Superficies Atribuibles
- Accion: Clasificar áreas según destino (deportistas, espectadores, mixtas).
- Regla-Mixtas: Repartir 50% de superficie a componente deportista y 50% a componente espectador.
#### Paso B Costo Medio Superficie
- Accion-1: Extraer partidas del presupuesto atribuibles a cada componente.
- Accion-2: Sumar costos prorrateados de áreas mixtas y partidas directas.
- Prop: Permite calcular indicadores CAE diferenciados (deportista y espectador).
### Criterios Evaluacion
#### Formativo Recreativo
#### Escala Menor Analisis Simplificado
- Cond: Proyectos de 5.000 a 8.000 UTM sin aumento de oferta.
#### Escala Mediana Costo Eficiencia Deportista
- Cond-1: Inversión en instalaciones existentes.
- Cond-2: Aforo limitado (<500 en cerrados, <1.500 en abiertos).
- Criterio-CAE-Deportista: Costo máximo 0,075 UTM.
#### Escala Mayor Costo Eficiencia Deportista Espectador
- Cond-Aforo-Cerradas: hasta 1.500 personas.
- Cond-Aforo-Abiertas: hasta 2.500 personas.
- Criterio-Evaluacion-Separada: CAE-Deportista 0,075 UTM; CAE-Espectador 0,11 UTM.
#### Alta Competencia
#### Caracteristicas
- Cond-Aforo-Cerradas: >1.500 personas.
- Cond-Aforo-Abiertas: >2.500 personas.
#### Evaluacion
- Prorrateo similar a escala mayor.
- Criterio-CAE-Deportista: hasta 0,12 UTM.
- Criterio-Espectadores: Análisis mediante indicadores VAN y TIR.
#### Alto Rendimiento
#### Niveles
- Regional (CER).
- Nacional (CAR).
#### Evaluacion
- Req: Respaldados por políticas y autoridades deportivas nacionales.
- Criterio-CAE-Deportista-CER: Puede incrementarse hasta 30% con enfoque en alto rendimiento.
- Criterio-CAE-Deportista-CAR: Sin limitación.
- Criterio-Espectadores-CAR: Evaluados con VAN y TIR.
- Rec: Uso de tecnologías para optimizar costos de operación y mantención.
#### Optimizacion
#### Prop
Mejorar eficiencia operativa y generar ahorros o ingresos reales.
#### Ejemplos
Iluminación LED, generadores, protección de canchas, calderas, deshumidificación, paneles fotovoltaicos, control de acceso.
### Postulacion Etapas
#### Prefactibilidad Factibilidad
#### Requisitos
Seguir Normas, Instrucciones y Procedimientos (NIP) de Inversión Pública.
#### Diseno
#### Antecedentes Req
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Formulación y evaluación (usar "Planilla evaluación-sector deporte" o "Metodología General"). |
| Req-2 | Req-2: Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran Edificación"). |
| Req-3 | Req-3: Certificación de propiedad del terreno. |
| Req-4 | Req-4: Presupuesto detallado de consultoría de diseño (incluye personal, horas, gastos adm.). |
| Req-5 | Req-5: Términos de referencia para la consultoría. |
| Req-6 | Req-6: Carta Gantt (incluye licitación, contratación, revisión). |
| Req-7 | Req-7: Calendario de financiamiento (incluye asignaciones y gastos adm.). |
| Req-8 | Req-8: Plan de gestión (según instrucciones del "Plan de Gestión"). |
#### Ejecucion
#### Antecedentes Req
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Presentación directa a ejecución (usando "Planilla evaluación-sector deporte" o "Metodología General"). |
| Req-2 | Req-2: Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran Edificación"). |
| Req-3 | Req-3: Listado valorizado de equipamiento y equipos (con especificaciones). |
| Req-4 | Req-4: Plan de gestión (según "Plan de Gestión"). |
