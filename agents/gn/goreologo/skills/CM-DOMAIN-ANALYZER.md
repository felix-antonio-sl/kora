---
_manifest:
  urn: "urn:gn:skill:goreologo-domain-analyzer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-DOMAIN-ANALYZER

## Proposito
Analizar en profundidad el dominio institucional de una consulta GORE: estructura normativa, actores, instrumentos, flujos y contexto especifico Nuble.

## Procedimiento
1. Identificar el dominio principal de analisis (legal, financiero, operativo, digital, territorial).
2. Descomponer el tema en dimensiones analizables (maximo 5 chunks):
   - Marco normativo vigente: ley, reglamento, instruccion CGR aplicable.
   - Estructura institucional: organos involucrados, competencias, dependencias.
   - Instrumentos o fondos: tipo, fuente, condiciones, plazos.
   - Flujo o proceso: etapas, actores, sistemas de informacion (SIGFE, BIP, SISREG).
   - Contexto Nuble especifico: datos regionales, estado actual, particularidades.
3. Identificar interrelaciones entre dimensiones.
4. Marcar con etiquetas: [norma vigente], [dato institucional], [interpretacion], [incertidumbre].
5. Detectar vacios de informacion y declararlos explicitamente.

## Output
Analisis estructurado en chunks 3-5: tabla Dimension/Contenido/Fuente. Etiquetas de certeza aplicadas. Lista de vacios de informacion identificados. Base para CM-SYNTHESIZER.
