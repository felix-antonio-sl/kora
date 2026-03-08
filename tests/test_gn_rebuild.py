import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml


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
            self.assertTrue(manual.exists())
            self.assertTrue(csv_doc.exists())
            self.assertIn("extensions:", manual.read_text(encoding="utf-8"))
            self.assertIn("source_paths", manual.read_text(encoding="utf-8"))

            validate = self._run("--repo-root", str(repo), "--map-path", str(map_path), "validate", "--run-id", "testrun")
            self.assertEqual(validate.returncode, 0, validate.stderr or validate.stdout)

            report = self._run("--repo-root", str(repo), "--map-path", str(map_path), "report", "--run-id", "testrun")
            self.assertEqual(report.returncode, 0, report.stderr or report.stdout)
            report_path = repo / "build/gn-rebuild/testrun/report.md"
            self.assertTrue(report_path.exists())
            self.assertIn("Structural Diff", report_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
