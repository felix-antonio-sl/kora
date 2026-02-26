---
_manifest:
  urn: "urn:tde:kb:nt-seguridad-ciberseguridad"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto7"
version: 1.0.0
status: published
tags: [decreto, norma-tecnica, seguridad-informacion, ciberseguridad, tde, ley-21180]
lang: es
---

# DS 7 — Norma Tecnica de Seguridad de la Informacion y Ciberseguridad

- **Promulgacion**: 19-MAY-2023
- **Publicacion**: 17-AGO-2023
- **Base legal**: Ley 21.180 (TDE) + DS 4/2020 (Reglamento) + DFL 1/2020 (Gradualidad)
- **Deroga**: DS 83/2004 SEGPRES (norma anterior seguridad docs electronicos)
- **Revision**: cada 2 anios desde vigencia

## Objeto (art. 1)

Estándares y directrices sobre seguridad de la informacion y ciberseguridad para organos de la Administracion del Estado → resguardar confidencialidad, integridad, disponibilidad de informacion e infraestructura de plataformas electronicas que sustentan procedimientos administrativos.

## Definiciones clave (art. 2)

| Termino | Definicion |
|---------|-----------|
| Activo | Elemento logico/fisico, hardware, sistema relacionado con informacion |
| Activo de informacion | Datos esenciales para funcionamiento del organo; proteger C-I-D |
| Ciberseguridad y SI | Acciones, politicas, medidas preventivas/reactivas ante amenazas/riesgos; proteger/preservar/restablecer C-I-D |
| Confidencialidad | Acceso exclusivo por autorizados |
| Control de seguridad | Estandares/buenas practicas para administrar riesgos TI |
| Disponibilidad | Accesibilidad y utilizacion a requerimiento de entidad autorizada |
| Gestion de riesgo | Proceso estructurado: identificar, evaluar, controlar, tratar riesgos |
| Incidente de seguridad | Evento indeseado/inesperado que compromete D-A-I-C de sistemas/activos/datos |
| Integridad | Exactitud, autenticidad, completitud |
| Plataforma electronica | Software + datos + infraestructura que sustenta procesos/procedimientos |
| Riesgo | Efecto de incertidumbre sobre activos; consecuencias x probabilidad |
| Servidor | Equipo virtual/fisico dedicado a servicios de red, BD, web, sistemas |
| Sistema informatico | Componentes logicos/fisicos interactuando para funcion disenada |
| Usuarios | Personas naturales/apoderados, representantes PJ, funcionarios que acceden a plataformas |

## Marco de trabajo (art. 3-4)

1. Diagnostico inicial del estado de ciberseguridad de plataformas (art. 4)
2. Incluir diagnostico en Catalogo de Plataformas de NT Calidad y Funcionamiento
3. Estructurar trabajo segun funciones y categorias (Titulo III)
4. Generar e implementar Politica de SI y Ciberseguridad

## Politica de SI y Ciberseguridad (art. 5)

Cada organo DEBE elaborar Politica aprobada por acto administrativo del Jefe Superior de Servicio.

**Contenido minimo**:
1. Objetivos generales y especificos
2. Alcance: activos/activos de informacion a proteger + roles involucrados
3. Legislacion y normativa aplicable
4. Roles obligatorios:
   - **Responsable institucional de SI y ciberseguridad**: velar seguridad, cumplimiento/actualizacion Politica, gestionar administracion SI
   - **Responsable de activos de informacion**: identificacion, clasificacion, gestion riesgo y niveles seguridad

**Restricciones**:
- Funciones NO externalizables bajo ninguna forma
- Organo decide si unifica ambos roles en una persona
- Encargado ciberseguridad nombrado por Instructivo Presidencial 8/2018 → requisito cumplido salvo nueva designacion

## 5 Funciones de seguridad (arts. 7-11)

| Funcion | Art. | Categorias |
|---------|------|-----------|
| **Identificacion** | 7 | Contexto/entorno, gobernanza, gestion activos informacion, gestion riesgos, contratacion/proveedores nube |
| **Proteccion** | 8 | Gestion servidores/redes, autenticacion/control acceso, concienciacion/formacion, seguridad datos, procesos proteccion informacion, registro eventos |
| **Deteccion** | 9 | Analisis eventos/anomalias, monitoreo continuo (proteccion codigo malicioso), proceso deteccion |
| **Respuesta** | 10 | Planificacion respuesta incidentes, comunicacion acciones, analisis incidentes, mitigacion, mejoras |
| **Recuperacion** | 11 | Planificacion recuperacion, mejoras planificacion/procesos, comunicacion estado recuperacion |

Detalle operativo de cada funcion → guias tecnicas (art. 12).

## Disposiciones finales

- **Guia tecnica** (art. 12): Division de Gobierno Digital dicta guias con aspectos operativos
- **Gradualidad** (art. 13): segun DFL 1/2020 SEGPRES; DGD define lineamientos/formato implementacion
- **Revision** (art. 14): cada 2 anios minimo; considerar aprendizajes, dificultades, buenas practicas
