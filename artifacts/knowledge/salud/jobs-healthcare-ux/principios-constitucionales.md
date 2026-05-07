---
_manifest:
  urn: urn:salud:kb:jobs-healthcare-ux-principios
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Extraido del agente jobs-healthcare-ux (~/.claude/agents/jobs-healthcare-ux.md),
      disenado para ser el corpus de conocimiento de la skill KORA correspondiente.
  version: 1.0.0
version: 1.0.0
status: publicado
family: normative
tags:
- salud
- healthcare-ux
- principios
- diseno-clinico
- ux
- ehr
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:jobs-healthcare-ux-principios
---

# 18 principios constitucionales de UX clinico

Principios que gobiernan el diseno de experiencias para sistemas
institucionales de salud. No son sugerencias ni heuristicas optativas.
Son la constitucion que gobierna cada juicio de diseno. Cuando dos
principios entran en tension, se explicita y se resuelve con criterio
clinico.

## I. La mirada pertenece al paciente

El medico debe mirar al paciente, no a la pantalla. Todo diseno que robe
la mirada del clinico esta robando la relacion terapeutica. La interfaz
ideal es la que no necesita ser mirada.

- **Operativamente**: ambient listening sobre formularios, voz sobre
 teclado, inferencia sobre entrada manual, resumen post-consulta sobre
 documentacion en tiempo real.
- **Metrica**: tiempo de pantalla ELIMINADO de la consulta, no
 "mejorado".

## II. El sistema tiene criterio, no configuracion

No dashboards personalizables. No "configure su vista". No layouts
drag-and-drop. Cada opcion de configuracion es una confesion de que el
disenador no tuvo el coraje de decidir. El sistema sabe que informacion
necesita cada perfil clinico.

- **Legitimo**: adaptacion contextual automatica -- el sistema observa
 como trabaja cada clinico y se ajusta.
- **Ilegitimo**: trasladar la carga de configuracion al usuario.

## III. Ganar el derecho a interrumpir

Cada alerta debe pasar una prueba: si esta alerta fuera una persona que
te toca el hombro mientras atiendes a un paciente, mereceria la
interrupcion?

- **NNT equivalente para alertas**: cuantas alertas se deben mostrar para
 que UNA prevenga un evento adverso real.
- **Estratificacion**: alertas de baja especificidad se acumulan
 silenciosamente en un canal secundario.
- **Learning loop**: si un clinico descarta sistematicamente un tipo de
 alerta, eso es senal de diseno, no de negligencia.

## IV. La complejidad es nuestra, la claridad es del usuario

La medicina es inherentemente compleja. Esa complejidad la absorbe el
sistema, no el usuario. Detras de una interfaz limpia hay un motor de
inferencia, normalizacion, cruce de datos y logica clinica trabajando.

- **Progressive disclosure clinico**: profundidad disponible bajo demanda,
 superficie radicalmente simple.

## V. El tiempo del clinico se mide en vidas

Cada minuto que el sistema le roba a un clinico es un minuto que no
dedica a un paciente. A escala institucional, 30 segundos ahorrados por
consulta en un hospital con 500 consultas diarias son 250 minutos -- mas
de 4 horas de atencion clinica recuperada cada dia.

- **Metrica**: tiempo-reloj real por flujo.
- **Benchmark**: cuanto toma el primer dia sin entrenamiento, no cuanto
 toma con entrenamiento.

## VI. La narrativa primero, la estructura despues

El pensamiento clinico es narrativo. Los formularios estructurados matan
esta narrativa natural. El sistema debe aceptar la narrativa en lenguaje
natural y EXTRAER la estructura, no imponerla.

- **SOAP natural**: el clinico habla o escribe como piensa. El sistema
 organiza. El clinico revisa y corrige.

## VII. Disenar para el equipo, no para el rol

La unidad de cuidado no es el medico. Es el equipo: medico, enfermero,
tecnico, farmaceutico, trabajador social, familiar. Los sistemas que
disenan vistas por rol crean silos de informacion.

- **Operativamente**: flujo de cuidado del paciente donde cada miembro
 ve lo que necesita PARA LA TAREA que esta realizando ahora.

## VIII. La transicion no existe

Para el paciente, el cuidado es continuo. No hay "alta de urgencias" y
"ingreso a piso" -- hay una persona que sigue enferma y se mueve de lugar.

- **Operativamente**: cero re-entrada de datos en transiciones. El
 contexto viaja con el paciente, no con el episodio administrativo.

## IX. Dignidad en cada pixel

El paciente es una persona, no un registro. Cada pantalla debe transmitir
dignidad: nombre antes que numero de historia clinica, contexto de vida
antes que lista de diagnosticos, preferencias antes que alergias codificadas.

- **Anti-lenguaje**: no "el diabetico de la cama 4" sino "Maria Gonzalez,
 67 anos, vive con su hija, diabetes desde 2015".

## X. Cero entrenamiento o no existe

Si el sistema requiere un curso de capacitacion, ha fracasado. Un
residente que llega a las 2 AM de su primer dia debe poder usar el sistema
productivamente en los primeros 5 minutos.

- **Defaults clinicamente inteligentes**. Guiar sin instruir.

## XI. Offline es el caso base

En Latinoamerica, en zonas rurales, en emergencias, la conectividad no es
garantia. El caso base de diseno es offline. La conectividad es un
enhancement.

- **Operativamente**: sistema completo en modo local. Sincroniza cuando
 puede. La version mas reciente del dato clinico gana en conflictos.

## XII. La privacidad es experiencia, no checkbox

La privacidad no se resuelve con un formulario de consentimiento. Se
resuelve con diseno: que informacion se muestra a quien, cuando, como.

- **Awareness contextual**: el sistema sabe donde esta el dispositivo
 (consultorio vs pasillo vs sala de espera) y ajusta la exposicion de
 datos sensibles.

## XIII. Medir lo que importa

Las metricas de exito no son clicks, page views ni adoption rate. Son:
tiempo-a-decision-clinica, eventos adversos prevenidos, readmisiones
evitadas, satisfaccion del paciente, burnout clinico reducido, continuidad
de cuidado.

- **Regla**: si una metrica no conecta con un outcome de salud, no es una
 metrica -- es vanidad.

## XIV. Lo bello no es decoracion, es funcion

La estetica en healthcare no es lujo. Es herramienta cognitiva. Una
interfaz visualmente clara reduce errores. Una jerarquia tipografica bien
disenada acelera el escaneo de informacion critica.

- **Cada decision visual responde a una pregunta clinica**: que necesita
 ver primero el clinico? que puede pasar desapercibido con consecuencias
 graves?

## XV. Disenar para las 2 AM

El usuario de diseno no es el medico descansado de las 10 AM. Es el
residente que lleva 18 horas de guardia, a las 2 AM, con tres pacientes
criticos, un celular con pantalla rota, y luz fluorescente.

- **Operativamente**: contraste alto por default, tamanos de fuente
 generosos, targets de toque grandes, flujos que perdonan errores, undo
 omnipresente.

## XVI. El error mas peligroso es el silencioso

Un error ruidoso (mensaje de error) es preferible a un error silencioso
(dato guardado mal, alerta no disparada, orden duplicada sin aviso).

- **Operativamente**: audit trail clinico completo, reconciliacion activa
 de datos, deteccion de anomalias en ordenes.

## XVII. Heredar con humildad, reemplazar con paciencia

Los sistemas de salud existentes tienen decadas de datos, flujos arraigados
y personal que aprendio a trabajar con sus limitaciones. No se puede llegar
con arrogancia a "disrumpir" un hospital.

- **Operativamente**: migracion progresiva, coexistencia con sistemas
 legacy, importacion fidedigna de datos historicos.

## XVIII. Esto no se termina nunca

El diseno de sistemas de salud no tiene version final. La medicina
evoluciona, las guias clinicas cambian, los patrones de enfermedad se
transforman. El sistema debe estar disenado para evolucionar continuamente
sin disrumpir el cuidado.

- **Operativamente**: arquitectura modular, configuracion sin redespliegue,
 feedback loops continuos, humildad epistemologica.
