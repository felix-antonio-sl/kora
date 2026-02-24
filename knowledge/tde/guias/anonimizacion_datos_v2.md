---
_manifest:
  urn: urn:tde:kb:anonimizacion-datos
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- datos
- privacidad
- anonimizacion
- chile
- tde
lang: es
---

# Guía de Anonimización de Datos

## Marco Conceptual y Definiciones
- **Dato Personal**: información vinculada a persona natural identificada o identificable (RUT, nombre, rasgos físicos).
- **Dato Sensible**: revelan origen étnico, afiliación política, salud, biométricos, orientación sexual, etc.
- **Tratamiento**: cualquier operación técnica sobre datos (recolección, almacenamiento, disociación, comunicación).
- **Identificación**: determinación de identidad específica usando datos únicos.
- **Reidentificación**: proceso de recuperar identidad a partir de datos tratados; riesgo clave a mitigar.

## Atributos y Estados de los Datos
### Clasificación de Atributos
- **Identificadores Directos**: identifican unívocamente (Nombre, RUT, Email, Pasaporte).
- **Identificadores Indirectos**: combinados permiten identificar (Edad, Género, Dirección, Carrera, IP, GPS).
- **Atributos Objetivos**: datos de análisis (Sueldo, Diagnóstico, Afiliación política).

### Estados del Dato
- **Desidentificados**: eliminados identificadores directos; riesgo de reidentificación persiste.
- **Anonimizados**: proceso irreversible; reidentificación imposible; deja de ser dato personal.
- **Seudonimizados**: no atribuibles sin información adicional protegida y separada.
- **Sintéticos**: generados artificialmente para análisis sin comprometer privacidad.

## Riesgos de Privacidad
- **Singularización**: identificación basada en información única o combinación de atributos.
- **Vinculabilidad**: conexión de registros en diferentes conjuntos para identificar personas.
- **Inferencia**: deducción de detalles sensibles usando datos disponibles.

## Proceso de Anonimización
### Fases Generales
1. **Identificar Objetivos**: definir uso (datos abiertos vs interno restringido) y responsables.
2. **Clasificación**: determinar si atributos son vitales, únicos o cruzables con otras fuentes.
3. **Desidentificación**: eliminación/modificación de identificadores directos.
4. **Aplicación de Técnicas**: tratar identificadores indirectos para balancear utilidad y privacidad.
5. **Finalización**: evaluación de utilidad y documentación del balance privacidad/utilidad.

### Uso de Seudónimos
- Sustitución por tokens robustos (aleatorios) sin relación lógica con original.
- Requiere tabla segura de mapeo para gestión interna permitiendo fusión de datos y análisis sin revelar identidad.


## Catálogo de Técnicas
### Enmascaramiento (Masking)
- **Supresión**: eliminar registros completos o atípicos (outliers).
- **Caracteres**: sustitución parcial (asteriscos) manteniendo formato.
- **Cifrado**: codificación reversible con clave para transmisión/almacenamiento.

### Aleatorización
- **Adición de Ruido**: variaciones aleatorias para reducir precisión manteniendo estructura.
- **Permutación**: intercambio de valores entre registros preservando correlaciones.
- **Privacidad Diferencial**: ruido calculado en consultas para proteger identidades individuales en agregados.

### Generalización
- **K-Anonimidad**: cada registro es indistinguible de otros k-1 (clase de equivalencia).
- **Diversidad-L / Proximidad-T**: aseguran diversidad de valores sensibles y ajustan distribución para evitar inferencia.

## Gobernanza y Aplicación
### Eficacia de Técnicas por Riesgo
- **Singularización**: mitigada eficazmente por K-Anonimidad, Diversidad-L, Proximidad-T.
- **Vinculabilidad**: mitigada parcialmente por aleatorización y privacidad diferencial.
- **Inferencia**: mitigada parcialmente por cifrados, ruido, permutación y proximidad-T.

### Casos de Uso Sugeridos
- **Datos Abiertos**: Supresión, K-Anonimidad, Diversidad-L.
- **Entre Organizaciones**: K-Anonimidad, Supresión, Proximidad-T.
- **Interno**: Enmascaramiento, Cifrado, Seudonimización.

## Herramientas y Conclusión
- **Herramientas Open Source**: ARX (<https://arx.deidentifier.org/>), Amnesia (<https://amnesia.openaire.eu/>).
- **Recomendación**: calcular riesgo de identificación ANTES de aplicar técnicas. Colaborar con expertos para adaptar técnicas al contexto y legislación vigente.
