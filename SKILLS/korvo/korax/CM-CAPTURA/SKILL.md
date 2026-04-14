---
_manifest:
  urn: urn:korvo:skill:cm-captura:1.1.0
  type: lazy_load_endofunctor
---

## Proposito

Crear un Candidato en el buffer a partir de texto libre del operador. Captura sin friccion: texto + timestamp, sin metadatos adicionales.

## Input/Output

- **Input:** texto libre del operador (string), canal de captura (contexto)
- **Output:** Candidato { id: CandidatoId, texto: string, fuente: FuenteCandidato, estado: "capturado", capturado_at: ISO8601 }

## Procedimiento

1. Recibir texto del operador.
2. Auto-detectar `fuente` del canal de interaccion (telegram, email, conversacion, nota, otro).
3. Crear entidad Candidato con:
   - `id`: identificador unico generado
   - `texto`: el input tal cual, sin modificar
   - `fuente`: canal auto-detectado
   - `estado`: "capturado"
   - `capturado_at`: momento de captura en ISO8601
4. NO agregar metadatos de trabajo (modo, urgencia, prioridad, contexto, clasificacion). Solo texto + fuente + timestamp (INV-05, P2).
5. Confirmar captura en una linea.
6. Si hay multiples items separados por saltos de linea, crear un Candidato por cada uno.

## Signature Output

```
📥 Capturado: "<texto truncado a 60 chars>" [<fuente>]
```

Si multiples:

```
📥 <N> candidatos capturados.
```
