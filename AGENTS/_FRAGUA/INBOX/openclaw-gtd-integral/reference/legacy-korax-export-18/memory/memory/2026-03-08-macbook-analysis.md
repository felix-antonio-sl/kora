# Análisis MacBook — Marzo 2026

*2026-03-08 02:19 UTC*

## Contexto

Apple anunció nuevos MacBooks el 3-4 marzo 2026. Korvo pidió investigación y recomendación de compra.

## Modelos lanzados

| Modelo | Chip | RAM base | Storage base | Precio Chile | Disponible |
|---|---|---|---|---|---|
| MacBook Neo 13" | A18 Pro | 8GB (fijo) | 256GB | ~$650K* | 11 mar |
| MacBook Air 13" | M5 | 16GB | 512GB | $1.249.990 | 11 mar |
| MacBook Air 15" | M5 | 16GB | 512GB | $1.499.990 | 11 mar |
| MacBook Pro 14" M5 | M5 | 16GB | 512GB | $1.899.990 | 11 mar |
| MacBook Pro 14" M5 Pro | M5 Pro | 24GB | 1TB | ~$2.3M+ | 11 mar |
| MacBook Pro 16" M5 Pro | M5 Pro | 24GB | 1TB | $2.999.990 | 11 mar |

*Neo: precio Chile no confirmado oficialmente.

## Perfil de uso Korvo

- Múltiples terminales (Ghostty, Antigravity) con SSH simultáneos
- Docker containers corriendo
- Apps tipo Excel + Figma a pantalla completa simultáneo
- 2 monitores externos + pantalla nativa (3 pantallas total)
- Carga sostenida diaria

## Análisis comparativo Air 15" vs Pro 14"

| Criterio | Air 15" M5 | Pro 14" M5/M5 Pro |
|---|---|---|
| Monitores externos | 2 + nativa | 2 (M5) o 3 (M5 Pro) + nativa |
| Carga sostenida (Docker+SSH+Figma) | ⚠️ Fanless → throttling | ✅ Ventilador activo |
| RAM máx | 32GB | 32GB (M5) / 128GB (M5 Max) |
| Puertos | 2x TB4 + MagSafe | 3x TB5 + HDMI + SD + MagSafe |
| Pantalla | 500 nits Liquid Retina | 1000/1600 nits XDR + ProMotion 120Hz |
| Batería | 18h | 24h |

## Recomendación final

**MacBook Pro 14" M5 Pro / 24GB / 1TB** (~$2.3M CLP)

Razones:
1. Ventilador activo = sin throttling bajo carga sostenida (Docker + múltiples terminales)
2. 24GB incluidos de fábrica — suficiente para multitarea pesada
3. TB5 + HDMI nativos para monitores sin dock
4. 307 GB/s ancho de banda memoria (vs 153 del M5 base) — impacto directo en multitarea
5. GPU 16 núcleos para Figma y apps gráficas
6. Hasta 3 monitores externos con M5 Pro

**Alternativa presupuesto ajustado:** Pro 14" M5 base / 24GB / 512GB (~$2.1M estimado)

**Descartado:** Air 15" — fanless no soporta el perfil de carga sostenida de Korvo.

## Notas

- Precios de upgrades no visibles aún (configurador deshabilitado en preventa)
- Disponible para compra desde 11 marzo 2026 en apple.com/cl
- Trade In disponible para Mac actual
- Financiamiento hasta 24 cuotas sin interés
