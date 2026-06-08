"""Tests for the unified check pipeline and check algebra properties."""

import re
import shutil
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4
from unittest.mock import patch
from common import run_cli, ROOT
from kora_lib.graph import GraphEdge


class CheckPipelineSmokeTests(unittest.TestCase):
    """Smoke tests for kora check CLI command."""

    def test_check_runs_without_error(self):
        result = run_cli("check")
        self.assertIn("Checks run:", result.stdout)
        self.assertIn("Summary", result.stdout)

    def test_check_list_shows_all_checks(self):
        result = run_cli("check", "--list")
        self.assertIn("Check Registry", result.stdout)
        self.assertIn("catalog-exists", result.stdout)
        self.assertIn("urn-integrity", result.stdout)
        self.assertIn("knowledge-zone", result.stdout)
        self.assertIn("lint-md", result.stdout)
        self.assertIn("traces-requirements-semantics", result.stdout)
        self.assertIn("formal-trace-discipline", result.stdout)
        self.assertIn("autoria-conformance", result.stdout)
        self.assertIn("construction-source-primary", result.stdout)
        self.assertIn("construction-vector-fit", result.stdout)
        self.assertIn("construction-knowledge-explicit", result.stdout)
        self.assertIn("construction-authoring-shape", result.stdout)

    def test_check_strict_exit_status_matches_diagnostics(self):
        result = run_cli("check", "--strict", check=False)
        self.assertIn("Summary", result.stdout)
        match = re.search(r"Total diagnostics:\s+(\d+)", result.stdout)
        diagnostics = int(match.group(1)) if match else 0
        expected = 0 if diagnostics == 0 else 1
        self.assertEqual(result.returncode, expected, f"check --strict status mismatch:\n{result.stdout}\n{result.stderr}")

    def test_check_scope_filter(self):
        result = run_cli("check", "--scope", "repo")
        self.assertIn("Checks run:", result.stdout)

    def test_check_severity_filter(self):
        result = run_cli("check", "--severity", "critical")
        self.assertIn("Checks run:", result.stdout)

    def test_check_phase_filter(self):
        result = run_cli("check", "--phase", "verify")
        self.assertIn("Checks run:", result.stdout)

    def test_catalog_exists_fix_hint_uses_toolchain_entrypoint(self):
        from unittest.mock import patch
        from kora_lib.checks import _check_catalog_exists

        with patch("kora_lib.catalog.load_catalog", return_value=None):
            diags = _check_catalog_exists()

        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].path, "docs/generated/catalog.yml")
        self.assertEqual(diags[0].fix_hint, "python3 toolchain/kora index")

    def test_lint_md_fix_hint_uses_toolchain_entrypoint(self):
        from unittest.mock import patch
        from kora_lib.checks import _check_lint_md

        fake_issues = {"issues": [("artifacts/knowledge/kora/example.md", "mock lint failure")]}
        with patch("kora_lib.validation.lint_markdown_paths", return_value=fake_issues):
            diags = _check_lint_md()

        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].fix_hint, "python3 toolchain/kora lint-md --fix")

    def test_traces_requirements_semantics_rejects_non_requirement_targets(self):
        from kora_lib.checks import _check_traces_requirements_semantics

        nodes = [
            {
                "urn": "urn:kora:kb:trace-model",
                "file": "artifacts/knowledge/kora/sys/trace-model.md",
                "relations": {"traces_requirements": ["urn:kora:kb:not-a-requirement"]},
                "is_requirement": False,
            },
            {
                "urn": "urn:kora:kb:not-a-requirement",
                "file": "artifacts/knowledge/kora/sys/not-a-requirement.md",
                "relations": {},
                "is_requirement": False,
            },
        ]

        with patch("kora_lib.kb_graph.collect_knowledge_nodes", return_value=nodes):
            diags = _check_traces_requirements_semantics()

        self.assertEqual(len(diags), 1)
        self.assertIn("non-requirement node", diags[0].message)

    def test_construction_checks_reject_non_current_shape(self):
        from kora_lib.checks import _check_construction_authoring_shape, _check_construction_vector_fit

        artifact = (
            ROOT / "artifacts" / "agents" / "demo" / "draft" / "AGENT.md",
            "artifacts/agents/demo/draft/AGENT.md",
            {
                "_manifest": {"urn": "urn:kora:artefacto:draft"},
                "status": "activo",
                "agent": {},
                "extensions": {
                    "kora": {
                        "atlas": {"forma_material": "agente-propiamente-tal"},
                        "harness_vector": {"pi": 1, "mu": 1, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1]},
                        "vector_ontologico": {"pi": 1, "mu": 1, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1]},
                    }
                },
            },
        )

        with patch("kora_lib.checks._iter_construction_artifacts", return_value=[artifact]):
            shape_diags = _check_construction_authoring_shape()
            vector_diags = _check_construction_vector_fit()

        self.assertTrue(any("artefacto" in d.message for d in shape_diags))
        self.assertTrue(any("harness_vector" in d.message for d in vector_diags))

    def test_construction_knowledge_requires_urns(self):
        from kora_lib.checks import _check_construction_knowledge_explicit

        artifact = (
            ROOT / "artifacts" / "skills" / "demo" / "bad-kb" / "SKILL.md",
            "artifacts/skills/demo/bad-kb/SKILL.md",
            {
                "_manifest": {"urn": "urn:kora:artefacto:bad-kb"},
                "status": "activo",
                "extensions": {
                    "kora": {
                        "atlas": {"forma_material": "habilidad"},
                        "conocimiento_permitido": ["serialization/autoria-spec.md"],
                    }
                },
            },
        )

        with patch("kora_lib.checks._iter_construction_artifacts", return_value=[artifact]):
            diags = _check_construction_knowledge_explicit()

        self.assertEqual(len(diags), 1)
        self.assertIn("no-URN", diags[0].message)

    def test_construction_iter_skips_archived_staging_when_path_filtered(self):
        from kora_lib.checks import _iter_construction_artifacts

        rels = [rel for _path, rel, _frontmatter in _iter_construction_artifacts("artifacts/agents")]

        self.assertFalse(
            any("/_archivo/" in rel for rel in rels),
            "archived staging artifacts must not be treated as current construction sources",
        )


class CheckAlgebraTests(unittest.TestCase):
    """Tests for categorical properties of the check algebra."""

    def test_no_duplicate_check_ids(self):
        from kora_lib.checks import all_checks
        checks = all_checks()
        ids = [c.id for c in checks]
        self.assertEqual(len(ids), len(set(ids)), f"Duplicate check IDs: {[x for x in ids if ids.count(x) > 1]}")

    def test_dependency_dag_is_acyclic(self):
        from kora_lib.checks import all_checks
        checks = all_checks()
        check_ids = {c.id for c in checks}
        # All dependencies reference existing checks
        for c in checks:
            for dep in c.depends:
                self.assertIn(dep, check_ids, f"Check {c.id} depends on nonexistent check {dep}")
        # No cycles via DFS
        adj = {c.id: list(c.depends) for c in checks}
        visited = set()
        in_stack = set()
        def has_cycle(node):
            if node in in_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            in_stack.add(node)
            for dep in adj.get(node, []):
                if has_cycle(dep):
                    return True
            in_stack.discard(node)
            return False
        for c in checks:
            self.assertFalse(has_cycle(c.id), f"Cycle detected involving check {c.id}")

    def test_topo_sort_produces_valid_ordering(self):
        from kora_lib.checks import all_checks, _topo_sort
        checks = all_checks()
        ordered = _topo_sort(checks)
        ordered_ids = [c.id for c in ordered]
        # Every check appears exactly once
        self.assertEqual(sorted(ordered_ids), sorted(c.id for c in checks))
        # Every dependency comes before the check that depends on it
        for c in ordered:
            pos = ordered_ids.index(c.id)
            for dep in c.depends:
                dep_pos = ordered_ids.index(dep)
                self.assertLess(dep_pos, pos, f"Dependency {dep} appears after {c.id}")

    def test_every_check_has_implementation(self):
        from kora_lib.checks import all_checks, _IMPLEMENTATIONS
        for c in all_checks():
            self.assertIn(c.id, _IMPLEMENTATIONS, f"Check {c.id} has no implementation")

    def test_checks_with_fix_have_fix_registered(self):
        from kora_lib.checks import all_checks, _FIXES
        # At least catalog-exists and lint-md have fixes
        self.assertIn("catalog-exists", _FIXES)
        self.assertIn("lint-md", _FIXES)

    def test_minimum_check_count(self):
        from kora_lib.checks import all_checks
        self.assertGreaterEqual(len(all_checks()), 10)

    def test_all_severities_valid(self):
        from kora_lib.checks import all_checks
        valid = {"critical", "high", "medium", "low"}
        for c in all_checks():
            self.assertIn(c.severity, valid, f"Check {c.id} has invalid severity {c.severity}")

    def test_all_scopes_valid(self):
        from kora_lib.checks import all_checks
        valid = {"artifact", "workspace", "repo"}
        for c in all_checks():
            self.assertIn(c.scope, valid, f"Check {c.id} has invalid scope {c.scope}")

    def test_urn_integrity_flags_alias_to_retired_and_unknown(self):
        """Bootstrap aliases and retired URNs cited directly remain accepted;
        deprecated aliases that resolve to retired URNs are flagged HIGH so
        the catalog cannot quietly carry obsolete references."""
        from kora_lib.checks import _check_urn_integrity

        fake_doc = {"_manifest": {"urn": "urn:kora:catalog:master:2.0.0"}, "Catalog": {}}
        fake_known = {
            "urn:kora:catalog:master:2.0.0",
            "urn:kora:kb:autoria-spec",
            "urn:kora:kb:cat-governance-lattice",
        }
        fake_edges = [
            GraphEdge("XRef", ROOT / "artifacts" / "agents" / "kora" / "guardian" / "AGENT.md", "urn:kora:agent-bootstrap:guardian-user:1.0.0"),
            GraphEdge("XRef", ROOT / "artifacts" / "agents" / "kora" / "guardian" / "AGENT.md", "urn:kora:kb:agent-spec-md"),
            GraphEdge("XRef", ROOT / "serialization" / "autoria-spec.md", "urn:kora:kb:agentfile-spec"),
            GraphEdge("XRef", ROOT / "serialization" / "md-spec.md", "urn:kora:kb:05-governance-lattice"),
            GraphEdge("XRef", ROOT / "serialization" / "md-spec.md", "urn:kora:kb:definitely-missing"),
        ]

        with patch("kora_lib.catalog.load_catalog", return_value=fake_doc), patch(
            "kora_lib.catalog.build_catalog_lookup",
            return_value=(fake_known, {}),
        ), patch("kora_lib.graph.build_reference_graph", return_value=(1, fake_edges)):
            diags = _check_urn_integrity()

        messages = [d.message for d in diags]
        self.assertEqual(len(diags), 2, f"expected 2 diagnostics, got: {messages}")
        alias_diag = next(d for d in diags if "agent-spec-md" in d.message)
        self.assertIn("RETIRED", alias_diag.message)
        self.assertEqual(alias_diag.severity, "high")
        unknown_diag = next(d for d in diags if "definitely-missing" in d.message)
        self.assertEqual(unknown_diag.message, "Broken URN reference: urn:kora:kb:definitely-missing")


class KbGraphSmokeTests(unittest.TestCase):
    """Smoke tests for kb-graph command."""

    def test_kb_graph_runs(self):
        result = run_cli("kb-graph")
        self.assertIn("Knowledge Graph", result.stdout)

    def test_kb_graph_json_produces_file(self):
        result = run_cli("kb-graph", "--json")
        import json
        graph_path = ROOT / "docs" / "generated" / "kb-graph.json"
        self.assertTrue(graph_path.exists())
        data = json.loads(graph_path.read_text())
        self.assertIn("nodes", data)
        self.assertIn("edges", data)
        self.assertIn("stats", data)

    def test_kb_graph_check_cycles_passes(self):
        result = run_cli("kb-graph", "--check-cycles", check=False)
        self.assertEqual(result.returncode, 0)


class PromoteSmokeTests(unittest.TestCase):
    """Smoke tests for promote command."""

    def test_promote_rejects_nonexistent_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            nonexistent = Path(tmp) / "nonexistent.md"
            result = run_cli("promote", str(nonexistent), check=False)
            self.assertNotEqual(result.returncode, 0)

    def test_promote_rejects_file_outside_drafts(self):
        result = run_cli("promote", "KNOWLEDGE/kora/sys/pipeline-ingesta.md", check=False)
        self.assertNotEqual(result.returncode, 0)

    def test_promote_skill_review_to_productive_namespace(self):
        name = f"test-promote-skill-{uuid4().hex[:10]}"
        review_dir = ROOT / "artifacts" / "skills" / "_TALLER" / "REVIEW" / name
        productive_dir = ROOT / "artifacts" / "skills" / "test" / name
        try:
            review_dir.mkdir(parents=True)
            (review_dir / "SKILL.md").write_text(
                f"""---
_manifest:
  urn: "urn:test:artefacto:{name}"
  type: artefacto
  provenance:
    created_by: "test"
    created_at: "2026-05-04"
    source: "test fixture"
version: "0.1.0"
status: borrador
nombre: {name}
descripcion: "Skill fixture para probar promote desde _TALLER/REVIEW a productivo."
tags: [test, promote]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 1
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 1, 1, 0]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [agentskills]
    nivel_prescripcion: bajo
    conocimiento_permitido: []
artefacto:
  perfil:
    dominio: [test]
    disparadores:
      - "probar promote"
    salidas:
      - "fixture promovido"
  plan:
    estado_inicial: inicio
    estado_terminal: cierre
    estados: [inicio, cierre]
  interfaz:
    herramientas: [Read]
    permisos: "fixture"
    protocolos:
      entrada: "fixture"
      salida: "fixture"
  invariantes:
    reglas_duras:
      - "No usar fuera de tests."
---

# {name}

## Proposito

Fixture minima para verificar promocion de skills desde REVIEW.
""",
                encoding="utf-8",
            )

            result = run_cli("promote", str(review_dir / "SKILL.md"), check=False)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            self.assertIn("PROMOTED:", result.stdout)
            self.assertFalse(review_dir.exists())
            promoted = productive_dir / "SKILL.md"
            self.assertTrue(promoted.exists(), promoted)
            self.assertIn("status: activo", promoted.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(review_dir, ignore_errors=True)
            shutil.rmtree(productive_dir, ignore_errors=True)


class TestRelationsLaws(unittest.TestCase):
    """Verifica leyes algebraicas declaradas en knowledge-spec §6.3."""

    def test_find_cycles_detects_supersedes_cycle(self):
        from kora_lib.checks import _find_cycles

        edges = [
            ("urn:kora:kb:a", "urn:kora:kb:b", "fa"),
            ("urn:kora:kb:b", "urn:kora:kb:c", "fb"),
            ("urn:kora:kb:c", "urn:kora:kb:a", "fc"),
        ]
        cycles = _find_cycles(edges)
        self.assertEqual(cycles, {"urn:kora:kb:a", "urn:kora:kb:b", "urn:kora:kb:c"})

    def test_find_cycles_returns_empty_on_dag(self):
        from kora_lib.checks import _find_cycles

        edges = [
            ("urn:kora:kb:a", "urn:kora:kb:b", "fa"),
            ("urn:kora:kb:b", "urn:kora:kb:c", "fb"),
            ("urn:kora:kb:a", "urn:kora:kb:c", "fac"),
        ]
        self.assertEqual(_find_cycles(edges), set())

    def test_check_detects_supersedes_antisymmetry_violation(self):
        from kora_lib.checks import _check_relations_laws

        # Fixture: supersedes bidireccional (viola antisimetria)
        fake_edges = [
            ("urn:kora:kb:x", "urn:kora:kb:y", "x.md"),
            ("urn:kora:kb:y", "urn:kora:kb:x", "y.md"),
        ]
        with patch(
            "kora_lib.checks._collect_relation_edges",
            side_effect=lambda rt: fake_edges if rt == "supersedes" else [],
        ):
            diags = _check_relations_laws()
        # Tanto ciclo como antisimetria deben dispararse
        antisym = [d for d in diags if "antisimetrica" in d.message]
        self.assertGreaterEqual(len(antisym), 1)
        self.assertEqual(antisym[0].severity, "high")

    def test_check_detects_refines_cycle(self):
        from kora_lib.checks import _check_relations_laws

        fake_edges = [
            ("urn:kora:kb:p", "urn:kora:kb:q", "p.md"),
            ("urn:kora:kb:q", "urn:kora:kb:p", "q.md"),
        ]
        with patch(
            "kora_lib.checks._collect_relation_edges",
            side_effect=lambda rt: fake_edges if rt == "refines" else [],
        ):
            diags = _check_relations_laws()
        refines_diags = [d for d in diags if "refines" in d.message]
        self.assertGreaterEqual(len(refines_diags), 1)


class VectorLawsTests(unittest.TestCase):
    """Regresion de la logica pura de las 5 leyes inter-eje (harness-spec §4.1).

    Antes vivia embebida en el recorrido de filesystem de `_check_vector_laws`
    sin test; `_vector_law_violations` la aisla para pinearla ley por ley.
    """

    def _codes(self, vector):
        from kora_lib.checks import _vector_law_violations
        return {code for code, _msg, _fix in _vector_law_violations(vector)}

    def test_clean_vector_has_no_violations(self):
        # pi=2 (<3), mu=1, xi=3 (!=4), lambda=1, phi=1 (<2), sigma todos>=2
        v = {"pi": 2, "mu": 1, "xi": 3, "lambda": 1, "phi": 1,
             "sigma": [2, 2, 2, 2, 2]}
        self.assertEqual(self._codes(v), set())

    def test_non_dict_vector_is_inert(self):
        from kora_lib.checks import _vector_law_violations
        self.assertEqual(_vector_law_violations(None), [])
        self.assertEqual(_vector_law_violations("(2,0,1)"), [])

    def test_L1_pi_requires_mu(self):
        self.assertIn("L1-pi-requiere-mu", self._codes({"pi": 3, "mu": 0}))
        self.assertNotIn("L1-pi-requiere-mu", self._codes({"pi": 3, "mu": 1}))

    def test_L2_xi_requires_lambda(self):
        self.assertIn("L2-xi-requiere-lambda", self._codes({"xi": 4, "lambda": 0}))
        self.assertNotIn("L2-xi-requiere-lambda", self._codes({"xi": 4, "lambda": 1}))
        # xi != 4 no dispara
        self.assertNotIn("L2-xi-requiere-lambda", self._codes({"xi": 3, "lambda": 0}))

    def test_L3_phi_requires_mu(self):
        self.assertIn("L3-phi-requiere-mu", self._codes({"phi": 2, "mu": 0}))
        self.assertNotIn("L3-phi-requiere-mu", self._codes({"phi": 2, "mu": 1}))

    def test_L4_accountability_requires_transparency(self):
        # sigma = [safety, fairness, transparency, accountability, sustainability]
        viola = {"sigma": [2, 2, 1, 2, 2]}   # accountability=2, transparency=1
        cumple = {"sigma": [2, 2, 2, 2, 2]}
        self.assertIn("L4-accountability-requiere-transparency", self._codes(viola))
        self.assertNotIn("L4-accountability-requiere-transparency", self._codes(cumple))

    def test_L5_society_requires_full_sigma(self):
        viola = {"lambda": 3, "sigma": [2, 2, 2, 2, 1]}  # un componente <2
        cumple = {"lambda": 3, "sigma": [2, 2, 2, 2, 2]}
        self.assertIn("L5-sociedad-requiere-sigma-completo", self._codes(viola))
        self.assertNotIn("L5-sociedad-requiere-sigma-completo", self._codes(cumple))

    def test_violations_carry_code_message_and_fix(self):
        from kora_lib.checks import _vector_law_violations
        out = _vector_law_violations({"pi": 3, "mu": 0})
        self.assertEqual(len(out), 1)
        code, msg, fix = out[0]
        self.assertTrue(code and msg and fix)


class RiskRegisterValidationTests(unittest.TestCase):
    """Mecaniza `risk-id-unique` y `risk-entry-shape` (risk-register-spec §6, §8).

    La spec §8 declaraba ambos "Enforcement: manual". El corpus productivo tiene
    `risk_register` en >10 agentes/skills, asi que un risk_id duplicado o un
    likelihood fuera de [0,1] pasaba los checks limpio.

    Diseno fiel-a-data: los campos numericos (likelihood/impact/sigma_exposure/
    residual_sigma_floor) son OPCIONALES en el corpus real (fugaz/polymath solo
    declaran risk_id/category/trigger/mitigation/owner/status). El shape valida
    dominios SOLO si el campo esta presente; el unico campo minimo es risk_id.
    """

    # --- risk-id-unique (§6.2) ---
    def _id_codes(self, entries):
        from kora_lib.checks import _risk_id_uniqueness_violations
        return {code for code, _m, _f in _risk_id_uniqueness_violations(entries)}

    def test_unique_ids_have_no_violation(self):
        self.assertEqual(self._id_codes([{"risk_id": "a"}, {"risk_id": "b"}]), set())

    def test_duplicate_id_is_flagged(self):
        self.assertIn("risk-id-duplicado", self._id_codes([{"risk_id": "d"}, {"risk_id": "d"}]))

    def test_empty_or_absent_register_is_inert(self):
        from kora_lib.checks import _risk_id_uniqueness_violations
        self.assertEqual(_risk_id_uniqueness_violations([]), [])
        self.assertEqual(_risk_id_uniqueness_violations(None), [])

    # --- risk-entry-shape (§3, §6.3-§6.4) ---
    def _shape_codes(self, entries):
        from kora_lib.checks import _risk_entry_shape_violations
        return {code for code, _m, _f in _risk_entry_shape_violations(entries)}

    def test_minimal_real_entry_passes(self):
        # Forma real del corpus (fugaz/polymath): solo campos cualitativos.
        entry = {"risk_id": "fg-scope-creep", "category": "quality",
                 "trigger": "x", "mitigation": "y", "owner": "agente",
                 "status": "mitigated"}
        self.assertEqual(self._shape_codes([entry]), set())

    def test_full_canonical_entry_passes(self):
        # Ejemplo canonico de risk-register-spec §5.
        entry = {"risk_id": "qa-fallback-01", "category": "quality",
                 "likelihood": 0.35, "impact": 0.40,
                 "sigma_exposure": [0.0, 0.0, 0.1, 0.2, 0.0],
                 "residual_sigma_floor": [0.67, 0.33, 0.67, 0.67, 0.33],
                 "owner": "runtime", "status": "mitigated"}
        self.assertEqual(self._shape_codes([entry]), set())

    def test_missing_risk_id_is_flagged(self):
        self.assertIn("risk-entry-sin-id", self._shape_codes([{"category": "quality"}]))

    def test_likelihood_out_of_range_is_flagged(self):
        self.assertIn("risk-entry-likelihood-fuera-de-rango",
                      self._shape_codes([{"risk_id": "a", "likelihood": 1.5}]))

    def test_impact_negative_is_flagged(self):
        self.assertIn("risk-entry-impact-fuera-de-rango",
                      self._shape_codes([{"risk_id": "a", "impact": -0.1}]))

    def test_boolean_likelihood_is_flagged(self):
        # True es int en Python; un booleano no es una probabilidad valida.
        self.assertIn("risk-entry-likelihood-fuera-de-rango",
                      self._shape_codes([{"risk_id": "a", "likelihood": True}]))

    def test_sigma_wrong_length_is_flagged(self):
        self.assertIn("risk-entry-sigma_exposure-malformado",
                      self._shape_codes([{"risk_id": "a", "sigma_exposure": [0.1, 0.2, 0.3, 0.4]}]))

    def test_sigma_out_of_domain_is_flagged(self):
        self.assertIn("risk-entry-residual_sigma_floor-malformado",
                      self._shape_codes([{"risk_id": "a",
                                          "residual_sigma_floor": [0.1, 0.2, 0.3, 0.4, 1.7]}]))

    def test_non_mapping_entry_is_flagged(self):
        self.assertIn("risk-entry-no-mapping", self._shape_codes(["soy un string"]))

    def test_violations_carry_code_message_and_fix(self):
        from kora_lib.checks import _risk_entry_shape_violations
        out = _risk_entry_shape_violations([{"risk_id": "a", "likelihood": 2}])
        self.assertTrue(out and all(len(t) == 3 and all(t) for t in out))

    # --- registro + corrida limpia sobre el repo vigente ---
    def test_checks_registered_as_high(self):
        from kora_lib.checks import get_check
        for cid in ("risk-id-unique", "risk-entry-shape"):
            c = get_check(cid)
            self.assertIsNotNone(c, f"{cid} no registrado")
            self.assertEqual(c.severity, "high")

    def test_real_corpus_passes_both_checks(self):
        # Anti-falso-positivo: el corpus productivo vigente debe pasar limpio.
        from kora_lib.checks import _check_risk_id_unique, _check_risk_entry_shape
        self.assertEqual(_check_risk_id_unique(), [])
        self.assertEqual(_check_risk_entry_shape(), [])


class CoalgebraConformanceTests(unittest.TestCase):
    """Regresion de los nucleos coalgebraicos puros: termination y cierre.

    `coalgebra-conformance` verificaba un FSM pero su logica no tenia test;
    `_fsm_trapped_states` y `_subcoalgebra_escapes` la aislan.
    """

    def test_terminating_fsm_has_no_trapped_states(self):
        from kora_lib.checks import _fsm_trapped_states
        # a -> b -> c (terminal)
        trapped = _fsm_trapped_states("a", ["c"], {"a": ["b"], "b": ["c"]})
        self.assertEqual(trapped, [])

    def test_self_loop_with_exit_terminates(self):
        from kora_lib.checks import _fsm_trapped_states
        # a -> {a, c}: el self-loop no atrapa porque existe salida a terminal
        trapped = _fsm_trapped_states("a", ["c"], {"a": ["a", "c"]})
        self.assertEqual(trapped, [])

    def test_sink_cycle_without_terminal_is_trapped(self):
        from kora_lib.checks import _fsm_trapped_states
        # a -> b -> b: ninguna orbita alcanza c; ambos quedan atrapados
        trapped = set(_fsm_trapped_states("a", ["c"], {"a": ["b"], "b": ["b"]}))
        self.assertEqual(trapped, {"a", "b"})

    def test_closed_subcoalgebra_has_no_escapes(self):
        from kora_lib.checks import _subcoalgebra_escapes
        # {a, b} cierra bajo transiciones internas
        self.assertEqual(
            _subcoalgebra_escapes(["a", "b"], {"a": ["b"], "b": ["a"]}),
            [],
        )

    def test_escaping_transition_is_detected(self):
        from kora_lib.checks import _subcoalgebra_escapes
        # a sale de la sub-coalgebra hacia b (no incluido)
        escapes = _subcoalgebra_escapes(["a"], {"a": ["b"]})
        self.assertEqual(escapes, ["a -> b"])


if __name__ == "__main__":
    unittest.main()
