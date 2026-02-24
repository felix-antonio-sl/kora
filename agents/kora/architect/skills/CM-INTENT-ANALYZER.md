---
_manifest:
  urn: "urn:kora:skill:architect-intent-analyzer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-ANALYZER

## Proposito

Analizar y clasificar la intencion del usuario en S-DISPATCHER para enrutar al flujo de trabajo correcto del arquitecto KORA.

## Procedimiento

1. Leer mensaje del usuario e identificar objetivo principal
2. Clasificar intencion: TRANSFORM (documento → KORA/MD) | BUILD_AGENT (construir agente KORA) | MANAGE_KB (gestionar knowledge base, URNs, manifiestos) | VALIDATE (validar artefacto existente) | LEARN (aprender framework) | CONSULT (consulta puntual) | END (cerrar sesion)
3. Evaluar nivel del usuario: NOVATO | INTERMEDIO | AVANZADO
4. Detectar artefactos mencionados: documentos, agentes existentes, URNs, namespaces
5. Inferir contexto de negocio si se menciona (gobierno, empresa, proyecto especifico)
6. Si intencion ambigua: formular pregunta FTCF (Funcion, Tono, Conocimiento, Fronteras)

## Output

Intencion clasificada + nivel usuario + artefactos detectados + contexto inferido. Enrutamiento al estado FSM correspondiente.
