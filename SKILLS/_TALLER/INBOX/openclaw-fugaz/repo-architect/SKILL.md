---
name: repo-architect
description: Evalua y mejora la estructura de un repositorio para hacerlo agent-friendly. Usar cuando el usuario pida organizar un repo, evaluar su estructura, o prepararlo para trabajo con agentes.
---

# Repo Architect

Disenar repos para que agentes puedan trabajar con minima friccion.

## Checklist de repo agent-friendly

- [ ] Estructura de directorios obvia (nombres autoexplicativos)
- [ ] README con setup en <5 comandos
- [ ] CLIs para operaciones importantes (build, test, deploy, seed)
- [ ] Docs locales por subsistema (no un solo README monolito)
- [ ] Convenciones repetibles y visibles
- [ ] Ejemplos concretos de uso (no solo API docs abstractas)
- [ ] Acceso simple a logs y DB
- [ ] Archivos <500 lineas (dividir si exceden)
- [ ] .env.example con todas las variables documentadas
- [ ] Scripts de operacion repetibles con un solo comando

## Principio

La ingenieria del repo ES ingenieria de contexto. Un directorio mal nombrado o un archivo de 2000 lineas no solo afectan a humanos — envenenan el contexto del agente y degradan la calidad de su output.

## Procedimiento

1. Auditar estructura actual (tree, tamano de archivos, convenciones)
2. Identificar anti-patrones: archivos gigantes, nombres ambiguos, falta de CLIs, docs ausentes
3. Proponer reestructuracion con blast radius estimado
4. Ejecutar cambios de menor a mayor blast radius
5. Verificar que el repo sigue funcional post-cambio (loop closer)
