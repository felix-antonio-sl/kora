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
        self.assertIn("urn:salud:kb:salubrista-fuentes-base-curadas", allowed)
        self.assertIn("urn:salud:kb:salubrista-fuente-salud-publica-global", allowed)
        self.assertIn("urn:salud:kb:salubrista-fuente-management-engineering", allowed)
        self.assertIn("urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss", allowed)
        self.assertIn("urn:salud:kb:hodom-reglamento-ds1-2022", allowed)
        self.assertIn("urn:salud:kb:hodom-norma-tecnica-2024", allowed)
        self.assertNotIn("urn:salud:kb:firs-framework-integrado-razonamiento-salud", allowed)
        self.assertNotIn("urn:salud:kb:perfil-salubrista-copiloto-estrategico", allowed)
        self.assertNotIn("urn:salud:kb:perfil-salubrista-hospitalizacion-integrada", allowed)

        composed = set(doc["extensions"]["kora"]["componible_con"])
        self.assertIn("urn:salud:artefacto:firs-razonamiento-sanitario", composed)
        self.assertIn("urn:salud:artefacto:hospitalista", composed)
        self.assertIn("urn:salud:artefacto:hospitalizacion-domiciliaria", composed)
        states = {state["id"] for state in doc["artefacto"]["plan"]["estados"]}
        self.assertIn("S-HOSPITALISTA", states)
        self.assertEqual(doc["artefacto"]["composicion"]["sub_agentes"], [])
        self.assertEqual(doc["artefacto"]["composicion"]["delegacion"]["max_depth"], 0)
        self.assertIn("urn:salud:artefacto:hospitalista", doc["artefacto"]["composicion"]["skills"])

    def test_hospitalista_skill_covers_intrahospital_corpus(self):
        doc, err = load_yaml_safe(ROOT / "artifacts" / "skills" / "salud" / "hospitalista" / "SKILL.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:salud:artefacto:hospitalista")

        allowed = set(doc["extensions"]["kora"]["conocimiento_permitido"])
        expected = {
            "urn:salud:kb:salubrista",
            "urn:salud:kb:salubrista-body-of-knowledge",
            "urn:salud:kb:salubrista-fuentes-base-curadas",
            "urn:salud:kb:salubrista-fuente-management-engineering",
            "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss",
            "urn:salud:kb:gestion-redes-unidades",
            "urn:salud:kb:gestion-redes-urgencias",
            "urn:salud:kb:gestion-redes-herramientas",
        }
        self.assertTrue(expected.issubset(allowed))
        self.assertNotIn("urn:salud:kb:firs-framework-integrado-razonamiento-salud", allowed)
        self.assertNotIn("urn:salud:kb:perfil-salubrista-hospitalizacion-integrada", allowed)

        composed = set(doc["extensions"]["kora"]["componible_con"])
        self.assertIn("urn:salud:artefacto:firs-razonamiento-sanitario", composed)
        self.assertIn("urn:salud:artefacto:hospitalizacion-domiciliaria", composed)

        rules = "\n".join(doc["artefacto"]["invariantes"]["reglas_duras"])
        self.assertIn("No reducir presion de camas", rules)
        self.assertIn("management engineering", rules)

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
            "urn:salud:kb:salubrista-fuentes-base-curadas",
            "urn:salud:kb:salubrista-fuente-management-engineering",
            "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss",
            "urn:salud:kb:gestion-redes-unidades",
            "urn:salud:kb:hodom-reglamento-ds1-2022",
            "urn:salud:kb:hodom-decreto-exento-31-2024",
            "urn:salud:kb:hodom-norma-tecnica-2024",
            "urn:salud:kb:hodom-direccion-tecnica",
            "urn:salud:kb:hodom-manual-alta-complejidad",
            "urn:salud:kb:hodom-situacion-chile-2026",
        }
        self.assertTrue(expected.issubset(allowed))
        self.assertNotIn("urn:salud:kb:firs-framework-integrado-razonamiento-salud", allowed)
        self.assertNotIn("urn:salud:kb:perfil-salubrista-hospitalizacion-integrada", allowed)

        composed = set(doc["extensions"]["kora"]["componible_con"])
        self.assertIn("urn:salud:artefacto:firs-razonamiento-sanitario", composed)
        self.assertIn("urn:salud:artefacto:hospitalista", composed)

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
        self.assertIn("urn:salud:kb:salubrista-fuentes-base-curadas", cites)
        self.assertIn("urn:salud:kb:salubrista-fuente-salud-publica-global", cites)
        self.assertIn("urn:salud:kb:salubrista-fuente-management-engineering", cites)
        self.assertIn("urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss", cites)
        self.assertNotIn("urn:salud:kb:firs-framework-integrado-razonamiento-salud", cites)
        self.assertNotIn("urn:salud:kb:perfil-salubrista-hospitalizacion-integrada", cites)
        self.assertIn("urn:salud:kb:hodom-direccion-tecnica", cites)

    def test_salubrista_agent_no_longer_mentions_hah_extension(self):
        agent_path = ROOT / "artifacts" / "agents" / "salud" / "salubrista" / "AGENT.md"
        doc, err = load_yaml_safe(agent_path)
        self.assertIsNone(err)
        self.assertNotIn("salubrista-hah", agent_path.read_text(encoding="utf-8"))
        self.assertNotIn("S-HAH-ROUTE", agent_path.read_text(encoding="utf-8"))

    def test_salubrista_curated_source_layer_accounts_for_inbox_without_duplication(self):
        doc, err = load_yaml_safe(
            ROOT / "artifacts" / "knowledge" / "salud" / "salubrista" / "fuentes-base-curadas.md"
        )
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:salud:kb:salubrista-fuentes-base-curadas")
        self.assertEqual(doc["extensions"]["kora"]["role"], "curated_source_layer")
        self.assertIn("raw_public_health", doc["extensions"]["kora"]["source_paths"])

        policy = doc["extensions"]["kora"]["anti_duplication_policy"]
        self.assertIn("No copiar crudos", policy)

    def test_salubrista_sources_are_physically_integrated_and_profiles_are_deprecated(self):
        source_paths = [
            ROOT / "artifacts" / "knowledge" / "salud" / "salubrista" / "fuentes" / "salud-publica-global.md",
            ROOT / "artifacts" / "knowledge" / "salud" / "salubrista" / "fuentes" / "management-engineering-sanitario.md",
            ROOT / "artifacts" / "knowledge" / "salud" / "salubrista" / "fuentes" / "continuidad-post-aguda-ltss.md",
        ]
        urns = {
            "urn:salud:kb:salubrista-fuente-salud-publica-global",
            "urn:salud:kb:salubrista-fuente-management-engineering",
            "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss",
        }
        for path in source_paths:
            doc, err = load_yaml_safe(path)
            self.assertIsNone(err)
            self.assertIn(doc["_manifest"]["urn"], urns)
            self.assertEqual(doc["extensions"]["kora"]["corpus_root_urn"], "urn:salud:kb:salubrista")

        firs_doc, firs_err = load_yaml_safe(
            ROOT / "artifacts" / "skills" / "salud" / "firs-razonamiento-sanitario" / "SKILL.md"
        )
        self.assertIsNone(firs_err)
        self.assertEqual(firs_doc["_manifest"]["urn"], "urn:salud:artefacto:firs-razonamiento-sanitario")

        profile, profile_err = load_yaml_safe(
            ROOT / "artifacts" / "knowledge" / "salud" / "perfiles" / "salubrista-hospitalizacion-integrada.md"
        )
        self.assertIsNone(profile_err)
        self.assertEqual(profile["status"], "deprecado")


if __name__ == "__main__":
    unittest.main()
