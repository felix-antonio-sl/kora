---
name: loop-closer
description: Cierra el loop de validacion despues de cada cambio de codigo. Usar automaticamente despues de cualquier modificacion de archivos de codigo fuente.
---

# Loop Closer

Despues de cada cambio de codigo, cerrar el loop. Nunca declarar una tarea como terminada sin pasar por este checklist.

## Procedimiento

1. **Build** — Compilar/transpilar el proyecto. Si falla, corregir antes de continuar.
2. **Test** — Ejecutar tests relevantes al cambio. Si no hay tests y el cambio es no trivial, escribirlos.
3. **Lint** — Ejecutar linter si el proyecto lo tiene configurado. Corregir warnings criticos.
4. **Verificar integracion** — El cambio se integra sin romper imports, tipos o dependencias existentes?
5. **Commit** — Commit atomico con mensaje descriptivo. Un cambio = un commit.

## Reglas

- Si el build falla, NO seguir adelante. Corregir primero.
- Si los tests fallan, diagnosticar y arreglar antes de continuar.
- No saltear pasos aunque el cambio parezca trivial.
- Si el proyecto no tiene test runner configurado, declararlo y sugerir setup minimo.

## Gotchas

- Proyectos monorepo pueden tener builds parciales — verificar que el build del paquete afectado pasa.
- Watch mode no cuenta como validacion — ejecutar build/test explicitamente.
- Tests de integracion lentos: ejecutar solo los relevantes, no la suite completa.
