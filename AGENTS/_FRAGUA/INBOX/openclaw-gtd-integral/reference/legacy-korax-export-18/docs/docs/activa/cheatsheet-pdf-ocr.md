# 📄 Cheatsheet: LLMs + PDFs con Contenido Visual Complejo

> Claude y otros LLMs **no leen PDFs nativamente**. Procesan texto extraído o imágenes renderizadas. Todo lo demás es ilusión.

---

## 🗺️ Mapa rápido: ¿qué tipo de PDF tenés?

| Tipo de PDF | Descripción | Estrategia |
|---|---|---|
| 📝 Texto nativo | Generado digitalmente, capa de texto real | `pdftotext` o extracción directa |
| 🖼️ Escaneado (imagen) | Foto de página, sin capa de texto | OCR primero (Drive, Tesseract, AWS) |
| 📊 Tablas complejas | Celdas anidadas, merges, multicolumna | Vision modelo + prompt estructurado |
| 🏛️ Formulario institucional | Campos con líneas, cajas, firma | Vision + extracción campo por campo |
| 🌀 Diagramación caótica | Columnas irregulares, sidebars, notas al margen | Imagen por página + instrucción explícita de orden |

---

## ✅ Qué funciona bien

- **PDFs de texto nativo bien formateados** → `pdftotext` entrega texto limpio, Claude lo procesa perfecto
- **Tablas simples** (sin merge, sin nesting) en texto o imagen clara → extracción confiable
- **Formularios con campos etiquetados** → Claude identifica clave-valor si la imagen es nítida
- **OCR previo de calidad** → si el texto ya fue extraído bien, el LLM trabaja normal
- **Una página a la vez** → más contexto visual, menos error de posicionamiento

---

## ❌ Qué falla o es poco confiable

| Problema | Por qué falla |
|---|---|
| PDFs escaneados enviados directo | No hay capa de texto; el LLM ve solo bytes binarios |
| Tablas con celdas fusionadas | La alineación espacial no se preserva en texto plano |
| Diagramas, gráficos, infografías | Son imágenes; sin vision no hay información |
| Múltiples columnas de texto | `pdftotext` las mezcla en orden incorrecto |
| Firmas, sellos, marcas de agua | Ruido visual que confunde extracción |
| PDFs protegidos o con permisos | Extracción bloqueada |
| >50 páginas de golpe | Contexto limitado, errores por saturación |

---

## 🛠️ Workarounds reales

### 1. Google Drive OCR (gratis, fácil)
```
1. Subir PDF a Google Drive
2. Clic derecho → "Abrir con Google Docs"
3. Drive aplica OCR automáticamente
4. Copiar texto resultante → pegar al LLM
```
✅ Funciona bien para escaneados simples. Falla en diagramas y tablas complejas.

---

### 2. `pdftotext` (CLI, Linux/Mac)
```bash
# Texto básico
pdftotext archivo.pdf salida.txt

# Mantener layout (mejor para tablas)
pdftotext -layout archivo.pdf salida.txt

# Página específica
pdftotext -f 3 -l 3 archivo.pdf -
```
✅ Ideal para PDFs digitales. Rápido y sin dependencias externas.

---

### 3. Renderizar como imagen + Vision model
```bash
# Convertir PDF a imágenes (requiere poppler)
pdftoppm -r 200 archivo.pdf pagina

# O con ImageMagick
convert -density 200 archivo.pdf pagina-%03d.png
```
Luego enviar imagen al LLM con instrucción:
> *"Extrae todo el contenido de esta página en orden de lectura natural. Si hay tabla, devuélvela en Markdown."*

---

### 4. AWS Textract / Azure Document Intelligence
- Mejor para formularios institucionales y tablas complejas
- API de pago, precisión profesional, devuelven JSON con coordenadas + estructura

### 5. Tesseract OCR (open source)
```bash
sudo apt install tesseract-ocr
tesseract pagina.png salida -l spa       # texto
tesseract pagina.png salida -l spa pdf   # PDF con capa de texto
```
✅ Gratis, offline. Calidad inferior a Drive/AWS en textos degradados.

---

## 📋 Protocolo por caso de uso

| Caso | Pasos clave |
|---|---|
| 🏛️ Formulario escaneado | Drive OCR → imagen por página → prompt: *"devuelve JSON {campo: valor}"* |
| 📊 Tabla compleja | Imagen recortada → *"N columnas, extrae como Markdown"* → si falla: fila por fila |
| 🌀 Diseño caótico | `pdftoppm` → 1-2 páginas por mensaje → especificar orden de lectura explícito |
| 📝 PDF largo nativo | `pdftotext -layout` → dividir en chunks de ~30K tokens → procesar por sección |

---

## ⚡ Reglas de oro

- **Siempre verificar si es texto o imagen** antes de procesar (`pdfinfo archivo.pdf`)
- **OCR primero, LLM después** — no al revés
- **Imagen nítida > imagen comprimida** — 150-200 DPI mínimo para OCR
- **Página por página > PDF completo** para contenido visual denso
- **No confiar ciegamente** en extracciones de tablas — siempre validar contra original
