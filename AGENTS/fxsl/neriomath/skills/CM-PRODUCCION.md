---
_manifest:
  urn: urn:fxsl:skill:neriomath-produccion:1.3.0
  type: lazy_load_endofunctor
---

## Proposito
Calibrar y ejecutar la produccion del output final al receptor. Verificar que beta-vigilancia aplico guardias anti-* durante operacion. Ejecutar paso MULTIPLICAR: transferir metodo, no solo resultado. Evaluar salida contra VCN antes de entregar.

## Input/Output
- **Input:** Outputs de todos los skills ejecutados (posicionador, diagnosticador, motor trialectico), perfil del receptor, clase de activacion
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

### 4. Ciclo borrador-critica
- Generar borrador -> criticar internamente (respondo lo que preguntaron? complejidad sin valor? perspectiva unica?) -> revisar
- Listar 2-3 objeciones probables; integrar respuestas o reconocer limites
- Si el siguiente paso real es humano, no cerrar en falso: explicitar handoff, responsable o decision humana pendiente

### 5. MULTIPLICAR
- Inspeccionar outputs de todos los skills previos: algun framework o patron transferible?
- Si el motor extrajo un patron reutilizable: integrarlo en la entrega
- Test triple: (1) se entiende? (2) se puede actuar? (3) el interlocutor queda con mas capacidad para pensar problemas similares solo?
- No pedagogizar lo obvio. Mostrar patron solo cuando genuinamente amplifica.
- En CLASE-1: omitir multiplicacion. En CLASE-2: mencionar patron si existe. En CLASE-3: transferencia explicita del metodo.

### 6. Evaluacion VCN final
Evaluar contra VCN (SOUL.md). Si algun costo presente (ruido, sesgo, ilusion, sobreconfianza): corregir antes de entregar. Si alguna ganancia ausente (verdad, claridad, resolucion, robustez, transferibilidad) por descuido: corregir.

### 7. Entrega
- Etiquetas [hecho]/[inferencia]/[especulacion]/[incertidumbre] donde corresponda
- Si limite_humano = true: explicitar el limite y el siguiente paso humano en vez de simular cierre analitico
- En CLASE-1: solo respuesta directa, sin fases visibles
- En CLASE-2: estructura compacta, patron si existe
- En CLASE-3: estructura completa con mapa de vulnerabilidades y metodo transferido

## Signature Output
Output estructurado segun contrato de salida, calibrado al receptor, evaluado contra VCN, con etiquetas epistemicas, objeciones anticipadas integradas, guardias anti-* verificadas, y patron reutilizable transferido si aplica.
