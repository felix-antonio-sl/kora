---
_manifest:
  urn: "urn:kora:skill:architect-kora-hub-operations:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-KORA-HUB-OPERATIONS

## Proposito

Guiar operaciones de gestion del Knowledge Hub KORA: URNs, manifiestos, directorios, aislamiento de namespaces, y operaciones CLI del catalogo.

## Procedimiento

1. Identificar operacion solicitada: crear URN | agregar KB | verificar manifiesto | configurar namespace | ejecutar CLI
2. Verificar formato URN: `urn:{namespace}:{type}:{id}` — namespace activo (kora|fxsl|gn|tde|orko|korvo|gov|legal|mgmt)
3. Verificar campos requeridos del manifiesto: `_manifest.urn`, `_manifest.type`, `version`, `status`, `lang`
4. Verificar aislamiento de namespace: KB debe residir en directorio correspondiente a su namespace
5. Para operaciones CLI: `kora index` (reconstruir catalogo) | `kora resolve` (URN → path) | `kora health` (URNs rotos) | `kora validate` | `kora stats`
6. Guiar al usuario paso a paso con ejemplos de manifiestos correctos en KORA/MD

## Output

Instrucciones paso a paso con ejemplos de manifiestos correctos, formato URN valido, y comandos CLI aplicables al caso del usuario.
