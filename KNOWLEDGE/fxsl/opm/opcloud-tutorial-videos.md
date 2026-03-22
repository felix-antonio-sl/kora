---
_manifest:
  urn: "urn:fxsl:kb:opcloud-tutorial-videos"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-22"
    source: "source/fxsl/opm-methodology/opcloud-tutorial-videos.md"
version: "2.1.0"
status: published
tags: [opcloud, opm, tutorial, modelado, video-course, cloud-tool, simulation]
lang: en
extensions:
  kora:
    family: tutorial
    video_count: 50
---

# OPCloud Tutorial Videos

OPCloud is the dedicated cloud-based software for Object-Process Methodology (OPM) modelling. It provides bimodal graphic-text editing: OPL sentences are generated automatically as OPDs are constructed. This tutorial covers the complete OPCloud workflow based on a 50-video course using the OnStar system as primary example (emergency assistance, GPS navigation, cellular communication, advisor interaction).

For OPM formal specification, notation and methodology, see `urn:fxsl:kb:opm-iso-19450`.

---

## Getting Started

### Creating Objects and Processes

- **Create process**: click process button in main toolbar (blue ribbon) → drag to canvas → enter name in popup → click Update or press Enter
- **Create object**: click object button → drag to canvas → enter name → Update/Enter
- **Create link**: click empty area (non-text part of element), drag to target element
- **Auto Format**: toggle checkbox to auto-capitalize each word; disable for custom naming (e.g., "onstar" instead of "OnStar")
- **Auto Capitalization**: default behaviour capitalizes the first letter of each word

### Saving and Loading Models

Main toolbar buttons: Undo, Redo, Save, Load, Share, Execution (simulation mode).

Main Menu: Create new model, Load model, Load examples (Global — all users; Organizational — admin-created). Save options: Quick save (current location), Save as (new location/rename).

**Model Options** (Main Menu):
- System map — visual overview of all OPDs
- Copy link — shareable model URL
- **Model validation** — validate computational values and ranges
- **Compare models** — diff two model versions
- Mark things — colour-code elements for team visibility

**Auto Save**: models save automatically on tab switch. Unsaved indicator shows "not saved" until first save.

### Model Navigation

- **OPD Navigator**: left pane tree view of all diagrams
- **Draggable Things panel**: all elements with type indicators — (i) Informational, (P) Physical, (E) Environmental, (S) Systemic. Drag elements directly to canvas.
- **Connected Things**: sub-view within Draggable Things showing attributes connected to their parent elements (e.g., danger status connected to driver). Displays hierarchical attribute-exhibitor relationships, not just flat element list.
- **Keyboard shortcuts**: Ctrl+Up → parent OPD, Ctrl+Down → child OPD
- Zoom in/out + drag to reposition

### Model Wizard

Access: Main Menu > New Model by Wizard. Implements the OPM SD construction procedure (see `urn:fxsl:kb:opm-iso-19450` § SD Construction Procedure) as a guided 12-stage interactive workflow.

**Help features**: hover hints on UI elements, assistant tooltips on bold items. Example model: OnStar system.

**12 Stages:**

| Stage | Wizard prompt | User action | OPM element created |
|-------|--------------|-------------|---------------------|
| 1 | System's main functionality | Write name of main process (must end in "-ing") | Main process (ellipse) in SD |
| 2 | Beneficiary group | Name the beneficiary (singular; "Set" for inanimate, "Group" for humans) | Beneficiary object (rectangle) |
| 3 | Beneficiary attribute | Name the attribute that describes how the beneficiary benefits | Attribute object (exhibition-characterization link) |
| 4 | Input/output states | Define input state (current, problematic) and output state (desired, satisfactory) of the attribute | States (rountangles) inside attribute + input-output effect link pair |
| 5 | Agent | "Is the beneficiary also the agent?" If not, name agent(s). Max 3, separated by Enter | Agent object(s) + agent link(s) (black lollipop) |
| 6 | System name | Default: main process name + "System". Or define custom name | System object (instrument of main process) |
| 7 | Instruments | Name instruments required for the process. Max 3, singular, Enter-separated. Select physical ones | Instrument objects + instrument links (white lollipop) |
| 8 | Inputs | Name objects consumed by the process. Max 3, Enter-separated. If affected → must also be output | Consumee objects + consumption links |
| 9 | Outputs | Select whether output is also an input. Name output objects | Resultee objects + result links |
| 10 | Environmental objects | Select from previously defined objects or add new | Environmental objects (dashed contour) |
| 11 | Connections | Review and adjust links between all elements | Link verification |
| 12 | Review | Final SD overview with OPD + OPL | System Diagram complete |

**Produces**: a complete System Diagram as top-level entry point with OPD + corresponding OPL paragraph.

**Limitations**: does not cover all OPCloud features (computational objects, simulation, templates, sub-models, etc.). Manual extension required after completion. Not all link types available in wizard — only basic transforming and enabling links.

---

## Core Features

### OPD3 and Diagram Management

OPDs auto-generate when using in-zoom or unfold. Naming convention: SD (top), SD1, SD1.1, SD1.1.1.

**Deletion rule**: only leaf nodes are deletable — inner nodes protected to maintain tree integrity. Error message on inner node deletion attempt.

Expand/collapse via right-click: expand all, collapse all, hide/show names. **Partial expansion**: models with >20 OPDs show only current level expanded by default.

### Searching Elements

Secondary toolbar > search button. Filter: all elements, processes only, objects only. Results show Location column (OPD where element exists). Click location → navigate to OPD and focus on element. Right-click in Draggable Things panel to filter by element name.

### Objects and Processes

Four essence types: Physical (tangible), Informational (abstract data), Environmental (external factors), Systemic (control systems). Change essence via secondary toolbar button.

- **Description**: add text, URLs, notes via double-click
- **URL links**: entities extension > view URL (images, videos, articles)
- **Unfold**: creates child OPD showing sub-components
- **Fold**: compact view with bold contour indicator
- **Update Button**: confirms name edits after modification
- **Inside objects**: created within in-zoom processes, exist only in process scope, **deleted when parent process deleted**
- **Outside objects**: created at system diagram level, exist independently, referenceable across OPDs
- **Conversion**: delete and recreate, or copy from Draggable Things to target location
- **Enveloping**: process enlargement can "swallow" outer objects (appear inside but revert when moved)

### States

Add via halo > add states OR secondary toolbar button. Default naming: state1, state2 (lowercase, left to right). **Exchange Symbol** toggles between effect link and in-out link pair. Clicking Update advances automatically to next state name.

- **State Examples**: `"requested call"`, `"online"` for a call object
- **Conditional Transitions**: states can connect to processes via instrument-condition links
- **Multiple States**: additional states created by repeating the add-state action

### Links and Connections

Create link: right-click source → drag to destination. Link Table: configure properties, multiplicity, tags, path probability.

- **Agent Links**: connect human agents to processes
- **Instance Links**: create specific instances of objects
- **Specialization**: represent generalization relationships between things

**Visual Instances**: same logical entity with different visual representation in different OPDs.
- Create with "use existing thing" option on naming conflict
- **Restriction**: cannot create visual instance between different element types (object → process forbidden)
- Visual instance = same thing, different view. Logical instance = inheritance relationship (classification-instantiation)

### Link Properties

Link properties: right-click link > properties. Source/target multiplicity, tag, path probability, style. Link style: colour (hex), width; copy style to other links.

### Advanced OPL Panel

Shift Pane: move OPL panel to left side. Toggle numbering on/off. **Minimize Panel**: stop rendering OPL for better performance on crowded diagrams. **Manual editing**: direct OPL script modification available.

### Touch Screen Support

Long press as alternative to right-click. Gesture-based OPD navigation. See user manual for complete gesture list.

### Inner and Outer Objects

- **Inner Objects**: created inside in-zoom processes; exist only within process scope; deleted when parent process is deleted
- **Outer Objects**: created at system diagram level; can be referenced across multiple OPDs
- **Conversion Methods**: delete/recreate or copy from Draggable Things into the target context
- **Drag Behavior**: dragging an outer object inside a process raises a warning
- **Visual Indicator**: inner objects use inside-process notation
- **Enveloping**: process enlargement can visually swallow an outer object, but the object reverts when moved

---

## Advanced Features

### Halo and Quick Commands

Click element → show halo (three dots near selection). Commands:
- Unfold/In-Zoom: navigate to or create child OPD
- **Convert to Computational**: change to calculation-capable process
- Delete: multi-instance handling (shows all instances for selection)
- **Time Duration**: set process duration for exception links
- Style Element: quick visual customization
- **Bring Connected**: load related elements from other OPDs
- Secondary toolbar provides same options

### Semi-Folding

View object parts without overcrowding. Activation: select object > semi-folded view. Compact view shows part names inside object container. **Extract Part**: double-click specific part to bring to main diagram. **Missing Parts Indicator**: number on link (e.g., "2 more") showing hidden parts. Restore: click link icon. Semi-folded shows names only; full unfold shows complete details.

### Text and Style

Style options: Reset, Font Size, Font Family, Text Color, Border, Alignment (left/center/right). Manual Positioning: X/Y control for precise text placement. Position presets: up, down, left, right, center. Link style via right-click > style > colour (hex), width. Copy Style to other links.

### Resizing and Auto-Size

OPCloud has default minimum size for elements. **Fit to Text**: entities extension > shrink to text (maintains auto-resizing). **Toggle Auto-Sizing**: entities extension > disable for manual resize, re-enable for automatic. With auto-sizing disabled, text cannot exceed element bounds.

### Grid Feature

Secondary toolbar > grid option. Default: off. Settings: Size (pixel increment, default: 5), Colour, Thickness, Scale Factor (higher = fewer lines). Critical for in-zoom process ordering — process height determines execution order in OPM.

### Images in Things

Three sources: **URL** (must end in .jpg/.jpeg/.png/.gif), **Heading Pool** (internal OPCloud library), **OPD Capture** (screenshot of current diagram). Display: show text+image simultaneously or toggle text-only/image-only. Camera icon indicates embedded image. Cycle multiple images with clicks. Preview before embedding.

---

## Model Management

### Export Options

- **Export OPL**: text with/without numbering
- **Export OPD as image**: JPEG or GIF, 100 DPI (default) or 300 DPI (high quality). Scope: current OPD, entire OPD tree, or system diagram only. Option to show computational process tooltips.
- **Export PDF**: include model URL, choose OPD range (specific or full), quality options
- File naming: default = model name; custom names supported

### Model Templates

Access: secondary toolbar > insert template. Three tiers: Private (user), Organizational (admin), Global (system admin). Preview: hover for system diagram popup. Load: insert button or double-click. Multi-OPD templates insert under current OPD as child diagrams. Folder support for organization. **Template updates do NOT propagate** — changes to source template do not update inserted copies.

### Organization Ontology

Enforce consistent terminology. Three enforcement levels: None, Suggest (popup suggests correct term, current default), Enforce (prevents non-standard terms). Click suggested term → auto-replace. Admin setup: Settings > Organization Management. Enforcement config: OPCloud Settings > Ontology Enforcement Level.

### Name Coherency

Warning on duplicate names. Dialog shows where existing item is located. Options: Use existing thing (create visual instance), Rename, Close (not recommended). Visual instance restriction: same element type only.

### Model Permissions

Share options: read (view-only), edit (writable). Group sharing: select entire group or specific users. **Cannot share across organizations**. Owner icon: key. Edit token: pen icon (current editor). Permission hierarchy: read required before write. Admin/owner override available.

### Moving Models

Cut/Paste workflow: (1) open load menu → (2) select model → (3) cut → (4) navigate to destination → (5) paste → (6) confirm warning. Move includes auto-save and version history. Show Versions toggle alongside model.

### Sub-Models

Concurrent work on subsystems by different modellers. Keep main-submodel connections minimal. Creation: select subsystem element > create sub-model. First implementation with planned enhancements. Scope: subsystem separation, not full model branching.

---

## Settings and Preferences

### User Settings

Access: Main Menu > User Settings OR gear icon near modeller name.

- Profile: name, address, access level
- Password reset via email (not available for SSO users)
- **OPL Language**: Chinese, French, German, Korean, and more (continuously expanding)
- Thing's Default Essence: Physical (default) or Informational as organizational default
- OPL Display: all sentences or only non-default essence
- Units Display: always / hide / only when applicable
- Alias Display: toggle visibility
- Numbering: toggle on/off

### Model Settings

**OPD3 Arrangement**: Automatic (tree reorders based on in-zoom process order) or Manual (user controls exact ordering). Organization defaults inherited from admin; user can override. Access: Settings > OPCloud Settings.

---

## Integration Features

### MQTT Protocol

Connect to IoT devices (Arduino, ESP8266, ESP32). Configuration: Settings > configure MQTT server (default: localhost:1883). Define publish/subscribe topics for sensor data. Example: Optimal Light Power Consumption — LDRs + microcontroller + room light, power = average of two sensors, self-invocation for continuous monitoring loop. Setup requires raw server AND MQTT server in preferences.

### ROS Connection

Connect to Robot Operating System. Requires ROS knowledge and architecture understanding. Create and publish messages to ROS master. Subscribe to ROS topics. Example: Turtle Scene (standard ROS example). Workflow: (1) define message creation → (2) publish to ROS master → (3) monitor feedback loop → (4) handle conditions and iteration counters. Messages connect to actual robot for real-world control.

---

## Simulation and Execution

### Conceptual Simulation

Access: main toolbar > simulation/execution button. Animation speed slider (default: 1 second/operation). Token flow visualises process execution with moving tokens. Tokens follow in-zoom hierarchy top → bottom. **Conceptual = visual simulation; Execution = actual calculations**. Common issue: process execution order may need adjustment.

### Computational Objects and Processes

Convert via halo or computation option. Value types: integer, float, string, character, boolean. Define measurement units. Alias: short name for calculations (e.g., "o1"). Predefined functions: addition, subtraction, multiplication, division, average, custom. Tooltip indicates computational nature. Computation process shows **braces {}** in diagram.

### Advanced Calculations

**Stereotypes**: parameter type templates. Global (G icon, all users) vs Organizational (no icon, admin-created). Components: sub-parameters with ranges per element.

**User-Defined Functions**: custom calculations integrated via API. OPCloud provides built-in functions accessible in the calculation dropdown.

**Point-Slope example** (canonical computational workflow):
1. Define two Point objects (e.g., Point1, Point2)
2. Set X and Y as **computational attributes** on each Point (type: float, with aliases e.g. "x1", "y1", "x2", "y2")
3. Create a **calculation process** (shows braces `{}` in diagram)
4. Define the formula using the aliases (e.g., slope = (y2-y1)/(x2-x1))
5. The calculation process consumes/affects the point objects and yields the result

This workflow demonstrates the pattern: stereotype defines the parameter structure → computational attributes hold values → calculation process applies the formula.

### Range Validation

Setup: entities extension > set range. Inclusion/exclusion brackets: `[inclusive`, `(exclusive`. Multiple ranges: `[1,10][20,30]`. State indication shows active range. Auto-created "type" attribute with range options. System enforces valid ranges during simulation.

### Conditions and Loops

Connect states to processes via instrument-condition links. Loops via invocation links. Yes/No states for binary decisions; multiple states for complex conditions. Process completes when condition unmet.

**Iteration tracking**: process states can track the **iteration count** (how many times the loop has executed) and completion status. Monitor these during simulation to debug loop behaviour.

**Visual indicators**: links display their **condition type** visually in the diagram — the "c" or "e" annotation is visible on the link, helping distinguish conditional from non-conditional paths at a glance.

### User Input in Simulation

**Agent requirement**: user must be connected via agent link to process.

Workflow:
1. Create user as physical object
2. Connect user to process via **agent link** (black lollipop)
3. Mark process to "get user input" during simulation
4. Create computational input object to receive user values
5. Connect process to input object via **effect link** (bidirectional arrowheads) — required link type for updating computational objects with user-provided values
6. In the computation, use **user-defined functions** with input variables — select **"User Input"** from the predefined API function dropdown to bind the input object to user interaction

**User Input Variable**: pre-defined in API (available in function dropdown). Without steps 5-6, the input object will not receive values during simulation.

---

## Requirements Modeling

Add, remove and view requirements on model elements. Access: select element > OPM Requirements group > Add requirements. Actions: add, remove, create consolidated requirements view. Link types: Exhibition (presence/absence), Characterization (attributes), Aggregation Participation (part-whole). Apply requirements to elements, links, or entire diagrams.

### Requirements Example (Door-Peephole System)

Example (Door-Peephole): peephole is part of door (aggregation). Height: 56-64 inches. Components: lens + sleeves. Optional: peephole cover. Function: one-way view for seeing visitors.

---

## Model Analysis

### System Map

Visual overview of entire OPD tree as minimised icons. Access: Main Menu > Model Options > System Map. Click any OPD to navigate. Shows in-zoom and unfold relationships. Essential for large models. Exit: double-click or close.

### Model Informativeness Grading

Premium feature. Access: Settings > Analyze Model > Model Knowledge. OPPL sentences classified: Definition, Structural, Procedural, Meta, Unknown. Metrics: total informative level, weighted score, INF average, total OPPL sentence count. Identifies missing precedence links, processes without inputs/outputs. **Compare model versions over time** for improvement tracking.

### Identification of Missing Knowledge

Access: Settings > Analyze Model > Model Knowledge > Identification of Missing Knowledge. Two algorithms:
- **Pistol**: fast, browser-based, good for initial filtering, may have suggestion limitations
- **RGCN**: Python-based, more accurate — **currently disabled**

Confidence threshold: filter by level (default: 0.5 = 50%). Adjust higher for more confident suggestions.

### AI Requirements Generation

Access: Generative AI menu > AI Requirement Generation. Output: Excel download or clipboard copy. Generated content: requirement text, **verification type**, **acceptance criteria**, **model triplets** (source, target, link relationships). Takes model OPPL as input. Processing time varies with model size. Auto-generated — not guaranteed complete.

---

## Data Import

### CSV Import for Attributes

Bulk add attribute instances and values. Access: select object > entities extension > add attribute instances and values from CSV. **Restriction**: object must not be an instance (not connected via instance structure link).

Options:
- **Ignore existing**: update existing attribute values (default)
- **Create non-existing**: add new attributes
- **Non-computational instances**: create with single state
- **Auto format**: toggle capitalisation (default: enabled)

Preview before import. CSV format: column-based with attribute names and values.

---

## Stereotypes

Pre-defined templates for common patterns (e.g., Security Level Computing). Admin creates for organisation. Apply: select thing > entities extension > set stereotype. Components include sub-components with parameter ranges. Global (G icon) vs Organizational.

Removal options:
- **Unlink**: remove stereotype but keep components in diagram
- **Unlink and remove**: remove stereotype AND all added components

Bring Connected to view stereotype components in other OPDs. Semi-Folding as alternative for internal structure view.

---

## OPD3 Management

Secondary toolbar > OPD management button. Features: search by name/number, hide/show names, open, cut, remove, paste, drag. Auto-arrangement: drag to reorder affects automatic tree layout.

---

## Workflow Tips

### Bring Connected Things

Select element > bring connected. Link type filter: Procedural (instrument, consumption, effect) or Fundamental (exhibition, characterisation). **Filtered Bring**: select specific things first, then bring links only between selected entities. Only directly connected things brought — not parent-child relations.

### Multiple Selection

Ctrl+Click for multiple elements. Lasso: drag rectangle to select area. **Bulk Operations**: select all targets → connect to single destination → creates links to all selected.

### Alignment

Vertexes: black dots on links. Click to add routing vertex; drag to merge back. Grid for precise alignment. Auto-Arrange via system map. Manual adjustment after auto-arrange.

---

## Summary

Complete OPCloud workflow coverage across fundamentals, modelling, simulation, governance, analysis and operations.

Compression rationale: this tutorial contains many atomic UI actions, control distinctions and click-path dependencies. More aggressive compression would reduce recoverability of operational workflows.
