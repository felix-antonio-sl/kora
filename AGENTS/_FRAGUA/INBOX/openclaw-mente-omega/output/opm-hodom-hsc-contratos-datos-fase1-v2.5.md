# HODOM HSC
# Contratos de Datos — Fase I

Versión: 2.5
Fecha: 2026-04-09
Estado: propuesta de contratos inicial

Propósito: definir contratos de datos suficientemente concretos para implementar Fase I sin entrar aún en DDL definitivo.

Objetos cubiertos:
- `v_estado_episodio_canonico`
- `v_plan_atencion_actual`
- `v_riesgo_episodio_actual`

---

## 1. Principio de diseño

Los contratos de Fase I deben cumplir 4 condiciones:
1. tener a `stay_id` como clave funcional central,
2. ser legibles por frontend sin reconstrucción excesiva,
3. permitir trazabilidad mínima,
4. no exigir refactor mayor inicial.

---

# 2. Contrato — `clinical.v_estado_episodio_canonico`

## 2.1 Propósito
Entregar una lectura única y compartida del estado del episodio para consumo transversal en UI y reporting operativo.

## 2.2 Clave
- `stay_id`

## 2.3 Campos propuestos

| Campo | Tipo lógico | Obligatorio | Descripción |
|------|-------------|-------------|-------------|
| `stay_id` | text/uuid | sí | identificador del episodio |
| `estado_canonico` | text | sí | postulado, elegible, admitido, activo, egresado, cerrado |
| `estado_fuente` | text | sí | estado original detectado en fuente actual |
| `tipo_egreso` | text nullable | no | causal de egreso si existe |
| `fecha_ingreso` | date/timestamp nullable | no | referencia temporal |
| `fecha_egreso` | date/timestamp nullable | no | referencia temporal |
| `fecha_estado` | timestamp nullable | no | timestamp relevante para estado actual |
| `origen_estado` | text | sí | derivado, explícito, mixto |
| `inconsistencia_estado` | boolean | sí | marca si el mapeo detecta contradicción |
| `detalle_inconsistencia` | text nullable | no | explicación breve |

## 2.4 Ejemplo de payload

```json
{
  "stay_id": "e7a4-...",
  "estado_canonico": "activo",
  "estado_fuente": "activo",
  "tipo_egreso": null,
  "fecha_ingreso": "2026-04-01",
  "fecha_egreso": null,
  "fecha_estado": "2026-04-01T10:22:00Z",
  "origen_estado": "derivado",
  "inconsistencia_estado": false,
  "detalle_inconsistencia": null
}
```

## 2.5 Reglas semánticas mínimas
- si hay `tipo_egreso`, no puede quedar como `activo`
- `cerrado` debería usarse cuando el episodio ya no solo egresó, sino que completó cierre documental/operativo
- `inconsistencia_estado = true` no bloquea consumo UI, pero debe señalizar deuda de datos

## 2.6 Consumidores iniciales
- ficha
- censo
- admisión
- egreso

---

# 3. Contrato — `clinical.v_plan_atencion_actual`

## 3.1 Propósito
Entregar una vista resumida y vigente del plan de atención del episodio, legible por clínica y coordinación.

## 3.2 Clave
- `stay_id`

## 3.3 Campos propuestos

| Campo | Tipo lógico | Obligatorio | Descripción |
|------|-------------|-------------|-------------|
| `stay_id` | text/uuid | sí | identificador del episodio |
| `plan_id` | text/uuid nullable | no | identificador técnico si existe |
| `version` | integer nullable | no | versión del plan |
| `estado_plan` | text | sí | borrador, activo, actualizado, cerrado |
| `objetivo_clinico` | text nullable | no | objetivo principal |
| `problema_principal` | text nullable | no | diagnóstico o problema central |
| `prestaciones_activas_resumen` | text nullable | no | resumen legible |
| `frecuencia_objetivo_resumen` | text nullable | no | resumen legible de frecuencia |
| `criterios_monitoreo_resumen` | text nullable | no | qué vigilar |
| `criterios_ajuste_resumen` | text nullable | no | cuándo ajustar |
| `criterios_egreso_resumen` | text nullable | no | cuándo egresar |
| `actualizado_por` | text nullable | no | profesional o usuario |
| `actualizado_en` | timestamp nullable | no | última actualización |
| `fuente_plan` | text | sí | manual, consolidado, híbrido |
| `plan_incompleto` | boolean | sí | marca operativa |
| `detalle_plan_incompleto` | text nullable | no | explicación breve |

## 3.4 Ejemplo de payload

```json
{
  "stay_id": "e7a4-...",
  "plan_id": null,
  "version": 1,
  "estado_plan": "activo",
  "objetivo_clinico": "Control clínico y manejo de descompensación respiratoria en domicilio",
  "problema_principal": "EPOC exacerbado",
  "prestaciones_activas_resumen": "Enfermería diaria, control médico, kinesiología respiratoria",
  "frecuencia_objetivo_resumen": "Visita diaria de enfermería, control médico cada 48h",
  "criterios_monitoreo_resumen": "SatO2, FR, uso de O2, signos de agotamiento",
  "criterios_ajuste_resumen": "Escalar si desatura o aumenta trabajo respiratorio",
  "criterios_egreso_resumen": "Estabilidad respiratoria mantenida y menor requerimiento de soporte",
  "actualizado_por": "Dra. X",
  "actualizado_en": "2026-04-08T14:12:00Z",
  "fuente_plan": "hibrido",
  "plan_incompleto": false,
  "detalle_plan_incompleto": null
}
```

## 3.5 Reglas semánticas mínimas
- `plan_incompleto = true` si faltan piezas esenciales para lectura clínica/operativa
- la vista no necesita resolver toda la riqueza de planes disciplinares en Fase I, solo consolidar una lectura operable
- un episodio activo sin fila en esta vista debe considerarse hallazgo de deuda operativa

## 3.6 Consumidores iniciales
- ficha
- luego censo resumido y agenda, si aporta valor

---

# 4. Contrato — `clinical.v_riesgo_episodio_actual`

## 4.1 Propósito
Entregar la categoría de riesgo vigente del episodio con trazabilidad mínima y utilidad operacional inmediata.

## 4.2 Clave
- `stay_id`

## 4.3 Campos propuestos

| Campo | Tipo lógico | Obligatorio | Descripción |
|------|-------------|-------------|-------------|
| `stay_id` | text/uuid | sí | identificador del episodio |
| `riesgo_id` | text/uuid nullable | no | identificador técnico |
| `categoria_riesgo` | text | sí | estable, en_observacion, inestable |
| `motivo_riesgo` | text nullable | no | explicación breve |
| `fuente_riesgo` | text | sí | manual, regla, híbrido |
| `actualizado_por` | text nullable | no | profesional o usuario |
| `actualizado_en` | timestamp nullable | no | última actualización |
| `accion_operativa_sugerida` | text nullable | no | lectura breve útil para coordinación |
| `riesgo_faltante` | boolean | sí | marca de deuda |

## 4.4 Ejemplo de payload

```json
{
  "stay_id": "e7a4-...",
  "riesgo_id": "r9b2-...",
  "categoria_riesgo": "en_observacion",
  "motivo_riesgo": "Saturación limítrofe y aumento de requerimiento de control",
  "fuente_riesgo": "hibrido",
  "actualizado_por": "Enf. Y",
  "actualizado_en": "2026-04-09T08:05:00Z",
  "accion_operativa_sugerida": "Mantener control estrecho y revisar en coordinación",
  "riesgo_faltante": false
}
```

## 4.5 Reglas semánticas mínimas
- el riesgo debe poder leerse en menos de 10 segundos
- la acción sugerida no reemplaza protocolo, pero ayuda a usar la señal
- `riesgo_faltante = true` es un hallazgo operativo importante

## 4.6 Consumidores iniciales
- censo
- ficha
- cockpit futuro

---

# 5. Contrato compuesto para frontend

## 5.1 Propuesta
Para la ficha del episodio, conviene un agregado de lectura rápida compuesto por:
- datos base del episodio
- estado canónico
- plan actual
- riesgo actual

### Nombre sugerido
`clinical.v_resumen_episodio_operativo`

## 5.2 Objetivo
Evitar 3 o 4 queries conceptualmente separadas en frontend cuando la necesidad de lectura es una sola.

## 5.3 Campos mínimos sugeridos
- `stay_id`
- `paciente`
- `diagnostico_principal`
- `fecha_ingreso`
- `dias_estada`
- `estado_canonico`
- `categoria_riesgo`
- `objetivo_clinico`
- `prestaciones_activas_resumen`
- `frecuencia_objetivo_resumen`
- `actualizado_en`

---

# 6. Estrategia técnica sugerida

## Etapa 1
Crear contratos individuales:
- `v_estado_episodio_canonico`
- `v_plan_atencion_actual`
- `v_riesgo_episodio_actual`

## Etapa 2
Construir agregado de consumo:
- `v_resumen_episodio_operativo`

## Etapa 3
Refinar persistencia o normalización según aprendizaje con casos reales.

---

# 7. Veredicto

Estos contratos son suficientes para empezar Fase I sin sobrediseñar.

Su mérito no está en ser perfectos.
Está en que vuelven explícita una semántica que hoy el sistema ya insinúa, pero aún no ofrece de forma unificada.
