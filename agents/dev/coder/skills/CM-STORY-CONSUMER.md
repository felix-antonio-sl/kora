---
_manifest:
  urn: "urn:dev:skill:coder-story-consumer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-STORY-CONSUMER

## Proposito
Lee y valida una historia antes de planificar su implementacion. Verifica que los 5 elementos estan completos y son suficientes para codear.

## Procedimiento
1. Leer historia completa.
2. Verificar 5 elementos (Xanpan::Agents §5.1):
   - [ ] Who/What/Why presente y claro.
   - [ ] Criterios de aceptacion testables (3-7 ACs numerados).
   - [ ] Valor de negocio asignado (1-5).
   - [ ] Senal de complejidad (simple|estandar|complejo|critico).
   - [ ] Clasificacion de riesgo (lectura|escritura|destructiva).
3. Si falta algun elemento: RECHAZAR con lista de elementos faltantes. Derivar a fxsl/planner.
4. Si todos presentes: extraer informacion clave para implementacion:
   - Entidades afectadas (mapear a SCHEMA.md).
   - Componentes UI afectados (si aplica).
   - Endpoints necesarios.
   - Dependencias con otras historias.
5. Cargar context files requeridos: CONVENTIONS.md + SCHEMA.md (minimo). ARCHITECTURE.md si la historia toca multiples componentes.
6. Pasar a CM-IMPLEMENTATION-PLANNER.

## Output
Historia validada: {elementos_ok: bool, entidades[], componentes[], endpoints[], dependencias[], context_files_cargados[]}. O RECHAZO con {elementos_faltantes[]}.
