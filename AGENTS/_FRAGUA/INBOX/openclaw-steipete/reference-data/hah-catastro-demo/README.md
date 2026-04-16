# HAH catastro demo para steipete

Origen
- Fuente: `/home/felix/projects/hdos/src/data/mockData.ts`
- Contexto: `HODOM Tele` demo del Hospital de San Carlos
- Clasificación: mock / no productivo

Contenido
- `patients.georef.sanitized.json` — pacientes demo sanitizados para mapa/rutas
- `routes.sanitized.json` — vehículos/rutas demo sanitizadas
- `localidades.json` — localidades usadas en el demo
- `provenance.json` — trazabilidad del origen y de la sanitización

Campos removidos
- nombre
- rut
- teléfono
- dirección exacta
- diagnóstico detallado
- consentimiento
- profesional responsable

Uso sugerido
- demos de georreferenciación
- mapas de rutas
- asignación por macrozonas
- simulaciones operativas sin datos clínicos identificables
