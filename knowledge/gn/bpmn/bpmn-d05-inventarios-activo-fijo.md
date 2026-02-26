---
_manifest:
  urn: urn:gn:kb:bpmn-d05-inventarios-activo-fijo
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bpmn
- inventarios
- activo-fijo
- sigas
- sigfe
- gn
lang: es
---

# BPMN D05: Gestión de Inventarios y Activo Fijo

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-INVENTARIOS-AF |
| Criticidad | Media |
| Dueño | DAF |
| Procesos | 2 (Inventarios/Bodegas, Activo Fijo) |
| Subprocesos | ~10 |
| Sistema | SIGAS |

## Mapa General

**P1 Existencias (Inventarios):** Catálogo materiales → Recepción desde OC → Consumo y despacho → Inventario físico / Control vencimientos.

**P2 Activo Fijo:** Alta de bienes → Valorización y depreciación → Movimientos internos → Baja de bienes / Inventario físico AF.

## P1: Gestión de Inventarios y Bodegas

### Catálogo de Materiales

1. Identificar necesidad de nuevo ítem
2. Verificar si existe código en SIGAS → ¿Existe?
   - Sí → usar código existente
   - No → crear nuevo código: nombre, unidad de medida, categoría, valorización

### Recepción de Bienes desde OC

1. OC aceptada por proveedor → proveedor entrega en bodega
2. Bodeguero verifica cantidad, calidad y guía de despacho → ¿Conforme?
   - No → rechazar/devolver
   - Sí → firmar guía de recepción
3. Ingresar en SIGAS → actualizar stock → notificar a requirente

### Consumo y Despacho

1. Unidad solicita materiales → generar vale de consumo
2. Jefatura autoriza
3. Bodeguero prepara pedido → despachar y firmar vale
4. Actualizar stock en SIGAS → imputar a centro de costo

### Inventario Físico

**Frecuencia:** Mensual o trimestral.

1. Programar inventario → bloquear movimientos en SIGAS
2. Equipo realiza conteo físico → comparar con saldo sistema → ¿Diferencias?
   - No → cerrar inventario
   - Sí → investigar causas → ¿Justificado?
     - Sí → ajustar sistema → cerrar
     - No → responsabilidad administrativa → cerrar

### Control de Vencimientos (FEFO)

1. Ingresar artículo con fecha de vencimiento → SIGAS registra y alerta
2. Despachar primero los próximos a vencer
3. Si próximo a vencer sin uso → evaluar: uso urgente, donación o baja

### Valorización de Existencias

| Método | Descripción | Uso |
| :--- | :--- | :--- |
| PPP | Precio Promedio Ponderado | Default |
| FIFO | First In, First Out | Alternativo |
| FEFO | First Expired, First Out | Perecibles |

## P2: Gestión de Activo Fijo

**Umbral de capitalización:** ≥ 3 UTM y vida útil > 1 año.
**Normativa:** NICSP 17, 21, 31.

### Alta de Bienes

1. Bien adquirido (compra, donación, etc.) → ¿Valor ≥ 3 UTM y vida útil > 1 año?
   - No → gasto del período
   - Sí → activo fijo
2. Asignar N° inventario → plaquetear bien
3. Registrar en SIGAS: código, valor, ubicación, responsable
4. Contabilizar en SIGFE

### Valorización y Depreciación

1. Determinar vida útil y valor residual
2. Calcular depreciación mensual (método línea recta)
3. SIGAS ejecuta depreciación automática
4. Generar asientos SIGFE mensuales
5. Valor libro = Costo − Depreciación Acumulada

### Movimientos Internos

1. Solicitud de traslado → jefatura origen autoriza
2. Actualizar ubicación y responsable en SIGAS
3. Bien se traslada físicamente → jefatura destino confirma recepción

### Baja de Bienes

| Causal | Documentación requerida |
| :--- | :--- |
| Deterioro irreparable | Informe técnico |
| Obsolescencia | Informe funcional |
| Pérdida/Hurto | Denuncia + Sumario |
| Donación | Autorización Gobernador/a |

Flujo: documentación causal → Resolución de baja → dar de baja en SIGAS → contabilizar en SIGFE → destino físico (destrucción, remate o donación).

### Inventario Físico Activo Fijo

**Frecuencia:** Anual.

1. Corte de sistema y reportes
2. Equipos verifican existencia física → escanear plaquetas o verificar N°
3. Comparar con registro SIGAS → ¿Diferencias?
   - Sí → investigar y regularizar → cerrar
   - No → cerrar inventario

## Casos Especiales

### Bienes de Proyectos FNDR

1. Proyecto FNDR entrega bienes
2. Transferencia a entidad receptora
3. GORE registra como ANF hasta traspasar
4. Resolución de transferencia
5. Receptor da de alta en su patrimonio

### Comodatos y Préstamos

| Tipo | Descripción |
| :--- | :--- |
| Comodato recibido | Bien de tercero en custodia GORE |
| Comodato entregado | Bien GORE en custodia de tercero |

Ambos requieren convenio y registro en control paralelo.

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-SIGAS | Gestión de inventarios y activo fijo |
| SYS-SIGFE | Contabilización |
| SYS-SIGFIN | Integración financiera |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| NICSP 17 | Propiedad, planta y equipo |
| NICSP 21 | Deterioro activos no generadores |
| NICSP 31 | Activos intangibles |
| Resoluciones CGR | Procedimientos de baja |
| Ley 18.575 | Responsabilidad patrimonial |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D04 Compras | Recepción desde OC |
| D02 Ciclo Presupuestario | Contabilización activo fijo |
