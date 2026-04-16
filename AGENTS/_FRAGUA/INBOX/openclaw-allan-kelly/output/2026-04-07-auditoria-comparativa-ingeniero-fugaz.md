# Auditoría Comparativa — Paquete "Ingeniero Fugaz" vs Paquete Allan Kelly

Fecha: 2026-04-07
Autor: Allan Kelly

---

## Veredicto ejecutivo

**El trabajo del ingeniero fugaz es bueno. No hay que desecharlo.**

Pero tampoco es equivalente al mío. Son dos paquetes con fortalezas distintas y complementarias. La recomendación es **fusionar selectivamente**, no elegir uno sobre otro.

---

## 1. Comparación dimensional

| Dimensión | Ingeniero fugaz (IF) | Allan Kelly (AK) | Juicio |
|---|---|---|---|
| **Usuarios identificados** | 19 (más granulares: médico regulador, gestor rutas, farmacia/bodega, conductor separados) | 17 (agrupación más compacta) | IF más granular; AK más comprimido. **Complementar** |
| **Historias de usuario** | ~20 nucleares narrativas + backlog MoSCoW de 40+ capacidades en 3 fases | 31 HU formales con CA, FHIR, normativa y prioridad P0/P1/P2 | AK más riguroso como contrato. IF más operativo como backlog. **Fusionar** |
| **Módulos** | 7 (M1-M7) | 11 | AK más granular en separación; IF más compacto. **AK subsume IF** |
| **Wireframes** | 5 pantallas + formulario visita móvil. Con datos reales HSC (nombres, diagnósticos, rutas reales) | 16 pantallas P0 con wireframes textuales genéricos | IF gana en realismo operativo; AK gana en cobertura P0. **Complementar** |
| **Modelo de datos** | 14 tablas MVP + DDL PostgreSQL ejecutable + vistas + funciones REM | Mapeo de 43 tablas ERD a módulos + mapeo FHIR de 25 recursos | IF tiene DDL ejecutable; AK tiene arquitectura completa. **Fusionar** |
| **Permisos/RBAC** | 14 roles × 7 módulos con CRUD+X detallado + segregación de datos sensibles | 17 usuarios × 11 módulos con R/W/RW | IF más rico en permisos (CRUD+X + segregación). **IF superior aquí** |
| **REM** | Funciones PostgreSQL ejecutables (fn_rem_*) | Especificación funcional + path equations | IF tiene implementación real. **IF superior aquí** |
| **Teleatención** | Diseño dedicado con tipos, reglas, escalamiento | 1 HU genérica P2 | IF mucho más profundo. **Complementar desde IF** |
| **Normativa** | Menciona DS 1/2022 y NT 2024 pero sin mapeo sistemático por HU | Cada HU tiene artículo normativo exacto | AK más trazable. **Complementar IF con trazabilidad AK** |
| **FHIR** | No menciona FHIR | 25 recursos mapeados | AK agrega capa de interoperabilidad. **Mantener de AK** |
| **Resumen ejecutivo** | Sí, orientado a dirección hospitalaria, con métricas de éxito | No tiene resumen ejecutivo separado | IF tiene pieza útil que AK no tiene. **Adoptar** |
| **Offline/mobile** | Diseño explícito offline-first para terreno | No abordado | IF agrega capacidad crítica. **Adoptar** |

---

## 2. Lo que IF tiene y AK no

### 2.1 DDL PostgreSQL ejecutable
IF entrega un `hodom-mvp.sql` con 14 tablas, enums, constraints, vistas y funciones REM listas para correr. AK no tiene DDL ejecutable.

**Veredicto: adoptar.** Es el artefacto más directamente ejecutable del paquete IF.

### 2.2 Datos reales en wireframes
Los wireframes de IF usan nombres reales de pacientes HSC (Néstor Riquelme, Corina Venegas, etc.), diagnósticos reales, rutas reales con 3 móviles (Servando, Hugo, Andrés) y datos operacionales verosímiles.

**Veredicto: adoptar como referencia de realismo.** AK usa datos genéricos.

### 2.3 Diseño de teleatención con profundidad
IF dedica una sección completa a teleatención:
- 6 tipos de interacción remota
- reglas de qué puede resolverse remotamente vs qué escala
- registro obligatorio por interacción
- diseño del módulo M4

AK tiene solo 1 HU genérica (HU-7.1, P2).

**Veredicto: adoptar el diseño de teleatención de IF.** Es una brecha clara de AK.

### 2.4 Permisos CRUD+X con segregación de datos sensibles
IF desglosa por capacidad dentro de cada módulo con permisos C/R/U/D/X, incluyendo reglas de episodio asignado, médico derivador, APS y paciente/cuidador.

AK tiene una matriz R/W/RW más simple.

**Veredicto: adoptar la matriz IF como base de RBAC.** Es más precisa.

### 2.5 Resumen ejecutivo para dirección
IF incluye un resumen de una página con problema, propuesta, métricas de éxito y entregables. Es un artefacto de comunicación institucional que AK no tiene.

**Veredicto: adoptar.** Útil para presentación a jefatura/dirección hospital.

### 2.6 Diseño offline-first para terreno
IF menciona explícitamente:
- "Mobile-first en terreno"
- "Offline-resilient: los registros de terreno deben poder crearse sin conexión y sincronizar después"
- Wireframe de registro de visita móvil con indicador de offline

AK no aborda offline.

**Veredicto: adoptar.** Es una necesidad real de la operación rural (zonas sin señal).

### 2.7 Métricas de éxito del MVP
IF define métricas concretas:

| Métrica | Línea base | Meta MVP |
|---|---|---|
| Tiempo generación REM | 2-3 días | < 1 hora |
| Registros en papel | ~80% | < 20% |
| Planillas Excel activas | 8-10 | 0 |
| Trazabilidad llamadas | parcial | 100% |
| Visitas sin registro | 10-15% | < 2% |

AK no tiene métricas de éxito.

**Veredicto: adoptar.** Cierra el contrato de valor del MVP.

---

## 3. Lo que AK tiene y IF no

### 3.1 Mapeo FHIR sistemático
25 recursos FHIR R4 mapeados a entidades del ERD. IF no menciona FHIR.

**Veredicto: mantener.** Habilita interoperabilidad futura y claridad semántica.

### 3.2 Trazabilidad normativa por HU
Cada HU de AK tiene artículo normativo exacto (DS 1/2022 art. X, NT 2024 §Y, Ley 20.584, etc.).

**Veredicto: mantener y aplicar a las HU que IF agrega.**

### 3.3 Path equations como constraints
12 path equations del modelo categorial traducidos a constraints implementables.

**Veredicto: mantener.** IF tiene algunos constraints en DDL, pero no los 12 del modelo categorial.

### 3.4 Flujos de estado formales
- Lifecycle del episodio (6 estados)
- Lifecycle de la visita (13 estados)
- Lifecycle del plan
- Lifecycle de medicación

IF tiene estados pero menos formalizados.

**Veredicto: mantener como referencia canónica de máquina de estados.**

### 3.5 Cobertura P0 completa en wireframes (16 pantallas)
AK cubre las 15 HU P0 en 16 pantallas. IF cubre 5 pantallas pero más ricas.

**Veredicto: mantener AK como cobertura completa; enriquecer con el realismo de IF.**

### 3.6 Arquitectura de información con 43 tablas mapeadas a módulos
AK mapea cada módulo a las entidades del ERD completo de 43 tablas + integraciones externas.

**Veredicto: mantener como arquitectura de referencia.** El DDL de IF es un subconjunto funcional correcto para MVP.

---

## 4. Dónde hay contradicción

### 4.1 Número de módulos
- IF: 7 módulos (M1-M7)
- AK: 11 módulos

**Resolución:** Los 7 de IF se mapean dentro de los 11 de AK. No hay contradicción real; AK es más granular. Usar los 11 de AK como referencia y los 7 de IF como agrupación MVP.

### 4.2 Priorización
- IF: MoSCoW (Must/Should/Could) en 3 fases
- AK: P0/P1/P2 en 3 fases

**Resolución:** Son equivalentes. Los Must de IF ≈ P0 de AK. Fusionar usando la nomenclatura P0/P1/P2 con el contenido de ambos.

### 4.3 Modelo de datos
- IF: 14 tablas MVP (subconjunto deliberado)
- AK: 43 tablas como referencia completa

**Resolución:** No hay contradicción. IF hizo un recorte MVP correcto. AK tiene la foto completa. Usar IF para implementar Fase 1 y AK como roadmap de expansión.

### 4.4 Usuarios
- IF: 19 usuarios (incluye médico regulador, gestor rutas, farmacia/bodega como roles separados)
- AK: 17 usuarios

**Resolución:** IF es más granular en roles operativos. Fusionar tomando la granularidad de IF donde agrega valor (médico regulador, gestor rutas, bodega).

---

## 5. Dónde IF es débil

### 5.1 Sin mapeo FHIR
No prepara interoperabilidad futura.

### 5.2 Sin trazabilidad normativa por capacidad
Menciona normativa pero no la ancla sistemáticamente.

### 5.3 Sin path equations ni constraints formales del modelo categorial
El DDL tiene algunos CHECK, pero no los 12 path equations.

### 5.4 Sin flujos de estado formalizados
Tiene estados pero no máquina de estados explícita con transiciones validadas.

### 5.5 No integra los modelos OPM v2.5 ni categorial v4.1 explícitamente
AK cruza con ambos modelos; IF trabaja más desde la documentación legacy y operacional directa.

---

## 6. Dónde AK es débil

### 6.1 Sin DDL ejecutable
No hay SQL para correr.

### 6.2 Sin diseño offline/mobile
No aborda la realidad del terreno rural.

### 6.3 Sin teleatención profunda
Solo 1 HU genérica vs diseño completo de IF.

### 6.4 Sin resumen ejecutivo para dirección
No tiene artefacto de comunicación institucional.

### 6.5 Sin métricas de éxito
No define cómo medir si el MVP funcionó.

### 6.6 Wireframes genéricos vs datos reales
AK usa datos ficticios; IF usa nombres y rutas reales de HSC.

---

## 7. Recomendación de fusión

### Base: AK (por rigor, trazabilidad y cobertura)

### Complementar con IF:

| Pieza IF | Acción | Destino |
|---|---|---|
| DDL PostgreSQL ejecutable | Adoptar como artefacto de implementación Fase 1 | Agregar al paquete |
| Diseño de teleatención (tipos, reglas, escalamiento) | Adoptar y expandir HU-7.1 | Enriquecer historias de usuario |
| Matriz RBAC CRUD+X + segregación | Reemplazar la matriz R/W/RW de AK | Actualizar arquitectura |
| Resumen ejecutivo | Adoptar como artefacto de comunicación | Agregar al paquete |
| Métricas de éxito MVP | Adoptar | Agregar al paquete |
| Diseño offline-first | Adoptar como requisito transversal | Agregar a arquitectura |
| Datos reales en wireframes | Usar como referencia de realismo | Enriquecer wireframes |
| Registro de llamadas como módulo | Adoptar la profundidad de IF | Enriquecer módulo |
| Backlog MoSCoW detallado | Fusionar con HU priorizadas de AK | Crear backlog unificado |
| Roles adicionales (médico regulador, gestor rutas, bodega) | Incorporar a la lista de usuarios | Actualizar usuarios |

### Mantener de AK sin cambio:

| Pieza AK | Razón |
|---|---|
| Mapeo FHIR (25 recursos) | IF no lo tiene |
| Trazabilidad normativa por HU | IF no la ancla |
| Path equations como constraints | IF solo tiene subset |
| Flujos de estado formales | IF tiene menos rigor |
| Cobertura completa P0 (16 pantallas) | IF cubre solo 5 |
| Arquitectura de información (43 tablas → módulos) | IF tiene solo 14 tablas MVP |
| Integraciones externas | IF no las especifica |

---

## 8. Lo que no hay que hacer

1. **No descartar el paquete IF.** Tiene artefactos ejecutables que AK no tiene.
2. **No descartar el paquete AK.** Tiene rigor, trazabilidad y cobertura que IF no tiene.
3. **No copiar ambos sin fusionar.** Eso genera duplicación y confusión.
4. **No tratar el DDL de IF como modelo final.** Es un MVP correcto, pero el modelo completo es el ERD de 43 tablas.

---

## 9. Calificación del trabajo IF

| Dimensión | Nota | Comentario |
|---|---|---|
| Comprensión del dominio | ⭐⭐⭐⭐ | Muy buena lectura operativa del problema real |
| Usuarios y necesidades | ⭐⭐⭐⭐ | 19 usuarios bien caracterizados, granulares |
| Diseño de módulos | ⭐⭐⭐⭐ | 7 módulos coherentes con bounded domains claros |
| Wireframes | ⭐⭐⭐⭐⭐ | Excelentes, con datos reales, mobile-first y offline |
| Modelo de datos | ⭐⭐⭐⭐ | DDL ejecutable, recorte MVP correcto |
| Permisos/RBAC | ⭐⭐⭐⭐⭐ | Mejor que AK en esta dimensión |
| Teleatención | ⭐⭐⭐⭐⭐ | Diseño profundo que AK no tiene |
| Trazabilidad normativa | ⭐⭐ | Menciona pero no ancla |
| FHIR/interoperabilidad | ⭐ | No lo aborda |
| Rigor formal (estados, constraints) | ⭐⭐ | Tiene algo, pero no formalizado |
| Ejecutabilidad | ⭐⭐⭐⭐⭐ | DDL + vistas + funciones REM listas |
| Comunicación institucional | ⭐⭐⭐⭐⭐ | Resumen ejecutivo muy claro |

**Nota global: trabajo sólido, pragmático y orientado a implementación.** Le falta rigor formal y preparación para interoperabilidad, pero compensa con ejecutabilidad directa.

---

## 10. Siguiente paso

Producir un **paquete fusionado v1.0** que tome:
- la estructura y rigor de AK como esqueleto
- los artefactos ejecutables de IF como músculo
- y cierre las brechas de ambos

Eso daría un paquete de diseño completo, ejecutable y trazable.
