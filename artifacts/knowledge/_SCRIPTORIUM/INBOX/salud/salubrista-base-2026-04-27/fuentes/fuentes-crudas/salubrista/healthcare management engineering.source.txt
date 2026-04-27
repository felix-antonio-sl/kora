# healthcare management engineering

<!-- /atomize · 290 proposiciones · ~125 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICIÓN, REGLA...), o por entidad -->

## Preface

### What Is This Book About?
- [P001] **DEFINICIÓN** — healthcare management engineering = desarrollo sistemático decisiones gerenciales → asignación eficiente recursos (materiales, humanos, financieros) mediante métodos matemáticos/simulación
- [P002] **DEFINICIÓN** — sinónimos management engineering: operations research, system engineering, industrial engineering, operations management, management science
- [P003] **HECHO** — autor Alexander Kolker, Children's Hospital Milwaukee WI; Springer 2012; ISBN 978-1-4614-2067-5
- [P004] **HECHO** — libro cubre 26 problemas gestión operacional hospital/clínica comparando enfoque tradicional vs management engineering
- [P005] **DEFINICIÓN** — sistema = elementos interconectados formando todo complejo comportándose diferente a elementos independientes
- [P006] **DEFINICIÓN** — sistema salud definible nivel nacional (hospitales, clínicas, aseguradoras, CMS) o hospital individual (ED, cirugía, ICU)
- [P007] **ALCANCE** — enfoque libro: management engineering escala hospital individual o clínica grande
- [P008] **ALCANCE** — dominios: capacidad, staffing, scheduling, patient flow, asignación recursos, forecasting, ubicación, workflow, productividad, supply chain, BI/DM
- [P009] **HECHO** — 5 tipos problema: (1) balance dinámico oferta/demanda DES/QAT, (2) optimización lineal/probabilística, (3) forecasting series temporales, (4) BI/data mining, (5) teoría juegos
- [P010] **HECHO** — software DES: ProcessModel 5.3.0; alternativas ProModel, Arena, Simul8, AnyLogic, Simio, FlexSim
- [P011] **⚠ TENSIÓN** — QAT frecuentemente recomendado para capacidad/patient flow hospitalario pero subestima limitaciones prácticas serias (D'Alesandro 2008) y sobreestima dificultad DES
- [P012] **HECHO** — reporte NAE/IOM (Reid et al. 2005): pocos profesionales salud equipados pensar analíticamente sobre healthcare delivery como sistema
- [P013] **HECHO** — Mayo Clinic definió Science of Healthcare Delivery como 1/4 direcciones estratégicas (Quality, Individualized Medicine, Integration)

### Who Is This Book For?
- [P014] **ALCANCE** — libro para líderes hospital/clínica (directores, VPs, COOs, CEOs, board) y estudiantes MBA/Healthcare Management

## Traditional Management and Management Engineering

### Definitions and Comparison
- [P015] **DEFINICIÓN** — traditional management = experiencia pasada, intuición, estimaciones, proyecciones lineales, valores promedio variables input
- [P016] **DEFINICIÓN** — management engineering pasos: (1) meta medible clara, (2) identificar recursos aprovechables, (3) modelos matemáticos testear escenarios/consecuencias
- [P017] **REGLA** — decisiones management engineering frecuentemente diferentes de tradicionales — a veces contraintuitivas
- [P018] **REGLA** — ambientes altamente variables; tratar promedios como fijos → conclusiones seriamente inexactas → `flaw of averages`
- [P019] **REGLA** — sistemas healthcare contienen interconexiones ocultas → consecuencias no intencionadas decisiones aparentemente razonables
- [P020] **REGLA** — efecto escala no lineal: sistemas grandes → mayor utilización + menor wait time que pequeños con mismo ratio volumen/capacidad (Green 2006, Kolker 2011)

## Dynamic Supply and Demand Balance Problems

### 2.1 Discrete Event Simulation Methodology
- [P021] **DEFINICIÓN** — DES = modelo computacional imitando comportamiento dinámico sistema → visualizar y analizar cuantitativamente rendimiento
- [P022] **DEFINICIÓN** — DES rastrea entidades moviéndose por sistema en puntos discretos tiempo (eventos), registrando tiempos procesamiento/espera
- [P023] **REGLA** — múltiples replicaciones DES necesarias capturar variabilidad sistema; cada replicación usa nuevos números aleatorios mismas distribuciones
- [P024] **HECHO** — promedio simple wait time engañoso para procesos altamente variables sin info dispersión
- [P025] **REGLA** — promedio ponderado por tiempo queue length = mejor métrica rendimiento que promedio aritmético; pondera duración cada paciente en cola
- [P026] **DEFINICIÓN** — bloques básicos DES: flow chart, entidades, actividades, recursos, ruteos entidades
- [P027] **HECHO** — DES sin restricción tipo distribución llegadas/servicio → modelar sistemas más complejos
- [P028] **ALCANCE** — aplicaciones DES: scheduling staff/producción, capacity planning, reducción cycle time, throughput, utilización, encontrar bottlenecks, what-if analysis

### 2.2 Queuing Analytic Theory
- [P029] **DEFINICIÓN** — QAT = técnicas analíticas como fórmulas matemáticas cerradas describiendo propiedades procesos con demanda/oferta aleatoria (colas)
- [P030] **RESTRICCIÓN** — fórmulas QAT tractables solo si flujo eventos = proceso Poisson steady-state con tasa llegada promedio constante
- [P031] **DEFINICIÓN** — modelo M/M/s: Markov con llegadas Poisson, tiempo servicio exponencial, cola ilimitada, s servidores
- [P032] **ALCANCE** — M/M/s calcula: probabilidad 0/K clientes, queue length promedio, wait time promedio, cycle time promedio, utilización servidor
- [P033] **RESTRICCIÓN** — fórmulas QAT intratables conforme complejidad sistema aumenta; no captura complejidad mayoría sistemas healthcare interés práctico
- [P034] **RESTRICCIÓN** — supuestos QAT inválidos muchos procesos healthcare: llegadas batch (accidentes), tasa dependiente llegadas previas, tasas variables temporalmente
- [P035] **REGLA** — test bondad ajuste requerido verificar distribución Poisson antes aplicar QAT; media debe = varianza para Poisson
- [P036] **RESTRICCIÓN** — Poisson usado supuesto teórico estándar operations research por conveniencia matemática pese aplicabilidad limitada patrones reales llegada pacientes
- [P037] **RESTRICCIÓN** — fórmulas QAT no aplicar si flujo contiene componente no aleatoria (llegadas programadas); componente no aleatoria debe eliminarse primero
- [P038] **REGLA** — QAT usable procesos steady-state simplemente estructurados si supuestos Poisson/exponencial se cumplen o coeficiente variación ≈ 1

### 2.3.1 Outpatient Clinic: Centralized or Separate Locations?
- [P039] **HECHO** — clínica gripe centralizada 4 enfermeras (28 pac/h, servicio 8 min): QAT → cola 11.9, wait 25.5 min, utilización 93%
- [P040] **HECHO** — dividir central 4 enfermeras → 2 clínicas × 2 enfermeras (14 pac/h): wait 25.5 → 54 min pese mismo ratio staff/paciente
- [P041] **REGLA** — recursos pooled con flujo aleatorio + cola ilimitada más eficientes que separados con misma carga total; separación ≈ duplica wait time
- [P042] **HECHO** — DES y QAT resultados prácticamente idénticos comparación centralizado/separado: DES cola 11.8, wait 25.3 min (vs QAT 11.9, 25.5)
- [P043] **REGLA** — recursos especializados (dedicados) requieren capacidad adicional planificada compensar pérdida eficiencia vs pooled

### 2.3.2 Outpatient Clinic: Nonsteady-State Operations
- [P044] **HECHO** — servicio promedio 8.0 → 8.6 min (solo +7.5%) empuja rho <1 a 1.003 → fórmulas QAT inaplicables
- [P045] **RESTRICCIÓN** — condición steady-state QAT: rho < 1; si rho ≥ 1 cola crece indefinidamente, no existe solución
- [P046] **HECHO** — DES maneja nonsteady-state y demuestra crecimiento indefinido cola; QAT no puede modelar nonsteady-state
- [P047] **REGLA** — sistemas colas healthcare no lineales: cambio pequeño input puede causar transición dramática steady → nonsteady — "consecuencias no intencionadas"

### 2.3.3 Limited Queue Size with Leaving Patients
- [P048] **HECHO** — cola limitada 15 sillas + pacientes abandonando 10-25 min (moda 15) convierte nonsteady → steady: wait ≈ 6 min, cola ≈ 3.2
- [P049] **⚠ TENSIÓN** — cola limitada + abandono mejora métricas espera solo porque ~10-11% pacientes perdidos; servir menos ≠ mejora real — pérdida revenue

### 2.3.4 Outpatient Clinic: Time-Varying Arrival Rates
- [P050] **HECHO** — enfoque SIPP (tasa promediada) + QAT da resultado engañoso; tasa entra no linealmente en exponencial Poisson; promediar antes sustituir = inválido
- [P051] **HECHO** — QAT SIPP sobreestima cola inicio día, subestima final; sin resultado para períodos rho > 1 (mediodía-3pm)
- [P052] **HECHO** — DES llegadas variables: cola/wait acumulan hacia final día; 3-6pm cola 4.9 vs 8-10am cola 0.15 — lag congestión tras pico
- [P053] **RESTRICCIÓN** — parche SIPP para QAT no confiable; pico congestión lag significativo vs pico llegada; Lag-SIPP más efectiva pero compleja

### 2.3.5 ICU Capacity and Access to Care
- [P054] **HECHO** — ICU 10 camas promedio 5 ocupadas: Poisson → >6 camas necesarias ~24% tiempo; recortar a 6 crea escasez regular
- [P055] **HECHO** — ICU 6 camas (QAT Poisson 2/día, LOS exponencial 2.5d): cola 2.9, wait ~35h, utilización 83%
- [P056] **HECHO** — DES mismos supuestos (Poisson + exponencial): cola 3.1, wait 28-34h (99% CI); 46% pacientes esperan >6h — confirma QAT
- [P057] **HECHO** — DES LOS acotado (triángulo 1-3d, misma media 2.5): cola baja a 1, wait 6-6.6h, 26% >6h — mucho mejor que exponencial ilimitada
- [P058] **REGLA** — variabilidad llegadas/LOS requiere capacidad reservada (a veces hasta 40%) evitar problemas operacionales regulares
- [P059] **REGLA** — QAT produce mismo resultado con mismos promedios independiente forma distribución; no distingue distribuciones diferentes misma media → `flaw of averages`
- [P060] **REGLA** — decisiones capacidad/staffing solo promedios sin distribuciones → miscálculos significativos

### 2.3.6 Mixed Patient Arrival Patterns
- [P061] **HECHO** — llegadas mixtas (8 programadas + 6 emergencia/día, 1h procedimiento, 1 sala): DES → cola 0.62, wait 1h
- [P062] **HECHO** — QAT llegadas mixtas (tratando todas aleatorias): cola 0.82, wait 1.4h — sobreestima +32% cola, +40% wait vs DES
- [P063] **REGLA** — mayor aleatoriedad llegada/servicio → menor rendimiento operacional; QAT sobreestima congestión cuando variabilidad real < Poisson

### 2.3.7 Small vs Large Hospital: Scale Effect
- [P064] **HECHO** — hospital grande 250 camas, 50 admisiones/día: wait 0.001-0.003h, 0.02-0.06% >2h, utilización 81%
- [P065] **HECHO** — hospital pequeño 25 camas, 5 admisiones/día (mismo ratio): wait 2.5-3.0h, 15.5-17.5% >2h, utilización 81%
- [P066] **REGLA** — hospitales grandes siempre mejor performance que pequeños mismo ratio input/capacidad; benchmarking lineal y ajustes proporcionales = inválidos → `scaling effect`
- [P067] **⚠ TENSIÓN** — hospital 25 camas: reducir LOS moda 4→3d elimina wait admisión pero utilización 81% → 53% — trade-off inevitable

### 2.3.8 Daily Load-Leveling of Elective Procedures
- [P068] **HECHO** — schedule electivo sin suavizar (3 ORs): wait emergencia 0.74h, electivo 1.2h
- [P069] **HECHO** — daily load-leveling (mismos totales, 3 ORs): wait emergencia 0.58h (-21%), electivo 0.82h (-32%)
- [P070] **REGLA** — load-leveling schedule electivo = estrategia poderosa reducir wait; Leapfrog Group (2011) incluyó en Patient Experience of Care
- [P071] **HECHO** — Kolker (2009): cap 5 electivos/día → reducir ICU diversion; confirmado Ryckman et al. (2009) Cincinnati Children's Hospital ≈ eliminación total
- [P072] **REGLA** — variabilidad carga quirúrgica programada = fuente "artificial" reducible estrés ICU; disponibilidad camas determinada más por variación demanda programada que no programada (McManus 2003)

### 2.3.9 Separate or Interchangeable ORs
- [P073] **HECHO** — Wullink et al. (2007) DES Erasmus Medical Center: ORs pooled redujeron wait emergencia 74 → 8 min vs dedicado → cierre OR emergencia dedicado
- [P074] **HECHO** — mayoría electivos (6/día): wait electivo dedicado 2.3-2.9h vs pooled 0.14-0.17h — >orden magnitud; dedicado utilización 99%, emergencia dedicado 35%
- [P075] **HECHO** — mayoría emergencias: wait emergencia dedicado 6.3-7.7h vs pooled 0.55-0.65h; pooled más cirugías emergencia (59-60 vs 53-54)
- [P076] **REGLA** — ORs pooled superan dedicados: (1) capacidad compartida buferea variabilidad vía overflow; (2) emergencias simultáneas posibles; (3) idle dedicado no absorbe overflow
- [P077] **⚠ TENSIÓN** — pooling puede no beneficiar si gran diferencia tiempo proceso entre tipos paciente o targets wait urgencia muy diferentes (Joustra 2010, radioterapia)
- [P078] **REGLA** — recomendación tradicional separar ORs scheduled/emergencia (Haraden 2003) contradicha por DES cuantitativo — pooled más eficiente ambos escenarios

### 2.3.10 Surgical Capacity Special Procedure ORs
- [P079] **HECHO** — fórmula tradicional (promedios): 4 camas recovery + 1 SPR suficiente 2,036 procedimientos/año; DES muestra subestimación seria
- [P080] **HECHO** — 4 camas + 1 SPR: 23% pacientes >1h wait SPR y 23% >5min wait recovery (ambos exceden 5% aceptable)
- [P081] **HECHO** — DES distribuciones reales (sesgadas): mínimo 6 camas + 2 SPR requeridos (~2% exceden límites)
- [P082] **REGLA** — cantidad correcta recursos healthcare variable solo predecible simulación; tiempos procedimiento/recovery distribuciones sesgadas colas largas excediendo promedios

### 2.3.11 Entire Hospital System Patient Flow
- [P083] **HECHO** — hospital comunitario grande típico: ED 25 camas, ICU 49, 12 ORs, 360 nursing; volumen mensual ~4,478 (ambulancia ~18%, walk-in ~82%)
- [P084] **REGLA** — patient flow = propiedad sistema hospital completo, no departamentos; interdependencia subsistemas debe modelarse → `system thinking`
- [P085] **HECHO** — reducción agresiva LOS ED (<6h): 4/9 métricas empeoran al mover bottleneck a OR/ICU; reducción moderada (<11h): 9/9 métricas ≥ baseline
- [P086] **REGLA** — balance patient flow: (1) admisiones entrando, (2) altas saliendo tras tiempo variable, (3) capacidad limitada; desequilibrio → overflow/bottleneck/subutilización
- [P087] **REGLA** — mejora subsistemas separados (optimización local) ≠ mejora sistema global; sistema óptimos locales puede ser muy ineficiente (Goldratt & Cox 2004) → `theory of constraints`
- [P088] **HECHO** — prioridad mejora: ICU (mayor % wait admisión >1h), luego OR, luego ED; reducción ED debe coordinarse capacidad downstream

### 2.4.1 Scheduling Order for Appointments
- [P089] **REGLA** — orden citas afecta wait time: menor variabilidad primero significativamente mejor que aleatorio o mayor variabilidad primero
- [P090] **HECHO** — menor variabilidad primero: wait 6-7.3 min, clínica 9.6-9.9h; mayor variabilidad primero: wait 17.7-21.6 min, clínica 11.9-12.8h
- [P091] **HECHO** — Monte Carlo IHI (25 días): menor variabilidad wait 6.3 min vs mayor 19.2 min — ratio ~3×; confirmado Klassen & Rohleder (1996), Cayirli et al. (2006)
- [P092] **REGLA** — principio scheduling fundamental (manufactura): orden variabilidad creciente → menor cycle time y wait global
- [P093] **HECHO** — overtime clínica = consecuencia variabilidad duración citas, no del promedio; enfoque tradicional subestima tiempo total

### 2.4.2 Centralized Discharge vs Individual Units
- [P094] **HECHO** — 4 enfermeras unidad (propias altas): ~74/semana; enfermera dedicada centralizada: ~60/semana — 19% menos
- [P095] **REGLA** — centralizar altas crea bottleneck: altas → serie eventos dependientes; delay una impacta todas subsiguientes
- [P096] **REGLA** — serie eventos dependientes: solo bottleneck define throughput sistema; capacidad extra días buenos se pierde, backlog días malos acumula (Goldratt & Cox 2004)
- [P097] **REGLA** — backlog solicitudes servicio puede existir estable incluso demanda promedio alta variabilidad < capacidad (Savin 2006)

### 2.4.3 Staffing Hospital Receiving Center
- [P098] **HECHO** — tradicional (10 min/paquete, 127,139/año): 11.1 FTE suficientes; DES: 11 FTE solo procesan 118,744 — crónicamente understaffed
- [P099] **HECHO** — DES: 12.5 FTE requeridos (12 full + 1 half) procesar todos 127,139 paquetes; utilización ~88%
- [P100] **REGLA** — staffing tradicional basado promedios siempre subestima recursos; cálculo correcto requiere distribución tiempos procesamiento reales
- [P101] **HECHO** — staffing 11 FTE: reducir procesamiento a 9 min rango 7-12 min permite procesar todo; estandarización reduce variabilidad

### 2.4.4 Staffing with Cross-trained Staff
- [P102] **HECHO** — fórmula tradicional (medias): 3.1 FTE case management (0.3 reservas + 1.4 admisión + 1.4 preregistro)
- [P103] **HECHO** — distribuciones altamente sesgadas: tiempos reales hasta 18, 38, 26 min (vs medias 4.1, 8.3, 4.5 min)
- [P104] **HECHO** — DES distribuciones reales + cross-training: 4.5 FTE requeridos vs tradicional 3.1 — 45% más staff
- [P105] **REGLA** — cross-trained staff aumenta productividad por soporte mutuo; fórmulas tradicionales no contabilizan sharing carga

### 2.4.5 Outpatient Clinic Costs and Staffing
- [P106] **HECHO** — tradicional: 2 FTE → 600 pac/sem, revenue $15,567; DES: 2 FTE → 474-476 (-21%), 121-123 (20%) se van sin atención
- [P107] **HECHO** — 2 FTE regular: revenue real $12,054; 2 FTE + 1h overtime: 513-515 pac, revenue $12,912
- [P108] **HECHO** — +0.6 FTE mañana (8am-1pm): 508 pac, revenue $12,620; mismo 0.6 FTE tarde (1-6pm): 557 pac, solo 38 se van, revenue $14,000
- [P109] **REGLA** — colocación FTE turno correcto > conteo total: mismo 0.6 FTE tarde vs mañana genera ~$1,400 más revenue/sem y ~50 más pacientes
- [P110] **HECHO** — 4 FTE: ~594 pac revenue $14,149; 4.6 FTE: ~599 pac revenue $13,933 — 0.6 extra no compensado por 5 pac más
- [P111] **REGLA** — revenue neto crece solo cuando ingreso pacientes adicionales compensa costo recurso; más allá punto óptimo, costo staff > revenue marginal

## Linear and Probabilistic Resource Optimization

### 3.1 Optimization of Patient Service Volumes
- [P112] **DEFINICIÓN** — LP estructura: (1) variables decisión, (2) función objetivo, (3) restricciones, (4) parámetros valores numéricos definidos
- [P113] **DEFINICIÓN** — función objetivo LP = meta cuantitativa con variables decisión y parámetros fijos en combinaciones lineales
- [P114] **DEFINICIÓN** — restricciones LP = desigualdades/ecuaciones lineales limitando alternativas/recursos
- [P115] **REGLA** — LP: maximizar/minimizar objetivo sujeto restricciones variando variables decisión; conjunto cumpliendo meta = solución
- [P116] **HECHO** — hospital 3 líneas servicio, 5 recursos: LOS, enfermería, radiología intervencionista, laboratorio, ORs
- [P117] **HECHO** — revenue neto/pac: línea 1 $560, línea 2 $790, línea 3 $1,100
- [P118] **RESTRICCIÓN** — límites recursos anuales: LOS 19,710 pac-días; enfermería 16,200h; radiología 3,000h; laboratorio 6,000h; ORs 1,040h
- [P119] **RESTRICCIÓN** — no-negatividad requerida: variables decisión (volúmenes) ≥ 0
- [P120] **RESTRICCIÓN** — restricción entera preferida para variables volumen pacientes; redondeo soluciones reales a veces aceptable
- [P121] **HECHO** — solución LP óptima: línea 1=520, línea 2=2,740, línea 3=0 pac; revenue máximo $2,455,800
- [P122] **HECHO** — línea 3 (mayor revenue/pac $1,100) eliminada completamente en óptimo porque viola restricciones recursos → `contraintuitivo`
- [P123] **HECHO** — restricciones binding: radiología (3,000h), laboratorio (6,000h), ORs (1,040h) — todas al límite
- [P124] **HECHO** — línea 3 a 100 pac: laboratorio excedido 350h, ORs excedido 400h
- [P125] **HECHO** — cirugía línea 3 reducida 4→1h + lab a 1.5h: óptimo cambia línea 1=261, 2=2,617, 3=518; revenue $2,783,390
- [P126] **REGLA** — LP permite evaluar muchos escenarios cambio parámetros, similar DES → `what-if analysis`
- [P127] **⚠ TENSIÓN** — LP determinístico usa promedios como ciertos; variables aleatorias pueden producir soluciones estructuralmente diferentes en LP estocástico
- [P128] **DEFINICIÓN** — LP estocástico (SLO): ≥1 datos representados variables aleatorias; incertidumbre afecta factibilidad y optimalidad
- [P129] **HECHO** — 2 enfoques LP estocástico: (1) modelado recurso; (2) restricciones probabilísticas limitando prob violación nivel preespecificado
- [P130] **HECHO** — LP ampliamente aplicado ingeniería/negocios/academia decades; menos usado gestión práctica healthcare
- [P131] **HECHO** — solución LP obtenible Microsoft Excel Solver con 'Assume Linear Model' + 'Assume Nonnegativity'

### 3.2 Optimization of Clinical Unit Staffing 24/7
- [P132] **DEFINICIÓN** — enfermera ICU full-time: 5 días/semana, 2 días libres consecutivos rotativos, turnos rotativos; 3 turnos 8h/día
- [P133] **HECHO** — tarifa: $50/h (base + overhead) lun-vie; +50% ($75/h) sáb-dom
- [P134] **HECHO** — 7 días × 3 turnos = 21 schedules enfermera posibles
- [P135] **HECHO** — ratio enfermera-paciente 1:2 todos turnos; demanda mínima staff = censo promedio turno × ratio
- [P136] **REGLA** — staffing tradicional reduce costo total pero no garantiza restricciones turno; resulta ajustes diarios + overtime eliminando ahorros
- [P137] **REGLA** — función objetivo LP staffing: minimizar costo semanal enfermería asignando staff correcto turno correcto
- [P138] **DEFINICIÓN** — variable binaria I(s,ds) = 1 si enfermeras schedule s asignadas día-turno ds, 0 si no
- [P139] **HECHO** — LP óptimo: pool = 36 enfermeras; costo semanal = $77,800
- [P140] **REGLA** — LP staffing acomoda ratios/tarifas variables por turno, part-time; puede maximizar satisfacción vía puntajes preferencia
- [P141] **⚠ TENSIÓN** — censo tratado fijo en LP staffing pero son variables aleatorias; problema estrictamente LP estocástico
- [P142] **HECHO** — variables decisión = Xs enfermeras por cada s=21 schedules; restricciones: cobertura real/turno ≥ demanda mínima

### 3.3 Resident Physician Restricted Work Hours
- [P143] **HECHO** — evidencia científica: fatiga horas largas + privación sueño → déficits rendimiento, accidentes, errores médicos (IOM 2009, Ulmer et al.)
- [P144] **HECHO** — horas largas y privación sueño típicas programas formación residentes US previo IOM 2009
- [P145] **RESTRICCIÓN** — IOM 2009: turnos residentes ≤12-16h máximo; ≥10h descanso entre turnos
- [P146] **RESTRICCIÓN** — IOM: ≥1 período 24h libre/semana sin promediar; + período 24h adicional → ≥48h continuas libres/mes ("golden weekend")
- [P147] **RESTRICCIÓN** — IOM: turno nocturno ≤4 noches consecutivas; ≥48h continuas libres tras 3-4 noches
- [P148] **RESTRICCIÓN** — ICU día: ≥4 residentes lun-vie, ≥3 sáb-dom
- [P149] **RESTRICCIÓN** — ICU noche: ≥3 residentes lun-vie, ≥2 sáb-dom
- [P150] **HECHO** — IOM requiere schedule mensual (4 sem) implementar golden weekend/mes + día libre/semana
- [P151] **HECHO** — turno día IOM genera 196 schedules posibles: 7 × 4 semanas × 7 patrones = 196
- [P152] **HECHO** — LP óptimo scheduling diurno: pool mínimo = 5 residentes cumpliendo todas restricciones IOM
- [P153] **HECHO** — scheduling nocturno: restricción IOM (≤4 noches + ≥48h libres) → patrón deslizante 6 semanas; solo 6 schedules
- [P154] **HECHO** — LP óptimo noche: rotación 4 noches trabajo + 2 días libres consecutivos, repitiendo cada 6 semanas
- [P155] **REGLA** — LP preferido sobre DES staffing cuando poca aleatoriedad y meta = staffing mínimo cobertura por seguridad/regulación, independiente workload
- [P156] **REGLA** — DES más apropiado que LP balance dinámico oferta/demanda con procesos aleatorios donde staffing depende volúmenes (workload)
- [P157] **REGLA** — scheduling tradicional residentes manual o software: manual impracticable; software cobertura pero no staffing mínimo optimizado

### 3.4 Optimized Pooled Screening Testing
- [P158] **HECHO** — CDC recomienda screening HIV todos pacientes 13-64 en todos settings healthcare: hospital EDs, urgent care, inpatient, STD/TB clinics, primary care
- [P159] **HECHO** — laboratorio capacidad 60 especímenes HIV/día; CDC nuevas recomendaciones → ~100/día, backlog + overtime
- [P160] **REGLA** — tradicional escasez capacidad: presupuestar staff/equipo adicional; restringido aprobación tight
- [P161] **DEFINICIÓN** — pooled testing: lote muestras combinado; lote negativo → todas negativas 1 test; lote positivo → retesteo individual
- [P162] **HECHO** — trade-off: reducción tests (lote negativo) vs retesteo (lote positivo); tamaño lote óptimo minimiza tests/espécimen
- [P163] **HECHO** — tests esperados/espécimen N = [1-(1-P)^n](n+1)/n + (1-P)^n; n=tamaño lote, P=prob positivo
- [P164] **RESTRICCIÓN** — reducción tests (N<1) solo si prevalencia P < ~30.6%
- [P165] **REGLA** — P 12.4-30.6%: lote óptimo = 3; P < 11.1%: lote ≈ 1/√P + 0.5 redondeado
- [P166] **HECHO** — CDC 2008: prevalencia HIV US fin 2006 P ≈ 0.447% (95% CI: 0.427-0.468%)
- [P167] **HECHO** — P=0.447%: lote óptimo 15; tests/espécimen ≈ 0.13 → reducción 87% — de 100 a ~13 diarios
- [P168] **HECHO** — grupo alto riesgo P=10%: lote óptimo 4; tests/espécimen ≈ 0.594 → ~59 diarios, dentro capacidad 60
- [P169] **RESTRICCIÓN** — dilución lote puede reducir especificidad/sensibilidad analítica; considerar en implementación
- [P170] **REGLA** — pooled testing mejorado sorting especímenes alto/bajo riesgo; ahorros adicionales con grupos alto riesgo identificables prevalencia mucho mayor
- [P171] **REGLA** — multistage testing: lotes positivos → lotes más pequeños retesteo; más eficiente prevalencia muy baja + pérdida sensibilidad mínima
- [P172] **ALCANCE** — pooled testing aplicable testing masivo cualquier fluido/espécimen, no limitado HIV

### 3.5 Projected Patients Discharged from ED
- [P173] **DEFINICIÓN** — ESI (Emergency Severity Index) clasifica pacientes ED; datos históricos LOS por ESI
- [P174] **HECHO** — predicción alta ED tradicional: evaluación médico/enfermera subjetiva; inexacta por dificultad integrar múltiples fuentes
- [P175] **REGLA** — LOS promedio insuficiente predecir altas; distribuciones LOS muy diferentes pueden compartir mismo promedio
- [P176] **DEFINICIÓN** — probabilidad condicional alta q(T,t): prob paciente no dado alta LOS=T será dado alta próximo período t
- [P177] **HECHO** — fórmula: q(T,t) = [F_ESI(T+t) - F_ESI(T)] / [1 - F_ESI(T)]; F_ESI = distribución acumulada LOS por ESI
- [P178] **HECHO** — Littig & Isken (2007): hazard ratio similar → prob condicional salida 24h dado LOS actual → predicción ocupación hospital
- [P179] **HECHO** — distribuciones acumuladas LOS por ESI aproximadas polinomios 3er orden → calculadora Excel
- [P180] **HECHO** — altas esperadas período t: N_ESI(T,t) = N_ESI(T) × q_ESI(T,t) redondeado
- [P181] **HECHO** — ejemplo lead time 2h: 44 pacientes ESI 1-4 → ~29 altas esperadas (ESI-1:7, ESI-2:8, ESI-3:9, ESI-4:5)
- [P182] **REGLA** — precisión predicciones depende calidad datos LOS; recolectar ≥1 año capturando variación estacional
- [P183] **ALCANCE** — anticipar altas ED → unidades inpatient downstream lead time agilizar camas, alta/transferencia pacientes existentes

## Forecasting Time Series

### 4.1 Forecasting Patient Volumes
- [P184] **HECHO** — forecasting volumen pacientes = paso crítico planificación capacidad, presupuesto, asignación recursos
- [P185] **HECHO** — método más simple: % crecimiento anual fijo (2-3%); asume crecimiento ilimitado sin insight tendencias
- [P186] **DEFINICIÓN** — métodos smoothing: regresión polinomial, Box-Jenkins, exponential smoothing, Holt-Winters, promedios móviles ponderados, ARIMA
- [P187] **REGLA** — smoothing: encontrar patrones series temporales → extrapolar patrón como forecast
- [P188] **REGLA** — antes forecast: identificar número datos pasados necesarios para predicciones
- [P189] **HECHO** — datos demasiado antiguos no afectan prácticamente datos recientes; recencia determina relevancia predictiva
- [P190] **DEFINICIÓN** — ACF (autocorrelation function) = interdependencia lineal datos separados k unidades tiempo (time lag)
- [P191] **REGLA** — datos fuertemente correlacionados (sobre umbral significancia) incluir; débilmente/no correlacionados excluir → evitar forecasts sesgados
- [P192] **⚠ TENSIÓN** — más datos reduce error pero riesgo overfitting; puntos recientes fuertemente correlacionados preferidos forecast más allá datos disponibles
- [P193] **REGLA** — ACF(k): 1 en k=0 → 0 para k grande; cutoff = máx k donde ACF(k) estadísticamente ≠ 0 (95% confianza)
- [P194] **HECHO** — volumen pacientes 1997-2009: ACF significativo k=1-4; solo 5 años recientes (2005-2009) correlación >0.8 usar
- [P195] **HECHO** — validación 2005-2008 → predecir 2009 (real=18,225): Growth curve 11.8%, Exponential 15.3%, S-curve 1.9%, Winters' 12.2%, Polynomial 11.9%, Moving avg 5%, ARIMA 7.2% error
- [P196] **HECHO** — ningún smoothing tradicional bueno prediciendo 1 año; improbable forecasts largo plazo confiables
- [P197] **HECHO** — polinomios producen tendencias descendentes espurias >2011; growth/Winters' sobrepredicen (35K/30.5K para 2015)
- [P198] **DEFINICIÓN** — recursive linear prediction: técnica señal digital; próximo dato = combinación lineal m valores previos con coeficientes d_j minimizando discrepancia
- [P199] **REGLA** — recursivo estable solo si raíces complejas polinomio característico |z| ≤ 1; coeficientes malos → output exponencial
- [P200] **HECHO** — forecast recursivo 2009: predicción 18,114 vs real 18,225 — error 0.6%, muy superior todos smoothing
- [P201] **HECHO** — recursivo predijo crecimiento moderado 2013, aplanamiento 2014, declive leve 2015 — más plausible que ilimitado/constante
- [P202] **REGLA** — ningún forecast perfectamente preciso; imposible predecir futuro desde pasado con certeza
- [P203] **REGLA** — recursivo confiable cuando factores subyacentes estables y datos recientes fuertemente correlacionados usados
- [P204] **HECHO** — forecast recursivo vastamente más poderoso que smoothing/extrapolación polinomial (Press et al. 1988)

### 4.2 Forecasting with Seasonal Variation
- [P205] **HECHO** — procesos fisiológicos varían estacionalmente (PA, FC, lípidos); eventos cardiovasculares, ACV, mortalidad fluctuación estacional
- [P206] **HECHO** — Tseng et al. (2005): variación estacional significativa A1C mensual veteranos diabéticos US; mayor invierno, menor verano
- [P207] **DEFINICIÓN** — descomposición estacional: (1) media móvil centrada, (2) valores estacionales brutos, (3) medianas/período, (4) índices promedio 1, (5) desestacionalizar, (6) tendencia lineal, reaplicar índices
- [P208] **HECHO** — Winters' calcula 3 componentes dinámicos (nivel, tendencia, estacional) vía Holt-Winters; estimaciones actualizan con valores vecinos
- [P209] **DEFINICIÓN** — ARIMA: filtra datos (autoregresivo → integrado → media móvil) hasta ruido aleatorio; flexible pero no automatizable y lento identificar/ajustar
- [P210] **HECHO** — descomposición, Winters', ARIMA: forecasts similares variación estacional; difícil identificar mejor
- [P211] **REGLA** — forecast recursivo no requiere descomposición tendencia/estacional; aplica directo datos originales
- [P212] **HECHO** — A1C 24 meses: ACF k=4-8 y k=15-16 no significativos; k=10-14 y k=17-21 significativos por patrón estacional; 22 meses necesarios
- [P213] **HECHO** — ACF A1C desestacionalizado significativa k=21; confirma usar 22 datos forecast 12 meses
- [P214] **HECHO** — recursivo A1C refleja estacionalidad máx Feb-Mar, mín Sep-Oct; amplitud menor que tradicionales porque directamente forecasteada

## Business Intelligence and Data Mining

### 5.1 Multivariate Database Analysis (PCA)
- [P215] **DEFINICIÓN** — BI = métodos cuantitativos extraer info/patrones bases datos grandes → decisiones gerenciales
- [P216] **DEFINICIÓN** — DM = análisis datasets observacionales → relaciones insospechadas, resúmenes novedosos (Hand et al. 2001)
- [P217] **DEFINICIÓN** — contribution margin (CM) = pagos cobrados paciente − costos variables paciente
- [P218] **HECHO** — dataset CM por zip code: 32 variables demográficas — 8 edad, 9 educación, 10 ingreso, 5 ocupación — 10 zip codes
- [P219] **HECHO** — categorías demográficas altamente correlacionadas: 'some HS'/ingreso <$15K r=0.899; master/$150-250K r=0.873 → info redundante
- [P220] **HECHO** — regresión 32 variables: R-sq(adj)=8.6%, coeficientes no significativos (p 0.1-0.97), VIF docenas-millones — fallo multicolinealidad
- [P221] **REGLA** — muchas variables correlacionadas → regresión tradicional falla extraer factores; PCA requerida
- [P222] **DEFINICIÓN** — PCA = identificar variables redundantes, retener pocos componentes principales no correlacionados (combinaciones lineales originales) con toda info; caso especial SVD
- [P223] **REGLA** — mayor correlación columnas → menos variables principales necesarias describir dataset
- [P224] **REGLA** — eigenvalues suman total variables originales p; grandes = alto contenido info; PCA reorganiza no destruye info
- [P225] **HECHO** — PCA 32 variables (Minitab 15): 9 PCs cubren 32 variables; primeros 5 PCs = 94% datos → alta redundancia
- [P226] **REGLA** — regresión con PCs: PCs menores (eigenvalue ≈ 0) NO eliminar — introduce sesgo; excepción pura reducción variables
- [P227] **REGLA** — PCs ortogonales → VIF=1 todos predictores; términos no significativos removibles sin afectar restantes → elimina multicolinealidad
- [P228] **HECHO** — best subset 7 PCs (PC1-4, PC6-8): R-sq=95.9%, R-sq(adj)=81.6%; solo PC6 significativo p=0.05
- [P229] **HECHO** — contribuyentes negativos PC6 a CM: edad 18-24/60-64; educación 'some HS'/'HS'; ingreso '$500K+'/'<$15K'; ocupación 'service'/'public service'
- [P230] **HECHO** — 'some HS' + <$15K correlacionados = misma población pobreza/baja educación asistencia gubernamental usando frecuentemente servicios hospital
- [P231] **REGLA** — aumentar CM: marketing zip codes mayores factores demográficos negativos PC6

### 5.2 Cluster Analysis
- [P232] **DEFINICIÓN** — cluster analysis = agrupar observaciones similitud intra-cluster >> similitud inter-cluster; cuando poca info estructura datos
- [P233] **HECHO** — ANOVA no válido datos población completa (no aleatorios); cluster analysis apropiado sin supuestos muestra aleatoria
- [P234] **REGLA** — PCA reduce variables (columnas); cluster analysis reduce observaciones (filas); ambos reducción volumen datos
- [P235] **DEFINICIÓN** — tres métodos DM: clasificación, clustering, asociación (Hand et al. 2001)
- [P236] **DEFINICIÓN** — hierarchical clustering (aglomerativo): observaciones separadas → unir par más cercano iterativamente; dendrogram; lento datasets grandes
- [P237] **DEFINICIÓN** — K-means (particional): k centroides aleatorios → reubicar objetos similitud iterativamente; más preciso/rápido que hierarchical; requiere k previo
- [P238] **DEFINICIÓN** — proximidad cluster: single linkage (nearest), complete (furthest), average, centroid; distancias: Euclidean, Mahalanobis, Manhattan, Minkowski
- [P239] **REGLA** — average linkage + centroid + Euclidean más usados: insensibilidad relativa outliers
- [P240] **HECHO** — K-means generalmente más preciso que hierarchical; hierarchical más lento, datasets menores
- [P241] **HECHO** — cluster 29 zip codes CM k=5 K-means: partición más intuitiva que hierarchical; 29 → 5 grupos
- [P242] **HECHO** — aplicaciones DM healthcare: fraude seguros, subdiagnóstico, marketing/costos, patrones frecuentes, relaciones enfermedades/fármacos (Yoo 2011)
- [P243] **RESTRICCIÓN** — cluster analysis siempre produce clusters incluso datos aleatorios; riesgo clusters espurios; métodos validación existen (Tibshirani 2001)

## The Use of Game Theory

### 6.1 Fair Distribution of Savings Between Cooperating Providers
- [P244] **HECHO** — hospitales: numerosos conflictos interés departamentos (ED↔ICU transferencia rápida vs capacidad; unidad prolonga stay vs otras quieren alta)
- [P245] **DEFINICIÓN** — payment bundling (reforma 2010): pago único organización cubriendo hospital + grupo médicos + SNF + HHA; organización asigna pagos y gain-sharing
- [P246] **HECHO** — bypass cardíaco bundled: Hospital $15K, Grupo Médicos $8K, SNF $6K, HHA $3K (total $32K); Medicare -13% → $4,160 ahorros distribuir
- [P247] **HECHO** — división igual $4,160/4 = $1,040 — injusta contribución difiere
- [P248] **HECHO** — proporcional costo: Hospital $1,950, PG $1,040, SNF $780, HHA $390 — desalienta participantes pequeños
- [P249] **DEFINICIÓN** — Shapley value = asignación justa ganancias/ahorros colectivos; miembro k compensado proporcional contribución marginal V(s)-V(s-k) promediada todos órdenes formación coalición
- [P250] **DEFINICIÓN** — coalición s = grupo cooperando; gran coalición S = todos; V(s) = valor coalición; Shapley promedia contribuciones marginales todos ordenamientos
- [P251] **REGLA** — incentivo permanecer coalición: (1) racionalidad individual — costo miembro < standalone; (2) racionalidad subgrupo — costo subgrupo < suma standalone; (3) distribución completa
- [P252] **DEFINICIÓN** — core = asignaciones satisfaciendo racionalidad individual + subgrupo; core no vacío → Shapley satisface; Shapley calculable core vacío
- [P253] **HECHO** — Shapley bypass 4 participantes: Hospital $1,598 (10.7%), PG $1,000 (12.5%), SNF $953 (15.9%), HHA $608 (20.3%); core no vacío
- [P254] **HECHO** — Shapley asigna mayor % ahorros participantes menor costo (SNF, HHA) vs proporcional → alienta cooperación
- [P255] **REGLA** — Shapley value = mejor enfoque asignación justa costos/ganancias sistemas economías escala no lineales o socios cooperativos
- [P256] **ALCANCE** — game theory aplica: bundled payment, ahorros recursos pooled, costos quirúrgicos con colas, centros diagnóstico/quirúrgicos conjuntos

## Summary of Fundamental Management Engineering Principles

### Core Principles
- [P257] **REGLA** — recursos pooled (intercambiables) más eficientes que dedicados misma capacidad/carga en wait time y throughput → `pooled resources`
- [P258] **REGLA** — recursos especializados requeridos (privacidad, infecciones, equipo fijo): planificar capacidad adicional compensar pérdida eficiencia
- [P259] **REGLA** — recursos especializados cuestan más que pooled intercambiables
- [P260] **REGLA** — variabilidad llegadas/servicio requiere capacidad reservada (hasta 40%) evitar problemas regulares
- [P261] **REGLA** — mayor aleatoriedad → menor rendimiento (cola mayor, wait mayor, utilización menor)
- [P262] **REGLA** — reducción variabilidad proceso = clave mejora patient flow, throughput, reducir delays
- [P263] **REGLA** — hospitales grandes siempre mejor performance que pequeños mismo ratio → `economies of scale`
- [P264] **REGLA** — benchmarking lineal/ajustes proporcionales misguided si efecto escala no considerado
- [P265] **⚠ TENSIÓN** — mayor utilización (bueno organización) → mayor wait (malo pacientes); utilización >80-85% → aumento significativo wait
- [P266] **REGLA** — workload leveling procedimientos electivos = estrategia efectiva reducir wait y mejorar flow
- [P267] **REGLA** — optimización local departamentos ≠ mejora sistema; sistema óptimos locales puede ser muy ineficiente → `theory of constraints`
- [P268] **REGLA** — análisis sistema complejo incompleto si interdependencias no consideradas
- [P269] **REGLA** — scheduling orden variabilidad creciente → menor cycle time y wait global
- [P270] **DEFINICIÓN** — bottleneck = recurso capacidad ≤ demanda; serie actividades dependientes: solo bottleneck define throughput
- [P271] **REGLA** — backlog puede existir estable incluso demanda promedio < capacidad con alta variabilidad
- [P272] **REGLA** — estimaciones capacidad/staffing/financieras basadas promedios sin variabilidad → sub/sobreestimación significativa → `flaw of averages`
- [P273] **REGLA** — prevalencia <30%: pooled specimen testing más eficiente que individual → `pooled testing`
- [P274] **REGLA** — forecasting: solo datos pasados recientes fuertemente correlacionados; excluir débilmente correlacionados → `ACF`
- [P275] **REGLA** — factores independientes de dataset correlacionado: descomponer en componentes no correlacionados vía PCA
- [P276] **REGLA** — PCA reduce variables; cluster analysis reduce observaciones; ambos reducción volumen datos

## Concluding Remarks and Definitions

### Concluding Remarks
- [P277] **DEFINICIÓN** — healthcare management engineering: decisiones gerenciales → asignación eficiente recursos para care alta calidad mediante métodos analíticos/simulación
- [P278] **HECHO** — traditional management carece medios contabilizar variabilidad, incertidumbre, escala, interconexiones → outcomes inexactos/efímeros
- [P279] **HECHO** — tendencia humana evitar incertidumbre ignorándola o convirtiendo certeza artificial → outcomes inexactos
- [P280] **HECHO** — management engineering revela interconexiones sistemas complejos, contabiliza economías escala, predice rendimiento real → decision-makers proactivos
- [P281] **ALCANCE** — 26 problemas: capacidad clínica/camas/OR, patient flow, staffing/scheduling, optimización recursos, forecasting, BI/DM, teoría juegos

### Appendix: Quantitative Methods
- [P282] **ALCANCE** — inventario métodos: data envelopment analysis, árboles decisión, DES, forecasting, teoría grafos, programación entera, just-in-time, LP, optimización no lineal, programación estocástica, Markov, inventario, Monte Carlo, ruta crítica, QAT, regresión PCA, control calidad, theory of constraints, system dynamics, game theory

### Definitions of Key Terms
- [P283] **DEFINICIÓN** — operations research = modelos matemáticos sistemas complejos variabilidad aleatoria → decisiones operacionales justificadas
- [P284] **DEFINICIÓN** — management science = metodología cuantitativa asignar recursos → metas operacionales sistema; basada operations research
- [P285] **DEFINICIÓN** — sistema complejo = interdependencia mutua componentes; cambio input → cambio no proporcional output
- [P286] **DEFINICIÓN** — DES = modelos computacionales sistemas reales rastreando eventos momentos discretos tiempo → analizar rendimiento
- [P287] **DEFINICIÓN** — QAT = métodos matemáticos colas sistemas simples sin interdependencia; fórmulas analíticas supuestos estrictos
- [P288] **DEFINICIÓN** — simulation package = software interfaz construir/procesar modelos DES; = simulation environment
- [P289] **DEFINICIÓN** — bottleneck/constraint = recurso capacidad ≤ demanda uso
- [P290] **DEFINICIÓN** — PCA = correlación multivariante; identifica variables redundantes; retiene componentes principales no correlacionados (combinaciones lineales originales)
