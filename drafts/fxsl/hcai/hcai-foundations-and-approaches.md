---
_manifest:
  urn: "urn:fxsl:kb:hcai-foundations-approaches"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-11"
    source: "source/fxsl/hcai/human-centered-artificial-intelligence-foundations-and-approaches--wei-xu.md"
version: "1.2.0"
status: draft
tags: [hcai, human-centered-ai, ai-governance, human-ai-interaction, ai-methodology, sociotechnical-systems]
lang: en
---

# Human-Centered Artificial Intelligence (HCAI): Foundations and Approaches

## Scope and chapter thesis

- AI is framed as a transformative but double-edged technology: it can advance welfare and societal progress, but also intensify bias, opacity, misinformation, loss of agency, security abuse, and broader systemic harm.
- The chapter grounds urgency with contemporary signals:
  - 233 reported AI incidents in 2024
  - 56.4% year-over-year increase
  - additional AI Incident Database cases logged in 2025
  - AI-driven security automation reaching 36,000 scans/second
- Governance responses cited include:
  - EU AI Act (2024)
  - NIST AI Risk Management Framework (2023)
- HCAI is positioned as both:
  - a research paradigm
  - a practical design approach
- Core HCAI claim: AI must be developed for and with humans so that it amplifies, augments, enhances, and empowers humans rather than harms or replaces them.
- Historical analogy: HCAI in the AI era plays a role analogous to human-centered design during the personal computing era.
- Chapter arc:
  - emerging characteristics and risks of AI technology
  - HCAI concepts and frameworks
  - HCAI guiding principles
  - HCAI methodological framework
  - strategies for HCAI practice
  - structure of the handbook

---

## Emerging characteristics of AI technology

### Transition from HCI to human-AI interaction

- Classical HCI studied interaction between humans and non-AI computing systems.
- Human-AI interaction marks a paradigm shift because AI systems now exhibit varying degrees of:
  - autonomy
  - perception
  - learning
  - adaptation
  - partial independence
  - context-sensitive operation
- Compared with earlier automation, AI systems can:
  - operate in some unpredictable environments
  - collaborate with humans rather than merely serve as passive tools
  - execute tasks beyond the scope of prior automation technologies

### Non-AI automated systems vs AI-based autonomous systems

| Dimension | Non-AI automated systems | AI-based autonomous systems |
| --- | --- | --- |
| Examples | Office software, washing machines, elevators, automated manufacturing lines | Smart speakers, intelligent decision-support systems, autonomous vehicles, service robots |
| Machine behavior | Fixed algorithms, deterministic logic, no adaptation | Learning, adaptation, self-execution; behavior may evolve, be uncertain, or biased |
| Machine role | Tools assisting human tasks | Possible collaborators, depending on autonomy level |
| Output | Deterministic and predictable | Probabilistic, uncertain, context-dependent |
| Human-machine relationship | Unidirectional human-to-machine interaction | Bidirectional collaborative interaction |
| Complementarity | Static allocation, no hybrid complementarity | Dynamic complementarity between human and machine intelligence |
| Sensing | Limited or absent | Present via multimodal sensing |
| Cognitive ability | Absent | Present to varying degrees |
| Self-execution | Requires manual activation | Independent execution in some contexts |
| Adaptation to unpredictable environments | Not possible | Possible depending on design |
| Initiative | Humans initiate actions | Humans and AI can actively initiate actions |
| Directionality | One-way human-directed trust and control | Shared trust, mutual situation awareness, collaborative execution |
| Human intervention | Always required | Human oversight remains crucial even when systems act proactively |

- The shift is not merely technical. It changes the underlying interaction paradigm from one-way control to two-way collaborative interaction.

### Emerging human-machine relationship

- Human-machine relationships evolve together with technology and with human factors, HCI, and UX disciplines.
- Evolution across eras:
  - pre-WWII: human adaptation to machines, machine-centered optimization
  - post-WWII: machine adaptation to humans, human-centered optimization
  - computer era: human-computer interaction, interface design plus training
  - AI era: human-AI collaboration
- In the AI era, systems increasingly move beyond the role of auxiliary tool toward a dual role:
  - tool
  - possible collaborator
- Xu and Gao's human-AI joint cognitive systems framework models a human-AI system as two collaborating cognitive agents:
  - a human cognitive agent
  - a machine cognitive agent
- The framework relies on situation awareness as an information-processing reference for both sides.
- The framework explicitly preserves:
  - human leadership
  - ultimate human authority
- The chapter notes ongoing debate over whether AI should be treated as teammate or tool, but from an HCAI perspective any teammate-like framing must still preserve human control and final authority.

### The double-edged sword effect of AI

- AI can benefit society when responsibly developed and used.
- AI can also generate ethical, social, legal, and security harms when misused, poorly designed, or weakly governed.
- Public infrastructures cited for AI incidents and harms include:
  - OECD AI Incident Monitor
  - Database of AI Litigation
  - AI Incident Database
  - AIAAIC repository
  - Political Deepfakes Incident Database
- Examples of harms cited in the chapter:
  - autonomous vehicles fatally striking pedestrians
  - trading algorithms triggering flash crashes
  - facial recognition contributing to wrongful arrests

### Main AI limitations highlighted in the chapter

- **Vulnerability**
  - performance can degrade outside training scope or under distribution shift
- **Perception limitations**
  - poor input quality can corrupt higher-level inference
- **Potential bias**
  - biased or incomplete data can produce biased outputs
- **Uninterpretability**
  - black-box models reduce understanding and accountability
- **Lack of causal models**
  - machine learning often recognizes patterns without causal understanding, limiting simulation, foresight, and reflection
- **Development bottleneck effect**
  - machine intelligence struggles to simulate higher-order human cognition
- **Autonomy effect**
  - autonomy can reproduce or amplify classic automation-related human factors problems such as automation confusion, irony, reduced situation awareness, out-of-the-loop issues, decision bias, and skill degradation
- **Ethical issues**
  - AI can generate problems involving privacy, justice, and fairness
- **Independent operability limits**
  - AI alone will not be able to handle many complex or unfamiliar situations in the foreseeable future; human involvement remains necessary and humans must retain final decision-making power

### Third-wave AI

- The chapter divides AI evolution into three waves:
  - first wave: 1950s-1980s
  - second wave: 1990s-2010s
  - third wave: 2010s-present
- Third-wave AI emerges from breakthroughs in:
  - deep machine learning
  - big data
  - increased computing power
- The chapter frames third-wave AI as more than technical scaling. It combines:
  - technological enhancement
  - application-oriented deployment
  - a human-centered approach
- Human-centered factors emphasized in this wave include:
  - human needs
  - human characteristics
  - human values
  - human roles
  - human knowledge
  - human abilities
- Characteristic themes of the third wave include:
  - application-driven ecosystems
  - attention to real user needs
  - human-machine hybrid enhanced intelligence
  - data-and-knowledge dual-driven AI
  - interpretability
  - ethical AI
  - meaningful human control
  - intelligent human-AI interfaces
  - stronger UX orientation
  - AI risk management and governance
- Human-machine hybrid enhanced intelligence is presented as a response to the bottleneck of developing machine intelligence in isolation.
- Data-and-knowledge dual-driven AI is presented as a response to fragility, data dependence, low robustness, poor interpretability, and limited reliability.
- The chapter's conclusion on the third wave:
  - AI is reframed from a purely technical pursuit into a cross-disciplinary systems-engineering endeavor
  - humans remain irreplaceable in the development and use of AI systems

| Wave | Approximate period | Core characteristics |
| --- | --- | --- |
| First wave | 1950s-1980s | Symbolic AI, rule-based systems, expert systems, laboratory orientation |
| Second wave | 1990s-2010s | Statistical learning, machine learning expansion, data-driven pattern recognition, broader industrial uptake |
| Third wave | 2010s-present | Deep learning, big data, computing-power breakthroughs, application-driven ecosystems, human-centered orientation, hybrid human-machine intelligence, data-and-knowledge dual-driven AI, interpretability, ethical AI, meaningful human control, intelligent interfaces, UX focus, risk management, governance |

---

## Human-Centered AI: concepts and frameworks

### HCAI as field formation

- HCAI emerges as a response to the challenges and harms of advancing AI.
- Stanford established the first Human-Centered AI research institute in 2018.
- The chapter surveys a multi-author field including:
  - Shneiderman
  - Xu
  - Riedl
  - Dignum and Dignum
  - AI-HLEG
  - Auernhammer

### Ben Shneiderman's frameworks

#### Two-dimensional HCAI framework

- Two key dimensions:
  - degree of human control
  - degree of AI autonomy
- Core claim: greater autonomy does not inherently require less human control.
- Preferred design target: high automation plus high human control.
- The framework rejects the classical one-dimensional tradeoff where more automation means less control.
- Named failure regions:
  - over-automation
  - over-control
- Intended outcome: systems that are reliable, safe, trustworthy, and performance-enhancing.

#### HCAI design metaphors

| Metaphor | Design meaning |
| --- | --- |
| **Supertools** | Information-rich, direct-manipulation systems that amplify human intent |
| **Tele-bots** | Remote effectors kept under human authority through teleoperation and continuous feedback |
| **Active appliances** | Bounded autonomy within clearly defined, well-understood tasks |
| **Control centers** | Human oversight, auditability, and responsive intervention over automated systems |

- Unifying principle: clarity of responsibility through effective human-AI interaction and user interface design.
- The metaphors reframe AI away from default assumptions of autonomous teammates.

#### AI's two grand goals

- Shneiderman distinguishes two overarching AI goals:
  - human emulation
  - useful application
- Confusing those goals produces unrealistic expectations and design risk.
- Four recurring mismatches identified in the chapter:
  - intelligent agent vs powerful tool
  - simulated teammate vs teleoperated device
  - autonomous system vs supervisory control
  - humanoid robot vs mechanoid appliance
- The compromise strategy favored by HCAI emphasizes:
  - supervisory control
  - teleoperation
  - mechanoid appliances
  - comprehensible, predictable, controllable interfaces
- Normative direction: focus less on machines that think like humans and more on technologies that empower humans.

#### Governance structures for trustworthy AI

- Four governance levels:
  - team
  - organization
  - industry
  - government regulation
- Three governance pillars:
  - reliability
  - safety culture
  - trustworthy certification
- Reliability requires:
  - validation
  - bias testing
  - audit trails
- Safety culture requires:
  - leadership commitment
  - near-miss reporting
  - internal review structures
- Trustworthy certification involves:
  - auditors
  - standards bodies
  - insurers
  - regulators
- The chapter also notes fifteen actionable recommendations spanning team, organizational, and industry/regulatory levels.
- Main implication: HCAI cannot be realized through algorithms alone; it requires process, evidence, and durable accountability.

### Wei Xu's frameworks

#### Technology-Human Factors-Ethics (THE) Triangle

- Proposed in 2019 as one of the earliest HCAI frameworks.
- Three inseparable perspectives:
  - technology
  - human factors
  - ethics
- Technology perspective includes:
  - models and algorithms
  - interaction technology
  - robustness and reliability
  - security and resilience
  - explainability mechanisms
  - data quality and representation
  - scalability and efficiency
  - system integration
- Human factors perspective includes:
  - user experience
  - accessibility
  - trust and interpretability
  - cognitive compatibility and mental models
  - emotional intelligence
  - human controllability
  - reskilling
  - training and education
- Ethics perspective includes:
  - fairness and non-discrimination
  - transparency
  - accountability and auditability
  - culture
  - privacy and data protection
  - sustainability
  - inclusivity and justice
  - regulatory compliance
- The framework defines an optimal integration zone where the three perspectives overlap.
- Main implication:
  - technology alone risks harm
  - ethics and human factors without technology risk weak innovation and poor scalability
  - viable HCAI solutions require systematic integration across all three

#### Hierarchical HCAI (hHCAI)

- Built from the intelligent sociotechnical systems framework.
- Central shift: in AI contexts, classical joint optimization of social and technical subsystems is insufficient; human-AI joint optimization must be prioritized.
- hHCAI frames HCAI as a multi-level paradigm:
  - individual human-AI systems
  - organizations
  - ecosystems
  - macrosocial / societal context
- Associated loop concepts:
  - keeping human-in/on-the-loop
  - keeping organization-in-the-loop
  - keeping ecosystem-in-the-loop
  - keeping society-in-the-loop
- Main implication: improving algorithms or isolated systems is insufficient if organizational, ecosystem, and societal alignment are missing.

#### HCAI Methodological Framework (HCAI-MF)

- Motivation: strong concepts exist, but practical implementation remains underdeveloped.
- Purpose: transform HCAI from a design philosophy into a structured, actionable methodology.
- Components highlighted in the chapter:
  - HCAI requirement hierarchy
  - HCAI method taxonomy
  - HCAI process
  - HCAI interdisciplinary collaboration approach
  - HCAI multi-level design paradigms

#### HCAI Maturity Model (HCAI-MM)

| Level | Name | Meaning |
| --- | --- | --- |
| 1 | Ad Hoc / Initial | Unsystematic, individual-effort-based practice |
| 2 | Repeatable / Developing | Partial guidelines introduced, often under external pressure |
| 3 | Defined | Standardized processes and cross-disciplinary collaboration |
| 4 | Managed | Continuous monitoring and measurable indicators such as fairness audits, usability metrics, and incident reporting pipelines |
| 5 | Optimizing | HCAI institutionalized in culture and strategy with continuous learning and predictive governance |

- The chapter also notes adjacent emerging Xu-related frameworks:
  - human-centered human-AI collaboration
  - human-centered human-AI interaction
  - human-centered privacy
  - human-centered artificial social intelligence

### Six HCAI grand challenges

- In 2022, 26 experts from academia, industry, and government reached consensus on six grand challenges.
- The six challenges:
  - **Human well-being**
  - **Responsible AI**
  - **Privacy**
  - **Human-centered design and evaluation**
  - **Governance and oversight**
  - **Human-AI interaction**
- The chapter links these challenges to a practical implementation stance:
  - sociotechnical design
  - ethics-by-design
  - participatory methodologies
  - lifecycle-wide coverage
- Examples of operational implications:
  - well-being metrics and UX measures in system objectives
  - transparent algorithms and auditability for responsible AI
  - privacy-preserving computation and clear data governance
  - collaboration among engineers, psychologists, and ethicists
  - multi-level governance using human and ecological welfare indicators
  - inclusive design, shared situation awareness, trust, shared control, and flexible autonomy

### Other emerging HCAI concepts

- Named approaches and research areas include:
  - Humanistic AI Design
  - Human-Centered Explainable AI
  - Human-Centered Machine Learning
  - human-centered LLMs
  - human-centered social computing
- Capel and Brereton's review of 250+ studies identifies four recurring themes:
  - explainable AI
  - human-centered design and evaluation
  - human-AI teaming
  - ethical AI, with a growing focus on human-AI interaction
- Their mapping uses two axes:
  - human values-led vs AI-led
  - designed vs in-use
- Schmager, Pappas, and Vassilakopoulou characterize HCAI through:
  - purposes: augmentation, AI-autonomy, automation
  - values: ethical, protection, performance
  - properties: oversight, comprehension, integrity
- Desolda et al. define HCAI systems as systems designed, developed, and evaluated with user involvement to improve human performance and satisfaction while remaining useful, usable, reliable, safe, and trustworthy.

### Summary

- Across frameworks, HCAI is consistently treated as both:
  - a guiding design principle
  - a methodological counterbalance to technology-centered AI
- The field has evolved from early ethical and technical integration toward:
  - multi-level sociotechnical perspectives
  - governance
  - interdisciplinary collaboration
  - practical methodologies

---

## HCAI guiding principles

### Why guiding principles matter

- HCAI principles establish the field's values, priorities, and boundaries.
- They provide a common language for engineers, human factors experts, ethicists, policymakers, and users.
- The chapter stresses that the hard problem is not naming principles but operationalizing them amid:
  - abstraction
  - tradeoffs
  - contextual differences
  - overlaps among fairness, ethics, trustworthiness, and responsibility agendas

### Consolidated principle set

| HCAI guiding principle | Definition and HCAI goal | Illustrative examples and selected handbook chapters |
| --- | --- | --- |
| **Human augmentation** | Design AI to amplify, empower, and enhance human abilities and potential rather than substitute for human intelligence | Hybrid intelligence; AI-augmented computational modeling of human behavior |
| **Human controllability** | Allow humans to understand, influence, oversee, and override AI systems when necessary; AI remains under human authority and controllability | From automation to autonomy through AI; human-in/on-the-loop design for controllability |
| **Ethical alignment** | Develop AI in alignment with ethical and societal norms to preserve human values, foster trust, and minimize harm | Human value alignment in AI; ethical AI standards and governance |
| **User experience** | Create interactions that are engaging, intuitive, accessible, and aligned with user expectations | Design thinking and AI; designing human-centered AI experiences |
| **Human-led collaboration** | Ensure humans direct and oversee collaboration with AI while leveraging AI to enhance human capabilities | Artificial social intelligence for team effectiveness; human-AI co-creation |
| **Transparency and explainability** | Provide explainable and understandable AI output to enhance trust and support informed decisions | Human-centered AI design principles for generative AI; LLM explainability |
| **Accountability and responsibility** | Establish responsible AI mechanisms that assign clear human accountability for AI actions and outcomes | Meaningful human control; trustworthy and responsible LLMs |
| **Safety and reliability** | Prioritize human safety, resilient performance, and risk reduction across diverse scenarios | AI risk, safety, and incident reporting; AI risk management frameworks |
| **Sustainability** | Support environmental, social, and economic well-being while aligning AI with long-term human flourishing | Sustainable AI and environmental sustainability perspectives |

### Principle implications

- **Human augmentation**
  - complements judgment, creativity, empathy, and ethical reasoning
  - compensates for limitations in memory, attention, processing scale, and scalability
  - applies from design and development to deployment and sociotechnical ecosystem use
- **Human controllability**
  - requires fallback modes and override options
  - requires transparent, usable, reliable controls in real-world conditions
  - requires operator situation awareness and final decision authority
  - extends to governance, regulation, and audit trails
- **Ethical alignment**
  - includes fairness, inclusivity, privacy, and human dignity
  - requires value-sensitive design, bias audits, impact assessment, and regulatory compliance
  - must adapt across organizational and cultural contexts while remaining aligned with broader human-rights principles
  - is ongoing rather than one-off
- **User experience**
  - goes beyond usability to include emotional, cognitive, and social dimensions
  - includes multimodal interfaces, emotional responsiveness, and adaptive personalization
  - requires user research, participatory design, iterative prototyping, usability testing, continuous feedback, accessibility, and cultural sensitivity
- **Human-led collaboration**
  - positions AI as adaptive collaborator without displacing human leadership
  - requires trust, shared situation awareness, understandable actions, and intervention capability
- **Transparency and explainability**
  - supports trust, accountability, and effective use
  - requires traceable outcomes and stakeholder-specific explanations
  - requires disclosure of system capabilities, risks, and uncertainty
- **Accountability and responsibility**
  - rejects liability displacement onto AI systems
  - requires documented choices, interaction logs, audit trails, ownership structures, and liability frameworks
  - spans developers, deployers, operators, organizations, and regulators
- **Safety and reliability**
  - includes physical, psychological, and social safety
  - requires error tolerance, alerts, emergency shutdown, transparent recovery, robust testing, monitoring, and incident reporting
  - includes resilience against misuse and cascading failures
- **Sustainability**
  - includes environmental efficiency, maintainability, adaptability, equity, and broader human well-being
  - explicitly connects to dual-driven AI and hybrid enhanced intelligence as alternatives to siloed technical development
  - includes avoiding digital divides and supporting resilient communities

---

## HCAI Methodological Framework (HCAI-MF)

### Requirement hierarchy

- Motivation: HCAI practice struggles to translate abstract principles into actionable, verifiable system requirements.
- HCAI-RH systematically links abstract values to concrete requirements.
- Four levels:
  - HCAI design goals
  - HCAI guiding principles
  - HCAI design guidelines
  - product-level requirements
- Product-level requirements include both functional and non-functional requirements such as:
  - usability
  - safety
  - human performance metrics
- Three defining properties highlighted in the source:
  - **means-end alignment**
  - **one-to-many mapping**
  - **goal-directed flow**
- The hierarchy is also informed by human-centered requirements practices such as:
  - user interviews
  - stakeholder interviews
  - participatory design
- Purpose: bridge strategic aspirations and operational implementation.

### Method taxonomy

- Motivation: HCAI still lacks sufficiently unified and scalable methods across the AI lifecycle.
- HCAI-MT organizes methods into five categories:
  - human-centered strategy
  - human-centered computing
  - interaction technology and design
  - human-centered controllability
  - human-centered AI risk management and governance
- The taxonomy details 16 representative methods.

| Method category | Representative methods | Human factors prioritized | Typical lifecycle activity |
| --- | --- | --- | --- |
| **Human-centered strategy** | Human value alignment with AI; hybrid human-artificial intelligence; data- and knowledge-dual-driven AI | Human values, needs, abilities, strategic role of humans | Strategic direction, problem framing, long-range system orientation |
| **Human-centered computing** | Human cognitive modeling; human-centered machine learning; human-centered explainable AI | Human cognition, interpretability, trust, compatibility with human reasoning | Modeling, training, explanation, evaluation |
| **Human-AI interaction technology and design** | Intelligent user interfaces; user experience design; human-AI interaction; human-led collaboration with AI | User experience, interaction quality, shared awareness, collaboration | Interaction design, system development, interface validation |
| **Human-centered controllability** | Human-in/on-the-loop design; machine behavior management; meaningful human control | Human authority, oversight, intervention capability, responsibility | Control design, supervision, escalation, operational governance |
| **Human-centered AI risk management and governance** | Ethical AI standards and governance; algorithm governance; data governance | Fairness, accountability, privacy, compliance, incident response | Governance, deployment, monitoring, audit, post-deployment refinement |

### Representative methods named in the chapter

- **Human-centered strategy**
  - human value alignment with AI
  - hybrid human-artificial intelligence
  - data- and knowledge-dual-driven AI
- **Human-centered computing**
  - human cognitive modeling
  - human-centered machine learning
  - human-centered explainable AI
- **Human-AI interaction technology and design**
  - intelligent user interfaces
  - user experience design
  - human-AI interaction
  - human-led collaboration with AI
- **Human controllability over AI**
  - human-in/on-the-loop system design
  - machine behavior management
  - meaningful human control
- **Human-centered AI risk management and governance**
  - ethical AI standards and governance
  - algorithm governance
  - data governance

### Practical scenarios in the chapter

| HCAI methods | Problems and requirements | Data collection and preparation | Model selection, training, interaction design, and development | Test and validation | Deployment | Monitoring and refinement |
| --- | --- | --- | --- | --- | --- | --- |
| **Human value alignment** | Define human values and desired outcomes | Ensure values such as fairness are reflected in data | Mitigate bias and value conflicts in models and development | Validate value alignment | Communicate clearly with users | Monitor feedback and update the system |
| **User experience design** | Define user needs and UX goals | Use participatory methods to gather user input | Design interaction models and interfaces around human needs | Test software and hardware with users | Provide user support | Track feedback and refine the system |
| **Human-centered machine learning** | Define human-centered problems and goals | Collect diverse and representative data | Use controlled algorithms and human-aware modeling choices | Test for ethical and human-factor issues | Gather and integrate user feedback | Refine algorithms and practices over time |
| **AI ethical governance** | Establish ethical policies and governance expectations | Mitigate ethical risks such as data bias | Choose and develop models for fairness and transparency | Perform ethical audits | Communicate ethical AI commitments to users | Monitor ethical issues and update governance controls |

### Benefits the chapter attributes to the taxonomy

- goal-oriented design
- comprehensive and scalable structure
- actionable guidance for practice

### Multi-level design paradigms

- The chapter treats paradigms as necessary lenses for HCAI practice, not optional framing.
- hHCAI supplies four paradigmatic levels:
  - individual
  - organizational
  - ecosystem
  - society / macrosocial

#### Human-in/on-the-loop

- HITL:
  - active, real-time human participation in critical decisions
  - enables intervention, ethical judgment, and contextual reasoning
- HOTL:
  - supervisory control with intervention when needed
  - supports scalability while preserving accountability
- HCAI extends HITL/HOTL across the entire lifecycle:
  - requirements
  - design
  - development
  - deployment
  - use
  - operations
  - governance
- Humans are embedded as:
  - requirement definers
  - interaction designers
  - model trainers
  - evaluators
  - feedback providers
  - decision participants
  - collaboration leaders
  - operational controllers
  - ultimate authorities with override power

#### Organization-in-the-loop

- Organizations are not just deployment contexts; they are:
  - users
  - enablers
  - mediators
  - regulators of AI effects
- OITL emphasizes organizational structures, workflows, cultures, and governance as design elements.
- Four organizational loops highlighted in the source:
  - use
  - customization
  - task
  - context
- Formal scaffolding:
  - governance
  - work design
- Informal scaffolding:
  - collaboration
  - organizational practices
  - culture
- Main goals:
  - transparency
  - accountability
  - human-centered co-evolution of AI and organizational systems

#### Ecosystem-in-the-loop

- Applies to intelligent ecosystems such as healthcare and transportation.
- Ecosystems are framed as distributed cognitive systems spanning:
  - humans
  - AI agents
  - organizations
  - multiple levels and timescales
- Four foundational pillars:
  - ecosystem-oriented system design
  - human-centered governance and ethics
  - dynamic collaboration and distributed intelligence
  - adaptation, learning, and co-evolution
- Practical concerns include:
  - coordination across subsystems
  - privacy and security
  - partnerships and stakeholder engagement
  - regulatory compliance

#### Society-in-the-loop

- Treats AI as embedded in sociotechnical systems rather than isolated technical artifacts.
- iSTS provides the unifying conceptual basis.
- Intelligence is treated as emergent from interactions among:
  - humans
  - AI technologies
  - organizational processes
  - social institutions
- Six core approaches named in the chapter:
  - systematic design thinking
  - human-centered design
  - multi-level design approach
  - organizational adaptation and redesign
  - human-AI co-learning and co-adaptation
  - open ecosystem perspective
- Non-technical subsystems the chapter explicitly identifies:
  - institutional environment
  - organizational structures
  - culture and values
  - human factors
  - social networks
  - trust and legitimacy
  - resource and economic structures
  - education and knowledge systems
  - political context

| Key dimension | Key non-technical system elements | Description |
| --- | --- | --- |
| **Institutional environment** | Laws, policies, ethical norms | Regulatory frameworks, privacy laws, and ethical standards governing AI |
| **Organizational structures** | Governance models, roles, internal workflows | How organizations deploy, regulate, and manage AI systems |
| **Culture and values** | Societal expectations, ethical beliefs, risk tolerance | Public acceptance, tolerance of bias, and concepts such as automated justice |
| **Human factors** | User behavior, skills, cognitive models | How users understand, interact with, and are trained to use AI systems |
| **Social networks** | Relationships among stakeholders | Interactions between governments, companies, NGOs, and the public around AI |
| **Trust and legitimacy** | Public trust and perceived legitimacy of AI | Whether AI decisions are seen as trustworthy, fair, and lawful |
| **Resource and economic structures** | Ownership and control of data and AI infrastructure | Data monopolies, AI resource centralization, platform capitalism |
| **Education and knowledge systems** | Access to AI literacy and education equality | Who can understand and use AI, and risks of digital divide |
| **Political context** | National strategies, political ideologies, global competition | AI shaped by geopolitics, tech nationalism, and governance philosophies |

### Implications of multi-design paradigms

- HCAI practice must extend beyond individual human-AI interaction.
- Full implementation requires action across all levels.
- Broad implication: AI projects are sociotechnical system projects, not merely engineering projects.

| Research area | Keeping human-in/on-the-loop | Keeping organization-in-the-loop | Keeping ecosystem-in-the-loop | Keeping society-in-the-loop |
| --- | --- | --- | --- | --- |
| **AI-based machine behavior** | Human participation in continuous interaction cycles with AI agents | Alignment of AI decisions and learning with organizational mission and standards | Behavior evolution across multiple AI systems in an intelligent ecosystem | Social factors shaping machine behavior and its ethical effects |
| **Ethical AI** | HITL/HOTL for bias detection, evaluation, and mitigation | Organizational responsibility across the AI lifecycle | Human authority and compatibility across multi-vendor AI systems | Ethical norms, governance, and environmental expectations in society |
| **Human-AI interaction** | Shared tasks, roles, and decision-making while retaining human authority | Organizations as mediators through governance, team design, and oversight | Interaction theory, modeling, technology, and design across multiple AI systems | Effects of cultural, ethical, and social environments on interaction design |
| **Explainable AI** | Humans co-construct explanations through iterative interaction and feedback | Organizational traceability, accountability, and continuous monitoring for XAI | XAI compatibility and conflict management across AI systems in ecosystems | Public trust, public acceptance, and the relation between XAI, culture, knowledge, and ethics |

### HCAI process

- The process integrates:
  - human-centered design
  - the AI system development lifecycle
- Lifecycle stages named in the chapter:
  - problems and requirements
  - data collection and preparation
  - model selection and training
  - interaction design and system development
  - test and validation
  - deployment
  - monitoring and refinement
- The process is intended to address common shortcomings:
  - late involvement of HCAI practitioners
  - fragmented ethics integration
  - limited feedback loops
  - inconsistent treatment of fairness, accountability, and transparency
- Four defining process features:
  - human-centered focus
  - iterative improvement
  - ethical development
  - interdisciplinary collaboration

### Interdisciplinary collaboration

- Interdisciplinary collaboration is foundational to HCAI, not optional.
- Disciplines explicitly positioned as complementary include:
  - HCI
  - human factors
  - psychology
  - ethics
  - law
  - policy
  - sociology
  - organizational studies
  - computer science
  - AI
  - data science
- Collaboration strategies summarized in the chapter:
  - establish shared goals and vision
  - assemble interdisciplinary teams
  - co-design with stakeholders
  - address ethical conflicts systematically
  - institutionalize HCAI methods and processes
  - define transparent decision frameworks
  - foster continuous communication
  - measure success holistically

| HCAI area | Area focus | Primary participating disciplines and approaches | Relevant chapter clusters |
| --- | --- | --- | --- |
| **Human-AI interaction** | Enable humans to engage, communicate, interact, and collaborate effectively with AI | HCI, AI, psychology, computer science, human factors, interaction design | Theory of mind, human-AI interaction, HRI, adaptive systems |
| **Human-centered AI design** | Use design thinking, interaction design, and UX to create HCAI solutions | Design thinking, interaction design, UX design, HCI, AI, ethics | Design thinking, generative AI design principles, human-centered AI experiences |
| **HCAI in computing** | Apply algorithmic design, modeling, and data-driven methods to build HCAI solutions | AI, simulation and modeling, ML, computer science, HCI, cognitive science, psychology, data science, ethics | Human-centered ML, computational modeling, recommender systems, social computing |
| **Human controllability over AI** | Ensure human control through HITL/HOTL, meaningful control, accountability, and traceability | AI, HCI, control systems engineering, robotics, law and policy, cybersecurity, safety-critical design, human factors | Meaningful human control, HITL/HOTL design, control problems, spaceflight, automated vehicles |
| **Human-centered AI risk management and governance** | Address risk reporting, measurement, assessment, governance, and mitigation | Risk management, AI, ethics, law and public policy, sociology, data science, systems engineering | Risk frameworks, privacy, trust, diversity, governance, participatory auditing |

### Maturity model

| Maturity level | Description | Characteristics | Assessment criteria | Objectives |
| --- | --- | --- | --- | --- |
| **Level 1: Initial** | Entry and startup phase with ad hoc HCAI awareness | Isolated human-factor efforts; limited user input; unstructured AI initiatives | Readiness assessment in progress; no formal stakeholder feedback or HCAI process | Build awareness and complete readiness/startup preparation |
| **Level 2: Developing** | Growing understanding and early structuring of HCAI practice | User interviews or surveys in select projects; basic usability testing; early interdisciplinary work | Partial methods, emerging processes, basic guidance | Move from ad hoc activity to repeatable practice |
| **Level 3: Defined** | Standardized HCAI processes across projects | Formal guidelines, structured user involvement, cross-functional collaboration | Documented governance, repeatable processes, defined roles | Institutionalize HCAI practices organization-wide |
| **Level 4: Managed** | Organization-wide implementation with measurable control | KPIs, continuous involvement, rigorous governance, quantitative monitoring | Monitored metrics, fairness/usability indicators, incident reporting, lifecycle evidence | Improve performance and governance through managed measurement |
| **Level 5: Optimizing** | HCAI institutionalized as strategy and culture | Continuous learning, proactive governance, mature co-design communities, ecosystem alignment | Predictive governance, strategic/cultural integration, sustained improvement | Achieve fully optimized, continuously improving HCAI capability |

- Assessment dimensions referenced in the chapter include:
  - design and engineering practices
  - metrics and evaluation
  - risk and incident management
  - organizational governance
  - culture and ecosystem engagement

---

## Strategies for HCAI practice

### Integrative multi-level and multi-layered approaches

- HCAI practice is framed as a sociotechnical implementation problem spanning:
  - technical gaps
  - ethical gaps
  - organizational gaps
  - data gaps
  - algorithmic gaps
  - ecosystem gaps
  - regulatory gaps
  - public-engagement gaps
- The chapter combines:
  - hierarchical HCAI
  - a three-layer implementation strategy

### Three-layer implementation strategy

| Implementation environment | Key HCAI actions | Related handbook chapter clusters |
| --- | --- | --- |
| **Projects** | Before development: define HCAI strategy and plan, set up a cross-disciplinary team, establish HCAI process, select methods, provide HCAI/ethical AI skill training. During development: execute HCAI processes and methods, manage AI behavior with user-participatory tuning/training, execute ethical AI, algorithmic governance, and data governance. After deployment: monitor and optimize AI behavior, track user design feedback, maintain accountability for ethical outcomes. | Foundations and approaches, generative AI design principles, AI experiences, human-centered ML, meaningful human control, HITL/HOTL design, ethical AI governance, data governance, algorithmic governance |
| **Organizations** | Before development: define organizational HCAI goals and guiding principles, establish organization-level HCAI and ethical AI design guidelines, set up AI governance, foster HCAI culture, build R&D resources. During and after development: redesign work systems, develop user support systems, implement HCAI/ethical AI governance, evaluate productivity, decision efficiency, fairness, privacy, and technological change impacts. | Design thinking and AI, ethical AI governance, AI transformation of organizations and society, HCAI maturity model, enterprise strategy, sociotechnical organizational design, business modeling |
| **Society** | Establish government and industry policy for ethical AI, set HCAI/ethical AI design standards at international, national, and industry levels, implement effective ethical AI governance, organize cross-industry and cross-disciplinary HCAI research and applications, cultivate interdisciplinary HCAI talent. | Multi-level sociotechnical systems, AI risk management frameworks, ethical AI standards and governance, international governance of AI, AI transformation of organizations and society |

- Summary implication from the chapter: HCAI must be operationalized across projects, organizations, and society throughout the entire AI lifecycle.

### Enterprise strategy

- HCAI is framed as enterprise transformation, not a narrow technical initiative.
- It requires rethinking how organizations align:
  - strategy
  - structure
  - culture
- Global frameworks cited as operational references:
  - OECD AI Principles
  - EU AI Act
  - NIST AI Risk Management Framework
- Enterprise transformation components highlighted in the chapter:
  - strategic planning
  - business process reengineering
  - work-system redesign
  - cross-functional collaboration
  - transparency
  - participatory design
  - accountability
  - meaningful human control
  - employee reskilling
  - incentive systems
  - multidimensional performance metrics spanning human, social, environmental, and financial outcomes

### Human-centered AI risk management and governance

- Risk management must be a continuous lifecycle program implemented across the organization.
- Required activities:
  - map sociotechnical risks with diverse stakeholders
  - prioritize risks by impact and likelihood
  - define controls across lifecycle stages
  - establish evaluation plans
  - perform failure analysis and abuse testing
  - monitor post-deployment behavior
  - maintain user feedback channels
  - support incident reporting
- Governance frameworks named in the chapter:
  - NIST AI RMF: `Govern -> Map -> Measure -> Manage`
  - ISO/IEC 23894:2023
  - ISO/IEC 42001:2023
- Governance also aligns with:
  - OECD AI Principles
  - EU AI Act
  - FDA Good Machine Learning Practice
- Governance requirements include:
  - traceability from policy to control to evidence
  - centralized documentation of purpose, data lineage, evaluation, and post-deployment plans
  - accountability across leadership, ethics committees, product lines, and research teams
  - user agency
  - transparency
  - contestability
  - KPIs for safety, efficacy, fairness, robustness, and human factors

### Design strategy

- The chapter argues that enterprise design strategy must move beyond technical optimization alone.
- Required design approaches:
  - design thinking
  - UX design
  - HITL/HOTL design
- Operational elements include:
  - AI readiness assessments
  - interdisciplinary collaboration among UX, AI, data, ethics, and policy roles
  - governance checkpoints in design workflows
  - playbooks for HITL/HOTL systems
  - evaluation metrics such as usability, explainability, and perceived control
  - post-deployment feedback channels

### Methodological strategy

- Organizations should tailor HCAI-MF to their size, maturity, and goals.
- High-level strategy in the chapter:
  - align HCAI initiatives with business objectives
  - demonstrate value through pilots
  - secure leadership advocacy
  - build awareness through training
  - define trust and ethics KPIs
  - standardize toolkits and processes
  - prioritize high-impact projects
- Main methodological components:
  - HCAI requirements
  - method adoption
  - HCAI process
  - interdisciplinary collaboration

### Progressive HCAI practice

- HCAI practice is evolutionary rather than instantaneous.
- Organizations need maturity frameworks to:
  - diagnose gaps
  - identify needs
  - define roadmaps
  - improve continuously
- Maturity indicators named in the chapter:
  - stakeholder engagement
  - structured governance
  - ethical oversight
  - interdisciplinary collaboration
  - continuous learning
  - measurable human-AI performance outcomes
- Final implication: HCAI becomes both:
  - a strategic capability
  - a governance system

---

## Structure of the handbook

- The handbook is organized into 10 sections.

| Section | Scope | Count |
| --- | --- | --- |
| Overview, Concepts, and Foundations | Core concepts, frameworks, methodologies, challenges, values, hybrid intelligence, sociotechnical systems, artificial social intelligence, artificial emotional intelligence, embodied intelligence | 7 chapters |
| Human-AI Interaction | Theory of mind, trust calibration, explainability, transparency, UX, role allocation, and social dynamics in practical human-AI interaction | multi-chapter section; exact count not stated in the chapter excerpted here |
| Human-Centered AI Design | Design thinking, participatory design, stakeholder engagement, iterative development, value-sensitive innovation | 5 chapters |
| Human-Centered AI in Computing | Recommender systems, social computing, hybrid intelligence architectures, system-level design | 5 chapters |
| Human Controllability over AI | HITL, HOTL, levels of automation, shared decision-making, responsibility allocation | 6 chapters |
| Human-Centered AI Risk Management | Technical, ethical, social, organizational, and environmental risk identification and mitigation | 7 chapters |
| Human-Centered AI Governance | Governance structures, policies, standards, and stakeholder participation across levels | 7 chapters |
| Human-Centered Large Language Models | Explainability, bias mitigation, deployment, interaction design, risk mitigation | 5 chapters |
| Sectoral Applications for Human-Centered AI | Healthcare, judiciary, nuclear power, cybersecurity, sustainability, arts | 6 chapters |
| Human-Centered AI Practice | Organizational adoption, maturity, business transformation, social impact, toolkits, and case studies for operational HCAI | final multi-chapter section; exact count not stated in the chapter excerpted here |

- The chapter describes each handbook chapter as contributing:
  - emerging HCAI approaches
  - current implementation status
  - key challenges and unresolved issues
  - future directions

---

## Conclusion

- HCAI is presented as an integrative, multi-level evolution in how humans design, develop, interact with, and govern AI systems.
- Convergent criteria for successful AI:
  - reliable
  - safe
  - trustworthy
  - fundamentally human-aligned
- HCAI reframes AI as part of interconnected:
  - human-AI systems
  - organizational contexts
  - ecosystems
  - sociotechnical structures
- Human values and needs must be preserved across:
  - design
  - development
  - deployment
  - use
  - governance
- Realizing HCAI requires:
  - cross-disciplinary collaboration
  - continuous methodological advancement
  - sustained organizational practice
- The HCAI-MF and HCAI-MM are presented as the main roadmaps for embedding HCAI across individuals, organizations, ecosystems, and societies.
- Final evaluative criterion: AI should be judged not only by technical sophistication but by its capacity to enhance human performance, safeguard human dignity, and strengthen societal benefit and trust.
