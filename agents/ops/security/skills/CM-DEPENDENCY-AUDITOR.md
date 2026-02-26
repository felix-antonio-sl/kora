---
_manifest:
  urn: "urn:ops:skill:security-dependency-auditor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Auditar dependencias del proyecto para CVEs evaluando exposicion REAL, no solo existencia de vulnerabilidad. Diferencia clave: "dependencia tiene CVE" vs "dependencia tiene CVE Y la funcion vulnerable esta expuesta a input externo en nuestro codebase." Proponer mitigacion priorizada por exposicion real.

## I/O

- **Input:** dependencies: {name: string, version: string}[], codebase_usage: {dependency: string, import_locations: FileLocation[], input_sources: InputSource[]}
- **Output:** audit: {total_cves: number, exposed_cves: number, findings: DependencyFinding[], mitigations: Mitigation[]}

## Procedimiento

1. **Consultar CVEs** para cada dependencia:
   - Buscar en base CVE: NVD, GitHub Advisory, OSV
   - Filtrar por version actual (descartar CVEs que no aplican a version instalada)
   - Registrar: cve_id, severity (CVSS), descripcion, funcion vulnerable, versiones afectadas

2. **Evaluar exposicion por CVE**:
   - **Localizar uso**: donde se importa/usa la dependencia en el codebase (import_locations)
   - **Identificar funcion vulnerable**: que funcion especifica tiene el CVE
   - **Trazar input**: la funcion vulnerable recibe input externo? (input_sources)
     - Externo directo: HTTP request body/params/headers, webhook payload, file upload
     - Externo indirecto: dato de DB que se origino de input usuario
     - Interno controlado: configuracion estatica, constantes, input hardcoded
   - **Clasificar exposicion**:
     - EXPOSED: funcion vulnerable + input externo directo o indirecto
     - NOT_EXPOSED: funcion vulnerable + input interno controlado
     - UNUSED: funcion vulnerable no se usa en el codebase

3. **Priorizar**:
   - EXPOSED + CVSS critical/high → prioridad CRITICAL
   - EXPOSED + CVSS medium → prioridad HIGH
   - NOT_EXPOSED + CVSS critical → prioridad MEDIUM (upgrade preventivo)
   - NOT_EXPOSED + CVSS medium/low → prioridad LOW
   - UNUSED → prioridad INFORMATIONAL

4. **Proponer mitigacion**:
   - CRITICAL/HIGH: patch o upgrade inmediato, con version target
   - MEDIUM: upgrade en proximo ciclo, workaround si disponible
   - LOW: registrar, aceptar riesgo con justificacion
   - Para cada mitigacion: esfuerzo estimado, breaking changes potenciales

## Signature Output

```yaml
audit:
  total_cves: 5
  exposed_cves: 2
  findings:
    - dependency: "requests"
      version: "2.28.0"
      cve_id: "CVE-2026-1234"
      cvss: 9.8
      vulnerable_function: "url_parse()"
      usage_location: "src/clients/external_api.py:15"
      input_source: "user_provided_url from HTTP request"
      exposure: "EXPOSED"
      priority: "CRITICAL"
    - dependency: "pyyaml"
      version: "5.4.1"
      cve_id: "CVE-2026-5678"
      cvss: 7.5
      vulnerable_function: "yaml.load()"
      usage_location: "src/config/loader.py:8"
      input_source: "static config file (internal)"
      exposure: "NOT_EXPOSED"
      priority: "MEDIUM"
  mitigations:
    - dependency: "requests"
      action: "upgrade"
      target_version: ">=2.31.0"
      priority: "CRITICAL"
      effort: "low"
      breaking_changes: "none known"
    - dependency: "pyyaml"
      action: "upgrade_next_cycle"
      target_version: ">=6.0.1"
      priority: "MEDIUM"
      effort: "low"
      breaking_changes: "yaml.load() requires explicit Loader param"
```
