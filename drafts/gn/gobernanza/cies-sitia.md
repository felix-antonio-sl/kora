---
_manifest:
  urn: urn:gn:kb:cies-sitia
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- seguridad-publica
- emergencias
- sitia
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml: 2e65308d557054d6aaac05e2bc0f238dc5cd5c29391108605cf5827bd3ed8796
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 3.14
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 7
    meat_count: 202
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__cies-sitia.md.json
---

# Centro Integrado de Emergencia y Seguridad (CIES) - SITIA Ñuble
## Source
### Contexto requerido
- staging/gn/kb_gn_080_cies_sitia.md
- CIES SITIA.md
- Ley N° 19.628 sobre Protección de la Vida Privada
### Contexto opcional
- knowledge/domains/gn/kb_gn_200_marco_legal_gores_koda.yml

## Glosario Conceptos Clave
### Proposito
Definir y referenciar conceptos estructurales del CIES y de la integración SITIA.
### Terminos
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-CIES | CIES-SITIA-DESC-CIES-NUBLE-01 | CIES-NUBLE |
| CIES-SITIA-GLOS-SITIA-PATENTES | CIES-SITIA-CAP-SITIA-PATENTES-01 | SITIA-Patentes |
| CIES-SITIA-GLOS-SITIA-EVIDENCIA | CIES-SITIA-CAP-SITIA-EVIDENCIA-01 | SITIA-Evidencia |
| CIES-SITIA-GLOS-SITIA-ARMAS | CIES-SITIA-CAP-SITIA-ARMAS-01 | SITIA-Armas |
| CIES-SITIA-GLOS-SITIA-UNIF-VID | CIES-SITIA-CAP-SITIA-UNIF-VID-01 | SITIA-Unificacion-Videos |
| CIES-SITIA-GLOS-GOB-DATOS | CIES-SITIA-DESC-GOB-DATOS-01 | Gobernanza-Datos |
| CIES-SITIA-GLOS-SPD |  | Subsecretaría de Prevención del Delito (SPD) |
| CIES-SITIA-GLOS-CADENA-CUSTODIA | CIES-SITIA-PROC-CADENA-CUST-01 | Cadena-Custodia-Digital |

## Descripcion General
### Conceptos
| ID | Cpt |
| --- | --- |
| CIES-SITIA-DESC-CIES-NUBLE-01 | CIES-NUBLE |
| CIES-SITIA-DESC-FUNC-PRINC-01 | Funcionalidad-Principal |
| CIES-SITIA-DESC-ALIANZA-01 | Alianza-Estrategica |
| CIES-SITIA-DESC-CAP-POT-01 | Capacidades-Potenciadas |
| CIES-SITIA-DESC-GOB-DATOS-01 | Gobernanza-Datos |

## Objetivos
### Objetivos
| Obj |
| --- |
| Mejorar capacidad de prevención y respuesta ante emergencias y delitos en la región. |
| Fortalecer coordinación interinstitucional para gestión efectiva de seguridad pública. |
| Potenciar análisis de video con herramientas de IA de nivel nacional. |
| Facilitar intercambio de evidencia digital con Ministerio Público y policías. |
| Contribuir al desarrollo social, económico y territorial de Ñuble. |

## Componentes Clave
### Infraestructura Tecnologica y Fisica
#### Sala Monitoreo Central
#### Contexto
Ubicada en GORE Ñuble.
#### Caracteristicas
| Cpt | Def | Ctx | Purp |
| --- | --- | --- | --- |
| Diseño-Ergonomia | Sala de 77,03 m². | Incluye zonas operativas, técnicas, de supervisión y de descanso. | Garantizar rendimiento óptimo y bienestar del personal. |
| Visualizacion-Centralizada | Video Wall de 6x2 metros. | Pantallas LED modulares 4K. | Permitir monitoreo global y detallado de puntos críticos. |
| Estaciones-Trabajo | 7 estaciones de trabajo (6 operadores, 1 supervisor). | 3 estaciones adicionales para Unidad Operativa de Control de Tránsito (UOCT)., Cada estación equipada con monitor Full HD 32", teclado ergonómico, joystick. | Control preciso de cámaras PTZ. |
| Centro-Datos | Infraestructura robusta. | Racks APC NetShelter SX., Servidores redundantes Dell PowerEdge R740., Sistemas de Alimentación Ininterrumpida (UPS). | Garantizar operación continua 24/7. |
#### Sistema Integrado Camaras y Red
#### Elementos
| Cpt | Def | Ctx |
| --- | --- | --- |
| Cobertura-Regional | 209 puntos de vigilancia en 21 comunas. | 140 cámaras PTZ 4K y 69 cámaras multisensor/panorámicas. |
| Conectividad | Red híbrida de alta velocidad con 316 nodos. | 80% fibra óptica (100Mbps) y 20% enlaces inalámbricos (50Mbps). |
| Arquitectura-Federacion | Modelo federado para gestión centralizada con autonomía local. |  |
| Software-Gestion-VMS | Plataforma HikCentral. | Compatibilidad con estándar ONVIF. |
| Almacenamiento-Seguro | Capacidad para 60 días de grabaciones a máxima resolución. |  |
#### Capacidades Analitica Avanzada CIES SITIA
#### Fundamento
El sistema CIES cuenta con analítica de video (VCA) para funciones base (detección de movimiento, seguimiento, conteo, intrusión).
#### Cpt
La capacidad es potenciada por la integración con plataformas especializadas de SITIA.
#### Capacidades
| ID | Cpt | Purp | Mech | Res |
| --- | --- | --- | --- | --- |
| CIES-SITIA-CAP-SITIA-PATENTES-01 | SITIA-Patentes | Complementar la lectura de placas local con una red integrada nacional (pórticos públicos y privados). | Datos contrastados en tiempo real con registro oficial de vehículos con encargo de búsqueda. | Genera dashboards dinámicos sobre zonas críticas de robo y rutas probables. |
| CIES-SITIA-CAP-SITIA-EVIDENCIA-01 | SITIA-Evidencia | Facilitar solicitud, almacenamiento y compartición segura de pruebas audiovisuales. |  | Asegura cadena de custodia digital y reduce tiempos de investigación. |
| CIES-SITIA-CAP-SITIA-ARMAS-01 | SITIA-Armas | Generar alertas automáticas en tiempo real al detectar un arma de fuego en la vía pública. | Implementa modelos de IA (basados en YOLOv11) en la red de cámaras. | Apoya labores de fiscalización y control. |
| CIES-SITIA-CAP-SITIA-UNIF-VID-01 | SITIA-Unificacion-Videos | Centralizar las señales de las cámaras del CIES en una interfaz única a nivel nacional. | Permite acceso a Carabineros de Chile. | Refuerza la coordinación y la capacidad de respuesta ante emergencias. |
### Personal y Estructura Operativa
#### Componentes
| Cpt | Def | Ctx |
| --- | --- | --- |
| Equipo-Humano | 3 operadores y 1 supervisor por turno en la sala. | Se integra personal de la UOCT. |
| Turnos-Operacion | Cobertura inicial de 16 horas diarias (08:00 a 00:00). | Dos turnos rotativos. |
| Roles-Capacitacion |  |  |
| Enlaces-Interinstitucionales | Personal que actúa como facilitador de comunicación directa. |  |
### Procesos y Protocolos Marco Operativo Legal
#### Fundamento
Todas las actuaciones se rigen por un estricto Manual de Operaciones.
#### Requisitos
Garantizar el cumplimiento de la Ley N° 19.628 sobre Protección de la Vida Privada.
#### Procesos
| Cpt | Def |
| --- | --- |
| Protocolos-Vigilancia-Respuesta | Procedimientos estandarizados para monitoreo, detección, clasificación y escalamiento de incidentes. |
| Cadena-Custodia-Digital | Las grabaciones son consideradas evidencia legal. |
| Gestion-Privacidad |  |
| Plan-Contingencia | Análisis de riesgos y plan de acción. |
| Coordinacion-Interinstitucional | Canales de comunicación directos y protocolos de acción conjunta. |

## Sostenibilidad y Modelo Gestion
### Componentes
| Cpt | Mech | Purp |
| --- | --- | --- |
| Financiamiento-Operativo | Continuidad garantizada a través de presupuesto anual. | Cubrir gastos recurrentes (RR.HH., mantenimiento, servicios). |
| Mantenimiento-Garantia |  |  |
| Convenio-Colaboracion | La relación con SITIA se formaliza a través de un convenio marco de colaboración. | Establecer los ejes de cooperación en integración tecnológica, intercambio de datos y capacitación. |

## Beneficios Para Region
### Resultados
- Mayor seguridad y protección (disuasión y respuesta rápida).
- Mejora en los tiempos de respuesta ante emergencias, minimizando daños.
- Fortalecimiento de la coordinación interinstitucional, optimizando uso de recursos.
- Generación de evidencia de alta calidad y estandarizada para apoyar procesos judiciales.
- Acceso a una red de inteligencia nacional, mejorando capacidad de análisis y prevención.
- Creación de un entorno más seguro para la inversión y la vida en comunidad en Ñuble.
