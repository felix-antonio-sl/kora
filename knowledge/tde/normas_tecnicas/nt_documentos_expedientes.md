---
_manifest:
  urn: urn:tde:kb:nt-documentos-expedientes
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- norma-tecnica
- gestion-documental
- expediente-electronico
- ley-21180
- chile
- tde
lang: es
---

# Norma Técnica de Documentos y Expedientes Electrónicos (Decreto 10)

## Objeto y Ámbito
- Establece estándares, formatos, metadatos y procesos para la gestión de documentos y expedientes electrónicos en los Órganos de la Administración del Estado (OAE).
- Aplica a todos los procedimientos administrativos regidos por la Ley 19.880 y la Ley 21.180 (Transformación Digital).


## Definiciones Principales
- **Expediente Electrónico**: unidad documental con identificador único (IUIe), estructurada por índices, documentos, metadatos y registros de trazabilidad.
- **Documento Electrónico**: representación de hechos o ideas creada, comunicada o recibida por medios electrónicos.
- **Comunicación Oficial**: mensaje entre órganos suscrito por autoridad mediante medio electrónico formal que asegure integridad.
- **Preservación Digital**: medidas para mantener el acceso y fidelidad de los documentos en el tiempo (migración de soportes y formatos).
- **Expediente Híbrido**: registro que combina actuaciones en soporte electrónico y papel (referenciado).

## Modelo de Gestión Documental
- Cada OAE debe implementar una **Política de Gestión Documental** (revisión cada 1-3 años) que incluya:

- Estructura institucional de almacenamiento (plataformas y repositorios).
- Roles responsables y gobernanza interna.
- Lineamientos de preservación y resguardo.
- Elementos mínimos: plataforma de expedientes y uno o más repositorios documentales.

## Plataformas y Repositorios
- **Funcionalidad**: deben soportar todas las fases del procedimiento (recepción, creación, procesamiento, disposición final).
- **Estándares**: uso de códigos del Gestor de Códigos del Estado; sincronización horaria con el SHOA (UTC+00:00).
- **Trazabilidad**: registro obligatorio de creación, incorporación, modificación, acceso, transferencia y eliminación.

## Estándares para Documentos Electrónicos
- **Estructura**: compuestos por datos, formatos autorizados y metadatos estandarizados.
- **Metadatos**: vinculación obligatoria con campos definidos en guías técnicas (obligatorios, condicionales y sugeridos).
- **Acceso**: validación mediante Norma de Autenticación para usuarios y Norma de Interoperabilidad para otros órganos.
- **Seguridad**: conservación en entornos que garanticen confidencialidad e integridad (Norma de Seguridad).

## Gestión de Expedientes Electrónicos
- **Creación**: generación automática del IUIe al inicio de todo procedimiento (oficio o parte).
- **Estructura**: debe contener índice electrónico, metadatos, registros de trazabilidad, actos administrativos y notificaciones.
- **Fidelidad**: registro íntegro y sucesivo de todas las actuaciones (Art. 16 bis Ley 19.880).
- **Incorporación**: documentos físicos deben ser digitalizados como microformas (con valor probatorio) según DFL 1/2020.
- **Interoperabilidad**: distinción clara entre datos interoperados y documentos interoperados; requiere registro de origen y servicio usado.

## Condiciones de Funcionamiento
- Habilitar consulta permanente de trazabilidad para interesados.
- Uso de enlaces persistentes para referenciar documentación en repositorios externos.
- Registro de accesos específico para documentos con **datos sensibles** (quién, cuándo y qué).
- Emisión automática de **Certificado de Presentación** electrónico para toda documentación ingresada.

## Disposiciones Finales
- **Actualización**: revisión cada 2 años basada en aprendizajes y dificultades reportadas.
- **Gradualidad**: sujeta al cronograma del DFL 1/2020.
- **Guías Técnicas**: la DGD proveerá detalles operativos sobre formatos, estructuras XML/JSON y perfiles de metadatos.
