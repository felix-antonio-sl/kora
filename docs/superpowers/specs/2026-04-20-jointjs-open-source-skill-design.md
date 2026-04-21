# JointJS Open-Source Skill Design

## Intento

Crear una skill para Claude Code especializada en **JointJS open-source** que
resuelva consultas, implementación y debugging consultando **siempre** la
documentación oficial viva en `https://docs.jointjs.com/` antes de responder,
incluso para preguntas simples de API o uso.

La skill debe ser **semi Claude Code-first**:

- Claude Code dirige el workflow y la síntesis.
- La autoridad técnica sustantiva vive en la documentación oficial.
- El bundle local no replica ni cachea contenido técnico de JointJS.

## Scope

Incluido:

- skill nueva bajo `artifacts/skills/kora/jointjs-open-source/`
- `SKILL.md` compacto en shape productiva KORA (`autoria-spec`)
- orientación para consultas, implementación, integración y debugging
- política explícita para distinguir JointJS OSS de JointJS+

Excluido:

- snapshots locales de la docs de JointJS
- scraping, mirrors o corpus interno de la documentación
- soporte a JointJS+
- ejemplos embebidos extensos copiados desde la docs
- wrappers de tooling que automaticen navegación o scraping de la docs

## Decisión de diseño

Se elige una skill **live-docs puro** con bundle mínimo:

- `SKILL.md`

No se agregan `references/` con contenido técnico de JointJS porque eso
introduciría drift y rompería el contrato principal de la skill: consultar la
fuente oficial viva como primer paso operativo.

## Nombre y ubicación

Nombre propuesto:

- `jointjs-open-source`

Ubicación:

- `artifacts/skills/kora/jointjs-open-source/`

Justificación:

- deja explícito que el scope es OSS
- evita confusión con JointJS+
- sigue la convención corta y descriptiva del repo

## Arquitectura de la skill

### 1. Bundle mínimo

La skill debe contener solo:

- `SKILL.md`

No debe contener:

- README
- changelog
- referencias técnicas locales de JointJS
- assets
- scripts de scraping o descarga de docs

### 2. Fuente de verdad

La skill declara como SSOT técnico:

- `https://docs.jointjs.com/`

Y, por extensión, solo páginas oficiales navegadas desde esa raíz, tales como:

- Introduction
- Quickstart
- Integration
- Features
- Testing
- API Reference

Si una respuesta requiere contenido no confirmado en docs oficial, la skill
debe decirlo explícitamente como inferencia.

### 3. Workflow operativo

Workflow obligatorio:

1. Clasificar la consulta:
   - API puntual
   - implementación
   - integración framework
   - debugging
   - arquitectura/selección de features
2. Ubicar la sección oficial más probable en `docs.jointjs.com`
3. Leer la documentación oficial viva antes de responder
4. Responder o implementar usando esa base
5. Citar la ruta o sección oficial consultada
6. Marcar explícitamente qué parte es confirmada vs inferida

### 4. Regla “no solo para temas complejos”

La skill debe consultar la docs oficial también para:

- imports
- nombres de clases
- eventos
- métodos
- shapes
- graph/paper
- puertos
- links
- tools
- integración React/Vue/Angular
- serialización
- testing

No se permite responder “de memoria” sobre la API de JointJS solo porque la
pregunta parezca simple.

### 5. Regla OSS vs Plus

La skill debe:

- asumir **OSS por defecto**
- detectar cuando una feature parece pertenecer a JointJS+
- decirlo explícitamente
- no presentar una feature Plus como si fuese parte del open-source

Si hay duda:

- consultar docs oficial
- responder con cautela
- explicitar la incertidumbre

## Contrato de salida

### Para consultas

Respuesta esperada:

- respuesta breve y accionable
- sección o página oficial consultada
- distinción entre dato confirmado e inferencia si aplica

### Para implementación

Salida esperada:

- código útil y mínimo
- mención explícita de la sección oficial usada
- si hay supuestos de versión o bundler, declararlos

### Para debugging

Salida esperada:

- hipótesis priorizadas
- contraste con docs oficial
- pasos concretos para verificar o corregir

## UX de la skill

La skill debe sentirse como:

- especialista pragmático en JointJS OSS
- disciplinado con fuente oficial
- corto en respuestas
- útil para producir código de inmediato

No debe sentirse como:

- mirror de la documentación
- tutorial largo
- experto performativo que responde sin verificar

## Shape de `SKILL.md`

Secciones mínimas:

- Propósito
- Cuándo usar
- Workflow
- Reglas duras
- Política OSS vs Plus
- Salida esperada

No hace falta una teoría extensa de diagramming ni de la historia del producto.

## Testing y validación

La skill queda aceptable si:

- su `SKILL.md` es compacto y claro
- el texto deja explícita la obligación de consultar docs viva
- se distingue JointJS OSS de JointJS+
- no se introduce corpus local técnico de JointJS

## Riesgos

1. El agente puede intentar responder por memoria si el `SKILL.md` no hace la
   regla suficientemente dura.
2. La docs oficial puede mover estructura o anchors; por eso conviene citar
   rutas y títulos, no solo anchors frágiles.
3. La frontera OSS/Plus puede confundirse si una página oficial menciona ambos
   productos en la misma sección; la skill debe explicitar esa frontera.

## Siguiente paso

Si este diseño queda aprobado, el siguiente paso es implementar la skill en:

- `artifacts/skills/kora/jointjs-open-source/SKILL.md`
