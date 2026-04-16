# Financiamiento del Sistema de Salud Chileno

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes principales**: DFL 1/2005; Ley de Presupuestos; FONASA; DIPRES

---

## 1. Estructura general del financiamiento

### 1.1 Gasto total en salud

- Gasto total en salud: ~9% del PIB [VERIFICAR dato actualizado]
- Gasto público: ~55-60% del gasto total [VERIFICAR]
- Gasto de bolsillo: ~30-35% [VERIFICAR] — alto para estándares OCDE
- Gasto en salud per cápita: [VERIFICAR dato actualizado USD PPP]

### 1.2 Fuentes de financiamiento

| Fuente | Mecanismo | Destino |
|---|---|---|
| Cotización obligatoria (7%) | Trabajadores dependientes e independientes | FONASA o ISAPRE |
| Aporte fiscal | Ley de Presupuestos | Subsidio a FONASA, inversión, programas |
| Copagos | Usuarios FONASA C/D y MLE; usuarios ISAPRE | Prestadores |
| Cotización adicional voluntaria | ISAPRE (sobre el 7%) | ISAPRE |
| Gasto de bolsillo | Medicamentos, prestaciones no cubiertas | Prestadores privados, farmacias |
| Ley 16.744 | Cotización empleador (0.95% + adicional diferenciado) | Mutuales/ISL |

---

## 2. Financiamiento del sector público

### 2.1 Per cápita APS

**Mecanismo principal de financiamiento de la APS municipal.**

- Asignación mensual por persona inscrita en el establecimiento
- **Per cápita basal**: Monto base por inscrito [VERIFICAR monto vigente]
- **Indexadores** que ajustan el per cápita:
  - Ruralidad
  - Pobreza (según indicadores comunales)
  - Proporción de adultos mayores
  - Asignación de zona (comunas extremas)
  - Dificultad para el desempeño

- **Per cápita adicional**:
  - Programas de Reforzamiento de APS (PRAPS)
  - Extensión horaria
  - Salud mental
  - Programa odontológico
  - Chile Crece Contigo

- **Convenios específicos**: Financiamiento adicional por convenio para programas focalizados

**Fórmula simplificada**:
```
Transferencia APS = (Per cápita basal × Indexadores × N° inscritos) + Per cápita adicional + Convenios
```

### 2.2 Programas de Prestaciones Valoradas (PPV)

- Pago por actividad a hospitales de los SS
- Cada prestación tiene un valor de referencia (arancel)
- Programados anualmente según metas de producción
- Incluye: consultas de especialidad, intervenciones quirúrgicas, procedimientos, etc.
- Mecanismo de pago retrospectivo por actividad

### 2.3 Programa de Prestaciones Institucionales (PPI)

- Transferencia global a los SS para financiar la operación de hospitales
- No vinculado directamente a producción
- Cubre: remuneraciones, bienes y servicios, mantención
- Es la base presupuestaria de los hospitales

### 2.4 GES Valorizado

- Financiamiento específico para garantías explícitas
- Canasta de prestaciones valorizada por problema de salud
- FONASA paga al SS/hospital el valor de la canasta GES por cada caso
- Prima GES: componente del 7% que FONASA destina a financiar GES

### 2.5 Ley Ricarte Soto

- Financiamiento fiscal directo para tratamientos de alto costo
- FONASA administra el fondo
- Sin copago para beneficiarios

### 2.6 Presupuesto sectorial

**Partida MINSAL en la Ley de Presupuestos** [VERIFICAR montos]:
- FONASA: ~70% del presupuesto sectorial
- SS: vía transferencias de FONASA
- Subsecretarías: programas, regulación
- CENABAST: intermediación
- Inversiones: Plan Nacional de Inversiones en Salud

---

## 3. FONASA en detalle

### 3.1 Tramos de beneficiarios

| Tramo | Criterio | Copago MAI | Copago MLE |
|---|---|---|---|
| A | Carentes de recursos, no cotizantes | 0% | No accede a MLE |
| B | Ingreso ≤ salario mínimo | 0% | Según arancel MLE |
| C | Ingreso > 1 y ≤ 1.46 SMM | 10% | Según arancel MLE |
| D | Ingreso > 1.46 SMM | 20% | Según arancel MLE |

*SMM = Salario Mínimo Mensual*

### 3.2 Modalidad de Atención Institucional (MAI)

- Atención en la red pública (hospitales y consultorios del SNSS)
- Copago según tramo
- Sin tope de gasto (salvo GES)
- Derivación desde APS

### 3.3 Modalidad de Libre Elección (MLE)

- Atención en prestadores privados o públicos adscritos
- FONASA bonifica un porcentaje según nivel del prestador (1, 2 o 3) y grupo de arancel
- Diferencia la paga el usuario
- Bono de atención electrónico
- No disponible para Tramo A

### 3.4 Protección financiera GES

- **Copago máximo GES**: Definido por decreto según problema de salud y tramo
- **Tramos A y B**: Copago $0 en GES
- **Tramos C y D**: Copago máximo 20% del arancel GES
- **Tope anual**: Existe un tope de copago acumulado anual por familia [VERIFICAR mecanismo actual]

---

## 4. Financiamiento ISAPRE

### 4.1 Cotización

- 7% obligatorio + cotización voluntaria adicional
- El plan de salud debe cubrir al menos las GES al mismo nivel que FONASA
- Excedentes de cotización cuando el plan cuesta menos que el 7%

### 4.2 Planes de salud

- Contratos individuales con cobertura definida (% de bonificación por prestación)
- **Tabla de factores**: Multiplica el precio base según sexo y edad → discriminación por riesgo
- [VERIFICAR] Post-fallo TC y Ley Corta ISAPRE: restricciones a la tabla de factores
- Deducible y topes de cobertura

### 4.3 CAEC (Cobertura Adicional para Enfermedades Catastróficas)

- Cobertura obligatoria para hospitalizaciones sobre un deducible
- ISAPRE cubre el 100% sobre el deducible en prestadores de la red cerrada
- Deducible: [VERIFICAR] ~UF 126 aproximadamente

### 4.4 Fondo de Compensación Solidario GES

- Las ISAPRE aportan a un fondo solidario para financiar las GES
- Redistribuye según perfil de riesgo de la cartera de beneficiarios de cada ISAPRE
- Administrado por la Superintendencia de Salud

---

## 5. Mecanismos de pago a prestadores

| Mecanismo | Descripción | Uso en Chile |
|---|---|---|
| **Capitación (per cápita)** | Pago por persona inscrita, independiente del uso | APS municipal |
| **Fee-for-service (pago por prestación)** | Pago por cada acto realizado | PPV hospitales, MLE, ISAPRE |
| **Presupuesto global** | Transferencia global no vinculada a producción | PPI hospitales |
| **Pago por caso (DRG/GRD)** | Pago por episodio según grupo diagnóstico | GES valorizado; piloto DRG [VERIFICAR estado] |
| **Pago por desempeño** | Incentivo vinculado a metas/indicadores | COMGES, IAAPS |

### 5.1 DRG/GRD en Chile

- GRD (Grupos Relacionados por el Diagnóstico): sistema de clasificación de egresos hospitalarios
- Chile implementó IR-GRD (International Refined GRD) [VERIFICAR versión]
- Uso actual: principalmente como herramienta de gestión y comparación; pago por GRD parcial
- Hospitales codifican egresos; FONASA utiliza para ajustar transferencias [VERIFICAR grado de implementación]

---

## 6. Indicadores de gasto

| Indicador | Descripción |
|---|---|
| Gasto total en salud / PIB | Esfuerzo macroeconómico |
| Gasto público en salud / Gasto total en salud | Proporción pública vs privada |
| Gasto de bolsillo / Gasto total en salud | Protección financiera |
| Per cápita salud (USD PPP) | Comparabilidad internacional |
| Gasto GES / Gasto total | Peso del programa de garantías |
| Gasto APS / Gasto total salud | Priorización de la atención primaria (~25-30%) [VERIFICAR] |

---

## 7. Fuentes

- Chile. DFL 1/2005. Ministerio de Salud.
- FONASA. Cuenta Pública anual. www.fonasa.cl
- DIPRES. Ley de Presupuestos del Sector Público. www.dipres.gob.cl
- OCDE. Health at a Glance (edición más reciente con datos Chile).
- OMS. Global Health Expenditure Database. apps.who.int/nha
- Cid C, Prieto L. "El gasto de bolsillo en salud: el caso de Chile, 1997 y 2007". Rev Panam Salud Publica 2012;31(4):310-316.
