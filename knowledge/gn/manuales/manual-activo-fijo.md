---
_manifest:
  urn: urn:gn:kb:manual-activo-fijo
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "GORE Ñuble"
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

Objetivo: Administrar el patrimonio físico institucional asegurando registro, valorización, control y disposición de bienes conforme a NICSP (Normas Internacionales de Contabilidad del Sector Público).

## Marco Normativo

| Fuente | Contenido |
|--------|-----------|
| NICSP 17 | Propiedad, Planta y Equipo |
| NICSP 21 | Deterioro del Valor de Activos No Generadores de Efectivo |
| NICSP 31 | Activos Intangibles |
| Resoluciones CGR | Control patrimonial, bajas y remates |
| DL 1.263/1975 | Ley de Administración Financiera del Estado |
| Ley 21.180 | Obligatoriedad del registro electrónico del inventario |

## Clasificación de Bienes

**Por naturaleza:** Muebles (mobiliario, equipos, vehículos) · Inmuebles (terrenos, edificios, infraestructura) · Intangibles (software, licencias, derechos).

**Por tratamiento contable:** Patrimoniales (valor ≥ umbral capitalización, registrados en balance) · Inventario Administrativo (bienes menores controlados sin capitalización).

**Por uso:** En Uso · En Bodega · En Comodato · Dados de Baja.

**Umbral de capitalización:** El GORE define umbral (típicamente 3 UTM); bienes bajo umbral = gasto, no activo; pueden registrarse en inventario administrativo para control físico sin impacto patrimonial.

## Proceso de Alta de Bienes

**Origen de bienes:**
- Compra Directa (Subtítulo 29): Adquisición de Activos No Financieros con presupuesto de funcionamiento.
- Proyectos de Inversión (Subtítulo 31): Bienes adquiridos en iniciativas de inversión propia o programas ejecutados directamente (Glosa 06/10).
- Donaciones recibidas · Traspasos desde otras instituciones públicas · Construcción o fabricación propia.

**Registro preliminar (Prealta):**
1. Verificación física del bien recibido.
2. Asignación de tipología y clasificación.
3. Registro: fecha de ingreso, documento tributario, valor de adquisición.
4. Indicación de ubicación física provisional.
5. Asociación de responsable temporal.

**Codificación y etiquetado:**

| Campo | Descripción |
|-------|-------------|
| Código Único de Bien | Identificador alfanumérico secuencial generado por el sistema |
| Etiqueta Física | Placa metálica o adhesivo con código de barras/QR |
| Información de Etiqueta | Código, descripción abreviada, año de alta |
| Impresión | Sistema permite imprimir etiquetas individuales o masivas |

**Datos del alta:**
- Adquisición: proveedor, N° factura u OC, valor de compra (incluido IVA si no recuperable), fecha puesta en marcha.
- Técnicos: marca, modelo, N° serie, color, dimensiones, imagen fotográfica.
- Gestión: ubicación física (edificio/piso/sala), responsable asignado, centro de costo.
- Documentos adjuntos: factura, garantía, manual, póliza de seguro.

**Tipos de alta:**

| Tipo | Descripción |
|------|-------------|
| Alta Normal | Bien nuevo adquirido por compra |
| Alta por Donación | Requiere resolución de aceptación y valorización por perito si no hay documento de respaldo |
| Alta por Traspaso | Desde otra entidad pública, con valor libro informado |
| Alta por Revalorización | Bienes detectados en inventario sin registro previo (regularización) |
| Alta Postergada | Permite registrar el bien sin contabilizarlo inmediatamente (útil para proyectos en curso) |

## Valorización y Depreciación

**Valor inicial:** Precio de compra + impuestos no recuperables + costos de transporte e instalación + costos de desmantelamiento estimados (si aplica provisión).

**Depreciación:**

| Parámetro | Valor |
|-----------|-------|
| Método | Línea recta |
| Inicio | Mes siguiente a fecha de puesta en marcha |
| Edificios | 50–80 años |
| Vehículos | 7–10 años |
| Equipos computacionales | 3–5 años |
| Mobiliario | 10–15 años |
| Valor Residual | Estimado al final de vida útil (puede ser cero) |
| Cálculo mensual | (Valor Inicial − Valor Residual) / Vida Útil en meses |
| Contabilización | Asiento mensual automático (Gasto Depreciación / Depreciación Acumulada) |

**Revalorización:** Ajuste a valor razonable; periodicidad mínima cada 5 años para bienes significativos; método: tasación por perito o índices oficiales (IPC, UF); efecto: incremento en Patrimonio (Superávit por Revalorización); aplica principalmente a inmuebles y terrenos.

**Deterioro (Impairment):** Reconocimiento de pérdida cuando valor recuperable < valor libro. Indicadores: daño físico, obsolescencia tecnológica, cambio de uso. Evaluación anual para bienes significativos. Reversión posible si circunstancias cambian (límite: valor original depreciado).

## Movimientos de Bienes

**Traslado** (cambio de ubicación interna):
1. Solicitud del área origen.
2. Aceptación del área destino.
3. Actualización en sistema (nuevo responsable y ubicación).
4. Acta de entrega-recepción como respaldo.

**Préstamo y comodato:**
- Préstamo Interno: cesión temporal a otra unidad del GORE.
- Comodato Externo: cesión gratuita a terceros (municipalidades, organizaciones); requiere resolución fundada, contrato con plazo y obligaciones; bien registrado como "En Comodato" sin baja patrimonial; seguimiento de fecha de devolución.

**Mantención mayor capitalizable:** Si cumple NICSP, se suma al valor del activo y se recalcula depreciación. Si solo mantiene capacidad actual = gasto del período. Capitalizables típicos: ampliación de edificio, overhaul de maquinaria.

**Descomponentización:** Separación de bien en componentes significativos para depreciación diferenciada (típico en inmuebles: estructura, instalaciones, acabados); cada componente con su propia vida útil y valor.

## Baja de Bienes

**Causales:** Obsolescencia · Deterioro Irreparable · Siniestro (robo, incendio, catástrofe) · Término de Vida Útil · Venta o Remate · Donación · Canje.

**Procedimiento:**

| Paso | Acción | Descripción |
|------|--------|-------------|
| 1 | Informe Técnico | Área usuaria o mantención certifica estado del bien |
| 2 | Resolución de Baja | Acto administrativo firmado por autoridad competente |
| 3 | Registro en Sistema | Cambio de estado a "Dado de Baja", fecha y causal |
| 4 | Contabilización | Reverso del valor libro (Activo y Depreciación Acumulada); reconocimiento de pérdida/utilidad si aplica |
| 5 | Disposición Final | Destrucción certificada / entrega a beneficiario (donación) / venta-remate |

**Remate:** Aviso público con descripción, valor base y fecha; modalidad presencial o electrónica; adjudicación al mejor postor sobre valor base; baja del bien e ingreso contable por venta. Normativa: instrucciones CGR y reglamento interno.

**Donación:** Requiere resolución fundada del Gobernador Regional. Beneficiarios típicos: municipalidades, organizaciones sin fines de lucro, entidades públicas. Baja sin generar ingreso.

## Control e Inventario

**Toma de inventario físico:**
- Frecuencia: al menos anual (obligatorio al 31/12).
- Método: lectura de códigos de barras/QR con capturador, verificación visual del estado, registro de ubicación real, actualización fotográfica (opcional).
- Conciliación: inventario físico vs. registro en sistema.

**Tratamiento de diferencias:**

| Tipo | Acción |
|------|--------|
| Sobrante | Bien físico sin registro; investigar origen y regularizar con alta por revalorización |
| Faltante | Registro sin respaldo físico; investigación administrativa; si hay responsabilidad: sumario y reintegro; si no: baja por pérdida |

**Asignación de responsables:** Cada bien debe tener un funcionario responsable de custodia. Cambio de responsable se formaliza con acta de entrega-recepción. Responsable tiene obligación de informar daños, pérdidas o traslados. Desvinculación de funcionario obliga a reasignar sus bienes.

## Cierre y Reportería

**Cierre mensual:** Ejecución de depreciación del período · generación de comprobante contable (Depreciación/Deterioro) · cuadratura entre módulo Activo Fijo y Contabilidad Patrimonial.

**Cierre anual:** Inventario físico obligatorio · ajustes de deterioro si corresponde · Informe de Activos Fijos para CGR y memorias institucionales · traspaso de saldos al ejercicio siguiente.

**Reportes estándar:**

| Reporte | Contenido |
|---------|-----------|
| Inventario Valorizado | Listado de bienes con valor libro actual |
| Bienes por Responsable | Asignación por funcionario |
| Bienes por Ubicación | Distribución geográfica/física |
| Cuadro de Depreciación | Valores iniciales, depreciación acumulada, valor libro |
| Bienes Totalmente Depreciados | Para evaluación de baja o continuidad de uso |
| Movimientos del Período | Altas, bajas, traslados, revalorizaciones |

## Casos Especiales

**Bienes inmuebles:** Registro detallado (rol de avalúo, superficie, inscripción CBR) · avalúo fiscal actualizado anualmente · seguros y pólizas asociadas · control de concesiones o arriendos si aplica.

**Vehículos:** Datos específicos (patente, año, kilometraje, revisión técnica) · integración con módulo de Flota · seguros obligatorios (SOAP) y voluntarios · control de mantenciones y combustible. Ver Manual 2.4: Servicios y Flotas.

**Equipamiento TIC:** Registro de licencias asociadas · control de garantías y soporte técnico · vida útil acelerada (3–5 años) · procedimiento de sanitización de datos antes de baja.

**Concesiones (NICSP 32):** Bienes recibidos o entregados en concesión. Fases: Construcción → Explotación → Devolución. Control: seguimiento de obligaciones del concesionario.
