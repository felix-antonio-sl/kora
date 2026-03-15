---
_manifest:
  urn: "urn:gn:kb:lean6-gestion-core"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-03-15"
    source: "complement/lean6.md"
version: "1.0.0"
status: draft
tags: [lean-six-sigma, mejora-continua, optimizacion-procesos, manufactura, calidad, dmaic, kanban, value-stream]
lang: en
extensions:
  gn:
    family: "guide"
---

# Lean Six Sigma: Core Methods and Tools

## Summary

Lean Six Sigma combines Lean Management (waste elimination, flow) with Six Sigma (defect reduction, statistical quality) into a holistic approach for process optimization. The core framework is the DMAIC cycle (Define, Measure, Analyze, Improve, Control), applicable across production structures. The methods presented directly impact Working Capital and company value via inventory reduction and operational efficiency.

## Economic Value and Working Capital

Economic value is created when Net Operating Profit After Taxes (NOPAT) exceeds capital costs. Capital costs are composed of fixed assets, Working Capital (WC), and the capital cost rate.

**Working Capital formula:**
- WC = Current Assets − Current Liabilities
- WC represents liquidity (current assets convert to cash faster than fixed assets) and financing needs.
- Reducing WC decreases financing needs, improves capital profitability, and reduces interest expenses.

**WC-influencing processes:**
- Order-to-Cash (income management)
- Total-Supply-Chain (inventory management)
- Purchase-to-Pay (expenditure management)

Methods such as SMED (setup time reduction), Poka Yoke (defect prevention), and Value Stream Analysis (transport/warehouse optimization) reduce inventory and thus WC.

## 5S: Workplace Organization

### Classification

5S is a Lean tool for systematically uncovering waste. It is not merely a housekeeping method—it is the foundation of every Lean management approach and a prerequisite for PDCA methodology.

### Five Components

| Step | Japanese | Meaning | Purpose |
|------|----------|---------|---------|
| 1 | Seiri | Sort | Remove unnecessary items; eliminate excessive circulating stocks, surplus/defective tools, unneeded documents |
| 2 | Seiton | Set in order | Create visible order; ergonomic placement of work equipment at defined, standardized locations |
| 3 | Seiso | Shine | Maintain cleanliness; enables faster error detection; prevents quality defects from dirt/foreign bodies |
| 4 | Seiketsu | Standardize | Standardize work processes; employees trained until standard maintained without documents (not fastest induction, but highest quality) |
| 5 | Shitsuke | Sustain | Continuously apply and improve; employees develop Muda-elimination suggestions; initiate CIP |

## Lean Six Sigma: DMAIC Methodology

### Classification

Lean Six Sigma combines productivity-enhancing Lean measures with quality-focused Six Sigma measures. Quality improvement and cost reduction are not contradictory—errors and waste are eliminated through systematic, fact-based process analysis.

### DMAIC Overview

| Phase | Target | Six Sigma Tools | Lean Tools |
|-------|--------|-----------------|------------|
| DEFINE | Identify customer requirements; determine financial impact; define participants; consider process influences; coordinate changes | Project profile, VoC, QFD, Kano model; Stakeholder analysis; SIPOC; Communication plan | Value added analysis |
| MEASURE | Map process; identify quality-critical influences; prepare/measure data; determine process capability and sigma level | Quality tree (CTQ); Data collection plan, sample survey; Quality control chart, process capability analysis | Value stream analysis, cycle time diagram |
| ANALYZE | Root cause analysis; compare process performance with best practice | FMEA, DoE, Brainstorming, Ishikawa diagram, hypothesis tests, regression analyses; Benchmarking | Seven types of waste, 5x Why (5W) |
| IMPROVE | Determine improvement starting points; implement improvement actions; install continuous improvement routine | Evaluate and select suitable tools; Simulation, piloting | 5S, SMED, Kanban, TPM; Kaizen (KVP) |
| CONTROL | Long-term safeguarding of results | PDCA, quality plan, project repetition plan | SOP, Poka Yoke |

### Define Phase

Describes the current situation and precisely defines goals and the problem. Key activities:
- Determine schedule and project organization.
- Create a detailed project contract.
- Define customer requirements (essential for project success).

**Voice of the Customer (VOC) cascade:**
- VOC (unfiltered customer statement)
- Customer requirements (list of needs)
- CTQs—Critical to Quality (measurable criteria with direct influence on output success)
- Project Ys (apex measurable outcomes)

**Project Contract contents:** company situation, problem statement, SMART goal description (Specific, Measurable, Attainable, Relevant, Time bound), financial effect, project team with assigned responsibilities.

### Measure Phase

Determines the current state as basis for process improvement. Critical measurement criteria selected; data quality verified through Measurement System Analysis (MSA).

**MSA characteristics checked:**
- Accuracy
- Stability
- Repeatability
- Reproducibility
- Resolution: ≤ 5% of tolerance

**Attributive MSA requirements:** ≥ 2 appraisers; ≥ 30 numbered parts (good and defective); each appraiser measures all parts twice in random order; goal = 100% match with reference value; minimum acceptable = 90%.

**Process Capability Metrics:**

| Metric | Perspective | Definition |
|--------|-------------|------------|
| DPMO (Defects Per Million Opportunities) | Internal/Company | Relates defects to number of error opportunities; softer metric |
| DPO (Defects Per Opportunities) | Internal | Used to convert to Sigma level |
| PPM (Parts Per Million) | Customer | Only counts defective units; sharper metric; used in automotive industry |

Note: DPMO and PPM are equal only when there is one possible error per unit. PPM is the sharper metric for actual quality evaluation; DPMO is preferred for internal comparison across complex systems.

**Process Capability Indices:**
- Dispersion index (Cp): relates process spread to tolerance. Necessary but not sufficient for high process sigma.
- Level index (Cpk): describes position of mean value within tolerance. Minimum value of 1.5 required for Six Sigma compliance.
- If mean shifts, Cpk changes (e.g., from 2.0 without shift to 1.5 with shift); Cp does not change.

**Sigma Level determination:**
- Convert error rate to Yield.
- Read Sigma level from Z-table.
- Sigma Short Term: does not account for external influences.
- Sigma Long Term: adds 1.5 sigma shift to account for environmental influences and wear.
- When determining via DPMO: outputs Sigma Long Term. Via Z-table of normal distribution: Sigma Short Term.

### Analysis Phase

Objective: Identify root causes and verify their resolution solves the process problem.

Two steps:
1. Find main influencing variables.
2. Determine cause-effect relationships.

**Common methods:**
- Distribution diagrams
- Cause-effect diagram (Ishikawa)
- Pareto diagram
- Flow diagrams
- Control Charts
- Regression analyses
- Hypothesis tests
- Design of Experiment (DoE)

**Pareto diagram:** Bar chart with values arranged largest to smallest, cumulated left-to-right. Based on Pareto principle: 80% of problems trace back to 20% of causes.

### Improve Phase

Reviews and concretizes impact forecasts. If results do not reach target level, DMAIC cycle is repeated.

Activities:
- Determine how process input variables and parameters should be set, considering disturbance variables.
- Test solution and check effectiveness.
- Create action and measure plans for sustainable implementation.

Solution evaluation criteria: cost-benefit ratio, degree of difficulty, implementation time, possible risks.

### Control Phase

Stabilizes the optimized process and monitors long-term results.

- Control system recognizes deviations and initiates corrective measures (internal audits, test plans).
- Demonstrate cost savings via before-and-after comparison using optimized rejects.
- Communicate findings company-wide so other projects benefit.
- After project completion, enter continuous improvement process (CIP) directly.

## Poka Yoke: Error Prevention

### Classification

Poka Yoke (invented by Shigeo Shingo at Toyota, 1961; renamed from "Baka Yoke" = foolproof, to "Poka Yoke" = avoidance of unintentional errors) prevents errors in assembly through appropriate process design. Principle: error source prevention—no errors can occur without an error source.

### Zero-Error-Production: Three Components

1. **Cause Analysis:** Check the process in advance for possible incorrect actions (not resulting errors) and their causes. Analyzing actions—not just errors—enables higher avoidance.
2. **100% Inspection:** All parts checked for potential incorrect actions, or the process designed to prevent the incorrect action. Economic 100% inspection is possible due to simplicity of facilities.
3. **Immediate Corrective Actions:** System designed so errors are not allowed; corrective measures initiated immediately.

### PDCA Integration

**Do Phase (Steps 5–6):**
- Step 5: Create action plan (responsibilities, deadlines, budgets).
- Step 6: Implement action plan; control and document progress and quality.

**Check Phase (Step 7):**
- Measure effects after all activities implemented.
- Specify degree of goal achievement.
- Deviations can trigger new PDCA iteration; pay special attention to implementation of planned measures in next iteration.

**Act Phase (Step 8):**
- Define a standard for the respective process.
- Conduct employee training if needed.
- Audits ensure long-term guarantee of process improvement.

## Line Balancing

### Classification

Line Balancing optimizes the value chain by eliminating waste. Goal: trim the production chain to flow production (One-Piece-Flow) and the TPS pull principle. Core concept: align cycle times of all workstations to customer demand (Takt time).

- If station time > customer cycle → bottleneck (WIP inventory builds).
- If station time < customer cycle → overproduction.

Origins: Toyota Production System (TPS); mathematical foundations from M.E. Salveson's "assembly line balancing problem."

### General Procedure

1. **Actual Analysis** — capture current, non-optimized production process.
2. **Waste Elimination** — identify and eliminate 7 (or 8) types of waste.
3. **Work Redistribution (Cycling)** — adapt all workstations to required customer demand.
4. **Standardization** — standardize improvements to ensure sustainability.

### Key Concepts for Actual Analysis

**Activities categories:**
- Value-adding activities (e.g., turning, welding, screwing)
- Necessary but non-value-adding activities (e.g., set-up, emptying containers)
- Non-value-adding activities (e.g., waiting, searching, rework)

**Customer Cycle:** Available production time ÷ customer order quantity. Represents the time limit for each process step.

**OEE (Overall Equipment Effectiveness):** Key figure combining units, speed, production time, and quality. Represents total losses; defined against ideal plant performance (no interruptions, no quality loss, maximum speed).

**Cycle Time vs. Takt Time:**
- Takt time: time for a single activity per part at a workstation.
- Cycle time: time in which a finished part leaves the work system.
- Required Cycle Time = Customer Takt ÷ OEE (compensates for loss factors; always lower than Customer Takt because OEE < 100%).

### Analysis Tools

**Work Distribution Diagram (AVD):** Color-coded column chart per workstation.
- Green: value-adding tasks
- Red: non-value-adding tasks
- Yellow: necessary tasks
- Blue: periodic tasks
- Upper dashed line = Customer Takt; lower line = Required Cycle Time.

**Operation List:** Tabular enumeration of operations. Contains: operation letter, predecessor activity, duration. Forms the basis for network planning.

**Network Planning Technique:** Circles (operations) connected by arrows (order); rectangles on each circle show duration. Describes temporal and final chaining of actions.

## Spaghetti Diagram

### Classification

The Spaghetti Diagram analyzes and illustrates waste (Muda) in existing processes, specifically the waste types "transport" and "movement." Part of process analysis tools; reduces throughput times and increases functional flexibility.

### Application: Six Steps

1. **Define local dimension:** Select and define work area (clear start/end point); create scale layout (existing floor plans + Gemba walk to verify).
2. **Define temporal dimension:** Determine observation period (sufficient for reliable analysis; cover all shifts if applicable; use different colors per shift for comparison).
3. **Determine observation object:** Define what to analyze—employee paths, material paths, or document flow.
4. **Draw process flow (Record):** Draw all paths taken into layout exactly; record repeated paths as well.
5. **Evaluate the diagram (Analyze):**
   - Quantitative: measure distances from scale drawing.
   - Qualitative: assess tangled lines (high frequency, long lines, frequent crossings indicate waste).
6. **Define measures (Perform) and prioritize:** Classify by integration effort; implement "quick-wins" first; re-evaluate layout changes after quick-wins.
7. **Iterate:** Repeat recording to check implemented measures; compare quantitatively.

### Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| No prior knowledge required | Quickly becomes unclear for large processes |
| Visualizes process execution | Difficulty evaluating many routes |
| Focuses specifically on Transport and Motion waste | Define phase critical to limit complexity |

## Value Stream Analysis

### Classification

Value Stream Analysis originates in the Toyota Production System (TPS). Purpose: holistic transparent representation of processes to eliminate waste, improve responsiveness, increase profitability and efficiency. Focus: optimizing throughput times while increasing production flexibility for different products per customer specifications.

### Procedure Overview

1. Categorize products (select product family for analysis).
2. Conduct customer demand analysis (based on prior fiscal year sales figures).
3. Record actual value stream.
4. Analyze potential improvements.

### Product Family Formation

One value stream = processes for exactly one product. Use a product family matrix or production process/product family similarity evaluation to group products into families (segments separated from factory for analysis).

### Customer Needs Analysis

**Customer Cycle formula:** Available production time ÷ customer order quantity.

- Too high cycle time → non-fulfillment of customer demand.
- Too low cycle time → overproduction.

For high demand fluctuations: either decouple production by creating stocks, or influence ordering behavior upstream (e.g., quantity/time-limited discounts).

### Value Stream Recording

- Start with material flow recording (upstream direction: start from customer, go opposite to material flow).
- Record information flow starting at customer order acceptance.

**Timeline (jump line):** Two levels below drawing.
- Upper level: material flow (storage range).
- Lower level: process (processing time).
- End: total throughput time + sum of processing times.

**Cycle Coordination Diagram:** Bar chart of cycle times across entire value stream. Largest bar = bottleneck. Customer Cycle entered to visualize capacity gaps.

### Seven Types of Waste (Taiichi Ohno / TPS)

| Waste Type | Cause / Mechanism |
|-----------|-------------------|
| Overproduction | Quantity produced exceeds demand; conditions other wastes; often from excess batch sizes |
| Inventories | High capital commitment, increased storage space; conceals production problems |
| Transport | Spatial separation of successive steps; poor layout; necessary intermediate storage |
| Movement | Unnecessary employee distances; poor ergonomics; secondary activities |
| Waiting times | Lack of material, machine downtimes, poor takt time across processes |
| Production process | Excessive setup/travel times; setup time itself = non-value-adding |
| Errors | Faulty parts requiring rework or removal |

## Kanban: Pull-Based Production Control

### Classification

Kanban ensures Just-In-Time manufacturing: right parts at the right time, in required quantity, at the right place. Globally used control method; reduces complexity, low susceptibility to interference, decentralized with reduced control effort.

Developed by Ohno in 1950. Based on the supermarket principle: a gap created by consumption must be filled by the upstream process.

### Information and Material Flow

- Information flow: backwards along Kanban line.
- Material flow: forward until required product completed.
- Customer order triggers from finished goods warehouse, propagating backwards through chain.

**Push vs. Pull distinction:** In Kanban (Pull), only the removed quantity is refilled. In Push, upstream process produces based on schedule regardless of downstream demand.

### Kanban Card Types

| Type | Circulation | Function |
|------|-------------|----------|
| Production Kanban | Between source and buffer storage | Contains container data, transport routes, delivery time, parts info; triggers production orders at source |
| Transport Kanban | Between buffer storage and consuming point | Triggers transport to supply consuming point from buffer storage; functions as order form if supplier included in system |

### 1-Card System

For short distances between processing stations where output and input warehouses can merge. One card serves dual function (transport + production). Empty container removal passes card to upstream process → triggers production order → removed quantity refilled.

### 2-Card System

Used when container must be fetched from a distant location, or when transport quantity differs from production order quantity.

Flow:
1. Consumer (sink) empties container.
2. Employee takes transport kanban + empty container to buffer storage.
3. Employee exchanges production kanban (on full container) with transport kanban; places production kanban in collection box.
4. Source collects production kanbans and produces.
5. Full containers returned to buffer storage.

Transport kanban regulates information flow; production kanban regulates material flow.

### Prerequisites for Successful Kanban

- High quality standard with appropriate QA measures (prevent faulty parts entering containers).
- Production only initiated by Kanban card receipt (no demand = no production).
- Only exact requested quantity produced (prevent overproduction).
- Standardized and stable production (frequent machine failures can halt entire line).
- Material flow must follow flow principle (avoid strong demand fluctuations).
- Short setup times for economical high-variety production.
- Variants with similar processing sequence preferred.

### E-Kanban

Physical Kanban cards with barcodes; scanning transfers data to IT system. Enables:
- Digital viewing of container quantities in company network.
- Simpler supplier connection (automatic order on "empty" status; delivery scanned on acceptance).
- Accurate material consumption booking; better order prioritization.
- Product tracking documentation.
- RFID (Radio Frequency Identification) as alternative Auto-ID technology.

### Signal Kanban (Kanban Board)

Traffic light system for batch-order bundling:

| Zone | Meaning |
|------|---------|
| Red (bottom) | No production yet |
| Yellow (middle) | Optional—decide based on workload |
| Green (top) | Sufficient cards accumulated → begin production |

Advantage: visualization of material flow control impulses and transparency.

### Kanban Dimensioning

**Number of Kanbans formula:**
- Parameters: parts per Kanban (PK); replenishment time (RT); safety stock (SS); safety factor (SF); average (or maximum for fluctuating demand) consumption.
- Safety factor should be reduced to 1 as quickly as possible (excess = waste in Lean context).
- Initial inventory = starting size when production stopped for extended period.
- Simulate system before introduction.

### Kanban Summary

| Advantage | Limitation |
|-----------|------------|
| Significantly reduces planning and control effort | Workplace disruption leads directly to production standstill |
| Greatly increases production responsiveness | Cannot compensate strong demand fluctuations |
| High supply security with minimal stocks | — |
| Simple, understandable, high employee involvement | — |
