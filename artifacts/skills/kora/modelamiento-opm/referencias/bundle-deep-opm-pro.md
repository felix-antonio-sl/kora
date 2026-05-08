---
_manifest:
  urn: "urn:kora:kb:bundle-deep-opm-pro"
  type: kb
  provenance:
    created_by: "FS"
    created_at: "2026-05-08"
    source: "Derivado de ~/projects/deep-opm-pro/app/src/serializacion/json.ts y app/src/modelo/tipos/* al 2026-05-08."
version: "1.0.0"
status: activo
nombre: bundle-deep-opm-pro
descripcion: "Contrato del bundle JSON 'deep-opm-pro.modelo.v0' que la skill modelamiento-opm emite para que el modelador deep-opm-pro lo importe."
tags: [opm, deep-opm-pro, contrato, json, importable]
lang: es
---

# Bundle deep-opm-pro — contrato de import

Documento JSON canonico que la skill `modelamiento-opm` emite cuando el destino es **edicion / refinamiento / revision** en el modelador `~/projects/deep-opm-pro/app/`.

> **SSOT del contrato**: el codigo del modelador. Si esta referencia tensiona con `app/src/serializacion/json.ts` o `app/src/modelo/tipos/*`, manda el codigo. Esta referencia es un resumen operativo curado.

## 1. Forma raiz

```json
{
  "formato": "deep-opm-pro.modelo.v0",
  "modelo": { /* Modelo */ },
  "carpetaId": "..."
}
```

- `formato`: literal exacto `"deep-opm-pro.modelo.v0"`. El detector de la app rechaza cualquier otro valor.
- `modelo`: objeto `Modelo` (ver §3).
- `carpetaId`: opcional, `string | null`. Solo lo usa el workspace local de la app; la skill puede omitirlo.

## 2. Reglas globales de emision

1. Identidades (`id`, `opdId`, `entidadId`, etc.) son strings cualquiera, no necesariamente UUIDs. Deben ser **internamente consistentes**: toda referencia debe resolver dentro del mismo modelo.
2. `nextSeq` de `Modelo` es un contador interno; emitir `0` o el numero de cosas + 1.
3. Toda apariencia visual (`Apariencia`, `AparienciaEnlace`) es opcional en sus campos no requeridos: si no hay certeza, **omitir**, no inventar. La app normaliza al hidratar.
4. Nombres de cosas son humanos y deben coincidir con los emitidos en OPL-ES y en el OPD.
5. No referenciar OPDs huerfanos: el OPD raiz es `opdRaizId` y todo OPD declarado debe ser alcanzable desde el (via `padreId`).
6. `validarReferenciasOpd` se aplica al hidratar: si una entidad referencia un OPD inexistente o un estado pertenece a una entidad ausente, el import falla con error legible.

## 3. Tipo `Modelo`

```ts
interface Modelo {
  id: string;
  nombre: string;
  descripcion?: string;
  opdRaizId: string;
  opds: Record<Id, Opd>;
  entidades: Record<Id, Entidad>;
  estados: Record<Id, Estado>;
  enlaces: Record<Id, Enlace>;
  abanicos?: Record<Id, Abanico>;
  archivado?: boolean;
  archivadoEn?: string;
  versiones?: VersionResumen[];
  crearVersionAlGuardar?: boolean;
  nextSeq: number;
}
```

## 4. Subtipos relevantes

### 4.1 Entidad

- `tipo: "objeto" | "proceso"`
- `esencia?: "informacional" | "fisica"` (default `"informacional"`)
- `afiliacion?: "sistemica" | "ambiental"` (default `"sistemica"`)
- `refinamientos?: { descomposicion?: { opdId, ... }, despliegue?: { opdId, modo? } }` — slots por tipo de refinamiento.
- Metadata extendida (`alias`, `unidad`, `descripcion`, `urls[]`, `valor`) opcional.

### 4.2 Estado

- `entidadId` obligatorio; debe apuntar a una `Entidad` tipo `"objeto"`.
- `nombre` humano, equivalente al usado en OPL-ES.
- `designaciones?: ("inicial" | "final" | "default" | "current")[]` — la app aplica exclusiones SSOT (no puede ser inicial+final, default es unico por entidad, etc.).
- `duracion?: { unidad, min, nominal, max }` — solo si la SSOT lo justifica.

### 4.3 Enlace

- `tipo` ∈ {`agregacion`, `exhibicion`, `generalizacion`, `clasificacion`, `agente`, `instrumento`, `consumo`, `resultado`, `efecto`, `invocacion`}
- `extremoOrigen`, `extremoDestino`: `{ kind: "entidad" | "estado", id }`. Los estructurales solo permiten `entidad-entidad`; los procedurales pueden involucrar estados segun la SSOT.
- `modificador?`, `subtipoModificador?` — opcionales; relevantes solo en procedurales.
- `multiplicidadOrigen?`, `multiplicidadDestino?` — strings cortos (e.g. `"1..n"`).
- `derivacion?`: marcado de enlaces externos derivados de refinamiento; emitir solo si el caso lo amerita.
- `estilo?: { color?, strokeWidth?, dashArray? }` — usar `tokens` del modelador, no inventar; preferible omitir.

### 4.4 OPD

- `padreId: Id | null` — `null` solo para el OPD raiz.
- `apariencias: Record<Id, Apariencia>` — un slot por entidad visible en este OPD (posicion + tamaño + estilo opcional).
- `enlaces: Record<Id, AparienciaEnlace>` — un slot por enlace visible (vertices, etiqueta, ruta).
- `ordenLocal?: number` — orden entre OPDs hermanos del mismo padre.

### 4.5 Apariencia y AparienciaEnlace

- `posicion: { x, y }` cuando se conoce; si no, **omitir** y dejar que el auto-layout de la app la asigne en `fit-to-view`.
- `tamaño: { ancho, alto }` opcional; el modelador usa 135x60 canonico cuando falta.
- `vertices`, `rutaEtiqueta`, `ordenPartes`, `modoPlegado`: especialistas — emitir solo cuando ya se exporto desde la propia app o se conoce con certeza.

### 4.6 Abanico

- Emitir solo si hay un `O`/`XOR` real entre enlaces que comparten puerto en una entidad de un OPD.
- `enlaceIds` debe listar enlaces ya declarados en `enlaces` y presentes en el OPD.

## 5. Errores comunes al importar

| Error | Causa | Fix en emision |
|--------|--------|-----------------|
| "JSON invalido" | parseo falla | revisar serializacion; usar `JSON.stringify(doc, null, 2)` |
| "formato no soportado" | `formato` distinto al literal | emitir exactamente `"deep-opm-pro.modelo.v0"` |
| "OPD raiz no existe" | `opdRaizId` no esta en `opds` | declarar el OPD raiz con `padreId: null` |
| "entidad referencia OPD inexistente" | refinamiento apunta a OPD no declarado | declarar el OPD destino antes de cerrar el bundle |
| "estado de entidad inexistente" | `entidadId` del estado roto | revisar consistencia |
| "extremo de enlace invalido" | `kind` o `id` incorrecto | re-validar con `validarFirmaEnlace` mental antes de emitir |
| "referencias OPD ciclicas" | refinement tree con ciclo | aplicar V-220/V-221 de `opd-es` |

## 6. Protocolo de uso desde la skill

1. Construir el `Modelo` en memoria respetando los tipos.
2. Aplicar `validar-modelo` antes de serializar; corregir bloqueos estructurales.
3. Serializar con `JSON.stringify(doc, null, 2)` (la app espera 2-space indentation por convencion, pero acepta cualquier whitespace valido).
4. Adjuntar el bundle al entregable y dar al usuario el camino de import: `cd ~/projects/deep-opm-pro/app && bun run dev` → UI → `Modelo / Importar JSON` → pegar.
5. Si la sesion ya tiene la app abierta y el bundle es chico, basta con copiar al portapapeles.

## 7. Cuando NO emitir bundle

- El destino es un documento estatico (markdown, PDF, lamina): preferir `serializar-opd` via jointjs-open-source.
- El usuario solo pide OPL-ES: emitir solo la serializacion textual.
- El modelo es solo conceptual y no se va a editar: documentar OPL + descripcion textual del OPD.

## 8. Ejemplo minimo

```json
{
  "formato": "deep-opm-pro.modelo.v0",
  "modelo": {
    "id": "modelo-cafetera",
    "nombre": "Cafetera domestica",
    "opdRaizId": "opd-sd",
    "opds": {
      "opd-sd": {
        "id": "opd-sd",
        "nombre": "SD",
        "padreId": null,
        "apariencias": {
          "ap-cafe-grano": { "entidadId": "ent-cafe-grano" },
          "ap-cafe-bebida": { "entidadId": "ent-cafe-bebida" },
          "ap-preparar": { "entidadId": "ent-preparar" }
        },
        "enlaces": {
          "ap-l1": { "enlaceId": "l1" },
          "ap-l2": { "enlaceId": "l2" }
        }
      }
    },
    "entidades": {
      "ent-cafe-grano": { "id": "ent-cafe-grano", "nombre": "Cafe en grano", "tipo": "objeto", "esencia": "fisica" },
      "ent-cafe-bebida": { "id": "ent-cafe-bebida", "nombre": "Cafe bebida", "tipo": "objeto", "esencia": "fisica" },
      "ent-preparar": { "id": "ent-preparar", "nombre": "Preparar", "tipo": "proceso" }
    },
    "estados": {},
    "enlaces": {
      "l1": { "id": "l1", "tipo": "consumo", "extremoOrigen": { "kind": "entidad", "id": "ent-cafe-grano" }, "extremoDestino": { "kind": "entidad", "id": "ent-preparar" } },
      "l2": { "id": "l2", "tipo": "resultado", "extremoOrigen": { "kind": "entidad", "id": "ent-preparar" }, "extremoDestino": { "kind": "entidad", "id": "ent-cafe-bebida" } }
    },
    "nextSeq": 4
  }
}
```

Este bundle es importable directo por el modelador y se renderiza con auto-layout sin necesidad de declarar posiciones.
