---
name: intent-hospitalization
description: Clasificar solicitudes sobre hospitalizacion integrada identificando escala, modalidad dominante, intencion principal, objeto operativo y tipo de producto. Usar como dispatcher semantico cuando el caso trata sobre hospital, transicion, domicilio o continuidad del episodio.
user-invocable: false
---

# Intent Hospitalization

## Procedimiento

1. Leer la consulta completa.
2. Clasificar la intencion dominante.
3. Identificar escala principal y secundarias.
4. Identificar modalidad dominante y secundarias.
5. Identificar objeto operativo dominante.
6. Si la solicitud es de producto, identificar tipo de producto.
7. Si no alcanza para distinguir intencion, escala o modalidad, marcar `clarificacion_requerida = true`.

## Salida esperada

- `escala`
- `modalidad`
- `intencion_primaria`
- `objeto`
- `tipo_producto`
- `escalas_secundarias`
- `modalidades_secundarias`
- `clarificacion_requerida`
- `motivo_ambiguedad`
