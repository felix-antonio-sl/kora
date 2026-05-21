---
_manifest:
  urn: urn:salud:kb:informatica-medica-ia
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Bridging AI and Human Intelligence in Healthcare (Hubner et al, Springer
      2026). INBOX/salud/
  version: 1.0.0
version: 1.0.0
status: publicado
family: note
tags:
- salud
- ia
- cdss
- machine-learning
- nlp
- etica-ia
- implementacion
lang: es
relations:
  cites:
  - urn:salud:kb:informatica-medica-indice
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:informatica-medica-ia
---

# Inteligencia Artificial en Salud

## Principios de IA en salud

- **Machine Learning**: aprendizaje supervisado/no-supervisado.
 Aplicacion: prediccion de deterioro, readmisiones, sepsis.
- **Deep Learning**: redes neuronales multicapa. Aplicacion: imagenologia,
 dermatologia, patologia digital.
- **NLP (Natural Language Processing)**: extraccion de texto clinico.
 Aplicacion: codificacion automatica, extraccion de fenotipos, summarizacion.

## Clinical Decision Support Systems (CDSS)

Sistemas que asisten la decision clinica con conocimiento basado en evidencia.
Tipos:
- **Basados en conocimiento**: reglas if-then, arboles de decision, guias
- **Basados en datos**: modelos predictivos entrenados en datos historicos
- **Hibridos**: combinacion de ambos

### Desafios de implementacion

1. **Alerta fatiga**: exceso de alertas → el clinico las ignora todas.
 Solucion: estratificar por severidad, learning loop de dismissals.
2. **Integracion con EHR**: el CDSS debe operar dentro del flujo clinico,
 no como sistema externo.
3. **Explicabilidad**: el clinico necesita entender POR QUE el sistema
 recomienda algo (no solo que lo recomienda).
4. **Sesgo algoritmico**: datos de entrenamiento no representativos producen
 recomendaciones inequitativas.

## Etica y regulacion de IA en salud

- **EU AI Act**: clasifica sistemas de IA en salud como "alto riesgo"
- **FDA Software as Medical Device (SaMD)**: marco regulatorio para software
 que toma decisiones clinicas sin intervencion humana
- **Principios eticos**: transparencia, equidad, no maleficencia,
 responsabilidad, privacidad
- **Brecha digital**: la IA puede ampliar desigualdades si no se disena
 para poblaciones diversas

## Implementacion de proyectos de IA

Framework de implementation science aplicado a IA en salud:
1. Evaluacion de preparacion organizacional
2. Seleccion del problema clinico (no tecnologico)
3. Desarrollo con datos locales representativos
4. Validacion prospectiva (no solo retrospectiva)
5. Integracion en el flujo de trabajo (no como add-on)
6. Monitoreo continuo de desempeno y equidad
