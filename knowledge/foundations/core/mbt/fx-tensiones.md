# Tensiones del Modelamiento de Sistemas

> Versión 2.2 | 2025-12-13

## Principio Estructural

```
┌───────────────────────────────────────────────────────────────┐
│ C: CONTEXTO (condiciones que modulan)                         │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ B: PRAXIS (cómo decide el modelador)                    │  │
│  │  ┌───────────────────────────────────────────────────┐  │  │
│  │  │ A: TENSIONES SUSTANTIVAS (qué debe decidir)       │  │  │
│  │  └───────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

---

## A: TENSIONES SUSTANTIVAS

### A1. SER

| Tensión                | Polo A          | Polo B        | Pregunta            |
| ---------------------- | --------------- | ------------- | ------------------- |
| Entidad ↔ Evento       | Persiste        | Ocurre        | ¿Es algo o sucede?  |
| Concreto ↔ Abstracto   | Material        | Informacional | ¿Ocupa espacio?     |
| Token ↔ Type           | Este específico | Del tipo      | ¿Instancia o clase? |
| Todo ↔ Partes          | Agregado        | Componentes   | ¿Composición?       |
| General ↔ Particular   | Superclase      | Subclase      | ¿Generalización?    |
| Simétrico ↔ Asimétrico | A↔B = B↔A       | A→B ≠ B→A     | ¿Recíproca?         |

### A2. DEVENIR

| Tensión                     | Polo A     | Polo B       | Pregunta          |
| --------------------------- | ---------- | ------------ | ----------------- |
| Estático ↔ Dinámico         | Invariante | Cambiante    | ¿Cambia?          |
| Instantáneo ↔ Durativo      | Punto      | Intervalo    | ¿Duración?        |
| Secuencial ↔ Paralelo       | En serie   | Simultáneo   | ¿Orden fijo?      |
| Causa ↔ Efecto              | Produce    | Es producido | ¿Qué origina qué? |
| Agente ↔ Paciente           | Actúa      | Es afectado  | ¿Quién a quién?   |
| Determinista ↔ Probabilista | Certeza    | Distribución | ¿Predecible?      |

### A3. CONOCER

| Tensión                | Polo A         | Polo B     | Pregunta           |
| ---------------------- | -------------- | ---------- | ------------------ |
| Conocido ↔ Desconocido | Tenemos info   | Falta info | ¿Lo sabemos?       |
| Cierto ↔ Incierto      | Alta confianza | Duda       | ¿Cuánta certeza?   |
| Hecho ↔ Supuesto       | Verificado     | Asumido    | ¿Confirmado?       |
| Explícito ↔ Tácito     | Declarado      | Implícito  | ¿Formalizado?      |
| Situado ↔ Universal    | Contextual     | General    | ¿Depende del caso? |
| AND ↔ OR ↔ XOR         | Todos          | Alguno/Uno | ¿Combinación?      |

### A4. EXPRESAR

| Tensión                    | Polo A   | Polo B    | Pregunta             |
| -------------------------- | -------- | --------- | -------------------- |
| Visual ↔ Textual           | Diagrama | Lenguaje  | ¿Cómo se representa? |
| Formal ↔ Informal          | Estricto | Libre     | ¿Procesable?         |
| Compacto ↔ Verboso         | Denso    | Explícito | ¿Economía?           |
| Prescriptivo ↔ Descriptivo | Debe ser | Es        | ¿Norma o realidad?   |
| Detalle ↔ Abstracción      | Fino     | Grueso    | ¿Cuánto zoom?        |
| Modular ↔ Monolítico       | Piezas   | Bloque    | ¿Separable?          |

---

## B: PRAXIS

### B1. DECIDIR

| Tensión                  | Polo A      | Polo B            | Pregunta           |
| ------------------------ | ----------- | ----------------- | ------------------ |
| Incluir ↔ Omitir         | Agregar     | Dejar fuera       | ¿Es relevante?     |
| Ahora ↔ Después          | Resolver ya | Postergar         | ¿Urgente?          |
| Compromiso ↔ Exploración | Fijar       | Mantener opciones | ¿Decido o exploro? |
| Regla ↔ Excepción        | Adherir     | Excepcionar       | ¿Estricto?         |

### B2. COMUNICAR

| Tensión                | Polo A       | Polo B      | Pregunta              |
| ---------------------- | ------------ | ----------- | --------------------- |
| Mi visión ↔ Compartida | Lo que yo sé | Lo acordado | ¿Refleja quién?       |
| Experto ↔ Novato       | Técnico      | General     | ¿Para quién?          |
| Consenso ↔ Autoridad   | Acuerdo      | Decisión    | ¿Cómo resuelvo?       |
| Fidelidad ↔ Utilidad   | Preciso      | Práctico    | ¿Exacto o suficiente? |

### B3. PROCEDER

| Tensión                 | Polo A        | Polo B       | Pregunta            |
| ----------------------- | ------------- | ------------ | ------------------- |
| Top-down ↔ Bottom-up    | Desde visión  | Desde partes | ¿Por dónde empiezo? |
| Análisis ↔ Síntesis     | Descomponer   | Componer     | ¿Separo o integro?  |
| Planificar ↔ Improvisar | Diseñar antes | Descubrir    | ¿Plan o emergente?  |
| Refinar ↔ Reestructurar | Mejorar       | Rehacer      | ¿Ajusto o rehago?   |

### B4. VALIDAR

| Tensión              | Polo A     | Polo B          | Pregunta                    |
| -------------------- | ---------- | --------------- | --------------------------- |
| Modelo ↔ Realidad    | Coherente  | Correspondiente | ¿Bien formado o representa? |
| Verificar ↔ Validar  | Bien hecho | Correcto        | ¿Cumple reglas o propósito? |
| Foco ↔ Contexto      | Detalle    | Visión general  | ¿Zoom in o out?             |
| Completar ↔ Entregar | Seguir     | Terminar        | ¿Cuándo suficiente?         |

---

## C: CONTEXTO

### C1. RECURSOS

| Tensión                | Polo A   | Polo B   | Pregunta       |
| ---------------------- | -------- | -------- | -------------- |
| Tiempo ↔ Calidad       | Rápido   | Riguroso | ¿Prioridad?    |
| Individual ↔ Colectivo | Solo     | Equipo   | ¿Quién modela? |
| Herramientas ↔ Manual  | Software | Papel    | ¿Con qué?      |

### C2. PROPÓSITO

| Tensión                | Polo A     | Polo B     | Pregunta        |
| ---------------------- | ---------- | ---------- | --------------- |
| Explorar ↔ Especificar | Descubrir  | Documentar | ¿Fase?          |
| Comunicar ↔ Computar   | Humanos    | Máquinas   | ¿Quién consume? |
| Temporal ↔ Permanente  | Desechable | Mantenible | ¿Vida útil?     |

### C3. DOMINIO

| Tensión             | Polo A          | Polo B       | Pregunta      |
| ------------------- | --------------- | ------------ | ------------- |
| Conocido ↔ Novedoso | Familiar        | Nuevo        | ¿Sé del tema? |
| Estable ↔ Volátil   | Cambia poco     | Cambia mucho | ¿Frecuencia?  |
| Simple ↔ Complejo   | Pocos elementos | Muchos       | ¿Escala?      |

### C4. CULTURA

| Tensión             | Polo A         | Polo B    | Pregunta      |
| ------------------- | -------------- | --------- | ------------- |
| Formal ↔ Informal   | Estricto       | Flexible  | ¿Rigor?       |
| Ágil ↔ Planificado  | Iterativo      | Fases     | ¿Metodología? |
| Tolerante ↔ Crítico | Aproximaciones | Precisión | ¿Estándar?    |

---

## Métricas

| Capa           | Categorías | Tensiones |
| -------------- | ---------- | --------- |
| A: Sustantivas | 4          | 24        |
| B: Praxis      | 4          | 16        |
| C: Contexto    | 4          | 12        |
| **Total**      | **12**     | **52**    |
