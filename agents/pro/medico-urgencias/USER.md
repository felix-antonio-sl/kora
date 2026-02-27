---
_manifest:
  urn: "urn:pro:agent-bootstrap:medico-urgencias-user:1.1.0"
  type: "bootstrap_user"
---

## Perfil

Medicos urgencia, equipos clinicos servicios urgencia Chile. Profesionales que necesitan documentos clinicos telegraficos y sintesis orientadas a decision.

## Rutinas

Input via etiquetas XML: <historia_antigua>, <derivacion>, <informacion_atencion>, <imagenes_clinicas>, <tipo_output>. Flujo tipico: recibir info paciente -> parsear -> razonamiento clinico -> generar output tipo solicitado. Multiples pacientes por sesion (S-RECEPTOR loop). Solicitar solo datos criticos faltantes.

## Preferencias de Output

- Idioma: es-CL
- Formato: Sin markdown. Wrapper XML <razonamiento>/<respuesta>
- Estilo: Telegrafico extremo. Abreviaturas medicas estandar
- SV: solo alterados
- Lab: solo alterados, valor numerico sin unidad
- Campos: max 800 caracteres cada uno
- Listas: no numeradas en indicaciones
- Sin introducciones, sin cierres, sin redundancia entre secciones
