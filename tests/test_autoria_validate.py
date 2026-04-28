"""Tests para el schema universal + validador funcional de autoria-spec v1.2.

Cubre dos capas:

1. Schema JSON `schemas/kora-artefacto.json` — seccion universal estructural.
2. Modulo funcional `kora_lib.autoria_validate` — fibra condicional
   (functor R: I -> Rules sobre atlas.forma_material).

El diseno es categorial: UNIVERSAL_RULES son la seccion terminal I -> 1;
FORM_RULES[forma] es la fibra. validate(art) = mconcat(universal ++ fibra(forma)).
"""

import json
import unittest
from copy import deepcopy
from pathlib import Path

from common import ROOT  # noqa: F401 (inyecta scripts/ al sys.path)

import jsonschema
import yaml

from kora_lib.autoria_validate import (
    FORM_RULES,
    UNIVERSAL_RULES,
    Diagnostic,
    compose,
    forbid,
    path,
    require,
    rules_for,
    validate,
    when,
)


SCHEMA_PATH = ROOT / "serialization" / "schemas" / "kora-artefacto.json"


# ---------------------------------------------------------------------------
# Fixtures: artefactos minimos canonicos por forma material
# ---------------------------------------------------------------------------

def _base_envelope():
    return {
        "_manifest": {
            "urn": "urn:kora:artefacto:fix",
            "type": "artefacto",
            "provenance": {"created_by": "FS", "created_at": "2026-04-18"},
        },
        "version": "1.0.0",
        "status": "activo",
        "nombre": "fix",
        "descripcion": "fixture canonico",
        "lang": "es",
    }


def habilidad_valida():
    art = _base_envelope()
    art["extensions"] = {
        "kora": {
            "vector_ontologico": {"pi": 2, "mu": 0, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1, 1, 1, 1, 1]},
            "presentacion": "estado-primario",
            "atlas": {"arnes_categorico": "utilidad", "forma_material": "habilidad"},
            "entornos_objetivo": ["claude-code"],
            "nivel_prescripcion": "medio",
        },
    }
    art["artefacto"] = {"perfil": {"descripcion": "x"}, "interfaz": {"tools": ["Read"]}}
    return art


def subagente_valido():
    art = _base_envelope()
    art["extensions"] = {
        "kora": {
            "vector_ontologico": {"pi": 2, "mu": 1, "xi": 2, "lambda": 0, "phi": 1, "sigma": [1, 1, 1, 1, 1]},
            "presentacion": "estado-primario",
            "atlas": {"arnes_categorico": "delegado", "forma_material": "subagente"},
            "entornos_objetivo": ["claude-code"],
        },
    }
    art["artefacto"] = {
        "perfil": {"descripcion": "x"},
        "plan": {"estado_inicial": "S0", "estado_terminal": "S-END", "estados": []},
        "interfaz": {"tools": ["Read"]},
    }
    return art


def agente_pt_valido():
    art = _base_envelope()
    art["extensions"] = {
        "kora": {
            "vector_ontologico": {"pi": 2, "mu": 2, "xi": 2, "lambda": 0, "phi": 2, "sigma": [2, 1, 2, 2, 1]},
            "presentacion": "estado-primario",
            "atlas": {"arnes_categorico": "persona", "forma_material": "agente-propiamente-tal"},
            "entornos_objetivo": ["claude-code", "codex"],
        },
    }
    art["artefacto"] = {
        "perfil": {"descripcion": "x"},
        "plan": {"estado_inicial": "S0", "estado_terminal": "S-END", "estados": []},
        "interfaz": {"tools": ["Read"]},
        "contexto": {"memoria_config": {"backend": "fs"}},
        "invariantes": {"compromisos_eticos": ["respeto"]},
    }
    return art


def agente_plataforma_valido():
    art = _base_envelope()
    art["extensions"] = {
        "kora": {
            "vector_ontologico": {"pi": 2, "mu": 3, "xi": 3, "lambda": 1, "phi": 2, "sigma": [2, 1, 2, 2, 1]},
            "presentacion": "estado-primario",
            "atlas": {"arnes_categorico": "servicio", "forma_material": "agente-plataforma"},
            "entornos_objetivo": ["openclaw"],
        },
        "openclaw": {"bot_handler": "x"},
    }
    art["artefacto"] = {
        "perfil": {"descripcion": "x"},
        "plan": {"estado_inicial": "S0", "estado_terminal": "S-END", "estados": []},
        "interfaz": {"tools": ["Read"]},
        "contexto": {"memoria_config": {"backend": "fs"}},
        "invariantes": {"compromisos_eticos": ["respeto"]},
    }
    return art


# ---------------------------------------------------------------------------
# 1) Schema JSON — seccion universal
# ---------------------------------------------------------------------------

class TestSchemaUniversal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.validator = jsonschema.Draft202012Validator(cls.schema)

    def _errors(self, art):
        return sorted((e.message for e in self.validator.iter_errors(art)))

    def test_habilidad_valida_pasa_schema(self):
        self.assertEqual(self._errors(habilidad_valida()), [])

    def test_subagente_valido_pasa_schema(self):
        self.assertEqual(self._errors(subagente_valido()), [])

    def test_agente_pt_valido_pasa_schema(self):
        self.assertEqual(self._errors(agente_pt_valido()), [])

    def test_agente_plataforma_valido_pasa_schema(self):
        self.assertEqual(self._errors(agente_plataforma_valido()), [])

    def test_schema_rechaza_urn_agent_legacy(self):
        art = habilidad_valida()
        art["_manifest"]["urn"] = "urn:kora:agent:curator"
        errs = self._errors(art)
        self.assertTrue(any("urn" in e.lower() or "pattern" in e.lower() for e in errs), errs)

    def test_schema_rechaza_urn_skill_legacy(self):
        art = habilidad_valida()
        art["_manifest"]["urn"] = "urn:kora:skill:atomize:1.0.0"
        self.assertNotEqual(self._errors(art), [])

    def test_schema_rechaza_status_ingles(self):
        art = habilidad_valida()
        art["status"] = "active"
        self.assertNotEqual(self._errors(art), [])

    def test_schema_rechaza_forma_material_desconocida(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["atlas"]["forma_material"] = "agent-workspace"
        self.assertNotEqual(self._errors(art), [])

    def test_schema_rechaza_arnes_desconocido(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["atlas"]["arnes_categorico"] = "unknown"
        self.assertNotEqual(self._errors(art), [])

    def test_schema_rechaza_vector_fuera_de_rango(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["vector_ontologico"]["pi"] = 99
        self.assertNotEqual(self._errors(art), [])

    def test_schema_rechaza_manifest_type_no_artefacto(self):
        art = habilidad_valida()
        art["_manifest"]["type"] = "skill"
        self.assertNotEqual(self._errors(art), [])


# ---------------------------------------------------------------------------
# 2) Validador funcional — fibra condicional
# ---------------------------------------------------------------------------

class TestValidateUniversal(unittest.TestCase):
    def test_fixture_valida_cada_forma_pasa_universal(self):
        # Todas las fixtures son validas en la seccion universal.
        for fixture in (
            habilidad_valida(),
            subagente_valido(),
            agente_pt_valido(),
            agente_plataforma_valido(),
        ):
            self.assertEqual(validate(fixture), (), fixture["extensions"]["kora"]["atlas"]["forma_material"])

    def test_urn_legacy_genera_diagnostic(self):
        art = habilidad_valida()
        art["_manifest"]["urn"] = "urn:kora:agent:curator"
        diags = validate(art)
        codes = {d.code for d in diags}
        self.assertIn("envelope-urn-formato", codes)

    def test_vector_fuera_de_rango(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["vector_ontologico"]["pi"] = 9
        diags = validate(art)
        codes = {d.code for d in diags}
        self.assertIn("vector-pi-rango", codes)


class TestValidateFibraHabilidad(unittest.TestCase):
    def test_habilidad_sin_nivel_prescripcion(self):
        art = habilidad_valida()
        del art["extensions"]["kora"]["nivel_prescripcion"]
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-habilidad-nivel-prescripcion", codes)

    def test_habilidad_mu_fuera_de_dominio(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["vector_ontologico"]["mu"] = 2
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-habilidad-mu-bound", codes)

    def test_habilidad_con_composicion_prohibida(self):
        art = habilidad_valida()
        art["artefacto"]["composicion"] = {"sub_agentes": []}
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-habilidad-composicion-prohibida", codes)

    def test_habilidad_arnes_fuera_de_dominio(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["atlas"]["arnes_categorico"] = "persona"
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-habilidad-arnes", codes)


class TestValidateFibraAgentePT(unittest.TestCase):
    def test_requiere_compromisos_eticos(self):
        art = agente_pt_valido()
        del art["artefacto"]["invariantes"]["compromisos_eticos"]
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-agente-pt-compromisos-eticos", codes)

    def test_xi_4_requiere_composicion(self):
        art = agente_pt_valido()
        art["extensions"]["kora"]["vector_ontologico"]["xi"] = 4
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-agente-pt-composicion-si-xi4", codes)

    def test_mu_ge_2_requiere_memoria_config(self):
        art = agente_pt_valido()
        del art["artefacto"]["contexto"]["memoria_config"]
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-agente-pt-memoria-si-mu2", codes)


class TestValidateFibraAgentePlataforma(unittest.TestCase):
    def test_requiere_mu_3(self):
        art = agente_plataforma_valido()
        art["extensions"]["kora"]["vector_ontologico"]["mu"] = 2
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-agente-plat-mu-servicio", codes)

    def test_requiere_extension_plataforma(self):
        art = agente_plataforma_valido()
        del art["extensions"]["openclaw"]
        codes = {d.code for d in validate(art)}
        self.assertIn("forma-agente-plat-requiere-extension", codes)


# ---------------------------------------------------------------------------
# 3) Propiedades del monoide Rule — composicion asociativa, identity
# ---------------------------------------------------------------------------

class TestMonoideRules(unittest.TestCase):
    def setUp(self):
        self.art = habilidad_valida()

    def test_compose_es_asociativo(self):
        r1 = require(path("no_existe"), code="r1", severity="low", location="x", message="m")
        r2 = require(path("tampoco"), code="r2", severity="low", location="y", message="m")
        r3 = require(path("nada"), code="r3", severity="low", location="z", message="m")

        left = compose(compose(r1, r2), r3)
        right = compose(r1, compose(r2, r3))
        flat = compose(r1, r2, r3)

        self.assertEqual(tuple(left(self.art)), tuple(right(self.art)))
        self.assertEqual(tuple(left(self.art)), tuple(flat(self.art)))

    def test_identity_es_neutral(self):
        empty = compose()  # mconcat []
        r = require(path("no_existe"), code="r", severity="low", location="x", message="m")

        self.assertEqual(tuple(compose(empty, r)(self.art)), tuple(r(self.art)))
        self.assertEqual(tuple(compose(r, empty)(self.art)), tuple(r(self.art)))

    def test_empty_compose_yields_no_diagnostics(self):
        self.assertEqual(tuple(compose()(self.art)), ())


# ---------------------------------------------------------------------------
# 4) Pullback: rules_for proyecta segun forma_material
# ---------------------------------------------------------------------------

class TestPullback(unittest.TestCase):
    def test_rules_for_incluye_universales(self):
        rules = rules_for(habilidad_valida())
        self.assertGreaterEqual(len(rules), len(UNIVERSAL_RULES))
        for universal in UNIVERSAL_RULES:
            self.assertIn(universal, rules)

    def test_rules_for_proyecta_fibra_correcta(self):
        h_rules = set(rules_for(habilidad_valida()))
        s_rules = set(rules_for(subagente_valido()))
        diff_h = h_rules - set(UNIVERSAL_RULES)
        diff_s = s_rules - set(UNIVERSAL_RULES)
        # Las fibras son distintas (excepto las shared shape rules)
        self.assertNotEqual(diff_h, diff_s)

    def test_forma_desconocida_retorna_solo_universales(self):
        art = habilidad_valida()
        art["extensions"]["kora"]["atlas"]["forma_material"] = "desconocida"
        rules = rules_for(art)
        self.assertEqual(len(rules), len(UNIVERSAL_RULES))


# ---------------------------------------------------------------------------
# 5) Integracion: artefactos migrados por a-autoria pasan universal-check
# ---------------------------------------------------------------------------

class TestIntegrationConMigrate(unittest.TestCase):
    """El pipeline a-autoria + validate debe cerrar: lo que el migrator
    produce debe pasar la capa universal del validador (aun si a veces falla
    la fibra por shape deep no migrado)."""

    def test_migrated_artifact_manifest_shape_pasa_universal(self):
        import tempfile
        from kora_lib.artifacts import load_markdown_parts
        from kora_lib.migration import migrate_artifact_to_autoria

        fixture = """---
_manifest:
  urn: urn:kora:agent:sample
  provenance:
    created_by: FS
    created_at: '2026-04-18'
version: 1.0.0
name: Sample
description: fixture para integracion
status: active
lang: es
extensions:
  kora:
    harness_vector:
      pi: 2
      mu: 1
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 1, 1, 1]
    presentation: state-primary
    atlas:
      harness_name: discipline
      form: skill-standard
    skill_freedom: medium
    target_environments: [claude-code]
agent:
  coalgebra:
    description: x
  interface:
    tools: [Read]
---
cuerpo.
"""
        import shutil
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        p = tmp / "SKILL.md"
        p.write_text(fixture, encoding="utf-8")
        migrate_artifact_to_autoria(p)
        fm, _ = load_markdown_parts(p)

        diags = validate(fm)
        universal_codes = {d.code for d in diags if d.code.startswith("envelope-") or d.code.startswith("atlas-") or d.code.startswith("vector-")}
        self.assertEqual(universal_codes, set(), f"Universales deben pasar. Diagnostics: {diags}")


# ---------------------------------------------------------------------------
# 6) Check registrado en kora check
# ---------------------------------------------------------------------------

class TestAutoriaCheckRegistered(unittest.TestCase):
    """El check autoria-conformance esta registrado y conectado al validador."""

    def test_check_registered(self):
        from kora_lib.checks import get_check

        c = get_check("autoria-conformance")
        self.assertIsNotNone(c, "autoria-conformance no registrado")
        self.assertEqual(c.phase, "verify")
        self.assertEqual(c.severity, "high")
        self.assertEqual(c.enforcement, "schema")
        self.assertIn("catalog-exists", c.depends)

    def test_fix_registered(self):
        from kora_lib.checks import _FIXES

        self.assertIn("autoria-conformance", _FIXES,
                      "Fix no registrado como adjoint izquierdo del check.")

    def test_check_emits_diagnostics_on_legacy_corpus(self):
        """Sobre un AGENT.md legacy no migrado, el check debe emitir diagnostics."""
        from kora_lib.checks import _IMPLEMENTATIONS

        impl = _IMPLEMENTATIONS.get("autoria-conformance")
        self.assertIsNotNone(impl)
        diags = impl()
        codes = {d.message.split(" @ ")[0] for d in diags if d.check_id == "autoria-conformance"}
        if diags:
            self.assertTrue(
                any("envelope-urn-formato" in c or "envelope-status-enum" in c for c in codes),
                f"Diagnostics esperados sobre legacy shape no encontrados. Codes: {codes}",
            )


# ---------------------------------------------------------------------------
# 7) Propiedades categoriales de la adjuncion Check |- Fix
# ---------------------------------------------------------------------------

class TestAdjunctionCheckFix(unittest.TestCase):
    """Verifica propiedades categoriales de la adjuncion parcial:

        CheckRenames |- FixRenames   (migrate_to_autoria)
        CheckFibra   sin adjunto     (residual humano)

    Sobre un sandbox aislado (tmpdir con fixture legacy) para no tocar el
    corpus real; el fix se aplica a un AGENT.md individual.
    """

    RENAME_CODES = frozenset({
        "envelope-urn-formato",
        "envelope-type-artefacto",
        "envelope-nombre-requerido",
        "envelope-descripcion-requerida",
        "envelope-status-enum",
        "atlas-arnes-enum",
        "atlas-forma-material-enum",
    })

    # Fixture: agente-propiamente-tal legacy con fibra INTENCIONALMENTE
    # incompleta — sin compromisos_eticos, sin memoria_config (aunque mu>=2).
    # Estas carencias las detecta CheckFibra y NO las repara migrate_to_autoria
    # (requieren autor humano). Son el residual que demuestra que FixFibra no
    # existe como adjunto.
    LEGACY_FRONTMATTER = """---
_manifest:
  urn: urn:kora:agent:sample
  provenance:
    created_by: FS
    created_at: '2026-04-18'
version: 1.0.0
name: Sample
description: fixture legacy para adjuncion
status: active
lang: es
extensions:
  kora:
    harness_vector:
      pi: 2
      mu: 2
      xi: 2
      lambda: 0
      phi: 2
      sigma: [2, 1, 2, 2, 1]
    presentation: state-primary
    atlas:
      harness_name: person
      form: agent-workspace
    target_environments: [claude-code]
agent:
  coalgebra:
    description: x
  plan:
    initial_state: S0
    terminal_state: S-END
    states: []
  interface:
    tools: [Read]
---
cuerpo.
"""

    def _sandbox(self):
        import shutil
        import tempfile
        from kora_lib.artifacts import load_yaml_safe
        from kora_lib.migration import migrate_artifact_to_autoria

        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        p = tmp / "AGENT.md"
        p.write_text(self.LEGACY_FRONTMATTER, encoding="utf-8")

        def diagnose():
            fm, _ = load_yaml_safe(p)
            return tuple(validate(fm))

        def fix():
            # Invoca el mismo mecanismo que el adjoint: migrate en sitio.
            migrate_artifact_to_autoria(p)

        return p, diagnose, fix

    def test_idempotencia_fix(self):
        """fix . fix = fix — segunda aplicacion sin cambios observables."""
        p, diagnose, fix = self._sandbox()
        fix()
        snapshot_after_first = p.read_text(encoding="utf-8")
        fix()
        snapshot_after_second = p.read_text(encoding="utf-8")
        self.assertEqual(snapshot_after_first, snapshot_after_second,
                         "fix no es idempotente — segunda corrida altera el archivo.")

    def test_reduccion_rename_diagnostics(self):
        """diagnose . fix no contiene ningun code de la familia rename."""
        _, diagnose, fix = self._sandbox()
        before_codes = {d.code for d in diagnose()}
        self.assertTrue(
            before_codes & self.RENAME_CODES,
            f"Precondicion: legacy debe emitir rename codes. Vi: {before_codes}",
        )
        fix()
        after_codes = {d.code for d in diagnose()}
        residual_renames = after_codes & self.RENAME_CODES
        self.assertEqual(
            residual_renames, set(),
            f"Tras fix, no debe persistir ningun rename code. Residual: {residual_renames}",
        )

    def test_fibra_es_residual_humano(self):
        """Los diagnostics de fibra (no rename) sobreviven al fix — son residual."""
        _, diagnose, fix = self._sandbox()
        fix()
        after = diagnose()
        non_rename = {d.code for d in after if d.code not in self.RENAME_CODES}
        # La fixture es una habilidad sin 'artefacto.perfil' expandido: esperamos
        # al menos un diagnostic de fibra/shape sobreviviente.
        self.assertTrue(
            non_rename,
            "FixFibra no debe existir — diagnostics no-rename deben persistir.",
        )


if __name__ == "__main__":
    unittest.main()
