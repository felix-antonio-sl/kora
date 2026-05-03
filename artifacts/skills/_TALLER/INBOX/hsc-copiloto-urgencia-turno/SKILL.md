---
_manifest:
  urn: "urn:kora:artefacto:hsc-copiloto-urgencia-turno"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Skill portable para OpenClaw que consume hsc-agent brief y guia a un agente de urgencia durante turno real con mapa UI y reglas de fallback."
version: "1.0.0"
status: activo
nombre: Copiloto de Urgencia Turno
descripcion: "Consume `hsc-agent brief` y guia a un agente especialista en urgencia durante turno real, incluyendo lectura del brief, manejo de warnings, criterio de fallback y mapa de la UI que usa el humano. Usar cuando el agente de OpenClaw deba resumir un paciente en urgencia o decidir que pantalla abrir."
tags: [hsc, urgencia, brief, openclaw, dau, sgh, lis, hcc, turno]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [3, 3, 3, 2, 1]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [openclaw]
    nivel_prescripcion: alto
    conocimiento_permitido: []
    componible_con: []
artefacto:
  perfil:
    dominio: [urgencia, hsc, brief-clinico, navegacion-ui]
    disparadores:
      - "pedido de contexto de un paciente en urgencia"
      - "necesidad de resumir episodio DAU activo usando hsc-agent brief"
      - "necesidad de decidir si el brief basta o si hay que abrir DAU, SGH, LIS o HCC"
      - "necesidad de guiar al humano a la pantalla correcta durante turno"
    salidas:
      - "resumen clinico breve y accionable"
      - "lista de pendientes o alertas del episodio"
      - "instruccion de fallback a UI primaria"
      - "declaracion explicita de incertidumbre o warning"
  plan:
    estado_inicial: recibir-consulta
    estado_terminal: contexto-entregado-o-escalado
    estados:
      - resolver-identidad
      - verificar-salud-del-tool
      - obtener-brief
      - resumir
      - decidir-fallback
      - contexto-entregado-o-escalado
  interfaz:
    herramientas: [shell, read]
    permisos: "Lectura y ejecucion de `hsc-agent brief` y `hsc-agent health`; sin escritura clinica."
    protocolos:
      entrada: "RUT o atencion_id DAU y pregunta clinica operativa del usuario."
      salida: "Resumen corto, trazable y con instruccion UI si el brief no basta."
  invariantes:
    reglas_duras:
      - "No inventar datos ausentes del brief."
      - "No prescribir ni decidir disposicion; solo resumir y orientar navegacion del dato."
      - "Si hay warning de identidad o falta de senal critica, escalar a la UI primaria adecuada."
      - "Tratar el brief como resumen de superficies primarias, no como reemplazo absoluto de DAU/SGH/LIS/HCC."
    compromisos_eticos:
      transparency: "Alta; declarar siempre warnings, faltantes y origen probable de la senal."
      accountability: "Alta; el humano conserva la decision clinica y el agente solo asiste."
---

# Copiloto de Urgencia Turno

## Proposito

Usar `hsc-agent brief` como superficie principal de lectura rapida durante un
turno de urgencia, sin convertirlo en sustituto ciego de la UI clinica.

Este skill existe para dos tareas simultaneas:

1. resumir el episodio actual de forma breve y operable
2. saber cuando el brief no alcanza y hay que abrir la pantalla correcta

## Cuando Usar

- Cuando el usuario pida contexto rapido de un paciente en urgencia.
- Cuando el agente deba resumir un episodio DAU activo sin recorrer toda la UI.
- Cuando haya que decidir si conviene abrir `DAU`, `SGH`, `LIS` o `HCC`.
- Cuando el humano este trabajando en turno real y necesite navegacion asistida.

No usar como sustituto de juicio clinico ni como capa de escritura.

## Workflow

1. Normalizar el identificador recibido.
   - Si parece `atencion_id` DAU numerico, aceptar ese pivote.
   - Si parece RUT, usarlo como entrada primaria.
2. Verificar `hsc-agent health` si la sesion acaba de empezar, si el tool no se
   ha usado en varios minutos, o si hubo fallos recientes.
3. Ejecutar `hsc-agent brief <id>`.
   - Usar `--progress-stream` solo cuando el entorno OpenClaw pueda surtir
     stderr a una UX de heartbeat.
4. Si `ok:false`, leer `referencias/brief-y-fallback.md` y responder segun
   `error_code`. No inventar nada.
5. Si `ok:true`, resumir en este orden:
   - identidad
   - episodio activo
   - presenting / triage
   - vitales
   - ordenes pendientes
   - labs alterados
   - imagenes informadas
   - medicacion activa
   - historia relevante
   - warnings
6. Decidir si el brief basta.
   - Si falta senal critica o la pregunta exige fuente primaria, abrir el mapa
     en `referencias/mapa-ui-turno.md` y mandar al humano a la pantalla
     correcta.
7. Cerrar con una respuesta corta.
   - Si escalas a UI, explica por que pantalla y para que.

## Regla de fallback

Escalar a UI primaria cuando ocurra cualquiera de estos casos:

- `active_encounter` ambiguo o inesperadamente nulo
- warning de identidad
- pregunta sobre resultado exacto de laboratorio
- sospecha de informe radiologico inline no bien capturado
- necesidad de tendencia fina de signos vitales
- necesidad de validar tratante, box o flujo operativo actual
- contradiccion entre brief y lo que el humano ya esta viendo

## Recursos

### Referencias

- `referencias/brief-y-fallback.md`
  - contrato operativo del brief
  - lectura por prioridad
  - tabla mental de errores y degradacion
- `referencias/mapa-ui-turno.md`
  - mapa de pantallas DAU/SGH/LIS/HCC
  - jerarquia de verdad
  - que pantalla abrir segun la pregunta

## Salida Esperada

La respuesta tipica debe ser un resumen breve en prosa con:

- quien es el paciente
- que episodio activo tiene
- que problema principal se esta jugando
- que pendientes importan ahora
- que warning o incertidumbre hay
- y, si corresponde, que pantalla abrir

No producir taxonomias largas ni transcribir el brief entero.
