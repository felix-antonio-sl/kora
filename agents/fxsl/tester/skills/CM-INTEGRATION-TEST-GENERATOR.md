---
_manifest:
  urn: "urn:fxsl:skill:tester-integration-test-generator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INTEGRATION-TEST-GENERATOR

## Proposito
Genera tests de integracion para boundaries entre componentes. Verifica que los contratos entre modulos, APIs, bases de datos y servicios externos funcionan correctamente en conjunto.

## Input/Output
- **Input:** Componentes y boundaries identificados: {componentes: string[], boundaries: [{from, to, protocolo, contrato}]}
- **Output:** Tests de integracion: {tests: [{boundary, test_name, test_code, tipo: api|db|service}]}

## Procedimiento

### Paso 1: Identificar boundaries
- Leer ARCHITECTURE.md o diagrama de componentes si disponible.
- Clasificar boundaries por tipo:
  - **API:** HTTP endpoints (request → handler → response)
  - **DB:** Queries y transacciones (service → repository → database)
  - **Service:** Llamadas a servicios externos (service → external API)
  - **Module:** Contratos entre modulos internos (module A → module B)
- Documentar: componente origen → componente destino → protocolo → contrato.

### Paso 2: Generar tests por boundary tipo API
Para cada endpoint:
1. **Happy path:** Request valido → response esperado (status code, body schema).
2. **Validation:** Request invalido → 400 con mensaje de error claro.
3. **Not found:** Recurso inexistente → 404.
4. **Conflict:** Operacion conflictiva (duplicado, estado invalido) → 409.
5. **Server error:** Fallo interno simulado → 500 con error generico (no leak de internals).
- Verificar headers, content-type, response schema.

### Paso 3: Generar tests por boundary tipo DB
Para cada query/transaccion:
1. **CRUD basico:** Create → Read → Update → Delete (cada operacion como test independiente).
2. **Constraints:** Violacion de unique, foreign key, not null → error apropiado.
3. **Transacciones:** Rollback en fallo parcial.
4. **Concurrencia:** Si aplica, race conditions basicas.
- Usar fixtures/seeds para datos de test. Limpiar despues de cada test.

### Paso 4: Generar tests por boundary tipo Service
Para cada servicio externo:
1. **Mock del servicio:** Simular respuestas del servicio externo.
2. **Happy path:** Servicio responde OK → comportamiento esperado.
3. **Timeout:** Servicio no responde → timeout handling.
4. **Error:** Servicio responde error → graceful degradation.
5. **Retry:** Si hay politica de retry, verificar que se respeta.

### Paso 5: Verificar independencia
- Cada test DEBE poder ejecutarse aislado.
- Setup y teardown por test (no compartir estado entre tests).
- Mocks/stubs reiniciados entre tests.

### Paso 6: Presentar para revision
- Tabla resumen: Boundary | Tipo | Tests Count | Cobertura.
- Codigo de cada test en bloque con lenguaje especificado.
- Solicitar aprobacion del Operador.

## Invariantes
- Tests de integracion cubren boundaries, NO logica interna.
- Cada boundary tiene al menos un test happy path + un test error path.
- Tests independientes y deterministicos.
- Mocks para servicios externos (nunca llamar a servicios reales en tests).
- Cleanup despues de cada test (no leak de estado).

## Signature Output
```
| Boundary          | Tipo    | Tests | Cobertura      |
|-------------------|---------|-------|----------------|
| POST /api/products| API     | 5     | happy,400,404,409,500 |
| ProductRepository | DB      | 4     | CRUD + constraints    |
| PaymentService    | Service | 3     | happy,timeout,error   |
```
[bloques de codigo por test]
