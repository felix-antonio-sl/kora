import subprocess
import sys
import tempfile
import textwrap
import unittest
import os
from pathlib import Path
from uuid import uuid4

from common import FIXTURES, ROOT, assert_path_in_output, run_cli, skill_artifact_dir
from kora_lib.artifacts import load_markdown_parts
from kora_lib.atomize import _atomic_frontmatter, _build_source_docs, _deduplicate_candidates, _extract_candidates
from kora_lib.promote import _atomic_bundle_paths
from kora_lib.validation import _collect_atomic_bundle_paths
from kora_lib.validation import lint_kora_markdown_parts, parse_atomic_propositions


ATOMIZE_DIR = skill_artifact_dir("kora", "atomize")


def write_atomic_acceptance_review(path: Path, bundle_root: str, *, decision: str = "accept", publish_ready: bool = True):
    path.write_text(
        textwrap.dedent(
            f"""\
            ---
            review_type: atomic_acceptance
            decision: {decision}
            publish_ready: {str(publish_ready).lower()}
            bundle_root: {bundle_root}
            ---

            # Atomic Acceptance Review

            Bundle de prueba para gate de promote.
            """
        ),
        encoding="utf-8",
    )


class AtomizeCliTests(unittest.TestCase):
    def test_atomic_frontmatter_uses_canonical_status_and_producer(self):
        frontmatter = _atomic_frontmatter("demo", Path("source.txt"), 1, False, "single")
        self.assertEqual(frontmatter["status"], "borrador")
        self.assertEqual(
            frontmatter["extensions"]["kora"]["atomic"]["producer"],
            "urn:kora:artefacto:atomize",
        )

    def test_review_atomic_acceptance_blocks_publish_ready_when_quality_fails(self):
        review_script = ATOMIZE_DIR / "scripts" / "review_atomic_acceptance.py"

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            artifact_path = tmpdir / "atomic-demo.md"
            artifact_path.write_text(
                textwrap.dedent(
                    """\
                    ---
                    status: draft
                    extensions:
                      kora:
                        family: atomic
                        atomic:
                          producer: urn:kora:artefacto:atomize
                          source_corpus: ./fuente.md
                          n_propositions: 1
                          segmented: false
                          segment_role: single
                          hand_edited: false
                    ---

                    # Atomic demo

                    ## Resumen

                    - Productor canonico: `urn:kora:artefacto:atomize`
                    - Corpus fuente: `./fuente.md`
                    - Proposiciones: `1`
                    - Fuentes: `1`
                    - Segmentado: `no`

                    ## Indice de fuentes

                    - `S01` · [fuente.md](./fuente.md) · Fuente de prueba

                    ## Dominio

                    - **P001** · `fact` · Hecho verificable minimo. · [src:S01:L10-L12](./fuente.md#L10-L12)
                    """
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(review_script),
                    str(artifact_path),
                    "--decision",
                    "accept",
                    "--summary",
                    "Intento de cierre sobre un draft demasiado pequeno.",
                ],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("publish_ready: no", result.stdout)

            review_path = tmpdir / "atomic-demo-review.md"
            self.assertTrue(review_path.exists())
            review_frontmatter, review_body = load_markdown_parts(review_path)
            self.assertEqual(review_frontmatter["review_type"], "atomic_acceptance")
            self.assertFalse(review_frontmatter["publish_ready"])
            self.assertIn("editorial_quality", review_frontmatter["blockers"])
            self.assertIn("## Semantic Fidelity Packet", review_body)

    def test_prepare_atomic_fidelity_review_prioritizes_tension_samples(self):
        review_script = ATOMIZE_DIR / "scripts" / "prepare_atomic_fidelity_review.py"
        fixture_dir = FIXTURES / "atomize" / "multifile-negation-conflict"

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()
            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-negation-conflict.md"
            result = subprocess.run(
                [
                    sys.executable,
                    str(review_script),
                    str(artifact_path),
                    "--sample-size",
                    "1",
                ],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("tension_count: 1", result.stdout)
            self.assertIn("sample_contains_tension: yes", result.stdout)
            self.assertIn("`tension`", result.stdout)
            self.assertIn("selection_reason: tension", result.stdout)

    def test_atomize_cli_generates_valid_single_atomic_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus"
            output_dir = tmpdir / "out"
            corpus.mkdir()
            output_dir.mkdir()
            (corpus / "doc.md").write_text(
                textwrap.dedent(
                    """\
                    # Manual de prueba

                    ## Alcance

                    Este procedimiento aplica a todos los operadores del sistema.

                    - El operador debe registrar cada evento dentro de 5 dias.
                    - El sistema puede aceptar correcciones posteriores.
                    """
                ),
                encoding="utf-8",
            )

            result = run_cli("atomize", str(corpus), "--output", str(output_dir))
            self.assertIn("segmented: no", result.stdout)

            artifact_path = output_dir / "atomic-corpus.md"
            self.assertTrue(artifact_path.exists())

            frontmatter, body = load_markdown_parts(artifact_path)
            self.assertEqual(frontmatter["extensions"]["kora"]["family"], "atomic")
            self.assertIn("## Indice de fuentes", body)
            self.assertIn("**P001**", body)
            self.assertRegex(body, r"\*\*P001\*\* · `scope` · .+ · \[src:S01:L\d+\]\(")
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_cli_infers_book_structure_from_plain_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            source = tmpdir / "sample-book.txt"
            output_dir = tmpdir / "out"
            output_dir.mkdir()
            source.write_text(
                textwrap.dedent(
                    """\
                    Book Title
                    Table of Contents
                    PART I Model-Based Systems Engineering Introduced
                    Chapter 1 Ready to Start Modeling? ................................................................................ 3
                    1.1 The Automatic Crash Response System ........................................................................ 3
                    Chapter 1
                    Ready to Start Modeling?
                    “All models are wrong.”
                    Box and Draper (1987)
                    We live in a world of interconnected systems. Formal diagrams help specify complex ideas.
                    1.1 The Automatic Crash Response System
                    The system uses GPS and cellular technology to link the vehicle and driver to the center.
                    2This is a footnote that should be suppressed.
                    continued footnote text should also disappear.
                    4
                    Running Header
                    The chapter continues with a real proposition.
                    1
                    © Springer Science+Business Media New York 2016
                    Chapter 2
                    Text and Simulation Enhancements
                    Language enhances understanding of systems. Models combine graphics with text.
                    2.1 OPL: A Subset of English
                    OPL is the textual modality of OPM.
                    """
                ),
                encoding="utf-8",
            )

            run_cli("atomize", str(source), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-sample-book.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            self.assertEqual(frontmatter["extensions"]["kora"]["family"], "atomic")
            self.assertIn("Chapter 1 Ready to Start Modeling?", body)
            self.assertIn("1.1 The Automatic Crash Response System", body)
            self.assertIn("Chapter 2 Text and Simulation Enhancements", body)
            self.assertNotIn("Table of Contents", body)
            self.assertNotIn("Springer Science+Business Media", body)
            self.assertNotIn("All models are wrong", body)
            self.assertNotIn("continued footnote text", body)
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_plain_text_preserves_original_line_numbers_in_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            source = tmpdir / "source.txt"
            source.write_text(
                textwrap.dedent(
                    """\
                    Book Title
                    Table of Contents
                    Chapter 1 Sample ................................................................................ 3
                    1.1 Intro .............................................................................................. 3
                    Chapter 1
                    Sample
                    Running Header
                    This is the first real sentence in the chapter.
                    """
                ),
                encoding="utf-8",
            )

            source_doc = _build_source_docs([source], source.parent, tmpdir)[0]
            propositions = _deduplicate_candidates(_extract_candidates(source_doc))

            self.assertEqual(len(propositions), 1)
            self.assertEqual(propositions[0].sources[0].line_start, 8)
            self.assertEqual(propositions[0].sources[0].line_end, 8)

    def test_atomize_cli_recovers_dirty_ocr_fixture(self):
        fixture_path = FIXTURES / "atomize" / "ocr-dirty-procedure.txt"
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()

            run_cli("atomize", str(fixture_path), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-ocr-dirty-procedure.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            propositions = parse_atomic_propositions(body)

            self.assertEqual(len(propositions), 7)
            self.assertIn("Incident Response Procedure / 1. Scope", body)
            self.assertIn("This procedure applies to all contracted operators.", body)
            self.assertIn("The field supervisor may escalate high-risk incidents to the response lead.", body)
            self.assertNotIn("OPERATIONS MANUAL 2024", body)
            self.assertNotIn("Figure 1 Incident Flow", body)
            self.assertNotIn("Continued on next page", body)
            self.assertEqual(propositions[0]["type"], "scope")
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_cli_multifile_dedup_fixture_preserves_multiple_sources(self):
        fixture_dir = FIXTURES / "atomize" / "multifile-dedup"
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()

            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-dedup.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            propositions = parse_atomic_propositions(body)

            self.assertEqual(len(propositions), 4)
            merged = next(
                proposition
                for proposition in propositions
                if proposition["text"] == "The operator must log each incident within 24 hours."
            )
            self.assertEqual(len(merged["sources"]), 3)
            self.assertEqual({source["label"] for source in merged["sources"]}, {"src:S01:L5", "src:S02:L5", "src:S03:L5"})
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_cli_multifile_conflict_fixture_emits_tension(self):
        fixture_dir = FIXTURES / "atomize" / "multifile-conflict"
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()

            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-conflict.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            propositions = parse_atomic_propositions(body)

            self.assertEqual(len(propositions), 4)
            tension = next(proposition for proposition in propositions if proposition["type"] == "tension")
            self.assertIn("Sources disagree on the same claim", tension["text"])
            self.assertIn("24 hours", tension["text"])
            self.assertIn("48 hours", tension["text"])
            self.assertEqual(len(tension["sources"]), 2)
            self.assertIn("## Tensiones entre fuentes · Incident Logging", body)
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_cli_multifile_negation_conflict_emits_tension(self):
        fixture_dir = FIXTURES / "atomize" / "multifile-negation-conflict"
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()

            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-negation-conflict.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            propositions = parse_atomic_propositions(body)

            self.assertEqual(len(propositions), 3)
            tension = next(proposition for proposition in propositions if proposition["type"] == "tension")
            self.assertIn("may access the archive", tension["text"])
            self.assertIn("may not access the archive", tension["text"])
            self.assertEqual(len(tension["sources"]), 2)
            self.assertIn("## Tensiones entre fuentes · Archive Access", body)
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomize_cli_multifile_exception_conflict_emits_tension(self):
        fixture_dir = FIXTURES / "atomize" / "multifile-exception-conflict"
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()

            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-exception-conflict.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            propositions = parse_atomic_propositions(body)

            self.assertEqual(len(propositions), 3)
            tension = next(proposition for proposition in propositions if proposition["type"] == "tension")
            self.assertIn("applies to all contractors", tension["text"])
            self.assertIn("except temporary staff", tension["text"])
            self.assertEqual(len(tension["sources"]), 2)
            self.assertIn("## Tensiones entre fuentes · Contractor Scope", body)
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_atomic_lint_accepts_inline_single_source_form_from_md_spec(self):
        body = textwrap.dedent(
            """\
            # Atomic prueba

            ## Resumen

            - Productor canonico: `urn:kora:artefacto:atomize`
            - Corpus fuente: `./fuente.md`
            - Proposiciones: `1`
            - Fuentes: `1`
            - Segmentado: `no`

            ## Indice de fuentes

            - `S01` · [fuente.md](./fuente.md) · Fuente de prueba

            ## Dominio

            - **P001** · `fact` · Hecho verificable minimo. · [src:S01:L10-L12](./fuente.md#L10-L12)
            """
        )
        frontmatter = {
            "_manifest": {"urn": "urn:kora:kb:atomic-prueba"},
            "status": "draft",
            "extensions": {
                "kora": {
                    "family": "atomic",
                    "atomic": {
                        "producer": "urn:kora:artefacto:atomize",
                        "source_corpus": "fuente.md",
                        "n_propositions": 1,
                        "segmented": False,
                        "segment_role": "single",
                        "hand_edited": False,
                    }
                }
            },
        }
        self.assertEqual(lint_kora_markdown_parts(frontmatter, body), [])

    def test_atomize_cli_segments_on_hard_proposition_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus"
            output_dir = tmpdir / "out"
            corpus.mkdir()
            output_dir.mkdir()
            lines = ["# Doc grande", "", "## Reglas", ""]
            lines.extend(
                f"- El operador debe registrar el evento numero {index} dentro de 3 dias."
                for index in range(1, 245)
            )
            (corpus / "doc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

            result = run_cli("atomize", str(corpus), "--output", str(output_dir))
            self.assertIn("segmented: yes", result.stdout)

            outputs = sorted(output_dir.glob("atomic-corpus*.md"))
            self.assertGreaterEqual(len(outputs), 3)
            self.assertTrue((output_dir / "atomic-corpus-index.md").exists())

            index_frontmatter, index_body = load_markdown_parts(output_dir / "atomic-corpus-index.md")
            self.assertIn("| Segmento | Rango Pxxx | Dominios |", index_body)
            self.assertRegex(index_body, r"\| \[01\]\(urn:kora:kb:atomic-corpus-01\) \| P001-P\d+ \|")
            self.assertEqual(
                lint_kora_markdown_parts(index_frontmatter, index_body, path=output_dir / "atomic-corpus-index.md"),
                [],
            )

            for artifact_path in outputs:
                frontmatter, body = load_markdown_parts(artifact_path)
                self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_promote_atomic_segmented_bundle_moves_all_files(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        slug = f"test-atomize-{uuid4().hex[:10]}"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus"
            corpus.mkdir()
            lines = ["# Doc grande", "", "## Reglas", ""]
            lines.extend(
                f"- El operador debe registrar el evento numero {index} dentro de 3 dias."
                for index in range(1, 230)
            )
            (corpus / "doc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

            try:
                atomize = run_cli("atomize", str(corpus), "--slug", slug)
                self.assertIn("segmented: yes", atomize.stdout)

                review_outputs = sorted(review_dir.glob(f"atomic-{slug}*.md"))
                self.assertGreaterEqual(len(review_outputs), 3)

                index_path = review_dir / f"atomic-{slug}-index.md"
                review_path = review_dir / f"atomic-{slug}-review.md"
                write_atomic_acceptance_review(review_path, f"atomic-{slug}")
                promote = run_cli("promote", str(index_path))
                self.assertIn("PROMOTED:", promote.stdout)

                published_outputs = sorted(published_dir.glob(f"atomic-{slug}*.md"))
                self.assertEqual(len(published_outputs), len(review_outputs))
                self.assertFalse(any(path.exists() for path in review_outputs))
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_atomic_bundle_helpers_include_segments_beyond_99(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            index_path = tmpdir / "atomic-demo-index.md"
            segment_99 = tmpdir / "atomic-demo-99.md"
            segment_100 = tmpdir / "atomic-demo-100.md"
            segment_101 = tmpdir / "atomic-demo-101.md"

            for path in (index_path, segment_99, segment_100, segment_101):
                path.write_text("---\nstatus: draft\nextensions:\n  kora:\n    family: atomic\n    atomic:\n      segmented: true\n---\n", encoding="utf-8")

            frontmatter, _ = load_markdown_parts(index_path)
            promote_paths = _atomic_bundle_paths(index_path, frontmatter)
            validation_paths = _collect_atomic_bundle_paths(index_path)

            self.assertEqual(
                [path.name for path in promote_paths],
                ["atomic-demo-index.md", "atomic-demo-99.md", "atomic-demo-100.md", "atomic-demo-101.md"],
            )
            self.assertEqual(
                [path.name for path in validation_paths],
                ["atomic-demo-index.md", "atomic-demo-99.md", "atomic-demo-100.md", "atomic-demo-101.md"],
            )

    def test_atomize_cli_can_overwrite_non_hand_edited_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            source = tmpdir / "source.txt"
            output_dir = tmpdir / "out"
            output_dir.mkdir()
            source.write_text(
                textwrap.dedent(
                    """\
                    Chapter 1
                    Sample
                    The first proposition survives the first run.
                    """
                ),
                encoding="utf-8",
            )

            run_cli("atomize", str(source), "--slug", "rerun", "--output", str(output_dir))
            source.write_text(
                textwrap.dedent(
                    """\
                    Chapter 1
                    Sample
                    The second run should overwrite the previous bundle cleanly.
                    """
                ),
                encoding="utf-8",
            )

            rerun = run_cli("atomize", str(source), "--slug", "rerun", "--output", str(output_dir))
            self.assertIn("ATOMIZED:", rerun.stdout)
            artifact_path = output_dir / "atomic-rerun.md"
            frontmatter, body = load_markdown_parts(artifact_path)
            self.assertIn("second run should overwrite", body)
            self.assertEqual(lint_kora_markdown_parts(frontmatter, body, path=artifact_path), [])

    def test_publish_atomic_wrapper_requires_fresh_accepted_review(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        review_script = ATOMIZE_DIR / "scripts" / "review_atomic_acceptance.py"
        publish_script = ATOMIZE_DIR / "scripts" / "publish_atomic.py"
        slug = "test-acceptance-1234567890"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus"
            corpus.mkdir()
            lines = ["# Politica", "", "## Reglas", ""]
            lines.extend(
                f"- El operador debe registrar el evento {index} dentro de 3 dias."
                for index in range(1, 9)
            )
            (corpus / "doc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

            try:
                atomize = run_cli("atomize", str(corpus), "--slug", slug)
                self.assertIn("ATOMIZED:", atomize.stdout)

                artifact_path = review_dir / f"atomic-{slug}.md"
                review_path = review_dir / f"atomic-{slug}-review.md"

                blocked = subprocess.run(
                    [sys.executable, str(publish_script), str(artifact_path)],
                    cwd=str(ROOT),
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertNotEqual(blocked.returncode, 0)
                self.assertIn("missing acceptance review", blocked.stdout)

                accepted = subprocess.run(
                    [
                        sys.executable,
                        str(review_script),
                        str(artifact_path),
                        "--decision",
                        "accept",
                        "--summary",
                        "Bundle limpio, con gates y muestras semanticas revisadas.",
                        "--reviewer",
                        "test-suite",
                        "--sample-size",
                        "4",
                    ],
                    cwd=str(ROOT),
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(accepted.returncode, 0, accepted.stdout + accepted.stderr)
                self.assertTrue(review_path.exists())

                published = subprocess.run(
                    [sys.executable, str(publish_script), str(artifact_path)],
                    cwd=str(ROOT),
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(published.returncode, 0, published.stdout + published.stderr)
                self.assertIn("ACCEPTANCE REVIEW:", published.stdout)
                self.assertTrue((published_dir / f"atomic-{slug}.md").exists())
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_promote_atomic_requires_acceptance_review(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        slug = f"test-promote-missing-{uuid4().hex[:10]}"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus.md"
            corpus.write_text(
                "# Norma\n\n- Registrar el evento en 48 horas.\n- Mantener trazabilidad.\n",
                encoding="utf-8",
            )

            try:
                run_cli("atomize", str(corpus), "--slug", slug)

                artifact_path = review_dir / f"atomic-{slug}.md"
                blocked = run_cli("promote", str(artifact_path), check=False)
                self.assertNotEqual(blocked.returncode, 0)
                self.assertIn("missing acceptance review", blocked.stdout)
                self.assertFalse((published_dir / f"atomic-{slug}.md").exists())
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_promote_atomic_rejects_stale_acceptance_review(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        slug = f"test-promote-stale-{uuid4().hex[:10]}"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus.md"
            corpus.write_text(
                "# Norma\n\n- Registrar el evento en 48 horas.\n- Mantener trazabilidad.\n",
                encoding="utf-8",
            )

            try:
                run_cli("atomize", str(corpus), "--slug", slug)

                artifact_path = review_dir / f"atomic-{slug}.md"
                review_path = review_dir / f"atomic-{slug}-review.md"
                write_atomic_acceptance_review(review_path, f"atomic-{slug}")
                stale_ts = review_path.stat().st_mtime + 5
                os.utime(artifact_path, (stale_ts, stale_ts))

                blocked = run_cli("promote", str(artifact_path), check=False)
                self.assertNotEqual(blocked.returncode, 0)
                self.assertIn("review is stale", blocked.stdout)
                self.assertFalse((published_dir / f"atomic-{slug}.md").exists())
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_promote_atomic_accepts_fresh_review(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        slug = f"test-promote-fresh-{uuid4().hex[:10]}"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus.md"
            corpus.write_text(
                "# Norma\n\n- Registrar el evento en 48 horas.\n- Mantener trazabilidad.\n",
                encoding="utf-8",
            )

            try:
                run_cli("atomize", str(corpus), "--slug", slug)

                artifact_path = review_dir / f"atomic-{slug}.md"
                review_path = review_dir / f"atomic-{slug}-review.md"
                write_atomic_acceptance_review(review_path, f"atomic-{slug}")

                promoted = run_cli("promote", str(artifact_path))
                self.assertIn("ACCEPTANCE REVIEW:", promoted.stdout)
                self.assertIn("PROMOTED:", promoted.stdout)
                self.assertTrue((published_dir / f"atomic-{slug}.md").exists())
                self.assertFalse(artifact_path.exists())
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_promote_atomic_accepts_explicit_review_override(self):
        review_dir = ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "REVIEW" / "kora" / "atomic"
        published_dir = ROOT / "artifacts" / "knowledge" / "kora" / "atomic"
        slug = f"test-promote-override-{uuid4().hex[:10]}"

        review_dir.mkdir(parents=True, exist_ok=True)
        published_dir.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            corpus = tmpdir / "corpus.md"
            corpus.write_text(
                "# Norma\n\n- Registrar el evento en 48 horas.\n- Mantener trazabilidad.\n",
                encoding="utf-8",
            )

            try:
                run_cli("atomize", str(corpus), "--slug", slug)

                artifact_path = review_dir / f"atomic-{slug}.md"
                review_path = tmpdir / f"atomic-{slug}-custom-review.md"
                write_atomic_acceptance_review(review_path, f"atomic-{slug}")

                promoted = run_cli("promote", str(artifact_path), "--review", str(review_path))
                assert_path_in_output(self, promoted.stdout, review_path, msg="ACCEPTANCE REVIEW path missing")
                self.assertIn("PROMOTED:", promoted.stdout)
                self.assertTrue((published_dir / f"atomic-{slug}.md").exists())
                self.assertFalse(artifact_path.exists())
            finally:
                for path in review_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)
                for path in published_dir.glob(f"atomic-{slug}*.md"):
                    path.unlink(missing_ok=True)

    def test_review_atomic_acceptance_records_bundle_risk_summary(self):
        review_script = ATOMIZE_DIR / "scripts" / "review_atomic_acceptance.py"
        fixture_dir = FIXTURES / "atomize" / "multifile-negation-conflict"

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "out"
            output_dir.mkdir()
            run_cli("atomize", str(fixture_dir), "--output", str(output_dir))

            artifact_path = output_dir / "atomic-multifile-negation-conflict.md"
            result = subprocess.run(
                [
                    sys.executable,
                    str(review_script),
                    str(artifact_path),
                    "--decision",
                    "reject",
                    "--summary",
                    "Conflicto detectado; requiere veredicto humano antes de aceptar.",
                    "--sample-size",
                    "1",
                ],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            review_path = output_dir / "atomic-multifile-negation-conflict-review.md"
            review_frontmatter, review_body = load_markdown_parts(review_path)
            self.assertEqual(review_frontmatter["sample_size"], 3)
            self.assertEqual(review_frontmatter["bundle_stats"]["tension_count"], 1)
            self.assertEqual(review_frontmatter["bundle_stats"]["negation_or_exception_count"], 2)
            self.assertIn("## Bundle Risk Summary", review_body)
            self.assertIn("`tension_count`: `1`", review_body)
            self.assertIn("- Effective sample size: `3`", review_body)
