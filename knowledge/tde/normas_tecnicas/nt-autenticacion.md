---
_manifest:
  urn: "urn:tde:kb:nt-autenticacion"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto9"
version: 1.0.0
status: published
tags: [decreto, norma-tecnica, autenticacion, clave-unica, clave-tributaria, tde, ley-21180]
lang: es
---

# DS 9 — Norma Tecnica de Autenticacion

- **Promulgacion**: 19-MAY-2023
- **Publicacion**: 17-AGO-2023
- **Base legal**: Ley 21.180 (TDE) + DS 4/2020 (Reglamento) + DFL 1/2020 (Gradualidad)
- **Revision**: cada 2 anios desde vigencia

## Objeto (art. 1)

Establecer forma en que organos AE implementan/integran mecanismos oficiales de autenticacion en plataformas electronicas institucionales → validar identidad de quienes acceden a plataformas que soportan procedimientos administrativos.

## Definiciones (art. 2)

| Termino | Definicion |
|---------|-----------|
| Autenticacion | Proceso electronico que valida datos identificacion usuario → acceso plataforma |
| Factor de autenticacion | Dato(s) reservado(s)/inherente(s) al usuario para establecer identidad con grado confianza |
| Mecanismo de autenticacion | Metodo/procesos que sustentan autenticacion con nivel confianza determinado |
| Mecanismo oficial | Mecanismo que cumple NT + validacion SEGPRES |
| Plataforma electronica | Software + datos + infraestructura que sustenta procesos/procedimientos |
| Usuarios | Personas naturales/apoderados, representantes PJ, funcionarios |

## Mecanismos oficiales de autenticacion

### Regla general (art. 3)
- Organos AE DEBEN usar mecanismos oficiales para acceso interesados a plataformas
- Excepcion: normativa aplicable exima tramitacion electronica (art. 18 inc. 5 Ley 19.880)
- Otros mecanismos: requieren autorizacion previa expresa de SEGPRES

### ClaveUnica (art. 4)

| Aspecto | Detalle |
|---------|---------|
| Administrador | SEGPRES via Division Gobierno Digital |
| Uso | Exclusivo personas naturales |
| Estandar | OpenID Connect |
| Factor | Contrasena creada/administrada por persona, vinculada a RUN |
| Enrolamiento | Servicio Registro Civil e Identificacion |
| Infraestructura | DGD administra plataforma habilitacion, infraestructura, monitoreo, validacion datos |
| TyC | Determinados por DGD; aceptados por Jefe Superior Servicio |

### Clave Tributaria (art. 5)

| Aspecto | Detalle |
|---------|---------|
| Administrador | Servicio Impuestos Internos |
| Uso | Exclusivo PJ / entidades sin personalidad juridica (como agrupacion) |
| Factor | Contrasena entregada por SII |
| Restriccion critica | Solo SII puede usar Clave Tributaria para autenticar personas naturales (en sus propias plataformas/tramites). Autenticacion PN via CT ante otros organos = sin validez |
| TyC | Determinados por SII; aceptados por Jefe Superior Servicio |

## Requisitos tecnicos (arts. 6-9)

### Estandares (art. 6)
- Protocolos: OpenID Connect + OAuth 2.0 (o superiores)
- Almacenamiento datos identificacion: cifrado con Bcrypt, PBKDF2, SHA-3, Argon2 (o superiores)
- Transmision: TLSv1.2 o superior
- Registros: trazables

### Prevencion accesos no autorizados (art. 7)
- Captcha u otros mecanismos
- Limite maximo intentos fallidos + bloqueo
- Procedimiento de desbloqueo obligatorio

### Usabilidad (art. 8)
- Buenas practicas UX y accesibilidad web
- Cumplir definiciones marca/lineamientos graficos del administrador mecanismo

### TyC (art. 9)
Administrador mecanismo publica TyC en su web.

## Integracion (arts. 10-11)

### Proceso integracion (art. 10)
Etapas:
1. Solicitud integracion al administrador mecanismo
2. Entrega credenciales + integracion en plataforma
3. Certificacion integracion + habilitacion

### Revocacion (art. 11)
Administrador revoca inmediatamente habilitacion a organo que incumpla estandares/usos de NT o guias.

## Uso por organos AE (arts. 12-15)

### Deber informacion (art. 12)
- Informar inmediatamente al CSIRT (Min. Interior) + administrador mecanismo ante sospecha riesgos/amenazas
- Informar oportunamente aumentos demanda no previstos que afecten funcionamiento

### Trazabilidad accesos (art. 13)
Registro por cada acceso autenticado:
1. Identificador usuario (PJ via CT: forma definida por SII)
2. Fecha/hora acceso en UTC+00:00 (sincronizacion con SHOA)

### Proteccion datos personales (art. 14)
- Cumplir Ley 19.628 (Proteccion Vida Privada)
- Mecanismos garantizando: reserva, proteccion, derecho acceso/rectificacion/cancelacion/oposicion
- Datos solo para finalidades previstas en ley

### Factores adicionales (art. 15)
- Organos PUEDEN implementar factores complementarios
- Especialmente en plataformas con informacion sensible
- Evaluar necesidad segun procedimientos; facilitar acceso interesados

## Validacion nuevo mecanismo oficial (arts. 16-18)

### Solicitud (art. 16)
- Cualquier momento ante SEGPRES via DGD
- Resolucion previa consulta a Registro Civil

### Requisitos (art. 17)
Cumplir procesos/estandares de esta NT + guia tecnica.

### Gestion usuarios (art. 18)
Mecanismo oficial requiere:
1. **Enrolamiento**: proceso seguro, minimizar suplantacion, protocolo atencion, politicas privacidad, acciones educacion/promocion, recomendaciones seguridad
2. **Gestion datos identificacion**: procesos creacion/modificacion/revocacion credenciales/dispositivos
3. **Soporte usuarios**: servicio consultas generales/especificas, problemas uso

## Disposiciones finales

- **Guia tecnica** (art. 19): DGD dicta guias aspectos operativos
- **Gradualidad** (art. 20): segun DFL 1/2020 SEGPRES
- **Revision** (art. 21): cada 2 anios minimo
