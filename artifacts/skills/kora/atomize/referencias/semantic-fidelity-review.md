# Semantic Fidelity Review

La validacion mecanica nunca basta para cerrar una atomizacion. Este protocolo
revisa si las proposiciones siguen diciendo lo mismo que la fuente. Los scripts
solo preparan evidencia; el juicio semantico lo hace el agente o una revision
humana.

## Objetivo

Confirmar que cada proposicion muestreada:

- esta soportada por la fuente
- no inventa interpretacion
- no pierde condiciones, negaciones o cuantificadores
- no fusiona hechos distinguibles

## Que revisar

Para cada muestra, comparar proposicion vs excerpt original y responder:

1. **Soporte**
   - ¿La fuente realmente afirma esto?
   - ¿O la proposicion agrega una conclusion interpretativa no explicitada?

2. **Fidelidad**
   - ¿Se preservaron cifras, cantidades, fechas y nombres propios?
   - ¿Se preservaron negaciones, excepciones y condiciones?
   - ¿Se mantuvo el alcance correcto (`solo`, `si`, `excepto`, `unless`)?

3. **No-colapso**
   - ¿La proposicion junta dos hechos que deberian ir separados?
   - ¿Comprime una lista o una regla compuesta de manera destructiva?

4. **Tipado**
   - ¿El tipo elegido corresponde a lo que la fuente expresa?
   - ¿Una restriccion o una obligacion quedo degradada a `fact`?

## Zonas de mayor riesgo

Prestar atencion extra a:

- definiciones
- restricciones numericas
- deadlines y duraciones
- exclusiones y excepciones
- frases con `if`, `unless`, `except`, `salvo`, `only`
- transiciones de pagina o OCR roto
- proposiciones multi-source
- proposiciones `tension`

## Prioridad de muestreo

El packet de revision debe priorizar, en este orden:

- `tension`
- negaciones y excepciones
- proposiciones multi-source
- restricciones numericas o temporales
- cobertura posicional de inicio / medio / final

Si el bundle contiene `tension`, el muestreo no puede dejar todas las tensiones
fuera del packet.

## Workflow recomendado

1. correr `review_atomic_quality.py`
2. correr `prepare_atomic_fidelity_review.py`
3. revisar el packet de muestras con juicio semantico del agente
4. si alguna muestra falla por no-soporte o perdida de condiciones, rehacer
5. si las muestras pasan, registrar el veredicto en `review_atomic_acceptance.py`

## Regla de rechazo

Una sola muestra que introduzca sentido no soportado o que pierda una
condicion critica alcanza para rechazar la corrida hasta corregirla.
