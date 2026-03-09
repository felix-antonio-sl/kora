import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

from scripts.kora_lib.artifacts import load_markdown_parts


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "gn_rebuild.py"


class GnRebuildTests(unittest.TestCase):
    def _run(self, *args, cwd=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=str(cwd or ROOT),
            capture_output=True,
            text=True,
            check=False,
        )

    def _write_md(self, path, urn, title):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "\n".join(
                [
                    "---",
                    "_manifest:",
                    f"  urn: {urn}",
                    "  provenance:",
                    "    created_by: fixture",
                    "    created_at: '2026-03-08'",
                    "    source: fixture",
                    "version: 1.0.0",
                    "status: published",
                    "tags: [gn, fixture, sample]",
                    "lang: es",
                    "extensions: {}",
                    "---",
                    "",
                    f"# {title}",
                    "",
                    "## Base",
                    "Fixture",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    def _write_kora_stub(self, repo):
        script = repo / "scripts/kora"
        script.write_text(
            "\n".join(
                [
                    "#!/usr/bin/env python3",
                    "import sys",
                    "command = sys.argv[1] if len(sys.argv) > 1 else ''",
                    "if command == 'index':",
                    "    print('indexed')",
                    "    raise SystemExit(0)",
                    "if command == 'health' and '--strict' in sys.argv[2:]:",
                    "    print('healthy')",
                    "    raise SystemExit(0)",
                    "raise SystemExit(1)",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        script.chmod(0o755)

    def test_freeze_build_validate_report_flow(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/gestion").mkdir(parents=True, exist_ok=True)
            (source_root / "domains/gn/05_data_raw").mkdir(parents=True, exist_ok=True)

            yaml_source = {
                "_manifest": {"urn": "urn:test:kb:src"},
                "ID": "GN-MANUAL-PPTO",
                "Resumen": {"Objetivo": "Mantener fidelidad", "Pasos": ["Uno", "Dos"]},
            }
            (source_root / "domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml").write_text(
                yaml.safe_dump(yaml_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            (source_root / "domains/gn/05_data_raw/kb_gn_012_progs_vigentes.csv").write_text(
                "programa,estado\nA,vigente\nB,vigente\n",
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/manuales/manual-presupuesto.md",
                "urn:gn:kb:manual-presupuesto",
                "Manual Presupuesto",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "manuales/manual-presupuesto.md",
                                "target_urn": "urn:gn:kb:manual-presupuesto",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            },
                            {
                                "source_paths": ["domains/gn/05_data_raw/kb_gn_012_progs_vigentes.csv"],
                                "source_type": "csv",
                                "target_path": "datos/programas-vigentes-resumen.md",
                                "target_urn": "urn:gn:kb:programas-vigentes-resumen",
                                "transform_class": "derive_csv_scope",
                                "scope_statement": "Resumen de programas vigentes",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Scope", "Resumen", "Muestra"],
                            },
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "testrun")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            self.assertTrue((repo / "source/gn/testrun/source-lock.yml").exists())

            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "testrun", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            manual = repo / "drafts/gn/manuales/manual-presupuesto.md"
            csv_doc = repo / "drafts/gn/datos/programas-vigentes-resumen.md"
            evidence = repo / "build/gn-rebuild/testrun/evidence/datos__programas-vigentes-resumen.md.json"
            self.assertTrue(manual.exists())
            self.assertTrue(csv_doc.exists())
            self.assertTrue(evidence.exists())
            self.assertIn("extensions:", manual.read_text(encoding="utf-8"))
            self.assertIn("source_paths", manual.read_text(encoding="utf-8"))
            evidence_payload = json.loads(evidence.read_text(encoding="utf-8"))
            self.assertEqual(evidence_payload["target_path"], "datos/programas-vigentes-resumen.md")
            self.assertEqual(evidence_payload["catalog_state"], "draft_unindexed")
            self.assertEqual(evidence_payload["draft_urn"], "urn:gn:kb:programas-vigentes-resumen")
            self.assertNotIn("target_urn", evidence_payload)

            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "testrun")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            report = self._run("--repo-root", str(repo), "--map-path", str(map_path), "report", "--run-id", "testrun")
            self.assertEqual(report.returncode, 0, report.stderr or report.stdout)
            report_path = repo / "build/gn-rebuild/testrun/report.md"
            self.assertTrue(report_path.exists())
            self.assertIn("Structural Diff", report_path.read_text(encoding="utf-8"))
            self.assertIn("build/ queda fuera de index, graph y health por diseno", report_path.read_text(encoding="utf-8"))

    def test_koda_hybrid_prefers_embedded_markdown_and_skips_technical_blocks(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/ipr").mkdir(parents=True, exist_ok=True)

            hybrid_source = {
                "_manifest": {"urn": "urn:test:kb:hybrid"},
                "ID": "HYBRID-01",
                "LLM_Parsing_Instructions": {"ID": "PARSER-01", "Content": "ignore"},
                "Content": {
                    "Body_MD": {
                        "Content": "# Glosario\n\n## Terminos\n- Uno\n- Dos\n"
                    }
                },
                "terminos": [
                    {"nombre": "Uno", "def": "Def uno"},
                    {"nombre": "Dos", "def": "Def dos"},
                ],
            }
            (source_root / "domains/gn/03_operacion/ipr/otroglosario.yml").write_text(
                yaml.safe_dump(hybrid_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gobernanza/glosario-ipr-consolidado.md",
                "urn:gn:kb:glosario-ipr-consolidado",
                "Glosario IPR",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "transform_class": "korafy_direct",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/otroglosario.yml"],
                                "target_path": "gobernanza/glosario-ipr-consolidado.md",
                                "target_urn": "urn:gn:kb:glosario-ipr-consolidado",
                                "transform_class": "korafy_koda_hybrid",
                                "review_gate": "manual",
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "hybridrun")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "hybridrun", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/glosario-ipr-consolidado.md")
            self.assertIn("# Glosario", body)
            self.assertIn("## Terminos", body)
            self.assertNotIn("LLM_Parsing_Instructions", body)
            self.assertNotIn("PARSER-01", body)

    def test_koda_hybrid_rejects_poor_embedded_record_lists_and_falls_back_to_structured_render(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/ipr").mkdir(parents=True, exist_ok=True)

            hybrid_source = {
                "_manifest": {"urn": "urn:test:kb:hybrid-glossary"},
                "Content": {
                    "Body_MD": {
                        "Content": "# Glosario\n\n## Terminos\n-\n  ### Nombre\n  VAN\n  ### Def\n  |\n-\n  ### Nombre\n  TIR\n  ### Def\n  Tasa interna\n"
                    }
                },
                "terminos": [
                    {"nombre": "VAN", "def": "|"},
                    {"nombre": "TIR", "def": "Tasa interna"},
                ],
            }
            (source_root / "domains/gn/03_operacion/ipr/otroglosario.yml").write_text(
                yaml.safe_dump(hybrid_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gobernanza/glosario-ipr-consolidado.md",
                "urn:gn:kb:glosario-ipr-consolidado",
                "Glosario IPR",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/otroglosario.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "gobernanza/glosario-ipr-consolidado.md",
                                "target_urn": "urn:gn:kb:glosario-ipr-consolidado",
                                "transform_class": "korafy_koda_hybrid",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "hybridtable")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "hybridtable", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/glosario-ipr-consolidado.md")
            self.assertIn("| nombre | def |", body)
            self.assertIn("| VAN | \\| |", body)
            self.assertNotIn("### Nombre", body)

    def test_korafy_direct_strips_koda_metadata_and_normalizes_columns_rows_tables(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/presupuesto").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:ley"},
                "ID": "GN-LEY-01",
                "Version": "1.0.0",
                "Status": "Draft",
                "Format": "KODA/Spec",
                "LLM_Parsing_Instructions": {"ID": "PARSER-01", "Content": "ignore"},
                "Ley_Presupuestos": {
                    "ID": "GN-LEY-PPTO",
                    "Purp": "Norma presupuestaria.",
                    "Resumen": {
                        "Asunto": "Partida 31",
                        "Tabla_Resumen": {
                            "Columns": ["Item", "Monto"],
                            "Rows": [["Ingresos", "100"], ["Gastos", "80"]],
                        },
                    },
                },
            }
            (
                source_root / "domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"
            ).write_text(yaml.safe_dump(source, sort_keys=False, allow_unicode=True), encoding="utf-8")

            self._write_md(
                repo / "knowledge/gn/normativa/ley-presupuestos-2026-partida-31.md",
                "urn:gn:kb:ley-presupuestos-2026-partida-31",
                "Partida 31",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "normativa/ley-presupuestos-2026-partida-31.md",
                                "target_urn": "urn:gn:kb:ley-presupuestos-2026-partida-31",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "directclean")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "directclean", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/normativa/ley-presupuestos-2026-partida-31.md")
            self.assertNotIn("## ID", body)
            self.assertNotIn("## Version", body)
            self.assertNotIn("LLM Parsing Instructions", body)
            self.assertIn("| Item | Monto |", body)
            self.assertIn("| Ingresos | 100 |", body)

    def test_korafy_direct_renders_homogeneous_dict_lists_as_tables_with_sparse_cells(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/ipr").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:glosario"},
                "Glosario": {
                    "Terminos": [
                        {"nombre": "VAN", "def": "|"},
                        {"nombre": "TIR"},
                    ]
                },
            }
            (source_root / "domains/gn/03_operacion/ipr/otroglosario.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gobernanza/glosario-ipr-consolidado.md",
                "urn:gn:kb:glosario-ipr-consolidado",
                "Glosario IPR",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/otroglosario.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "gobernanza/glosario-ipr-consolidado.md",
                                "target_urn": "urn:gn:kb:glosario-ipr-consolidado",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "dictlist")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "dictlist", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/glosario-ipr-consolidado.md")
            self.assertIn("| nombre | def |", body)
            self.assertIn("| VAN | \\| |", body)
            self.assertIn("| TIR |  |", body)

    def test_validate_rejects_koda_residue_in_body(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/presupuesto").mkdir(parents=True, exist_ok=True)
            yaml_source = {
                "_manifest": {"urn": "urn:test:kb:src"},
                "Resumen": {"Objetivo": "Mantener fidelidad"},
            }
            (source_root / "domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml").write_text(
                yaml.safe_dump(yaml_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/normativa/ley-presupuestos-2026-partida-31.md",
                "urn:gn:kb:ley-presupuestos-2026-partida-31",
                "Partida 31",
            )

            draft_path = repo / "drafts/gn/normativa/ley-presupuestos-2026-partida-31.md"
            draft_path.parent.mkdir(parents=True, exist_ok=True)
            draft_path.write_text(
                "\n".join(
                    [
                        "---",
                        "_manifest:",
                        "  urn: urn:gn:kb:ley-presupuestos-2026-partida-31",
                        "  provenance:",
                        "    created_by: fixture",
                        "    created_at: '2026-03-08'",
                        "    source: fixture",
                        "version: 1.0.0",
                        "status: draft",
                        "tags: [gn, normativa, presupuesto]",
                        "lang: es",
                        "extensions:",
                        "  gn:",
                        "    source_paths: [domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml]",
                        "    source_hashes:",
                        "      domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml: deadbeef",
                        "    source_type: koda_yaml",
                        "    transformation_mode: korafy_direct",
                        "    fs: 100",
                        "    cr: 2.0",
                        "    run_id: residue",
                        "    review_gate: auto",
                        "---",
                        "",
                        "# Partida 31",
                        "",
                        "## ID",
                        "GN-LEY-PPTO",
                        "",
                        "## Contenido",
                        "BEGIN_LLM_INSTRUCTIONS",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "normativa/ley-presupuestos-2026-partida-31.md",
                                "target_urn": "urn:gn:kb:ley-presupuestos-2026-partida-31",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "residue")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)

            evidence_root = repo / "build/gn-rebuild/residue/evidence"
            evidence_root.mkdir(parents=True, exist_ok=True)
            (evidence_root / "normativa__ley-presupuestos-2026-partida-31.md.json").write_text(
                json.dumps(
                    {
                        "target_path": "normativa/ley-presupuestos-2026-partida-31.md",
                        "draft_urn": "urn:gn:kb:ley-presupuestos-2026-partida-31",
                        "catalog_state": "draft_unindexed",
                        "preserved_facts": ["Resumen.Objetivo=Mantener fidelidad"],
                    },
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "residue")
            self.assertNotEqual(validate.returncode, 0)
            self.assertIn("residuo KODA en headings", validate.stdout)
            self.assertIn("residuo KODA en cuerpo", validate.stdout)

    def test_korafy_composite_omits_source_headings_from_body(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/01_fundamentos/intro").mkdir(parents=True, exist_ok=True)
            (source_root / "ontologies/onto_gorenuble").mkdir(parents=True, exist_ok=True)

            primary = {
                "_manifest": {"urn": "urn:test:kb:organigrama"},
                "Organigrama": {
                    "Purp": "Describir estructura organizacional.",
                    "Unidades": [{"nombre": "Gabinete", "dependencia": "Gobernador Regional"}],
                },
            }
            secondary = "<a> <b> <c> .\n"
            (source_root / "domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml").write_text(
                yaml.safe_dump(primary, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            (source_root / "ontologies/onto_gorenuble/organigrama.ttl").write_text(secondary, encoding="utf-8")

            self._write_md(
                repo / "knowledge/gn/gobernanza/organigrama.md",
                "urn:gn:kb:organigrama",
                "Organigrama",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": [
                                    "domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml",
                                    "ontologies/onto_gorenuble/organigrama.ttl",
                                ],
                                "source_type": "mixed",
                                "target_path": "gobernanza/organigrama.md",
                                "target_urn": "urn:gn:kb:organigrama",
                                "transform_class": "korafy_composite",
                                "scope_statement": "Vista compuesta de estructura organizacional.",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "composite")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "composite", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/organigrama.md")
            self.assertNotIn("## Fuente principal", body)
            self.assertNotIn("## Fuentes derivadas", body)

    def test_validate_rejects_public_target_urn_in_draft_evidence(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/gestion").mkdir(parents=True, exist_ok=True)
            yaml_source = {
                "_manifest": {"urn": "urn:test:kb:src"},
                "ID": "GN-MANUAL-PPTO",
                "Resumen": {"Objetivo": "Mantener fidelidad"},
            }
            (source_root / "domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml").write_text(
                yaml.safe_dump(yaml_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            self._write_md(
                repo / "knowledge/gn/manuales/manual-presupuesto.md",
                "urn:gn:kb:manual-presupuesto",
                "Manual Presupuesto",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "manuales/manual-presupuesto.md",
                                "target_urn": "urn:gn:kb:manual-presupuesto",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "badurn")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "badurn", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            evidence_path = repo / "build/gn-rebuild/badurn/evidence/manuales__manual-presupuesto.md.json"
            payload = json.loads(evidence_path.read_text(encoding="utf-8"))
            payload["target_urn"] = payload["draft_urn"]
            evidence_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "badurn")
            self.assertNotEqual(validate.returncode, 0)
            self.assertIn("evidence expone target_urn publico antes de cutover", validate.stdout)

    def test_build_normalizes_legacy_and_external_urns_in_body(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/gestion").mkdir(parents=True, exist_ok=True)
            (source_root / "domains/gn/03_operacion/presupuesto").mkdir(parents=True, exist_ok=True)

            manual_source = {
                "_manifest": {"urn": "urn:test:kb:manual"},
                "Resumen": {"Objetivo": "Mantener fidelidad"},
            }
            composite_source = {
                "_manifest": {"urn": "urn:test:kb:composite"},
                "Content": {
                    "Body_MD": {
                        "Content": "\n".join(
                            [
                                "# Manual Operacional DGI",
                                "",
                                "## Referencias",
                                "- urn:knowledge:gorenuble:gn:manual-presupuesto:1.0.0",
                                "- urn:knowledge:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-03",
                                "- urn:knowledge:koda:core:spec:1.0.0",
                                "",
                            ]
                        )
                    }
                },
            }

            (source_root / "domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml").write_text(
                yaml.safe_dump(manual_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            (source_root / "domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml").write_text(
                yaml.safe_dump(manual_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            (source_root / "domains/gn/03_operacion/gestion/kb_gn_099_manual_operacional_dgi_koda.yml").write_text(
                yaml.safe_dump(composite_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/manuales/manual-presupuesto.md",
                "urn:gn:kb:manual-presupuesto",
                "Manual Presupuesto",
            )
            self._write_md(
                repo / "knowledge/gn/manuales/manual-operacional-dgi.md",
                "urn:gn:kb:manual-operacional-dgi",
                "Manual Operacional DGI",
            )
            self._write_md(
                repo / "knowledge/gn/normativa/ley-presupuestos-2026-partida-31.md",
                "urn:gn:kb:ley-presupuestos-2026-partida-31",
                "Partida 31",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml"],
                                "target_path": "manuales/manual-presupuesto.md",
                                "target_urn": "urn:gn:kb:manual-presupuesto",
                                "transform_class": "korafy_direct",
                            },
                            {
                                "source_paths": ["domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"],
                                "target_path": "normativa/ley-presupuestos-2026-partida-31.md",
                                "target_urn": "urn:gn:kb:ley-presupuestos-2026-partida-31",
                                "transform_class": "korafy_direct",
                            },
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_099_manual_operacional_dgi_koda.yml"],
                                "target_path": "manuales/manual-operacional-dgi.md",
                                "target_urn": "urn:gn:kb:manual-operacional-dgi",
                                "transform_class": "korafy_koda_hybrid",
                            },
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "urnnorm")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "urnnorm", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/manuales/manual-operacional-dgi.md")
            self.assertIn("urn:gn:kb:manual-presupuesto", body)
            self.assertNotIn("urn:knowledge:gorenuble:gn:manual-presupuesto:1.0.0", body)
            self.assertIn("urn:gn:kb:ley-presupuestos-2026-partida-31", body)
            self.assertNotIn("#GN-LEY-PPTO-2026-P31-GLO-03", body)
            self.assertIn("KODA Core Spec 1.0.0", body)
            self.assertNotIn("urn:knowledge:koda:core:spec:1.0.0", body)

    def test_cutover_promotes_drafts_and_revalidates_knowledge_tree(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            self._write_kora_stub(repo)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/gestion").mkdir(parents=True, exist_ok=True)
            yaml_source = {
                "_manifest": {"urn": "urn:test:kb:src"},
                "ID": "GN-MANUAL-PPTO",
                "Resumen": {"Objetivo": "Mantener fidelidad", "Pasos": ["Uno", "Dos"]},
            }
            (source_root / "domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml").write_text(
                yaml.safe_dump(yaml_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            self._write_md(
                repo / "knowledge/gn/manuales/manual-presupuesto.md",
                "urn:gn:kb:manual-presupuesto",
                "Manual Presupuesto",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "manuales/manual-presupuesto.md",
                                "target_urn": "urn:gn:kb:manual-presupuesto",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "cutrun")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "cutrun", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            cutover = self._run("--repo-root", str(repo), "--map-path", str(map_path), "cutover", "--run-id", "cutrun")
            self.assertEqual(cutover.returncode, 0, cutover.stderr or cutover.stdout)
            self.assertIn("GN promoted-tree validation passed.", cutover.stdout)
            self.assertIn("cutover complete", cutover.stdout)
            promoted = repo / "knowledge/gn/manuales/manual-presupuesto.md"
            self.assertTrue(promoted.exists())
            frontmatter, _body = load_markdown_parts(promoted)
            self.assertEqual(frontmatter["status"], "published")

    def test_generic_family_suppresses_source_metadata_and_local_paths(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/gestion").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:manual"},
                "Source_ID": "SRC-01",
                "Primary-Source": "staging/brow_speculativo/manual.md",
                "Authoritative-Sources": [
                    {
                        "Path": "staging/temp/brutos/documento.yml",
                        "Type": "Resolucion",
                        "Priority": 1,
                    }
                ],
                "Last-Validated": "2026-01-01",
                "Manual_Demo": {
                    "Title": "Manual Demo",
                    "Objetivo": {"Obj": "Mantener estructura semántica."},
                },
                "Referencias_Cruzadas": {
                    "Ctx_Optional": ["knowledge/domains/gn/manuales/manual_demo_previo.yml"]
                },
            }
            (source_root / "domains/gn/03_operacion/gestion/kb_gn_500_manual_demo_koda.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/manuales/manual-demo.md",
                "urn:gn:kb:manual-demo",
                "Manual Demo",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/gestion/kb_gn_500_manual_demo_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "manuales/manual-demo.md",
                                "target_urn": "urn:gn:kb:manual-demo",
                                "transform_class": "korafy_direct",
                                "review_gate": "auto",
                                "dependencies": [],
                                "expected_sections": ["Contenido"],
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "genericmeta")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "genericmeta", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "genericmeta")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/manuales/manual-demo.md")
            self.assertNotIn("Source ID", body)
            self.assertNotIn("Authoritative Sources", body)
            self.assertNotIn("staging/", body)
            self.assertNotIn("knowledge/domains", body)

    def test_normative_family_renders_mixed_content_without_field_heading_dump(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/presupuesto").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:normativa"},
                "Ley_Presupuestos": {
                    "Purp": "Regular la ejecución presupuestaria.",
                    "Definiciones_Reutilizables": [{"ID": "LEY19886", "Def": "Ley de compras públicas."}],
                    "Articulos": {
                        "Articulo_01": {
                            "Contenido": [
                                "Aplica conforme a la",
                                {"Ref": "LEY19886"},
                                ".",
                            ]
                        }
                    },
                },
            }
            (
                source_root / "domains/gn/03_operacion/presupuesto/kb_gn_777_normativa_demo_koda.yml"
            ).write_text(yaml.safe_dump(source, sort_keys=False, allow_unicode=True), encoding="utf-8")

            self._write_md(
                repo / "knowledge/gn/normativa/normativa-demo.md",
                "urn:gn:kb:normativa-demo",
                "Normativa Demo",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "transform_class": "korafy_direct",
                            "document_family": "normative",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/presupuesto/kb_gn_777_normativa_demo_koda.yml"],
                                "target_path": "normativa/normativa-demo.md",
                                "target_urn": "urn:gn:kb:normativa-demo",
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "normmixed")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "normmixed", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "normmixed")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/normativa/normativa-demo.md")
            self.assertIn("## Articulo 01", body)
            self.assertIn("Aplica conforme a la LEY19886.", body)
            self.assertNotIn("### Contenido", body)
            self.assertNotIn("{'Ref':", body)

    def test_normative_glosa_heading_derives_subject_when_source_has_no_asunto(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/presupuesto").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:glosa"},
                "Ley_Presupuestos": {
                    "Glosas": {
                        "Glosa_03": {
                            "Contenido": "Los recursos del presupuesto regional no podrán financiar gastos en personal."
                        }
                    }
                },
            }
            (source_root / "domains/gn/03_operacion/presupuesto/kb_gn_778_glosa_demo_koda.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/normativa/glosa-demo.md",
                "urn:gn:kb:glosa-demo",
                "Glosa Demo",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "transform_class": "korafy_direct",
                            "document_family": "normative",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/presupuesto/kb_gn_778_glosa_demo_koda.yml"],
                                "target_path": "normativa/glosa-demo.md",
                                "target_urn": "urn:gn:kb:glosa-demo",
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "glosasubject")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "glosasubject", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/normativa/glosa-demo.md")
            self.assertIn("## Glosa 03 - Los recursos del presupuesto regional no podrán financiar gastos en", body)
            self.assertNotIn("...", body)
            self.assertNotIn("## Glosa 03\n", body)

    def test_validate_rejects_truncated_heading_in_knowledge_doc(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("drafts/gn",):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            draft_path = repo / "drafts/gn/demo.md"
            draft_path.write_text(
                "\n".join(
                    [
                        "---",
                        "_manifest:",
                        "  urn: urn:gn:kb:demo",
                        "  provenance:",
                        "    created_by: fixture",
                        "    created_at: '2026-03-09'",
                        "    source: fixture",
                        "version: 1.0.0",
                        "status: draft",
                        "tags: [gn, demo, test]",
                        "lang: es",
                        "extensions:",
                        "  gn:",
                        "    source_paths: [demo.yml]",
                        "    source_hashes:",
                        "      demo.yml: deadbeef",
                        "    source_type: koda_yaml",
                        "    transformation_mode: korafy_direct",
                        "    document_family: normative",
                        "    publication_class: knowledge",
                        "    fs: 100",
                        "    cr: 2.0",
                        "    run_id: testrun",
                        "    review_gate: auto",
                        "---",
                        "",
                        "# Demo",
                        "",
                        "## Glosa 03 - Texto truncado...",
                        "Contenido",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            from scripts.kora_lib.gn_validation import validate_gn_markdown

            result = validate_gn_markdown(draft_path, expected_rel_path="demo.md", expected_urn="urn:gn:kb:demo")
            self.assertTrue(any("heading truncado no permitido" in item for item in result["failures"]))

    def test_validate_rejects_nonrecoverable_normative_primary_heading(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            draft_path = repo / "drafts/gn/demo.md"
            draft_path.parent.mkdir(parents=True, exist_ok=True)
            draft_path.write_text(
                "\n".join(
                    [
                        "---",
                        "_manifest:",
                        "  urn: urn:gn:kb:demo",
                        "  provenance:",
                        "    created_by: fixture",
                        "    created_at: '2026-03-09'",
                        "    source: fixture",
                        "version: 1.0.0",
                        "status: draft",
                        "tags: [gn, demo, test]",
                        "lang: es",
                        "extensions:",
                        "  gn:",
                        "    source_paths: [demo.yml]",
                        "    source_hashes:",
                        "      demo.yml: deadbeef",
                        "    source_type: koda_yaml",
                        "    transformation_mode: korafy_direct",
                        "    document_family: normative",
                        "    publication_class: knowledge",
                        "    fs: 100",
                        "    cr: 2.0",
                        "    run_id: testrun",
                        "    review_gate: auto",
                        "---",
                        "",
                        "# Demo",
                        "",
                        "## Glosa 03",
                        "Contenido",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            from scripts.kora_lib.gn_validation import validate_gn_markdown

            result = validate_gn_markdown(draft_path, expected_rel_path="demo.md", expected_urn="urn:gn:kb:demo")
            self.assertTrue(any("heading primario no recuperable" in item for item in result["failures"]))

    def test_glossary_conflicts_can_be_resolved_in_map_contract(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/ipr").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:glossary"},
                "terminos": [
                    {"nombre": "Población Objetivo", "def": "Grupo específico afectado por el problema central."},
                    {"nombre": "Población objetivo", "def": "Segmento de personas al que se dirige la solución."},
                ],
            }
            (source_root / "domains/gn/03_operacion/ipr/otroglosario.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gobernanza/glosario-ipr-consolidado.md",
                "urn:gn:kb:glosario-ipr-consolidado",
                "Glosario IPR",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "transform_class": "korafy_koda_hybrid",
                            "document_family": "glossary",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/otroglosario.yml"],
                                "target_path": "gobernanza/glosario-ipr-consolidado.md",
                                "target_urn": "urn:gn:kb:glosario-ipr-consolidado",
                                "glossary_conflict_resolutions": {
                                    "población objetivo": {
                                        "canonical_name": "Población objetivo",
                                        "definition": "Grupo específico afectado por el problema central.",
                                        "aliases": ["Población Objetivo"],
                                    }
                                },
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "glossaryres")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "glossaryres", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "glossaryres")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/glosario-ipr-consolidado.md")
            self.assertEqual(frontmatter["extensions"]["gn"]["glossary_conflicts"], 0)
            self.assertIn("Población objetivo", body)
            self.assertIn("Población Objetivo", body)

    def test_omega_family_normalizes_legacy_urn_refs_and_omits_unpublishable_ones(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/03_operacion/ipr").mkdir(parents=True, exist_ok=True)

            omega_source = {
                "_meta": {
                    "urn": "urn:gorenuble:omega:ontology:test:1.0.0",
                    "type": "Ω-Ontology",
                    "schema": "urn:goreos:omega:schema:2.0.0",
                    "based_on": [
                        "urn:knowledge:gorenuble:gn:selector-ipr:3.1.0",
                        "urn:fxsl:cat:omega-opm-ws:1.0.0",
                    ],
                    "date": "2026-03-08",
                },
                "omega_objects": [{"id": "Ω-IPR", "type": "Ω-Object", "description": "Objeto base."}],
                "omega_processes": [{"id": "P-INGRESAR", "name": "Ingresar", "type": "Ω-Transform", "actor": "GORE"}],
                "omega_coalgebra": {
                    "functor": "F(S)",
                    "state_space": {"fase_1_ingreso": ["POSTULADA"]},
                    "transitions": [{"from": "POSTULADA", "to": "ADMISIBLE", "event": "Revision", "morphism": "P-INGRESAR"}],
                },
                "omega_constructions": [{"id": "Ω-CONS", "type": "Adjunction", "name": "Construcción"}],
                "omega_monads": [{"id": "Ω-MONAD", "name": "Monad", "evaluator": "GORE", "structure": "T(X)"}],
                "omega_profunctor": {
                    "signature": "Π: A × B",
                    "composition_law": "Selector determina el dictamen",
                    "mappings": [{"selector": "MEC-1", "gestion": {"fase2": "TRACK-A", "fase3": "TRACK-B", "dictamen": "RS"}}],
                },
                "omega_axioms": [{"id": "AX-1", "statement": "Todo mecanismo determina un track."}],
            }
            selector_source = {"_manifest": {"urn": "urn:test:kb:selector"}, "Selector": {"Resumen": {"Objetivo": "Clasificar IPR."}}}

            (source_root / "domains/gn/03_operacion/ipr/kb_omega_test.yml").write_text(
                yaml.safe_dump(omega_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            (source_root / "domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml").write_text(
                yaml.safe_dump(selector_source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(repo / "knowledge/gn/gobernanza/omega-test.md", "urn:gn:kb:omega-test", "Omega Test")
            self._write_md(repo / "knowledge/gn/ris/selector-ipr.md", "urn:gn:kb:selector-ipr", "Selector IPR")

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml"],
                                "source_type": "koda_yaml",
                                "target_path": "ris/selector-ipr.md",
                                "target_urn": "urn:gn:kb:selector-ipr",
                                "transform_class": "korafy_direct",
                            },
                            {
                                "source_paths": ["domains/gn/03_operacion/ipr/kb_omega_test.yml"],
                                "source_type": "ontology_yaml",
                                "target_path": "gobernanza/omega-test.md",
                                "target_urn": "urn:gn:kb:omega-test",
                                "target_title": "Omega Test",
                                "transform_class": "derive_ttl_scope",
                                "document_family": "omega",
                                "scope_statement": "Derivado Ω de prueba.",
                            },
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "omegair")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "omegair", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "omegair")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gobernanza/omega-test.md")
            self.assertIn("(urn:gn:kb:selector-ipr)", body)
            self.assertNotIn("urn:knowledge:gorenuble:gn:selector-ipr:3.1.0", body)
            self.assertNotIn("urn:fxsl:cat:omega-opm-ws:1.0.0", body)
            self.assertNotIn("### Type", body)

    def test_cq_catalog_always_emits_non_empty_summary(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            source_root = Path(tmpdir) / "source"
            (source_root / "ontologies/onto_gorenuble").mkdir(parents=True, exist_ok=True)

            source = {
                "Dom_01_Estructura": {
                    "Existenciales": [{"ID": "CQ-001", "Q": "¿Qué es un GORE?"}],
                    "Relacionales": [{"ID": "CQ-002", "Q": "¿Qué división participa?"}],
                }
            }
            (source_root / "ontologies/onto_gorenuble/goreNubleCQs_Master.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gn-cqs-master.md",
                "urn:gn:kb:gn-cqs-master",
                "Catálogo Maestro de Preguntas de Competencia",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                        },
                        "defaults": {
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["ontologies/onto_gorenuble/goreNubleCQs_Master.yml"],
                                "source_type": "ontology_yaml",
                                "target_path": "gn-cqs-master.md",
                                "target_urn": "urn:gn:kb:gn-cqs-master",
                                "transform_class": "derive_ttl_scope",
                                "document_family": "cq_catalog",
                                "scope_statement": "Preguntas maestras del dominio GN.",
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "cqsummary")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "cqsummary", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "cqsummary")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            _frontmatter, body = load_markdown_parts(repo / "drafts/gn/gn-cqs-master.md")
            self.assertIn("## Resumen", body)
            self.assertIn("Preguntas maestras del dominio GN.", body)
            self.assertIn("Total de CQs: 2", body)

    def test_cutover_routes_control_publication_out_of_knowledge(self):
        with TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir) / "repo"
            repo.mkdir()
            for directory in ("scripts", "knowledge/gn", "inbox/gn", "source/gn", "drafts/gn", "build", "docs/reports"):
                (repo / directory).mkdir(parents=True, exist_ok=True)

            self._write_kora_stub(repo)

            source_root = Path(tmpdir) / "source"
            (source_root / "domains/gn/00_meta").mkdir(parents=True, exist_ok=True)

            source = {
                "_manifest": {"urn": "urn:test:kb:inventory"},
                "Taxonomia_Conocimiento": {
                    "Purp": "Organizar dominios.",
                    "Gobernanza": {"Def": "Gobernanza", "Areas": ["Planificación"]},
                },
                "Indice_Artefactos": {
                    "Gobernanza": {
                        "Titulo": "Artefactos de gobernanza",
                        "Artefactos": [{"id": "kb_gn_001", "nombre": "Documento base", "path": "gn/001.yml", "tipo": "KODA"}],
                    }
                },
            }
            (source_root / "domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml").write_text(
                yaml.safe_dump(source, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

            self._write_md(
                repo / "knowledge/gn/gobernanza/matriz-integracion-organica.md",
                "urn:gn:kb:matriz-integracion-organica",
                "Matriz Integración Orgánica",
            )

            map_path = repo / "scripts/gn_rebuild_map.yml"
            map_path.write_text(
                yaml.safe_dump(
                    {
                        "config": {
                            "source_root": str(source_root),
                            "inbox_root": "inbox/gn",
                            "source_mirror_root": "source/gn",
                            "draft_root": "drafts/gn",
                            "knowledge_root": "knowledge/gn",
                            "control_draft_root": "drafts/gn-control",
                            "control_root": "docs/reports/gn-control",
                        },
                        "defaults": {
                            "source_type": "koda_yaml",
                            "transform_class": "korafy_direct",
                            "review_gate": "auto",
                            "dependencies": [],
                            "expected_sections": ["Contenido"],
                        },
                        "entries": [
                            {
                                "source_paths": ["domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml"],
                                "target_path": "gobernanza/matriz-integracion-organica.md",
                                "target_urn": "urn:gn:kb:matriz-integracion-organica",
                                "document_family": "inventory",
                                "publication_class": "control",
                            }
                        ],
                        "exclusions": [],
                    },
                    sort_keys=False,
                    allow_unicode=True,
                ),
                encoding="utf-8",
            )

            freeze = self._run("--repo-root", str(repo), "--map-path", str(map_path), "freeze-source", "--run-id", "controlcut")
            self.assertEqual(freeze.returncode, 0, freeze.stderr or freeze.stdout)
            build = self._run("--repo-root", str(repo), "--map-path", str(map_path), "build", "--run-id", "controlcut", "--clean")
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            cutover = self._run("--repo-root", str(repo), "--map-path", str(map_path), "cutover", "--run-id", "controlcut")
            self.assertEqual(cutover.returncode, 0, cutover.stderr or cutover.stdout)

            self.assertFalse((repo / "knowledge/gn/gobernanza/matriz-integracion-organica.md").exists())
            control_doc = repo / "docs/reports/gn-control/gobernanza/matriz-integracion-organica.md"
            self.assertTrue(control_doc.exists())
            frontmatter, _body = load_markdown_parts(control_doc)
            self.assertEqual(frontmatter["status"], "published")


if __name__ == "__main__":
    unittest.main()
