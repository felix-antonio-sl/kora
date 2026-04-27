---
_manifest:
  urn: "urn:salud:kb:salubrista-atlas-integrado"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Integracion organica del corpus salubrista, gestion-redes, FIRS y HODOM sin perdida de informacion."
version: "1.0.0"
status: published
tags: [salubrista, atlas, gestion-redes, hospitalista, hospitalizacion-domiciliaria, hodom]
lang: es
relations:
  depends:
    - "urn:salud:kb:salubrista"
  cites:
    - "urn:salud:kb:salubrista-body-of-knowledge"
    - "urn:salud:kb:gestion-redes-indice"
    - "urn:salud:kb:gestion-redes-general"
    - "urn:salud:kb:gestion-redes-unidades"
    - "urn:salud:kb:gestion-redes-urgencias"
    - "urn:salud:kb:gestion-redes-salud-mental"
    - "urn:salud:kb:gestion-redes-herramientas"
    - "urn:salud:kb:firs-framework-integrado-razonamiento-salud"
    - "urn:salud:kb:perfil-salubrista-copiloto-estrategico"
    - "urn:salud:kb:perfil-salubrista-hospitalizacion-integrada"
    - "urn:salud:kb:hodom-reglamento-ds1-2022"
    - "urn:salud:kb:hodom-decreto-exento-31-2024"
    - "urn:salud:kb:hodom-norma-tecnica-2024"
    - "urn:salud:kb:hodom-direccion-tecnica"
    - "urn:salud:kb:hodom-manual-alta-complejidad"
    - "urn:salud:kb:hodom-situacion-chile-2026"
extensions:
  kora:
    family: atlas
    corpus_root_urn: "urn:salud:kb:salubrista"
    role: "integration_map"
    integration_scope: "salud/salubrista + salud/hodom + salud/perfiles"
---

# Atlas integrado Salubrista

Este atlas une el corpus salubrista como un solo cuerpo de conocimiento para
salud publica aplicada, gestion de redes y hospitalizacion integrada. No fusiona
mecanicamente los documentos fuente. Define como se compone el corpus y como
bajar desde una consulta a los nodos correctos.

## Principio De Integracion

La unidad basica del corpus salubrista es:

`problema sanitario + escala + capacidad + continuidad + gobernanza + evidencia`

La pregunta no debe resolverse solo por tema clinico o por dispositivo. Debe
explicitar escala, decision, restricciones, indicadores y consecuencias para la
red.

## Capas Canonicas

| Capa | URN | Funcion |
|------|-----|---------|
| Entrada canonica | `urn:salud:kb:salubrista` | Punto de entrada y contrato de corpus |
| Atlas integrado | `urn:salud:kb:salubrista-atlas-integrado` | Mapa de rutas, modos y partes |
| BOK salubrista | `urn:salud:kb:salubrista-body-of-knowledge` | Doctrina integrada y competencias |
| Gestion de redes | `urn:salud:kb:gestion-redes-indice` | Operacion de redes, unidades, urgencias, salud mental y herramientas |
| FIRS | `urn:salud:kb:firs-framework-integrado-razonamiento-salud` | Control epistemico micro/meso/macro |
| Perfil salubrista | `urn:salud:kb:perfil-salubrista-copiloto-estrategico` | Identidad y limites del copiloto |
| Perfil hospitalizacion integrada | `urn:salud:kb:perfil-salubrista-hospitalizacion-integrada` | Lente hospitalista y continuidad hospital-domicilio |
| HODOM normativo y directivo | familia `hodom-*` | Reglas, direccion tecnica, alta complejidad y situacion Chile |

## Rutas De Uso

### Ruta 1: Diagnostico Situacional

Usar cuando se pida leer un territorio, red, establecimiento o unidad.

1. Entrar por salubrista.
2. Recuperar FIRS para fijar escala e inferencias.
3. Recuperar gestion-redes general y el modulo de unidad/red pertinente.
4. Salida: brechas, prioridades, indicadores, riesgos y opciones de accion.

### Ruta 2: Diseno De Red O Unidad

Usar para modelos de atencion, cartera de servicios, procesos, dotacion,
interoperabilidad, indicadores y gobernanza.

1. Recuperar gestion-redes indice y general.
2. Bajar a unidades, urgencias, salud mental o herramientas.
3. Usar FIRS para separar evidencia clinica, epidemiologica y operacional.
4. Salida: diseno, supuestos, trade-offs y plan de implementacion.

### Ruta 3: Hospitalista De Red

Usar cuando la pregunta trate hospitalizacion intrahospitalaria, capacidad,
camas, altas, boarding, flujo, continuidad y transiciones.

1. Recuperar perfil de hospitalizacion integrada.
2. Recuperar gestion-redes unidades y general.
3. Recuperar herramientas si se requieren KPI, BPMN, madurez o interoperabilidad.
4. Salida: lectura de capacidad, cuello de botella, plan de flujo, tablero y
   criterios de transicion.

### Ruta 4: Hospitalista A Domicilio

Usar para HODOM, HaH, alta precoz, camas virtuales, direccion tecnica, criterios
de ingreso/egreso, reingreso, cuidador y cumplimiento normativo.

1. Recuperar HODOM normativo: DS 1/2022, DE 31/2024 y Norma Tecnica 2024.
2. Recuperar direccion tecnica y manual de alta complejidad.
3. Recuperar gestion-redes unidades y herramientas.
4. Usar FIRS para controlar que la respuesta no confunda caso individual,
   programa, establecimiento y red.
5. Salida: check normativo, ruta operativa, riesgos de seguridad, indicadores y
   gatillos de escalamiento.

### Ruta 5: Evaluacion Y Politica

Usar cuando se soliciten resultados, evaluacion de programa, politica sanitaria,
escenarios o decision de inversion.

1. Recuperar FIRS y gestion-redes general.
2. Recuperar herramientas para KPI y madurez.
3. Recuperar HODOM situacion Chile cuando el tema sea hospitalizacion
   domiciliaria o capacidad virtual.
4. Salida: escenario, evidencia, equidad, sostenibilidad, costo y riesgos
   residuales.

## Regla De Preservacion De Shards

Los archivos `--pNN` son partes materiales del documento raiz indicado por
`extensions.kora.shard_root_urn`. No deben tratarse como corpus independientes.
La entrada canonica siempre es el URN raiz sin sufijo `pNN`.

## Limite De Seguridad

El corpus apoya decisiones de sistema. No prescribe tratamientos individuales,
no reemplaza juicio clinico, no reemplaza normativa vigente y no debe crear una
indicacion de hospitalizacion domiciliaria sin validar estabilidad clinica,
entorno, cuidador, cobertura, consentimiento y capacidad de reingreso.
