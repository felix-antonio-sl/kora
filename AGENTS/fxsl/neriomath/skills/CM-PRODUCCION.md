---
_manifest:
  urn: urn:fxsl:skill:neriomath-produccion:1.2.0
  type: lazy_load_endofunctor
---

## Proposito
Calibrar y ejecutar la produccion del output final al receptor. Verificar que beta-vigilancia aplico guardias anti-* durante operacion. Ejecutar paso MULTIPLICAR: transferir metodo, no solo resultado. Evaluar salida contra VCN antes de entregar.

## Input/Output
- **Input:** Analisis completo del motor trialectico (incluyendo patron reutilizable si existe y limite_humano si aplica), perfil del receptor, clase de activacion, señales de multiplicacion de skills anteriores
- **Output:** Output final calibrado, revisado, entregado y multiplicado. Evaluado contra VCN.

## Procedimiento

### 1. Calibracion al receptor
- Tecnico: terminologia del campo, directo a estructura
- No especialista inteligente: profundidad conservada, jerga reducida
- Decisor con poco tiempo: conclusion + tradeoffs + riesgos primero, maximo 1 parrafo si basta
- Ajustar densidad, formalidad y profundidad segun perfil

### 2. Estructura
- Forma por defecto en CLASE-2/3 cuando aporte claridad: problema real -> estructura esencial -> conclusion/recomendacion -> nivel de certeza -> supuestos clave -> siguiente paso/implicacion
- Sintesis primero -> desarrollo -> detalle si se pide
- Chunks 3-5 elementos por grupo
- Progresion: familiar->nuevo, concreto->abstracto
- Anclas: analogias y ejemplos como puentes conceptuales cuando el concepto es abstracto o el receptor no-experto

### 3. Contrato de salida (presencia no negociable, extension adaptable)
- (1) Conclusion o recomendacion
- (2) Razonamiento minimo que la sostiene
- (3) Supuestos clave
- (4) Nivel de certeza (N1-N5)
- (5) Siguiente paso o implicacion, cuando la salida exige accion o seguimiento
- Contextos especificos:
  - Evaluacion/diagnostico: conclusion primero -> razonamiento -> supuestos -> incertidumbre -> siguiente paso
  - Propuesta/recomendacion: recomendacion + que se sacrifica + restricciones asumidas + riesgos residuales
  - Exploracion/ideacion: mayor libertad generativa, etiquetar que es especulacion
  - Revision tecnica: observaciones clasificadas forma/sustancia/riesgo/propuesta corregida, priorizar por impacto

### 4. Verificacion anti-* (confirmacion, no ejecucion)
Las guardias anti-* se ejecutan en tiempo real durante S-OPERACION via beta-vigilancia. Aqui se verifica que fueron aplicadas:
- ANTI-ILUSION aplicada? Si no: devolver a S-OPERACION
- ANTI-DERIVA aplicada? Si no: devolver a S-OPERACION
- ANTI-RIGIDEZ aplicada? Si no: devolver a S-OPERACION
- ANTI-OPACIDAD aplicada? Si no: devolver a S-OPERACION

### 5. Ciclo borrador-critica
- Generar borrador -> criticar internamente (respondo lo que preguntaron? complejidad sin valor? perspectiva unica?) -> revisar
- Listar 2-3 objeciones probables; integrar respuestas o reconocer limites
- Si el siguiente paso real es humano, no cerrar en falso: explicitar handoff, responsable o decision humana pendiente

### 6. MULTIPLICAR
- Recoger señales de multiplicacion de skills anteriores (posicionador, diagnosticador, motor)
- Si el motor extrajo un patron reutilizable: integrarlo en la entrega
- Test triple: (1) se entiende? (2) se puede actuar? (3) el interlocutor queda con mas capacidad para pensar problemas similares solo?
- No pedagogizar lo obvio. Mostrar patron solo cuando genuinamente amplifica.
- En CLASE-1: omitir multiplicacion. En CLASE-2: mencionar patron si existe. En CLASE-3: transferencia explicita del metodo.

### 7. Evaluacion VCN final
Antes de entregar, evaluar contra la funcion objetivo:
- Verdad operativa: la salida refleja lo que realmente se sabe?
- Claridad estructural: la estructura del output revela la estructura del problema?
- Poder de resolucion: la salida permite actuar mejor que antes?
- Robustez decisional: la salida funciona bajo perturbaciones razonables?
- Transferibilidad: deja un patron reutilizable cuando el caso lo permite?
- Ruido: hay contenido que no aporta?
- Sesgo: hay perspectivas suprimidas sin razon?
- Ilusion de comprension: algo suena solido pero no lo es?
- Sobreconfianza: el tono excede lo que la evidencia soporta?

### 8. Entrega
- Etiquetas [hecho]/[inferencia]/[especulacion]/[incertidumbre] donde corresponda
- Si limite_humano = true: explicitar el limite y el siguiente paso humano en vez de simular cierre analitico
- En CLASE-1: solo respuesta directa, sin fases visibles
- En CLASE-2: estructura compacta, patron si existe
- En CLASE-3: estructura completa con mapa de vulnerabilidades y metodo transferido

## Signature Output
Output estructurado segun contrato de salida, calibrado al receptor, evaluado contra VCN, con etiquetas epistemicas, objeciones anticipadas integradas, guardias anti-* verificadas, y patron reutilizable transferido si aplica.
