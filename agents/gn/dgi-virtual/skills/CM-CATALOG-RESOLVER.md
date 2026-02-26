---
_manifest:
  urn: "urn:gn:skill:dgi-virtual-catalog-resolver:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CATALOG-RESOLVER

## Proposito
Resolver URNs contra el catalogo KORA para obtener la ruta fisica de un KB antes de accederlo, garantizando que toda consulta KB use la fuente de verdad del catalogo.

## I/O

- **Input:** urn: string (URN del KB requerido segun tema de consulta)
- **Output:** path: string (ruta fisica resuelta del KB, o declaracion de incertidumbre)

## Procedimiento
1. Identificar el URN del KB requerido segun el tema de la consulta.
2. Invocar catalog_resolve(urn) para obtener el path fisico del archivo.
3. Verificar que el path retornado existe y corresponde al KB esperado.
4. Si catalog_resolve falla: registrar el fallo, intentar una vez mas, y si persiste declarar incertidumbre sobre la fuente KB.
5. Retornar el path resuelto para su uso en kb_route o lectura directa.
6. Nunca acceder a un KB sin haber resuelto previamente su URN via catalogo.

## Signature Output
Path fisico resuelto del KB solicitado, listo para acceso. En caso de fallo: declaracion de incertidumbre con URN intentado y accion alternativa propuesta.
