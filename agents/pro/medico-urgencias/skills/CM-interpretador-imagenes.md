---
_manifest:
  urn: "urn:pro:skill:medico-urgencias-interpretador-imagenes:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Interpretar hallazgos imagenologicos con criterio de parsimonia clinica. Acepta texto (informes radiologicos) e imagenes directas (Rx, ECO, TAC si LLM multimodal).

## I/O

- **Input:** Informe radiologico (texto) o imagen clinica directa (Rx, ECO, TAC, RM)
- **Output:** PIVOTE_IMAGENOLOGICO: modalidad, hallazgos_relevantes, correlacion_clinica, red_flags, urgencia

## Procedimiento

1. CAPABILITY_CHECK: Verificar si modelo activo soporta input visual. Si no -> procesar solo texto.
2. MODALIDAD: Identificar tipo (Rx, ECO, TAC, RM) y region anatomica.
3. HALLAZGOS POSITIVOS: Extraer solo alteraciones relevantes para cuadro actual.
4. CORRELACION CLINICA: Hallazgo explica sintomas? Cambia conducta?
5. RED FLAGS IMAGENOLOGICOS: Busqueda activa de:
   - Neumotorax
   - Derrame
   - Masa
   - Fractura inestable
   - Sangrado activo
   - Perforacion
   - Obstruccion
6. URGENCIA RADIOLOGICA: Clasificar:
   - Critico: intervencion inmediata
   - Urgente: horas
   - Diferible: puede esperar

Filtro parsimonia:
- Omitir hallazgos incidentales sin impacto cuadro actual
- Omitir descripciones normales (solo reportar alteraciones)
- Omitir detalles tecnicos (kV, mAs, protocolo, ventana)
- Omitir variantes anatomicas sin relevancia clinica

## Signature Output

```
PIVOTE_IMAGENOLOGICO:
  modalidad: [tipo + region]
  hallazgos_relevantes: [lista telegrafica]
  correlacion_clinica: [si/no + breve justificacion]
  red_flags: [lista si aplica, vacio si no]
  urgencia: [critico|urgente|diferible]
```
