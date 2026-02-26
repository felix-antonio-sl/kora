---
_manifest:
  urn: "urn:tde:kb:guia-seguridad-ciberseguridad"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/guias/GU-CIBER-001"
version: 1.0.0
status: published
tags: [tde, guia, seguridad-informacion, ciberseguridad, norma-tecnica, ley-21180]
lang: es
---

# Guía Técnica de Seguridad de la Información y Ciberseguridad

Base legal: art. 12, Norma Técnica de Seguridad de la Información y Ciberseguridad (Ley N° 21.180).
Objetivo: lineamientos para implementar controles de seguridad de la información y ciberseguridad en OAE.
Versión: 1.0 (24/03/2025).

---

## 1. Marco normativo y alcance

- Términos e implementación se interpretan según la Norma Técnica de Seguridad de la Información y Ciberseguridad.
- Aplica a todos los órganos de la Administración del Estado (OAE).
- Complementa: Ley Marco de Ciberseguridad, Norma Técnica de Interoperabilidad, Norma Técnica de Calidad y Funcionamiento.

## 2. Función de Identificación

### 2.1 Gestión de activos de información

- Identificar, clasificar y registrar activos de información (hardware, software, datos, redes, personas).
- Mantener inventario actualizado con: nombre, tipo, ubicación, responsable, nivel de criticidad.
- Clasificar según confidencialidad, integridad, disponibilidad.

### 2.2 Política de Seguridad de la Información y Ciberseguridad

Contenido mínimo:
- Objetivos institucionales de seguridad
- Alcance organizacional
- Roles y responsabilidades
- Lineamientos para gestión de riesgos
- Marco regulatorio aplicable
- Mecanismos de actualización y difusión

### 2.3 Gestión de riesgos

- Implementar metodología formal de gestión de riesgos (ej. ISO 31000, NIST CSF).
- Evaluar probabilidad e impacto por activo.
- Definir controles mitigadores y riesgos residuales aceptables.
- Revisión periódica (mínimo anual).

### 2.4 Roles institucionales

| Rol | Responsabilidad clave |
|-----|----------------------|
| Jefatura de Servicio | Aprobación de política, asignación de recursos |
| Encargado de Seguridad (CISO) | Coordinación del SGSI, gestión de incidentes |
| Encargado de Ciberseguridad | Implementación técnica de controles |
| Coordinador TI | Soporte infraestructura y plataformas |
| Delegado de Datos Personales | Cumplimiento normativa de datos personales |
| Funcionarios | Cumplimiento de políticas, reporte de incidentes |

### 2.5 Seguridad en cadena de suministro

- Incluir cláusulas de seguridad en contratos con proveedores.
- Evaluar cumplimiento de seguridad de terceros periódicamente.
- Controlar accesos de proveedores a sistemas institucionales.

## 3. Función de Protección

### 3.1 Control de acceso

- Principio de mínimo privilegio.
- Autenticación multifactor para sistemas críticos.
- Revisión periódica de permisos y cuentas.
- Bloqueo automático tras intentos fallidos.
- Registro de accesos (usuarios, fecha/hora, acciones).

### 3.2 Capacitación y concientización

- Programa permanente de formación en seguridad.
- Campañas periódicas de concientización.
- Capacitación específica por rol.
- Evaluación de efectividad de las acciones formativas.

### 3.3 Seguridad de datos

#### Controles criptográficos

| Nivel de cifrado | Largo mínimo clave | Uso recomendado |
|-----------------|--------------------|--------------------|
| Bajo | AES 128 bits / RSA 2048 bits | Información general |
| Medio | AES 192 bits / RSA 3072 bits | Información sensible |
| Alto | AES 256 bits / RSA 4096 bits | Datos personales, información crítica |

- Cifrado en tránsito: TLS 1.2+ obligatorio.
- Cifrado en reposo: según clasificación de activo.
- Gestión segura de claves criptográficas.

#### Eliminación segura de datos

- Procedimientos formales de eliminación.
- Respetar plazos reglamentarios de retención (auditorías, legales).
- Certificar destrucción de medios.

### 3.4 Interoperabilidad y transferencia segura

- Cifrado punto a punto en toda interoperabilidad.
- Protocolos no obsoletos ni de baja seguridad.
- Autenticación segura de nodos y servicios.
- Datos personales/sensibles: cifrado nivel alto.
- Responsabilidades definidas por cada OAE que interopera.
- Cumplimiento de Norma Técnica de Interoperabilidad.

### 3.5 Desarrollo seguro de plataformas

- Entorno de desarrollo seguro + capacitación periódica.
- Ambientes separados: desarrollo, testing, producción.
- Seguridad en repositorios de código fuente.
- Pautas de codificación segura por lenguaje/framework (ej. OWASP).
- Requisitos mínimos de seguridad al inicio del ciclo.
- Ethical hacking + análisis de vulnerabilidades antes de pase a producción.
- Herramientas de análisis de código automatizadas.

### 3.6 Control de cambios

Procedimiento mínimo:
- Revisión de pertinencia + autorización + pruebas (ej. pull requests, tests unitarios).
- Registro de actividades del cambio.
- Evaluación de riesgo de seguridad (ej. herramientas de análisis de código).
- Planes de rollback.
- Proceso hotfix para vulnerabilidades urgentes.
- Gestores de versionamiento para recuperar estados anteriores.

### 3.7 Gestión de respaldos

- Frecuencia definida y documentada según plan de continuidad.
- Pruebas de integridad de cada respaldo.
- Procedimiento de restauración documentado + verificación post-restauración.
- Almacenamiento en locación geográfica distinta al servidor.
- Mismas medidas de protección física/lógica que servidores.
- Respaldos cifrados según controles criptográficos.

### 3.8 Gestión de vulnerabilidades técnicas

- Categorización por nivel de riesgo.
- Líneas de acción con roles y tiempos definidos por criticidad.
- Aplicación de parches y controles correctivos.
- Enmarcado en gestión de cambios o respuesta a incidentes según urgencia.

### 3.9 Plan de continuidad

- Equipo de Respuesta a Incidentes de Seguridad Informática (art. 24 lit. d, Ley Marco de Ciberseguridad).
- Nivel de riesgos tolerables y tiempo máximo de recuperación por plataforma.
- Planes de respuesta y recuperación por plataforma.
- Planes de prueba para servicios esenciales.

### 3.10 Procesos de RRHH

Cláusulas de seguridad en nombramientos/convenios:
- Confidencialidad y no divulgación de datos personales/sensibles.
- Restricciones sobre propiedad intelectual.
- Responsabilidad de clasificación de información.
- Sanciones por omisión de requisitos de seguridad.
- Vigencia mientras duren contratos/convenios (extensibles por ley).

## 4. Función de Detección

### 4.1 Registro de eventos

Contenido mínimo de logs:
- Identificación del usuario (IP, nombre).
- Registro horario.
- Intentos fallidos y exitosos.
- Acciones y transacciones realizadas.
- Información accedida.

### 4.2 Análisis de eventos

- Identificación de causal de origen y motivo.
- Correlación con eventos anteriores.
- Determinación de impacto potencial.
- Herramientas de correlación de logs + alertas tempranas.
- Separación de eventos de riesgo tolerable vs. eventos que requieren análisis profundo.

### 4.3 Monitoreo continuo

#### Gestión de código malicioso
- Protección actualizada automáticamente.
- Revisiones rutinarias a plataformas y redes.
- Incorporación en plan de continuidad.
- Análisis de comportamiento del código malicioso detectado.

#### Monitoreo de red
- Acceso solo a autorizados formalizados.
- Cortafuegos (nunca configuración de fábrica).
- Registro y monitoreo de tráfico (normal vs. eventos).
- Monitoreo continuo de puertos, protocolos, servicios.
- Todos los puertos cerrados por defecto; apertura controlada y temporal.
- Segregación de redes por dominios y nivel de acceso.

### 4.4 Proceso de detección

- Roles y responsabilidades definidos.
- Cumplimiento de política de seguridad + análisis de riesgos.
- Comunicación de eventos a interesados.
- Mediciones continuas de efectividad.

## 5. Función de Respuesta

### 5.1 Plan de respuesta ante incidentes

Activación: una vez confirmado el incidente. Contenido mínimo:

1. **Notificación**: a ANCi y regulador cuando corresponda.
2. **Identificación**: activos, controles, roles afectados; evaluación de impacto; verificación de interceptación/compromiso; evaluación de datos sensibles comprometidos; evaluación de daño a servidores.
3. **Mitigación**: contención inmediata para minimizar amplitud del incidente.
4. **Restablecimiento**: erradicación del riesgo, actualización de parches, cierre de accesos, modificación de contraseñas comprometidas, reconfiguración/reemplazo de hardware, restauración de servicio, verificación de exfiltración/pérdida de datos.
5. **Comunicación**: canales definidos; declaraciones internas y públicas describiendo naturaleza, causas, alcance, pasos y actualizaciones.
6. **Evidencia forense**: preservar artefactos y detalles para análisis posterior.
7. **Registro y seguimiento**: registro completo (hora, datos, tipo, descubridor, ubicación, alcance).
8. **Informe**: componentes afectados documentados.
9. **Mejora continua**: lecciones aprendidas, identificación de causa raíz, mejora de controles.

### 5.2 Análisis forense

Post-incidente:
- Recopilación de evidencia con integridad y cadena de custodia.
- Resolución de debilidad/vulnerabilidad causante.
- Actualización de procedimientos con lecciones aprendidas.

## 6. Función de Recuperación

### 6.1 Gestión de incidentes de seguridad

Proceso mínimo:
- Escala de la Guía de Notificación de Incidentes de ANCi.
- Determinación de activos involucrados e impacto sobre servicios.
- Activación de planes de respuesta y continuidad operativa.
- Notificación al CSIRT de Gobierno según Guía de Notificación.

## 7. Revisión y actualización

- Revisión mínimo anual.
- Registro de todas las versiones y adecuaciones.

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | 24/03/2025 | Versión inicial |
