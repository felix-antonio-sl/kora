---
_manifest:
  urn: "urn:tde:kb:nt-notificaciones"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto8"
version: 1.0.0
status: published
tags: [decreto, norma-tecnica, notificaciones, casilla-unica, domicilio-digital-unico, tde, ley-21180]
lang: es
---

# DS 8 — Norma Tecnica de Notificaciones

- **Promulgacion**: 19-MAY-2023
- **Publicacion**: 17-AGO-2023
- **Base legal**: Ley 21.180 (TDE) + DS 4/2020 (Reglamento) + DFL 1/2020 (Gradualidad)
- **Revision**: cada 2 anios desde vigencia

## Objeto (art. 1)

Detallar funcionamiento de Plataforma de Notificaciones y forma en que organos de la Administracion del Estado practican notificaciones electronicas en procedimientos administrativos, usando Registro de Domicilios Digitales Unicos (DDU) del Servicio de Registro Civil e Identificacion (art. 46 Ley 19.880).

## Definiciones (art. 2)

| Termino | Definicion |
|---------|-----------|
| DDU (Domicilio Digital Unico) | Medio electronico para recibir notificaciones: Casilla Unica o correo electronico |
| Plataforma de Notificaciones | Plataforma para practicar notificaciones electronicas de organos AE |
| Reglamento | DS 4/2020 SEGPRES |
| Servicios Web | Servicios automatizados con estandares/protocolos para interoperabilidad datos |
| Usuarios | Personas naturales/apoderados, representantes PJ, funcionarios |

## Registro de DDU (art. 3)

Dependiente del Registro Civil (art. 46 Ley 19.880, art. 20 Reglamento). Contiene:
1. Tipo persona (natural/juridica) + RUN/RUT
2. DDU vigente configurado via modulo administracion
3. Historial cambios DDU (fecha + cambio)
4. Excepciones a notificacion electronica (arts. 28+ Reglamento)

## Componentes Plataforma de Notificaciones (art. 4)

| # | Componente | Funcion |
|---|-----------|---------|
| 1 | **Casilla Unica** | Acceso centralizado a notificaciones; bandeja de mensajes |
| 2 | **Modulo institucional** | Envio notificaciones, consulta estado, registro excepciones |
| 3 | **Componente envio mensajes** | Envio al DDU de cada persona |
| 4 | **API de notificaciones** | Integracion automatica plataformas organos → envio notificaciones |
| 5 | **Modulo administracion DDU** | Configurar/modificar DDU; dispuesto por Registro Civil |

Administracion: Division de Gobierno Digital (excepto modulo DDU → Registro Civil).

## Configuracion y funcionamiento DDU (arts. 5-10)

### Configuracion (art. 5)
- DDU = Casilla Unica (default) o correo electronico
- Acceso via portal web con mecanismo oficial autenticacion (NT Autenticacion)
- Activar Casilla Unica → luego acceder notificaciones
- PJ: indicar personas naturales autorizadas acceder
- Ultimo medio configurado = DDU vigente

### Bandeja de mensajes (art. 6)
- Todas notificaciones ordenadas por fecha y organo remitente

### Aviso de notificacion (art. 7)
- Cuando DDU = Casilla Unica: medio electronico para recibir avisos
- PJ: avisos al correo representante/autorizados
- Aviso = caracter informativo; NO hace veces de notificacion
- No recepcion de aviso NO invalida notificacion

### Excepciones (art. 8)
- Solicitud por interesado segun Parrafo 2, Titulo V Reglamento
- Ante organo tramitante o Registro Civil
- Organos que acojan → comunicar decision a Registro Civil via modulo institucional

### Leyes especiales (art. 9)
- Procedimientos con notificaciones propias: enviar copia al DDU (no sustituye forma legal especial)
- Solo actos administrativos efecto particular (excluye publicaciones)

### Reconfiguracion (art. 10)
- Cambiar Casilla Unica → correo electronico via modulo DDU
- Correo requiere validacion

## Notificaciones via Plataforma (arts. 11-21)

### Administrador institucional (art. 11)
Jefe Superior Servicio designa administrador permisos/perfiles notificaciones.

### Formas de envio (art. 12)
1. Funcionarios autorizados via modulo institucional (portal web)
2. API notificaciones (integracion automatica plataformas)

### Datos envio (art. 13)
1. Codigo organo (Gestor Codigos Estado, NT Interoperabilidad)
2. RUN/RUT destinatario(s)
3. Identificador expediente electronico (NT Documentos/Expedientes)
4. Identificacion procedimiento administrativo (NT Interoperabilidad)
5. Tipo notificacion (guia tecnica)
6. Asunto y descripcion
7. Documentos adjuntos o URI persistente expediente

### Estados resultado (art. 15)
1. Enviada exitosamente
2. Persona excepcionada → notificar segun art. 46 inc. 2-3 Ley 19.880
3. Sin DDU registrado → notificar segun art. 25 inc. 2 Reglamento
4. No enviada → reenviar; error persistente → comunicar Mesa Ayuda DGD

### Constancia fecha/hora (art. 16)
- Plataforma registra: fecha/hora envio, recepcion, codigo identificador transaccion
- Certificado digital (art. 26 Reglamento)
- Correo como DDU: constancia fecha/hora envio

### Trazabilidad (art. 17)
Plataforma registra:
1. Informacion envio (art. 13)
2. Estado notificaciones (art. 15)
3. Datos art. 16
4. Todos datos derivados operacion

### Consulta estado (art. 18)
Cada organo verifica estado via codigo identificador transaccion.

### Notificacion presencial (art. 19)
Funcionario deja constancia fecha/hora en Plataforma.

### Correo como DDU (art. 20)
Informar al interesado:
1. Mantener cuenta habilitada con capacidad recepcion
2. Revisar casilla correo no deseado
3. Verificar remitente via codigo transaccion

### Interrupcion servicio (art. 21)
- Indisponibilidad: certificado situacion
- Mantenciones programadas: aviso previo con fechas/horas
- Publicacion en portal web (arts. 47/7 Reglamento)
- Notificaciones pendientes: reenviar al restaurar servicio

## Disposiciones finales

- **Guia tecnica** (art. 22): DGD dicta guias aspectos operativos
- **Gradualidad** (art. 23): segun DFL 1/2020 SEGPRES
- **Revision** (art. 24): cada 2 anios minimo
