# Canonización ISO OPM en español

Fecha: 2026-04-14

## Hecho principal

- Se cerró una versión española de uso interno de ISO/PAS 19450 en:
  `/home/felix/kora/KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-iso-19450.md`

## Decisión

- Tratar ese archivo como ISO interno operativo para OPM en español.
- No usarlo como traducción libre ni como resumen editorial: quedó con cobertura estructural equivalente al original.
- Usar `opm-opl-es.md` como referencia canónica para la superficie textual OPL en español.

## Invariantes editoriales fijadas

- OPL-ES usa verbos canónicos como `genera`, `maneja`, `requiere`, `cambia ... de ... a ...`, `puede estar`, `se descompone en`, `consta de`, `es una instancia de`.
- Los estados se expresan detrás del objeto con `en`, no como modificadores ingleses previos.
- El documento se dejó sin residuos de fórmulas OPL inglesas en el cuerpo español.
- La revisión editorial cerró terminología, metalenguaje y ejemplos para que el documento pueda usarse sin "proxy" al inglés.

## Verificación estructural

- La versión española quedó con la misma arquitectura del original:
  - 138 encabezados
  - 308 filas de tabla
  - 14 bloques de código

## Consecuencia operativa

- Para trabajo futuro sobre OPM en español, este documento ya puede funcionar como base cerrada de modelado, documentación, enseñanza y normalización interna.
- Si se extiende o deriva, la regla es preservar este canon y no reintroducir variantes locales o dependencias innecesarias del inglés.
