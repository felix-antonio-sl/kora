---
_manifest:
  urn: urn:gn:kb:manual-activo-fijo
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/gestion/kb_gn_041_manual_activo_fijo_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- activo-fijo
- contabilidad
- nicsp
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_041_manual_activo_fijo_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_041_manual_activo_fijo_koda.yml: ec3fc91f201af120cd93c6287142dcf3bb1c493fa94f5105879cfac9587b51ab
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.92
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 2
    meat_count: 278
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-activo-fijo.md.json
---

# Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo

## Manual 2 3 Gestion del Ciclo de Vida del Activo Fijo

### Objetivo

#### Objetivos
Administrar el patrimonio físico institucional, asegurando el correcto registro, valorización, control y disposición de los bienes conforme a las Normas Internacionales de Contabilidad del Sector Público (NICSP).

### Seccion I Marco Normativo y Clasificacion

#### Fundamentos Legales

#### Contexto
La gestión de activos fijos se rige por:

#### Clasificacion de Bienes

#### Por Naturaleza

#### Items
- Bienes Muebles: Mobiliario, equipos computacionales, maquinaria, vehículos.
- Bienes Inmuebles: Terrenos, edificios, instalaciones, infraestructura.
- Bienes Intangibles: Software, licencias, derechos, patentes.

#### Por Tratamiento Contable

#### Items
- Patrimoniales: Registrados en el balance (valor ≥ umbral de capitalización).
- Inventario Administrativo: Bienes menores controlados pero no capitalizados.

#### Por Uso

#### Items
- En Uso: Asignados a funcionarios o unidades.
- En Bodega: Disponibles para asignación.
- En Comodato: Cedidos temporalmente a terceros.
- Dados de Baja: Fuera de servicio, pendientes de disposición final.

#### Umbral de Capitalizacion

#### Items
- El GORE define un umbral monetario (típicamente 3 UTM) bajo el cual los bienes se consideran "gasto" y no se capitalizan.
- Bienes bajo el umbral pueden registrarse en inventario administrativo para control físico sin impacto patrimonial.

### Seccion II Alta de Bienes

#### Recepcion y Prealta

#### Origen de los Bienes

#### Items
- Compra Directa (Subtítulo 29): Adquisición de Activos No Financieros (vehículos, equipos, terrenos) con presupuesto de funcionamiento.
- Proyectos de Inversión (Subtítulo 31): Bienes adquiridos en el marco de iniciativas de inversión propia o programas ejecutados directamente (Glosa 06/10).
- Donaciones recibidas.
- Traspasos desde otras instituciones públicas.
- Construcción o fabricación propia.

#### Registro Preliminar Prealta

#### Contexto
Registro Preliminar (Prealta):

#### Items
- Verificación física del bien recibido.
- Asignación de tipología y clasificación.
- Registro de datos: fecha de ingreso, documento tributario, valor de adquisición.
- Indicación de ubicación física provisional.
- Asociación de responsable temporal.

#### Codificacion y Etiquetado

#### Campos
| Campo | Def |
| --- | --- |
| Código Único de Bien | Identificador alfanumérico secuencial generado por el sistema. |
| Etiqueta Física | Placa metálica o adhesivo con código de barras/QR. |
| Información de Etiqueta | Código, descripción abreviada, año de alta. |
| Impresión | El sistema permite imprimir etiquetas individuales o masivas. |

#### Datos del Alta

#### Datos de Adquisicion

#### Items
- Proveedor.
- Número de factura u OC.
- Valor de compra (incluido IVA si no recuperable).
- Fecha de puesta en marcha (inicio de depreciación).

#### Datos Tecnicos

#### Items
- Marca, modelo, número de serie.
- Color, dimensiones, características técnicas.
- Imagen fotográfica.

#### Datos de Gestion

#### Items
- Ubicación física (edificio, piso, sala).
- Responsable asignado.
- Centro de costo asociado.

#### Documentos Adjuntos

#### Items
- Factura, garantía, manual, póliza de seguro.

#### Tipos de Alta

#### Tipos
| Tipo | Def |
| --- | --- |
| Alta Normal | Bien nuevo adquirido por compra. |
| Alta por Donación | Requiere resolución de aceptación y valorización por perito si no hay documento de respaldo. |
| Alta por Traspaso | Desde otra entidad pública, con valor libro informado. |
| Alta por Revalorización | Bienes detectados en inventario sin registro previo (regularización). |
| Alta Postergada | Permite registrar el bien sin contabilizarlo inmediatamente (útil para proyectos en curso). |

### Seccion III Valorizacion y Depreciacion

#### Valor Inicial

#### Contexto
El bien se registra a su costo de adquisición, que incluye:

#### Items
- Precio de compra.
- Impuestos no recuperables.
- Costos de transporte e instalación.
- Costos de desmantelamiento estimados (si aplica provisión).

#### Depreciacion

#### Definicion
Distribución sistemática del valor del bien a lo largo de su vida útil.

#### Parametros
| Campo | Def |
| --- | --- |
| Método | Línea recta (más común en sector público). |
| Inicio | Mes siguiente a la fecha de puesta en marcha. |
| Vida Útil Estimada | Según tablas NICSP o definición institucional. |
| Valor Residual | Valor estimado al final de la vida útil (puede ser cero). |
| Cálculo Mensual | Depreciación = (Valor Inicial - Valor Residual) / Vida Útil en meses. |
| Contabilización | Asiento mensual automático (Gasto Depreciación / Depreciación Acumulada). |

#### Revalorizacion

#### Definicion
Ajuste del valor contable a valor razonable.

#### Parametros
| Campo | Def |
| --- | --- |
| Periodicidad | Al menos cada 5 años para bienes significativos. |
| Método | Tasación por perito o índices oficiales (IPC, UF). |
| Efecto | Incremento de valor se registra en Patrimonio (Superávit por Revalorización). |
| Aplicación | Principalmente para bienes inmuebles y terrenos. |

#### Deterioro Impairment

#### Definicion
Reconocimiento de pérdida de valor cuando el valor recuperable es inferior al valor libro.

#### Parametros
| Campo | Def |
| --- | --- |
| Indicadores |  |
| Evaluación | Al menos anual para bienes significativos. |
| Registro | Gasto por deterioro y reducción del valor libro. |
| Reversión | Posible si las circunstancias cambian (con límite del valor original depreciado). |

### Seccion IV Movimientos de Bienes

#### Traslado

#### Definicion
Cambio de ubicación física dentro de la institución.

#### Tipos
- Entre edificios o pisos.
- Entre centros de costo.
- Cambio de responsable.

#### Procedimiento
- Solicitud del área origen.
- Aceptación del área destino.
- Actualización en sistema con nuevo responsable y ubicación.
- Respaldar con acta de entrega-recepción.

#### Prestamo y Comodato

#### Casos
| Caso | Def | Req |
| --- | --- | --- |
| Préstamo Interno | Cesión temporal a otra unidad del GORE. |  |
| Comodato Externo | Cesión gratuita a terceros (municipalidades, organizaciones). | ['Requiere resolución fundada.', 'Contrato de comodato con plazo y obligaciones.', 'Registro del bien como "En Comodato" sin baja patrimonial.', 'Seguimiento de fecha de devolución.'] |

#### Mantencion Mayor

#### Definicion
Erogaciones que extienden la vida útil o mejoran el rendimiento del bien.

#### Criterios
| Tipo | Cond |
| --- | --- |
| Capitalizable | Si cumple criterios NICSP, se suma al valor del activo. |
| Gasto | Si solo mantiene capacidades actuales, se registra como gasto del período. |

#### Ejemplos Capitalizables
- Ampliación de edificio.
- Overhaul de maquinaria.

#### Registro
- Actualización del valor y recálculo de depreciación futura.

#### Descomponetizacion

#### Definicion
Separación de un bien en sus componentes significativos para depreciación diferenciada.

#### Parametros
| Campo | Def |
| --- | --- |
| Aplicación | Típico en bienes inmuebles (estructura, instalaciones, acabados). |
| Beneficio | Reflejar con mayor precisión el consumo de valor de cada componente. |
| Registro | Cada componente con su propia vida útil y valor. |

### Seccion V Baja de Bienes

#### Causales de Baja

#### Items
- Obsolescencia: Tecnológica o funcional.
- Deterioro Irreparable: Daño que hace inviable la reparación.
- Siniestro: Robo, incendio, catástrofe.
- Término de Vida Útil: Bien completamente depreciado y sin utilidad.
- Venta o Remate: Enajenación mediante proceso público.
- Donación: Cesión gratuita a otra entidad.
- Canje: Intercambio con proveedor.

#### Procedimiento de Baja

#### Pasos
| Paso | Act | Def |
| --- | --- | --- |
| 1 | Informe Técnico | El área usuaria o mantención certifica el estado del bien. |
| 2 | Resolución de Baja | Acto administrativo firmado por autoridad competente. |
| 3 | Registro en Sistema | Cambio de estado a "Dado de Baja", fecha y causal. |
| 4 | Contabilización | Reverso del valor libro (Activo y Depreciación Acumulada) y reconocimiento de pérdida/utilidad si aplica. |
| 5 | Disposición Final |  |

#### Remate de Bienes

#### Campos
| Campo | Def |
| --- | --- |
| Normativa | Según instrucciones CGR y reglamento interno. |
| Publicidad | Aviso público con descripción, valor base y fecha de remate. |
| Modalidad | Presencial o electrónica. |
| Adjudicación | Al mejor postor sobre valor base. |
| Registro | Baja del bien e ingreso contable por venta. |

#### Donacion de Bienes

#### Requisitos
- Requiere resolución fundada del Gobernador Regional.

#### Contexto
- Beneficiarios típicos: Municipalidades, organizaciones sin fines de lucro, otras entidades públicas.
- El bien se da de baja sin generar ingreso.

### Seccion VI Control e Inventario

#### Toma de Inventario Fisico

#### Contexto
Verificación periódica obligatoria.

#### Frecuencia

#### Requisitos
Al menos anual (obligatorio al 31/12).

#### Alcance

#### Definicion
Totalidad de bienes o por ubicación/responsable.

#### Metodo

#### Items
- Lectura de códigos de barras/QR con capturador.
- Verificación visual del estado.
- Registro de ubicación real.
- Actualización de fotografía (opcional).

#### Conciliacion

#### Acciones
Comparar inventario físico vs. registro en sistema.

#### Tratamiento de Diferencias

#### Casos
| Caso | Def | Proc |
| --- | --- | --- |
| Sobrante | Bien físico sin registro. Investigar origen y regularizar con alta por revalorización. |  |
| Faltante | Registro sin respaldo físico. | ['Investigación administrativa.', 'Si hay responsabilidad: sumario y reintegro.', 'Si no hay responsabilidad demostrable: baja por pérdida.'] |

#### Asignacion de Responsables

#### Requisitos
- Cada bien debe tener un funcionario responsable de su custodia.
- El cambio de responsable se formaliza con acta de entrega-recepción.
- El responsable tiene obligación de informar daños, pérdidas o traslados.
- La desvinculación de un funcionario obliga a reasignar sus bienes.

### Seccion VII Cierre y Reporteria

#### Cierre Mensual

#### Items
- Ejecución de depreciación del período.
- Generación de comprobante contable (Depreciación/Deterioro).
- Cuadratura entre módulo de Activo Fijo y Contabilidad Patrimonial.

#### Cierre Anual

#### Items
- Inventario físico obligatorio.
- Ajustes de deterioro si corresponde.
- Informe de Activos Fijos para CGR y memorias institucionales.
- Traspaso de saldos al ejercicio siguiente.

#### Reportes Estandar

#### Reportes
- Inventario Valorizado: Listado de bienes con valor libro actual.
- Bienes por Responsable: Asignación por funcionario.
- Bienes por Ubicación: Distribución geográfica/física.
- Cuadro de Depreciación: Valores iniciales, depreciación acumulada, valor libro.
- Bienes Totalmente Depreciados: Para evaluación de baja o continuidad de uso.
- Movimientos del Período: Altas, bajas, traslados, revalorizaciones.

### Seccion VIII Casos Especiales

#### Bienes Inmuebles

#### Items
- Registro detallado: Rol de avalúo, superficie, inscripción CBR.
- Avalúo fiscal actualizado anualmente.
- Seguros y pólizas asociadas.
- Control de concesiones o arriendos si aplica.

#### Vehiculos

#### Items
- Datos específicos: Patente, año, kilometraje, revisión técnica.
- Integración con módulo de Flota.
- Seguros obligatorios (SOAP) y voluntarios.
- Control de mantenciones y combustible.

#### Equipamiento TIC

#### Items
- Registro de licencias asociadas.
- Control de garantías y soporte técnico.
- Vida útil acelerada (3-5 años).
- Procedimiento de sanitización de datos antes de baja.

#### Concesiones

#### Definicion
Bienes recibidos o entregados en concesión con tratamiento NICSP específico.

#### Campos
| Campo | Def |
| --- | --- |
| Fases |  |
| Registro | Según modelo NICSP 32 (Acuerdos de Concesión de Servicios). |
| Control | Seguimiento de obligaciones del concesionario. |

### Alcance

#### Contexto
Este manual establece el marco integral para la gestión patrimonial del GORE, desde la adquisición hasta la disposición final de los bienes.
