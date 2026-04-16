# Modelo OPM — HODOM HSC
# Núcleo Canónico Local

Versión: 1.0
Fecha: 2026-04-09
Estado: consolidación canónica local inicial

Este documento consolida el trabajo previo en un primer núcleo canónico local para modelar la Hospitalización Domiciliaria del Hospital de San Carlos.

No reemplaza la normativa ni el modelo normativo general. Su función es distinta:
- tomar la semántica normativa como restricción,
- incorporar la arquitectura operativa real insinuada por HSC,
- y ofrecer una base de diseño y gobierno suficientemente estable para iteraciones posteriores.

---

## 1. Tesis central

La HODOM HSC debe modelarse como:

**un sistema socio-técnico episódico, territorial, regulado, remotamente sensible y autoobservable.**

Cada una de esas palabras importa:

- **socio-técnico**: integra personas, protocolos, infraestructura, registros, software y red.
- **episódico**: la unidad operativa central es el episodio de hospitalización domiciliaria.
- **territorial**: el cuidado solo existe si puede territorializarse en rutas, tiempos y móviles.
- **regulado**: la atención remota y la continuidad con la red no son accidentales, son parte constitutiva del sistema.
- **autoobservable**: la unidad no solo atiende; también se vuelve legible a sí misma vía censo, cupos, trazabilidad y REM.

---

## 2. Fuentes de verdad utilizadas

### 2.1 Restricción normativa
- DS 1/2022
- Decreto Exento 31/2024
- Norma Técnica HODOM 2024

### 2.2 Evidencia de sistema HSC
- `hdos-app/README.md`
- `hdos-app/docs/specs/00-INDICE.md`
- `hdos-app/docs/specs/01-diseno-sistema-operativo-hodom-hsc.md`
- `hdos-app/docs/specs/13-portal-paciente-mvp.md`
- `hdos/README.md`

### 2.3 Modelos previos absorbidos
- `opm-hodom-normativo-v1.0.md`
- `opm-hodom-model-v2.5.md`
- `opm-hodom-hsc-procesos-v0.1.md`
- `opm-hodom-hsc-procesos-v0.2.md`
- `opm-hodom-hsc-procesos-v0.3.md`
- `opm-hodom-hsc-procesos-v0.4.md`
- `opm-hodom-hsc-gobernanza-v0.5.md`

---

## 3. SD canónico local

### 3.1 Sistema

**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos**

### 3.2 Proceso principal

*Hospitalizar en Domicilio*

### 3.3 Beneficiario

**Grupo de Pacientes**

### 3.4 Atributo de valor

**Condición Clínica**: `agudo-reagudizado` → `recuperado`

### 3.5 Doble exhibition propuesta

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Hospitalizar en Domicilio* así como *Gobernar Sistema HODOM HSC*.
```

Consecuencia:
- el modelo local reconoce desde el nivel superior que la unidad tiene una función asistencial y una función de autogobierno operativo.

---

## 4. SD1 canónico local — sistema asistencial-operativo

### 4.1 Backbone consolidado

```opl
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.
```

### 4.2 Macrolectura del backbone

1. **Evaluar Elegibilidad**
   - decide si el caso puede entrar.
2. **Admitir Episodio**
   - convierte el caso en episodio trazable.
3. **Planificar Atención Interdisciplinaria**
   - convierte admisión en programa clínico.
4. **Programar Visitas y Rutas**
   - convierte programa clínico en territorialidad ejecutable.
5. **Ejecutar Atención Domiciliaria**
   - produce la intervención presencial.
6. **Regular Atención a Distancia**
   - absorbe incertidumbre y continuidad no presencial.
7. **Monitorear Evolución Clínica**
   - produce juicio clínico recurrente.
8. **Gestionar Comunicación Clínica**
   - mantiene acoplamiento con paciente, cuidador y red.
9. **Egresar Episodio**
   - cierra el episodio por causal.
10. **Realizar Seguimiento Post-Egreso**
   - vigila continuidad y desenlace inmediato.
11. **Tributar Producción y REM**
   - transforma actividad asistencial en visibilidad operativa.

---

## 5. SD3 canónico local — sistema de gobierno

### 5.1 Backbone consolidado

```opl
*Gobernar Sistema HODOM HSC* se descompone en *Gestionar Autorización y Cumplimiento*, *Gobernar Protocolos y Procedimientos*, *Gestionar Capacidad y Continuidad Operativa*, *Auditar Calidad y Seguridad*, *Validar Observabilidad y REM* y *Gestionar Desarrollo de Competencias*, en paralelo.
```

### 5.2 Macrolectura del backbone

1. **Gestionar Autorización y Cumplimiento**
2. **Gobernar Protocolos y Procedimientos**
3. **Gestionar Capacidad y Continuidad Operativa**
4. **Auditar Calidad y Seguridad**
5. **Validar Observabilidad y REM**
6. **Gestionar Desarrollo de Competencias**

---

## 6. Objetos canónicos locales

### 6.1 Núcleo clínico-episódico
- **Episodio de Hospitalización Domiciliaria**
- **Condición Clínica**
- **Estado de Hospitalización**
- **Ficha Clínica**
- **Plan de Atención**
- **Resumen Clínico Domiciliario**
- **Decisión de Continuidad**
- **Epicrisis**

### 6.2 Núcleo territorial-operativo
- **Visita Domiciliaria**
- **Agenda Clínica**
- **Ruta Diaria**
- **Vehículo de Transporte**
- **Capacidad Operativa**
- **Cupo Consolidado**

### 6.3 Núcleo de regulación y comunicación
- **Llamado Clínico**
- **Motivo de Consulta**
- **Indicación Remota**
- **Decisión de Escalamiento**
- **Registro de Regulación**
- **Documento de Emergencia**

### 6.4 Núcleo de observabilidad y gobierno
- **REM A21**
- **Estado de Observabilidad**
- **Conjunto de Protocolos**
- **Estado de Calidad y Seguridad**
- **Cumplimiento de Competencias**
- **Estado de Autorización Sanitaria**

---

## 7. Decisiones canónicas de frontera

### 7.1 Unidad canónica
La unidad del dominio es el **episodio**, no el paciente aislado.

### 7.2 Territorialidad
La agenda y la ruta no son soporte administrativo; son parte constitutiva del cuidado.

### 7.3 Remoticidad
Las llamadas y TIC no son canal accesorio; son modalidad clínica regulatoria.

### 7.4 Doble cierre del episodio
Todo episodio tiene dos cierres distintos:
- cierre clínico-operacional
- cierre estadístico

### 7.5 Doble sistema en un mismo sistema
El sistema HODOM HSC exhibe dos macrofunciones:
- atender
- gobernarse para poder seguir atendiendo bien

---

## 8. OPL-ES mínimo canónico local

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Hospitalizar en Domicilio* así como *Gobernar Sistema HODOM HSC*.
**Grupo de Pacientes** exhibe **Condición Clínica**.
*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.
*Gobernar Sistema HODOM HSC* se descompone en *Gestionar Autorización y Cumplimiento*, *Gobernar Protocolos y Procedimientos*, *Gestionar Capacidad y Continuidad Operativa*, *Auditar Calidad y Seguridad*, *Validar Observabilidad y REM* y *Gestionar Desarrollo de Competencias*, en paralelo.
```

---

## 9. Tabla de hipótesis pendientes

| Hipótesis | Motivo | Prioridad |
|-----------|--------|-----------|
| El episodio existe como entidad suficientemente explícita en BD y UI | hoy está muy sugerido, falta cierre semántico total | alta |
| La categorización de riesgo tiene regla local estable | importante para monitoreo y cupos | alta |
| El flujo de llamadas distingue administrativo vs clínico vs urgente | clave para regulación | alta |
| El REM puede modelarse como subproceso asistencial derivado o debe migrar completo a SD3 | afecta frontera canónica | media |
| Comunicación clínica merece macroproceso propio estable | puede redistribuirse | media |
| Documento de emergencia y portal deben convertirse en submodelo propio | ya asoman como capa relevante | media |

---

## 10. Qué ya puede usarse operativamente

Este núcleo ya sirve para:
- pensar arquitectura funcional del sistema,
- discutir roles entre Dirección Técnica y Coordinación,
- orientar rediseño de procesos,
- decidir qué módulos del software corresponden a qué procesos reales,
- distinguir mejor entre clínica, coordinación y gobierno,
- evitar diseñar una app que sea solo ficha o solo agenda.

---

## 11. Veredicto

Este `v1.0` no es el final del modelado.
Pero sí es el primer punto donde el modelo HODOM HSC deja de ser exploración y empieza a comportarse como canon local de trabajo.

A partir de aquí, lo correcto ya no es seguir expandiendo sin fin.
Lo correcto es:
- validar,
- depurar,
- alinear con BD/pantallas/formularios,
- y endurecer lo que hoy todavía es hipótesis.
