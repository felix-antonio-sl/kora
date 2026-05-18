"""Tests para el perfil `a-autoria` de `kora migrate`.

Cubre las reglas de `autoria-spec v1.2 §13`:
- URN rename de agent/skill -> artefacto (con extraccion de version embebida).
- `_manifest.type: artefacto`.
- Renames envelope: name->nombre, description->descripcion, status ingles->espanol.
- Renames overlay KORA: harness_vector->vector_ontologico, presentation->presentacion,
  skill_freedom->nivel_prescripcion, atlas.harness_name->atlas.arnes_categorico,
  atlas.form->atlas.forma_material (con slugs en espanol).
- Renames shape agent.*->artefacto.* con sub-renames profundos.
- Barrido de urn:kora:kb:spec-md -> urn:kora:kb:md-spec.
- Eliminacion de scaffolds legacy del workspace.
- Rename de subdirs (references/, assets/, memory/) al glosario espanol.
- Idempotencia: segunda corrida = sin cambios.
- Skiplist (SKILLS/kora/atomize/ no se toca).
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from common import ROOT  # noqa: F401 (inyecta scripts/ al sys.path)

import yaml

from kora_lib.artifacts import load_markdown_parts
from kora_lib.migration import (
    AUTORIA_MIGRATION_SKIPLIST,
    _autoria_rename_urn,
    _autoria_rewrite_urn_refs,
    _is_skipped_for_autoria,
    migrate_artifact_to_autoria,
    migrate_to_autoria,
)


AGENT_LEGACY_FRONTMATTER = """---
_manifest:
  urn: urn:kora:agent:curator
  provenance:
    created_by: FS
    created_at: '2026-04-14'
    source: legacy
version: 3.0.0
name: Curator
description: Curador legacy
status: active
tags: [test]
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
      relational_metaphor: control-panel
    allowed_knowledge:
      - urn:kora:kb:spec-md
      - urn:kora:kb:md-spec
    composable_with:
      - urn:kora:agent:custodio
agent:
  coalgebra:
    description: Curador del corpus
    domain: [curacion]
    triggers: [nuevo_artefacto]
    outputs: [artefacto]
    invariants: [fidelidad]
  plan:
    initial_state: S-INIT
    terminal_state: S-END
    states:
      - id: S-INIT
        act: Recibir
        transitions:
          - condition: ok
            target: S-END
            priority: 1
  interface:
    tools: [Read]
  context:
    identity: Curator
  invariants:
    hard_rules: [no_borrar_knowledge]
---

# Curator

Ver urn:kora:kb:spec-md para detalles.
"""


SKILL_LEGACY_FRONTMATTER = """---
_manifest:
  urn: urn:gn:skill:dgi-meyer:1.2.0
  type: lazy_load_endofunctor
name: dgi-meyer
description: Meyer principles
extensions:
  kora:
    harness_vector:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 1, 1, 1]
    presentation: state-primary
    skill_freedom: medium
    atlas:
      harness_name: discipline
      form: skill-standard
---

# dgi-meyer

Cuerpo.
"""


class TestUrnRename(unittest.TestCase):
    def test_rename_agent_urn(self):
        new, ver = _autoria_rename_urn("urn:kora:agent:curator")
        self.assertEqual(new, "urn:kora:artefacto:curator")
        self.assertIsNone(ver)

    def test_rename_skill_urn_extracts_version(self):
        new, ver = _autoria_rename_urn("urn:gn:skill:dgi-meyer:1.2.0")
        self.assertEqual(new, "urn:gn:artefacto:dgi-meyer")
        self.assertEqual(ver, "1.2.0")

    def test_rename_skill_urn_without_version(self):
        new, ver = _autoria_rename_urn("urn:kora:skill:atomize")
        self.assertEqual(new, "urn:kora:artefacto:atomize")
        self.assertIsNone(ver)

    def test_rewrite_sweeps_spec_md_and_urn_refs(self):
        value, changed = _autoria_rewrite_urn_refs(
            "ver urn:kora:kb:spec-md y urn:kora:agent:curator"
        )
        self.assertTrue(changed)
        self.assertIn("urn:kora:kb:md-spec", value)
        self.assertIn("urn:kora:artefacto:curator", value)
        self.assertNotIn("urn:kora:agent:", value)
        self.assertNotIn("urn:kora:kb:spec-md", value)

    def test_non_legacy_urn_unchanged(self):
        new, ver = _autoria_rename_urn("urn:kora:artefacto:curator")
        self.assertEqual(new, "urn:kora:artefacto:curator")
        self.assertIsNone(ver)


class TestAgentMigration(unittest.TestCase):
    def _write_and_migrate(self, content):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        path = tmp / "AGENT.md"
        path.write_text(content, encoding="utf-8")
        migrate_artifact_to_autoria(path)
        fm, body = load_markdown_parts(path)
        return fm, body, path

    def test_envelope_renames(self):
        fm, _, _ = self._write_and_migrate(AGENT_LEGACY_FRONTMATTER)
        self.assertEqual(fm["_manifest"]["urn"], "urn:kora:artefacto:curator")
        self.assertEqual(fm["_manifest"]["type"], "artefacto")
        self.assertEqual(fm["nombre"], "Curator")
        self.assertEqual(fm["descripcion"], "Curador legacy")
        self.assertEqual(fm["status"], "activo")
        self.assertNotIn("name", fm)
        self.assertNotIn("description", fm)

    def test_envelope_hoists_status_and_version_from_manifest(self):
        """Adjuncion Check ⊣ Fix: status/version dentro de _manifest se mueven a root.

        Cierra los codes `envelope-status-fuera-de-lugar` y
        `envelope-version-fuera-de-lugar` del validador.
        """
        from kora_lib.migration import _autoria_migrate_manifest

        # Caso A: ambos campos solo en _manifest, root vacio.
        fm_a = {
            "_manifest": {
                "urn": "urn:kora:artefacto:test-a",
                "type": "artefacto",
                "status": "activo",
                "version": "1.0.0",
            },
            "nombre": "test",
        }
        changed_a = _autoria_migrate_manifest(fm_a)
        self.assertTrue(changed_a)
        self.assertEqual(fm_a.get("status"), "activo")
        self.assertEqual(fm_a.get("version"), "1.0.0")
        self.assertNotIn("status", fm_a["_manifest"])
        self.assertNotIn("version", fm_a["_manifest"])

        # Caso B: conflicto root vs _manifest — root prevalece, _manifest se limpia.
        fm_b = {
            "_manifest": {
                "urn": "urn:kora:artefacto:test-b",
                "type": "artefacto",
                "version": "1.0.0",
            },
            "version": "2.0.0",
            "status": "activo",
        }
        _autoria_migrate_manifest(fm_b)
        self.assertEqual(fm_b["version"], "2.0.0")
        self.assertNotIn("version", fm_b["_manifest"])

        # Caso C: idempotencia. Segunda corrida no cambia nada.
        fm_c = dict(fm_a)
        fm_c["_manifest"] = dict(fm_a["_manifest"])
        changed_c = _autoria_migrate_manifest(fm_c)
        self.assertFalse(changed_c, "fix . fix = fix (idempotencia)")

    def test_envelope_hoist_reduces_validator_diagnostics(self):
        """Reduccion: diagnose . fix no contiene los codes envelope-*-fuera-de-lugar."""
        from kora_lib.autoria_validate import validate
        from kora_lib.migration import _autoria_migrate_manifest

        fm = {
            "_manifest": {
                "urn": "urn:kora:artefacto:reduc",
                "type": "artefacto",
                "status": "activo",
                "version": "1.0.0",
            },
            "nombre": "reduc",
            "descripcion": "test",
            "lang": "es",
            "extensions": {"kora": {
                "atlas": {"forma_material": "habilidad", "arnes_categorico": "utilidad"},
                "vector_ontologico": {"pi": 1, "mu": 0, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1,1,1,1,0]},
                "presentacion": "estado-primario",
                "entornos_objetivo": ["claude-code"],
                "nivel_prescripcion": "medio",
            }},
        }
        pre_codes = {d.code for d in validate(fm)}
        self.assertIn("envelope-status-fuera-de-lugar", pre_codes)
        self.assertIn("envelope-version-fuera-de-lugar", pre_codes)

        _autoria_migrate_manifest(fm)
        post_codes = {d.code for d in validate(fm)}
        self.assertNotIn("envelope-status-fuera-de-lugar", post_codes)
        self.assertNotIn("envelope-version-fuera-de-lugar", post_codes)
        self.assertNotIn("envelope-status-requerido", post_codes)
        self.assertNotIn("envelope-version-requerido", post_codes)

    def test_kora_overlay_renames(self):
        fm, _, _ = self._write_and_migrate(AGENT_LEGACY_FRONTMATTER)
        kora = fm["extensions"]["kora"]
        self.assertIn("vector_ontologico", kora)
        self.assertNotIn("harness_vector", kora)
        self.assertEqual(kora["presentacion"], "estado-primario")
        self.assertNotIn("presentation", kora)
        atlas = kora["atlas"]
        self.assertEqual(atlas["arnes_categorico"], "persona")
        self.assertEqual(atlas["forma_material"], "agente-propiamente-tal")
        self.assertEqual(atlas["metafora_relacional"], "centro-de-control")

    def test_kora_overlay_urn_lists_rewritten(self):
        fm, _, _ = self._write_and_migrate(AGENT_LEGACY_FRONTMATTER)
        kora = fm["extensions"]["kora"]
        self.assertIn("urn:kora:kb:md-spec", kora["conocimiento_permitido"])
        self.assertNotIn("urn:kora:kb:spec-md", kora["conocimiento_permitido"])
        self.assertEqual(kora["componible_con"], ["urn:kora:artefacto:custodio"])

    def test_shape_deep_renames(self):
        fm, _, _ = self._write_and_migrate(AGENT_LEGACY_FRONTMATTER)
        self.assertIn("artefacto", fm)
        self.assertNotIn("agent", fm)
        art = fm["artefacto"]
        # coalgebra -> perfil
        self.assertIn("perfil", art)
        self.assertEqual(art["perfil"]["descripcion"], "Curador del corpus")
        self.assertEqual(art["perfil"]["dominio"], ["curacion"])
        self.assertEqual(art["perfil"]["disparadores"], ["nuevo_artefacto"])
        # plan deep rename
        plan = art["plan"]
        self.assertEqual(plan["estado_inicial"], "S-INIT")
        self.assertEqual(plan["estado_terminal"], "S-END")
        estado0 = plan["estados"][0]
        self.assertIn("transiciones", estado0)
        self.assertEqual(estado0["accion"], "Recibir")
        trans0 = estado0["transiciones"][0]
        self.assertEqual(trans0["condicion"], "ok")
        self.assertEqual(trans0["destino"], "S-END")
        self.assertEqual(trans0["prioridad"], 1)
        # interface -> interfaz, context -> contexto, invariants -> invariantes
        self.assertIn("interfaz", art)
        self.assertIn("contexto", art)
        self.assertIn("invariantes", art)
        # coalgebra.invariants promovida a invariantes.reglas_duras
        self.assertIn("fidelidad", art["invariantes"]["reglas_duras"])

    def test_body_spec_md_barrido(self):
        _, body, _ = self._write_and_migrate(AGENT_LEGACY_FRONTMATTER)
        self.assertIn("urn:kora:kb:md-spec", body)
        self.assertNotIn("urn:kora:kb:spec-md", body)

    def test_idempotencia(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        path = tmp / "AGENT.md"
        path.write_text(AGENT_LEGACY_FRONTMATTER, encoding="utf-8")

        first = migrate_artifact_to_autoria(path)
        second = migrate_artifact_to_autoria(path)

        self.assertEqual(len(first), 1, "primera corrida debe cambiar el archivo")
        self.assertEqual(second, [], "segunda corrida debe ser no-op (idempotente)")


class TestSkillMigration(unittest.TestCase):
    def test_skill_urn_version_extraction(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        path = tmp / "SKILL.md"
        path.write_text(SKILL_LEGACY_FRONTMATTER, encoding="utf-8")
        migrate_artifact_to_autoria(path)
        fm, _ = load_markdown_parts(path)
        self.assertEqual(fm["_manifest"]["urn"], "urn:gn:artefacto:dgi-meyer")
        self.assertEqual(fm["_manifest"]["type"], "artefacto")
        self.assertEqual(fm["version"], "1.2.0")

    def test_skill_overlay_renames(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        path = tmp / "SKILL.md"
        path.write_text(SKILL_LEGACY_FRONTMATTER, encoding="utf-8")
        migrate_artifact_to_autoria(path)
        fm, _ = load_markdown_parts(path)
        kora = fm["extensions"]["kora"]
        self.assertEqual(kora["nivel_prescripcion"], "medio")
        self.assertNotIn("skill_freedom", kora)
        atlas = kora["atlas"]
        self.assertEqual(atlas["arnes_categorico"], "disciplina")
        self.assertEqual(atlas["forma_material"], "habilidad")


class TestWorkspaceScaffoldPurge(unittest.TestCase):
    def test_legacy_scaffolds_purged_and_subdirs_renamed(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)

        # Monta un workspace simulado
        (tmp / "AGENT.md").write_text(AGENT_LEGACY_FRONTMATTER, encoding="utf-8")
        for scaffold in ("SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md", "AGENTS.md", "config.json"):
            (tmp / scaffold).write_text("legacy", encoding="utf-8")
        (tmp / "references").mkdir()
        (tmp / "references" / "x.md").write_text("ref", encoding="utf-8")
        (tmp / "assets").mkdir()
        (tmp / "memory").mkdir()

        # Usa las funciones internas directamente (orquestacion sin discovery).
        from kora_lib.migration import (
            _autoria_purge_legacy_scaffolds,
            _autoria_rename_subdirs,
        )

        renamed = _autoria_rename_subdirs(tmp)
        self.assertTrue((tmp / "referencias").is_dir())
        self.assertFalse((tmp / "references").exists())
        self.assertTrue((tmp / "recursos").is_dir())
        self.assertTrue((tmp / "memoria").is_dir())
        self.assertEqual(len(renamed), 3)

        removed = _autoria_purge_legacy_scaffolds(tmp)
        self.assertGreaterEqual(len(removed), 6)
        for scaffold in ("SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md", "AGENTS.md", "config.json"):
            self.assertFalse((tmp / scaffold).exists(), f"{scaffold} deberia borrarse")
        self.assertTrue((tmp / "AGENT.md").exists(), "AGENT.md debe preservarse")


class TestSkiplist(unittest.TestCase):
    def test_atomize_is_skipped(self):
        self.assertIn("artifacts/skills/kora/atomize", AUTORIA_MIGRATION_SKIPLIST)
        self.assertIn("artifacts/skills/_TALLER/INBOX/atomize", AUTORIA_MIGRATION_SKIPLIST)
        from kora_lib.config import KORA_ROOT
        self.assertTrue(_is_skipped_for_autoria(KORA_ROOT / "artifacts/skills/kora/atomize"))
        self.assertTrue(_is_skipped_for_autoria(KORA_ROOT / "artifacts/skills/kora/atomize/SKILL.md"))
        self.assertTrue(_is_skipped_for_autoria(KORA_ROOT / "artifacts/skills/_TALLER/INBOX/atomize"))
        self.assertTrue(_is_skipped_for_autoria(KORA_ROOT / "artifacts/skills/_TALLER/INBOX/atomize/SKILL.md"))
        self.assertFalse(_is_skipped_for_autoria(KORA_ROOT / "artifacts/skills/kora/other"))

    def test_migrate_skips_atomize(self):
        paths = migrate_to_autoria(dry_run=True)
        for path in paths:
            self.assertNotIn("artifacts/skills/kora/atomize", str(path))
            self.assertNotIn("artifacts/skills/_TALLER/INBOX/atomize", str(path))


class TestRealCorpusDryRunIdempotency(unittest.TestCase):
    """Segunda corrida del dry-run sobre el corpus real debe ser estable
    (la primera corrida no mutua nada, y si re-ejecutamos da el mismo set)."""

    def test_dry_run_is_deterministic(self):
        first = sorted(str(p) for p in migrate_to_autoria(dry_run=True))
        second = sorted(str(p) for p in migrate_to_autoria(dry_run=True))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
