# WikiGuías Corpus

## Overview

This corpus contains a structured capture of the [WikiGuías de la Secretaría de Gobierno Digital de Chile](https://wikiguias.digital.gob.cl/).
The content was exhaustively crawled on 2025-12-09.

## Structure

The corpus is organized by the main categories found in the sidebar:

- **Regulación**
- **Lineamientos Técnicos**
- **Plataformas Compartidas**
- **Estrategias**
- **Protección de Datos Personales**

Each guide is saved as a Markdown file with YAML frontmatter containing metadata:

- `title`: The title of the guide.
- `url`: The original URL.
- `category`: The category path.
- `tags`: Associated tags.
- `description`: Brief description.
- `updated_at`: Last update timestamp.

## Content

Total Guides Captured: 39

## Statistics

To see file counts:

```bash
find . -type f -name "*.md" | wc -l
```
