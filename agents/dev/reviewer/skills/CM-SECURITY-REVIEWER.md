---
_manifest:
  urn: "urn:dev:skill:reviewer-security-reviewer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-SECURITY-REVIEWER

## Proposito
Analiza seguridad de un PR en contexto arquitectonico. No es SAST estatico — es analisis contextual.

## Procedimiento
1. Leer diff del PR + ARCHITECTURE.md (si disponible).
2. Clasificar superficie de ataque afectada por el cambio:
   - Autenticacion/autorizacion.
   - Datos sensibles (PII, financieros, medicos).
   - Interfaces externas (APIs publicas, webhooks).
   - Criptografia/tokens/secrets.
   - Interaccion con LLMs (prompt injection surface).
3. Verificar por categoria:

### Input Validation
- [ ] Todo input de usuario validado con Zod/Pydantic antes de procesamiento.
- [ ] No hay concatenacion de strings para SQL (solo parametrizado).
- [ ] No hay interpolacion de user input en templates HTML (XSS).
- [ ] No hay eval(), exec() con user input.

### Secrets
- [ ] No hay secrets hardcoded (API keys, tokens, passwords).
- [ ] Secrets inyectados via variables de entorno.
- [ ] No hay secrets en logs ni error messages.

### Privilegios
- [ ] Principio de minimo privilegio respetado.
- [ ] No hay escalada de privilegios (usuario accede a datos de otro).
- [ ] Row-level security si datos multi-tenant.

### LLM-Specific (si aplica)
- [ ] User input NO concatenado en system prompts.
- [ ] Output de LLM tratado como untrusted (validado antes de ejecutar acciones).
- [ ] No hay datos sensibles en prompts enviados a LLMs externos.
- [ ] Budget enforcement en llamadas a LLM.

4. Registrar hallazgos con severidad CRITICO para toda vulnerabilidad de seguridad.
5. Analizar en contexto: una dependencia vulnerable que NO esta expuesta a input externo es MENOR, no CRITICO.

## Output
Hallazgos de seguridad: tabla [{severidad, categoria, archivo:linea, descripcion, sugerencia}]. Superficie de ataque clasificada.
