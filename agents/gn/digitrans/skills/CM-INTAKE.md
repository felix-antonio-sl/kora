---
_manifest:
  urn: urn:gn:skill:digitrans-intake:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTAKE

## Proposito
Clasificar cada consulta entrante de DIGITRANS por dominio TDE, nivel de profundidad y necesidad de puente evolutivo.

## Input/Output
- **Input:** Consulta entrante sobre Transformacion Digital del Estado
- **Output:** Clasificacion estructurada: [Dominio TDE] + [Nivel de profundidad] + [Necesita ORKO bridge?]

## Procedimiento
1. Identificar si la consulta cae en normativa, plataformas, estrategia/madurez o CPAT.
2. Determinar si la respuesta puede quedarse en marco TDE o requiere puente hacia ORKO y H_org.
3. Detectar cuando la consulta exige distinguir norma vigente, dato institucional, interpretacion o incertidumbre.
4. Devolver clasificacion lista para enrutar a S-NORMATIVO, S-PLATAFORMAS, S-ORKO-BRIDGE o S-CPAT.

## Signature Output
Clasificacion estructurada: [Dominio TDE] + [Nivel de profundidad] + [Necesita ORKO bridge?] + [Etiquetas requeridas].
