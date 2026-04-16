---
_manifest:
  urn: urn:korvo:skill:cm-catalizador:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Diagnostico existencial y alineamiento estrategico. HUMAN 3.0 (4 cuadrantes x 3 niveles) + Life Worth Living Goals + filtro anti-vision como instrumentos de navegacion vital. Traces to: manual-de-vida §7.1, §7.2, §6.1; dan-koe-filosofia-creador HUMAN 3.0.

## Input/Output

- **Input:** Contexto vital actual del operador, objetivos PCA activos (via `pca estado` si disponible)
- **Output:** Diagnostico por cuadrante + secuencia de desbloqueo + alineamiento LWLG + alertas anti-vision

## Procedimiento

### Paso 1: Diagnostico HUMAN 3.0 (§7.1)

Para cada cuadrante, preguntar y evaluar nivel 1.0/2.0/3.0:

| Cuadrante | 1.0 Supervivencia | 2.0 Estabilidad | 3.0 Expresion |
| --- | --- | --- | --- |
| **Cuerpo** | Dolor cronico, sedentarismo, sueno roto | Rutina basica de movimiento, sueno OK | Entrenamiento consistente, energia alta, vitalidad |
| **Mente** | Rumiacion, ansiedad persistente, confusion | Claridad funcional, puede planificar | Curiosidad activa, aprendizaje por placer, creatividad |
| **Espiritu** | Aislamiento, cinismo, vacio | Conexiones funcionales, algo de proposito | Comunidad, servicio, trascendencia, gratitud espontanea |
| **Vocacion** | Trabajo por obligacion, sin agencia | Competencia reconocida, estabilidad | Trabajo como expresion, impacto, flujo frecuente |

Preguntar por cada cuadrante: *"Del 1 al 3, donde sientes que estas en <cuadrante>?"*

Identificar el cuadrante mas bajo = **punto de apalancamiento**.

### Paso 2: Secuencia de desbloqueo

El cuadrante mas bajo desbloquea al siguiente en sentido horario:

```
       Mente
        ↑  ↘
Espiritu    Vocacion
        ↗  ↙
       Cuerpo
```

| Si mas bajo es | Desbloquea | Como |
| --- | --- | --- |
| Cuerpo | Espiritu | Vitalidad fisica genera capacidad de conexion |
| Espiritu | Mente | Seguridad relacional permite cuestionar creencias |
| Mente | Vocacion | Claridad mental habilita trabajo autentico |
| Vocacion | Cuerpo | Estabilidad economica/profesional permite invertir en salud |

Proponer 1-2 acciones concretas para el cuadrante de apalancamiento:
- Cuerpo: "10 min caminata diaria", "dormir 30 min antes"
- Espiritu: "1 conversacion real esta semana", "5 min gratitud manana"
- Mente: "leer 15 min algo que te interese", "escribir 1 pagina libre"
- Vocacion: "1 bloque DEEP en tu proyecto core", "compartir 1 aprendizaje"

### Paso 3: Alineamiento LWLG (§7.2)

Life Worth Living Goals = los objetivos que hacen que la vida valga la pena vivirla.

Preguntar:
1. *"Cuales son tus Life Worth Living Goals ahora mismo? (3 maximo)"*
2. *"Tus PROPOSITOS en el sistema PCA reflejan estos LWLGs?"*
   - Si hay PROPOSITOS PCA: comparar titulos y anti_vision con LWLGs
   - Si no hay: *"Quieres crear PROPOSITOS que reflejen tus LWLGs?"*
3. *"Hay disonancia entre lo que haces dia a dia (UTs) y lo que quieres ser?"*
   - Si disonancia: *"Que tendria que cambiar? Es un tema de prioridad, de coraje, o de claridad?"*

### Paso 4: Filtro anti-vision (§6.1)

Anti-vision = la vida que te niegas a vivir.

Preguntar:
1. *"Que es lo que te niegas a vivir? (sin filtro)"*
2. *"Alguna decision reciente te acerca a esa anti-vision?"*
3. Si hay PROPOSITOS PCA con restricciones: *"Alguna UT activa viola tus restricciones declaradas?"*
   - Cruzar con RI-12 del sistema PCA

Si se detecta acercamiento a anti-vision: alertar sin juzgar. *"Esto parece acercarse a lo que dijiste que te niegas a vivir. Quieres hablar de eso?"*

### Paso 5: Sintesis

Consolidar diagnostico + alineamiento + alertas en reporte breve.

Si el diagnostico revela necesidad de cambio profundo: *"Quieres activar un protocolo de reinvencion? (2 dias, manual-de-vida §10)"*

## Signature Output

```
🔮 Diagnostico Vital
   HUMAN 3.0: Mente=<n> Cuerpo=<n> Espiritu=<n> Vocacion=<n>
   Apalancamiento: <cuadrante mas bajo> → desbloquea <cuadrante siguiente>
   Accion propuesta: <1-2 acciones concretas>
   LWLG: {alineados|disonancia detectada: <detalle>}
   Anti-vision: {limpio|⚠️ <alerta>}
```
