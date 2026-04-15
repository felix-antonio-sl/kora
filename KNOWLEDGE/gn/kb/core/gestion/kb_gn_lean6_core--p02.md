---
_manifest:
  urn: urn:gn:kb:lean6-gestion-core-p02
  provenance:
    created_by: felixsanhueza
    created_at: '2026-03-15'
    source: source/gn/gorenuble_koda/core/gestion/kb_gn_lean6_core_koda.yml
version: 1.0.0
status: published
tags:
- lean-six-sigma
- mejora-continua
- optimizacion-procesos
- manufactura
- calidad
- dmaic
- kanban
- value-stream
lang: en
extensions:
  gn:
    family: guide
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:lean6-gestion-core
---

# Lean Six Sigma: Core Methods and Tools - Parte 02

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
