# Precedencia de capas — protocolo de resolucion de tensiones

Cuando dos capas de la SSOT OPM aparentan dar instrucciones distintas para un mismo hecho, esta es la regla de desempate.

## Orden canonico

1. **`urn:fxsl:kb:opm-es`** — capa semantica/ontologica.
2. **`urn:fxsl:kb:opd-es`** ≡ **`urn:fxsl:kb:opl-es`** — realizaciones (visual ≡ textual; nivel par).
3. **`urn:fxsl:kb:manual-metodologico-opm-es`** — capa procedimental.

> Capa mas baja (mas fundamental) gana sobre capa mas alta. La metodologia describe procedimiento, no semantica; nunca contradice a las capas inferiores.

## Tabla de tensiones tipicas

| Tension | Quien manda | Razonamiento |
|---------|-------------|--------------|
| Visual sugiere geometria que la semantica prohibe | `opm-es` | la semantica define las clases; la geometria es realizacion |
| Textual permite formulacion que la semantica niega | `opm-es` | una sentencia OPL valida sintacticamente puede expresar un hecho semanticamente prohibido |
| Visual y textual se contradicen | empate; revisar el hecho del modelo y reformular ambas | la bimodalidad exige equivalencia; si no hay equivalencia, el hecho esta mal capturado |
| Metodologia recomienda algo que rompe semantica | `opm-es` | la metodologia es protocolo, no norma |
| Metodologia recomienda algo que rompe gramatica visual | `opd-es` | igual: protocolo cede a realizacion |
| Metodologia recomienda algo que rompe gramatica textual | `opl-es` | igual |
| OPCloud o herramienta sugiere notacion fuera del corpus | la capa correspondiente | herramientas implementan, no definen |

## Empate entre realizaciones (visual ≡ textual)

Cuando `opd-es` y `opl-es` parecen dar respuestas diferentes para un mismo hecho:

1. **No hay tension real**: la bimodalidad garantiza que toda formulacion valida en una modalidad tiene contraparte valida en la otra.
2. **Si parece haberla**, el hecho subyacente esta mal capturado. Volver al modelo y aclarar: ¿que esta diciendo realmente?
3. Reformular **ambas modalidades juntas** desde el hecho clarificado.

No "elegir una sobre la otra". El sintoma es estructural.

## Cuando consultar al usuario en lugar de decidir

Aun aplicando precedencia, la skill puede tropezar con casos donde:
- la capa apropiada esta ambigua sobre el hecho (laguna de la SSOT).
- el hecho del usuario admite mas de una interpretacion semantica.
- el dominio del usuario impone restricciones externas a OPM.

En esos casos, **declarar el supuesto y consultar antes de modelar**:

> "Estoy interpretando que <Cosa-X> es un proceso (no un objeto) porque la pregunta menciona transformacion. ¿Es correcto?"

> "La SSOT no especifica como modelar <patron-Y>. Voy a usar <interpretacion-Z>; si tienes preferencia distinta, aclaramela."

## Anti-patrones de precedencia

- **"En este caso particular conviene la metodologia sobre la semantica"**: NO. La precedencia es absoluta, no contextual.
- **"OPCloud lo permite, asi que es valido"**: NO. La SSOT manda sobre la herramienta; OPCloud puede ser permisivo en casos que el corpus rechaza.
- **"Como ambas capas tienen la misma severidad, elijo la que prefiera el usuario"**: NO. Visual ≡ textual implica equivalencia, no eleccion.
- **"Si no encuentro una regla, asumo que esta permitido"**: NO. Si la SSOT no especifica, declarar el vacio y consultar; no inventar.

## Como citar capa propietaria en una decision

Cuando la skill aplica una regla, debe citar de donde viene:

- "Por V-13 (`opd-es`), los enlaces procedurales conectan proceso ↔ (objeto | estado), no proceso ↔ proceso. Por eso `Diagnosticar invoca Pedir Examen` se modela con enlace de invocacion, no como agregacion."
- "Por §3.2 de `opm-es`, `agent` es humano u organizacion. La cafetera va como `instrument`."
- "Por plantilla canonica de `opl-es`, la sentencia es `Hacer Cafe consume Agua y Cafe Molido`, no `Hacer Cafe consume Agua, y Cafe Molido tambien`."
- "El manual metodologico §wizard recomienda partir por la funcion. Si tu pregunta empieza por la estructura, voy a derivar la funcion antes."

Citar siempre. Es transparencia y trazabilidad.
