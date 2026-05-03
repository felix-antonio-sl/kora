# Family Decision Table

| Señal del input | Naturaleza | Familia / Veredicto | Funtor | Productor / Ruta | Zona inicial | Gate de salida |
|---|---|---|---|---|---|---|
| Documento descriptivo legible y orientado a lectura humana | descriptivo | KB normal | F | knowledge-curator | INBOX o REVIEW | listo para promote si pasa validación |
| Corpus denso, multi-source o de alta granularidad factual | descriptivo | atomic | F | atomize | INBOX | acceptance review + promote |
| Reglas, restricciones, contratos, workflow normativo | prescriptivo | reroute a spec | G | salir del pipeline de knowledge y derivar a authoring prescriptivo | fuera de knowledge | no promote en `artifacts/knowledge/` |
| Draft existente con shape correcto pero dudas de calidad | depende | misma familia | depende | repair guiado | REVIEW | revalidar readiness |
| Artefacto publicado con drift o defectos | depende | misma familia | depende | repair sobre publicado | publicado | revalidar o deprecar |

## Reglas

1. `atomic` no es default.
2. Un documento prescriptivo no se curte como KB normal ni se publica como knowledge.
3. Un documento descriptivo no debe ir a `spec` salvo decisión explícita de authoring prescriptivo fuera de este skill.
4. `atomize` solo aplica a la familia `atomic`.
