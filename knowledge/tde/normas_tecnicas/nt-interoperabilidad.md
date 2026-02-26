---
_manifest:
  urn: "urn:tde:kb:nt-interoperabilidad"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto12"
version: 1.0.0
status: published
tags: [decreto, norma-tecnica, interoperabilidad, nodo, gestor-codigos, red-interoperabilidad, tde, ley-21180]
lang: es
---

# DS 12 — Norma Tecnica de Interoperabilidad

- **Promulgacion**: 19-MAY-2023
- **Publicacion**: 17-AGO-2023
- **Base legal**: Ley 21.180 (TDE) + DS 4/2020 (Reglamento) + DFL 1/2020 (Gradualidad)
- **Revision**: cada 2 anios desde vigencia

## Objeto (art. 1)

Definir estandares, protocolos y herramientas para que organos AE interoperen datos, documentos y expedientes electronicos.

## Definiciones (art. 2)

| Termino | Definicion |
|---------|-----------|
| Codigo | Secuencia simbolos que identifica univocamente objeto/entidad/estado |
| Consumidor | Organo AE que demanda servicio interoperabilidad |
| Dato | Representacion atributo/variable; capturado via observacion/medicion |
| Dato abierto | Dato digital con caracteristicas tecnicas/juridicas para uso/reutilizacion/redistribucion libre |
| Dato digital | Dato en variables discretas (bits); tratable por dispositivos |
| Endpoints | Direccion URI servicio web para recibir/enviar informacion |
| Interoperar | Operacion entre 2 organos AE conectados via nodo: intercambiar/transmitir datos/docs/expedientes |
| Metadatos | Datos que describen contexto, contenido, estructura de un dato |
| Protocolo comunicacion | Reglas/estandares transmision datos en red interoperabilidad |
| Proveedor | Organo AE al que se demanda servicio interoperabilidad |
| Servicios interoperabilidad | Servicios automatizados con estandares/protocolos para interoperar via nodo validado |
| Transaccion | Instancia completa comunicacion: consulta consumidor → recepcion proveedor → respuesta → recepcion consumidor |
| Token | Secuencia caracteres vinculada a informacion protegida; credencial autenticacion/ID sesion/transaccion |
| URI | Medio para identificar recurso en internet |

## Red de Interoperabilidad (arts. 3-5)

### Descripcion (art. 3)
- Conjunto conexiones directas/seguras via internet
- Nodos alojados en infraestructura organos AE
- Organos actuan como proveedores y/o consumidores
- Trazabilidad, registro, autorizaciones → almacenamiento centralizado via servicios centralizados

### Componentes (art. 4)
1. Nodos de interoperabilidad
2. Servicios centralizados de interoperabilidad
3. Herramientas complementarias: Gestor Codigos Estado + Catalogo Elementos Transmisibles
4. Elementos transmisibles

Componentes 1-3: dispuestos por DGD SEGPRES.

### Integracion (art. 5)
Organos se integran como proveedores y/o consumidores via nodos conectados a servicios centralizados.

## Nodo de Interoperabilidad (art. 6)

Software alojado en infraestructura organo AE; integra sistemas/plataformas a red.

DGD pone nodo a disposicion; organo puede desarrollar propio.

**10 requisitos minimos**:
1. Conexion segura entre organos (guia tecnica + NT Seguridad)
2. Enviar/recibir datos, docs, expedientes electronicos
3. Recepcion/envio mensajes entre organos
4. Conexion directa a otro nodo + servicios centralizados (trazabilidad)
5. Conexion gestor autorizaciones
6. Unica via acceso a servicios interoperabilidad
7. Encriptar mensajes/respuestas (metodos en guia tecnica)
8. Validar certificado autenticacion nodo consumidor
9. Auto-monitoreo operaciones
10. Protocolos autorizados por DGD

Organo puede tener 1+ nodos segun arquitectura. Comunicacion nodo-sistemas internos → responsabilidad organo.

## Servicios Centralizados (arts. 7-15)

### Descripcion general (art. 7)
Software + infraestructura que habilita: Catalogo Servicios, Registro Trazabilidad, Directorio Datos, Catalogo Esquemas, Gestor Acuerdos, Gestor Autorizaciones. Desarrollados por DGD. Cada organo designa funcionarios responsables actualizacion/mantencion.

### Catalogo Servicios Interoperabilidad (art. 8)
- Lista datos/docs/expedientes disponibles por proveedores
- Publicar TODOS servicios bajo administracion organo
- Cada servicio: codigo univoco (Gestor Codigos) + codigos procedimientos (CPAT)
- Publicar por cada servicio:
  1. Datos entrada/salida
  2. Forma entrega (requiere esquema?)
  3. Funcionario responsable
  4. TPS (transacciones/segundo)
  5. ANS (% acuerdo nivel servicio)
- Primera carga: DGD; posterior: responsabilidad cada organo
- Funcionario designado para publicacion/actualizacion

### Registro Trazabilidad (art. 9)
Almacena info cada transaccion. Nodos registran:
1. Plataforma/servicio web solicitud/recepcion
2. Organo requirente, funcionario, organo destinatario, procedimiento, gestion, plazo
3. Marca tiempo UTC+00:00 (sincronizacion SHOA)
4. Datos sensibles: RUN interesado + autorizacion + funcionario responsable (art. 24 bis Ley 19.880)
5. Tipo respuesta (error/exito)
6. Nombre/codigo organo proveedor
7. Nombre/codigo organo consumidor

Envio trazabilidad: paralelo e inmediato. Interrupcion/alta carga/fuerza mayor: envio diferido via paquetes dentro 48h desde primera transaccion.

### Directorio de Datos (art. 10)
- Exhibe datos disponibles en Catalogo Servicios
- Contiene: nombre, descripcion, clasificacion (art. 20), funcionario responsable
- Todos datos expuestos via servicio publicado → deben estar en Directorio
- Organos hacen catastro datos segun competencias
- Dato necesario publicado → solicitarlo via Catalogo Servicios
- Dato sensible → requiere autorizacion interesado via Gestor Autorizaciones

### Catalogo de Esquemas (art. 11)
- **Esquema basal**: define dato atomico / pequeno conjunto datos relacionados semanticamente
- **Esquema documental**: define conjunto datos componen documento; compuesto de esquemas basales
- Catalogo gestiona listado esquemas aprobados
- Primera carga: DGD; posterior: responsabilidad organos
- Publicar: descripcion esquema documental + basales relacionados
- Cambio funcionario responsable: actualizar en max 3 dias
- Esquema no publicado → sugerir incorporacion (visado DGD); error sintactico/incompatibilidad → rechazo + notificacion

### Gestor de Acuerdos (art. 12)
- Facilita solicitud servicio interoperabilidad consumidor-proveedor
- Habilita conexion + define niveles servicio via TyC/convenios
- Aplica a datos/servicios en Directorio/Catalogo (NO datos abiertos)
- Consumidor → redirigido a Gestor Acuerdos para materializar requerimiento
- Acuerdos: uso unico o acceso permanente; indicar volumen/modalidad transacciones
- Solo celebrar acuerdos via Gestor Acuerdos

### Tramitacion acuerdos (art. 13)
- Solicita: Jefe Unidad TI consumidor (con visto bueno juridico)
- Envio via Gestor Acuerdos → copia automatica a DGD
- Plazo respuesta proveedor: **15 dias habiles** (extensible +5)
- Acepta: Jefe Unidad TI proveedor (con visto bueno juridico)
- Negativa: siempre justificada
- Negativa → DGD media; puede solicitar aceptacion
- Falta capacidad manifiesta: DGD evalua (funcionarios, infraestructura, presupuesto, otras circunstancias) y puede prestar apoyo tecnico
- Negativa injustificada/fuera plazo → DGD decide por si
- Aprobada → firma electronica avanzada Jefes Superiores Servicio

### Gestor de Autorizaciones (art. 14)
- Personas naturales interesadas autorizan interoperabilidad datos personales sensibles (arts. 16 bis, 17d, 24 bis, 30f Ley 19.880)
- Integrado a ClaveUnica
- Funciones interesado:
  1. Acceso historial autorizaciones/revocaciones (verificable: quien, cuando, como, para que, que datos)
  2. Revocar autorizaciones
  3. No otorgar consentimiento
- Autorizacion se extiende a todo el procedimiento hasta total tramitacion
- Incorporar autorizacion como documento al expediente

### Requisitos consentimiento (art. 15)
1. Prestado por interesado / apoderado / representante legal
2. Por escrito
3. Acto afirmativo claro (via Gestor Autorizaciones; excepcion soporte papel)
4. Libre: no obligado; posibilidad negarse sin perder derecho; procedimiento NO termina por negar
5. Especifico, informado, inequivoco: lenguaje simple/claro, proposito, alcance procedimiento
6. Esencialmente revocable: posibilidad revocar; procedimiento NO termina por revocar

Negativa/revocacion → interesado aporta documentos/informacion por si. Revocacion sin efecto retroactivo.

## Herramientas Complementarias (arts. 16-18)

### Gestor de Codigos del Estado (art. 17)
Software gestiona codigos estandarizados: organos AE, procedimientos administrativos, nombres territoriales.
Funciones:
1. Visualizar codigos disponibles
2. Gestionar codigos internos + metadatos
3. Acceder equivalencias codigos otros organos
4. Incorporar categorias adicionales + metadatos + relaciones

### Catalogo Procedimientos Administrativos y Tramites (art. 18)
Nomina con codificacion, estandarizacion, caracterizacion. Cada organo especifica:
1. Nombre + ley origen + codigo univoco
2. Requiere interoperar datos/docs/expedientes?
3. Vinculo con Directorio Datos y Catalogo Servicios
4. Necesidad Gestor Autorizaciones (datos sensibles)
5. Mecanismo contacto para interesado

## Elementos Transmisibles (arts. 19-20)

### Que se transmite (art. 19)
- Proveedores transmiten datos/docs competencia necesarios para procedimiento del consumidor
- Documentos: acorde esquema documental (art. 11)
- Datos personales interesados + otros relevantes
- Documentos/expedientes necesarios
- Datos abiertos: consumo directo, fuera concepto interoperabilidad NT
- Documentos publicos: publicados en portales (Ley 20.285)

### Clasificacion datos (art. 20)
Cada organo clasifica en Directorio: personales, sensibles, estadisticos, secretos, reservados, otros (Ley 19.628 + normativa aplicable).

## Coordinacion Interoperabilidad (arts. 21-26)

### 3 niveles (art. 22)

| Nivel | Nombre | Coordinacion | Funcion |
|-------|--------|-------------|---------|
| 1o | Institucional | DGD + representantes organos | Resolver problemas operativos interoperabilidad |
| 2o | Sectorial | Comites por sector economico/social + apoyo DGD | Coordinar estandares/codificaciones/esquemas sectoriales |
| 3o | Estrategico | Composicion por acto SEGPRES, presidido Jefe DGD | Validar/aprobar estandares, protocolos, resolver discrepancias, sugerir datos/esquemas/metadatos basales transversales |

### Rol DGD (art. 26)
- Apoyo coordinacion estrategica: documentos, guias, propuestas estandares/esquemas/codigos
- Asesoria implementacion red
- Convocatoria instancias transversales/sectoriales

## Disposiciones finales

- **Guia tecnica** (art. 27): DGD dicta guias aspectos operativos
- **Gradualidad** (art. 28): segun DFL 1/2020 SEGPRES
- **Revision** (art. 29): cada 2 anios minimo

## Disposiciones transitorias

| Transitorio | Contenido |
|-------------|-----------|
| 1o | 1 anio desde vigencia para construir catastro inicial datos (art. 10) e incorporar al Directorio |
| 2o | **31-DIC-2026**: ultimo dia funcionamiento PISEE; red interoperabilidad = unica via |
| 3o | Migracion PISEE → red interoperabilidad: 2025 (grupos A+B), 2026 (grupo C); pueden iniciar antes Fase 6 |
| 4o | 1 anio desde vigencia para revisar/modificar/ajustar esquemas PISEE → Catalogo Servicios |
| 5o | Convenios interoperabilidad vigentes: sin efecto en lo incompatible con esta NT (art. 4 transitorio Reglamento) |
