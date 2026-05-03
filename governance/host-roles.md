---
_manifest:
  urn: "urn:kora:kb:host-roles"
  provenance:
    created_by: "FS"
    created_at: "2026-05-03"
    source: "decision HITL: declarar el servidor Hetzner como SSOT operacional de KORA; clones en otras maquinas se comportan como replicas read-mostly; v1.1 agrega hook pre-push versionado y runbook de recuperacion"
version: "1.1.0"
status: publicado
tags: [gobernanza, identidad, hosts, ssot, operacional]
lang: es
extensions:
  kora:
    family: spec
relations:
  cites:
    - "urn:kora:kb:gobernanza"
---

# KORA/Host Roles v1.1.0

## 1. Definicion

Esta doctrina fija la **identidad operacional por maquina** del corpus KORA.
Distingue dos roles: `primary` y `secondary`. Solo existe **un** host
`primary` activo por instalacion del corpus; cualquier otra maquina con un
clon de este repositorio es `secondary` por defecto.

Esta doctrina NO modifica el canon ontologico ni de serializacion: regula la
operacion del filesystem como SSOT, la disciplina de push a `origin/master`,
y la forma en que el toolchain identifica al host.

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Host | Maquina concreta con un clon del repositorio KORA. |
| Primary | Host autoritativo para `master`. Puede pushear directamente. Es la SSOT operacional del corpus. |
| Secondary | Host replica. Trabaja en ramas feature, no pushea a `master` directamente, propone cambios via PR. |
| Marker de host | Archivo local fuera del repo (`~/.kora/host.yml`) que declara el rol del host actual. |
| Default | Si el marker no existe, el host se interpreta como `secondary`. |

## 3. Host primary canonico

A la fecha de canonizacion de esta doctrina:

| Campo | Valor |
|-------|-------|
| Hostname | `hetzner2897261` |
| Machine ID | `9976abf4e8f6428b9f28f26221dbcdce` |
| Sistema | Ubuntu 24.04 (Hetzner) |
| Operador | Felix (FS) |
| Declarado | 2026-05-03 |

Solo este host es `primary`. La transferencia de rol `primary` a otra maquina
es una decision HITL explicita que **DEBE** registrarse como nueva version de
esta doctrina (§7).

## 4. Reglas operacionales

### 4.1 Push a `origin/master`

1. Solo el host `primary` **DEBE** pushear directamente a `origin/master`.
2. Hosts `secondary` **NO DEBEN** ejecutar `git push origin master` ni
   equivalentes (`git push --force`, push a HEAD, etc.) sobre la rama
   protegida.
3. Hosts `secondary` **PUEDEN** crear ramas feature, pushear esas ramas a
   `origin` y abrir Pull Requests; el merge a `master` lo resuelve el host
   `primary`.

### 4.2 Estado vivo y artefactos derivados

1. `_BUILD/` por workspace, `docs/generated/`, sesiones, secretos y runtime
   en `~/.openclaw/` se consideran autoritativos solo en el host `primary`.
2. Hosts `secondary` **PUEDEN** regenerar derivados localmente (`kora index`,
   `kora sync-docs`, `kora transmute`) pero **NO DEBEN** considerar esos
   derivados como SSOT para el resto de la federacion.
3. La sincronizacion de runtime entre hosts queda **fuera del alcance** de
   esta doctrina y se documenta cuando exista.

### 4.3 Toolchain y verificacion

1. El toolchain `python3 toolchain/kora` **DEBE** poder leer el marker de
   host sin fallar si esta ausente; ausencia = `secondary`.
2. Comandos de mutacion potencialmente destructivos sobre el corpus
   (`migrate`, `promote`, `deprecate`) **PUEDEN** verificar el rol y advertir
   si se ejecutan en `secondary`.
3. El hook versionado `toolchain/git-hooks/pre-push` **DEBE** bloquear push
   directo a `origin/master` si el host no es `primary` o si el marker es
   inconsistente.
4. La instalacion local del hook se realiza con
   `python3 toolchain/kora install-hooks`, que configura
   `core.hooksPath=toolchain/git-hooks`.

## 5. Marker de host

El rol del host se declara en un archivo local fuera del repositorio:

- Path: `~/.kora/host.yml`
- Formato: YAML
- Versionado: NO (es estado de maquina, no de corpus)
- Default si ausente: `secondary`

Shape minimo:

```yaml
role: primary | secondary
hostname: "{hostname real}"
machine_id: "{contenido de /etc/machine-id}"
declared_at: "YYYY-MM-DD"
declared_by: "{operador}"
notes: "{texto libre}"
```

Reglas:

1. El campo `role` es obligatorio.
2. `hostname` y `machine_id` deben corresponder a la maquina real al momento
   de la lectura; divergencia indica que el marker fue copiado entre maquinas
   y **DEBE** corregirse antes de operar.
3. El marker no se sincroniza entre hosts. Cada maquina mantiene el suyo.

## 6. Enforcement

| Regla | Nivel |
|-------|-------|
| Default secondary si marker ausente | manual |
| Solo primary pushea a master | hook local + branch protection GitHub |
| Marker consistente con maquina real | manual |
| Derivados no autoritativos en secondary | manual |

Esta doctrina vive en nivel 5 de precedencia (§3 de `gobernanza.md`):
extension de namespace que estrecha la operacion sin relajar el canon.

## 7. Cambio de host primary

Transferir el rol `primary` a otra maquina **DEBE**:

1. Emitir nueva version de esta doctrina con la nueva identidad (`hostname`,
   `machine_id`, fecha, operador).
2. Actualizar `~/.kora/host.yml` en ambas maquinas: el nuevo `primary`
   declara `role: primary`; el anterior se rebaja a `secondary`.
3. Registrar la transicion como entrada en handoff bajo `docs/reports/`.
4. Ejecutar `python3 toolchain/kora host -v` en ambas maquinas y archivar la
   salida en el handoff de transferencia.
5. Ejecutar `python3 toolchain/kora install-hooks` en el nuevo `primary` y en
   cada `secondary` que vaya a pushear ramas feature.

No se admite cohabitacion de dos hosts `primary` simultaneos.

### 7.1 Runbook de recuperacion si el primary no esta disponible

Si `hetzner2897261` queda inaccesible y KORA debe seguir operando:

1. Pausar pushes directos a `master` hasta completar la promocion HITL de un
   reemplazo.
2. Elegir una maquina candidata con clon actualizado y ejecutar
   `git fetch --all --prune` seguido de `git pull --rebase origin master`.
3. Verificar estado local con `python3 toolchain/kora host -v`,
   `python3 toolchain/kora check --strict` y
   `python3 -m unittest discover -s tests`.
4. Crear o actualizar `~/.kora/host.yml` en la candidata con `role: primary`,
   `hostname` y `machine_id` reales.
5. Bajar el host anterior a `secondary` cuando vuelva a estar accesible; si no
   vuelve, dejar constancia explicita en el handoff.
6. Actualizar esta doctrina con version nueva, registrar el cambio en
   `docs/reports/`, regenerar indice si corresponde y pushear desde el nuevo
   primary.
7. Reinstalar hooks con `python3 toolchain/kora install-hooks` y confirmar que
   `git config core.hooksPath` apunta a `toolchain/git-hooks`.

## 8. Invariantes

1. Existe **a lo mas un** host `primary` por instalacion del corpus.
2. Los hosts `secondary` no son SSOT y sus derivados no obligan al `primary`.
3. La identidad operacional del host es **local**: no vive dentro del repo
   versionado, vive en el filesystem de la maquina.
4. Esta doctrina no altera precedencia constitucional; opera como extension
   de gobernanza.
