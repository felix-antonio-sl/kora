---
_manifest:
  urn: urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad-p02
  provenance: https://wikiguias.digital.gob.cl/guias/GU-CIBER-001
version: 1.0.0
status: published
tags:
- tde
- lineamientos-guias
- seguridad-de-la-informacion
- ciberseguridad
- datos
- guia-tecnica
lang: es
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad
---

# Guía Técnica de Seguridad de la Información y Ciberseguridad - Parte 02

## Función de Respuesta

### Planes de respuesta ante incidentes

El plan se activa una vez **confirmado** un incidente. Debe abordar:

1. Notificar a la ANCi y al regulador cuando corresponda
2. Identificar activos, controles, roles y responsabilidades involucrados
3. Evaluar impacto del incidente
4. Determinar si la red fue comprometida (incluidos ataques de día cero y APT)
5. Determinar si datos sensibles fueron comprometidos (riesgo para titulares)
6. Evaluar daño a servidores
7. **Acciones de mitigación:** contener afectaciones y aislar el incidente
8. **Acciones de restablecimiento:**
 - Erradicar el riesgo de acceso del atacante
 - Actualizar parches, blindar infraestructura, cerrar accesos, modificar contraseñas comprometidas
 - Erradicar archivos infectados; reconfigurar o reemplazar hardware si necesario
 - Restaurar nivel de servicio al estado anterior al incidente
 - Verificar exfiltración/pérdida de datos una vez recuperada la integridad, disponibilidad y confidencialidad
9. Canales de comunicación definidos durante mitigación y recuperación
10. Preparar y publicar declaraciones internas y públicas (naturaleza, causas, alcance, pasos, actualizaciones)
11. Preservar evidencias para análisis forense posterior (artefactos, logs, detalles de vulneración)
12. Registro y seguimiento completo del incidente (hora, datos, tipo, descubridor, ubicación, alcance)
13. Informe de respuesta a incidentes
14. Mejora continua a partir de lecciones aprendidas y análisis de causa raíz

### Análisis forense

Posterior al incidente, realizar análisis que:
- Recopile información y evidencia preservando la cadena de custodia
- Resuelva la vulnerabilidad causante
- Actualice procedimientos de respuesta con lecciones aprendidas

---

## Función de Recuperación

Implementar todas las acciones, procesos y procedimientos para restablecer cualquier capacidad, plataforma, sistema, servidor, red o servicio afectado.

### Gestión de incidentes — proceso obligatorio

Etapas mínimas:
1. Usar escala de la Guía de Notificación de Incidentes de ANCi
2. Determinar activos involucrados e impacto sobre servicios
3. Activar planes de respuesta y, si corresponde, plan de continuidad operativa
4. Notificar al CSIRT de Gobierno según la Guía de Notificación de Incidentes

---

## Revisión y actualización

La guía debe revisarse al menos cada año. Se deja registro de todas las versiones.

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | 24/03/2025 | Versión inicial |
