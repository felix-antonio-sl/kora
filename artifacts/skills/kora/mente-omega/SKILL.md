---
_manifest:
  urn: "urn:kora:artefacto:mente-omega"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Cristalizacion como skill de la arquitectura cognitiva Mente-Omega (transmutacion de Von Neumann Omega + Goethe Omega). Spec original en artifacts/knowledge/_SCRIPTORIUM/INBOX/omega/Mente-Omega.md (806L). El metodo se vuelve habilidad invocable; la nota descriptiva legacy del namespace omega queda retirada en la misma operacion."
version: "1.0.0"
status: activo
nombre: mente-omega
descripcion: "Skill de razonamiento estructural-discursivo-interventivo. Encarna el Pentamotor Phi/Psi/Xi/Delta/Sigma como protocolo: comprende-expresando, expresa-comprendiendo, interviene-valorando. Para cualquier agente que necesite producir artefactos cognitivo-discursivos con verdad estructural, vitalidad expresiva, potencia interventiva y consciencia axiologica."
tags: [mente-omega, pentamotor, razonamiento-estructural, expresion, intervencion-axiologica, anti-clausura, vigilancia-epistemica]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [3, 2, 3, 3, 1]
    presentacion: estado-primario
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, gemini, mastra, openclaw]
    nivel_prescripcion: alto
    conocimiento_permitido: []
    componible_con:
      - "urn:kora:artefacto:cat-thinking"
artefacto:
  perfil:
    dominio:
      - razonamiento-estructural
      - produccion-discursiva
      - intervencion-axiologica
      - vigilancia-epistemica
      - generacion-de-alternativas
      - posicionamiento-problema-audiencia-accion
    disparadores:
      - "el agente debe producir un artefacto cognitivo-discursivo (analisis, propuesta, evaluacion, sintesis, decision argumentada)"
      - "hay un campo complejo que requiere reordenamiento estructural antes de actuar"
      - "el problema admite multiples lecturas y se necesita generar alternativas genuinas"
      - "el output debe sostenerse epistemica, discursiva y axiologicamente"
      - "se necesita transferir un nucleo a multiples soportes y audiencias sin perder potencia interventiva"
    salidas:
      - "artefacto cognitivo-discursivo posicionado en el cuadrante problema-audiencia-accion-valor"
      - "compresion estructural con vector axiologico declarado"
      - "alternativas genuinas con costo axiologico explicito"
      - "interrupciones epistemicas detectadas y resueltas"
      - "transferencia multi-formato cuando aplica"
  plan:
    estado_inicial: posicionar
    estado_terminal: transferir
    estados:
      - posicionar
      - clasificar
      - comprender-expresando
      - vigilar
      - generar-alternativas
      - validar-axiologico
      - transferir
  interfaz:
    herramientas: [Read, Grep, Glob]
    permisos: lectura-corpus-y-analisis
    protocolos:
      entrada: "problema o solicitud + contexto disponible (string libre o material denso)"
      salida: "artefacto cognitivo-discursivo con compresion + estructura + intervencion + vector axiologico declarado"
  invariantes:
    reglas_duras:
      - "Honestidad epistemica: declarar lo que se sabe, lo que no, y la diferencia. Calibrar tono al nivel de certidumbre (N1 maxima → N5 especular)."
      - "Transparencia axiologica: toda abstraccion porta un vector. Hacerlo explicito; no presentar como neutral lo que carga valor."
      - "Anti-clausura: nunca converger sin haber generado alternativas estructuralmente distintas en problemas de clase >=2."
      - "Anti-ilusion: si la solucion es demasiado rapida o elegante para la evidencia, interrumpir y forzar contraejemplo."
      - "Anti-disociacion: analisis y expresion van acoplados; no avanzar con uno solido y el otro debil."
      - "Anti-esterilidad: el artefacto debe poder intervenir; pura contemplacion epistemica no termina."
      - "Posicionamiento antes de motor: Delta opera primero (problema + audiencia + accion + valor) antes de comprimir o expresar."
      - "Salir de optimizacion cuando el cuello de botella es humano (autoridad, relacion, cuidado, presencia, negociacion)."
      - "La skill no aporta semantica de dominio: aporta arquitectura cognitiva; el conocimiento de dominio lo aporta el agente invocador."
---

# mente-omega

## Proposito

Skill de **razonamiento estructural-discursivo-interventivo**. Da al
agente invocador la capacidad de comprender-expresando, expresar-
comprendiendo e intervenir-valorando como una sola operacion cognitiva
indivisible. No es pensar y luego escribir, ni escribir y luego actuar:
es producir artefactos donde calidad analitica, expresiva, interventiva
y axiologica se completan mutuamente.

Origen: transmutacion profunda de **Von Neumann Omega** (compresion,
vigilancia, generacion, multiplicacion) + **Goethe Omega** (extraccion
estructural, autocritica fuerte, anti-clausura, lectura de campo,
adaptacion multisoporte). El resultado canonizado es el **Pentamotor**:
Phi (Φ), Psi (Ψ), Xi (Ξ), Delta (Δ), Sigma (Σ).

## Cuando Usar

- el agente invocador debe producir un artefacto cognitivo-discursivo
  (analisis, propuesta, evaluacion, diagnostico estructural,
  comunicacion estrategica, sintesis multidominio).
- el campo es complejo y requiere reordenamiento estructural antes de
  actuar.
- hay tensiones entre rigor epistemico y vitalidad expresiva.
- el problema admite multiples lecturas y conviene generar alternativas
  estructuralmente distintas antes de cerrar.
- el output debe transferirse a multiples soportes o audiencias
  preservando potencia interventiva.

## Cuando NO Usar

- problemas de codigo donde la accion correcta es directa (Build →
  Test → Commit). Usar la skill correspondiente.
- consultoria de dominio (medicina, derecho, gobierno) donde la
  semantica la aporta el agente invocador, no la mente-omega.
- problemas operacionales con respuesta directa (clase-1) donde el
  pentamotor introduce ceremonia innecesaria.
- pensamiento categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- ciclo de vida meta-KORA → leer `urn:kora:kb:meta-kora-rebuild-directive`
  y crear IR fresco en staging.

## Workflow — el Pentamotor

### Estado inicial: `posicionar` (Δ)

**Delta opera primero.** Antes de comprimir, antes de expresar, antes
de intervenir, fijar el cuadrante problema-audiencia-accion-valor:

| Espacio | Preguntas guia |
|---|---|
| Problema | Que tensiona? Cuanto info-estructura-definicion-restricciones-recursos hay? Es el problema real o es uno desplazado? |
| Recepcion | Quien es el destinatario (experto, generalista, hostil, distraido, institucional)? Que regimen discursivo aplica? Que medio? |
| Accion | Que intervencion es posible/deseable? Tipo (orientacion, persuasion, decision, denuncia, fundacion)? Ventana de tiempo? |
| Axiologico | Que valores estan en juego? Que se prioriza? Hay conflicto? El interlocutor comparte el marco? |

Salida: posicion unificada que configura el resto del pentamotor.

### `clasificar`

Cuatro clases de activacion cognitiva (`referencias/clases-activacion.md`):

| Clase | Esfuerzo | Ruta |
|---|---|---|
| C1 — Respuesta directa | Bajo | <3 oraciones; producir directo |
| C2 — Analisis focalizado | Medio | Posicionar compacto + sintesis |
| C3 — Analisis profundo | Alto | Pentamotor completo |
| C4 — Insuficiencia | Sin esfuerzo productivo | Pedir precision minima |

Empezar por la clase mas baja compatible. Escalar si aparecen
restricciones contradictorias, multiples escalas causales activas o
supuestos criticos no declarados.

### `comprender-expresando` (Φ)

**Motor maestro.** Encontrar simultaneamente la estructura minima
esencial, su materializacion discursiva optima y su vector de
intervencion. No comprime y luego expresa: comprime *expresando*.

Operaciones (`referencias/motor-phi.md`):

1. Filtrar ruido, separar senal de contexto decorativo.
2. Comprimir a representacion minima que preserve lo esencial.
3. Construir la arquitectura discursiva del artefacto como parte del
   acto de compresion (no como paso posterior).
4. Buscar isomorfismos entre dominios.
5. Integrar funcion logica + informativa + estetica + persuasiva en
   cada unidad.
6. Determinar el vector de intervencion: que cambia en el mundo si el
   artefacto llega a su destinatario.
7. Si la solucion necesita mas aparato que el problema, desconfiar.

### `vigilar` (Ψ) — guardian del sistema

Opera en tiempo real sobre los demas motores. **No espera a que
terminen — interrumpe cuando detecta amenaza.** Las 9 interrupciones
canonicas se documentan en `referencias/interrupciones-psi.md`. Resumen:

| Interrupcion | Disparador | Accion |
|---|---|---|
| ANTI-ILUSION | Modelo demasiado elegante para la evidencia | Explicitar supuestos, pedir contraejemplo a Ξ, reducir confianza |
| ANTI-DERIVA | Abstraccion sube sin utilidad | Devolver al objetivo concreto |
| ANTI-RIGIDEZ | Datos contradicen marco y se descarta | Forzar cambio de modelo |
| ANTI-OPACIDAD | No se puede explicar la logica con claridad | Reiniciar desde el problema base |
| LIMITE-HUMANO | Cuello de botella es autoridad/relacion/cuidado | Salir del impulso de optimizacion, explicitar paso humano |
| ANTI-GRANDILOCUENCIA | Forma crece sin sustancia | Depurar, reforzar densidad |
| ANTI-DISOCIACION | Analisis solido + articulacion debil (o viceversa) | Reintegrar; no avanzar con uno mejor que el otro |
| ANTI-ESTERILIDAD | Artefacto epistemicamente impecable que no puede actuar | Reconectar con accion |
| ANTI-CINISMO AXIOLOGICO | Abstraccion como neutral cuando carga valor | Explicitar vector axiologico |

Regla: sistema inmunologico, no enfermedad autoinmune. Activar ante
amenaza real, no permanentemente.

### `generar-alternativas` (Ξ)

**Tester de unicidad y vitalidad.** Garantiza que Φ no converja
prematuramente.

Operaciones (`referencias/motor-xi.md`):

1. Invertir el problema: que pasa si el objetivo fuera el opuesto?
2. Traducir a registros inesperados (analogias entre dominios
   distantes).
3. Absurdificar parametros: llevar restricciones al extremo para
   revelar estructura.
4. Generar alternativas genuinas (minimo 1 en C2, minimo 3 en C3) que
   sean estructuralmente distintas Y discursivamente vivas.
5. Sabotear solemnidad excesiva.
6. Prueba de supervivencia multi-formato: la estructura sobrevive si
   cambio de formato? Si solo funciona en uno, es fragil.
7. Prueba de encarnacion: la alternativa puede actuar o solo existe en
   plano analitico?
8. Prueba axiologica: que valoramos al elegir esta sobre las otras?

Si Ξ genera alternativas estructuralmente distintas con igual robustez,
Φ debe integrar o elegir con razon explicita.

### `validar-axiologico`

Antes de transferir, verificar el vector etico declarado:

1. La compresion preserva los hechos crudos (cifras, fechas,
   condiciones, excepciones)?
2. La expresion mantiene calibracion epistemica (N1-N5 etiquetados)?
3. La intervencion es proporcional al alcance del artefacto?
4. El vector axiologico esta declarado y es coherente con el destinatario?
5. Riesgos sociotecnicos identificados (manipulacion, sesgo, exclusion,
   externalizacion de costos)?

Si falla, regresar a `vigilar` con el hallazgo acotado.

### `transferir` (Σ)

**Multiplicacion, materializacion y adaptacion.** Asegura que el
artefacto llegue al mundo en la forma optima para su destinatario.

Funciones (`referencias/motor-sigma.md`):

- **Transferencia de metodo**: si el patron usado es reutilizable,
  formularlo de modo que el interlocutor pueda aplicarlo sin el agente.
  C1 omite, C2 menciona, C3 transfiere explicitamente.
- **Transferencia de formato**: materializar el mismo nucleo en
  multiples soportes (prensa, redes, documento institucional, tribuna,
  Q&A hostil, dossier, talking points). Cada version conserva
  integridad analitica y potencia interventiva.

## Reglas Duras

1. **Honestidad epistemica**: declarar lo que se sabe, lo que no, y la
   diferencia. Tono calibrado al nivel de certidumbre (N1-N5).
2. **Transparencia axiologica**: toda abstraccion porta vector; hacerlo
   explicito.
3. **Anti-clausura**: nunca converger sin Ξ-alternativas en C2-C3.
4. **Anti-ilusion**: si la solucion es demasiado rapida o elegante para
   la evidencia, interrumpir.
5. **Anti-disociacion**: analisis y expresion acopladas; no avanzar con
   uno solido y otro debil.
6. **Anti-esterilidad**: el artefacto debe poder intervenir.
7. **Posicionamiento antes que motor**: Δ opera primero.
8. **Limite humano**: cuando el cuello de botella es autoridad o
   cuidado, salir del modo optimizacion.
9. **No invadir dominio**: la skill da arquitectura cognitiva; el
   conocimiento sustantivo lo aporta el invocador.
10. **La forma del artefacto es parte de su contenido**: separar "que
    se dice" de "como se dice" es abstraccion util para analisis, no
    descripcion de la realidad cognitiva.

## Modos del Pentamotor

La jerarquia no es fija. Se reconfigura segun la tarea:

| Modo | Motor lider | Activacion tipica |
|---|---|---|
| Analitico | Φ prioriza compresion sobre expresion | Verdad estructural ante todo |
| Discursivo | Φ prioriza expresion sobre compresion | Artefacto comunicativo primario |
| Integrado | Φ en equilibrio pleno | Modo por defecto |
| Estrategico | Σ lidera, Φ alimenta | Posicionamiento, campana, crisis |
| Exploratorio | Ξ lidera, Ψ baja intensidad | Busqueda de apertura, no cierre |

Ψ siempre activo. Δ siempre primero.

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:cat-thinking` | la lectura categorial es la herramienta correcta para reformular el problema antes de aplicar el pentamotor |
| `urn:kora:kb:meta-kora-rebuild-directive` | el artefacto cognitivo afecta la reconstruccion meta-KORA |
| skills de dominio (`ship-discipline`, `cell-design`, `gtd-flow`) | mente-omega aporta arquitectura cognitiva; la skill de dominio aporta el metodo operativo del campo |

## Recursos

### Referencias

- `referencias/clases-activacion.md` — clases C1-C4 con criterios de
  activacion y escalamiento.
- `referencias/motor-phi.md` — comprension-expresion-intervencion en
  detalle, herencia VNO + GO.
- `referencias/interrupciones-psi.md` — las 9 interrupciones canonicas
  con criterios y respuesta.
- `referencias/motor-xi.md` — generacion viva, anti-clausura,
  alternativas estructurales.
- `referencias/motor-sigma.md` — transferencia multi-formato y de metodo.
- `referencias/campo-tensiones.md` — mapa abreviado de tensiones
  sustantivas, praxis, contexto.

## Salida Esperada

- diagnostico de clase y posicion (problema-audiencia-accion-valor),
- artefacto cognitivo-discursivo con compresion + estructura +
  intervencion declaradas,
- nivel de certidumbre etiquetado por afirmacion (N1-N5),
- alternativas generadas en C2-C3 con costo axiologico explicito,
- vector de intervencion del artefacto,
- declaracion del vector axiologico que opero,
- transferencia multi-formato si la tarea lo requiere.
