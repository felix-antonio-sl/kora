---
_manifest:
  urn: "urn:kora:agent-bootstrap:custodio-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

- Operador: Felix Sanhueza (operador solitario)
- Contexto: Mantiene y evoluciona el monorepo KORA como unico responsable
- Nivel tecnico: Avanzado (entiende F-coalgebras, KORA specs, CLI)
- Idioma: Espanol (es-CL)

## Rutinas

- Mantenimiento periodico: kora health + kora stats para verificar estado
- Post-ingesta: kora index para sincronizar catalogo despues de agregar artefactos
- Post-agentificacion: kora validate para verificar workspaces nuevos/modificados
- Pre-commit: verificar que no haya URNs rotas ni workspaces incompletos

## Preferencias de Output

- Reportes concisos con tablas
- Severidad explicita (ERROR|WARNING|OK)
- Accion directa sobre diagnosticos extensos
- Confirmar antes de escribir/borrar
- Rutas completas para navegacion rapida
