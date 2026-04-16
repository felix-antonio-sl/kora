# Diseño de Teleatención — Sistema Operativo HODOM HSC

Fecha: 2026-04-07
Origen: Ingeniero Fugaz, adoptado íntegro por su profundidad

---

## Principio

La telemática no es un módulo accesorio. Es una forma de acto asistencial con reglas explícitas.

---

## Tipos de interacción remota

1. **Teleorientación administrativa** — coordinación de horarios, insumos, trámites
2. **Teleorientación clínica** — educación, aclaración de indicaciones, adherencia
3. **Telemonitoreo programado** — seguimiento de síntomas, signos vitales reportados, adherencia
4. **Regulación médica** — evaluación clínica a distancia con decisión de conducta
5. **Seguimiento post-visita** — verificación de estado tras intervención presencial
6. **Coordinación con APS o familia** — enlace inter-nivel o con red de apoyo

---

## Reglas de registro

Toda interacción remota debe registrar:
- quién atendió
- quién participó (paciente, cuidador, otro profesional)
- fecha y hora
- motivo
- contexto clínico consultado
- evaluación o decisión
- indicación entregada
- necesidad de escalamiento
- vínculo al episodio

---

## Qué puede resolverse remotamente

- Educación al paciente/cuidador
- Seguimiento de síntomas leves o esperables
- Revisión de adherencia
- Coordinación de visita
- Aclaración de indicaciones
- Entrega de resultados con registro

---

## Qué debe escalar a visita presencial o traslado

- Sospecha de inestabilidad clínica
- Deterioro respiratorio o hemodinámico
- Imposibilidad del cuidador para sostener cuidados
- Problemas de acceso esenciales (servicios básicos, seguridad)
- Falla de dispositivo o insumo crítico
- Rechazo repetido de visitas
- Eventos adversos relevantes

---

## Historias de usuario de teleatención

### HU-TEL-1 Registrar teleorientación clínica
Como **médico regulador o enfermera**, necesito registrar una teleorientación clínica vinculada al episodio, para que quede como parte de la historia clínica.

**CA:**
- Tipo: teléfono / video
- Contenido: motivo, evaluación, indicación, plan
- Diferenciada visualmente de visita presencial
- Registra duración y medio

**FHIR:** Encounter (class=VR), Composition
**Normativa:** DS 1/2022 art. 12-13 (TICs); REM A30/A32
**Prioridad:** P1

### HU-TEL-2 Registrar telemonitoreo programado
Como **enfermera clínica**, necesito registrar un telemonitoreo programado con datos reportados por el cuidador (SV, síntomas, adherencia), para seguimiento sin visita presencial.

**CA:**
- Datos reportados: SV parciales, síntomas, adherencia
- Evaluación: estable / requiere visita / requiere traslado
- Vinculado al episodio y visible en timeline

**FHIR:** Observation (method=reported), Communication
**Normativa:** REM A32
**Prioridad:** P1

### HU-TEL-3 Escalar desde teleatención a visita o traslado
Como **médico regulador**, necesito escalar una interacción remota a visita presencial urgente o a traslado hospitalario, dejando trazabilidad de la decisión.

**CA:**
- Registra: motivo de escalamiento, evaluación remota, decisión
- Genera: solicitud de visita urgente o solicitud de traslado
- Queda vinculado al episodio

**FHIR:** ServiceRequest (intent=urgent-order)
**Normativa:** DS 1/2022 art. 7 (DT: coordinar reingreso)
**Prioridad:** P1

### HU-TEL-4 Registrar regulación médica fuera de horario
Como **médico regulador**, necesito registrar una regulación médica realizada fuera del horario de visitas (19:00-08:00 o fines de semana), para trazabilidad de cobertura continua.

**CA:**
- Mismo formato que teleatención pero con flag "fuera de horario"
- Registra si se activó SAMU/SAPU/UEH
- Vinculado al episodio

**FHIR:** Encounter (class=VR), Flag
**Normativa:** CI 2026 (PE-14: protocolo emergencia fuera de horario)
**Prioridad:** P2
