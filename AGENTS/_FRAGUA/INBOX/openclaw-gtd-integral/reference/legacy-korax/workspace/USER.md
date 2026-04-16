## Perfil

- **Nombre:** Felix Sanhueza
- **Nombre operativo:** Korvo
- **Rol:** Funcionario GORE Nuble / Hospital. Lider tecnico, profesional multidisciplinario.
- **Ubicacion:** Santiago timezone (America/Santiago, UTC-3/UTC-4)
- **Contexto organizacional:** Gobierno Regional, sector publico, coordinacion interinstitucional

## Rutinas

| Rutina | Horario | Frecuencia | Trigger |
| --- | --- | --- | --- |
| Planificacion matutina | 08:00 | L-V | heartbeat_morning / `/plan` |
| Cierre nocturno | 21:00 | Diario | heartbeat_evening / `/close` |
| Sincronizacion estrategica | Viernes 20:00 | Quincenal (semanas impares) | heartbeat_sync / `/sync` |
| Modo Caos | Libre | Minimo 2h/semana (INV-11) | `/caos` |

## Umbrales de Salud del Sistema

| Metrica | Rango Saludable | Senal de Problema | Accion |
| --- | --- | --- | --- |
| Candidatos en buffer | 0-30 | >30 | Sugerir triaje urgente o bancarrota |
| UTs bloqueadas | <50% | >=50% | Alertar en micro-check |
| Bloques DEEP/semana | >=2 | 0-1 | Alertar deficit de tiempo profundo |
| Dias sin triaje | 0-2 | >=3 | Activar protocolo de abandono |
| Senales de colapso | 0-1 | >=3 | Activar modo emergencia |
| Horas Modo Caos/semana | >=2 | 0 | Recordar proteccion de caos |
| Tiempo en sistema | <10% | >10% | Simplificar (P1) |
| Bloqueos cross-project >7d | 0 | >=1 | Alertar en sync |
| completitud() estancada >14d | N/A | Objetivo sin progreso | Candidato a bancarrota |
| Throughput 14d | >=0 | <0 por >4 semanas | Alertar acumulacion de deuda |

## Preferencias de Output

- **Idioma:** es-CL (espanol chileno)
- **Registro:** casual pero preciso
- **Formato:** Markdown con emojis funcionales (📥 captura, ✅ completado, ⚠️ alerta, 🛑 colapso, 🌀 caos). Tablas para datos, bullets para listas.
- **Longitud:** minima necesaria. Si se puede decir en 1 linea, no usar 3.
- **Detalle:** Minimo viable. Datos > prosa.
- **Confirmaciones:** Una linea. Sin elaboracion.
- **Reportes:** Tablas y conteos. Sin narrativa.
