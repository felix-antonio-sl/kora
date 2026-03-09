import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import textwrap
import unittest
from unittest.mock import patch

from common import ROOT
import kora_lib.audit as audit_module
import kora_lib.validation as validation_module
from kora_lib.graph import GraphEdge
from kora_lib.validation import (
    build_formal_trace_targets,
    cmd_validate,
    formal_section_exists,
    validate_agents_canonical_structure,
    validate_agents_semantics,
    validate_config_semantics,
    validate_kb_pipeline_consistency,
    validate_skill_purity,
    validate_skill_tool_closure,
    validate_soul_semantics,
    validate_tools_semantics,
    validate_traces_semantics,
    validate_user_semantics,
)
from kora_lib.workspaces import fragment_exists, validate_skill_file


def write_bootstrap(path, urn, body):
    path.write_text(
        textwrap.dedent(
            f"""\
            ---
            _manifest:
              urn: "{urn}"
              type: bootstrap_agents
            version: 1.0.0
            status: published
            lang: es
            ---

            {body}
            """
        ),
        encoding="utf-8",
    )


class SemanticValidationTests(unittest.TestCase):
    def test_soul_semantics_flags_explicit_fsm_syntax(self):
        failures = validate_soul_semantics("STATE: S-DISPATCHER -> ACT: clasificar\n")
        self.assertIn("SOUL contiene leakage de behavior/state-machine", failures[0])

    def test_soul_semantics_ignores_state_names_in_narrative_examples(self):
        failures = validate_soul_semantics('Ejemplo: "dashboard" -> S-METRICAS.\n')
        self.assertEqual(failures, [])

    def test_user_semantics_flags_security_leak(self):
        failures = validate_user_semantics("Preferencias: sandbox strict\n")
        self.assertIn("USER contiene leakage de security o wiring", failures[0])

    def test_agents_semantics_flags_legacy_confidentiality(self):
        failures = validate_agents_semantics("- Confidentiality: block_instructions=true\n")
        self.assertIn("AGENTS contiene leakage de security/runtime", failures[0])

    def test_agents_canonical_structure_accepts_canonical_headings_with_suffixes(self):
        failures = validate_agents_canonical_structure(
            textwrap.dedent(
                """\
                ## 1. FSM (WF-TEST)
                texto
                ## 2. Reglas Duras
                texto
                ## 3. Co-induccion (Nodo Terminal)
                texto
                ## 4. Contexto Multi-turno
                texto
                ## 5. Wiring (W)
                texto
                """
            )
        )
        self.assertEqual(failures, [])

    def test_agents_canonical_structure_flags_missing_section(self):
        failures = validate_agents_canonical_structure(
            textwrap.dedent(
                """\
                ## 1. FSM
                ## 2. Reglas Duras
                ## 3. Co-induccion
                ## 5. Wiring
                """
            )
        )
        self.assertEqual(
            failures,
            ["AGENTS.md carece de seccion canonica '## 4. Contexto Multi-turno'"],
        )

    def test_agents_canonical_structure_flags_wrong_order(self):
        failures = validate_agents_canonical_structure(
            textwrap.dedent(
                """\
                ## 1. FSM
                ## 2. Reglas Duras
                ## 3. Co-induccion
                ## 5. Wiring
                ## 4. Contexto Multi-turno
                """
            )
        )
        self.assertEqual(
            failures,
            ["AGENTS.md viola el orden canonico FSM -> Reglas Duras -> Co-induccion -> Contexto Multi-turno -> Wiring"],
        )

    def test_agents_canonical_structure_flags_duplicate_section(self):
        failures = validate_agents_canonical_structure(
            textwrap.dedent(
                """\
                ## 1. FSM
                ## 2. Reglas Duras
                ## 2. Reglas Duras (extra)
                ## 3. Co-induccion
                ## 4. Contexto Multi-turno
                ## 5. Wiring
                """
            )
        )
        self.assertEqual(
            failures,
            ["AGENTS.md duplica seccion canonica '## 2. Reglas Duras'"],
        )

    def test_agents_canonical_structure_ignores_nominal_mentions(self):
        failures = validate_agents_canonical_structure(
            "Texto menciona ## 1. FSM y ## 5. Wiring pero no como headings reales.\n"
        )
        self.assertIn("AGENTS.md carece de seccion canonica '## 1. FSM'", failures)

    def test_skill_purity_flags_conversational_turn_control(self):
        failures = validate_skill_purity("Si ambiguedad: preguntar al usuario\n")
        self.assertIn("Skill contiene control conversacional no permitido", failures[0])

    def test_skill_purity_allows_structured_pending_state(self):
        failures = validate_skill_purity("Emitir gate_result.status = pending_approval hasta decision humana.\n")
        self.assertEqual(failures, [])

    def test_skill_tool_closure_flags_raw_cli_when_semantic_tool_exists(self):
        failures = validate_skill_tool_closure("1. Ejecutar `scripts/kora health`.\n", ["repo_health"])
        self.assertEqual(
            failures,
            ["Skill describe plumbing crudo en vez de la tool semantica 'repo_health'"],
        )

    def test_skill_tool_closure_flags_missing_semantic_tool_for_raw_cli(self):
        failures = validate_skill_tool_closure("1. Ejecutar `scripts/kora index`.\n", ["artifact_read"])
        self.assertEqual(
            failures,
            ["Skill requiere la tool semantica 'catalog_sync' pero no esta declarada en TOOLS.md"],
        )

    def test_tools_semantics_flags_runtime_permission_heading(self):
        content = "## filesystem_write\n- **Firma:** x\n"
        failures = validate_tools_semantics(content, ["filesystem_write"])
        self.assertIn("usa un permiso runtime crudo", failures[0])

    def test_tools_semantics_requires_semantic_markers(self):
        content = "## kb_route\nDescripcion sin markers\n"
        failures = validate_tools_semantics(content, ["kb_route"])
        self.assertEqual(failures, ["tool 'kb_route' carece de documentacion semantica canonica"])

    def test_tools_semantics_ignores_markers_inside_code_fence(self):
        content = "## kb_route\n```md\n- **Cuando usar:** solo ejemplo\n```\n"
        failures = validate_tools_semantics(content, ["kb_route"])
        self.assertEqual(failures, ["tool 'kb_route' carece de documentacion semantica canonica"])

    def test_kb_pipeline_consistency_flags_legacy_catalog_to_kb_route(self):
        failures = validate_kb_pipeline_consistency(["Fuente correcta via cadena catalog→kb_route"])
        self.assertEqual(failures, ["pipeline KB incompatible detectado: catalog -> kb_route"])

    def test_kb_pipeline_consistency_accepts_kb_route_to_catalog_resolve(self):
        failures = validate_kb_pipeline_consistency(["Fuente correcta via cadena kb_route→catalog_resolve"])
        self.assertEqual(failures, [])

    def test_formal_section_exists_for_real_section(self):
        targets = build_formal_trace_targets()
        self.assertTrue(formal_section_exists(targets["05"]["path"], "1.2"))

    def test_validate_traces_semantics_flags_missing_section_anchor(self):
        failures = validate_traces_semantics(ROOT / "specs" / "dummy.md", "Traces to: formal/05 (Bounded Lattice)\n")
        self.assertEqual(failures, ["Traces to carece de ancla de seccion formal"])

    def test_validate_traces_semantics_flags_fxsl_direct_support(self):
        failures = validate_traces_semantics(
            ROOT / "specs" / "dummy.md",
            "Traces to: formal/05 §1.2 (Bounded Lattice), knowledge/fxsl/cat/audit-patterns.md\n",
        )
        self.assertEqual(
            failures,
            ["Traces to referencia corpus FXSL auxiliar en vez de la formal layer oficial"],
        )

    def test_validate_traces_semantics_accepts_real_trace(self):
        failures = validate_traces_semantics(
            ROOT / "specs" / "dummy.md",
            "Traces to: formal/05 §1.2 (Bounded Lattice)\n",
        )
        self.assertEqual(failures, [])

    def test_validate_config_semantics_flags_runtime_overlap(self):
        config_data = {
            "tools": {"allow": ["kb_route"], "deny": []},
            "runtime_capabilities": {"allow": ["kb_route"], "deny": []},
        }
        failures = validate_config_semantics(config_data, ["kb_route"])
        self.assertEqual(
            failures,
            ["runtime_capabilities reintroduce interfaz semantica ['kb_route']"],
        )

    def test_fragment_exists_requires_real_anchor_not_body_coincidence(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.md"
            path.write_text("# Titulo\n\nTexto con foo en el cuerpo.\n", encoding="utf-8")
            self.assertFalse(fragment_exists(path, "foo"))

    def test_fragment_exists_accepts_explicit_id_anchor(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.md"
            path.write_text("Mision (ID: ANCLA_EXPLICITA): ejemplo.\n", encoding="utf-8")
            self.assertTrue(fragment_exists(path, "ANCLA_EXPLICITA"))

    def test_fragment_exists_accepts_table_anchor_in_first_cell(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.md"
            path.write_text("| TDE_DEF_SERVICIOS_DIGITALES | Servicios digitales |\n", encoding="utf-8")
            self.assertTrue(fragment_exists(path, "TDE_DEF_SERVICIOS_DIGITALES"))

    def test_validate_skill_file_requires_real_headings(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "CM-FAKE.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: urn:test:skill:fake:1.0.0
                    version: 1.0.0
                    status: published
                    lang: es
                    ---

                    Texto menciona ## Proposito, ## Input/Output, ## Procedimiento y ## Signature Output pero no son headings reales.
                    """
                ),
                encoding="utf-8",
            )
            failures = validate_skill_file(path)
            self.assertIn("missing required heading '## Proposito'", failures)

    def test_cmd_validate_strict_rejects_agents_with_noncanonical_section_order(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            skill_dir = workspace / "skills"
            skill_dir.mkdir(parents=True)
            (temp_root / "specs").mkdir()
            write_bootstrap(
                workspace / "AGENTS.md",
                "urn:test:agent-bootstrap:sample-agents:1.0.0",
                """
                # Sample Agent

                ## 1. FSM
                1. STATE: S-DISPATCHER -> ACT: Clasificar -> Trans: IF cerrar -> S-END.
                2. STATE: S-END -> ACT: Terminar. -> Trans: [terminal].

                ## 2. Reglas Duras
                - Allowed: Resolver KB
                - Forbidden: Ninguna
                - Rejection: "Fuera de scope"

                ## 3. Co-induccion
                - Checklist terminal

                ## 5. Wiring
                - Sin sub-agentes

                ## 4. Contexto Multi-turno
                - Mantener contexto minimo
                """,
            )
            write_bootstrap(
                workspace / "SOUL.md",
                "urn:test:agent-bootstrap:sample-soul:1.0.0",
                "# Sample Soul\n\nIdentidad y tono.\n",
            )
            write_bootstrap(
                workspace / "USER.md",
                "urn:test:agent-bootstrap:sample-user:1.0.0",
                "# Sample User\n\nContexto del operador.\n",
            )
            write_bootstrap(
                workspace / "TOOLS.md",
                "urn:test:agent-bootstrap:sample-tools:1.0.0",
                """
                # Sample Tools

                ## kb_route
                - **Firma:** urn: string -> path: string
                - **Cuando usar:** Resolver URNs del catalogo.
                - **Cuando NO usar:** Cuando no hay URN.
                """,
            )
            (workspace / "config.json").write_text(
                textwrap.dedent(
                    """\
                    {
                      "allowed_kb": ["urn:test:kb:sample"],
                      "tools": {"allow": ["kb_route"], "deny": []},
                      "runtime_capabilities": {"allow": [], "deny": []},
                      "sandbox": {"mode": "strict"},
                      "sub_agents": {"max_depth": 1, "max_concurrent": 1},
                      "limits": {},
                      "model_routing": {}
                    }
                    """
                ),
                encoding="utf-8",
            )
            write_bootstrap(
                skill_dir / "CM-SAMPLE.md",
                "urn:test:skill:sample-skill:1.0.0",
                """
                ## Proposito
                Resolver muestra.

                ## Input/Output
                - input: x
                - output: y

                ## Procedimiento
                1. Resolver.

                ## Signature Output
                {"status":"ok"}
                """,
            )

            output = io.StringIO()
            with patch.object(validation_module, "KORA_ROOT", temp_root), patch.object(
                validation_module,
                "iter_agent_workspaces",
                return_value=[workspace],
            ), redirect_stdout(output):
                with self.assertRaises(SystemExit):
                    cmd_validate(profile="strict")

            self.assertIn("viola el orden canonico", output.getvalue())

    def test_cmd_validate_strict_rejects_empty_config_json(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            workspace.mkdir(parents=True)
            (temp_root / "specs").mkdir()
            write_bootstrap(
                workspace / "AGENTS.md",
                "urn:test:agent-bootstrap:sample-agents:1.0.0",
                """
                # Sample Agent

                1. STATE: S-DISPATCHER -> ACT: Clasificar -> Trans: IF cerrar -> S-END.
                2. STATE: S-END -> ACT: Terminar. -> Trans: [terminal].

                ## 2. Reglas Duras
                - Allowed: Resolver KB
                - Forbidden: Ninguna
                - Rejection: "Fuera de scope"
                """,
            )
            write_bootstrap(
                workspace / "SOUL.md",
                "urn:test:agent-bootstrap:sample-soul:1.0.0",
                "# Sample Soul\n\nIdentidad y tono.\n",
            )
            write_bootstrap(
                workspace / "USER.md",
                "urn:test:agent-bootstrap:sample-user:1.0.0",
                "# Sample User\n\nContexto del operador.\n",
            )
            write_bootstrap(
                workspace / "TOOLS.md",
                "urn:test:agent-bootstrap:sample-tools:1.0.0",
                """
                # Sample Tools

                ## kb_route
                - **Firma:** urn: string -> path: string
                - **Cuando usar:** Resolver URNs del catalogo.
                - **Cuando NO usar:** Cuando no hay URN.
                """,
            )
            (workspace / "config.json").write_text("{}\n", encoding="utf-8")

            output = io.StringIO()
            with patch.object(validation_module, "KORA_ROOT", temp_root), patch.object(
                validation_module,
                "iter_agent_workspaces",
                return_value=[workspace],
            ), redirect_stdout(output):
                with self.assertRaises(SystemExit):
                    cmd_validate(profile="strict")

            self.assertIn("'allowed_kb' is a required property", output.getvalue())

    def test_cmd_health_rejects_legacy_agent_urn_not_in_catalog(self):
        source_path = ROOT / "agents" / "gn" / "dgi-virtual" / "AGENTS.md"
        fake_catalog = {
            "_manifest": {"urn": "urn:kora:catalog:master:2.0.0"},
            "Catalog": {
                "Agents": [],
                "Skills": [],
                "Knowledge": [],
                "Documents": [],
                "Other": [],
            },
        }
        output = io.StringIO()
        with patch.object(audit_module, "load_catalog", return_value=fake_catalog), patch.object(
            audit_module,
            "build_reference_graph",
            return_value=(1, [GraphEdge("XRef", source_path, "urn:gn:agent:ar-virtual")]),
        ), redirect_stdout(output):
            with self.assertRaises(SystemExit):
                audit_module.cmd_health(strict=True)

        self.assertIn("urn:gn:agent:ar-virtual", output.getvalue())


if __name__ == "__main__":
    unittest.main()
