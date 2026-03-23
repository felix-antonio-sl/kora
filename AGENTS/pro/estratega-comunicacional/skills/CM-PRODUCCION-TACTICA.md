---
_manifest:
  urn: urn:pro:skill:estratega-produccion-tactica:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Generar piezas comunicacionales concretas y listas para usar: briefs, lineas discursivas, Q&A voceros, FAQs y narrativas cortas. Verificar que cada pieza tenga mensaje central claro, un solo CTA y tono consistente.

## Input/Output

- **Input:** Formato solicitado (brief | lineas_discursivas | qa_voceros | faq | narrativa_corta) + contexto o narrativa previa.
- **Output:** PiezaTactica { formato, contenido_estructurado, verificacion }

## Procedimiento

1. Identificar formato solicitado:
   - **BRIEF**: objetivo, audiencia, mensaje central, tono, CTA, restricciones.
   - **LINEAS DISCURSIVAS**: principales + apoyo + lo que NO decir.
   - **Q&A VOCEROS**: pregunta probable -> respuesta recomendada -> puente a mensaje clave.
   - **FAQ**: pregunta frecuente -> respuesta clara -> contexto.
   - **NARRATIVA CORTA**: hook -> desarrollo -> cierre con CTA.
2. Generar pieza con estructura del formato elegido.
3. Verificar: mensaje central claro en primeros 10 segundos, un solo CTA, tono consistente con narrativa.
4. Calibrar output: chunks de 3-5 elementos, capas sintesis -> desarrollo -> detalle, progresion familiar -> nuevo.

## Signature Output

```
[FORMATO]: <tipo>
<contenido estructurado segun formato>
Verificacion: Mensaje central: <si/no> | CTA unico: <si/no> | Tono consistente: <si/no>
```
