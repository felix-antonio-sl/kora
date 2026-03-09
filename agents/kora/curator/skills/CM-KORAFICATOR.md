---
_manifest:
  urn: urn:kora:skill:curator-koraficator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-KORAFICATOR

## Proposito
Ejecuta el Funtor K: DocHumano → KORA/MD conforme a md-spec §6. Transforma documentos humanos en artefactos descriptivos RAG-optimizados preservando fidelidad absoluta.

## Input/Output
- **Input:** documento_fuente: Document (documento humano a koraficiar), plan: ArtifactPlan | null (plan de CM-ARTIFACT-DESIGNER, si existe)
- **Output:** KoraficationResult (ver Signature Output)

## Procedimiento
### Fase 0: Pre-Analisis Documental (NUEVA)
Antes de cualquier transformacion, escanear el documento fuente:
1. **Inventario MEAT/FAT/SKELETON**:
   - MEAT: hechos atomicos, cifras, fechas, plazos, excepciones, condiciones, referencias legales -> PRESERVAR SIEMPRE
   - FAT: retorica, introduciones, transiciones, hedging, frases de relleno, repeticiones -> ELIMINAR
   - SKELETON: titulos, subtitulos, estructura jerarquica -> PRESERVAR
2. **Enumerar hechos atomicos** del documento fuente → registrar N_hechos (denominador para FS en Fase 8)
3. **Estimar %meat/%fat** del documento (orientativo):
   - >60% meat: documento denso, CR esperado ~1.2-1.8
   - 30-60% meat: documento mixto, CR esperado ~1.5-2.5
   - <30% meat: documento con mucha grasa, CR esperado >2.0
4. **Identificar candidatos a deduplicacion**: hechos que aparecen en multiples secciones
5. **Identificar familia documental**: normative, glossary, organigram, cq_catalog, inventory/control u otra familia explicitada por el plan
6. **Output interno** (no incluir en artefacto final): reporte pre-analisis con N_hechos, %meat/%fat estimado, lista candidatos dedup y familia propuesta

### Fase 1: Evaluacion del Input (md-spec §6.4)
1. Clasificar documento segun criterios:
   - Largo: <5K(directo), 5K-15K(segmentado), >15K(segmentado+adversarial)
   - Estructura: con headings(segmentar por headings) vs monolitica(segmentar por temas)
   - Contenido numerico: alto(verificacion mecanica obligatoria) vs bajo(opcional)
   - Familia documental: define invariantes de surface realization
2. **Docs monoliticos** (sin headings claros o un solo bloque de texto):
   - Identificar temas semanticos recurrentes (personas, procesos, fechas, condiciones)
   - Proponer titulo sintetico por segmento tematico antes de transformar
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

### Fase 3: Compresion Semantica (md-spec §6.6.1)
Por cada segmento (o documento completo si <5K):
1. Comprimir toda prosa a forma mas densa sin perder informacion.
2. Preservar: toda cifra, fecha, plazo, excepcion, condicion, referencia legal.
3. Preservar idioma: output en mismo idioma del input.
4. Preservar estructuras: toda lista conserva todos sus items, toda tabla conserva todas sus filas y columnas.
5. Promover: prosa comparativa/condicional → tablas o listas. Direccion siempre prosa→estructura.
6. NO reorganizar estructura de secciones. Mantener orden del original.
7. Prohibido: introducciones, transiciones, hedging, saludos, retorica.
8. **Anti-patrones (deteccion activa)**:
   - SOBRE-RESUMEN: ¿se perdio algun hecho de Fase 0 (MEAT)? → restaurar. Sintoma: cifra/fecha/condicion ausente.
   - SUB-TRANSFORMACION: ¿quedan introducciones/transiciones/hedging/saludos? → eliminar. Sintoma: "Este documento explica...", "A continuacion se presenta...", "Es importante destacar que...".
   - DEGRADACION-ESTRUCTURAL: ¿se convirtio tabla/lista en prosa? → revertir. Direccion correcta: siempre prosa→estructura, nunca estructura→prosa.
   - SOBRE-COMPRESION-SUPERFICIAL: ¿la salida ya suena a dump comprimido? → deferir a Fase 3b.

### Fase 3b: Realizacion Superficial (md-spec §5.4.2, §6.6.2)
1. Elegir forma final del contenido: prosa, lista o tabla.
2. Realizar headings finales recuperables y no truncados.
3. Eliminar labelese: headings-campo, serializacion de `Asunto`, `Contenido`, `Tipo`, `Path`, etc.
4. Mantener listas y tablas solo cuando mejoren recuperacion real.
5. Si una lista o tabla degrada legibilidad sin aportar estructura, convertir a prosa tecnica breve.
6. Aplicar invariantes de la familia documental detectada en Fase 0.
7. Validar que la salida suena a conocimiento curado, no a dump comprimido.

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
- Realizacion superficial pobre aun con fidelidad correcta

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
- Headings no truncados: `...` en heading = falla
- Headings-campo prohibidos en KB publicada = falla
- Resumen obligatorio por familia cuando aplique = falla

### Fase 8: Verificacion de Fidelidad y Calidad (md-spec §6.11)
Ejecutar siempre como cierre estructurado de fidelidad y calidad:

1. **Reporte estructurado de hechos** (usando N_hechos de Fase 0):
   Para cada hecho atomico identificado en Fase 0, clasificar:
   - **Preservado**: aparece en output con mismo contenido semantico
   - **Comprimido**: aparece en output en forma mas densa pero semanticamente equivalente
   - **Omitido**: no aparece en output → FALLA CRITICA
   - **Agregado**: aparece en output pero no estaba en fuente → FALLA (alucinacion)

2. **Calcular metricas**:
   - FS = (preservados + comprimidos) / N_hechos × 100 → objetivo: 100%
   - CR = len(fuente) / len(output) → objetivo: >1.5
3. **Auditoria de superficie**:
   - headings recuperables
   - ausencia de labelese
   - ausencia de dumping estructural
   - calidad tecnica minima de la salida
4. **Algoritmo de iteracion acotada** (maximo 2 iteraciones):
   - Si FS < 100%: restaurar hechos omitidos
   - Si CR < 1.5: reducir redundancia restante o justificar alta densidad
   - Si la superficie falla: volver a Fase 3b y reparar forma final sin tocar fidelidad
   - Si tras 2 iteraciones FS < 100%: reportar omisiones especificas al usuario con lista de hechos afectados
   - Si tras 2 iteraciones CR < 1.5 (pero FS=100%): reportar alta densidad informacional
   - Si tras 2 iteraciones la superficie sigue fallando: reportar fallo de realizacion superficial
5. **Output de verificacion** (incluir en respuesta al usuario):
   ```
   VERIFICACION FIDELIDAD Y CALIDAD
   N_hechos_fuente: {N}
   Preservados: {n} | Comprimidos: {n} | Omitidos: {n} | Agregados: {n}
   FS: {X}% | CR: {Y} | Iteraciones: {Z}
   Superficie: PASS|FAIL
   Status: FIDELIDAD COMPLETA | OMISIONES DETECTADAS | SUPERFICIE DEFECTUOSA
   ```

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artefacto | string | Artefacto KORA/MD completo (frontmatter + cuerpo) |
| FS | number | Fidelity Score (objetivo: 100%) |
| CR | number | Compression Ratio (objetivo: >1.5) |
