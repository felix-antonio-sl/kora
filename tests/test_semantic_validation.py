import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import textwrap
import unittest
from unittest.mock import patch

from common import AGENTS_ROOT, ROOT, run_cli
import kora_lib.audit as audit_module
from kora_lib.config import URN_REF_PATTERN
import kora_lib.validation as validation_module
from kora_lib.artifacts import dump_yaml_frontmatter_and_body
from kora_lib.graph import GraphEdge
from kora_lib.validation import (
    auto_fix_published_kora_markdown_parts,
    build_formal_trace_targets,
    cmd_validate,
    find_empty_primary_wrapper_headings,
    find_field_like_markdown_headings,
    find_html_fragments,
    find_meta_intro_headings,
    find_opaque_internal_refs,
    find_oversized_primary_chunks,
    split_kora_markdown_parts,
    find_truncated_markdown_headings,
    find_unverifiable_external_references,
    formal_section_exists,
    lint_published_kora_markdown,
    normalize_angle_bracket_urls,
    resolve_document_family,
    resolve_max_lines_per_h2,
    should_enforce_published_kora_markdown,
    validate_agents_canonical_structure,
    validate_agents_semantics,
    validate_coinduction_minimum,
    validate_config_semantics,
    validate_kb_pipeline_consistency,
    validate_multiturno_minimum,
    validate_skill_purity,
    validate_skill_tool_closure,
    validate_soul_canonical,
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
    def test_urn_ref_pattern_keeps_nested_kb_urns_intact(self):
        text = 'urn:kora:kb:tde:estrategias:estrategia-gobierno-digital-2030:1.0.0'
        self.assertEqual(URN_REF_PATTERN.findall(text), [text])

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

    # --- Co-induccion minima ---

    def test_coinduction_minimum_passes_with_all_three_checks(self):
        text = textwrap.dedent("""\
            ## 1. FSM
            ## 2. Reglas Duras
            ## 3. Co-induccion
            ### Checklist Pre-Output
            1. SCOPE_COMPLIANCE — dentro del dominio
            2. STATE_AWARENESS — coherente con FSM
            3. INTERFACE_DISCIPLINE — solo tools declaradas
            ### Protocolo de Correccion
            - IF SCOPE_COMPLIANCE fails -> rechazar
            ## 4. Contexto Multi-turno
            ## 5. Wiring
        """)
        failures = validate_coinduction_minimum(text)
        self.assertEqual(failures, [])

    def test_coinduction_minimum_flags_missing_scope_compliance(self):
        text = textwrap.dedent("""\
            ## 3. Co-induccion
            1. STATE_AWARENESS — coherente con FSM
            2. INTERFACE_DISCIPLINE — solo tools declaradas
            ## 4. Contexto Multi-turno
        """)
        failures = validate_coinduction_minimum(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("SCOPE_COMPLIANCE", failures[0])

    def test_coinduction_minimum_flags_all_three_missing(self):
        text = textwrap.dedent("""\
            ## 3. Co-induccion
            1. FOCUS — respondo lo que preguntaron?
            2. BULLSHIT_CHECK — jerga vacia?
            ## 4. Contexto Multi-turno
        """)
        failures = validate_coinduction_minimum(text)
        self.assertEqual(len(failures), 3)

    def test_coinduction_minimum_skips_when_section_absent(self):
        text = "## 1. FSM\n## 2. Reglas Duras\n"
        failures = validate_coinduction_minimum(text)
        self.assertEqual(failures, [])

    # --- Contexto Multi-turno minimo ---

    def test_multiturno_minimum_passes_with_all_keywords(self):
        text = textwrap.dedent("""\
            ## 4. Contexto Multi-turno
            - Detectar desvio de dominio comparando solicitud actual
            - IF cambio radical -> S-DISPATCHER
            - Retencion entre turnos: preservar estado activo del FSM
            ## 5. Wiring
        """)
        failures = validate_multiturno_minimum(text)
        self.assertEqual(failures, [])

    def test_multiturno_minimum_flags_missing_detection(self):
        text = textwrap.dedent("""\
            ## 4. Contexto Multi-turno
            - IF cambio -> S-DISPATCHER
            - Retencion: preservar estado
            ## 5. Wiring
        """)
        failures = validate_multiturno_minimum(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("deteccion", failures[0])

    def test_multiturno_minimum_flags_missing_action(self):
        text = textwrap.dedent("""\
            ## 4. Contexto Multi-turno
            - Detectar desvio de dominio
            - Retencion: preservar estado
            ## 5. Wiring
        """)
        failures = validate_multiturno_minimum(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("accion", failures[0])

    def test_multiturno_minimum_flags_missing_retention(self):
        text = textwrap.dedent("""\
            ## 4. Contexto Multi-turno
            - Detectar desvio de dominio
            - IF shift -> S-DISPATCHER
            ## 5. Wiring
        """)
        failures = validate_multiturno_minimum(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("retencion", failures[0])

    def test_multiturno_minimum_flags_all_three_missing(self):
        text = textwrap.dedent("""\
            ## 4. Contexto Multi-turno
            - TODO
            ## 5. Wiring
        """)
        failures = validate_multiturno_minimum(text)
        self.assertEqual(len(failures), 3)

    def test_multiturno_minimum_skips_when_section_absent(self):
        text = "## 1. FSM\n## 2. Reglas Duras\n"
        failures = validate_multiturno_minimum(text)
        self.assertEqual(failures, [])

    # --- SOUL.md canonico ---

    def test_soul_canonical_passes_with_canonical_headings(self):
        text = textwrap.dedent("""\
            ## Identidad Dialectica
            Guardian normativo.
            ## Paradigma Cognitivo
            Conservadurismo estructural.
            ## Tono
            Sobrio, preciso.
        """)
        failures = validate_soul_canonical(text)
        self.assertEqual(failures, [])

    def test_soul_canonical_passes_with_optional_voz(self):
        text = "## Identidad Dialectica\n## Paradigma Cognitivo\n## Tono\n## Voz\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(failures, [])

    def test_soul_canonical_flags_behavior_saludo(self):
        text = "## Identidad Dialectica\n## Tono\n## Saludo\nHola.\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("behavior", failures[0])
        self.assertIn("Saludo", failures[0])

    def test_soul_canonical_flags_behavior_estilo(self):
        text = "## Identidad Dialectica\n## Paradigma Cognitivo\n## Tono\n## Estilo Respuesta\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("behavior", failures[0])

    def test_soul_canonical_flags_behavior_ejemplos(self):
        text = "## Identidad Dialectica\n## Tono\n## Ejemplos Comportamiento\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("behavior", failures[0])

    def test_soul_canonical_flags_noncanonical_heading(self):
        text = "## Identidad Dialectica\n## Paradigma Cognitivo\n## Tono\n## Cosmovision\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("no canonica", failures[0])
        self.assertIn("Cosmovision", failures[0])

    def test_soul_canonical_flags_missing_paradigma_as_noncanonical(self):
        text = "## Identidad\n## Tono\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(len(failures), 1)
        self.assertIn("no canonica", failures[0])
        self.assertIn("Identidad", failures[0])

    def test_soul_canonical_ignores_h3_subheadings(self):
        text = "## Identidad Dialectica\n### Linaje\n## Paradigma Cognitivo\n### Ejes\n## Tono\n"
        failures = validate_soul_canonical(text)
        self.assertEqual(failures, [])

    # --- Bootstrap frontmatter (integration via validate_workspaces) ---

    def test_validate_strict_flags_bootstrap_extra_frontmatter(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            skill_dir = workspace / "skills"
            skill_dir.mkdir(parents=True)
            (temp_root / "specs").mkdir()
            write_bootstrap(workspace / "AGENTS.md", "urn:test:agent-bootstrap:sample-agents:1.0.0", textwrap.dedent("""\
                ## 1. FSM
                1. STATE: S-DISPATCHER -> ACT: Clasificar. -> Trans: IF x [prioridad 1] -> S-END.
                2. STATE: S-END -> ACT: Fin. -> Trans: [terminal].
                ## 2. Reglas Duras
                - Scope: REJECT_OUT_OF_SCOPE
                ## 3. Co-induccion
                ### Checklist Pre-Output
                1. SCOPE_COMPLIANCE — ok
                2. STATE_AWARENESS — ok
                3. INTERFACE_DISCIPLINE — ok
                ### Protocolo de Correccion
                - IF SCOPE_COMPLIANCE fails -> rechazar
                ## 4. Contexto Multi-turno
                - Deteccion de desvio: comparar solicitud
                - Accion: IF desvio -> S-DISPATCHER
                - Retencion: preservar estado entre turnos
                ## 5. Wiring
                - Tipo: raiz
            """))
            write_bootstrap(workspace / "SOUL.md", "urn:test:agent-bootstrap:sample-soul:1.0.0", "## Identidad Dialectica\nx\n## Paradigma Cognitivo\nx\n## Tono\nx\n")
            write_bootstrap(workspace / "USER.md", "urn:test:agent-bootstrap:sample-user:1.0.0", "## Perfil\nx\n")
            write_bootstrap(workspace / "TOOLS.md", "urn:test:agent-bootstrap:sample-tools:1.0.0", "")
            (workspace / "config.json").write_text('{"_manifest":{"urn":"x","type":"bootstrap_config"},"tools":{"allow":[]},"sandbox":{"mode":"strict"}}', encoding="utf-8")
            with patch.object(validation_module, "KORA_ROOT", temp_root), \
                 patch.object(validation_module, "iter_agent_workspaces", return_value=[workspace]):
                result = validation_module.validate_workspaces(profile="strict", emit=False)
            fm_issues = [i for i in result["issues"] if i["category"] == "bootstrap_frontmatter"]
            self.assertTrue(len(fm_issues) >= 1, f"Expected bootstrap_frontmatter issues, got: {[i['category'] for i in result['issues']]}")
            self.assertIn("version", fm_issues[0]["message"])

    # --- Skill naming SCREAMING_CASE (integration via validate_workspaces) ---

    def test_validate_strict_flags_lowercase_skill_name(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            skill_dir = workspace / "skills"
            skill_dir.mkdir(parents=True)
            (temp_root / "specs").mkdir()
            (workspace / "AGENTS.md").write_text("---\n_manifest:\n  urn: x\n  type: bootstrap_agents\n---\n## 1. FSM\n1. STATE: S-DISPATCHER -> ACT: CM-my-skill. -> Trans: IF x [prioridad 1] -> S-END.\n2. STATE: S-END -> ACT: Fin. -> Trans: [terminal].\n## 2. Reglas Duras\n- Scope: REJECT_OUT_OF_SCOPE\n## 3. Co-induccion\n### Checklist Pre-Output\n1. SCOPE_COMPLIANCE — ok\n2. STATE_AWARENESS — ok\n3. INTERFACE_DISCIPLINE — ok\n### Protocolo de Correccion\n- IF SCOPE_COMPLIANCE fails -> rechazar\n## 4. Contexto Multi-turno\n- Deteccion de desvio: comparar solicitud\n- Accion: IF desvio -> S-DISPATCHER\n- Retencion: preservar estado entre turnos\n## 5. Wiring\n- Tipo: raiz\n", encoding="utf-8")
            (workspace / "SOUL.md").write_text("---\n_manifest:\n  urn: x\n  type: bootstrap_soul\n---\n## Identidad Dialectica\nx\n## Paradigma Cognitivo\nx\n## Tono\nx\n", encoding="utf-8")
            (workspace / "USER.md").write_text("---\n_manifest:\n  urn: x\n  type: bootstrap_user\n---\n## Perfil\nx\n", encoding="utf-8")
            (workspace / "TOOLS.md").write_text("---\n_manifest:\n  urn: x\n  type: bootstrap_tools\n---\n", encoding="utf-8")
            (workspace / "config.json").write_text('{"_manifest":{"urn":"x","type":"bootstrap_config"},"tools":{"allow":[]},"sandbox":{"mode":"strict"}}', encoding="utf-8")
            (skill_dir / "CM-my-skill.md").write_text("---\n_manifest:\n  urn: x\n  type: lazy_load_endofunctor\n---\n## Proposito\nx\n## Input/Output\nx\n## Procedimiento\nx\n## Signature Output\nx\n", encoding="utf-8")
            with patch.object(validation_module, "KORA_ROOT", temp_root), \
                 patch.object(validation_module, "iter_agent_workspaces", return_value=[workspace]):
                result = validation_module.validate_workspaces(profile="strict", emit=False)
            naming_issues = [i for i in result["issues"] if i["category"] == "skill_naming"]
            self.assertEqual(len(naming_issues), 1)
            self.assertIn("CM-my-skill", naming_issues[0]["message"])
            self.assertIn("CM-MY-SKILL", naming_issues[0]["message"])

    def test_validate_workspaces_accepts_autoria_agent_md(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            workspace.mkdir(parents=True)
            schemas_dir = temp_root / "serialization" / "schemas"
            schemas_dir.mkdir(parents=True)
            (schemas_dir / "kora-artefacto.json").write_text(
                (ROOT / "serialization" / "schemas" / "kora-artefacto.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            frontmatter = {
                "_manifest": {
                    "urn": "urn:test:artefacto:sample",
                    "type": "artefacto",
                    "provenance": {
                        "created_by": "test",
                        "created_at": "2026-04-18",
                        "source": "fixture",
                    },
                },
                "version": "1.0.0",
                "status": "activo",
                "nombre": "Sample",
                "descripcion": "Cuando se necesita orientar un caso de prueba, Sample responde bajo autoria-spec.",
                "tags": ["sample"],
                "lang": "es",
                "extensions": {
                    "kora": {
                        "vector_ontologico": {"pi": 2, "mu": 1, "xi": 2, "lambda": 0, "phi": 2, "sigma": [2, 1, 2, 2, 1]},
                        "presentacion": "estado-primario",
                        "atlas": {"arnes_categorico": "persona", "forma_material": "agente-propiamente-tal"},
                        "entornos_objetivo": ["codex"],
                    }
                },
                "artefacto": {
                    "perfil": {
                        "dominio": ["pruebas"],
                        "disparadores": ["caso de validacion"],
                        "salidas": ["resultado"],
                    },
                    "plan": {
                        "estado_inicial": "S-DISPATCHER",
                        "estado_terminal": "S-END",
                        "estados": [{"id": "S-DISPATCHER", "accion": "clasificar"}, {"id": "S-END", "accion": "cerrar"}],
                    },
                    "interfaz": {"tools": [], "permissions": {"allow": [], "deny": []}},
                    "contexto": {"memory": {"mode": "session"}},
                    "invariantes": {
                        "reglas_duras": ["consistencia con dominio declarado"],
                        "compromisos_eticos": {
                            "safety_norm": "Alta; fixture no debe inducir dano.",
                            "fairness": "Media; aplica criterio uniforme.",
                            "transparency": "Alta; explicita supuestos.",
                            "accountability": "Alta; deja trazabilidad del caso.",
                            "sustainability": "Media; fixture simple y mantenible.",
                        },
                    },
                },
            }
            dump_yaml_frontmatter_and_body(workspace / "AGENT.md", frontmatter, "# Sample\n")
            with patch.object(validation_module, "KORA_ROOT", temp_root), \
                 patch.object(validation_module, "iter_agent_workspaces", return_value=[workspace]):
                result = validation_module.validate_workspaces(profile="strict", emit=False)
            self.assertTrue(result["ok"], result["issues"])
            self.assertEqual(result["workspace_invalid"], 0)
            self.assertEqual(result["issues"], [])
            self.assertEqual(result["bootstrap_validated"], 1)

    def test_validate_workspaces_flags_autoria_agent_missing_descripcion(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            workspace.mkdir(parents=True)
            schemas_dir = temp_root / "serialization" / "schemas"
            schemas_dir.mkdir(parents=True)
            (schemas_dir / "kora-artefacto.json").write_text(
                (ROOT / "serialization" / "schemas" / "kora-artefacto.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            frontmatter = {
                "_manifest": {
                    "urn": "urn:test:artefacto:sample",
                    "type": "artefacto",
                    "provenance": {
                        "created_by": "test",
                        "created_at": "2026-04-18",
                        "source": "fixture",
                    },
                },
                "version": "1.0.0",
                "status": "activo",
                "nombre": "Sample",
                "tags": ["sample"],
                "lang": "es",
                "extensions": {
                    "kora": {
                        "vector_ontologico": {"pi": 2, "mu": 1, "xi": 2, "lambda": 0, "phi": 2, "sigma": [2, 1, 2, 2, 1]},
                        "presentacion": "estado-primario",
                        "atlas": {"arnes_categorico": "persona", "forma_material": "agente-propiamente-tal"},
                        "entornos_objetivo": ["codex"],
                    }
                },
                "artefacto": {
                    "perfil": {
                        "dominio": ["pruebas"],
                        "disparadores": ["caso de validacion"],
                        "salidas": ["resultado"],
                    },
                    "plan": {
                        "estado_inicial": "S-DISPATCHER",
                        "estado_terminal": "S-END",
                        "estados": [{"id": "S-DISPATCHER", "accion": "clasificar"}, {"id": "S-END", "accion": "cerrar"}],
                    },
                    "interfaz": {"tools": [], "permissions": {"allow": [], "deny": []}},
                    "contexto": {"memory": {"mode": "session"}},
                    "invariantes": {
                        "reglas_duras": ["consistencia con dominio declarado"],
                        "compromisos_eticos": {
                            "safety_norm": "Alta; fixture no debe inducir dano.",
                            "fairness": "Media; aplica criterio uniforme.",
                            "transparency": "Alta; explicita supuestos.",
                            "accountability": "Alta; deja trazabilidad del caso.",
                            "sustainability": "Media; fixture simple y mantenible.",
                        },
                    },
                },
            }
            dump_yaml_frontmatter_and_body(workspace / "AGENT.md", frontmatter, "# Sample\n")
            with patch.object(validation_module, "KORA_ROOT", temp_root), \
                 patch.object(validation_module, "iter_agent_workspaces", return_value=[workspace]):
                result = validation_module.validate_workspaces(profile="strict", emit=False)
            categories = {issue["category"] for issue in result["issues"]}
            self.assertIn("envelope-descripcion-requerida", categories)
            self.assertFalse(result["ok"])

    def test_validate_workspaces_strict_fails_if_autoria_schema_missing(self):
        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            workspace = temp_root / "agents" / "test" / "sample"
            workspace.mkdir(parents=True)
            frontmatter = {
                "_manifest": {
                    "urn": "urn:test:artefacto:sample",
                    "type": "artefacto",
                    "provenance": {
                        "created_by": "test",
                        "created_at": "2026-04-18",
                        "source": "fixture",
                    },
                },
                "version": "1.0.0",
                "status": "activo",
                "nombre": "Sample",
                "descripcion": "Fixture valida salvo por schema ausente.",
                "tags": ["sample"],
                "lang": "es",
                "extensions": {
                    "kora": {
                        "vector_ontologico": {"pi": 2, "mu": 1, "xi": 2, "lambda": 0, "phi": 2, "sigma": [2, 1, 2, 2, 1]},
                        "presentacion": "estado-primario",
                        "atlas": {"arnes_categorico": "persona", "forma_material": "agente-propiamente-tal"},
                        "entornos_objetivo": ["codex"],
                    }
                },
                "artefacto": {
                    "perfil": {
                        "dominio": ["pruebas"],
                        "disparadores": ["caso de validacion"],
                        "salidas": ["resultado"],
                    },
                    "plan": {
                        "estado_inicial": "S-DISPATCHER",
                        "estado_terminal": "S-END",
                        "estados": [{"id": "S-DISPATCHER", "accion": "clasificar"}, {"id": "S-END", "accion": "cerrar"}],
                    },
                    "interfaz": {"tools": [], "permissions": {"allow": [], "deny": []}},
                    "contexto": {"memory": {"mode": "session"}},
                    "invariantes": {
                        "reglas_duras": ["consistencia con dominio declarado"],
                        "compromisos_eticos": {
                            "safety_norm": "Alta; fixture no debe inducir dano.",
                            "fairness": "Media; aplica criterio uniforme.",
                            "transparency": "Alta; explicita supuestos.",
                            "accountability": "Alta; deja trazabilidad del caso.",
                            "sustainability": "Media; fixture simple y mantenible.",
                        },
                    },
                },
            }
            dump_yaml_frontmatter_and_body(workspace / "AGENT.md", frontmatter, "# Sample\n")
            with patch.object(validation_module, "KORA_ROOT", temp_root), \
                 patch.object(validation_module, "iter_agent_workspaces", return_value=[workspace]):
                result = validation_module.validate_workspaces(profile="strict", emit=False)
            self.assertFalse(result["ok"])
            self.assertEqual(result["global_failures"], 1)
            self.assertIn("autoria_schema_missing", result["issue_counts"])

    def test_agentfile_dimensions_reads_autoria_dimensions(self):
        from kora_lib import config as config_module
        from kora_lib.checks import _check_agentfile_dimensions

        with TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            agents_root = temp_root / "AGENTS"
            workspace = agents_root / "test" / "sample"
            workspace.mkdir(parents=True)
            (workspace / "AGENT.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: urn:test:artefacto:sample
                      type: artefacto
                    version: 1.0.0
                    status: activo
                    nombre: Sample
                    descripcion: Fixture
                    lang: es
                    extensions:
                      kora:
                        vector_ontologico:
                          pi: 2
                          mu: 1
                          xi: 2
                          lambda: 0
                          phi: 2
                          sigma: [2, 1, 2, 2, 1]
                    artefacto:
                      perfil: {}
                      plan: {}
                      interfaz: {}
                      invariantes: {}
                    ---
                    """
                ),
                encoding="utf-8",
            )
            with patch.object(config_module, "AGENTS_ROOT", agents_root), \
                 patch.object(config_module, "KORA_ROOT", temp_root):
                diags = _check_agentfile_dimensions()
            self.assertEqual(len(diags), 1)
            self.assertIn("contexto", diags[0].message)

    def test_find_truncated_markdown_headings_detects_ellipsis_suffix(self):
        headings = find_truncated_markdown_headings("# Demo\n\n## Glosa 03 - Texto truncado...\n")
        self.assertEqual(headings, ["Glosa 03 - Texto truncado..."])

    def test_find_field_like_markdown_headings_detects_serialized_fields(self):
        headings = find_field_like_markdown_headings(
            "# Demo\n\n## Taxonomía\n\n### Titulo\n\n### Path\n",
            {"titulo", "path"},
        )
        self.assertEqual(headings, ["Titulo", "Path"])

    def test_find_html_fragments_detects_raw_html(self):
        findings = find_html_fragments("texto <a id=\"x\"></a>\n| A | B<br>C |\n")
        self.assertEqual(findings, ['<a id="x">', '<br>'])

    def test_normalize_angle_bracket_urls_converts_web_host_notation(self):
        fixed = normalize_angle_bracket_urls("Plataforma: <www.chileindica.cl>\n")
        self.assertEqual(fixed, "Plataforma: https://www.chileindica.cl\n")

    def test_find_opaque_internal_refs_detects_id_like_refs(self):
        findings = find_opaque_internal_refs("[-> GORE-NUBLE-GUIA-CTX-01](#gore-nuble-guia-ctx-01)\n")
        self.assertEqual(findings, ["GORE-NUBLE-GUIA-CTX-01"])

    def test_find_unverifiable_external_references_detects_source_artifacts_and_aliases(self):
        findings = find_unverifiable_external_references(
            "Fuente: kb_gn_009_ccpp_sts.md\nBase: `CPR-ART111-01`\n"
        )
        self.assertEqual(findings, ["kb_gn_009_ccpp_sts.md", "`CPR-ART111-01`"])

    def test_find_meta_intro_headings_detects_manual_prologue(self):
        findings = find_meta_intro_headings(
            "# Demo\n\n## Introduccion general\n\n### Proposito\n\n### Alcance\n"
        )
        self.assertEqual(findings, ["Introduccion general", "Proposito", "Alcance"])

    def test_find_empty_primary_wrapper_headings_detects_heading_only_container(self):
        findings = find_empty_primary_wrapper_headings("# Demo\n\n## Contenedor\n\n## Hijo real\n")
        self.assertEqual(findings, ["Contenedor"])

    def test_find_oversized_primary_chunks_flags_large_h2_block(self):
        text = "# Demo\n\n## Grande\n" + "\n".join(f"- item {i}" for i in range(8))
        findings = find_oversized_primary_chunks(text, max_lines=5)
        self.assertEqual(findings, [("Grande", 9)])

    def test_lint_published_kora_markdown_flags_kb_publication_issues(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:kora:kb:test"
                    version: "1.0.0"
                    status: published
                    tags: [a, b, c]
                    lang: es
                    ---

                    # Demo

                    ## Introduccion general

                    ## Contenedor

                    ## Hijo real

                    Texto con <a id="x"></a>, `CPR-ART111-01` y [-> GORE-NUBLE-GUIA-CTX-01](#gore-nuble-guia-ctx-01).
                    """
                ),
                encoding="utf-8",
            )
            failures = lint_published_kora_markdown(path, max_lines_per_h2=5)
            joined = "\n".join(failures)
            self.assertIn("meta_intro_heading", joined)
            self.assertIn("html_raw", joined)
            self.assertIn("opaque_internal_ref", joined)
            self.assertIn("unverifiable_ref", joined)
            self.assertIn("empty_primary_wrapper", joined)

    def test_lint_published_kora_markdown_uses_family_specific_thresholds(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "normative.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:kora:kb:test-normative"
                    version: "1.0.0"
                    status: published
                    tags: [a, b, c]
                    lang: es
                    extensions:
                      kora:
                        family: normative
                    ---

                    # Demo

                    ## Glosa 01
                    """
                )
                + "\n".join(f"- item {i}" for i in range(120))
                + "\n",
                encoding="utf-8",
            )
            failures = lint_published_kora_markdown(path)
            self.assertTrue(any("oversized_primary_chunk" in item for item in failures))

    def test_should_enforce_published_kora_markdown_accepts_canonical_spanish_statuses(self):
        published = {
            "_manifest": {"urn": "urn:kora:kb:test-publicado"},
            "status": "publicado",
        }
        deprecated = {
            "_manifest": {"urn": "urn:kora:kb:test-deprecado"},
            "status": "deprecado",
        }
        draft = {
            "_manifest": {"urn": "urn:kora:kb:test-borrador"},
            "status": "borrador",
        }

        self.assertTrue(should_enforce_published_kora_markdown(published, Path("published.md")))
        self.assertTrue(should_enforce_published_kora_markdown(deprecated, Path("deprecated.md")))
        self.assertFalse(should_enforce_published_kora_markdown(draft, Path("draft.md")))

    def test_lint_published_kora_markdown_accepts_publicado_as_published_like(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad-publicado.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:kora:kb:test-publicado"
                    version: "1.0.0"
                    status: publicado
                    tags: [a, b, c]
                    lang: es
                    ---

                    # Demo

                    ## Resumen

                    Texto con <a id="x"></a>.
                    """
                ),
                encoding="utf-8",
            )
            failures = lint_published_kora_markdown(path)
            self.assertTrue(any("html_raw" in item for item in failures), failures)

    def test_resolve_document_family_infers_bok_from_urn_and_tags(self):
        frontmatter = {
            "_manifest": {
                "urn": "urn:salud:kb:bok-demo",
                "tags": ["body-of-knowledge"],
            }
        }
        self.assertEqual(resolve_document_family(frontmatter), "bok")

    def test_resolve_max_lines_per_h2_uses_spec_family_threshold(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:demo-spec"},
            "extensions": {"kora": {"family": "spec"}},
        }
        self.assertEqual(resolve_max_lines_per_h2(frontmatter), 450)

    def test_auto_fix_published_kora_markdown_parts_removes_html_and_semanticizes_refs(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix"},
            "version": "1.0.0",
            "status": "published",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = textwrap.dedent(
            """\
            # Demo

            ## Introduccion general

            Texto meta.

            <a id="ANCLA"></a>

            ## Tema real

            ### Subtema resoluble

            Texto con [-> GORE-NUBLE-GUIA-TEMA-01](#subtema-resoluble) y <br>.
            """
        )
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=20)
        self.assertNotIn("<a id=", fixed)
        self.assertNotIn("<br>", fixed)
        self.assertNotIn("GORE-NUBLE-GUIA-TEMA-01", fixed)
        self.assertIn("[-> Subtema resoluble](#subtema-resoluble)", fixed)
        self.assertNotIn("## Introduccion general", fixed)

    def test_auto_fix_published_kora_markdown_parts_removes_nested_intro_prologue(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-intro"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n### Introduccion\n\nTexto meta.\n\n## Tema real\n\nContenido.\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertNotIn("### Introduccion", fixed)
        self.assertIn("## Tema real", fixed)

    def test_auto_fix_published_kora_markdown_parts_removes_nested_presentacion_heading(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-presentacion"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n## Presentacion\n\nTexto util.\n\n## Tema real\n\nContenido.\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertNotIn("## Presentacion", fixed)
        self.assertNotIn("Texto util.", fixed)

    def test_auto_fix_published_kora_markdown_parts_removes_field_scaffold_heading(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-field"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n## Tema\n\n### Contenido\n\nTexto util.\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertNotIn("### Contenido", fixed)
        self.assertIn("Texto util.", fixed)

    def test_auto_fix_published_kora_markdown_parts_strips_unverifiable_kb_file_refs(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-kbref"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n## Tema\n\nReferencia: kb_021_extractos_legales.md\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertNotIn("kb_021_extractos_legales.md", fixed)

    def test_auto_fix_published_kora_markdown_parts_strips_local_paths(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-path"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n## Tema\n\nFuente: knowledge/domains/gn/foo.md y file:///example/bar.md\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertNotIn("knowledge/domains/gn/foo.md", fixed)
        self.assertNotIn("file:///example/bar.md", fixed)

    def test_auto_fix_published_kora_markdown_parts_adds_primary_summary_when_missing(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-summary"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\nTexto sin chunk primario.\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertIn("## Resumen", fixed)

    def test_auto_fix_published_kora_markdown_parts_promotes_enumerated_outline_to_h2(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-fix-outline"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
        }
        body = "# Demo\n\n1. EJE TERRITORIO Y MEDIO AMBIENTE\n- item\n"
        fixed = auto_fix_published_kora_markdown_parts(frontmatter, body)
        self.assertIn("## EJE TERRITORIO Y MEDIO AMBIENTE", fixed)
        self.assertNotIn("## Resumen", fixed)

    def test_split_kora_markdown_parts_splits_large_normative_body(self):
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:test-split"},
            "version": "1.0.0",
            "status": "draft",
            "tags": ["a", "b", "c"],
            "lang": "es",
            "extensions": {"kora": {"family": "normative"}},
        }
        sections = []
        for idx in range(10):
            sections.append(f"## Seccion {idx+1}\n\n" + "\n".join(f"- item {n}" for n in range(25)))
        body = "# Demo\n\n" + "\n\n".join(sections) + "\n"
        shards, report = split_kora_markdown_parts(frontmatter, body)
        self.assertTrue(report["applied"])
        self.assertGreater(len(shards), 1)
        self.assertEqual(report["shard_count"], len(shards))

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
        failures = validate_traces_semantics(ROOT / "governance" / "dummy.md", "Traces to: formal/05 (Bounded Lattice)\n")
        self.assertEqual(failures, ["Traces to carece de ancla de seccion formal"])

    def test_validate_traces_semantics_flags_fxsl_direct_support(self):
        failures = validate_traces_semantics(
            ROOT / "governance" / "dummy.md",
            "Traces to: formal/05 §1.2 (Bounded Lattice), artifacts/knowledge/fxsl/cat/audit-patterns.md\n",
        )
        self.assertEqual(
            failures,
            ["Traces to referencia corpus FXSL auxiliar en vez de la formal layer oficial"],
        )

    def test_validate_traces_semantics_accepts_real_trace(self):
        failures = validate_traces_semantics(
            ROOT / "governance" / "dummy.md",
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

    def test_lint_md_cli_fails_on_published_markdown_with_html_and_opaq_refs(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:kora:kb:test-cli"
                    version: "1.0.0"
                    status: published
                    tags: [lint, md, test]
                    lang: es
                    ---

                    # Demo

                    ## Introduccion general

                    Texto con <a id="x"></a> y [-> GORE-NUBLE-GUIA-CTX-01](#gore-nuble-guia-ctx-01).
                    """
                ),
                encoding="utf-8",
            )
            result = run_cli("lint-md", str(path), check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("meta_intro_heading", result.stdout)
            self.assertIn("html_raw", result.stdout)
            self.assertIn("opaque_internal_ref", result.stdout)

    def test_lint_md_cli_fix_repairs_safe_structural_issues(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "fixable.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:kora:kb:test-cli-fix"
                    version: "1.0.0"
                    status: published
                    tags: [lint, md, test]
                    lang: es
                    ---

                    # Demo

                    ## Introduccion general

                    Texto meta.

                    <a id="X"></a>

                    ## Tema real

                    ### Seccion valida

                    Texto con [-> GORE-NUBLE-GUIA-CTX-01](#seccion-valida) y <br>.
                    """
                ),
                encoding="utf-8",
            )
            result = run_cli("lint-md", str(path), "--fix", check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            rewritten = path.read_text(encoding="utf-8")
            self.assertNotIn("<a id=", rewritten)
            self.assertNotIn("<br>", rewritten)
            self.assertNotIn("GORE-NUBLE-GUIA-CTX-01", rewritten)

    def test_dump_yaml_frontmatter_and_body_blocks_invalid_kb_when_safe_fix_is_insufficient(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad.md"
            frontmatter = {
                "_manifest": {"urn": "urn:kora:kb:test-dump"},
                "version": "1.0.0",
                "status": "draft",
                "tags": ["a", "b", "c"],
                "lang": "es",
            }
            body = "# Demo\n\n## Titulo\n\nTexto con `CPR-ART111-01`.\n"
            with self.assertRaisesRegex(ValueError, "KORA/MD blocked by lint"):
                dump_yaml_frontmatter_and_body(path, frontmatter, body)

    def test_dump_yaml_frontmatter_and_body_autofixes_safe_kb_issues_before_write(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "fixed.md"
            frontmatter = {
                "_manifest": {"urn": "urn:kora:kb:test-dump-fix"},
                "version": "1.0.0",
                "status": "draft",
                "tags": ["a", "b", "c"],
                "lang": "es",
            }
            body = textwrap.dedent(
                """\
                # Demo

                ## Introduccion general

                Texto meta.

                <a id="x"></a>

                ## Tema real

                ### Seccion util

                Texto con [-> GORE-NUBLE-GUIA-CTX-01](#seccion-util) y <br>.
                """
            )
            dump_yaml_frontmatter_and_body(path, frontmatter, body)
            written = path.read_text(encoding="utf-8")
            self.assertNotIn("<a id=", written)
            self.assertNotIn("<br>", written)
            self.assertNotIn("GORE-NUBLE-GUIA-CTX-01", written)
            self.assertIn("[-> Seccion util](#seccion-util)", written)

    def test_dump_yaml_frontmatter_and_body_writes_split_shards_and_report(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "split.md"
            frontmatter = {
                "_manifest": {"urn": "urn:kora:kb:test-writer-split"},
                "version": "1.0.0",
                "status": "draft",
                "tags": ["a", "b", "c"],
                "lang": "es",
                "extensions": {"kora": {"family": "normative"}},
            }
            body = "# Demo\n\n" + "\n\n".join(
                f"## Seccion {idx+1}\n\n" + "\n".join(f"- item {n}" for n in range(30))
                for idx in range(12)
            ) + "\n"
            report = dump_yaml_frontmatter_and_body(path, frontmatter, body)
            self.assertTrue(report["split"]["applied"])
            self.assertGreater(report["split"]["shard_count"], 1)
            self.assertTrue(path.exists())
            self.assertTrue((path.parent / "split--p02.md").exists())

    def test_dump_yaml_frontmatter_and_body_allows_non_kb_published_bootstrap(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "agents.md"
            frontmatter = {
                "_manifest": {"urn": "urn:test:agent-bootstrap:sample-agents:1.0.0"},
                "version": "1.0.0",
                "status": "published",
                "lang": "es",
            }
            dump_yaml_frontmatter_and_body(path, frontmatter, "# Demo\n")
            self.assertTrue(path.exists())

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
        source_path = AGENTS_ROOT / "gn" / "dgi-virtual" / "AGENTS.md"
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


class DeprecatedFilterTests(unittest.TestCase):
    def test_is_workspace_deprecated_returns_true_for_deprecated(self):
        from kora_lib.workspaces import _is_workspace_deprecated

        with TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            config = workspace / "config.json"
            config.write_text(
                '{"_manifest": {"urn": "urn:test:agent-bootstrap:x-config:1.0.0", '
                '"type": "bootstrap_config", "status": "deprecated"}}',
                encoding="utf-8",
            )
            self.assertTrue(_is_workspace_deprecated(workspace))

    def test_is_workspace_deprecated_reads_canonical_status_from_agent_md(self):
        from kora_lib.workspaces import _is_workspace_deprecated

        with TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            (workspace / "AGENT.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    _manifest:
                      urn: "urn:test:artefacto:demo"
                    version: "1.0.0"
                    status: deprecado
                    lang: es
                    ---
                    """
                ),
                encoding="utf-8",
            )
            self.assertTrue(_is_workspace_deprecated(workspace))

    def test_is_workspace_deprecated_returns_false_for_active(self):
        from kora_lib.workspaces import _is_workspace_deprecated

        with TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            config = workspace / "config.json"
            config.write_text(
                '{"_manifest": {"urn": "urn:test:agent-bootstrap:x-config:1.0.0", '
                '"type": "bootstrap_config"}}',
                encoding="utf-8",
            )
            self.assertFalse(_is_workspace_deprecated(workspace))

    def test_is_workspace_deprecated_returns_false_for_missing_config(self):
        from kora_lib.workspaces import _is_workspace_deprecated

        with TemporaryDirectory() as tmpdir:
            self.assertFalse(_is_workspace_deprecated(Path(tmpdir)))

    def test_iter_agent_workspaces_excludes_deprecated_by_default(self):
        from kora_lib.workspaces import iter_agent_workspaces

        workspaces = iter_agent_workspaces()
        for ws in workspaces:
            config_path = ws / "config.json"
            if config_path.exists():
                import json

                data = json.loads(config_path.read_text(encoding="utf-8"))
                self.assertNotEqual(
                    data.get("_manifest", {}).get("status"),
                    "deprecated",
                    msg=f"deprecated workspace {ws} should be excluded",
                )

    def test_iter_agent_workspaces_includes_deprecated_when_requested(self):
        from kora_lib.workspaces import iter_agent_workspaces

        default_count = len(iter_agent_workspaces())
        all_count = len(iter_agent_workspaces(include_deprecated=True))
        self.assertGreaterEqual(all_count, default_count)

    def test_catalog_index_excludes_deprecated_artifacts(self):
        result = run_cli("index")
        self.assertIn("Successfully indexed", result.stdout)
        from kora_lib.catalog import load_catalog

        catalog = load_catalog()
        for category, items in catalog["Catalog"].items():
            for item in items:
                self.assertNotEqual(
                    item.get("status"),
                    "deprecated",
                    msg=f"deprecated artifact {item.get('urn')} should not be indexed",
                )


if __name__ == "__main__":
    unittest.main()
