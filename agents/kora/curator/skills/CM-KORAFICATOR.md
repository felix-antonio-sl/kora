---
_manifest:
  urn: "urn:kora:skill:curator-koraficator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-KORAFICATOR

## Proposito
Ejecuta el Funtor F: DocHumano → KORA/MD conforme a md-spec §6. Transforma documentos humanos en artefactos descriptivos RAG-optimizados preservando fidelidad absoluta.

## Procedimiento

### Fase 1: Evaluacion del Input (md-spec §6.4)
1. Clasificar documento segun criterios:
   - Largo: <5K(directo), 5K-15K(segmentado), >15K(segmentado+adversarial)
   - Estructura: con headings(segmentar por headings) vs monolitica(segmentar por temas)
   - Contenido numerico: alto(verificacion mecanica obligatoria) vs bajo(opcional)

### Fase 2: Segmentacion (md-spec §6.5, si >5K tokens)
1. Identificar puntos de corte naturales (titulos, capitulos, secciones).
2. Cada segmento: tematica coherente, ~3-5K tokens.
3. Numerar: [Seg-1], [Seg-2], ..., [Seg-N].
4. NUNCA cortar dentro de tabla, lista o parrafo.

### Fase 3: Telegrafizacion Fiel (md-spec §6.6)
Por cada segmento (o documento completo si <5K):
1. Telegrafizar: comprimir toda prosa a forma minima sin perder informacion.
2. Preservar: toda cifra, fecha, plazo, excepcion, condicion, referencia legal.
3. Preservar idioma: output en mismo idioma del input.
4. Preservar estructuras: toda lista conserva todos sus items, toda tabla conserva todas sus filas y columnas.
5. Promover: prosa comparativa/condicional → tablas o listas. Direccion siempre prosa→estructura.
6. NO reorganizar estructura de secciones. Mantener orden del original.
7. Headings telegraficos: sintagmas nominales, nunca oraciones completas.
8. Prohibido: introducciones, transiciones, hedging, saludos, retorica.

### Fase 4: Ensamblaje (md-spec §6.7, si segmentado)
1. Concatenar segmentos koraficados en orden.
2. Agregar # (H1) como titulo unificado.
3. Agregar separadores --- entre secciones ##.

### Fase 5: Normalizacion Opcional (md-spec §6.8)
Solo si redundancia evidente o estructura suboptima:
1. Fusionar secciones que tratan mismo tema.
2. Dividir secciones excesivamente largas.
3. Eliminar info duplicada (conservar instancia mas completa).
4. NO modificar texto de celdas, items de lista ni definiciones.
5. NO agregar ni eliminar informacion factual.

### Fase 6: Inyeccion Frontmatter (md-spec §6.9)
1. Agregar bloque YAML al inicio: _manifest(urn, provenance), version, status, tags(min 3), lang.
2. Schema conforme a md-spec §3.1.

### Fase 7: Verificacion Mecanica (md-spec §6.10)
Checks deterministas obligatorios:
- Conteo items lista: source vs output (diferencia > 0 = falla)
- Conteo filas tabla: source vs output (output < source = falla)
- Cifras preservadas: extraer \d+[\.,]?\d* del source, verificar en output
- Fechas preservadas: extraer patrones fecha, verificar en output
- Frontmatter valido: parsear YAML entre --- delimitadores
- URN sin version: buscar 4+ segmentos en cuerpo (match = falla)
- Lang coherente: campo lang vs idioma detectado

### Fase 8: Verificacion Adversarial (md-spec §6.11, si >15K o alto numerico)
1. Comparar original con artefacto generado.
2. Listar toda informacion presente en original NO representada en output.
3. Si omisiones detectadas → volver a Fase 3 para segmentos afectados.
4. Si cero omisiones → "FIDELIDAD: COMPLETA".

## Output
Artefacto KORA/MD completo (frontmatter + cuerpo). Metricas: FS (Fidelity Score, objetivo: 100%), CR (Compression Ratio, objetivo: >1.0).
