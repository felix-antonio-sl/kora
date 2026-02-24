---
_manifest:
  urn: urn:gn:kb:manual-activo-fijo
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "GORE \xD1uble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- activo-fijo
- contabilidad
- nicsp
- gn
lang: es
---

# Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo

## Objetivo

- Administración del patrimonio físico institucional mediante el registro, valorización, control y disposición de bienes bajo normativa NICSP.


## Marco Normativo y Clasificación

### Fundamentos Legales
*   **NICSP 17:** Propiedad, Planta y Equipo.
*   **NICSP 21:** Deterioro del Valor de Activos No Generadores de Efectivo.
*   **NICSP 31:** Activos Intangibles.
*   **DL 1.263/1975:** Ley de Administración Financiera del Estado.
*   **Ley 21.180:** Registro electrónico obligatorio del inventario.
*   **Resoluciones CGR:** Normativa sobre control patrimonial, bajas y remates.

### Clasificación de Bienes

| Criterio | Categorías | Ejemplos |
| :--- | :--- | :--- |
| **Naturaleza** | Muebles | Mobiliario, equipos computacionales, maquinaria, vehículos. |
| | Inmuebles | Terrenos, edificios, instalaciones, infraestructura. |
| | Intangibles | Software, licencias, derechos, patentes. |
| **Tratamiento** | Patrimoniales | Registrados en balance (valor ≥ umbral capitalización). |
| | Administrativos | Bienes menores controlados sin capitalización. |
| **Uso** | En Uso | Asignados a funcionarios o unidades. |
| | En Bodega | Disponibles para asignación. |
| | En Comodato | Cedidos temporalmente a terceros. |
| | Dados de Baja | Fuera de servicio, pendientes de disposición. |

### Umbral de Capitalización
*   **Monto:** 3 UTM (típicamente definido por GORE).
*   **Tratamiento < Umbral:** Considerado "gasto", registro en inventario administrativo para control físico.

## Alta de Bienes

### Origen de Ingresos
*   **Subtítulo 29:** Compra directa de activos no financieros (presupuesto funcionamiento).
*   **Subtítulo 31:** Proyectos de inversión (propia o programas Glosa 06/10).
*   **Otros:** Donaciones recibidas, traspasos entre instituciones públicas, construcción propia.

### Proceso de Prealta y Registro
1.  Verificación física del bien.
2.  Asignación de tipología y clasificación.
3.  Registro de fecha, documento tributario y valor de adquisición.
4.  Ubicación física provisional y responsable temporal.

### Codificación y Etiquetado
*   **Código Único:** Identificador alfanumérico secuencial del sistema.
*   **Etiqueta Física:** Placa metálica o adhesivo con código de barras/QR.
*   **Contenido Etiqueta:** Código, descripción abreviada, año de alta.

### Tipos de Alta

| Tipo | Definición / Requisito |
| :--- | :--- |
| **Alta Normal** | Bien nuevo por compra. |
| **Donación** | Requiere resolución de aceptación y valorización (perito si no hay respaldo). |
| **Traspaso** | Desde entidad pública con valor libro informado. |
| **Revalorización** | Regularización de bienes detectados en inventario sin registro. |
| **Postergada** | Registro sin contabilización inmediata (proyectos en curso). |

## Valorización y Depreciación

### Valor Inicial
- Incluye precio de compra, impuestos no recuperables, costos de transporte, instalación y estimación de desmantelamiento (si aplica).


### Parámetros de Depreciación
*   **Método:** Línea recta.
*   **Inicio:** Mes siguiente a la puesta en marcha.
*   **Cálculo:** `(Valor Inicial - Valor Residual) / Vida Útil (meses)`.
*   **Contabilización:** Asiento mensual automático (Gasto Depreciación / Depreciación Acumulada).

#### Vidas Útiles Estimadas
*   **Edificios:** 50-80 años.
*   **Mobiliario:** 10-15 años.
*   **Vehículos:** 7-10 años.
*   **Equipos Computacionales:** 3-5 años.

### Revalorización y Deterioro
*   **Revalorización:** Ajuste a valor razonable (tasación/IPC) al menos cada 5 años (principalmente inmuebles).
*   **Deterioro (Impairment):** Evaluación anual por daño físico u obsolescencia. Registro como gasto si el valor recuperable es inferior al valor libro.

## Movimientos de Bienes

### Traslado Interno
*   Cambio de ubicación, centro de costo o responsable.
*   Requiere solicitud origen, aceptación destino y acta entrega-recepción.

### Préstamo y Comodato
*   **Préstamo Interno:** Cesión temporal entre unidades GORE.
*   **Comodato Externo:** Cesión gratuita a terceros (municipios/ONG). Requiere resolución fundada y contrato con plazo definido.

### Mantención Mayor y Descomponetización
*   **Mantención Mayor:** Capitalizable si extiende vida útil o mejora rendimiento; gasto si es mantenimiento de capacidad actual.
*   **Descomponetización:** Separación de componentes (ej: estructura vs instalaciones en edificios) para depreciación diferenciada por vida útil.

## Baja de Bienes

### Causales
*   Obsolescencia tecnológica/funcional.
*   Deterioro irreparable o siniestro (robo/incendio).
*   Término de vida útil sin utilidad remanente.
*   Venta, remate, donación o canje.

### Procedimiento Administrativo
1.  **Informe Técnico:** Certificación del estado del bien.
2.  **Resolución de Baja:** Acto administrativo de autoridad competente.
3.  **Registro en Sistema:** Estado "Dado de Baja" con fecha y causal.
4.  **Contabilización:** Reverso de valor libro y registro de pérdida/utilidad.
5.  **Disposición Final:** Destrucción certificada, donación o remate público.

## Control e Inventario

### Toma de Inventario Físico
*   **Frecuencia:** Obligatorio anual (al 31/12).
*   **Método:** Capturadores QR/Barras, verificación visual y ubicación real.
*   **Conciliación:** Comparación física vs sistema.

### Tratamiento de Diferencias
*   **Sobrante:** Regularización vía alta por revalorización.
*   **Faltante:** Investigación administrativa. Si hay responsabilidad, sumario y reintegro; de lo contrario, baja por pérdida.

### Responsabilidad de Custodia
*   Asignación obligatoria a un funcionario responsable.
*   Formalización mediante acta de entrega-recepción.
*   Obligación de informar daños, traslados o pérdidas.

## Cierre y Reportería

### Operaciones de Cierre
*   **Mensual:** Ejecución de depreciación y cuadratura con Contabilidad Patrimonial.
*   **Anual:** Inventario obligatorio, ajustes de deterioro y traspaso de saldos.

### Reportes Estándar
*   Inventario valorizado (valor libro actual).
*   Asignación por responsable y ubicación física.
*   Cuadro de depreciación (acumulada y mensual).
*   Bienes totalmente depreciados (para evaluación de baja).
*   Bitácora de movimientos (altas, bajas, traslados).

## Casos Especiales

### Bienes Inmuebles y Vehículos
*   **Inmuebles:** Registro de Rol de avalúo, superficie e inscripción CBR. Requiere avalúo fiscal actualizado y seguros.
*   **Vehículos:** Control de patente, kilometraje y revisión técnica. Integración con gestión de flota y seguros (SOAP/Voluntarios).

### TIC y Concesiones
*   **Equipamiento TIC:** Gestión de licencias y garantías. Vida útil acelerada. Sanitización de datos previa a la baja.
*   **Concesiones (NICSP 32):** Control de fases (construcción/explotación/devolución) y seguimiento de obligaciones del concesionario.
