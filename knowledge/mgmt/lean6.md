---
_manifest:
  urn: urn:mgmt:kb:lean6
  provenance:
    created_by: felixsanhueza
    created_at: '2026-01-29'
    source: Lean Six Sigma reference (complement/lean6.md)
version: 2.0.0
status: published
tags:
- lean
- six-sigma
- quality
- process-improvement
- dmaic
- 5s
- poka-yoke
- kanban
- value-stream
- line-balancing
- knowledge
lang: en
---

# Lean Six Sigma — Core Concepts

ID: LEAN6-KODA-CORE-01 | Source: complement/lean6.md
Warn: Content derived from potentially copyright-protected source; internal use only; verify rights before redistribution.

## Economic Value Added (TOPIC-001)

- Methods optimize processes and directly impact Working Capital (WC = inventories + receivables − liabilities).
- WC reduction → lower financing needs → improved capital profitability and interest expenses.
- Economic value created only when NOPAT (Net Operating Profit After Taxes) covers capital costs.
- WC is determined by: Order-to-Cash (income mgmt), Total-Supply-Chain (inventory mgmt), Purchase-to-Pay (expenditure mgmt). Focus: inventory management.
- Tools that reduce WC: SMED (setup time reduction), Poka Yoke (waste/scrap reduction), Value Stream Analysis (transport/warehouse optimization).

## 5S

### Classification (TOPIC-002)

- 5S: Lean tool for systematically uncovering waste (Muda); named after 5 Japanese terms.
- Beyond tidy workplace: systematic elimination of non-value-adding activities; foundation for further improvements (Total Productive Maintenance, standard work, etc.).
- Prerequisite for other Lean methods.

### Description (TOPIC-003)

5 steps (also "5A" in German literature):

| Step | Japanese | Meaning | Action |
|------|---------|---------|--------|
| 1S | Seiri (Sorting) | Eliminate unnecessary items | Remove unneeded material from workplace |
| 2S | Seiton (Set in order) | Organize/arrange remaining items | Assign fixed location to each item for easy access |
| 3S | Seiso (Shine/Sweep) | Cleanliness | Clean workplace; identify contamination sources |
| 4S | Seiketsu (Standardize) | Maintain and standardize | Fix cleanliness standard; document and implement rules |
| 5S | Shitsuke (Sustain) | Habit/discipline | Internalize as daily routine via audits and visual management |

## Lean Six Sigma

### Classification (TOPIC-004)

- Lean Six Sigma: combination of Lean Management (productivity) + Six Sigma (quality) techniques.
- Goal: higher success through joint planning and enhancement of both dimensions simultaneously.
- Quality improvement and cost reduction are not contradictory.
- Mechanism: systematic, fact-based process analysis eliminates errors and waste.
- Outcome: increased customer satisfaction and company value [refs 1–3].

### DMAIC Cycle (TOPIC-005)

Core element: DMAIC cycle — 5 phases for structured analysis of a defined problem; ensures continuous improvement.

| Phase | Focus |
|-------|-------|
| Define (D) | Define current situation, goals, problem |
| Measure (M) | Determine current state; collect data |
| Analyze (A) | Identify root causes |
| Improve (I) | Select and implement solutions |
| Control (C) | Stabilize optimized process; monitor long-term |

### Define Phase (TOPIC-006)

- Describe current situation; define goals and problem precisely.
- Determine schedule and project organization.
- Create uniform team understanding → detailed project contract.
- Define customer requirements (essential for project success).

### VOC — Voice of Customer (TOPIC-007)

- VOC: completely unfiltered customer statement.
- Process: VOC → measurable criteria → Project Ys (enable measuring project success).
- Methods to capture VOC: market analyses, individual interviews.

### Project Contract (TOPIC-008)

- Document at end of Define Phase summarizing all information.
- Contents: company situation (justifies project need); precise problem statement; goal description (SMART: Specific, Measurable, Achievable, Relevant, Time-bound); project schedule; resource plan; team composition; success metrics.

### Measure Phase (TOPICs 009, 018)

- Goal: determine current state as baseline for improvement.
- Select critical measurement criteria; gather data to evaluate customer requirement fulfillment.
- Data quality is crucial; must be verified before use.

### Measurement System Analysis — MSA (TOPICs 010, 019)

- Data collected by trained individuals using defined tools and uniform methods.
- MSA verifies reliability of measurement system before use.
- MSA checks: Accuracy; Stability; Linearity; Repeatability (same person/tool); Reproducibility (different persons/tools).
- Method: Gauge R&R study (Repeatability and Reproducibility).

### Process Capability Analysis (TOPICs 011, 020)

Key metrics:
- **DPMO** (Defects Per Million Opportunities): error rate from company perspective. Formula: DPMO = (Defects / (Units × Opportunities)) × 1,000,000.
- **DPO** (Defects Per Opportunities): conversion metric for Sigma level. Formula: DPO = Defects / (Units × Opportunities).
- **PPM** (Parts Per Million): error rate from customer perspective. Formula: PPM = DPO × 1,000,000.
- If only one opportunity per unit: DPMO = PPM.

### Process Capability Indices (TOPICs 012, 021)

- **Cp** (dispersion index): relates process spread to tolerance. Formula: Cp = Tolerance / (6 × standard deviation). Does NOT reflect position of mean value.
- **Cpk** (level index): represents process centering; describes mean value position within tolerance range. Cpk ≤ Cp always.
- Cp ≥ 1.33 is commonly required for capable processes.

### Sigma Level (TOPICs 013, 022)

- Convert error rate to Yield: Yield = 1 − DPO (or 1 − DPMO/1,000,000).
- Sigma level read from Z-table using calculated yield.
- Sigma Short Term vs. Sigma Long Term: long-term accounts for environmental influences and wear; typical shift of 1.5 sigma between ST and LT.
- Target: 6 Sigma ≈ 3.4 DPMO.

### Analysis Phase (TOPICs 014, 023)

- Objective: identify root causes of problem; verify that resolving them solves the process problem.
- Two steps: (1) find main influencing variables; (2) determine cause-effect relationships.
- Methods: distribution diagrams, Ishikawa (cause-effect) diagram, correlation analysis, regression analysis, hypothesis tests, FMEA.

### Pareto Diagram (TOPICs 015, 024)

- Bar chart: values arranged largest to smallest (left to right), cumulated.
- Based on Pareto principle: 80% of problems trace to 20% of causes.
- Enables resource focus on highest-impact factors.

### Improve Phase (TOPICs 016, 025)

- Review and concretize impact forecasts with improved data from Measure/Analyze.
- If target not reached: repeat DMAIC cycle.
- Activities: determine optimal input variable and parameter settings considering disturbances; test solution; verify effectiveness; create action plans for implementation.

### Control Phase (TOPICs 017, 026)

- Goal: stabilize optimized process; monitor target level long-term.
- Control system: detects deviations; initiates corrective measures (internal audits, test plans).
- Demonstrate cost savings via before-and-after comparisons.
- Transfer successful findings to other processes (horizontal deployment).

## Poka Yoke

### Classification (TOPIC-027)

- Purpose: prevent errors in assembly through appropriate process design.
- Enables One-Piece-Flow and zero-defect production.
- Based on Shigeo Shingo's Zero-Error-Production concept.
- Key principle: detect and stop errors at source before defective parts are passed downstream.

### Description (TOPIC-028)

Zero-Error-Production (Shingo) — 3 components:

1. **Cause Analysis**: check process in advance for possible incorrect actions (not resulting errors); prevent causes before they produce defects.
2. **100% Inspection**: inspect every part, not just samples; automated where possible.
3. **Immediate Feedback**: detect and stop errors immediately when they occur; no further processing of defective parts.

Poka Yoke device types:
- **Prevention type**: makes incorrect action physically impossible (shape encoding, guides).
- **Detection type**: signals when incorrect action occurs (light, sound, mechanical stop).

### PDCA Cycle — Do Phase (TOPIC-029)

Step 5 — Create action plan: define responsibilities, deadlines, budgets.
Step 6 — Implement action plan: team implements measures; monitor progress and document outcomes.

### PDCA Cycle — Check Phase (TOPIC-030)

Step 7 — Measure effects: verify whether desired effects occurred after implementing action plan; specify degree of goal achievement; analyze deviations in realized vs. planned improvements.

### PDCA Cycle — Act Phase (TOPIC-031)

Step 8 — Standardization and assurance:
- Define standard for the process; train employees on new standard.
- If target not reached: repeat PDCA cycle with refined approach.
- If target reached: document and roll out standard organization-wide.

## Line Balancing

### Classification (TOPIC-033)

- Purpose: eliminate bottlenecks, underutilizations, and waiting times in manufacturing to withstand cost pressure.
- Bottleneck: workstation where cycle time > customer cycle time → limits overall output.
- Goal: balance workstations so no single station becomes a bottleneck.

### Description (TOPIC-034)

- Line Balancing: smooth irregular production orders (quantity and temporal sequence) from customer orders.
- Balance individual workstations so no station creates a bottleneck, limiting overall system throughput.
- Requires actual analysis of the value/process chain first.

### Actual Analysis (TOPIC-035)

Required data: cycle times per activity per workstation; number of activities per workstation; number of workstations; OEE (Overall Equipment Effectiveness).
- Tools: cycle time recording, OEE calculation, work distribution diagram.

### Activities Classification (TOPIC-036)

Every action recorded by time and classified:
- **Value-adding**: directly creates value for customer.
- **Non-value-adding (Muda)**: consumes resources without adding value; eliminate.
- **Necessary non-value-adding**: required by current process design (walking, waiting); minimize.

### Customer Cycle (TOPIC-037)

- Customer Cycle = Available Production Time / Customer Order Quantity.
- Represents maximum allowable time per process step.
- Cycle time > Customer Cycle → bottleneck occurs.
- Cycle time < Customer Cycle → underutilization; excess capacity.

### OEE — Overall Equipment Effectiveness (TOPIC-038)

- KPI combining availability, performance, and quality.
- Formula: OEE = Availability × Performance × Quality.
- Makes total losses visible to employees.
- Used in actual analysis to identify improvement potential.

### Cycle and Takt Time (TOPIC-039)

- **Takt time**: time for a single activity per part at a workstation.
- **Cycle time**: time between successive finished parts leaving a workstation; determines output rate.
- Key for time recording in actual analysis and workstation balancing.

### Work Distribution Diagram (TOPIC-040)

- Visual tool: column per workstation; tasks shown as color-coded bars.
  - Green: value-adding. Red: non-value-adding. Yellow: necessary non-value-adding.
- Customer cycle displayed as horizontal reference line across all workstations.
- Enables identification of overloaded and underloaded stations at a glance.

### Operation List (TOPIC-041)

- Tabular enumeration of all operations in the entire work process.
- Each operation assigned a letter; predecessor operation specified per operation.
- Basis for Network Planning Technique.

### Network Planning Technique (TOPIC-042)

- Circles represent operations (labeled with letters); connected by directed arrows showing dependencies.
- Enables identification of critical path (longest dependency chain; determines minimum process duration).
- Reveals parallelization opportunities to reduce total cycle time.

## Spaghetti Diagram

### Classification (TOPIC-043)

- Tool for analyzing and illustrating waste (Muda) in existing processes.
- Visualizes material flow, information flow, and employee movement paths on a floor plan sketch.
- Used for process analysis alongside value stream analysis.

### Description (TOPIC-044)

- Starting point: floor plan sketch of the work area (clearly defined boundaries).
- Method: observe process ("Gemba Walk" — go to where work happens); draw movement paths on floor plan.
- Result: spaghetti-like path visualization reveals inefficient routing, unnecessary transport, and distance waste.

### Application — 6 Steps (TOPIC-045)

1. Define local dimension (Define): select and bound work area for analysis.
2. Create floor plan sketch with all relevant stations/workstations.
3. Observe process; draw movement paths on floor plan during Gemba Walk.
4. Measure total distances traveled per cycle.
5. Analyze: identify longest paths, loops, backtracking.
6. Redesign layout: propose improvements to minimize total movement distance.

### Advantages and Disadvantages (TOPIC-046)

Advantages:
- No prior knowledge required; immediate recording after layout creation.
- Intuitive: directly shows where waste occurs; easily communicable to stakeholders.

Disadvantages:
- Only quantifies distances, not time or frequency without additional data.
- 2D representation; does not capture vertical movements or multi-level flows.

## Value Stream Analysis

### Classification (TOPIC-047)

- Roots in Toyota Production System (TPS).
- Principle: see the whole to improve the whole; includes analysis beyond production (procurement, shipping, information flows).
- Goal: identify all value-adding and non-value-adding activities for a product family.

### Description (TOPIC-048)

Steps: categorize products → select product/family → customer demand analysis → record current state value stream → identify waste → design future state.

### Product Family Formation (TOPIC-049)

- Value stream is always for exactly one product or product family.
- Method: product-process matrix; group products that share similar process steps and equipment.
- Select product family with highest improvement potential (high volume, frequent problems).

### Customer Needs Analysis (TOPIC-050)

- Goal: orient production towards customer demand.
- Customer cycle (Takt time) derived from customer demand: Available Time / Customer Demand.
- Customer cycle is the pace setter for the entire value stream design.

### Value Stream Recording (TOPIC-051)

Two parallel recordings:
1. Material flow: record upstream (start from customer, go backward against flow direction); document process steps, cycle times, changeover times, inventory levels.
2. Information flow: record from customer order to production control to each process; identify push vs. pull signals.

Combine both into current state map.

### Potential Analysis (TOPIC-052)

- Identify and eliminate the 7 wastes (Toyota Production System, Taiichi Ohno):
  1. Overproduction
  2. Waiting
  3. Transport
  4. Over-processing
  5. Inventory
  6. Motion
  7. Defects/Rework
- Design future state map targeting JIT flow, pull systems, continuous flow, and leveled production.

## Kanban

### Classification (TOPIC-053)

- Muda: any activity consuming resources without creating value; minimize Muda.
- Goal: Just-In-Time (JIT) manufacturing — right parts, right quantity, right time, right place.
- Kanban: demand-pull signal system; production triggered by consumption, not forecast.

### Description (TOPIC-054)

- Developed by Taiichi Ohno, Toyota, 1950.
- Oldest principle of coordinated, self-regulating work systems.
- Supermarket principle: gap on shelf (consumption) triggers replenishment (production/delivery).
- Kanban card = authorization signal; one card per container; no card = no production.
- Establishes pull system: downstream consumption pulls upstream production.

### 1-Card System (TOPIC-055)

- Basic model; suitable when output warehouse of first process can merge with input warehouse of next.
- Single production kanban type; container = production signal.
- Simple; used for short distances between consecutive stations.

### 2-Card System (TOPIC-056)

- Used when source is geographically distant or transport quantity ≠ production order quantity.
- Two card types: Transport Kanban (authorize movement) + Production Kanban (authorize production).
- Transport Kanban: triggers fetch of full container from upstream buffer.
- Production Kanban: triggers refilling of upstream buffer.

### Conditions for Kanban System (TOPIC-057)

- High and consistent quality standard required; defective parts must not enter Kanban containers.
- Stable demand; high demand fluctuations undermine system effectiveness.
- Short and reliable lead times; must define minimum and maximum inventory levels.
- Discipline: every card movement must be tracked; no workarounds.

### E-Kanban (TOPIC-058)

- Addresses deficiencies of manual Kanban: lack of transparency, manual material booking, no IT integration.
- Electronic signal replaces physical card; integrates with ERP/MES systems.
- Benefits: real-time inventory visibility, automatic booking, faster signal transmission, reduced card loss.

### Signal Kanban / Kanban Board (TOPIC-059)

- Variant: batch-based triggering; do not trigger production per empty container but wait until critical order quantity accumulates.
- Traffic light system on Kanban board: Green (produce), Yellow (prepare), Red (stop).
- Enables batch production while maintaining pull discipline.

### Visualization in Kanban (TOPIC-060)

- Key component: enables self-control and transparent performance visibility for employees.
- Tools: Kanban boards (physical or digital), color coding, WIP limits per column.
- Motivational function: employees identify directly with their performance.

### Dimensioning (TOPIC-061)

- Central question: how many Kanbans (control elements) must circulate to ensure reliable material availability?

Number of Kanbans formula:
- N = (Average demand × Replenishment lead time × (1 + safety factor)) / Container quantity
- Parameters: demand quantity per period, replenishment lead time, safety factor (buffer for variability), container/lot size.
- Fewer Kanbans = leaner system but higher risk of stockout; more Kanbans = higher inventory.

### Summary (TOPIC-062)

- Kanban self-regulates production; significantly reduces planning and control overhead.
- Increases production responsiveness; guarantees high material supply security with minimal stock.
- Benefits: reduced WIP, faster throughput, visual process control, improved flow discipline.
