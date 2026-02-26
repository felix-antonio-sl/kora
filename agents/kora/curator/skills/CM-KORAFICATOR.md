---
_manifest:
  urn: "urn:kora:skill:curator-koraficator:1.1.0"
  type: "skill"
version: "1.1.0"
status: published
lang: es
---
# CM-KORAFICATOR

## Proposito
Ejecuta el Funtor F: DocHumano → KORA/MD conforme a md-spec §6. Transforma documentos humanos en artefactos descriptivos RAG-optimizados preservando fidelidad absoluta.

## Procedimiento

### Fase 0: Pre-Analisis Documental (NUEVA)
Antes de cualquier transformacion, escanear el documento fuente:
1. **Inventario MEAT/FAT/SKELETON**:
   - MEAT: hechos atomicos, cifras, fechas, plazos, excepciones, condiciones, referencias legales → PRESERVAR SIEMPRE
   - FAT: retorica, introduciones, transiciones, hedging, frases de relleno, repeticiones → ELIMINAR
   - SKELETON: titulos, subtitulos, estructura jerarquica → PRESERVAR (telegrafizar headings)
2. **Enumerar hechos atomicos** del documento fuente → registrar N_hechos (denominador para FS en Fase 8)
3. **Estimar %meat/%fat** del documento (orientativo):
   - >60% meat: documento denso, CR esperado ~1.2-1.8
   - 30-60% meat: documento mixto, CR esperado ~1.5-2.5
   - <30% meat: documento con mucha grasa, CR esperado >2.0
4. **Identificar candidatos a deduplicacion**: hechos que aparecen en multiples secciones
5. **Output interno** (no incluir en artefacto final): reporte pre-analisis con N_hechos, %meat/%fat estimado, lista candidatos dedup

### Fase 1: Evaluacion del Input (md-spec §6.4)
1. Clasificar documento segun criterios:
   - Largo: <5K(directo), 5K-15K(segmentado), >15K(segmentado+adversarial)
   - Estructura: con headings(segmentar por headings) vs monolitica(segmentar por temas)
   - Contenido numerico: alto(verificacion mecanica obligatoria) vs bajo(opcional)
2. **Docs monoliticos** (sin headings claros o un solo bloque de texto):
   - Identificar temas semanticos recurrentes (personas, procesos, fechas, condiciones)
   - Proponer titulo sintetico por segmento tematico antes de telegrafizar
   - Registrar titulos propuestos para Fase 4

### Fase 2: Segmentacion (md-spec §6.5, si >5K tokens)
1. Identificar puntos de corte naturales (titulos, capitulos, secciones).
2. Cada segmento: tematica coherente, ~3-5K tokens.
3. Numerar: [Seg-1], [Seg-2], ..., [Seg-N].
4. NUNCA cortar dentro de tabla, lista o parrafo.
5. **Contexto deslizante**: al inicio de cada segmento (excepto [Seg-1]), incluir ancla de calibracion:
   `[Contexto previo: {1-2 oraciones resumen del segmento anterior}]`
   - Proposito: prevenir drift de nivel de compresion entre segmentos
   - Se ELIMINA completamente en Fase 4 (ensamblaje)
   - NO incluir en artefacto final

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
9. **Anti-patrones (deteccion activa)**:
   - SOBRE-RESUMEN: ¿se perdio algun hecho de Fase 0 (MEAT)? → restaurar. Sintoma: cifra/fecha/condicion ausente.
   - SUB-TRANSFORMACION: ¿quedan introducciones/transiciones/hedging/saludos? → eliminar. Sintoma: "Este documento explica...", "A continuacion se presenta...", "Es importante destacar que...".
   - DEGRADACION-ESTRUCTURAL: ¿se convirtio tabla/lista en prosa? → revertir. Direccion correcta: siempre prosa→estructura, nunca estructura→prosa.

### Fase 4: Ensamblaje (md-spec §6.7, si segmentado)
1. Concatenar segmentos koraficados en orden.
2. **Eliminar todos los marcadores** `[Contexto previo: ...]` del contexto deslizante.
3. Agregar # (H1) como titulo unificado.
4. Agregar separadores --- entre secciones ##.

### Fase 4b: Deduplicacion SSOT (NUEVA)
Escanear artefacto ensamblado:
1. Identificar informacion duplicada entre secciones (de lista candidatos de Fase 0 + revision completa).
2. Para cada duplicado:
   - Conservar instancia mas completa/contextualizada
   - Eliminar instancias redundantes
   - Si el concepto se necesita en multiples secciones: usar referencia interna Markdown `[→ Seccion-Nombre]`
   - NO usar "Ref: ID" (no existe en KORA/MD)
3. Verificar: cada hecho atomico aparece en exactamente un lugar (SSOT).

### Fase 5: Normalizacion (md-spec §6.8)
Condicional — aplicar SOLO si se cumple alguno de estos triggers:
- Redundancia estructural detectada (secciones sobre mismo tema NO resueltas en Fase 4b)
- Jerarquia de headings suboptima (H4/H5 cuando podrian ser H2/H3)
- Secciones excesivamente largas que degradan calidad chunk RAG (>800 palabras)

Si trigger presente:
1. Fusionar secciones que tratan mismo tema.
2. Dividir secciones excesivamente largas.
3. Reorganizar jerarquia de headings.
4. NO modificar texto de celdas, items de lista ni definiciones.
5. NO agregar ni eliminar informacion factual.

Si no hay trigger: omitir esta fase completamente.

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
- **Conteo de hechos**: verificar que N_hechos_output >= N_hechos_fuente (de Fase 0)

### Fase 8: Verificacion de Fidelidad (md-spec §6.11)
Reemplaza verificacion adversarial simple. Ejecutar siempre (no solo si >15K o alto numerico):

1. **Reporte estructurado de hechos** (usando N_hechos de Fase 0):
   Para cada hecho atomico identificado en Fase 0, clasificar:
   - **Preservado**: aparece en output con mismo contenido semantico
   - **Comprimido**: aparece en output en forma mas densa pero semanticamente equivalente
   - **Omitido**: no aparece en output → FALLA CRITICA
   - **Agregado**: aparece en output pero no estaba en fuente → FALLA (alucinacion)

2. **Calcular metricas**:
   - FS = (preservados + comprimidos) / N_hechos × 100 → objetivo: 100%
   - CR = len(fuente) / len(output) → objetivo: >1.5

3. **Algoritmo de iteracion acotada** (maximo 2 iteraciones):
   - Si FS < 100% o CR < 1.5:
     a. Identificar segmentos afectados (donde estan los hechos omitidos o la grasa restante)
     b. Re-telegrafizar SOLO esos segmentos (volver a Fase 3 parcialmente)
     c. Actualizar metricas
   - Si tras 2 iteraciones FS < 100%: reportar omisiones especificas al usuario con lista de hechos afectados
   - Si tras 2 iteraciones CR < 1.5 (pero FS=100%): reportar que documento tiene alta densidad informacional (CR bajo es aceptable si no hay grasa eliminable)

4. **Output de verificacion** (incluir en respuesta al usuario):
   ```
   VERIFICACION FIDELIDAD
   N_hechos_fuente: {N}
   Preservados: {n} | Comprimidos: {n} | Omitidos: {n} | Agregados: {n}
   FS: {X}% | CR: {Y} | Iteraciones: {Z}
   Status: FIDELIDAD COMPLETA | OMISIONES DETECTADAS (listar)
   ```

## Output
Artefacto KORA/MD completo (frontmatter + cuerpo). Metricas: FS (Fidelity Score, objetivo: 100%), CR (Compression Ratio, objetivo: >1.5 — >1.0 trivial, >1.5 objetivo, >2.0 excelente).
