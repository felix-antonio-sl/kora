---
_manifest:
  urn: urn:tde:kb:nt-interoperabilidad
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- norma-tecnica
- interoperabilidad
- datos
- red-interoperabilidad
- chile
- tde
lang: es
---

# Norma Técnica de Interoperabilidad (Decreto 12)

## Objeto y Definiciones
- Define estándares y herramientas para que los Órganos de la Administración del Estado (OAE) intercambien datos, documentos y expedientes electrónicos.

- **Interoperar**: operación de intercambio seguro entre dos órganos conectados por nodos.
- **Nodo de Interoperabilidad**: software alojado en el OAE que permite la conexión a la red.
- **Consumidor**: órgano que demanda el servicio.
- **Proveedor**: órgano que entrega la información.
- **Dato Abierto**: información digital usable libremente por cualquier persona.

## Red de Interoperabilidad del Estado
- Conjunto de conexiones directas y seguras a través de internet basadas en nodos.

- **Integración**: obligatoria para todos los OAEs para cumplir los principios de la Ley 19.880.
- **Componentes**: Nodos, Catálogo de Servicios, Registro de Trazabilidad, Directorio de Datos, Catálogo de Esquemas y Gestores de Acuerdos/Autorizaciones.

## Nodo de Interoperabilidad (Requisitos)
- Establecer conexiones cifradas según Norma de Seguridad.
- Validar certificados de autenticación de nodos consumidores.
- Registrar trazabilidad de mensajes en tiempo real (máximo 48h en casos excepcionales).
- Sincronización horaria obligatoria con SHOA (UTC+00:00).
- Usar protocolos autorizados por la Secretaría de Gobierno Digital (SGD).

## Servicios Centralizados
- **Catálogo de Servicios**: lista oficial de servicios de interoperabilidad (datos/docs/expedientes).
- **Directorio de Datos**: descripción y clasificación de datos (personales, sensibles, estadísticos, etc.).
- **Trazabilidad**: almacenamiento de metadatos de cada transacción realizada en la red.
- **Catálogo de Esquemas**: gestión de estructuras XML/JSON aprobadas para el intercambio.

## Gestión de Acuerdos y Autorizaciones
- **Gestor de Acuerdos**: plataforma para negociar términos y condiciones de servicios. Respuesta obligatoria del proveedor en 15 días hábiles. Firma electrónica avanzada requerida.
- **Gestor de Autorizaciones**: sistema para que ciudadanos otorguen consentimiento para el intercambio de sus **datos sensibles**. Consentimiento debe ser libre, informado y revocable (integrado con ClaveÚnica).

## Coordinación y Gobernanza
- **Nivel Institucional**: resolución de problemas operativos liderada por la SGD.
- **Nivel Sectorial**: comités para coordinar estándares y esquemas específicos por industria o área social.
- **Nivel Estratégico**: aprobación de estándares transversales presidida por la SGD.

## Disposiciones Transitorias
- **Migración PISEE**: la Plataforma Integrada de Servicios Electrónicos del Estado (PISEE) dejará de funcionar el **31 de diciembre de 2026**.
- **Plazos de Migración**: Grupo A y B deben migrar a la nueva red en 2025; Grupo C en 2026.
- **Catastro**: OAEs tienen un año para completar su Directorio de Datos institucional.
- **Convenios**: quedan sin efecto acuerdos previos incompatibles con esta norma técnica.
