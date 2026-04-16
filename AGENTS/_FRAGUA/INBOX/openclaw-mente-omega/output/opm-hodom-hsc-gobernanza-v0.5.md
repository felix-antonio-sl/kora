# Modelo OPM — HODOM HSC
# SD3 — Gobernar Sistema HODOM HSC

Versión: 0.5
Fecha: 2026-04-09
Estado: borrador de gobernanza operativa

Propósito de esta versión: formalizar la capa de gobierno del sistema HODOM HSC, diferenciándola de la capa asistencial episódica.

## Convención de evidencia

- [N] Normativa HODOM
- [S] Sistema/repositorio HSC (`hdos-app`, `hdos`)
- [M] Modelo OPM previo
- [H] Hipótesis pendiente de validación local

## Fuentes base

### Normativa
- [N] `01-reglamento-hodom-ds1-2022.md`
- [N] `03-norma-tecnica-hodom-2024.md`

### Sistema HSC
- [S] `hdos-app/README.md`
- [S] `hdos-app/docs/specs/00-INDICE.md`
- [S] `hdos-app/docs/specs/01-diseno-sistema-operativo-hodom-hsc.md`
- [S] `hdos/README.md`

### Modelos previos
- [M] `opm-hodom-normativo-v1.0.md`
- [M] `opm-hodom-model-v2.5.md`
- [M] `opm-hodom-hsc-procesos-v0.4.md`

---

# 1. Tesis de esta capa

La HODOM HSC no se gobierna solo mediante personas con autoridad. Se gobierna mediante procesos informaticales que actúan sobre el sistema mismo.

Eso significa que el sistema exhibe, además de *Hospitalizar en Domicilio*, un segundo gran proceso:

**Gobernar Sistema HODOM HSC**. [N][M][H]

Este segundo proceso transforma al propio sistema sobre seis frentes:
- autorización y cumplimiento,
- protocolos,
- continuidad operativa y capacidad,
- calidad y seguridad,
- consistencia estadística,
- desarrollo de competencias.

---

# 2. SD3 propuesto

## 2.1 Proceso principal de gobierno

**EN:** *System Governing* [M]
**ES:** *Gobernar Sistema HODOM HSC* [M][H]

## 2.2 Exhibición propuesta

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Gobernar Sistema HODOM HSC* así como *Hospitalizar en Domicilio*.
```

## 2.3 Subprocesos de SD3

```opl
SD se refina por descomposición de *Gobernar Sistema HODOM HSC* en SD3.
*Gobernar Sistema HODOM HSC* se descompone en *Gestionar Autorización y Cumplimiento*, *Gobernar Protocolos y Procedimientos*, *Gestionar Capacidad y Continuidad Operativa*, *Auditar Calidad y Seguridad*, *Validar Observabilidad y REM* y *Gestionar Desarrollo de Competencias*, en paralelo.
```

---

# 3. Tabla de elementos SD3

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Gobernar Sistema HODOM HSC* | Informatical | Sistémico | — | [N][M][H] |
| Proceso | *Gestionar Autorización y Cumplimiento* | Informatical | Sistémico | — | [N][H] |
| Proceso | *Gobernar Protocolos y Procedimientos* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Gestionar Capacidad y Continuidad Operativa* | Informatical | Sistémico | — | [N][S][H] |
| Proceso | *Auditar Calidad y Seguridad* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Validar Observabilidad y REM* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Gestionar Desarrollo de Competencias* | Informatical | Sistémico | — | [N][M] |
| Objeto | **Estado de Autorización Sanitaria** | Informatical | Sistémico | `vigente`, `observada`, `vencida` | [N][H] |
| Objeto | **Conjunto de Protocolos** | Informatical | Sistémico | `desactualizado`, `vigente` | [N][M] |
| Objeto | **Capacidad Operativa** | Informatical | Sistémico | `suficiente`, `estresada`, `insuficiente` | [S][H] |
| Objeto | **Cumplimiento de Continuidad** | Informatical | Sistémico | `estable`, `riesgo de quiebre` | [N][S][H] |
| Objeto | **Estado de Calidad y Seguridad** | Informatical | Sistémico | `conforme`, `en observación`, `crítico` | [N][H] |
| Objeto | **Estado de Observabilidad** | Informatical | Sistémico | `consistente`, `inconsistente` | [S][H] |
| Objeto | **Cumplimiento de Competencias** | Informatical | Sistémico | `no cumple`, `cumple` | [N][M] |
| Objeto | **Director Técnico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Profesional Coordinador** | Físico | Sistémico | — | [N][M] |
| Objeto | **SEREMI** | Físico | Ambiental | — | [N][M] |
| Objeto | **Normativa Vigente** | Informatical | Ambiental | — | [N][M] |
| Objeto | **REM A21** | Informatical | Sistémico | `generado`, `validado` | [S][M] |
| Objeto | **Ficha Clínica** | Informatical | Sistémico | `abierta`, `cerrada` | [N][S][M] |
| Objeto | **Llamado Clínico** | Informatical | Sistémico | `recibido`, `triageado`, `cerrado` | [S][H] |
| Objeto | **Equipo de Salud** | Físico | Sistémico | — | [N][M] |

---

# 4. Tabla de enlaces SD3

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Gobernar Sistema HODOM HSC* | 6 subprocesos | RF6 | [M] |
| Effect (input-output) | *Gestionar Autorización y Cumplimiento* | **Estado de Autorización Sanitaria** | TS3 | [N][H] |
| Instrument | *Gestionar Autorización y Cumplimiento* | **SEREMI** | H2 | [N][M] |
| Instrument | *Gestionar Autorización y Cumplimiento* | **Normativa Vigente** | H2 | [N][M] |
| Agent | **Director Técnico** | *Gestionar Autorización y Cumplimiento* | H1 | [N][M] |
| Effect (input-output) | *Gobernar Protocolos y Procedimientos* | **Conjunto de Protocolos** | TS3 | [N][M] |
| Instrument | *Gobernar Protocolos y Procedimientos* | **Normativa Vigente** | H2 | [N][M] |
| Agent | **Director Técnico** | *Gobernar Protocolos y Procedimientos* | H1 | [N][M] |
| Effect (input-output) | *Gestionar Capacidad y Continuidad Operativa* | **Capacidad Operativa** | TS3 | [S][H] |
| Effect (input-output) | *Gestionar Capacidad y Continuidad Operativa* | **Cumplimiento de Continuidad** | TS3 | [N][S][H] |
| Agent | **Profesional Coordinador** | *Gestionar Capacidad y Continuidad Operativa* | H1 | [N][M] |
| Effect (input-output) | *Auditar Calidad y Seguridad* | **Estado de Calidad y Seguridad** | TS3 | [N][H] |
| Instrument | *Auditar Calidad y Seguridad* | **Ficha Clínica** | H2 | [N][M] |
| Instrument | *Auditar Calidad y Seguridad* | **Llamado Clínico** | H2 | [S][H] |
| Agent | **Director Técnico** | *Auditar Calidad y Seguridad* | H1 | [N][M] |
| Effect (input-output) | *Validar Observabilidad y REM* | **Estado de Observabilidad** | TS3 | [S][H] |
| Instrument | *Validar Observabilidad y REM* | **REM A21** | H2 | [S][M] |
| Agent | **Profesional Coordinador** | *Validar Observabilidad y REM* | H1 | [S][H] |
| Effect (input-output) | *Gestionar Desarrollo de Competencias* | **Cumplimiento de Competencias** | TS3 | [N][M] |
| Instrument | *Gestionar Desarrollo de Competencias* | **Equipo de Salud** | H2 | [N][M] |
| Agent | **Profesional Coordinador** | *Gestionar Desarrollo de Competencias* | H1 | [N][M] |

---

# 5. OPL-ES SD3

```opl
SD se refina por descomposición de *Gobernar Sistema HODOM HSC* en SD3.
*Gobernar Sistema HODOM HSC* se descompone en *Gestionar Autorización y Cumplimiento*, *Gobernar Protocolos y Procedimientos*, *Gestionar Capacidad y Continuidad Operativa*, *Auditar Calidad y Seguridad*, *Validar Observabilidad y REM* y *Gestionar Desarrollo de Competencias*, en paralelo.

**Estado de Autorización Sanitaria** puede estar `vigente`, `observada` o `vencida`.
*Gestionar Autorización y Cumplimiento* requiere **SEREMI**.
*Gestionar Autorización y Cumplimiento* requiere **Normativa Vigente**.
*Gestionar Autorización y Cumplimiento* cambia **Estado de Autorización Sanitaria** de `observada` a `vigente`.
**Director Técnico** maneja *Gestionar Autorización y Cumplimiento*.

**Conjunto de Protocolos** puede estar `desactualizado` o `vigente`.
*Gobernar Protocolos y Procedimientos* requiere **Normativa Vigente**.
*Gobernar Protocolos y Procedimientos* cambia **Conjunto de Protocolos** de `desactualizado` a `vigente`.
**Director Técnico** maneja *Gobernar Protocolos y Procedimientos*.

**Capacidad Operativa** puede estar `suficiente`, `estresada` o `insuficiente`.
**Cumplimiento de Continuidad** puede estar `estable` o `riesgo de quiebre`.
*Gestionar Capacidad y Continuidad Operativa* cambia **Capacidad Operativa** de `estresada` a `suficiente`.
*Gestionar Capacidad y Continuidad Operativa* cambia **Cumplimiento de Continuidad** de `riesgo de quiebre` a `estable`.
**Profesional Coordinador** maneja *Gestionar Capacidad y Continuidad Operativa*.

**Estado de Calidad y Seguridad** puede estar `conforme`, `en observación` o `crítico`.
*Auditar Calidad y Seguridad* requiere **Ficha Clínica**.
*Auditar Calidad y Seguridad* requiere **Llamado Clínico**.
*Auditar Calidad y Seguridad* cambia **Estado de Calidad y Seguridad** de `en observación` a `conforme`.
**Director Técnico** maneja *Auditar Calidad y Seguridad*.

**Estado de Observabilidad** puede estar `consistente` o `inconsistente`.
*Validar Observabilidad y REM* requiere **REM A21**.
*Validar Observabilidad y REM* cambia **Estado de Observabilidad** de `inconsistente` a `consistente`.
**Profesional Coordinador** maneja *Validar Observabilidad y REM*.

**Cumplimiento de Competencias** puede estar `no cumple` o `cumple`.
*Gestionar Desarrollo de Competencias* requiere **Equipo de Salud**.
*Gestionar Desarrollo de Competencias* cambia **Cumplimiento de Competencias** de `no cumple` a `cumple`.
**Profesional Coordinador** maneja *Gestionar Desarrollo de Competencias*.
```

---

# 6. Lectura directiva del SD3

## 6.1 Qué gobierna el Director Técnico

Procesos donde la autoridad no es solo operativa, sino institucional:
- autorización y cumplimiento,
- protocolos,
- calidad y seguridad.

## 6.2 Qué gobierna la Coordinación

Procesos donde la autoridad es de continuidad, capacidad, consistencia y competencias:
- capacidad operativa,
- observabilidad y REM,
- desarrollo de competencias.

## 6.3 Qué revela esto

La Dirección Técnica no es un “superclínico”.
Es el nodo que asegura legitimidad, conformidad, protocolo y seguridad.

La Coordinación tampoco es solo agenda.
Es el nodo que sostiene continuidad, capacidad real, consistencia de operación y aprendizaje organizacional.

---

# 7. Insight fuerte

Con SD3 aparece una verdad incómoda pero útil:

si el sistema asistencial cuida pacientes,
el sistema de gobernanza cuida la posibilidad misma de seguir cuidando bien.

Cuando esta segunda capa falla, la primera se degrada aunque el equipo clínico individual sea bueno.

---

# 8. Próximo paso autónomo recomendado

La continuación natural ya no es seguir agregando procesos sueltos.
Ahora conviene construir un artefacto de consolidación:

**`opm-hodom-hsc-canonic-local-v1.0.md`**

que integre:
- SD
- SD1 asistencial-operativo
- SD3 gobernanza/observabilidad
- objetos transversales canónicos
- decisiones de frontera
- tabla de hipótesis pendientes

Ese documento puede convertirse en el primer núcleo canónico local del dominio.
