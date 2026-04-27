import unittest

from common import ROOT
from kora_lib.artifacts import load_yaml_safe


class SalubristaHodomTests(unittest.TestCase):
    def test_salubrista_declares_hospitalist_modes_and_hodom_skill(self):
        doc, err = load_yaml_safe(ROOT / "artifacts" / "agents" / "salud" / "salubrista" / "AGENT.md")
        self.assertIsNone(err)

        allowed = set(doc["extensions"]["kora"]["conocimiento_permitido"])
        self.assertIn("urn:salud:kb:salubrista", allowed)
        self.assertIn("urn:salud:kb:salubrista-atlas-integrado", allowed)
        self.assertIn("urn:salud:kb:hodom-reglamento-ds1-2022", allowed)
        self.assertIn("urn:salud:kb:hodom-norma-tecnica-2024", allowed)

        composed = set(doc["extensions"]["kora"]["componible_con"])
        self.assertIn("urn:salud:artefacto:hospitalizacion-domiciliaria", composed)

        states = {state["id"] for state in doc["artefacto"]["plan"]["estados"]}
        self.assertIn("S-HOSPITALISTA", states)
        self.assertIn("S-HODOM", states)

        modes = doc["artefacto"]["contexto"]["modos"]
        self.assertIn("hospitalista", modes)
        self.assertIn("hospitalista_domicilio", modes)

    def test_hospitalizacion_domiciliaria_skill_covers_hodom_corpus(self):
        doc, err = load_yaml_safe(
            ROOT / "artifacts" / "skills" / "salud" / "hospitalizacion-domiciliaria" / "SKILL.md"
        )
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:salud:artefacto:hospitalizacion-domiciliaria")

        allowed = set(doc["extensions"]["kora"]["conocimiento_permitido"])
        expected = {
            "urn:salud:kb:salubrista",
            "urn:salud:kb:salubrista-body-of-knowledge",
            "urn:salud:kb:gestion-redes-unidades",
            "urn:salud:kb:hodom-reglamento-ds1-2022",
            "urn:salud:kb:hodom-decreto-exento-31-2024",
            "urn:salud:kb:hodom-norma-tecnica-2024",
            "urn:salud:kb:hodom-direccion-tecnica",
            "urn:salud:kb:hodom-manual-alta-complejidad",
            "urn:salud:kb:hodom-situacion-chile-2026",
        }
        self.assertTrue(expected.issubset(allowed))

        rules = "\n".join(doc["artefacto"]["invariantes"]["reglas_duras"])
        self.assertIn("No tratar HD/HODOM como atencion domiciliaria ambulatoria", rules)
        self.assertIn("estabilidad clinica", rules)

    def test_salubrista_corpus_root_links_integrated_layers(self):
        doc, err = load_yaml_safe(ROOT / "artifacts" / "knowledge" / "salud" / "salubrista" / "index.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:salud:kb:salubrista")

        cites = set(doc["relations"]["cites"])
        self.assertIn("urn:salud:kb:salubrista-atlas-integrado", cites)
        self.assertIn("urn:salud:kb:salubrista-body-of-knowledge", cites)
        self.assertIn("urn:salud:kb:firs-framework-integrado-razonamiento-salud", cites)
        self.assertIn("urn:salud:kb:perfil-salubrista-hospitalizacion-integrada", cites)
        self.assertIn("urn:salud:kb:hodom-direccion-tecnica", cites)


if __name__ == "__main__":
    unittest.main()
