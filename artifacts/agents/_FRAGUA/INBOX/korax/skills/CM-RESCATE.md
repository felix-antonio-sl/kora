---
_manifest:
  urn: urn:korvo:skill:cm-rescate:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Protocolo de emergencia emocional. Estabilizar antes de operar. REGULACION primero, siempre. Combina TIP (§9), autocompasion (§5.3) y conexion con yo-futuro (§5.4). Traces to: manual-de-vida §9, §5.3, §5.4.

## Input/Output

- **Input:** Senal de crisis (operador explicita, colapso PCA detectado, abandono prolongado)
- **Output:** Secuencia de estabilizacion completada + 1 accion minima reconectora propuesta

## Procedimiento

### Paso 1: PARAR

*"Para todo. Respira."*

Sin juicio (A1). Sin analisis. Solo presencia.

### Paso 2: TIP (§9)

Guiar secuencia fisiologica:

| Tecnica | Instruccion | Efecto |
| --- | --- | --- |
| **T**emperatura | Agua fria en cara o munecas. Si no hay agua, hielo en manos. | Activa reflejo de inmersion, baja frecuencia cardiaca |
| **I**ntenso | 10-20 min ejercicio vigoroso: caminar rapido, subir escaleras, flexiones | Metaboliza cortisol, libera endorfinas |
| **P**aced breathing | Inhalar 4 tiempos, exhalar 8 tiempos. 5 ciclos minimo. | Activa parasimpatico, baja arousal |

Preguntar despues: *"Como estas ahora? Mejor, igual, peor?"*

Si no mejora: repetir T o P. No forzar I si el cuerpo no quiere.

### Paso 3: DETECTAR

*"Que emocion sientes? Donde la sientes en el cuerpo?"*

Usar 8 firmas corporales (§5.1) para nombrar la emocion. Nombrar reduce intensidad (affect labeling).

### Paso 4: REGULAR

**Si autocritica activa** → Autocompasion (§5.3):

Tres componentes:
1. **Auto-amabilidad:** *"Que te dirias si un amigo estuviera pasando por esto?"*
2. **Humanidad comun:** *"Esto es parte de ser humano. Otros tambien lo viven."*
3. **Mindfulness:** *"Esto es dolor. No necesito amplificarlo ni suprimirlo."*

Si la crisis fue post-procrastinacion, agregar autoperdon:
1. Responsabilidad: *"Si, no hice lo que queria. Eso paso."*
2. Emocion: *"Que siento al respecto? Nombrar sin juzgar."*
3. Restitucion: *"Cual es 1 cosa concreta que puedo hacer para reparar?"*

**Si desconexion del futuro** → Yo-futuro (§5.4):

Tres tecnicas (usar la que resuene):
1. **Concreto inmediato:** *"Como se siente tu yo de manana a las 8am si haces 1 cosa pequena ahora?"*
2. **Carta al yo-futuro:** *"Escribe 3 lineas a tu yo de 6 meses. Que le dices?"*
3. **Tres preguntas de significado:** *"Que dice esto de quien estoy construyendo? Que conexion tiene con mi vida? Que puedo aprender?"*

### Paso 5: RECONECTAR — Una accion minima

*"Cual es la cosa mas pequena que puedes hacer ahora mismo? No tiene que ser productiva. Solo tiene que ser un paso."*

Ejemplos: lavarse la cara, caminar 5 minutos, escribir 1 frase, enviar 1 mensaje.

La accion minima rompe la inercia. No es para resolver — es para reconectar.

### Paso 6: Transitar

Si el operador se estabilizo: transitar al estado PCA correspondiente (S-IDLE, o continuar con CM-BANCARROTA si era S-COLLAPSE).

Si no se estabilizo: *"No hay prisa. Podemos quedarnos aqui. Quieres hablar de algo?"*

## Signature Output

```
🛟 Rescate activado.
   TIP: {completado|pendiente}
   Emocion: <emocion detectada>
   Intervencion: {autocompasion|yo-futuro|ambas}
   1 accion minima: <propuesta>
```
