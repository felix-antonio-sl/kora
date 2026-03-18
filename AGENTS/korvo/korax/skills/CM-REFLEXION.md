---
_manifest:
  urn: urn:korvo:skill:cm-reflexion:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Cierre reflexivo del dia (3-2-1) y revisiones periodicas (semanal, mensual, trimestral). Integra rutina diaria (§8) y cadencias de revision (§11). Traces to: manual-de-vida §8, §11.

## Input/Output

- **Input:** Momento del ciclo (diario/semanal/mensual/trimestral), contexto del dia o periodo
- **Output:** Reflexion estructurada + intencion para el siguiente periodo

## Procedimiento

### A. DIARIO (en S-CLOSE, despues de CM-CLOSE)

Guiar reflexion 3-2-1 en menos de 5 minutos:

1. *"3 cosas que salieron bien hoy (por pequenas que sean)."*
   - Incluir completar UTs, conversaciones, momentos de presencia, autocuidado.
   - Si el operador dice "nada": *"Despertaste. Llegaste hasta aca. Eso cuenta."*

2. *"2 lecciones o cosas que harias diferente."*
   - Sin juicio. Observar, no castigar.
   - Si bloqueo: *"Que te sorprendio hoy? Que te costo mas de lo esperado?"*

3. *"1 intencion para manana."*
   - Concreta, no abstracta. *"Que es lo primero que quieres hacer manana?"*
   - Vincular con la UT de mayor PxU si hay plan activo.

Cerrar: *"Listo. Buen cierre."*

Sugerir: papel y lapiz > pantalla para la reflexion.

### B. SEMANAL (en S-SYNC o S-CLOSE del viernes)

3 preguntas de revision semanal:

1. *"Moviste las palancas diarias (levers) esta semana? Cuales si, cuales no?"*
   - Levers = las 1-3 acciones diarias que mas mueven la aguja (§6.2)

2. *"Protegiste tus bloques DEEP?"*
   - Cruzar con throughput PCA: `pca throughput --dias 7`
   - Si 0 bloques DEEP: *"Sin tiempo profundo esta semana. Que lo impidio?"*

3. *"Tu energia estuvo al servicio del trabajo o lo saboteo?"*
   - Si saboteo: *"Que habria ayudado? Dormir, movimiento, limites?"*

### C. MENSUAL (fin de mes)

3 preguntas de revision mensual:

1. **Anti-vision:** *"Te acercaste a algo que te niegas a vivir?"*
   - Referencia: anti_vision del PROPOSITO PCA si existe

2. **Vision:** *"Progresaste hacia tus Life Worth Living Goals?"*
   - Cruzar con completitud() de PROPOSITOS PCA activos

3. **Desatasco:** *"Hay algun proyecto estancado que necesite Ready-Set-Go?"*
   - Si hay UTs >30d sin actividad: proponerlas

### D. TRIMESTRAL (fin de trimestre)

2 preguntas + derivacion:

1. *"Es momento de un diagnostico HUMAN 3.0."* → derivar a CM-CATALIZADOR
2. *"Cual cuadrante necesita atencion?"* → secuencia de desbloqueo

## Signature Output

```
🌙 Reflexion <diaria|semanal|mensual|trimestral>
   3: <wins>
   2: <lessons>
   1: <intencion>
```
