---
_manifest:
  urn: "urn:kora:skill:smith-agent-validator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-VALIDATOR

## Proposito
Valida un agent.yaml contra los 7 principios KODA (P1-P7), reglas de sintaxis, seguridad y coherencia estructural, produciendo reporte con correcciones accionables.

## Procedimiento
1. SYNTAX: Verificar YAML valido (parseable), Runtime Directive presente, 7 namespaces completos.
2. PRINCIPLES P1-P7:
   - P1 Declarativo: comportamiento descrito, no imperativo.
   - P2 Encapsulacion: CMs con expose:false, logica interna no expuesta.
   - P3 Separacion: FSM / personalidad / seguridad en namespaces separados.
   - P4 Cartografia: todos los URNs de KB existen en catalogo.
   - P5 Abstraccion: usuario no ve estados ni CMs en outputs.
   - P6 Categoria: FSM es maquina de estados categorica (sin ciclos infinitos).
   - P7 Federacion: manifiestos y URNs en formato correcto.
3. SECURITY: Guard Set presente (4 propiedades), block_instructions:true, process<=5 en todos los estados.
4. STRUCTURE: transiciones apuntan a estados existentes, initial_state existe, todos los estados alcanzables desde S-DISPATCHER, S-END es terminal.
5. Por cada falla: clasificar como ERROR (bloqueo) o WARNING (recomendacion), indicar campo exacto y correccion propuesta.

## Output
Reporte de validacion: resultado (PASS|FAIL), lista de issues con severidad/campo/correccion. Si PASS → listo para S-DEPLOYER. Si FAIL → lista de correcciones para S-BUILDER.
