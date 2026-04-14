---
_manifest:
  urn: urn:korvo:skill:cm-regulacion-emocional:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Detectar estado emocional via 8 firmas corporales, calibrar con "fits the facts", y aplicar accion opuesta cuando la emocion es excesiva. Incluye Ready-Set-Go rapido para resistencia y procrastinacion. Traces to: manual-de-vida §5.1, §5.2, §6.3.

## Input/Output

- **Input:** Estado energetico del operador (alto/medio/bajo/crisis), contexto actual (S-PLAN check-in o S-EXECUTE resistencia)
- **Output:** Diagnostico emocional + accion regulatoria propuesta + ready-set-go si aplica

## Procedimiento

### Paso 1: Chequeo corporal

Preguntar: *"Como estas? Que sientes en el cuerpo?"*

Mapear respuesta a 8 firmas corporales:

| Firma | Que observar |
| --- | --- |
| Temperatura | Calor/frio, sudoracion |
| Tension muscular | Mandibula, hombros, estomago |
| Ritmo cardiaco | Acelerado, normal, lento |
| Respiracion | Corta/superficial, profunda, contenida |
| Postura | Encogida, rigida, relajada |
| Expresion facial | Ceno fruncido, mandibula apretada, neutra |
| Energia general | Agitacion, pesadez, alerta |
| Impulso de accion | Huir, atacar, congelarse, acercarse |

### Paso 2: Identificar emocion dominante

Segun patron de firmas:
- Calor + tension + impulso atacar = **ira**
- Frio + encogimiento + impulso huir = **miedo**
- Pesadez + postura baja + impulso retirarse = **tristeza**
- Agitacion + respiracion corta + impulso escapar = **ansiedad**
- Rigidez + contencion + impulso congelarse = **verguenza**

### Paso 3: Calibrar — Fits the facts?

Preguntar: *"Tu <emocion> es proporcional a lo que esta pasando? Del 1 al 10, cuanto de esa emocion es por la situacion real y cuanto es por lo que imaginas?"*

- Si proporcional (>=7 situacion real): **validar**. *"Tiene sentido sentir esto. Que necesitas ahora?"*
- Si excesiva (<7 situacion real): **accion opuesta** (Paso 4)

### Paso 4: Accion opuesta por dominio (§5.2)

| Emocion excesiva | Accion opuesta |
| --- | --- |
| Ira | Enfriarse: bajar temperatura, relajar cara, reclinar postura, alargar exhalacion |
| Miedo | Aproximarse: dar un paso hacia lo temido, expandir postura, respirar profundo |
| Tristeza | Activarse: movimiento fisico, musica energetica, contacto social breve |
| Ansiedad | Anclarse: 5-4-3-2-1 sensorial (5 cosas que ves, 4 que tocas...), pies en el suelo |
| Verguenza | Exponerse: nombrar la verguenza en voz alta, recordar que otros tambien lo viven |

### Paso 5: Si resistencia/procrastinacion

Preguntar: *"Cual es la tension implicita? Que estas protegiendo?"*

Tension tipica: proteger autoestima ahora <-> invertir en yo-futuro.

Ready-Set-Go rapido (§6.3):
1. **Ready:** "Que es lo minimo que necesitas saber para empezar? Ni mas."
2. **Set:** "Elimina 1 distraccion ahora. Pon el archivo/herramienta frente a ti."
3. **Go:** "Cual es la accion mas pequena? Hazla en los proximos 2 minutos."

### Paso 6: Transitar

Reportar estado emocional procesado y volver al estado PCA que invoco (S-PLAN o S-EXECUTE).

## Signature Output

```
🫀 Estado: <emocion> (<intensidad>/10)
   Calibracion: <fits the facts? si/no>
   {Accion opuesta: <intervencion> | Validacion: <canalizacion>}
   {Ready-Set-Go: <1 accion minima> | }
```
