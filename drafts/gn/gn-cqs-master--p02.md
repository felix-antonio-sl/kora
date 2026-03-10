---
_manifest:
  urn: urn:gn:kb:gn-cqs-master-p02
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: ontologies/onto_gorenuble/goreNubleCQs_Master.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- competency-questions
- consultas
- knowledge
- gn
lang: es
extensions:
  gn:
    source_paths:
    - ontologies/onto_gorenuble/goreNubleCQs_Master.yml
    source_hashes:
      ontologies/onto_gorenuble/goreNubleCQs_Master.yml: 54ff9c22ace906e6a52ad6b0c08c11ff59cadc67a90e4605ba777f2a0e142bb0
    source_type: ontology_yaml
    transformation_mode: derive_ttl_scope
    fs: 100
    cr: 1.36
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Preguntas de competencia maestras del bundle ontologico GN.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: cq_catalog
    publication_class: knowledge
    skeleton_count: 21
    meat_count: 1024
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gn-cqs-master.md.json
  kora:
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:gn:kb:gn-cqs-master
---

# Catálogo Maestro de Preguntas de Competencia - Parte 02

## 06 Convenios

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-141 | ¿Qué es un Convenio de Transferencia? |
| CQ-142 | ¿Qué es un Convenio Mandato? |
| CQ-143 | ¿Qué es una Transferencia Corriente (Subtítulo 24)? |
| CQ-144 | ¿Qué es una Transferencia de Capital (Subtítulo 33)? |
| CQ-145 | ¿Qué es una garantía de fiel cumplimiento? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-146 | ¿Qué entidades pueden ser receptoras de transferencias? |
| CQ-147 | ¿Qué relación existe entre tipo de convenio y tipo de entidad receptora? |
| CQ-148 | ¿Qué división GORE gestiona los convenios? |
| CQ-149 | ¿Qué relación tiene el convenio con la Resolución aprobatoria? |
| CQ-150 | ¿Qué condiciones activan la exigencia de garantía? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-151 | ¿Cuál es el plazo para firma del convenio tras aprobación? |
| CQ-152 | ¿Cuál es el plazo para primera transferencia tras firma? |
| CQ-153 | ¿Cuál es la vigencia típica de un convenio? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-154 | ¿Cuántos convenios vigentes tiene el GORE? |
| CQ-155 | ¿Cuál es el monto total transferido en el año? |
| CQ-156 | ¿Cuántas entidades tienen convenio vigente con el GORE? |
| CQ-157 | ¿Cuántos convenios por tipo de entidad existen? |
| CQ-158 | ¿Cuántos convenios requirieron garantía? |
| CQ-159 | ¿Cuál es el monto promedio de transferencia por convenio? |
| CQ-160 | ¿Cuál es el umbral de 1.000 UTM para garantías a privados? |

## 07 Ejecucion

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-161 | ¿Qué es el seguimiento de una IPR? |
| CQ-162 | ¿Qué es un informe de avance? |
| CQ-163 | ¿Qué es el avance físico de un proyecto? |
| CQ-164 | ¿Qué es el avance financiero de un proyecto? |
| CQ-165 | ¿Qué es un ITO (Inspector Técnico de Obra)? |
| CQ-166 | ¿Qué es una modificación de proyecto? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-167 | ¿Qué unidad GORE realiza el seguimiento de IPR? |
| CQ-168 | ¿Qué relación existe entre ejecutor e informes de avance? |
| CQ-169 | ¿Qué tipos de modificaciones requieren aprobación CORE? |
| CQ-170 | ¿Qué rol cumple el ITO en el seguimiento? |
| CQ-171 | ¿Qué acciones se derivan de un incumplimiento de hitos? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-172 | ¿Con qué periodicidad se entregan informes de avance? |
| CQ-173 | ¿Cuál es el plazo máximo de ejecución de un proyecto FRIL? |
| CQ-174 | ¿Cuál es el plazo máximo de ejecución de una iniciativa FRPD? |
| CQ-175 | ¿Cuál es el plazo de ejecución de una iniciativa 8%? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-176 | ¿Cuántas IPR están en ejecución actualmente? |
| CQ-177 | ¿Cuál es el porcentaje promedio de avance físico de IPR en ejecución? |
| CQ-178 | ¿Cuántas IPR presentan retrasos en su ejecución? |
| CQ-179 | ¿Cuántas modificaciones de proyecto fueron aprobadas en el año? |
| CQ-180 | ¿Cuántos ITO están asignados a proyectos GORE? |
| CQ-181 | ¿Cuántas IPR fueron terminadas en el año vigente? |
| CQ-182 | ¿Cuál es la tasa de cumplimiento de plazos de ejecución? |

## 08 Rendicion

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-183 | ¿Qué es el SISREC (Sistema de Rendición Electrónica de Cuentas)? |
| CQ-184 | ¿Qué es una rendición de cuentas? |
| CQ-185 | ¿Qué es la Resolución N°30 de CGR? |
| CQ-186 | ¿Qué es un reparo de rendición? |
| CQ-187 | ¿Qué es el cierre administrativo de una IPR? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-188 | ¿Qué entidades deben rendir cuentas al GORE? |
| CQ-189 | ¿Qué unidad GORE revisa las rendiciones? |
| CQ-190 | ¿Qué relación existe entre rendición y cierre de convenio? |
| CQ-191 | ¿Qué acciones se derivan de rendiciones pendientes? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-192 | ¿Cuál es el plazo para rendir cuentas tras término de ejecución? |
| CQ-193 | ¿Cuál es el plazo para subsanar reparos de rendición? |
| CQ-194 | ¿Con qué periodicidad se rinden cuentas parciales? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-195 | ¿Cuántas rendiciones pendientes existen con el GORE? |
| CQ-196 | ¿Cuál es el monto total de rendiciones pendientes? |
| CQ-197 | ¿Cuántas entidades tienen rendiciones pendientes? |
| CQ-198 | ¿Cuántas rendiciones fueron aprobadas en el año? |
| CQ-199 | ¿Cuántos reparos de rendición fueron emitidos? |
| CQ-200 | ¿Cuál es la tasa de aprobación de rendiciones? |

## 09 Normativo

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-201 | ¿Qué es la LOC GORE (Ley 19.175)? |
| CQ-202 | ¿Qué es la Ley de Presupuestos (21.796)? |
| CQ-203 | ¿Qué es el DL 1.263 (Administración Financiera del Estado)? |
| CQ-204 | ¿Qué es la Ley 19.880 (Procedimientos Administrativos)? |
| CQ-205 | ¿Qué es el Oficio Circular N°33 de Hacienda? |
| CQ-206 | ¿Qué son las NIP (Normas de Inversión Pública)? |
| CQ-207 | ¿Qué es la Resolución N°30 de CGR? |
| CQ-208 | ¿Qué es la Ley 19.862 (Registro de Colaboradores del Estado)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-209 | ¿Qué leyes regulan las atribuciones del GORE? |
| CQ-210 | ¿Qué normas regulan la evaluación de proyectos SNI? |
| CQ-211 | ¿Qué normas regulan las transferencias a terceros? |
| CQ-212 | ¿Qué normas regulan las rendiciones de cuentas? |
| CQ-213 | ¿Qué relación tiene la Ley de Presupuestos con las glosas FNDR? |
| CQ-214 | ¿Qué normas regulan el concurso 8%? |
| CQ-215 | ¿Qué normas regulan el FRIL? |
| CQ-216 | ¿Qué normas regulan el FRPD? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-217 | ¿Cuál es la vigencia de la Ley de Presupuestos? |
| CQ-218 | ¿Cuándo fue promulgada la LOC GORE? |
| CQ-219 | ¿Cuándo fue emitido el Oficio Circular N°33? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-220 | ¿Cuántas leyes principales regulan el funcionamiento del GORE? |
| CQ-221 | ¿Cuántas resoluciones CGR aplican a transferencias? |
| CQ-222 | ¿Cuántos oficios circulares de Hacienda aplican al GORE? |
| CQ-223 | ¿Cuántas glosas presupuestarias tiene la Partida 31? |
| CQ-224 | ¿Cuántas metodologías NIP están vigentes? |
| CQ-225 | ¿Cuántas normas de probidad aplican a funcionarios GORE? |

## 10 TDE

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-226 | ¿Qué es la TDE (Transformación Digital del Estado)? |
| CQ-227 | ¿Qué es la Ley de TDE (21.180)? |
| CQ-228 | ¿Qué es un documento electrónico oficial? |
| CQ-229 | ¿Qué es la firma electrónica avanzada (FEA)? |
| CQ-230 | ¿Qué es GESDOC? |
| CQ-231 | ¿Qué es la interoperabilidad del Estado? |
| CQ-232 | ¿Qué es Clave Única? |
| CQ-233 | ¿Qué es el expediente electrónico? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-234 | ¿Qué relación tiene TDE con los procedimientos administrativos? |
| CQ-235 | ¿Qué organismos están obligados a implementar TDE? |
| CQ-236 | ¿Qué relación existe entre GESDOC y el BIP? |
| CQ-237 | ¿Qué servicios de interoperabilidad usa el GORE? |
| CQ-238 | ¿Qué plataformas digitales administra el GORE Ñuble? |
| CQ-239 | ¿Qué relación tiene la FEA con la validez de documentos GORE? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-240 | ¿Cuándo entró en vigencia la Ley TDE para GORE? |
| CQ-241 | ¿Cuáles son las etapas de implementación de TDE en GORE? |
| CQ-242 | ¿Cuándo debe estar completada la digitalización de trámites GORE? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-243 | ¿Cuántos trámites GORE están digitalizados? |
| CQ-244 | ¿Cuántos usuarios utilizan GESDOC en el GORE? |
| CQ-245 | ¿Cuántos documentos electrónicos fueron procesados en el año? |
| CQ-246 | ¿Cuál es el porcentaje de trámites digitalizados vs presenciales? |
| CQ-247 | ¿Cuántas firmas electrónicas avanzadas están habilitadas en el GORE? |
| CQ-248 | ¿Cuántos servicios de interoperabilidad consume el GORE? |
| CQ-249 | ¿Cuál es el nivel de madurez digital del GORE Ñuble? |

## 11 Gestion Operacional IPR

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-250 | ¿Qué es una IPR según la guía operacional? |
| CQ-251 | ¿Qué es un IDI (Iniciativa de Inversión) en contexto GORE? |
| CQ-252 | ¿Qué significa el estado PRE-ADMISIBLE CDR? |
| CQ-253 | ¿Qué estados de admisibilidad existen para una IPR? |
| CQ-254 | ¿Qué estados de financiamiento puede tener una IPR? |
| CQ-255 | ¿Qué es el Comité Directivo Regional (CDR)? |
| CQ-256 | ¿Qué es un CDP (Certificado de Disponibilidad Presupuestaria)? |
| CQ-257 | ¿Qué es el SISREC y para qué se utiliza? |
| CQ-258 | ¿Qué es un RATE y cuáles son sus valores posibles (RS, FI, OT)? |
| CQ-259 | ¿Qué significa el estado NV (No Vigente)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-260 | ¿Quién preside el Comité Directivo Regional (CDR)? |
| CQ-261 | ¿Qué relación existe entre la DIPIR y el proceso de evaluación técnica? |
| CQ-262 | ¿Qué unidad debe emitir el CDP para una IPR? |
| CQ-263 | ¿Qué organismos intervienen en el Track A (SNI)? |
| CQ-264 | ¿Quién realiza la evaluación de programas en Track B (Glosa 06)? |
| CQ-265 | ¿Qué divisiones componen el CDR? |
| CQ-266 | ¿Qué relación existe entre el CORE y la aprobación de IPR >7.000 UTM? |
| CQ-267 | ¿Qué entidad emite la RS para proyectos que ingresan al SNI? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-268 | ¿Cuál es el plazo orientativo de MDSF para evaluación de admisibilidad (Track A)? |
| CQ-269 | ¿Cuál es el plazo orientativo para el Análisis Técnico-Económico de MDSF? |
| CQ-270 | ¿Cuál es el plazo máximo para subsanar observaciones FI/OT en SNI? |
| CQ-271 | ¿Cuánto tiempo tiene el GORE para emitir el primer RATE en FRIL? |
| CQ-272 | ¿Cuánto tiempo dispone un formulador para enviar el Diseño tras aprobación de Perfil (PPR)? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-273 | ¿Cuántas fases tiene el proceso end-to-end de gestión de IPR? |
| CQ-274 | ¿Cuántos tracks de evaluación técnica existen según el tipo de IPR? |
| CQ-275 | ¿Cuántas etapas contempla la Fase 1 (Ingreso y Admisibilidad)? |
