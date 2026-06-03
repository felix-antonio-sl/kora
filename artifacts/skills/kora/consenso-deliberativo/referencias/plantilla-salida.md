# Plantilla de salida del documento de deliberacion

Estructura obligatoria del entregable de `entregar`. Las ocho secciones son
fijas; su extension se escala al problema.

```markdown
# Deliberacion: <titulo del problema>

## 1. Sintesis final

<la sintesis consensuada>

(o, si no hubo consenso:)

## 1. Mapa de disenso

| Posicion | Sostenida por | Fundamento | Que la resolveria |
|----------|---------------|------------|--------------------|
| ...      | ...           | ...        | evidencia/decision X |

Decision devuelta al operador (HITL).

## 2. Razonamiento consolidado

<el camino argumental: que propuestas iniciales hubo, que sobrevivio a la
critica, que objeciones criticas surgieron en refutacion y como se
resolvieron>

## 3. Aportes por experto

### <Experto 1> (<identidad>)
- <aporte atribuido>

### <Experto 2> (<identidad>)
- <aporte atribuido>

### <Experto N> (<identidad>)
- <aporte atribuido>

## 4. Supuestos aceptados

| Supuesto | Levantado por | Por que se acepta |
|----------|---------------|--------------------|

## 5. Riesgos pendientes

| Riesgo | Levantado por | Severidad | Mitigacion sugerida |
|--------|---------------|-----------|---------------------|

## 6. Incertidumbres

<que no se sabe, que evidencia faltaria, que cambiaria la conclusion>

## 7. Confianza por experto

| Experto | Confianza | Justificacion | Que la subiria |
|---------|-----------|---------------|-----------------|

(nunca promediar; la divergencia de confianza es informacion)

## 8. Metadatos de la deliberacion

- modo de realizacion: encarnacion | orquestacion
- ciclos de refutacion ejecutados: <n> / max <max_ciclos>
- objeciones criticas resueltas: <n>
- objeciones menores registradas: <n>
- resultado: consenso | disenso estructurado
```

## Criterios de calidad del documento

- Toda afirmacion central de la sintesis debe ser rastreable a un aporte
  atribuido (§3) o a la resolucion de una objecion (§2).
- §4 y §5 no pueden estar vacios en un problema no trivial: una deliberacion
  sin supuestos ni riesgos registrados es senal de consenso de cortesia.
- Si §7 muestra divergencia fuerte de confianza, §6 debe explicar que ve el
  experto menos confiado que los otros no ven.
