---
_manifest:
  urn: "urn:salud:kb:salubrista"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Corpus consolidado desde gestion-redes, FIRS, perfiles salubristas, HODOM y dossier salubrista-base-2026-04-27."
version: "1.0.0"
status: published
tags: [salubrista, salud-publica, gestion-redes, hospitalista, hospitalizacion-domiciliaria, hodom, corpus, indice]
lang: es
relations:
  cites:
    - "urn:salud:kb:salubrista-atlas-integrado"
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
    family: catalog
    corpus_root: true
---

# Corpus Salubrista

Indice canonico del corpus `salud/salubrista`. Fija
`urn:salud:kb:salubrista` como punto de entrada productivo para el agente
salubrista y para sus modos de activacion como hospitalista de red y
hospitalista a domicilio.

El corpus se integra mediante el
[Atlas integrado Salubrista](urn:salud:kb:salubrista-atlas-integrado), que
define capas, rutas de uso, modos operativos y regla de preservacion de shards.

## Capas Del Corpus

- [Body of Knowledge Salubrista](urn:salud:kb:salubrista-body-of-knowledge):
  marco integrado de salud publica aplicada, gestion de redes, hospitalizacion
  como sistema, HODOM/HaH, evaluacion, politica y seguridad.
- [Atlas integrado](urn:salud:kb:salubrista-atlas-integrado): mapa de rutas
  para consultas de territorio, red, establecimiento, unidad hospitalaria,
  hospitalizacion domiciliaria y evaluacion.
- [Gestion de Redes Asistenciales](urn:salud:kb:gestion-redes-indice): corpus
  operativo para diseno, operacion y mejora continua de redes y unidades.
- [FIRS](urn:salud:kb:firs-framework-integrado-razonamiento-salud): marco de
  razonamiento clinico-epidemiologico-gestion para no mezclar niveles micro,
  meso y macro.
- [Perfil Salubrista](urn:salud:kb:perfil-salubrista-copiloto-estrategico):
  identidad, limites y modo de colaboracion con el humano conductor.
- [Perfil Hospitalizacion Integrada](urn:salud:kb:perfil-salubrista-hospitalizacion-integrada):
  lente hospitalista para integrar cama cerrada, domicilio, continuidad,
  capacidad y transiciones.
- [HODOM](urn:salud:kb:hodom-reglamento-ds1-2022): normativa y manuales de
  hospitalizacion domiciliaria.

## Modos De Activacion

### Salubrista General

Usar para diagnostico situacional, vigilancia, gestion territorial, diseno de
redes, evaluacion de programas, politica sanitaria y lectura de inequidad.

### Hospitalista De Red

Usar cuando la pregunta trate cama, capacidad, flujo hospitalario, unidad de
agudos, UCI, altas, boarding, transiciones, continuidad asistencial o
coordinacion hospital-red. La base primaria es gestion-redes + FIRS + perfil de
hospitalizacion integrada.

### Hospitalista A Domicilio

Usar cuando la pregunta trate hospitalizacion domiciliaria, HODOM, HaH, alta
precoz con domicilio, direccion tecnica HD, cumplimiento normativo, criterios de
ingreso/egreso, escalamiento, reingreso, cuidador, entorno domiciliario,
monitoreo remoto o camas virtuales. La base primaria es HODOM + gestion-redes
unidades/herramientas + FIRS.

## Regla De Uso

Toda consulta entra por `urn:salud:kb:salubrista` y se baja a una ruta:

1. determinar escala: unidad, establecimiento, red, territorio, nacional o
   multi;
2. clasificar modo: salubrista general, hospitalista de red u hospitalista a
   domicilio;
3. recuperar FIRS si hay riesgo de mezclar inferencias clinicas, poblacionales
   y de gestion;
4. recuperar gestion-redes para diseno y operacion;
5. recuperar HODOM cuando exista componente domiciliario, normativo o de
   capacidad virtual;
6. declarar vacio o necesidad de verificacion vigente cuando el corpus no cubra
   una norma, fecha, precio, regulacion o dato operacional actual.

Este corpus no reemplaza la conduccion humana ni las normas vigentes. Su uso
previsto es apoyo tecnico a decisiones de sistema con supuestos explicitos,
trazabilidad y preservacion de responsabilidad humana.
