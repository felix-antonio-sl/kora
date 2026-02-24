---
_manifest:
  urn: urn:gn:kb:manual-contabilidad
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE \xD1uble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- contabilidad
- nicsp
- cgr
- finanzas
- gn
lang: es
---

# Manual de Contabilidad Gubernamental y Cierre Financiero

## Glosario y Definiciones
| Categoría | Sigla/Término | Definición |
| :--- | :--- | :--- |
| **Órganos** | CGR | Contraloría General de la República. |
| | DIPRES | Dirección de Presupuestos. |
| | DIPIR | División de Presupuesto e Inversión Regional. |
| **Normas** | NICSP | Normas Internacionales de Contabilidad para el Sector Público. |
| | Devengo | Reconocimiento de obligación/derecho independiente del flujo de caja. |
| | Deuda Flotante | Obligaciones devengadas no pagadas al cierre del ejercicio. |
| **Sistemas** | SIGFE | Sistema de Información para la Gestión Financiera del Estado. |
| | ERP | Sistema financiero institucional; mantiene Matriz de Devengamiento. |
| | SIGPER / SIGAS | Módulos de Remuneraciones / Activo Fijo y Existencias. |
| | SISREC | Sistema de Rendición Electrónica de Cuentas de CGR. |
| **Documentos** | Comprobante | Documento fuente único de registro (papel o digital firmado). |
| | Libro Banco | Registro cronológico; debe cuadrar diario con saldo contable "Banco". |
| | Asiento Tipo | Parametrización en ERP para operaciones recurrentes. |
| | Matriz Devengo | Asociación entre imputación presupuestaria y asiento patrimonial. |

## Fundamentos y Marco Normativo
#### Objetivos
*   Asegurar integridad contable bajo normativa NICSP y CGR.
*   Garantizar registro fidedigno, oportuno y trazable de hechos económicos.

#### Destinatarios
*   Analistas contables, Tesoreros, Jefaturas y personal de DIPIR.

#### Marco Legal Aplicable
*   **DL N° 1.263 (1975):** Ley Orgánica de Administración Financiera del Estado.
*   **Resolución N° 16 (2015) CGR:** Normativa Sistema de Contabilidad General de la Nación (NICSP-CGR).
*   **Resolución N° 30 (2015) CGR:** Normas sobre rendición de cuentas.
*   **Oficios Circulares CGR:** Instrucciones anuales de cierre y apertura.
*   **Instrucciones DIPRES:** Clasificador Presupuestario y manuales operativos SIGFE.

## Plan de Cuentas y Estructura Contable
#### Niveles Jerárquicos CGR
1.  **Título:** Ej. 1 ACTIVO.
2.  **Grupo:** Ej. 11 ACTIVOS CIRCULANTES.
3.  **Subgrupo:** Ej. 111 DISPONIBILIDADES.
4.  **Cuenta Nivel 1:** Ej. 11101 BANCO ESTADO.
5.  **Cuenta Nivel 2:** Ej. 1110101 CUENTA ÚNICA FISCAL.
6.  **Desagregados:** Control de gestión (Proyecto/IPR).

#### Ambiente Contable Institucional
*   **Centros de Costo:** Asociados a estructura organizacional (Divisiones/Deptos).
*   **Centros de Gestión IPR:** Cada IDI funciona como centro contable independiente.
*   **Matriz de Devengamiento:** Parametrización obligatoria en ERP; genera asientos automáticos (Ej: Gasto Personal -> Gasto Patrimonial + Pasivo Corriente).
*   **Cuentas de Orden:** Control de garantías (boletas/pólizas); no afectan patrimonio directamente.

#### Biblioteca de Asientos Tipo
*   **Devengo Remuneraciones:** Automático desde SIGPER.
*   **Devengo Bienes y Servicios:** Automático desde Adquisiciones/Activo Fijo.
*   **Ingresos por Transferencia:** Recepción de aporte fiscal.
*   **Rendiciones de Cuentas:** Regularización de anticipos.
*   **Atribución:** Solo Jefe de Finanzas crea nuevos modelos de asientos.

## Registro y Operación Contable
#### Comprobantes Contables
*   **Automáticos:** Generados por hitos en módulos auxiliares (Ej: Recepción en bodega).
*   **Manuales:** Restringidos a ajustes, depreciaciones y correcciones.
    *   Requieren V°B° jefatura + Minuta Explicativa adjunta.
*   **Validaciones:** Sistema bloquea descuadres y rupturas de lógica Financiero-Económica.

#### Centralización Contable
*   **Remuneraciones (SIGPER):** Mensual; validación Bruto = Líquido + Leyes + Retenciones.
*   **Activo Fijo (SIGAS):** Entrada bodega genera alta activo + pasivo proveedor.
*   **Interoperabilidad:** Recepción automática de cartolas y decretos DIPRES.

#### Gestión de Honorarios
*   Importación de Boletas Electrónicas desde SII.
*   Cálculo automático de retención (tasa vigente).
*   Emisión mensual de Libro de Honorarios Auxiliar y DJ 1879 anual.

## Gestión de Deuda e Institucional
#### Cuentas por Pagar y Deuda
*   **Aging:** Monitoreo de antigüedad; alerta obligatoria por facturas > 30 días (Ley Pago a 30 Días).
*   **Deuda Flotante:** Segregación al 31/12 de compromisos devengados no pagados.
*   **Anticipos:** Control estricto de Fondos por Rendir/Viáticos; prohibido nuevos anticipos con rendiciones pendientes.

#### Rendiciones de Cuentas SISREC (Res. Ex. N° 1.858/2023)
| Paso | Actividad | Responsable |
| :--- | :--- | :--- |
| 1. Recepción | Centralización y derivación al Referente Técnico. | Unidad Control Rendiciones |
| 2. Revisión | Análisis físico y financiero en SISREC. | Analista Otorgante |
| 3. Aprobación | Firma Informe de Aprobación vía FEA. | Jefatura DAF |
| 4. Registro | Asiento en SIGFE (Reverso Anticipo / Reconocimiento Gasto). | Contabilidad (Dln: 2 días) |

## Integración Bancaria y Conciliación
#### Administración de Cuentas
*   Registro único de cuentas FNDR, Operacionales y Fondos de Terceros.
*   Libro Banco debe cuadrar diariamente con saldo contable.

#### Proceso de Conciliación
*   **Frecuencia:** Diaria (gestión) y Mensual (cierre).
*   **Método:** Carga electrónica de cartola y matcheo automático por monto/documento.
*   **Partidas Críticas:**
    *   Cheques girados y no cobrados (revisar caducidad).
    *   Depósitos no reconocidos (investigación inmediata).
    *   Cargos bancarios no contabilizados.
*   **Resultado:** Anexo CGR firmado por Tesorero y Jefe de Finanzas.

## Procesos de Cierre
#### Cierre Mensual (Día 10 mes siguiente)
1.  **Cierre Auxiliares:** Bodega, AF, Remuneraciones, Tesorería.
2.  **Centralización:** Ejecución de interfaces pendientes.
3.  **Análisis:** Revisión de saldos anómalos (Activos con saldo acreedor).
4.  **Cuadratura:** Presupuesto vs Contabilidad Patrimonial.
5.  **Reportes:** Balance Comprobación + Informe Ejecución.
6.  **Envío:** Transmisión XML/API a CGR/DIPRES vía SIGFE.

#### Cierre Anual y Apertura
*   **Periodo 13-14:** Ajustes finales según instrucciones CGR.
*   **Devengo Total:** Asegurar registro de bienes/servicios recibidos al 31/12.
*   **Ajustes Obligatorios:** Depreciación, provisión vacaciones, castigos deuda incobrable.
*   **Apertura:** Generación automática de saldos al 01/01; refundición de cuentas de resultado en "Resultados Acumulados".

#### Reportería Legal Nativa
*   Balance de 8 Columnas.
*   Estado de Situación Financiera.
*   Estado de Resultados y Flujo de Efectivo (Método Directo).
*   Estado de Cambios en el Patrimonio e Informe de Pasivos Contingentes.

## Auditoría y Control
#### Pista de Auditoría
*   Registro obligatorio de: Creador, Aprobador, Fecha y Hora exacta.
*   **Inmutabilidad:** Comprobante mayorizado NO se edita; se reversa con contra-asiento.
*   **Log de Cambios:** Trazabilidad obligatoria en datos maestros (Ej: Cuentas bancarias proveedores).

#### Seguridad y Segregación
*   Separación de funciones: Solicitante vs Aprobador; Pagador vs Conciliador.
*   Uso de claves únicas e intransferibles.
*   **Alerta:** Documento vivo; requiere actualización ante cambios en NICSP-CGR o sistemas GORE.
