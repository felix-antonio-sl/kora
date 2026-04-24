---
_manifest:
  urn: urn:gn:skill:asesor-juridico-clasificador-acto:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar un acto administrativo del GORE segun tipo, autoridad firmante, materia y regimen de control (exento/afecto Toma de Razon CGR). Arbol de decision basado en LOC 19.175, Ley 19.880 y Resolucion CGR N7/2019.

## Input/Output
- **Input:** materia: string, autoridad: string, monto_utm: number | null, partes: string[], descripcion: string
- **Output:** clasificacion: {tipo_acto: string, autoridad_firmante: string, materia: string, control: string, requiere_toma_razon: boolean, fundamento: string}

## Procedimiento
1. **Identificar materia** del acto: Personal, Financiero, Convenio, Contrato, Administrativo.
2. **Determinar autoridad firmante**: Gobernador Regional, Administrador Regional, Jefe de Division, otro.
3. **Clasificar tipo de acto** segun arbol de decision:
   - IF materia Personal + autoridad Gobernador → Resolucion Exenta.
   - IF materia Financiera + monto > 2500 UTM → Resolucion Afecta.
   - IF materia Financiera + monto <= 2500 UTM → Resolucion Exenta.
   - IF convenio con terceros publicos → Convenio Marco + Resolucion Aprobatoria.
   - IF convenio con privados + monto > 10000 UTM → Afecto Toma de Razon.
   - IF contrato + monto > umbrales CGR → Afecto Toma de Razon.
   - IF decreto → Decreto (siempre firma Gobernador).
   - DEFAULT → Resolucion Exenta.
4. **Determinar regimen de control**:
   - Exento: bajo umbrales, se registra pero no va a tramite CGR.
   - Afecto Toma de Razon: sobre umbrales o materia sensible (personal planta, contrataciones > 2500 UTM, convenios privados > 10000 UTM). Requiere envio a CGR.
5. **Validar coherencia**: tipo acto compatible con autoridad y materia. IF incoherencia → solicitar mas informacion.
6. **Emitir fundamento**: citar norma habilitante (LOC 19.175, Resolucion CGR N7/2019, Ley 19.880).

## Signature Output
```yaml
clasificacion:
  tipo_acto: "Resolucion Afecta"
  autoridad_firmante: "Gobernador Regional"
  materia: "Financiero"
  control: "Afecto Toma de Razon"
  requiere_toma_razon: true
  fundamento: "Monto supera 2.500 UTM — Resolucion CGR N7/2019. LOC 19.175 Art.24 letra a."
```
