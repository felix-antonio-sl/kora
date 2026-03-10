---
_manifest:
  urn: urn:gn:kb:guia-idi-sni-sts-p02
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_024_guia_idi_sni_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- idi
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_024_guia_idi_sni_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_024_guia_idi_sni_koda.yml: 27498c2f7e5b50b99638989c8b70acde4909175d98cedfc6d56ca2eec3664ed4
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.24
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 2
    meat_count: 534
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/guias__guia-idi-sni-sts.md.json
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:guia-idi-sni-sts
---

# Guía de Formulación de Iniciativas de Inversión (IDI) en el SNI para Gobiernos Regionales - Parte 02

## Sec 6 Ejecucion y Transferencias
- **XRef Required:** [Partida 31: Gobiernos Regionales - Ley de Presupuestos 2026](urn:gn:kb:ley-presupuestos-2026-partida-31), [Partida 31: Gobiernos Regionales - Ley de Presupuestos 2026](urn:gn:kb:ley-presupuestos-2026-partida-31), [Ley de Presupuestos 2026: Normas Generales](urn:gn:kb:ley-presupuestos-2026-normas-generales)
### Restricciones Presupuesto 2026
### Glosa 03
- **XRef Required:** [Partida 31: Gobiernos Regionales - Ley de Presupuestos 2026](urn:gn:kb:ley-presupuestos-2026-partida-31)
- **Contenido:** Los recursos de los presupuestos de inversión regional no podrán financiar préstamos, gastos en personal, o gastos en bienes y servicios de consumo de las entidades receptoras. Asimismo, no podrán destinarse para constituir, efectuar aportes o comprar sociedades o empresas.

### Glosa 04
- **XRef Required:** [Partida 31: Gobiernos Regionales - Ley de Presupuestos 2026](urn:gn:kb:ley-presupuestos-2026-partida-31)
- **Contenido:** Se podrán traspasar recursos desde cualquier Subtítulo e Ítem del presupuesto de inversión del Gobierno Regional respectivo a los Subtítulos 24, 26, 29, 31, 32.06, 33 y 34.07.
Los gobiernos regionales podrán realizar convenios de mandato con los municipios de acuerdo con el artículo 16 de la ley N°18.091, para el financiamiento de estudios definidos en el subtítulo 22 ítem 11, del Decreto de Hacienda N° 854 del 2004, sobre clasificaciones presupuestarias.

### Articulo 07
- **XRef Required:** [Ley de Presupuestos 2026: Normas Generales](urn:gn:kb:ley-presupuestos-2026-normas-generales)
- **Proposito:** Reglas para decretos con transferencias (Subtítulos 24 y 33).
### Decretos Transferencias
- **Subtitulos:** Subtítulo 24: Transferencias Corrientes, Subtítulo 33: Transferencias de Capital
- **Puede Indicar:** Uso o destino que la institución receptora deberá dar a los recursos, Condiciones o modalidades de reintegro, Información sobre aplicación a remitir y organismo destinatario
### Transferencias Subtitulo24 Unidades Programas
- **Condiciones:** Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste
- **Resultados:** Desglose constituye autorización máxima de gasto por concepto
- **Proc Modificacion:** Modificaciones mediante igual procedimiento
### Requisitos
- **Desc:** Desglose previo a la ejecución presupuestaria en conceptos de gasto
- **Referencias:** SNI-ACTOR-DIPRES-01
### Req Reporte
- **Frecuencia:** Mensual
- **Destinatario:** DIPRES
- **Contenido:** Informe avance actividades, Información ejecución presupuestaria
### Contexto
- **Visacion:** Puede efectuarse desde fecha publicación de esta ley
### Prohibiciones
- **Desc:** No incluir recursos para gastos en personal ni bienes y servicios de consumo
- **Condiciones:** Salvo autorización por norma expresa en el respectivo presupuesto
### Res Personal
- **Resultados:** Personal contratado con cargo a dichos recursos no forma parte de la dotación del Servicio
### Ejecucion Directa GORE
- **Definicion:** GORE actúa como Unidad Técnica y Financiera, licitando, contratando y pagando directamente.
- **Imputacion:** Generalmente Subtítulo 31 – Iniciativas de Inversión.
### Ejecucion Terceros Transferencias
- **Contexto:** El GORE monitorea avance físico, incluso cuando la ejecución presupuestaria recae en otra entidad.
### Tipos
| ID | Cpt | Receptor_Tipico | Mech |
| --- | --- | --- | --- |
| SNI-TRANSF-NC-01 | Transferencia Directa (No Consolidable) | Municipalidades., Entidades privadas sin fines de lucro. | Convenio de transferencia GORE–receptor., Toma de razón (según corresponda)., Rendición de cuentas detallada al GORE. |
| SNI-TRANSF-CONS-01 | Transferencia Consolidable | Ministerios y servicios públicos con presupuesto en Ley de Presupuestos. | Decreto de DIPRES que rebaja presupuesto del GORE y aumenta el de la entidad receptora., Gasto se registra en presupuesto de la entidad receptora. |

## Sec 7 Procedimientos Especiales
### FRIL Exencion 5000 UTM
- **Definicion:** Proyectos FRIL < 5.000 UTM no requieren informe favorable MDSyF, pero deben ingresar información necesaria al SNI para control/registro.
- **Proposito:** Agilizar inversión en infraestructura menor a escala local.
- **Contexto:** Se rige por glosas específicas y guía operativa detallada del GORE., kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-12
### Proyectos Conservacion Circular 33
- **Definicion:** Procedimiento simplificado para proyectos de conservación de infraestructura pública.
- **Contexto:** Marco normativo en Circular 33 y normativa asociada.
### Reconstruccion Emergencias
- **Proposito:** Permitir inversión ágil para reparar o reponer infraestructura dañada por desastres.
- **Clasificacion BIP:** Con decreto de zona de catástrofe: descriptor BIP específico, ficha de daños obligatoria., Sin decreto pero con criticidad: descriptor 'Emergencia' más acto administrativo que la declara.
- **Proc Agilizados:** Prioridad de revisión MDSF (plazo máximo 10 días hábiles)., Posibilidad de postular ejecución incluyendo diseño, con hito de aprobación de diseño previo a obras.
- **Tipos Intervencion:** Reparación: Recupera estándar y capacidad original., Reposición sin cambio de capacidad., Reposición con cambio de capacidad (sigue reglas estándar del SNI, no agilizadas).
