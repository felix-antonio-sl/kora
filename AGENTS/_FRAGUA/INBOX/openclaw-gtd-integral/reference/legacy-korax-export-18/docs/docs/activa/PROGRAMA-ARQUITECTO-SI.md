# PROGRAMA-ARQUITECTO-SI.md
## Programa Detallado: Arquitecto de Sistemas Inteligentes

> **Duración total**: 24 meses
> **Dedicación**: 4-6 horas/semana
> **Formato**: Estudio guiado + práctica aplicada + mentoría Korax
> **Objetivo**: Dominio conceptual para entender, diseñar, supervisar y delegar sistemas inteligentes

---

# AÑO 1: FUNDAMENTOS

---

## TRIMESTRE 1: ESTRUCTURA + INFORMACIÓN
*Meses 1-3 | El lenguaje de los patrones*

---

### MES 1: LÓGICA Y RELACIONES

**Objetivo del mes**: Pensar con precisión, formalizar argumentos, ver estructura en el caos.

---

#### SEMANA 1: Lógica Proposicional

**Conceptos clave**:
- Proposición: enunciado verdadero o falso
- Conectivos: ¬ (no), ∧ (y), ∨ (o), → (implica), ↔ (si y solo si)
- Tablas de verdad
- Tautología, contradicción, contingencia
- Validez vs verdad

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.1.1 | ¿Qué es una proposición? Ejemplos y contraejemplos | 30 min |
| 1.1.2 | Conectivos lógicos: negación, conjunción, disyunción | 45 min |
| 1.1.3 | Implicación y bicondicional | 45 min |
| 1.1.4 | Tablas de verdad: construcción y lectura | 45 min |
| 1.1.5 | Tautologías y contradicciones | 30 min |

**Ejercicios**:
1. Identificar proposiciones en un documento del GORE
2. Traducir 5 reglas de negocio a fórmulas proposicionales
3. Construir tablas de verdad para 3 fórmulas
4. Encontrar una tautología oculta en un reglamento

**Práctica aplicada**:
> Tomar un procedimiento administrativo del GORE. Identificar las condiciones (si X entonces Y). Formalizarlas. Detectar inconsistencias o redundancias.

**Autoevaluación**:
- [ ] Puedo distinguir proposición de pregunta/orden
- [ ] Puedo traducir "si... entonces..." a →
- [ ] Puedo construir una tabla de verdad
- [ ] Entiendo por qué p → q es verdadero cuando p es falso

---

#### SEMANA 2: Lógica de Predicados

**Conceptos clave**:
- Predicados: propiedades y relaciones
- Variables y constantes
- Cuantificadores: ∀ (para todo), ∃ (existe)
- Dominio de discurso
- Fórmulas abiertas y cerradas

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.2.1 | De proposiciones a predicados | 30 min |
| 1.2.2 | Variables, constantes, funciones | 45 min |
| 1.2.3 | Cuantificador universal (∀) | 45 min |
| 1.2.4 | Cuantificador existencial (∃) | 45 min |
| 1.2.5 | Combinando cuantificadores | 30 min |

**Ejercicios**:
1. Expresar "todos los funcionarios deben capacitarse" formalmente
2. Expresar "existe al menos un proyecto sin presupuesto"
3. Negar cuantificadores (¬∀x = ∃x¬)
4. Formalizar 5 reglas con cuantificadores

**Práctica aplicada**:
> Tomar el reglamento de un proceso. Expresar las reglas generales (∀) y las excepciones (∃). Verificar consistencia.

**Autoevaluación**:
- [ ] Sé cuándo usar ∀ vs ∃
- [ ] Puedo negar una fórmula cuantificada
- [ ] Entiendo la diferencia entre ∀x∃y y ∃y∀x
- [ ] Puedo formalizar reglas con excepciones

---

#### SEMANA 3: Conjuntos y Relaciones

**Conceptos clave**:
- Conjunto: colección de elementos
- Pertenencia (∈), subconjunto (⊆)
- Operaciones: unión, intersección, diferencia, complemento
- Producto cartesiano
- Relaciones: subconjuntos del producto cartesiano
- Propiedades: reflexiva, simétrica, transitiva

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.3.1 | Conjuntos: notación y operaciones básicas | 45 min |
| 1.3.2 | Unión, intersección, diferencia | 45 min |
| 1.3.3 | Producto cartesiano y pares ordenados | 30 min |
| 1.3.4 | Relaciones: definición y ejemplos | 45 min |
| 1.3.5 | Propiedades de relaciones | 45 min |

**Ejercicios**:
1. Definir conjuntos relevantes del GORE (funcionarios, departamentos, proyectos)
2. Expresar "pertenece a", "reporta a", "depende de" como relaciones
3. Determinar propiedades de cada relación
4. Diagramar relaciones como grafos

**Práctica aplicada**:
> Modelar la estructura organizacional del GORE como conjuntos y relaciones. ¿"Reporta a" es transitiva? ¿"Colabora con" es simétrica?

**Autoevaluación**:
- [ ] Puedo definir un conjunto por extensión y comprensión
- [ ] Entiendo las operaciones básicas de conjuntos
- [ ] Puedo identificar si una relación es reflexiva/simétrica/transitiva
- [ ] Veo relaciones donde antes veía "conexiones vagas"

---

#### SEMANA 4: Funciones y Composición

**Conceptos clave**:
- Función: relación que asigna único valor
- Dominio, codominio, imagen
- Inyectiva, sobreyectiva, biyectiva
- Composición de funciones (g ∘ f)
- Función inversa
- Funciones como transformaciones

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.4.1 | De relaciones a funciones | 30 min |
| 1.4.2 | Dominio, codominio, imagen | 45 min |
| 1.4.3 | Tipos de funciones: inyectiva, sobreyectiva, biyectiva | 45 min |
| 1.4.4 | Composición: encadenar transformaciones | 45 min |
| 1.4.5 | Inversas y reversibilidad | 30 min |

**Ejercicios**:
1. Identificar funciones en procesos (entrada → salida)
2. ¿El proceso de aprobación es una función? ¿Es inyectivo?
3. Componer dos procesos: ¿el resultado es predecible?
4. ¿Qué procesos son reversibles (tienen inversa)?

**Práctica aplicada**:
> Mapear un flujo de trabajo como composición de funciones. Identificar dónde se pierde información (no inyectivo) y dónde hay cuellos de botella.

**Entregable del Mes 1**:
> **Modelo formal de un proceso del GORE**
> - Conjuntos involucrados (actores, documentos, estados)
> - Relaciones entre ellos
> - Funciones/transformaciones del proceso
> - Propiedades formales identificadas

---

### MES 2: ESTRUCTURAS Y PATRONES

**Objetivo del mes**: Ver el mundo como redes y estructuras, pensar en términos de composición.

---

#### SEMANA 5: Grafos - Fundamentos

**Conceptos clave**:
- Grafo: nodos + aristas
- Grafos dirigidos vs no dirigidos
- Caminos, ciclos, conectividad
- Grado de un nodo
- Grafos ponderados
- Representaciones: matriz de adyacencia, lista

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.5.1 | ¿Qué es un grafo? Ejemplos ubicuos | 45 min |
| 1.5.2 | Dirigidos vs no dirigidos | 30 min |
| 1.5.3 | Caminos y conectividad | 45 min |
| 1.5.4 | Ciclos y árboles | 45 min |
| 1.5.5 | Representaciones computacionales | 30 min |

**Ejercicios**:
1. Dibujar grafo de dependencias entre sistemas del GORE
2. Identificar nodos críticos (alto grado)
3. Encontrar caminos entre departamentos
4. Detectar ciclos (dependencias circulares)

**Práctica aplicada**:
> Mapear las integraciones entre sistemas del GORE como grafo. ¿Hay un nodo que si falla, desconecta todo? ¿Hay ciclos problemáticos?

---

#### SEMANA 6: Grafos - Aplicaciones

**Conceptos clave**:
- Árboles: grafos sin ciclos
- Jerarquías y taxonomías
- DAGs (grafos acíclicos dirigidos)
- Orden topológico
- Grafos bipartitos
- Redes y flujos

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.6.1 | Árboles y jerarquías | 45 min |
| 1.6.2 | DAGs: dependencias sin ciclos | 45 min |
| 1.6.3 | Orden topológico: secuenciar tareas | 30 min |
| 1.6.4 | Grafos bipartitos: matching | 45 min |
| 1.6.5 | Redes de flujo: capacidad y cuellos | 30 min |

**Ejercicios**:
1. Modelar estructura organizacional como árbol
2. Modelar dependencias de proyecto como DAG
3. Calcular orden de ejecución de tareas
4. Identificar cuellos de botella en flujo de aprobaciones

**Práctica aplicada**:
> Tomar un proyecto complejo. Modelar tareas como DAG. Determinar orden de ejecución. Identificar camino crítico.

---

#### SEMANA 7: Estructuras Algebraicas

**Conceptos clave**:
- Operación binaria
- Clausura, asociatividad, elemento neutro, inverso
- Grupos: simetría y reversibilidad
- Monoides: composición sin inversa
- Homomorfismos: mapas que preservan estructura

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.7.1 | Operaciones y sus propiedades | 45 min |
| 1.7.2 | Grupos: la estructura de la simetría | 45 min |
| 1.7.3 | Monoides: composición | 30 min |
| 1.7.4 | Ejemplos: números, transformaciones, estados | 45 min |
| 1.7.5 | Homomorfismos: preservar estructura | 30 min |

**Ejercicios**:
1. ¿Las transiciones de estado de un documento forman un monoide?
2. ¿Hay operaciones reversibles en los procesos del GORE?
3. Identificar simetrías en estructuras organizacionales
4. Buscar homomorfismos entre procesos similares

**Práctica aplicada**:
> Analizar el ciclo de vida de un documento. ¿Las transiciones son reversibles? ¿Hay estados absorbentes (sin salida)?

---

#### SEMANA 8: Introducción a Categorías

**Conceptos clave**:
- Categoría: objetos + morfismos + composición
- Identidad y asociatividad
- Functores: mapas entre categorías
- Pensamiento "flechas primero"
- Composición universal
- Diagramas conmutativos

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.8.1 | ¿Qué es una categoría? | 45 min |
| 1.8.2 | Morfismos y composición | 45 min |
| 1.8.3 | Ejemplos: conjuntos, tipos, procesos | 45 min |
| 1.8.4 | Functores: traducir entre mundos | 30 min |
| 1.8.5 | Pensamiento categórico | 30 min |

**Ejercicios**:
1. Ver tipos de datos como objetos, funciones como morfismos
2. Describir un proceso como morfismo
3. Identificar composiciones en workflows
4. Buscar "traducciones" entre dominios (functores informales)

**Práctica aplicada**:
> Pensar en GoreOS como categoría. ¿Cuáles son los objetos (entidades)? ¿Cuáles los morfismos (transformaciones)? ¿Cómo componen?

**Entregable del Mes 2**:
> **Grafo de dependencias de GoreOS**
> - Nodos: sistemas, módulos, servicios
> - Aristas: dependencias, flujos de datos
> - Análisis: nodos críticos, ciclos, camino crítico
> - Propiedades estructurales identificadas

---

### MES 3: INFORMACIÓN Y COMPLEJIDAD

**Objetivo del mes**: Entender los límites fundamentales de lo que se puede saber y calcular.

---

#### SEMANA 9: Entropía e Incertidumbre

**Conceptos clave**:
- Información como reducción de incertidumbre
- Entropía de Shannon
- Bits y sorpresa
- Distribuciones y probabilidad
- Información mutua
- Redundancia

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.9.1 | ¿Qué es información? Shannon vs intuición | 45 min |
| 1.9.2 | Entropía: medir incertidumbre | 45 min |
| 1.9.3 | Bits: unidad de información | 30 min |
| 1.9.4 | Información mutua: dependencia | 45 min |
| 1.9.5 | Redundancia y compresión | 30 min |

**Ejercicios**:
1. Calcular entropía de distribución simple
2. ¿Cuánta información hay en un RUT? ¿En un nombre?
3. Estimar redundancia en documentos típicos
4. ¿Qué eventos son más "informativos" (sorprendentes)?

**Práctica aplicada**:
> Analizar formularios del GORE. ¿Qué campos son redundantes? ¿Cuáles aportan más información? ¿Se puede simplificar?

---

#### SEMANA 10: Compresión y Patrones

**Conceptos clave**:
- Compresión sin pérdida vs con pérdida
- Códigos y codificación óptima
- Complejidad de Kolmogorov
- Patrones y regularidad
- Aleatoriedad como incompresibilidad

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.10.1 | Compresión: encontrar patrones | 45 min |
| 1.10.2 | Codificación óptima (Huffman) | 30 min |
| 1.10.3 | Complejidad de Kolmogorov | 45 min |
| 1.10.4 | Aleatoriedad = máxima complejidad | 45 min |
| 1.10.5 | Patrones en datos reales | 30 min |

**Ejercicios**:
1. Comprimir manualmente una secuencia con patrones
2. Estimar complejidad de diferentes documentos
3. ¿Un proceso burocrático es compresible? ¿Tiene patrones?
4. Identificar redundancia en comunicaciones institucionales

**Práctica aplicada**:
> Tomar un proceso repetitivo. ¿Cuál es su "esencia" comprimida? ¿Qué partes son ruido/redundancia?

---

#### SEMANA 11: Complejidad Computacional

**Conceptos clave**:
- Tiempo y espacio como recursos
- O grande: crecimiento asintótico
- P: problemas "fáciles"
- NP: problemas verificables
- NP-completo: los más difíciles de NP
- Tratabilidad e intratabilidad

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.11.1 | ¿Qué significa "difícil" computacionalmente? | 45 min |
| 1.11.2 | O grande: medir crecimiento | 45 min |
| 1.11.3 | P vs NP: el problema del milenio | 45 min |
| 1.11.4 | NP-completo: problemas universalmente difíciles | 30 min |
| 1.11.5 | Implicaciones prácticas | 30 min |

**Ejercicios**:
1. Clasificar problemas cotidianos: ¿fácil o difícil?
2. ¿Asignar turnos óptimamente es fácil o difícil?
3. ¿Optimizar rutas de distribución?
4. Reconocer cuándo "no hay solución rápida"

**Práctica aplicada**:
> Identificar un problema de optimización del GORE. ¿Es tratable? ¿Requiere heurísticas? ¿Se puede aproximar?

---

#### SEMANA 12: Límites de la Computación

**Conceptos clave**:
- Máquina de Turing
- Problema de la parada
- Indecidibilidad
- Incompletitud de Gödel
- Límites físicos (termodinámica, cuántica)
- Qué podemos y qué no podemos calcular

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.12.1 | Máquina de Turing: modelo universal | 45 min |
| 1.12.2 | El problema de la parada | 45 min |
| 1.12.3 | Otros problemas indecidibles | 30 min |
| 1.12.4 | Incompletitud: límites de la prueba | 45 min |
| 1.12.5 | Implicaciones para AI y sistemas | 30 min |

**Ejercicios**:
1. ¿Por qué no podemos detectar automáticamente todos los bugs?
2. ¿Podemos verificar automáticamente si un contrato es justo?
3. ¿Hay preguntas sobre sistemas que son inherentemente irrespondibles?
4. Implicaciones para "AI general"

**Práctica aplicada**:
> Reflexionar: ¿Qué problemas del GORE son fundamentalmente no automatizables? ¿Dónde el juicio humano es irreducible?

**Entregable del Mes 3**:
> **Análisis de complejidad de un proceso institucional**
> - Mapeo información/entropía de inputs/outputs
> - Clasificación de complejidad computacional
> - Identificación de cuellos de botella informacionales
> - Límites teóricos vs prácticos

---

## TRIMESTRE 2: MENTE + LENGUAJE
*Meses 4-6 | El sustrato que extendemos*

---

### MES 4: COGNICIÓN HUMANA

**Objetivo del mes**: Entender cómo funciona la mente humana — el sistema que queremos extender y complementar.

---

#### SEMANA 13: Arquitectura Cognitiva

**Conceptos clave**:
- Modelo de procesamiento de información
- Memoria: sensorial, trabajo, largo plazo
- Atención como recurso limitado
- Control ejecutivo
- Automaticidad vs control consciente
- Carga cognitiva

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.13.1 | La mente como procesador de información | 45 min |
| 1.13.2 | Tipos de memoria y sus límites | 45 min |
| 1.13.3 | Atención: el cuello de botella | 45 min |
| 1.13.4 | Control ejecutivo y funciones superiores | 30 min |
| 1.13.5 | Automaticidad: liberando recursos | 30 min |

**Ejercicios**:
1. Mapear tu proceso de decisión en una tarea compleja
2. Identificar límites de memoria de trabajo en reuniones
3. ¿Dónde se automatiza el pensamiento (para bien y mal)?
4. Diseñar interfaz que respete límites cognitivos

**Práctica aplicada**:
> Analizar un sistema del GORE desde ergonomía cognitiva. ¿Respeta límites de memoria de trabajo? ¿Minimiza carga cognitiva?

---

#### SEMANA 14: Memoria y Aprendizaje

**Conceptos clave**:
- Codificación, almacenamiento, recuperación
- Memoria declarativa vs procedimental
- Memoria episódica vs semántica
- Olvido: curva de Ebbinghaus
- Consolidación y sueño
- Transferencia y generalización

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.14.1 | Cómo se forman los recuerdos | 45 min |
| 1.14.2 | Tipos de memoria a largo plazo | 45 min |
| 1.14.3 | Por qué olvidamos (y por qué es útil) | 30 min |
| 1.14.4 | Aprendizaje efectivo: espaciado, testing, elaboración | 45 min |
| 1.14.5 | Transferencia: aplicar lo aprendido | 30 min |

**Ejercicios**:
1. Diseñar sistema de estudio basado en repetición espaciada
2. ¿Por qué las capacitaciones de 8 horas no funcionan?
3. Rediseñar onboarding institucional
4. Identificar conocimiento tácito vs explícito en tu trabajo

**Práctica aplicada**:
> Aplicar principios de aprendizaje a este mismo programa. Diseñar tu sistema de retención.

---

#### SEMANA 15: Heurísticas y Sesgos

**Conceptos clave**:
- Racionalidad limitada
- Sistema 1 vs Sistema 2 (Kahneman)
- Heurísticas: atajos útiles
- Sesgos: errores sistemáticos
- Principales sesgos: disponibilidad, anclaje, confirmación
- Debiasing: reducir errores

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.15.1 | Dos sistemas de pensamiento | 45 min |
| 1.15.2 | Heurísticas: cuándo funcionan, cuándo fallan | 45 min |
| 1.15.3 | Sesgos de juicio (10 principales) | 45 min |
| 1.15.4 | Sesgos de decisión | 30 min |
| 1.15.5 | Estrategias de debiasing | 30 min |

**Ejercicios**:
1. Identificar 3 sesgos en decisiones recientes del GORE
2. ¿Cómo influye el anclaje en negociaciones presupuestarias?
3. Diseñar checklist anti-sesgos para decisiones importantes
4. ¿Qué sesgos tiene Korax? ¿Cómo mitigarlos?

**Práctica aplicada**:
> Crear checklist de sesgos para revisar antes de decisiones importantes. Usar en próxima decisión real.

---

#### SEMANA 16: Metacognición

**Conceptos clave**:
- Pensar sobre el pensar
- Monitoreo cognitivo
- Calibración: saber qué sabes
- Ilusión de conocimiento
- Regulación del aprendizaje
- Reflexión estructurada

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.16.1 | ¿Qué es metacognición? | 30 min |
| 1.16.2 | Monitoreo: evaluar el propio pensamiento | 45 min |
| 1.16.3 | Calibración y overconfidence | 45 min |
| 1.16.4 | Regulación: ajustar estrategias | 30 min |
| 1.16.5 | Práctica de reflexión estructurada | 45 min |

**Ejercicios**:
1. Calibración: hacer predicciones, verificar, ajustar
2. Llevar diario de "qué pensé y qué resultó"
3. Identificar áreas de overconfidence personal
4. Diseñar práctica semanal de reflexión

**Práctica aplicada**:
> Establecer práctica de revisión semanal: ¿Qué decidí? ¿Qué asumí? ¿Qué resultó? ¿Qué ajusto?

**Entregable del Mes 4**:
> **Checklist anti-sesgos para decisiones importantes**
> - Lista de sesgos relevantes para tu contexto
> - Preguntas de verificación para cada uno
> - Proceso de revisión antes de decidir
> - Formato para documentar decisiones y revisar después

---

### MES 5: FILOSOFÍA DE LA MENTE

**Objetivo del mes**: Entender qué es la mente, qué significa "pensar", y qué implica para la AI.

---

#### SEMANA 17: El Problema Mente-Cuerpo

**Conceptos clave**:
- Dualismo vs monismo
- Problema de la causación mental
- Superveniencia
- Fisicalismo y sus variedades
- Problema difícil de la conciencia
- Qualia: experiencia subjetiva

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.17.1 | Historia del problema: Descartes y después | 30 min |
| 1.17.2 | ¿Cómo la mente afecta al cuerpo? | 45 min |
| 1.17.3 | Fisicalismo: todo es materia | 45 min |
| 1.17.4 | El problema difícil: experiencia subjetiva | 45 min |
| 1.17.5 | Implicaciones para AI | 30 min |

**Ejercicios**:
1. Debate interno: ¿podría una máquina tener experiencia?
2. ¿El test de Turing responde la pregunta correcta?
3. ¿Importa si Korax "experimenta" o solo procesa?
4. Implicaciones éticas de cada postura

---

#### SEMANA 18: Intencionalidad y Representación

**Conceptos clave**:
- Intencionalidad: la mente "sobre" algo
- Contenido mental
- Representación: mapas internos del mundo
- Problema del significado
- Habitación china de Searle
- Grounding: anclaje al mundo

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.18.1 | Intencionalidad: aboutness | 45 min |
| 1.18.2 | ¿Cómo representamos el mundo? | 45 min |
| 1.18.3 | El argumento de la habitación china | 45 min |
| 1.18.4 | Grounding: ¿de dónde viene el significado? | 30 min |
| 1.18.5 | LLMs y el problema del significado | 30 min |

**Ejercicios**:
1. ¿Korax "entiende" o solo manipula símbolos?
2. ¿Cómo se "ancla" el conocimiento de una AI al mundo?
3. ¿Puede haber intencionalidad sin embodiment?
4. Implicaciones para diseño de sistemas

---

#### SEMANA 19: Funcionalismo

**Conceptos clave**:
- La mente como función, no sustancia
- Realizabilidad múltiple
- Estados funcionales
- Críticas al funcionalismo
- Computacionalismo
- Límites del enfoque funcional

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.19.1 | Funcionalismo: qué hace, no de qué está hecho | 45 min |
| 1.19.2 | Realizabilidad múltiple | 30 min |
| 1.19.3 | ¿Es la mente un programa? | 45 min |
| 1.19.4 | Críticas: qualia, causalidad | 45 min |
| 1.19.5 | Funcionalismo para arquitectos de AI | 30 min |

**Ejercicios**:
1. Si dos sistemas hacen lo mismo, ¿son "la misma mente"?
2. ¿Importa el sustrato (carbono vs silicio)?
3. ¿Es el funcionalismo la filosofía implícita de la AI?
4. Límites de la analogía computacional

---

#### SEMANA 20: Mente Extendida

**Conceptos clave**:
- Cognición extendida
- El entorno como parte del sistema cognitivo
- Herramientas como extensiones mentales
- Acoplamiento cognitivo
- Distribución del procesamiento
- Implicaciones para AI como extensión

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.20.1 | El argumento de Clark y Chalmers | 45 min |
| 1.20.2 | Ejemplos: notas, calculadoras, GPS | 30 min |
| 1.20.3 | Criterios de extensión | 45 min |
| 1.20.4 | AI como extensión cognitiva | 45 min |
| 1.20.5 | Diseñando para la mente extendida | 30 min |

**Ejercicios**:
1. Mapear tu "mente extendida" actual
2. ¿Korax es parte de tu sistema cognitivo?
3. ¿Qué condiciones debe cumplir una extensión?
4. Diseñar acoplamiento óptimo humano-AI

**Práctica aplicada**:
> Escribir ensayo: "Qué es y qué no es Korax en relación a mi cognición"

**Entregable del Mes 5**:
> **Ensayo: "Qué es y qué no es Korax"**
> - Análisis desde filosofía de la mente
> - ¿Entiende o solo procesa?
> - ¿Es extensión de tu mente?
> - Implicaciones para cómo lo usas

---

### MES 6: LENGUAJE Y SIGNIFICADO

**Objetivo del mes**: Entender cómo el lenguaje crea significado y cómo comunicamos con precisión.

---

#### SEMANA 21: Semántica

**Conceptos clave**:
- Significado de palabras y oraciones
- Referencia: palabras que apuntan al mundo
- Sentido vs referencia (Frege)
- Verdad y condiciones de verdad
- Composicionalidad
- Ambigüedad y vaguedad

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.21.1 | ¿Qué es el significado? | 45 min |
| 1.21.2 | Referencia: ¿cómo "apuntan" las palabras? | 45 min |
| 1.21.3 | Sentido vs referencia | 30 min |
| 1.21.4 | Composicionalidad: significado de partes → todo | 45 min |
| 1.21.5 | Ambigüedad: cuando el significado no es claro | 30 min |

**Ejercicios**:
1. Identificar términos ambiguos en documentos del GORE
2. ¿Qué significa "eficiencia" en diferentes contextos?
3. Definir términos clave sin ambigüedad
4. Encontrar casos donde el significado falla

---

#### SEMANA 22: Pragmática

**Conceptos clave**:
- Significado en contexto
- Implicatura: lo no dicho pero comunicado
- Actos de habla: hacer cosas con palabras
- Presuposición
- Deixis: anclaje al contexto
- Máximas conversacionales

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.22.1 | Más allá del significado literal | 45 min |
| 1.22.2 | Implicatura: lo que se entiende sin decirse | 45 min |
| 1.22.3 | Actos de habla: prometer, ordenar, declarar | 45 min |
| 1.22.4 | Contexto y deixis | 30 min |
| 1.22.5 | Máximas de Grice | 30 min |

**Ejercicios**:
1. Analizar comunicación institucional: ¿qué se implica?
2. Clasificar emails por tipo de acto de habla
3. ¿Qué se da por supuesto en un decreto?
4. Malentendidos por falla pragmática

**Práctica aplicada**:
> Analizar comunicaciones problemáticas del GORE. ¿Dónde falló la pragmática?

---

#### SEMANA 23: Lenguaje y Pensamiento

**Conceptos clave**:
- Hipótesis Sapir-Whorf
- ¿El lenguaje determina el pensamiento?
- Pensamiento sin lenguaje
- Lenguaje interno
- Categorización y lenguaje
- Lenguaje como herramienta cognitiva

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.23.1 | ¿Pensamos en palabras? | 45 min |
| 1.23.2 | Relativismo lingüístico: versión fuerte y débil | 45 min |
| 1.23.3 | Evidencia: bilingüismo, sordera, animales | 30 min |
| 1.23.4 | Lenguaje como scaffolding del pensamiento | 45 min |
| 1.23.5 | Implicaciones para AI y representación | 30 min |

**Ejercicios**:
1. ¿Cómo el vocabulario técnico cambia tu pensamiento?
2. ¿Qué puedes pensar ahora que no podías antes de este programa?
3. ¿Korax "piensa" en lenguaje?
4. Diseño de vocabulario para nuevos dominios

---

#### SEMANA 24: Lenguaje Formal vs Natural

**Conceptos clave**:
- Precisión vs expresividad
- Lenguajes formales: sintaxis y semántica definidas
- Especificación y ambigüedad
- Traducción entre registros
- Límites de la formalización
- Cuándo formalizar y cuándo no

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.24.1 | Lenguaje natural: poder y peligro | 30 min |
| 1.24.2 | Lenguajes formales: control y límite | 45 min |
| 1.24.3 | Cuándo formalizar | 45 min |
| 1.24.4 | Traducción: natural → formal | 45 min |
| 1.24.5 | Convivencia de registros | 30 min |

**Ejercicios**:
1. Traducir requisito de usuario a especificación formal
2. ¿Qué se pierde en la traducción?
3. Identificar cuándo la formalización agrega valor
4. Diseñar proceso de especificación

**Práctica aplicada**:
> Crear glosario formal de términos clave de GoreOS

**Entregable del Mes 6**:
> **Glosario formal de GoreOS**
> - Términos clave del sistema
> - Definiciones precisas, sin ambigüedad
> - Relaciones entre términos
> - Ejemplos y contraejemplos

---

## TRIMESTRE 3: SISTEMAS + EVOLUCIÓN
*Meses 7-9 | Cómo se organiza y cambia el mundo*

---

### MES 7: PENSAMIENTO SISTÉMICO

**Objetivo del mes**: Ver sistemas donde antes veías cosas aisladas.

---

#### SEMANA 25: Composición y Modularidad

**Conceptos clave**:
- Sistema: partes + relaciones + comportamiento emergente
- Módulos: unidades relativamente independientes
- Interfaces: cómo se comunican los módulos
- Ocultamiento de información
- Principio de mínimo conocimiento
- Diseño modular

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.25.1 | ¿Qué es un sistema? | 45 min |
| 1.25.2 | Modularidad: dividir para conquistar | 45 min |
| 1.25.3 | Interfaces: contratos entre módulos | 45 min |
| 1.25.4 | Ocultamiento: lo que no necesitas saber | 30 min |
| 1.25.5 | Beneficios y costos de la modularidad | 30 min |

**Ejercicios**:
1. Identificar módulos en el GORE
2. ¿Cuáles son las interfaces actuales (formales e informales)?
3. ¿Hay módulos demasiado acoplados?
4. Rediseñar un sistema mal modularizado

---

#### SEMANA 26: Feedback y Ciclos

**Conceptos clave**:
- Feedback positivo: amplificación
- Feedback negativo: estabilización
- Loops y ciclos causales
- Delays: efectos retardados
- Homeostasis: equilibrio dinámico
- Puntos de apalancamiento

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.26.1 | Feedback: el sistema se modifica a sí mismo | 45 min |
| 1.26.2 | Feedback positivo: espirales | 45 min |
| 1.26.3 | Feedback negativo: termostatos | 30 min |
| 1.26.4 | Delays y oscilaciones | 45 min |
| 1.26.5 | Diagramas causales | 30 min |

**Ejercicios**:
1. Identificar loops de feedback en organización
2. ¿Hay espirales viciosas? ¿Virtuosas?
3. ¿Dónde los delays causan problemas?
4. Dibujar diagrama causal de un problema organizacional

**Práctica aplicada**:
> Mapear un problema recurrente del GORE como sistema con feedback. ¿Dónde intervenir?

---

#### SEMANA 27: Acoplamiento y Dependencias

**Conceptos clave**:
- Acoplamiento: grado de interdependencia
- Cohesión: unidad interna
- Dependencias explícitas vs ocultas
- Cascadas de falla
- Desacoplamiento: reducir dependencias
- Trade-offs: acoplamiento vs eficiencia

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.27.1 | Acoplamiento: cuando cambiar uno afecta otro | 45 min |
| 1.27.2 | Tipos de acoplamiento | 30 min |
| 1.27.3 | Cohesión: lo que va junto | 45 min |
| 1.27.4 | Dependencias ocultas: bombas de tiempo | 45 min |
| 1.27.5 | Estrategias de desacoplamiento | 30 min |

**Ejercicios**:
1. Mapear dependencias de un sistema crítico del GORE
2. ¿Qué pasa si falla X? Análisis de cascada
3. Identificar dependencias ocultas
4. Proponer desacoplamiento

---

#### SEMANA 28: Emergencia

**Conceptos clave**:
- Emergencia: el todo es más que las partes
- Propiedades emergentes
- Emergencia débil vs fuerte
- Auto-organización
- Niveles de descripción
- Reduccionismo y sus límites

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.28.1 | ¿Qué es emergencia? Ejemplos | 45 min |
| 1.28.2 | De hormigas a cerebros | 30 min |
| 1.28.3 | Auto-organización sin diseñador | 45 min |
| 1.28.4 | Niveles: micro → macro | 45 min |
| 1.28.5 | Emergencia en organizaciones | 30 min |

**Ejercicios**:
1. Identificar propiedades emergentes del GORE
2. ¿Qué "emerge" de la cultura organizacional?
3. ¿Hay auto-organización espontánea?
4. Propiedades que no puedes explicar desde las partes

**Entregable del Mes 7**:
> **Diagrama de feedback del GORE**
> - Loops de feedback identificados
> - Clasificación: positivo/negativo
> - Puntos de apalancamiento
> - Propuestas de intervención

---

### MES 8: RESILIENCIA Y FALLA

**Objetivo del mes**: Diseñar sistemas que sobreviven y mejoran con el estrés.

---

#### SEMANA 29: Resiliencia y Robustez

**Conceptos clave**:
- Robustez: resistir perturbaciones
- Resiliencia: recuperarse de perturbaciones
- Redundancia: copias y alternativas
- Diversidad: múltiples estrategias
- Margen: capacidad de reserva
- Graceful degradation

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.29.1 | Robustez vs resiliencia | 45 min |
| 1.29.2 | Redundancia: el costo de la seguridad | 45 min |
| 1.29.3 | Diversidad: no todos los huevos en una canasta | 30 min |
| 1.29.4 | Margen y buffers | 30 min |
| 1.29.5 | Degradación elegante | 45 min |

**Ejercicios**:
1. Evaluar resiliencia de sistemas del GORE
2. ¿Hay redundancia suficiente?
3. ¿Qué pasa cuando falla el sistema X?
4. Diseñar degradación elegante

---

#### SEMANA 30: Antifragilidad

**Conceptos clave**:
- Antifragilidad: mejorar con estrés
- Frágil → Robusto → Antifrágil
- Opcionalidad: beneficiarse del upside
- Via negativa: fortaleza por sustracción
- Barbell: combinar extremos
- Skin in the game

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.30.1 | Más allá de la resiliencia: antifragilidad | 45 min |
| 1.30.2 | Ejemplos: biológicos, económicos, organizacionales | 45 min |
| 1.30.3 | Opcionalidad y asimetría | 45 min |
| 1.30.4 | Via negativa: quitar para fortalecer | 30 min |
| 1.30.5 | Diseñar para antifragilidad | 30 min |

**Ejercicios**:
1. Clasificar sistemas del GORE: frágil/robusto/antifrágil
2. ¿Qué sistemas mejoran con el caos?
3. ¿Dónde hay opcionalidad oculta?
4. Propuesta para aumentar antifragilidad

---

#### SEMANA 31: Modos de Falla

**Conceptos clave**:
- Falla silenciosa vs ruidosa
- Falla gradual vs catastrófica
- Single points of failure
- Fallas en cascada
- Fallas bizantinas
- Post-mortem: aprender de fallas

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.31.1 | Taxonomía de fallas | 45 min |
| 1.31.2 | Fallas silenciosas: el peor tipo | 45 min |
| 1.31.3 | Cascadas y contagio | 45 min |
| 1.31.4 | Análisis pre-mortem | 30 min |
| 1.31.5 | Post-mortem efectivo | 30 min |

**Ejercicios**:
1. Identificar single points of failure
2. Análisis pre-mortem de proyecto actual
3. Diseñar fallas ruidosas (que se detecten)
4. Template de post-mortem

---

#### SEMANA 32: Colapso y Recuperación

**Conceptos clave**:
- Transiciones de fase: cambio abrupto
- Umbrales críticos
- Histéresis: el camino de vuelta es diferente
- Señales tempranas de colapso
- Estrategias de recuperación
- Planificación de contingencia

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.32.1 | Colapso sistémico: cuándo todo falla junto | 45 min |
| 1.32.2 | Umbrales y transiciones | 45 min |
| 1.32.3 | Señales tempranas | 30 min |
| 1.32.4 | Recuperación: qué hacer después | 45 min |
| 1.32.5 | Planificación de contingencia | 30 min |

**Ejercicios**:
1. ¿Qué podría causar colapso sistémico en el GORE?
2. Identificar umbrales críticos
3. Diseñar sistema de alertas tempranas
4. Plan de contingencia para escenario crítico

**Entregable del Mes 8**:
> **Análisis de resiliencia de sistema crítico**
> - Evaluación frágil/robusto/antifrágil
> - Single points of failure
> - Plan de contingencia
> - Propuestas de fortalecimiento

---

### MES 9: EVOLUCIÓN Y CAMBIO

**Objetivo del mes**: Entender cómo cambian los sistemas en el tiempo, incluyendo la dinámica exponencial.

---

#### SEMANA 33: Selección y Adaptación

**Conceptos clave**:
- Variación, selección, herencia
- Fitness: adaptación al entorno
- Presiones selectivas
- Adaptación vs adopción
- Evolución de organizaciones
- Memes: evolución cultural

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.33.1 | Mecanismos de evolución | 45 min |
| 1.33.2 | Selección en organizaciones | 45 min |
| 1.33.3 | Presiones adaptativas en el GORE | 45 min |
| 1.33.4 | Evolución cultural y memes | 30 min |
| 1.33.5 | Diseñar para evolución | 30 min |

**Ejercicios**:
1. ¿Qué "sobrevive" en la organización? ¿Por qué?
2. Identificar presiones evolutivas actuales
3. ¿Qué prácticas se replican y transmiten?
4. Diseñar proceso que pueda evolucionar

---

#### SEMANA 34: Coevolución

**Conceptos clave**:
- Coevolución: cambio mutuo
- Red Queen: correr para quedarse en el lugar
- Lock-in y path dependence
- Coevolución tecnología-sociedad
- Coevolución humano-AI
- Puntos de intervención

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.34.1 | Coevolución: predador-presa, tecnología-uso | 45 min |
| 1.34.2 | Path dependence: la historia importa | 45 min |
| 1.34.3 | Lock-in: atrapados en una trayectoria | 30 min |
| 1.34.4 | Coevolución humano-AI | 45 min |
| 1.34.5 | Anticipar coevolución | 30 min |

**Ejercicios**:
1. Mapear coevolución proceso-sistema en el GORE
2. ¿Hay lock-in tecnológico?
3. ¿Cómo coevolucionas con Korax?
4. Escenarios de coevolución futura

---

#### SEMANA 35: Dinámica Exponencial

**Conceptos clave**:
- Crecimiento exponencial y sus engaños
- Tiempo de duplicación
- Curvas S: crecimiento → saturación
- Límites y carrying capacity
- Ley de Moore y similares
- Cuando los exponenciales se cruzan

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.35.1 | Intuición exponencial (o falta de ella) | 45 min |
| 1.35.2 | Modelar crecimiento exponencial | 45 min |
| 1.35.3 | Curvas S: el exponencial tiene límites | 30 min |
| 1.35.4 | Múltiples exponenciales cruzándose | 45 min |
| 1.35.5 | Implicaciones para planificación | 30 min |

**Ejercicios**:
1. Graficar crecimiento de datos/capacidad en el GORE
2. ¿Dónde hay crecimiento exponencial no reconocido?
3. ¿Qué exponenciales importan para los próximos 5 años?
4. Planificar bajo incertidumbre exponencial

---

#### SEMANA 36: Escenarios y Discontinuidades

**Conceptos clave**:
- Escenarios: futuros posibles
- Wildcards: eventos de baja probabilidad, alto impacto
- Cisnes negros
- Señales débiles
- Robustez ante incertidumbre
- Metodología de escenarios

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.36.1 | ¿Por qué pensar en escenarios? | 30 min |
| 1.36.2 | Metodología básica de escenarios | 45 min |
| 1.36.3 | Wildcards y cisnes negros | 45 min |
| 1.36.4 | Señales débiles: detectar el futuro | 45 min |
| 1.36.5 | Estrategias robustas | 30 min |

**Ejercicios**:
1. Identificar 2 ejes de incertidumbre para el GORE
2. Construir 4 escenarios (matriz 2x2)
3. ¿Qué wildcards podrían cambiar todo?
4. ¿Qué estrategia funciona en todos los escenarios?

**Entregable del Mes 9**:
> **3 escenarios a 5 años para GoreOS**
> - Escenario optimista
> - Escenario pesimista
> - Escenario disruptivo
> - Estrategias robustas para cada uno

---

## TRIMESTRE 4: ÉTICA + INTEGRACIÓN
*Meses 10-12 | El marco normativo y síntesis*

---

### MES 10: FUNDAMENTOS ÉTICOS

**Objetivo del mes**: Construir un framework ético explícito para guiar decisiones.

---

#### SEMANA 37: Consecuencialismo

**Conceptos clave**:
- Juzgar acciones por sus resultados
- Utilitarismo: maximizar bienestar
- Cálculo de consecuencias
- Problemas: predicción, agregación, derechos
- Consecuencialismo de reglas
- Aplicación a sistemas tecnológicos

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.37.1 | La idea básica: resultados importan | 30 min |
| 1.37.2 | Utilitarismo clásico | 45 min |
| 1.37.3 | Problemas del cálculo consecuencialista | 45 min |
| 1.37.4 | Variantes: reglas, preferencias, bienestar | 30 min |
| 1.37.5 | Consecuencialismo en diseño de sistemas | 45 min |

**Ejercicios**:
1. Analizar decisión reciente con lente consecuencialista
2. ¿Qué consecuencias importan?
3. Problemas de medición y comparación
4. ¿Cuándo el consecuencialismo falla?

---

#### SEMANA 38: Deontología

**Conceptos clave**:
- Juzgar acciones por reglas/deberes
- Imperativo categórico de Kant
- Derechos y deberes
- Restricciones: lo que no se puede hacer
- Problemas: conflicto de deberes, rigidez
- Aplicación a sistemas

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.38.1 | Más allá de las consecuencias | 30 min |
| 1.38.2 | Kant y el imperativo categórico | 45 min |
| 1.38.3 | Derechos: límites a la maximización | 45 min |
| 1.38.4 | Conflictos de deberes | 30 min |
| 1.38.5 | Deontología en diseño de sistemas | 45 min |

**Ejercicios**:
1. Identificar deberes en tu rol
2. ¿Hay cosas que no deberías hacer aunque maximicen resultados?
3. ¿Qué derechos debe respetar un sistema AI?
4. Conflictos: privacidad vs seguridad

---

#### SEMANA 39: Ética de Virtudes

**Conceptos clave**:
- Juzgar por carácter, no solo acciones
- Virtudes: disposiciones excelentes
- Eudaimonia: florecimiento humano
- Phronesis: sabiduría práctica
- Virtud en contexto profesional
- Aplicación a diseño

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.39.1 | Del "qué hacer" al "quién ser" | 30 min |
| 1.39.2 | Aristóteles y las virtudes | 45 min |
| 1.39.3 | Phronesis: sabiduría práctica | 45 min |
| 1.39.4 | Virtudes profesionales | 30 min |
| 1.39.5 | Diseñar para el florecimiento | 45 min |

**Ejercicios**:
1. ¿Qué virtudes requiere tu rol?
2. ¿Qué carácter debería tener Korax?
3. Diseño que promueva virtud vs que la inhiba
4. Florecimiento humano en sistemas automatizados

---

#### SEMANA 40: Tu Framework Ético

**Conceptos clave**:
- Integración de enfoques
- Casos donde divergen
- Tu jerarquía personal
- Procedimiento de decisión
- Documentar y revisar

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.40.1 | Comparando los tres enfoques | 45 min |
| 1.40.2 | Casos difíciles: cuando divergen | 45 min |
| 1.40.3 | Construyendo tu framework | 45 min |
| 1.40.4 | Procedimiento de decisión ética | 30 min |
| 1.40.5 | Revisión y ajuste | 30 min |

**Ejercicios**:
1. Escribir tu framework ético explícito
2. Aplicar a caso difícil
3. ¿Cuándo priorizar consecuencias? ¿Reglas? ¿Carácter?
4. Plan de revisión periódica

**Entregable del Mes 10**:
> **Tu framework ético explícito**
> - Principios fundamentales
> - Jerarquía en conflictos
> - Procedimiento de decisión
> - Casos ejemplo

---

### MES 11: ÉTICA TECNOLÓGICA

**Objetivo del mes**: Aplicar ética al diseño y uso de sistemas tecnológicos.

---

#### SEMANA 41: Responsabilidad y Accountability

**Conceptos clave**:
- ¿Quién responde cuando falla un sistema?
- Cadenas de responsabilidad
- Accountability distribuida
- Problema de las muchas manos
- Responsabilidad prospectiva vs retrospectiva
- Diseñar para accountability

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.41.1 | El problema de la responsabilidad tecnológica | 45 min |
| 1.41.2 | Muchas manos: ¿quién es responsable? | 45 min |
| 1.41.3 | Accountability en sistemas automatizados | 45 min |
| 1.41.4 | Responsabilidad prospectiva: anticipar | 30 min |
| 1.41.5 | Diseñar para atribuir responsabilidad | 30 min |

**Ejercicios**:
1. ¿Quién responde si Korax comete un error?
2. Mapear cadena de responsabilidad de un sistema
3. ¿Hay vacíos de accountability?
4. Propuesta para clarificar responsabilidades

---

#### SEMANA 42: Transparencia y Explicabilidad

**Conceptos clave**:
- Derecho a entender decisiones que te afectan
- Explicabilidad técnica vs social
- Trade-offs: rendimiento vs explicabilidad
- Niveles de transparencia
- Auditoría y verificación
- Documentación como transparencia

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.42.1 | ¿Por qué importa la explicabilidad? | 45 min |
| 1.42.2 | Tipos de explicación | 45 min |
| 1.42.3 | Trade-offs con rendimiento | 30 min |
| 1.42.4 | Auditoría: verificar sin explicar todo | 45 min |
| 1.42.5 | Documentación efectiva | 30 min |

**Ejercicios**:
1. ¿Puedes explicar cómo Korax toma decisiones?
2. Niveles de explicación para diferentes audiencias
3. Diseñar proceso de auditoría
4. Mejorar documentación de sistema

---

#### SEMANA 43: Justicia Algorítmica

**Conceptos clave**:
- Bias en datos y algoritmos
- Fairness: múltiples definiciones
- Discriminación directa e indirecta
- Grupos protegidos
- Trade-offs entre tipos de fairness
- Mitigación de bias

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.43.1 | Bias: de dónde viene | 45 min |
| 1.43.2 | Definiciones de fairness (y por qué son incompatibles) | 45 min |
| 1.43.3 | Detectar bias | 30 min |
| 1.43.4 | Mitigar bias | 45 min |
| 1.43.5 | Justicia más allá del algoritmo | 30 min |

**Ejercicios**:
1. ¿Dónde podría haber bias en sistemas del GORE?
2. ¿Qué definición de fairness aplicar?
3. Diseñar proceso de detección de bias
4. Propuesta de mitigación

---

#### SEMANA 44: Límites - Qué NO Automatizar

**Conceptos clave**:
- Decisiones que requieren juicio humano
- Contexto y excepcionalidad
- Dignidad y despersonalización
- Autonomía del afectado
- Reversibilidad
- Líneas rojas

**Contenido**:

| Sesión | Tema | Duración |
|--------|------|----------|
| 1.44.1 | Automatización y deshumanización | 45 min |
| 1.44.2 | Cuándo el contexto importa demasiado | 45 min |
| 1.44.3 | Decisiones que afectan dignidad | 30 min |
| 1.44.4 | Preservar autonomía humana | 45 min |
| 1.44.5 | Definir líneas rojas | 30 min |

**Ejercicios**:
1. Listar decisiones que NO debe tomar Korax
2. ¿Por qué esas y no otras?
3. Diseñar safeguards para líneas rojas
4. Política de límites para AI en GORE

**Entregable del Mes 11**:
> **Política ética para uso de AI en GORE**
> - Principios de uso
> - Responsabilidades claras
> - Requisitos de transparencia
> - Límites y líneas rojas

---

### MES 12: INTEGRACIÓN AÑO 1

**Objetivo del mes**: Consolidar todo lo aprendido en un modelo coherente.

---

#### SEMANA 45: Revisión Estructura + Información

**Actividades**:
- Revisar conceptos clave de Meses 1-3
- Conectar con práctica actual
- Identificar brechas
- Actualizar entregables anteriores

---

#### SEMANA 46: Revisión Mente + Lenguaje

**Actividades**:
- Revisar conceptos clave de Meses 4-6
- Conectar con práctica actual
- Identificar brechas
- Actualizar entregables anteriores

---

#### SEMANA 47: Revisión Sistemas + Evolución

**Actividades**:
- Revisar conceptos clave de Meses 7-9
- Conectar con práctica actual
- Identificar brechas
- Actualizar entregables anteriores

---

#### SEMANA 48: Síntesis - Mi Modelo del Mundo v1

**Actividades**:
- Integrar todos los dominios
- Escribir documento síntesis
- Identificar conexiones entre áreas
- Plan para Año 2

**Entregable del Mes 12**:
> **"Mi modelo del mundo v1"**
> - Síntesis de los 7 dominios
> - Conexiones entre áreas
> - Aplicación a tu contexto
> - Preguntas abiertas para Año 2

---

# AÑO 2: PROFUNDIZACIÓN

## TRIMESTRE 5-8: Esquema

El Año 2 se estructura de manera similar pero con mayor profundidad y enfoque en aplicación.

### Q5: Inteligencia Artificial (Meses 13-15)
- Representación y aprendizaje
- Razonamiento y decisión
- Agencia y alineamiento

### Q6: Gobernanza + Arquitectura (Meses 16-18)
- Gobernanza de sistemas
- Pensamiento arquitectural
- Delegación efectiva

### Q7: Escenarios + Futurismo (Meses 19-21)
- Dinámica del cambio
- Metodología de escenarios
- Adaptabilidad personal

### Q8: Síntesis + Proyecto (Meses 22-24)
- Integración total
- Proyecto capstone
- Tu modelo del mundo v2

---

*[El programa detallado del Año 2 se elaborará al completar el Año 1, adaptándose a tu progreso y necesidades emergentes]*

---

## APÉNDICES

### A. Glosario de Conceptos Clave

*(Se irá construyendo durante el programa)*

### B. Recursos Recomendados por Dominio

*(Se agregará según interés específico)*

### C. Templates de Entregables

*(Se irán refinando con la práctica)*

### D. Log de Progreso

| Mes | Semana | Completado | Notas |
|-----|--------|------------|-------|
| 1 | 1 | ☐ | |
| 1 | 2 | ☐ | |
| ... | ... | ... | ... |

---

*Última actualización: 2026-01-31*
*Versión: 1.0*
*Arquitecto del programa: Korvo + Korax*
