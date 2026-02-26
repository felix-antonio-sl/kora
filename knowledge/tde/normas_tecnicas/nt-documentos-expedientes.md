---
_manifest:
  urn: "urn:tde:kb:nt-documentos-expedientes"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto10"
version: 1.0.0
status: published
tags: [decreto, norma-tecnica, documentos-electronicos, expediente-electronico, gestion-documental, comunicacion-oficial, tde, ley-21180]
lang: es
---

# DS 10 — Norma Tecnica de Documentos y Expedientes Electronicos

- **Promulgacion**: 19-MAY-2023
- **Publicacion**: 17-AGO-2023
- **Base legal**: Ley 21.180 (TDE) + DS 4/2020 (Reglamento) + DFL 1/2020 (Gradualidad) + Ley 19.799 (firma electronica) + DFL 1/2020 Min. Culturas (microformas)
- **Revision**: cada 2 anios desde vigencia

## Objeto (art. 1)

Definir estandares, formatos, metadatos, registros trazabilidad, fases y procesos para administrar/gestionar documentos y expedientes electronicos en procedimientos administrativos.

## Definiciones clave (art. 2)

| Termino | Definicion |
|---------|-----------|
| Comunicacion oficial | Mensaje entre organos AE, suscrito por Jefe Superior/delegado, medio electronico formal con integridad/registro |
| Conservacion documental digital | Medidas/estandares/acciones para mantener acceso a documentos en el tiempo; incluye migracion soportes/formatos |
| Copia autorizada | Generada por plataforma gestion expedientes con medio verificacion autenticidad |
| Documento | Informacion creada/recibida/conservada como evidencia/activo |
| Documento electronico | Representacion hecho/imagen/idea creada/enviada/recibida por medios electronicos, almacenada para uso posterior |
| Expediente administrativo | Registro integro actuaciones procedimiento (docs presentados, actuaciones, resoluciones, notificaciones) en orden |
| Expediente electronico | Unidad documental con ID unico: indices + docs electronicos + metadatos + registros; generada en plataforma |
| Expediente hibrido | Expediente electronico que registra actuaciones en soporte electronico y papel (art. 14 Reglamento) |
| Gestion documental | Procesos administracion ciclo vida documentos (creacion/captura → disposicion final) |
| IUIe | Identificador Unico Institucional de Expedientes; numero unico asignado automaticamente |
| Plataforma gestion documental | Sistema que dirige/controla procesos incorporacion, gestion, acceso documentos en el tiempo |

## Politica de Gestion Documental (arts. 3-4)

Cada organo DEBE definir Politica de Gestion Documental. Contenido minimo:
1. Objetivo institucional gestion documental
2. Roles responsables del proceso
3. Identificacion procedimientos administrativos (segun NT Interoperabilidad)
4. Metas/lineamientos preservacion y resguardo
5. Criterios para procesos gestion documental
6. Gobernanza interna implementacion

**Revision**: periodo minimo 1 anio, maximo 3 anios.

## Elementos requeridos (art. 5)

Cada organo debe contar con:
1. Plataforma de gestion de expedientes
2. Uno o mas repositorios documentales
3. Procesos creacion documentos electronicos estandarizados/interoperables

## Plataforma de Gestion de Expedientes (art. 6)

Debe sustentar formalizacion expediente durante todas etapas procedimiento y fases ciclo vital:
1. Recepcion documentos electronicos
2. Creacion expediente electronico
3. Procesamiento expediente
4. Transicion expediente
5. Disposicion final expediente

## Repositorio Documental (art. 7)

- Minimo 1 por organo
- Almacenar/custodiar documentos y expedientes
- Asegurar trazabilidad, relaciones, metadatos
- Preservacion largo plazo: cumplir especificaciones Archivo Nacional

## Requisitos transversales

### Codificacion (art. 8)
Usar codigos estandarizados Gestor de Codigos del Estado (NT Interoperabilidad): organos, procedimientos, cobertura geografica.

### Fecha y hora (art. 9)
- UTC+00:00 + ubicacion geografica organo
- Sincronizacion permanente con SHOA

### Interconexion (art. 10)
Toda plataforma que se interconecte/integre/interopere con gestion expedientes debe cumplir NTs art. 57 Reglamento.

### Trazabilidad (art. 11)
Registros minimos:
1. Creacion, incorporacion, modificacion, transferencia, eliminacion
2. Acceso al expediente
3. Autorizacion poderes (cuando corresponda)

## Documentos Electronicos (arts. 12-17)

### Estructura estandarizada (art. 12)
Componentes: datos + formato archivo + metadatos estandarizados.

### Formatos validos (art. 13)
- Segun guias tecnicas
- Formato no disponible → sugerir incorporacion a guia (visado DGD, consulta Archivo Nacional)
- Mientras no se incorpore: incluir al expediente con razon expresa + crear copia en formato aprobado

### Metadatos (art. 14)
Todo documento electronico → estructura metadatos estandarizados (campos obligatorios, condicionales, sugeridos en guias).

### Acceso (art. 15)
- Interesados: via NT Autenticacion
- Otros organos: via NT Interoperabilidad

### Verificacion (art. 16)
Habilitar consulta trazabilidad para verificar identificacion docs + constatar modificaciones.

### Preservacion (art. 17)
- Conservar en entorno C-I-D (NT Seguridad)
- Custodiar en repositorios (art. 7)
- Disponible por tiempo definido en Politica Gestion Documental
- Posterior: eliminar o transferir a Archivo Nacional

## Expedientes Electronicos (arts. 18-34)

### Creacion (art. 18)
Al iniciar procedimiento (oficio o peticion parte) → crear expediente en plataforma + asignar IUIe + metadatos obligatorios.

### Esquema estructural (art. 19)
1. Documentos electronicos estandarizados
2. Indice electronico expediente
3. Metadatos estandarizados expediente
4. Registro trazabilidad
5. Registro accesos (autenticaciones + autorizaciones terceros)
6. Registro actos administrativos (propios + interoperados)
7. Registro demas acciones gestion documental/expedientes

### Principio fidelidad (art. 20)
Registrar integramente y en orden sucesivo todas actuaciones procedimiento.

### Incorporacion documentos (art. 21)

**Peticion de parte**:
- a) Formularios/solicitudes via plataformas web → conformar documento electronico visualizable + metadatos
- b) Documentos electronicos via plataforma organo → conformar metadatos + incorporar
- c) Documento fisico → microforma (DFL 1/2020 Min. Culturas)

**De oficio**: crear expediente + incorporar acto inicio como documento electronico estandarizado.

### Vinculacion metadatos (art. 22)
Todo contenido vinculado univocamente a indice + metadatos.

### Trazabilidad incorporacion (art. 23)
Mecanismos:
1. Directamente como documento electronico estandarizado
2. Enlace persistente a repositorio externo
3. Enlace a otro expediente (anidamiento; obligatorio en acumulacion procedimientos art. 33 Ley 19.880)

### Interoperabilidad (art. 24)
Datos interoperados → incorporar via documento electronico estandarizado. Debe registrar:
- a) Identificacion como elemento interoperado
- b) Codigo organo origen (Gestor Codigos)
- c) Servicio interoperabilidad utilizado
- d) Autorizacion interesado (datos sensibles)

### Documentacion fisica / microformas (art. 25)
Copia digitalizada calidad copia fiel → formato microforma (DFL 1/2020 Min. Culturas, DS 23/2020).

### Expedientes hibridos (art. 26)
Excepcion art. 14 Reglamento: cuando no sea posible digitalizar → documento electronico que describa/referencie documentacion fisica.

### Comunicaciones oficiales (art. 27)
Incorporar todas al expediente via Plataforma Comunicaciones Oficiales (DGD).

### Notificaciones (art. 28)
Incorporar todas las notificaciones al expediente.

### Accesibilidad expedientes (art. 29)
- Interesados: NT Autenticacion
- Otros organos: NT Interoperabilidad

### Certificado presentacion (art. 30)
Plataforma emite automaticamente certificado con firma electronica:
1. Fecha/hora presentacion
2. Origen incorporacion
3. Numero expediente
4. Organo tramitante
5. Identificacion quien presenta
6. Funcionario/plataforma recepciona

Excepciones (art. 19 bis Ley 19.880): tambien emitir en fisico si interesado lo solicita.

### Verificacion expedientes (art. 31)
Habilitar consulta trazabilidad para verificar/constatar contenido y gestiones.

### Preservacion (art. 32)
- Conservar C-I-D (NT Seguridad) + repositorios (art. 7)
- Disponible segun normativa transferencia documental
- Posterior: eliminar o transferir Archivo Nacional

### Enlaces persistentes (art. 33)
Organos pueden usar enlaces externos referenciar docs/expedientes en plataformas otros organos o repositorios propios.

### Registro actuaciones (art. 34)
Validar identidad usuarios para toda gestion/actuacion; identificar ingresos automatizados.

## Condiciones funcionamiento (arts. 35-37)

### Estandares minimos (art. 35)
1. Control poderes apoderados/representantes
2. Control roles acceso plataformas + documentos sensibles
3. Generar copias autorizadas
4. Condiciones basicas gestion expedientes/repositorios
5. Caracteristicas internas repositorios + aseguramiento servicios

### Roles acceso (art. 36)
Asegurar acceso interesados + organos interoperantes (NTs Autenticacion, Interoperabilidad, Seguridad).
Expedientes disponibles en dependencias para consulta via medios electronicos.

### Datos sensibles/personales (art. 37)
- Registro todos accesos a documentos con datos sensibles: usuario, fecha/hora, documentos
- Ciclo Mejora Continua: perfiles acceso para impedir acceso cruzado datos sensibles entre partes

## Disposiciones finales

- **Guias tecnicas** (art. 38): DGD dicta guias aspectos operativos/procedimientos
- **Gradualidad** (art. 39): segun DFL 1/2020 SEGPRES
- **Revision** (art. 40): cada 2 anios minimo
