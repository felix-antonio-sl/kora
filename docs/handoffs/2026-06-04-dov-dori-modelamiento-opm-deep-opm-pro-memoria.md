# Memoria — Dori/modelamiento-opm/deep-opm-pro

Consolidacion 2026-06-04:

- `modelamiento-opm v1.5.1` es la fuente KORA que consume
  `deep-opm-pro.log-decisiones.v0` mediante estado `re-elicitar`.
- Regla clave: solo `ratificado-con-fuente` con `fuente` presente muta anclas;
  `anotado-en-mesa` no muta.
- `dov-dori v1.2.1` no duplica mecanica: conduce, exige funcion/ontologia y
  delega serializacion/re-elicitacion a `modelamiento-opm v1.5.1`.
- `AnclaNormativa` vive como extension meta declarada, no como primitiva OPM.
- KORA desplego ambos artefactos a `claude-code`, `codex`, `opencode` y
  `openclaw`. `deploy-status`: `ok:196 stale:0 missing:0 unsupported:0`.
- `deep-opm-pro` fue verificado y remediado: se agrego test de store para
  HU-15.008, se re-sincronizo dashboard HU y `quality:gate` vuelve a PASS.
- Commit externo `deep-opm-pro`: `b602609 test(canvas): cover automatic fan evidence`.
- Excluir de futuros commits KORA los documentos salud sin trackear, salvo
  instruccion explicita.
