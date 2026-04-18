"""Validacion funcional de artefactos conformes a autoria-spec v1.0.

Marco categorial
----------------

Sea I = {habilidad, subagente, agente-propiamente-tal, agente-plataforma} el
conjunto indexador de formas materiales (atlas B).

Un artefacto es un morfismo  a: 1 -> Art  con proyeccion canonica
  forma : Art -> I,  a |-> extensions.kora.atlas.forma_material(a).

La validacion es el functor de requerimientos
  R : I -> List[Rule]
que asigna a cada forma la lista de reglas que sus artefactos deben
satisfacer. Mas las reglas UNIVERSALES (factorizadas por I -> 1).

Una Rule es un morfismo en la categoria de Kleisli del monad List[Diagnostic]:
  Rule  = Artifact -> Iterable[Diagnostic]
La composicion es concatenacion:  (r1 . r2)(a) = r1(a) ++ r2(a).

El schema JSON `schemas/kora-artefacto.json` captura la seccion universal
estructural (tipos, enums cerrados, regex URN). Este modulo captura la
fibra condicional (reglas que dependen de la forma material).

validate(a)  =  mconcat [ rule(a) | rule in UNIVERSAL_RULES ++ R(forma(a)) ]

Implementacion funcional
------------------------
- Sin clases mutables, sin acumuladores imperativos.
- Combinadores puros: `path`, `compose`, `when`, `require`, `forbid`, `in_set`.
- Diagnostic es NamedTuple inmutable.
- El catalogo FORM_RULES es un mapping inmutable (MappingProxyType).
"""

from __future__ import annotations

import re
from functools import reduce
from itertools import chain
from types import MappingProxyType
from typing import Any, Callable, Iterable, Mapping, NamedTuple, Tuple


# ---------------------------------------------------------------------------
# Objeto Diagnostico y alias
# ---------------------------------------------------------------------------

class Diagnostic(NamedTuple):
    severity: str   # "critical" | "high" | "medium" | "low"
    code: str       # estable, kebab-case
    path: str       # dotted path en el artefacto
    message: str


# Rule : Artifact -> Iterable[Diagnostic]
Rule = Callable[[Mapping[str, Any]], Iterable[Diagnostic]]

# Predicate : Artifact -> bool
Predicate = Callable[[Mapping[str, Any]], bool]


# ---------------------------------------------------------------------------
# Lens funcional (path acceder anidado sin mutacion)
# ---------------------------------------------------------------------------

def path(*keys: str) -> Callable[[Mapping[str, Any]], Any]:
    """Lens-like accessor: path('a','b','c')(d) == d['a']['b']['c'] o None."""
    def get(obj: Any) -> Any:
        return reduce(
            lambda acc, k: acc.get(k) if isinstance(acc, Mapping) else None,
            keys,
            obj,
        )
    return get


def dotted(*keys: str) -> str:
    return ".".join(keys)


# ---------------------------------------------------------------------------
# Monoide de reglas — composicion es concatenacion
# ---------------------------------------------------------------------------

def _empty(_art: Mapping[str, Any]) -> Iterable[Diagnostic]:
    return ()


def compose(*rules: Rule) -> Rule:
    """mconcat en la categoria de Kleisli del monad List[Diagnostic]."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        return chain.from_iterable(rule(art) for rule in rules)
    return run


def when(predicate: Predicate, rule: Rule) -> Rule:
    """Regla condicional: si el predicado es falso, descarta."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        return rule(art) if predicate(art) else ()
    return run


# ---------------------------------------------------------------------------
# Combinadores primitivos para construir reglas declarativamente
# ---------------------------------------------------------------------------

def require(
    lens: Callable[[Mapping[str, Any]], Any],
    *,
    code: str,
    severity: str,
    location: str,
    message: str,
) -> Rule:
    """Exige que el lens resuelva a algo distinto de None/vacio."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        value = lens(art)
        absent = value is None or (isinstance(value, (list, tuple, dict, str)) and len(value) == 0)
        return (Diagnostic(severity, code, location, message),) if absent else ()
    return run


def forbid(
    lens: Callable[[Mapping[str, Any]], Any],
    *,
    code: str,
    severity: str,
    location: str,
    message: str,
) -> Rule:
    """Prohibe que el lens resuelva a algo no-None."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        value = lens(art)
        return (Diagnostic(severity, code, location, message),) if value is not None else ()
    return run


def in_set(
    lens: Callable[[Mapping[str, Any]], Any],
    allowed: frozenset,
    *,
    code: str,
    severity: str,
    location: str,
    message_template: str = "valor fuera del conjunto permitido: {value!r}",
) -> Rule:
    """Exige que el valor (si existe) pertenezca al conjunto permitido."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        value = lens(art)
        if value is None:
            return ()
        if value not in allowed:
            return (Diagnostic(severity, code, location, message_template.format(value=value)),)
        return ()
    return run


def bound(
    lens: Callable[[Mapping[str, Any]], Any],
    lo: int,
    hi: int,
    *,
    code: str,
    severity: str,
    location: str,
    message_template: str = "valor {value} fuera de rango [{lo}, {hi}]",
) -> Rule:
    """Exige que el valor entero (si existe) este en [lo, hi]."""
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        value = lens(art)
        if value is None:
            return ()
        if not isinstance(value, int) or value < lo or value > hi:
            return (Diagnostic(severity, code, location, message_template.format(value=value, lo=lo, hi=hi)),)
        return ()
    return run


def regex_match(
    lens: Callable[[Mapping[str, Any]], Any],
    pattern: re.Pattern,
    *,
    code: str,
    severity: str,
    location: str,
    message: str,
) -> Rule:
    def run(art: Mapping[str, Any]) -> Iterable[Diagnostic]:
        value = lens(art)
        if value is None or (isinstance(value, str) and pattern.fullmatch(value)):
            return ()
        return (Diagnostic(severity, code, location, message),)
    return run


# ---------------------------------------------------------------------------
# Predicados factorizados
# ---------------------------------------------------------------------------

_URN_ARTEFACTO = re.compile(r"urn:[a-z][a-z0-9-]*:artefacto:[a-z][a-z0-9-]*")

forma_of: Callable[[Mapping[str, Any]], Any] = path(
    "extensions", "kora", "atlas", "forma_material"
)
arnes_of: Callable[[Mapping[str, Any]], Any] = path(
    "extensions", "kora", "atlas", "arnes_categorico"
)
vec_of: Callable[[Mapping[str, Any]], Any] = path(
    "extensions", "kora", "vector_ontologico"
)


def axis(axis_name: str) -> Callable[[Mapping[str, Any]], Any]:
    return path("extensions", "kora", "vector_ontologico", axis_name)


def has_any_platform_extension(art: Mapping[str, Any]) -> bool:
    extensions = art.get("extensions") if isinstance(art, Mapping) else None
    if not isinstance(extensions, Mapping):
        return False
    plat_keys = ("claude_code", "codex", "gemini", "mastra", "openclaw")
    return any(isinstance(extensions.get(k), Mapping) and extensions.get(k) for k in plat_keys)


# ---------------------------------------------------------------------------
# Reglas universales (factorizadas por I -> 1). Se evaluan en todo artefacto.
# Duplican parcialmente el schema JSON pero entregan diagnostics uniformes.
# ---------------------------------------------------------------------------

UNIVERSAL_RULES: Tuple[Rule, ...] = (
    require(
        path("_manifest", "urn"),
        code="envelope-urn-requerido",
        severity="critical",
        location="_manifest.urn",
        message="_manifest.urn es obligatorio (autoria-spec §3.1).",
    ),
    regex_match(
        path("_manifest", "urn"),
        _URN_ARTEFACTO,
        code="envelope-urn-formato",
        severity="critical",
        location="_manifest.urn",
        message="_manifest.urn debe cumplir urn:{ns}:artefacto:{id} (autoria-spec §10.1).",
    ),
    in_set(
        path("_manifest", "type"),
        frozenset({"artefacto"}),
        code="envelope-type-artefacto",
        severity="critical",
        location="_manifest.type",
        message_template="_manifest.type debe ser 'artefacto' (autoria-spec §3.1), no {value!r}.",
    ),
    require(
        path("nombre"),
        code="envelope-nombre-requerido",
        severity="high",
        location="nombre",
        message="Campo 'nombre' obligatorio (autoria-spec §3.1).",
    ),
    require(
        path("descripcion"),
        code="envelope-descripcion-requerida",
        severity="high",
        location="descripcion",
        message="Campo 'descripcion' obligatorio (autoria-spec §3.1).",
    ),
    in_set(
        path("status"),
        frozenset({"borrador", "activo", "publicado", "deprecado", "retirado"}),
        code="envelope-status-enum",
        severity="high",
        location="status",
        message_template="status={value!r} fuera del enum espanol (gobernanza §5).",
    ),
    in_set(
        forma_of,
        frozenset({"habilidad", "subagente", "agente-propiamente-tal", "agente-plataforma"}),
        code="atlas-forma-material-enum",
        severity="critical",
        location="extensions.kora.atlas.forma_material",
        message_template="forma_material={value!r} fuera del enum (autoria-spec §4.3).",
    ),
    in_set(
        arnes_of,
        frozenset({"utilidad", "disciplina", "delegado", "persona",
                   "orquestador", "servicio", "arquetipo"}),
        code="atlas-arnes-enum",
        severity="critical",
        location="extensions.kora.atlas.arnes_categorico",
        message_template="arnes_categorico={value!r} fuera del enum (autoria-spec §4.2).",
    ),
    # Vector ontologico — cada eje con su dominio.
    bound(axis("pi"), 0, 3,
          code="vector-pi-rango", severity="high",
          location="extensions.kora.vector_ontologico.pi"),
    bound(axis("mu"), 0, 3,
          code="vector-mu-rango", severity="high",
          location="extensions.kora.vector_ontologico.mu"),
    bound(axis("xi"), 0, 4,
          code="vector-xi-rango", severity="high",
          location="extensions.kora.vector_ontologico.xi"),
    bound(axis("lambda"), 0, 3,
          code="vector-lambda-rango", severity="high",
          location="extensions.kora.vector_ontologico.lambda"),
    bound(axis("phi"), 0, 4,
          code="vector-phi-rango", severity="high",
          location="extensions.kora.vector_ontologico.phi"),
)


# ---------------------------------------------------------------------------
# Catalogos de reglas condicionales por forma material (functor R: I -> Rules)
# ---------------------------------------------------------------------------

# Compartidas — las 4 formas requieren perfil + interfaz.
_SHARED_SHAPE_RULES: Tuple[Rule, ...] = (
    require(path("artefacto", "perfil"),
            code="shape-perfil-requerido", severity="high",
            location="artefacto.perfil",
            message="artefacto.perfil es obligatorio en toda forma material."),
    require(path("artefacto", "interfaz"),
            code="shape-interfaz-requerida", severity="high",
            location="artefacto.interfaz",
            message="artefacto.interfaz es obligatorio en toda forma material."),
)


_HABILIDAD_RULES: Tuple[Rule, ...] = (
    in_set(arnes_of,
           frozenset({"utilidad", "disciplina", "delegado"}),
           code="forma-habilidad-arnes",
           severity="high",
           location="extensions.kora.atlas.arnes_categorico",
           message_template="habilidad admite arnes {{utilidad, disciplina, delegado}}; recibido {value!r}."),
    require(path("extensions", "kora", "nivel_prescripcion"),
            code="forma-habilidad-nivel-prescripcion",
            severity="high",
            location="extensions.kora.nivel_prescripcion",
            message="habilidad requiere nivel_prescripcion (autoria-spec §6)."),
    bound(axis("pi"), 0, 2,
          code="forma-habilidad-pi-bound",
          severity="high",
          location="extensions.kora.vector_ontologico.pi",
          message_template="habilidad admite pi in [0,2]; recibido {value}."),
    bound(axis("mu"), 0, 1,
          code="forma-habilidad-mu-bound",
          severity="high",
          location="extensions.kora.vector_ontologico.mu",
          message_template="habilidad admite mu in [0,1]; recibido {value}."),
    forbid(path("artefacto", "contexto", "memoria_config"),
           code="forma-habilidad-memoria-prohibida",
           severity="high",
           location="artefacto.contexto.memoria_config",
           message="habilidad no puede declarar memoria_config (Mu<=1)."),
    forbid(path("artefacto", "composicion"),
           code="forma-habilidad-composicion-prohibida",
           severity="high",
           location="artefacto.composicion",
           message="habilidad no puede declarar composicion (sin sub-artefactos)."),
)


_SUBAGENTE_RULES: Tuple[Rule, ...] = (
    in_set(arnes_of,
           frozenset({"delegado", "persona"}),
           code="forma-subagente-arnes",
           severity="high",
           location="extensions.kora.atlas.arnes_categorico",
           message_template="subagente admite arnes {{delegado, persona}}; recibido {value!r}."),
    require(path("artefacto", "plan"),
            code="forma-subagente-plan-requerido", severity="high",
            location="artefacto.plan",
            message="subagente requiere artefacto.plan."),
    forbid(path("artefacto", "composicion"),
           code="forma-subagente-composicion-prohibida", severity="high",
           location="artefacto.composicion",
           message="subagente no puede declarar composicion."),
)


_AGENTE_PT_RULES: Tuple[Rule, ...] = (
    in_set(arnes_of,
           frozenset({"persona", "orquestador"}),
           code="forma-agente-pt-arnes",
           severity="high",
           location="extensions.kora.atlas.arnes_categorico",
           message_template="agente-propiamente-tal admite arnes {{persona, orquestador}}; recibido {value!r}."),
    require(path("artefacto", "plan"),
            code="forma-agente-pt-plan-requerido", severity="high",
            location="artefacto.plan",
            message="agente-propiamente-tal requiere artefacto.plan."),
    require(path("artefacto", "invariantes", "compromisos_eticos"),
            code="forma-agente-pt-compromisos-eticos",
            severity="high",
            location="artefacto.invariantes.compromisos_eticos",
            message="agente-propiamente-tal requiere compromisos_eticos (autoria-spec §6)."),
    # Condicional: xi == 4 -> composicion requerida
    when(
        lambda art: axis("xi")(art) == 4,
        require(path("artefacto", "composicion"),
                code="forma-agente-pt-composicion-si-xi4",
                severity="high",
                location="artefacto.composicion",
                message="artefacto con xi=4 requiere composicion (autoria-spec §6)."),
    ),
    # Condicional: mu >= 2 -> memoria_config requerida
    when(
        lambda art: isinstance(axis("mu")(art), int) and axis("mu")(art) >= 2,
        require(path("artefacto", "contexto", "memoria_config"),
                code="forma-agente-pt-memoria-si-mu2",
                severity="high",
                location="artefacto.contexto.memoria_config",
                message="artefacto con mu>=2 requiere memoria_config (autoria-spec §6)."),
    ),
)


_AGENTE_PLAT_RULES: Tuple[Rule, ...] = (
    in_set(arnes_of,
           frozenset({"orquestador", "servicio"}),
           code="forma-agente-plat-arnes",
           severity="high",
           location="extensions.kora.atlas.arnes_categorico",
           message_template="agente-plataforma admite arnes {{orquestador, servicio}}; recibido {value!r}."),
    in_set(axis("mu"),
           frozenset({3}),
           code="forma-agente-plat-mu-servicio",
           severity="high",
           location="extensions.kora.vector_ontologico.mu",
           message_template="agente-plataforma requiere mu=3 (materia ambiental); recibido {value}."),
    require(path("artefacto", "contexto", "memoria_config"),
            code="forma-agente-plat-memoria-requerida",
            severity="high",
            location="artefacto.contexto.memoria_config",
            message="agente-plataforma requiere memoria_config (autoria-spec §6)."),
    require(path("artefacto", "invariantes", "compromisos_eticos"),
            code="forma-agente-plat-compromisos-eticos",
            severity="high",
            location="artefacto.invariantes.compromisos_eticos",
            message="agente-plataforma requiere compromisos_eticos."),
    # extensions.{plataforma} at least one
    when(
        lambda art: not has_any_platform_extension(art),
        require(
            lambda art: None,  # siempre None -> siempre falla cuando el predicado es True
            code="forma-agente-plat-requiere-extension",
            severity="high",
            location="extensions.{plataforma}",
            message="agente-plataforma requiere al menos una extension de plataforma (claude_code|codex|gemini|mastra|openclaw).",
        ),
    ),
)


# ---------------------------------------------------------------------------
# Functor R : I -> Tuple[Rule, ...]
# ---------------------------------------------------------------------------

FORM_RULES: Mapping[str, Tuple[Rule, ...]] = MappingProxyType({
    "habilidad":              _SHARED_SHAPE_RULES + _HABILIDAD_RULES,
    "subagente":              _SHARED_SHAPE_RULES + _SUBAGENTE_RULES,
    "agente-propiamente-tal": _SHARED_SHAPE_RULES + _AGENTE_PT_RULES,
    "agente-plataforma":      _SHARED_SHAPE_RULES + _AGENTE_PLAT_RULES,
})


# ---------------------------------------------------------------------------
# API publica — pullback
# ---------------------------------------------------------------------------

def rules_for(artifact: Mapping[str, Any]) -> Tuple[Rule, ...]:
    """Pullback: retorna las reglas aplicables al artefacto segun su forma."""
    forma = forma_of(artifact)
    return UNIVERSAL_RULES + FORM_RULES.get(forma, ())


def validate(artifact: Mapping[str, Any]) -> Tuple[Diagnostic, ...]:
    """Evalua el artefacto como pullback sobre atlas.forma_material.

    Retorna tupla inmutable de diagnosticos.
    """
    return tuple(compose(*rules_for(artifact))(artifact))


def validate_many(artifacts: Iterable[Mapping[str, Any]]) -> Tuple[Diagnostic, ...]:
    """Validacion en paralelo sobre multiples artefactos, acumulando diagnostics."""
    return tuple(chain.from_iterable(validate(a) for a in artifacts))


__all__ = [
    "Diagnostic",
    "Rule",
    "UNIVERSAL_RULES",
    "FORM_RULES",
    "rules_for",
    "validate",
    "validate_many",
    "compose",
    "when",
    "path",
    "require",
    "forbid",
    "in_set",
    "bound",
    "regex_match",
]
