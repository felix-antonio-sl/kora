---
_manifest:
  urn: urn:salud:kb:hodom-glosario-handoff
  provenance:
    created_by: Claude Code (Opus 4.7, 1M context) con Felix Sanhueza Luna
    created_at: '2026-05-18'
    updated_at: '2026-05-18'
version: 1.0.0
status: handoff
lang: es
tags:
  - hodom
  - glosario
  - handoff
  - vocabulario-controlado
---

# HANDOFF — Glosario Terminológico HODOM

Estado a **2026-05-18** tras pasada de autoría polymath (v1.4.0). Documento de continuidad para sesiones futuras.

## 1. Estado actual de los archivos

Tres archivos coexisten en `artifacts/knowledge/salud/salubrista/hodom/`:

| Archivo | Versión | Líneas | Lemas | Origen | Estado |
|---|---|---:|---:|---|---|
| `glosario-terminologico-hodom.md` | 1.0.1 | 724 | 118 | agente Hermes hospitalista (línea paralela del operador) | zona ajena — no tocar |
| `glosario-terminologico-hodom-v1.3.0.md` | 1.3.2 | 1181 | 174 | esta línea de trabajo (Claude + salubrista) | publicado, auditado P0/P1/P2 cerrados |
| `glosario-terminologico-hodom-v1.4.0.md` | 1.4.0 | 1708 | 182 | esta línea con autoridad polymath | publicado |

Notas:

- El path del archivo v1.3.2 conserva el sufijo `-v1.3.0` por convención: la versión semántica vive en el frontmatter; renombrar requeriría `git mv` y se difirió.
- Los archivos no se sobrescriben entre sí. v1.3.2 queda como histórico depurado de la línea estrictamente normativa; v1.4.0 es la línea con autoridad polymath y techo técnico sobre la norma.

## 2. Cadena de autoridad declarada

Definida por el operador el 2026-05-18:

```
Norma (DS 1/2022, Acto Exento 31/2024, NT 2024)
    ↓ piso, no techo
Salubrista (KB salubrista, literatura clínica, sociedades científicas)
    ↓ amplía con conocimiento sustantivo no estrictamente normativo
Polymath
    ↓ autoridad resolutoria de escritura final con estricta precisión semántica
v1.4.0
```

En el frontmatter de v1.4.0: `polymath_authored: true`, `authority_layer: polymath`, `family: normative-technical`.

## 3. Decisiones editoriales acumuladas

- **v1.0.0 → v1.1.0**: limpieza de rastros del modelo OPM (URNs `e-*`, deltas `Δ-*`, supuestos, refinamientos, Unfolds, subprocesos SD-*). Glosario terminológico puro, sin bitácora de modelado.
- **v1.1.0 → v1.2.0**: endurecimiento de cita normativa (artículo + letra + inciso), forma denotativa, umbrales textuales, distinciones explícitas en pares confundibles.
- **v1.2.0 → v1.3.0**: 15 renombramientos canónicos (Médico de Atención Directa, Transferencia a HD, Egreso de HD, UGC, Atención No Programada, Capacidad Operacional HODOM, etc.); 2 disoluciones de constructos OPM residuales (Coordinación Clínica HD → Seguimiento + Categorización + Continuidad; Reporte Información → Registro Evolutivo); 21 lemas nuevos; 2 desdobles; 1 fusión.
- **v1.3.0 → v1.3.1**: 4 P0 + 6 P1 sustantivos (regresión `Equipo de Salud HD`, 3 redirectoras prometidas en índice y ausentes en cuerpo, desambiguación `Solicitud (proceso)/(documento)`, `Atención Cerrada` en índice, `Relacionados:` en hubs y causales, transiciones de estado en subprocesos de Evaluación, `Distinción:` triangular en cadena del paciente, excepciones al esquema declaradas).
- **v1.3.1 → v1.3.2**: 6 P2 (política de siglas, glosa anexa en redirector, letras unitarias del índice, sinónimos no replicados, HaH fuera del índice, `Distinción` Indicación↔Solicitud proceso).
- **v1.3.2 → v1.4.0**: salto de criterio editorial. Norma deja de ser techo. Polymath introduce dos campos: `Anclaje técnico:` (autoridad sustantiva no normativa, 74 lemas) y `Refinamiento polymath:` (delta sobre la norma, 20 lemas). Tres secciones nuevas: 7 Indicadores operativos, 9 Calidad/seguridad/resultados, 11 Anexo terminológico internacional (HaH y modalidades adyacentes).

## 4. Anclajes normativos verificados

- `art. 19` letras a–l: dependencias físicas, infraestructura, equipamiento (5+ menciones residuales legítimas, no actualizar).
- `art. 21 N° 2`: Constancia de Acciones en caso de Fallecimiento.
- `art. 21 N° 3`: Encuesta de Satisfacción Usuaria al Egreso.
- `art. 21 N° 4`: Consentimiento Informado.
- `art. 21 N° 5`: Carta de Derechos y Deberes.
- `art. 21 N° 6`: Formulario de Ingreso.
- `art. 21 N° 8`: Plan de Cuidados de Enfermería y Plan Terapéutico.
- `art. 21 N° 9`: Reporte de Atención Profesional.

Estos anclajes fueron incorporados desde la línea Hermes y verificados contra DS 1/2022. La línea original v1.0.0 los citaba como `art. 19 letras b–i` (incorrecto).

## 5. Coexistencia con la línea Hermes

- El agente Hermes hospitalista (PID 3034725, perfil `--profile hospitalista`) trabaja el archivo `glosario-terminologico-hodom.md` (canónico, v1.0.1) como parte de su workflow propio del operador.
- Hermes no ha tocado el archivo desde 2026-05-14 09:55. Su actividad reciente es en epicrisis, sesiones clínicas DAU/LIS/HCC y borradores en `/home/felix/_TEMP_BORRAR/`.
- **Regla operativa**: cualquier intervención sobre el glosario debe **no tocar** `glosario-terminologico-hodom.md`. Las líneas de trabajo se mantienen separadas por path.
- Pendiente del operador: decidir si fusionar las dos líneas o mantenerlas paralelas indefinidamente.

## 6. Pendientes

- **Renombrar archivo de v1.3.2** a `glosario-terminologico-hodom-v1.3.2.md` (requiere `git mv` y actualización del path en referencias internas). Diferido.
- **Política de coexistencia con Hermes**: decidir si v1.4.0 reemplaza al canónico, si se mantienen paralelas, o si Hermes debe migrar a la línea polymath. Decisión del operador, pendiente.
- **Auditoría P0/P1/P2 de v1.4.0**: aún no se ha hecho. La auditoría de v1.3.0 detectó 22 hallazgos. Esperar misma cantidad o más en v1.4.0 por el mayor volumen.
- **Comparativa cuantitativa v1.4.0 vs canónico Hermes** (qué cubre cada uno, qué dice cada uno sobre los mismos lemas).
- **Validación clínica de los `Refinamiento polymath:`** (20 puntos donde el glosario va sobre la norma) con clínicos HODOM reales.

## 7. Supuestos vigentes

- El operador prefiere mantener las dos líneas (Hermes y polymath) en paralelo hasta resolver explícitamente.
- Polymath tiene autoridad resolutoria sobre el glosario v1.4.0; no requiere ratificación por capa normativa para `Refinamiento polymath:` y `Anclaje técnico:`.
- Los 32 lemas propuestos por salubrista para v1.4.0 fueron filtrados a 8 netos por polymath con criterio de utilidad operativa real; el resto (Carga del Cuidador, Polifarmacia, Determinantes Sociales, Cuidador Formal/Informal, Adherencia al Plan, Admisión Evitada, Alta Temprana Asistida) puede reintroducirse en v1.5.0 si el operador lo pide.
- Los anclajes `art. 19` / `art. 21 N° N` que adoptó la línea polymath provienen de la corrección de Hermes; se asumen correctos contra DS 1/2022 vigente.

## 8. Riesgos

- **Riesgo de divergencia**: si Hermes vuelve a modificar el canónico y el operador no decide política de fusión, las dos líneas se separarán semánticamente con el tiempo.
- **Riesgo de proliferación de archivos**: cada salto mayor sin renombrado físico de archivos puede llevar a confusión de paths. Convenio actual: versión vive en frontmatter; conservar.
- **Riesgo de over-engineering**: v1.4.0 introduce 11 secciones, 74 anclajes técnicos y 11 entradas de anexo internacional. Si el lector clínico chileno solo necesita el vocabulario operativo, el glosario quedó pesado. Mitigación: la sec. 11 (anexo) está separada visualmente para que pueda saltarse.
- **Riesgo de obsolescencia normativa**: el DS 1/2022 podría actualizarse y romper anclajes. Mitigación parcial: el campo `Fuente:` es quirúrgico (art. + letra + inciso) y un diff normativo se detectaría rápido.

## 9. Artefactos relacionados

- KB normativa primaria:
  - `urn:salud:kb:hodom-reglamento-ds1-2022` → `normativa/01-reglamento-hodom-ds1-2022.md`
  - `urn:salud:kb:hodom-decreto-exento-31-2024` → `normativa/02-decreto-exento-31-2024-aprueba-norma-tecnica.md`
  - `urn:salud:kb:hodom-norma-tecnica-2024` → `normativa/03-norma-tecnica-hodom-2024.md`
- KB de dirección técnica HODOM:
  - `urn:salud:kb:hodom-direccion-tecnica` → `director/01-manual-direccion-tecnica.md`
  - `urn:salud:kb:hodom-manual-alta-complejidad` → `director/02-manual-alta-complejidad.md`
  - `urn:salud:kb:hodom-situacion-chile-2026` → `director/03-situacion-chile-2026.md`
- Modelo OPM HODOM v1.1: `/home/felix/projects/hd-hsc-os/docs/models/opm-hodom-bundle-v1.1.json` (línea de modelado conceptual paralela; el glosario es deliberadamente independiente de ella).
- Informe intermedio del salubrista (v1.4.0): persistido temporalmente en `/tmp/informe-salubrista-ampliacion-hodom-v1.4.0.md` durante la sesión; no commiteado.

## 10. Cómo retomar

1. Leer este HANDOFF.
2. Decidir uno de:
   - Auditar v1.4.0 (siguiente pasada lógica).
   - Resolver coexistencia con Hermes (decisión política).
   - Continuar agregando lemas pendientes (Carga del Cuidador, Polifarmacia, etc.).
   - Renombrar archivo v1.3.2 a su nombre canónico.
3. Confirmar con el operador antes de actuar sobre la línea Hermes (zona ajena).
