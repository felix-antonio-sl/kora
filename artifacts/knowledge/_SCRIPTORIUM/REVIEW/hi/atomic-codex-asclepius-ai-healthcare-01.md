---
_manifest:
  urn: urn:hi:kb:atomic-codex-asclepius-ai-healthcare-01
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/ia med.md — atomizacion Codex
      Asclepius (AI for Improving Healthcare); output de /atomize 2026-04-10
version: 1.0.0
status: borrador
tags:
- atomic
- ai
- healthcare
- codex-asclepius
- hi
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 200
      producer: urn:kora:artefacto:atomize
      source_corpus: Codex Asclepius — AI for Improving Healthcare
      segmented: true
      segment_role: segment
      hand_edited: true
      segment_index: 1
      segment_count: 4
---

# Codex Asclepius - Segmento 01

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/ia med.md`
- Proposiciones: `200`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `01/04`
- Rango: `P001-P200`

## Indice de fuentes

- `S01` · [ia med.md](../../INBOX/hi/ia med.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 01 del corpus atomizado.

## Chapter 1 — Introduction: AI for Improving Healthcare

### AI and Digital Transformation
- **P001** · `fact` · AI developments are entrenched in digitalization; AI and digitalization shape each other · [src:S01](../../INBOX/hi/ia med.md)
- **P002** · `fact` · Without massive EHR adoption hosting digital structured data, no broad-scale analysis of patient demographics, biomarkers, diagnoses, treatments would be possible · [src:S01](../../INBOX/hi/ia med.md)
- **P003** · `definition` · Learning Health System (LHS) = epitome of striving for improvement of patient services through data; analysis (not always AI-based) is LHS engine · [src:S01](../../INBOX/hi/ia med.md)
- **P004** · `fact` · Milestones of digitalization: democratization of information/knowledge, real-time knowledge development, enhanced visualization, cognitive support, connectivity, mobility [1] · [src:S01](../../INBOX/hi/ia med.md)
- **P005** · `definition` · Democratization of information/knowledge = process of opening previously secluded information to broad public via internet and open-access policies · [src:S01](../../INBOX/hi/ia med.md)
- **P006** · `tension` · DL models simultaneously enable and undermine transparency → black box phenomenon; clinicians cannot explain AI predictions to patients · [src:S01](../../INBOX/hi/ia med.md)
- **P007** · `definition` · XAI (Explainable AI) = methods developed to achieve greater insight into mechanisms of deep AI models · [src:S01](../../INBOX/hi/ia med.md)

### Recent Applications from the Real World
- **P008** · `fact` · AI tools performed equally or superior to human experts in cardiological imaging (scoping review) [2] · [src:S01](../../INBOX/hi/ia med.md)
- **P009** · `fact` · DL methods matched human sensitivity and surpassed specificity for lung cancer detection on CT images (scoping review) [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P010** · `fact` · In population-wide mammography screening, AI decreased radiologist workload while enhancing screening performance [4] · [src:S01](../../INBOX/hi/ia med.md)
- **P011** · `fact` · LLMs became popular in early 2020s for workflow improvement, safer patient care, knowledge extraction · [src:S01](../../INBOX/hi/ia med.md)
- **P012** · `fact` · AI-enabled workflow for patient portal messages contributed to time reduction before qualified clinician review [5] · [src:S01](../../INBOX/hi/ia med.md)
- **P013** · `fact` · Pipeline using GPT for PubMed literature retrieval + ranking + summarization yielded good results for relevance, quality, accuracy [6] · [src:S01](../../INBOX/hi/ia med.md)
- **P014** · `fact` · ChatGPT + Pinecone algorithm extracted knowledge from NIH National Standards for Diabetes Self-Management Education; expert-reviewed tool achieved very high accuracy for patient health literacy [7] · [src:S01](../../INBOX/hi/ia med.md)
- **P015** · `scope` · AI applications in healthcare cover: operational efficiency, decision support, diagnostic accuracy, advanced interaction, communication, logistical support, workload relief, professional development (scoping review) [8] · [src:S01](../../INBOX/hi/ia med.md)
- **P016** · `requirement` · AI performance and safe use must be evaluated in RCTs and realistic experiments to prove accuracy, sensitivity, specificity, and added value vs. usual procedures · [src:S01](../../INBOX/hi/ia med.md)

### A Short History of AI in Medicine
- **P017** · `fact` · AI in medicine started with knowledge-based approach: rules + facts → inference; 1970s database of pharmaceutical/chemical relations deduced drug interactions from pharmacokinetic/pharmacodynamic relationships [9] · [src:S01](../../INBOX/hi/ia med.md)
- **P018** · `fact` · MYCIN = expert system for infectious disease diagnosis and therapy selection; incorporated rule acquisition, explanation component, consultation module for physicians [10] · [src:S01](../../INBOX/hi/ia med.md)
- **P019** · `fact` · GoCom system recommended medication management of multimorbid patients based on goal-oriented input from clinical guidelines + medical ontologies [11] · [src:S01](../../INBOX/hi/ia med.md)
- **P020** · `fact` · Ontology-based CDSS for diabetes used fuzzy rules from AACE/ACE guidelines to propose individual HbA1c target values and recommend antidiabetic medication [12] · [src:S01](../../INBOX/hi/ia med.md)
- **P021** · `fact` · Knowledge-based approaches (ontologies, semantic web, decision tables, rules, logic, probabilistic models) remain active research field [13] · [src:S01](../../INBOX/hi/ia med.md)
- **P022** · `fact` · ML rooted in: Turing's learning machine concept, perceptron algorithm for binary classification (1940s-1950s), backpropagation idea (1980s) [14] · [src:S01](../../INBOX/hi/ia med.md)
- **P023** · `fact` · ML application in healthcare was difficult due to lack of large-scale digital data; now evolving exponentially with EHRs, PACS, observational health data · [src:S01](../../INBOX/hi/ia med.md)
- **P024** · `fact` · Crucial parallel trends: rise of DL (neural networks with multiple layers) [15], pretrained AI models, increased computational power, HPC clusters, in-memory computing (e.g., SAP HANA) · [src:S01](../../INBOX/hi/ia med.md)
- **P025** · `tension` · Knowledge-based vs. ML approaches sometimes regarded as opposites (evidence from RCTs vs. observational data), but both strive for knowledge → complementary rather than contrary · [src:S01](../../INBOX/hi/ia med.md)

### What Is Intelligence?
- **P026** · `definition` · Cattell-Horn-Carroll (CHC) theory: fluid intelligence (inductive/deductive reasoning) + crystallized intelligence (acquired knowledge); Horn added perception/processing, short-term memory, long-term storage/retrieval, speed of processing; Carroll arranged into 3-strata hierarchy with "general intelligence" at top [16] · [src:S01](../../INBOX/hi/ia med.md)
- **P027** · `fact` · Human intelligence is agreed to be multidimensional phenomenon [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P028** · `definition` · Gardner (1983) "Frames of Mind: Theory of Multiple Intelligences" = linguistic, musical, spatial, mathematical-logical, bodily-kinesthetic, personal intelligence; speaks of intelligences in plural [18] · [src:S01](../../INBOX/hi/ia med.md)
- **P029** · `definition` · Sternberg's meta-intelligence = creative, analytical, practical, wisdom-based approaches collaborate/interact; meta-components: (1) recognize problem, (2) define problem, (3) allocate resources, (4) mentally represent, (5) formulate strategy, (6) monitor strategy, (7) evaluate strategy [19] · [src:S01](../../INBOX/hi/ia med.md)
- **P030** · `definition` · Human intelligence (Gignac & Szodorai) = maximal capacity to achieve novel goal successfully using perceptual-cognitive processes [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P031** · `definition` · Artificial intelligence (Gignac & Szodorai) = maximal capacity of artificial system to successfully achieve novel goal through computational algorithms [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P032** · `definition` · Human learning (Gignac & Szodorai) = demonstrable change in probability/intensity of specific behavior, underpinned by neurological processes and cognitive strategies in response to stimuli [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P033** · `definition` · Artificial learning (Gignac & Szodorai) = demonstrable change in probability/intensity of specific response/decision-making potential, underpinned by computational algorithms and data [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P034** · `definition` · Transfer learning = pretrain networks on large unspecific dataset when target dataset is small; meta learning = training procedure for various tasks; autonomous learning = training model of world unsupervised (without labeled data) [20] · [src:S01](../../INBOX/hi/ia med.md)
- **P035** · `fact` · AI assistance increased performance of junior readers assessing radiographic knee osteoarthritis images; improved interobserver agreement across all experience levels [21] · [src:S01](../../INBOX/hi/ia med.md)

### The Promise of Augmenting Human Capacity
- **P036** · `fact` · Isaac Asimov coined "robotics"; in "Intelligences Together" (1986) criticized trope that AI will inevitably replace humans; argued AI + HI differ and should combine [22] · [src:S01](../../INBOX/hi/ia med.md)
- **P037** · `rule` · Value proposition of AI in medicine/healthcare = augment human capacity rather than automate processes and outcomes; especially when clinician is personally liable for decisions · [src:S01](../../INBOX/hi/ia med.md)
- **P038** · `fact` · Humans are imperfect: limited attention, memory, reaction time due to sensory, cognitive, time constraints → quest to counterbalance human deficits with intelligent algorithms and vice versa · [src:S01](../../INBOX/hi/ia med.md)
- **P039** · `fact` · AI-human partnering improved detection of artery occlusions from CT angiography: sensitivity, specificity, accuracy all improved with AI assistance [23] · [src:S01](../../INBOX/hi/ia med.md)
- **P040** · `fact` · AI support improved diagnostic skills of readers irrespective of specialty, beyond what self-training alone achieved [24] · [src:S01](../../INBOX/hi/ia med.md)
- **P041** · `fact` · AI support significantly decreased reporting times → improved diagnostic efficiency [25] · [src:S01](../../INBOX/hi/ia med.md)
- **P042** · `requirement` · Need for studies investigating AI-human partnering at cognitive model level incorporating theories of decision-making and mediators (attention, reaction time) [26] · [src:S01](../../INBOX/hi/ia med.md)
- **P043** · `fact` · De-professionalization/de-skilling fear contradicted by experienced AI-using clinicians who regarded AI recommendation as complementary view, not undermining profession [27] · [src:S01](../../INBOX/hi/ia med.md)
- **P044** · `tension` · Clinical decision-making: clinicians = "ecologically bound" (selected cues from patient + environment); ML models = "de-bounding" (correlations from large datasets without clinical context) → distinct paths, can reach same conclusions [26] · [src:S01](../../INBOX/hi/ia med.md)
- **P045** · `fact` · In supervised ML, humans label training data → forced collaboration; feedback on model output enables mutual augmentation · [src:S01](../../INBOX/hi/ia med.md)
- **P046** · `fact` · Robot-assisted surgery most frequently applied for radical prostatectomy worldwide; ≥ 10 AI use cases including haptic feedback for suture breakage, augmented reality for tumor identification, predicting continence [28] · [src:S01](../../INBOX/hi/ia med.md)
- **P047** · `fact` · Smart insulin pumps predict glucose level and adjust pump activity based on physical activity level → help type 1 diabetes patients avoid hypoglycemia during exercise [29] · [src:S01](../../INBOX/hi/ia med.md)
- **P048** · `scope` · Data quality criteria: accuracy (correctness, timeliness, validity), completeness (relevance, no missing values), redundancy (minimality, conciseness, normalization), readability (comprehensibility, clarity), accessibility, consistency (cohesion, no contradictions), usefulness, trust (reliability, data security) [31] · [src:S01](../../INBOX/hi/ia med.md)

### The Risks of AI
- **P049** · `rule` · Only high-quality data yield high-quality AI models; data quality cannot be taken for granted, particularly for secondary data use from EHRs · [src:S01](../../INBOX/hi/ia med.md)
- **P050** · `requirement` · Data must be interoperable (structural + semantic) to merge into big data lakes; AI models claiming generalizability require representative multi-center data · [src:S01](../../INBOX/hi/ia med.md)
- **P051** · `fact` · Skin lesion AI models require diverse skin types/colors in dataset; correctness of manual data labels susceptible to human errors, prejudices, predilections · [src:S01](../../INBOX/hi/ia med.md)
- **P052** · `constraint` · Low data quality → AI models insufficient, possibly biased, may perpetuate inequalities at large scale · [src:S01](../../INBOX/hi/ia med.md)
- **P053** · `fact` · Data imbalance had stronger deteriorating effect on model performance than data size (accuracy saturated with size) [32] · [src:S01](../../INBOX/hi/ia med.md)
- **P054** · `definition` · Automation bias = overreliance, under-reliance, or reduced vigilance for errors when using automated systems [26] · [src:S01](../../INBOX/hi/ia med.md)
- **P055** · `fact` · Overreliance associated with: high trust in system, lack of self-confidence, time pressure, cognitive overload, demanding tasks [33, 34] · [src:S01](../../INBOX/hi/ia med.md)
- **P056** · `fact` · Automation bias → errors of commission (following incorrect algorithmic decision) or errors of omission (not performing task because AI did not suggest it) [33] · [src:S01](../../INBOX/hi/ia med.md)
- **P057** · `fact` · Clinicians with low diagnostic skills, no special training, high perceived benefit from CDSS showed trend of automation bias; profession and gender influenced acceptance of wrong recommendations [35] · [src:S01](../../INBOX/hi/ia med.md)
- **P058** · `definition` · Perfect automation schema = exaggerated high-performance expectations ascribed to AI vs. humans; disappointment → loss of trust; overconfidence → automation bias [36] · [src:S01](../../INBOX/hi/ia med.md)
- **P059** · `fact` · Generative AI risk: ChatGPT known to fabricate DOI numbers; ~1/3 of clinical decisions deemed synthetic wound images to be real (clinicians with ≥ moderate knowledge) [37] · [src:S01](../../INBOX/hi/ia med.md)
- **P060** · `definition` · SHAP (SHapley Additive exPlanation) = model-agnostic method from coalitional game theory showing feature importance for prediction; applies to logistic regression, boosted trees, transformer NLP [38] · [src:S01](../../INBOX/hi/ia med.md)
- **P061** · `definition` · Grad-CAM (Gradient-weighted Class Activation Mapping) = method showing main activation of algorithm in image via heatmaps [39] · [src:S01](../../INBOX/hi/ia med.md)
- **P062** · `fact` · Diagnostic performance of domain experts benefits from XAI (heatmaps juxtaposed with medical images) compared to simple AI [40] · [src:S01](../../INBOX/hi/ia med.md)
- **P063** · `tension` · Alternative view: accuracy of data models more important than full explainability [41]; focus should be on reliability (robust + valid results) [42]; patients not interested in technical intricacies but clinical implications [43] · [src:S01](../../INBOX/hi/ia med.md)
- **P064** · `fact` · Risk of skill decay over time using AI may go unnoticed; tasks demanding greater cognitive workload most affected; well-developed clinical skills = antidote against automation bias [44, 35] · [src:S01](../../INBOX/hi/ia med.md)
- **P065** · `requirement` · Regulations/frameworks addressing data protection, security, accountability, liability are of special interest to AI given large sensitive datasets · [src:S01](../../INBOX/hi/ia med.md)

### From Theory to Practice
- **P066** · `fact` · SCCM (Society of Critical Care Medicine) established data science campaign for critical care; Panel on Data Harmonization/Sharing defined core data elements using LOINC, OMOP, HL7 FHIR [45] · [src:S01](../../INBOX/hi/ia med.md)
- **P067** · `fact` · STANDING Together = international collaboration recommending procedures to assess/declare limitations and biases of datasets; 18 core topics including dataset summary, identity, access, sampling, ethics, governance [46] · [src:S01](../../INBOX/hi/ia med.md)
- **P068** · `fact` · CFIR (Consolidated Framework for Implementation Research) + ERIC (Expert Recommendations for Implementing Change) used as templates for AI implementation in radiotherapy; barriers: lack of AI knowledge, lacking trust, low data confidence, lack of stakeholder involvement, research-practice gap [48] · [src:S01](../../INBOX/hi/ia med.md)
- **P069** · `definition` · TUCAPA scheme of AI literacy: TU = technological understanding, CA = critical appraisal, PA = practical application [49] · [src:S01](../../INBOX/hi/ia med.md)
- **P070** · `fact` · Ng et al. extended AI literacy: technical concepts, appraisal, validation, ethics; 3 user levels: consumer, translator, developer [50] · [src:S01](../../INBOX/hi/ia med.md)
- **P071** · `scope` · Consumer competencies: explain AI/ML, confusion matrix, limitations, accountability, evidence levels; Translator: supervised/unsupervised training, information governance, bias mitigation, clinical endpoints; Developer: training paradigms, synthetic data, interpretable engineering, algorithm analysis [50] · [src:S01](../../INBOX/hi/ia med.md)
- **P072** · `fact` · Scoping review identified 3 AI curricula pillars: "AI use", "interpreting results from AI", "explaining results from AI" [51] · [src:S01](../../INBOX/hi/ia med.md)

### Outlook and Conclusions
- **P073** · `rule` · Bridging AI and HI requires respecting existence of two distinct worlds; avoid anthropomorphisms (e.g., "hallucinations" instead of "errors") · [src:S01](../../INBOX/hi/ia med.md)
- **P074** · `rule` · AI methods/applications must be leveraged under umbrella of human oversight; may stem from ML/data-driven or knowledge-based approaches, or integrate both · [src:S01](../../INBOX/hi/ia med.md)
- **P075** · `rule` · Bridging AI + HI denotes deliberating/agreeing on human regulations and frameworks for avoiding detrimental and unethical consequences of AI · [src:S01](../../INBOX/hi/ia med.md)

## Chapter 2 — Principles of AI and Big Data in Healthcare

### Definitions and Core Concepts
- **P076** · `definition` · AI encompasses computational methods/algorithms designed to perform tasks requiring human intelligence: learning from data, recognizing patterns, making decisions [29] · [src:S01](../../INBOX/hi/ia med.md)
- **P077** · `definition` · ML = subset of AI; algorithms learn patterns from data, make predictions/decisions without explicit programming; types: supervised, unsupervised, reinforcement learning [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P078** · `definition` · DL = specialized branch of ML using artificial neural networks with multiple layers; captures complex nonlinear relationships in large unstructured datasets [6] · [src:S01](../../INBOX/hi/ia med.md)
- **P079** · `definition` · NLP = enables machines to understand, interpret, generate human language; essential for clinical documentation analysis, voice-enabled interfaces [26, 27] · [src:S01](../../INBOX/hi/ia med.md)
- **P080** · `definition` · Computer vision = AI systems extracting meaningful information from medical images for diagnostics and image-guided procedures [6, 13] · [src:S01](../../INBOX/hi/ia med.md)
- **P081** · `definition` · Big Data in healthcare = datasets of substantial volume, velocity, variety, complexity (EHRs, imaging archives, genomic sequences, wearable sensor data); exceed traditional analytical capabilities [23] · [src:S01](../../INBOX/hi/ia med.md)

### Historical Context
- **P082** · `fact` · MYCIN (1970s) = first notable healthcare AI system; recommended antibiotics based on patient symptoms + lab results [22] · [src:S01](../../INBOX/hi/ia med.md)
- **P083** · `fact` · Late 1990s-early 2000s: pivot to data-driven learning as EHRs became ubiquitous; ML classifiers predicted hospital readmission and sepsis risk [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P084** · `fact` · 2010s: major inflection with GPU-accelerated DL; CNNs demonstrated radiologist-level accuracy in image classification across radiology, dermatology, pathology [6] · [src:S01](../../INBOX/hi/ia med.md)
- **P085** · `fact` · Transformer architectures + self-attention [24] enabled large-scale language/vision models; foundation models BioBERT, Med-PaLM achieved near-expert-level on QA tasks · [src:S01](../../INBOX/hi/ia med.md)
- **P086** · `fact` · GANs and diffusion models produce high-fidelity synthetic medical images addressing data scarcity, class imbalance, privacy preservation · [src:S01](../../INBOX/hi/ia med.md)

### Rule-Based Versus Data-Driven AI
- **P087** · `definition` · Rule-based AI = explicit instructions/rules coded by experts; logical pathways for decision-making; limited by inability to adapt without manual intervention [22] · [src:S01](../../INBOX/hi/ia med.md)
- **P088** · `definition` · Data-driven AI = ML algorithms identifying patterns from large complex datasets; learns continuously; includes supervised, unsupervised, reinforcement learning [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P089** · `tension` · Rule-based systems offer high transparency but limited adaptability; data-driven (especially DL) perceived as "black boxes" with thousands/millions of parameters → prompted XAI research [1] · [src:S01](../../INBOX/hi/ia med.md)
- **P090** · `definition` · Hybrid AI = combines rule-based (safety/interpretability) + ML (adaptability); example: TREWS (Targeted Real-time Early Warning System) for sepsis at Johns Hopkins — physiological thresholds trigger alert (rule-based), gradient-boosting model recalibrates risk (data-driven) [12] · [src:S01](../../INBOX/hi/ia med.md)

### Embodied and Disembodied AI
- **P091** · `definition` · Embodied AI = AI integrated into physical/robotic platforms interacting physically with environment (surgical assistants, rehabilitation devices, patient-care robots) · [src:S01](../../INBOX/hi/ia med.md)
- **P092** · `fact` · da Vinci Surgical System = exemplar of embodied AI; enhances surgeon precision, stability, dexterity in minimally invasive surgery [21] · [src:S01](../../INBOX/hi/ia med.md)
- **P093** · `definition` · Disembodied AI = software-based, no physical presence (virtual assistants, predictive analytics in EHR, CDSS); delivers predictions/recommendations via digital interfaces [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P094** · `fact` · Smart insulin pumps blur embodied/disembodied divide: on-body sensors (CGM) + embedded control algorithms, cloud-updated and app-controlled [5] · [src:S01](../../INBOX/hi/ia med.md)

### From Traditional Statistics to Machine Learning
- **P095** · `fact` · Traditional statistical methods (linear/logistic regression, decision trees, survival analysis) assume specific data distributions, require predefined hypotheses → highly interpretable but limited for high-dimensional/unstructured data [11] · [src:S01](../../INBOX/hi/ia med.md)
- **P096** · `constraint` · Traditional methods face limitations with medical images, genomic sequences, free-text clinical notes, EHRs that violate linearity, independence, normality assumptions [3] · [src:S01](../../INBOX/hi/ia med.md)
- **P097** · `fact` · Traditional ML (random forests, SVMs, gradient boosting) require less computational power and smaller datasets than DL; more feasible for many clinical tasks [14] · [src:S01](../../INBOX/hi/ia med.md)
- **P098** · `fact` · CNNs achieved human-level or superhuman performance detecting lung tumors (CT), breast cancer (mammograms), diabetic retinopathy (retinal scans) [6, 13] · [src:S01](../../INBOX/hi/ia med.md)

### Generative AI in Healthcare
- **P099** · `definition` · Generative AI = techniques generating new data instances resembling real-world training data; prominent models: GANs, VAEs (variational autoencoders), transformer-based models · [src:S01](../../INBOX/hi/ia med.md)
- **P100** · `fact` · GANs employ generator + discriminator in adversarial training → produce synthetic medical images, clinical scenarios, textual data · [src:S01](../../INBOX/hi/ia med.md)
- **P101** · `fact` · GANs generate synthetic medical images enhancing training datasets → improved performance/robustness of diagnostic AI; beneficial when real data limited, sensitive, costly [28] · [src:S01](../../INBOX/hi/ia med.md)
- **P102** · `fact` · Generative AI in drug discovery: AI-driven molecular modeling → rapid identification/synthesis of novel compounds, significantly reducing time and cost [30] · [src:S01](../../INBOX/hi/ia med.md)
- **P103** · `fact` · 2023: FDA released draft guidance on synthetic data for medical-device algorithms; emphasized provenance, fidelity testing, disclosure requirements [8] · [src:S01](../../INBOX/hi/ia med.md)
- **P104** · `constraint` · Generative AI risks: data bias, ethical oversight gaps, model explainability concerns; synthetic data may perpetuate disparities; must clearly delineate real vs. generated data [4, 25] · [src:S01](../../INBOX/hi/ia med.md)

### Data-Driven AI: Algorithms, Data, and Explainability
- **P105** · `definition` · XAI techniques LIME (Local Interpretable Model-agnostic Explanations) and SHAP gained prominence for elucidating AI decision-making in healthcare [1] · [src:S01](../../INBOX/hi/ia med.md)
- **P106** · `fact` · MitPlan (Michalowski et al.) = AI-driven system for multimorbid patients; offers "Level 3" explanations: why action chosen, why modifications made, how cost/adherence influenced choices → improved physician understanding + trust [17] · [src:S01](../../INBOX/hi/ia med.md)
- **P107** · `fact` · LLM Meditron70B tested for auto-generating treatment explanations; matched quality of manually curated explanations in evidence reflection and self-containment; but risk of hallucinations/clinical inaccuracies requiring oversight [18] · [src:S01](../../INBOX/hi/ia med.md)
- **P108** · `rule` · Explainability must be actionable, clinically relevant, context-aware; especially in multimorbidity where CDSS must reconcile overlapping/conflicting guidelines · [src:S01](../../INBOX/hi/ia med.md)
- **P109** · `requirement` · FDA increasingly emphasizes explainability + transparency as critical factors evaluating AI-based medical devices/software [9] · [src:S01](../../INBOX/hi/ia med.md)

### Ethical Considerations and Human Oversight
- **P110** · `requirement` · Robust data governance frameworks, secure data handling, clear informed consent processes essential to mitigate privacy risks in AI [25] · [src:S01](../../INBOX/hi/ia med.md)
- **P111** · `fact` · AI-driven predictive algorithms shown to exhibit biases systematically disadvantaging racial/socioeconomic groups when training data reflect inequalities [19] · [src:S01](../../INBOX/hi/ia med.md)
- **P112** · `fact` · EU AI Act [7] classifies most medical AI as "high-risk" → mandates rigorous quality-management systems, post-market monitoring, transparency artefacts · [src:S01](../../INBOX/hi/ia med.md)
- **P113** · `obligation` · Ultimate responsibility for patient care must remain with healthcare professionals; human oversight safeguards against AI errors, biases, ethical missteps [23] · [src:S01](../../INBOX/hi/ia med.md)

### Illustrative Case Studies
- **P114** · `fact` · CNN-based tools achieved remarkable accuracy detecting breast cancer lesions from mammograms, identifying subtle features humans might overlook [16] · [src:S01](../../INBOX/hi/ia med.md)
- **P115** · `rule` · AI radiology tools designed to augment not replace radiologists; provide second opinions or highlight regions of interest for closer review [1] · [src:S01](../../INBOX/hi/ia med.md)
- **P116** · `fact` · Hospitals implementing AI-driven early warning systems significantly reduced adverse clinical events via timely alerts → proactive rather than reactive care [3, 20] · [src:S01](../../INBOX/hi/ia med.md)
- **P117** · `fact` · ML models analyzing genomic data predict individual responses to therapies, identify genetic predispositions, tailor interventions to genetic makeup [2] · [src:S01](../../INBOX/hi/ia med.md)
- **P118** · `fact` · AI models used to predict response to trastuzumab in HER2-positive breast cancer [6]; flag CYP2C19 variants influencing clopidogrel response [3] · [src:S01](../../INBOX/hi/ia med.md)

### Outlook and Conclusions
- **P119** · `fact` · Multimodal foundation models fusing imaging, text, waveforms, genomics (e.g., GPT-4-based Med-PaLM Multimodal) promise unified reasoning across disparate data sources · [src:S01](../../INBOX/hi/ia med.md)
- **P120** · `requirement` · Success of multimodal models hinges on federated-learning protocols, synthetic-data safeguards, transparent evaluation benchmarks reflecting real-world diversity · [src:S01](../../INBOX/hi/ia med.md)
- **P121** · `requirement` · AI in healthcare can only be realized through conscientious, transparent, human-centered whole-person integration prioritizing patient/family/community well-being · [src:S01](../../INBOX/hi/ia med.md)

## Chapter 3 — Human Intelligence and the Caring Imperative

### Principles of Human Decision
- **P122** · `definition` · Expected utility theory = decisions made through purely rational deliberation aiming to maximize expected utility of outcome · [src:S01](../../INBOX/hi/ia med.md)
- **P123** · `definition` · Prospect theory (Kahneman & Tversky) = people avoid losses in risky decisions; losses perceived as having more significant consequences than equivalent gains; 2 behaviors: risk aversion (gains) + risk seeking (losses) [1] · [src:S01](../../INBOX/hi/ia med.md)
- **P124** · `fact` · Framing (gain vs. loss) significantly influences decision-making behavior; heuristics simplify complex facts along with subjective probabilities and values [1, 2] · [src:S01](../../INBOX/hi/ia med.md)
- **P125** · `definition` · 3 key heuristics: (1) representativeness (probability based on stereotype), (2) availability (frequency/size of class), (3) anchoring (predictions based on reference points) [2] · [src:S01](../../INBOX/hi/ia med.md)
- **P126** · `fact` · Dual-system model: System I = fast, automatic, unconscious; System II = slow, effortful, intentional, conscious; only System II accesses capacity-limited working memory [4] · [src:S01](../../INBOX/hi/ia med.md)
- **P127** · `fact` · Experts reach conclusions quickly/intuitively (System I); novices require more time analytically (System II); experts may struggle with novel situations requiring adaptation of fast processes [4] · [src:S01](../../INBOX/hi/ia med.md)

### Translating Principles into Healthcare
- **P128** · `definition` · Regret theory = decisions based on utility appraisal + anticipation of feelings of regret/rejoicing when comparing outcomes of alternative choices [6] · [src:S01](../../INBOX/hi/ia med.md)
- **P129** · `fact` · Regret (System I proxy) + utility (System II proxy) model explained physicians treating only patients with very high pulmonary embolism probability → anticipated regret of causing bleeding through anticoagulants; interaction of System I/II → undertreatment or overtreatment [7] · [src:S01](../../INBOX/hi/ia med.md)
- **P130** · `fact` · Prospect theory applied to healthcare: loss-aversion framing made individuals accept COVID-19 measures (distancing, vaccination) more readily when messaging emphasized avoiding losses [5] · [src:S01](../../INBOX/hi/ia med.md)

### Evidence-Based Practice
- **P131** · `definition` · Evidence-based medicine (EBM) = relies on data from epidemiological/biostatistical analyses of patient/population studies; contrasts with habit/tradition; synthesizes findings via meta-analyses into decision aids (odds ratios) [8] · [src:S01](../../INBOX/hi/ia med.md)
- **P132** · `fact` · EBM was instrumental in establishing Cochrane Collaboration; evidence-based practice provides common foundation for interprofessional communication, decision-making, sharing responsibilities [8] · [src:S01](../../INBOX/hi/ia med.md)
- **P133** · `rule` · Evidence-based practice aims to provide best rational basis (evidence) for decision-making while incorporating personal experience and patient values/preferences · [src:S01](../../INBOX/hi/ia med.md)
- **P134** · `fact` · LLMs tested for evidence tasks (PICO extraction, RCT synthesis, simplifying medical texts) show considerable potential but reveal limitations in factual consistency and domain accuracy → human expert oversight still necessary [10] · [src:S01](../../INBOX/hi/ia med.md)

### Further Concepts: Social and Emotional Intelligence
- **P135** · `definition` · Social intelligence (1920s-1930s) = "ability to understand and manage people" [11]; distinct from academic intelligence; comprises social understanding, social memory, social knowledge [12] · [src:S01](../../INBOX/hi/ia med.md)
- **P136** · `definition` · Emotional intelligence = "ability to reason about and use emotions to enhance thought"; capacity to perceive, monitor, discriminate, manage own and others' emotions [13] · [src:S01](../../INBOX/hi/ia med.md)
- **P137** · `fact` · Problem-solving skills in nurses influenced by perceived academic achievement, solution-focused thinking, and emotional intelligence [14] · [src:S01](../../INBOX/hi/ia med.md)
- **P138** · `fact` · Emotional intelligence components (well-being, self-control, emotionality, sociability) improve nurse work performance: well-being + sociability → task + contextual performance; self-control → task performance; emotionality + sociability → reduced counterproductive behaviors [15] · [src:S01](../../INBOX/hi/ia med.md)
- **P139** · `fact` · Physician emotional intelligence + patient follow-up visits → patient trust; patient-physician relationship mediates trust → satisfaction [16] · [src:S01](../../INBOX/hi/ia med.md)
- **P140** · `fact` · Emotional intelligence is developable state rather than innate trait; social perspective-taking training improves EI over ~6 months of practice [18] · [src:S01](../../INBOX/hi/ia med.md)
- **P141** · `fact` · LLM experiment on video-based emotional intelligence: humans used non-verbal info + context + temporal dynamics + cultural background; LLM relied on specific utterances, interpreted literally, but identified tone/atmosphere/central figures [19] · [src:S01](../../INBOX/hi/ia med.md)
- **P142** · `fact` · LLM performed above population norm in Emotional Awareness test; considered for training tool for mental health patients with emotional awareness impairments [20] · [src:S01](../../INBOX/hi/ia med.md)

### The Patient-Provider-Technology Relationship
- **P143** · `definition` · Emanuel & Emanuel 4 models of patient-physician relationship: (1) paternalistic (guardian), (2) informative (engineer), (3) interpretative (consultant), (4) deliberative (friend) [21] · [src:S01](../../INBOX/hi/ia med.md)
- **P144** · `rule` · Paternalistic model generally considered least appropriate in modern medicine/nursing except when patient explicitly requests provider act on their behalf; undermines patient autonomy [21] · [src:S01](../../INBOX/hi/ia med.md)
- **P145** · `definition` · Narrative medicine = formal approach harnessing patients' stories for diagnostic/treatment purposes using cognitive, symbolic, affective means; sharing illness narrative can be therapeutic; providers + patients collaboratively uncover meaning behind signs, symptoms, values [22] · [src:S01](../../INBOX/hi/ia med.md)
- **P146** · `definition` · Compassion = "attitude of active regard for another's welfare with imaginative awareness and emotional response" [23]; develops when considered core value + sufficient energy/capacity + sustained patient-provider connection · [src:S01](../../INBOX/hi/ia med.md)
- **P147** · `fact` · Introduction of AI transforms dyadic patient-provider relationship → triad; AI can influence provider, patient individually, or overall dynamic of relationship · [src:S01](../../INBOX/hi/ia med.md)

### AI Affecting the Provider
- **P148** · `definition` · From physician perspective, AI can serve as tool, assistant, or peer [24]; as peer → greatest influence on provider; provider must make AI role transparent to patient · [src:S01](../../INBOX/hi/ia med.md)
- **P149** · `tension` · Debate: young providers/novices benefit as AI helps develop skills vs. experienced practitioners better evaluate/appraise AI output → tailoring AI support to different expertise levels advisable [24] · [src:S01](../../INBOX/hi/ia med.md)
- **P150** · `fact` · Less qualified diagnosticians more prone to automation bias, accepting incorrect AI recommendations more readily than skilled colleagues [26] · [src:S01](../../INBOX/hi/ia med.md)
- **P151** · `fact` · Correct AI support = most powerful driver enhancing human diagnostic accuracy; incorrect AI support significantly impairs diagnostic judgment; AI model impact > diagnostic performance + training + work experience [27] · [src:S01](../../INBOX/hi/ia med.md)

### AI Affecting the Patient
- **P152** · `tension` · AI-enabled chatbots for patient counselling = double-edged sword: available 24/7 (helpful) but may build illusion of unjustified reality; LLMs can fabricate patient stories → dangerous for vulnerable patients (e.g., cancer) [29] · [src:S01](../../INBOX/hi/ia med.md)
- **P153** · `obligation` · Overseeing chatbots and AI tools used by patients/consumers becomes imperative; AI-knowledgeable providers must guide patients to use right tools in right situation · [src:S01](../../INBOX/hi/ia med.md)

### AI and Technology Shaping the Patient-Provider Relationship
- **P154** · `rule` · Medicine/healthcare = both art and science (Saunders [30]); AI should shape scientific aspect rather than art component; art of medicine incorporates rules of thumb beyond objective scientific knowledge · [src:S01](../../INBOX/hi/ia med.md)
- **P155** · `tension` · Concern AI could dictate treatments without considering patient priorities/value-plurality → revert to paternalistic practices, undermining autonomy of both providers and patients [31] · [src:S01](../../INBOX/hi/ia med.md)
- **P156** · `tension` · AI promised as time saver for physicians → more empathetic relationships; but no guarantee extra time used for empathy; may be redirected to increase patient throughput [32] · [src:S01](../../INBOX/hi/ia med.md)
- **P157** · `rule` · In provider-patient-AI triangle, AI must prove trustworthiness via reliability (explainability + validity) or high accuracy/certainty; AI becomes meaningful if it preserves good human-to-human empathetic relationship and respects autonomy; AI should not interfere with practicing medicine as art [33] · [src:S01](../../INBOX/hi/ia med.md)

### When AI "Outperforms" Humans
- **P158** · `fact` · AI outperformed clinicians without pertinent formal qualification in clinically less demanding diagnostic task (maceration detection) [34] · [src:S01](../../INBOX/hi/ia med.md)
- **P159** · `fact` · AI outperformed clinical experts in medical licensing exam [35] · [src:S01](../../INBOX/hi/ia med.md)
- **P160** · `fact` · Clinical expertise = formal qualification + training + high self-confidence in clinical capacity; work experience and job title may play minor/no role [34] · [src:S01](../../INBOX/hi/ia med.md)
- **P161** · `fact` · Complex real-world task study (information-gathering + guideline adherence + robustness to info order/quantity): medical doctors achieved significantly higher accuracy in 3/4 conditions; LLMs only matched humans for simplest condition (appendicitis) [35] · [src:S01](../../INBOX/hi/ia med.md)
- **P162** · `fact` · No LLM provided clinically meaningful recommendations for required combination of treatments; LLM accuracy did not increase with more information; changing information order changed LLM diagnostic accuracy [35] · [src:S01](../../INBOX/hi/ia med.md)
- **P163** · `constraint` · Most AI vs. human studies rely on single specialized task paradigm; complex multi-task real-world scenarios reveal different (human-favoring) results · [src:S01](../../INBOX/hi/ia med.md)

### Conclusions: The Caring Imperative
- **P164** · `obligation` · Medical/nursing schools must adopt AI courses or blend AI knowledge with traditional courses; professional associations obligated to offer continuing AI education as field evolves · [src:S01](../../INBOX/hi/ia med.md)
- **P165** · `rule` · Caring imperative should guide AI course development and implementation; patient well-being remains at core of medicine, nursing, healthcare · [src:S01](../../INBOX/hi/ia med.md)
- **P166** · `fact` · Human experts possess singular capability of providing care in authentic and holistic manner; does not preclude AI tool use but professionals must be well equipped for new challenges · [src:S01](../../INBOX/hi/ia med.md)


## Chapter 4 — Leadership for Innovation in AI (McBride)

### Introduction
- **P167** · `definition` · Leadership = inspiring/catalyzing others → achieve institutional mission + shared goals in evolving context by designing new ways of achieving long-held values · [src:S01](../../INBOX/hi/ia med.md)
- **P168** · `definition` · Leadership incorporates 3 views: (a) personal = ability to inspire/catalyze others; (b) institutional mission = meeting goals/outcomes; (c) future-readiness = innovatively addressing challenges from evolving context · [src:S01](../../INBOX/hi/ia med.md)
- **P169** · `fact` · Leadership not defined by administrative title but as complex skill set exercised in service to purpose by all licensed healthcare professionals · [src:S01](../../INBOX/hi/ia med.md)
- **P170** · `fact` · Non-specialist healthcare leaders most likely to decide whether AI solutions get developed, implemented, evaluated, sustained · [src:S01](../../INBOX/hi/ia med.md)
- **P171** · `fact` · Benner's From Novice to Expert (1984) established journey from novice → competent → proficient → expert post-licensure · [src:S01](../../INBOX/hi/ia med.md)

### Career Stages
- **P172** · `definition` · 5 career stages (Dalton/Thompson/Price 1977 + McBride adaptation): (1) Preparation, (2) Independent Contributions, (3) Development of Home Setting, (4) Development of Field/Health Care, (5) Gadfly (Wise Person) Period · [src:S01](../../INBOX/hi/ia med.md)
- **P173** · `definition` · Stage 1 Preparation: central activity = learning; primary relationship = student; theme = assimilating values + knowledge + clinical/inquiry skills · [src:S01](../../INBOX/hi/ia med.md)
- **P174** · `requirement` · IT/AI basics in Preparation stage include: information literacy, computer competencies, information management systems, data analysis, evidence-based information access, data for R&D, virtual assistants, cybersecurity · [src:S01](../../INBOX/hi/ia med.md)
- **P175** · `fact` · TIGER framework provides globally-accepted core competencies in health informatics for nursing; authors note competencies must evolve → continuous learning required · [src:S01](../../INBOX/hi/ia med.md)
- **P176** · `fact` · ACGME Clinical Informatics Milestones track informatics abilities Level 1-5 (novice → expert) for specialty/subspecialty residents/fellows · [src:S01](../../INBOX/hi/ia med.md)
- **P177** · `definition` · Stage 2 Independent Contributions: focus = fledgling abilities → competence; theme = dealing with gap between ideals learned and work-setting realities; involves team building + learning organizational strengths · [src:S01](../../INBOX/hi/ia med.md)
- **P178** · `definition` · Stage 3 Development of Home Setting: focus shifts personal development → organizational development + enhancement of others; theme = building home setting's image/infrastructure/resources; moving from competence → expertise · [src:S01](../../INBOX/hi/ia med.md)
- **P179** · `fact` · Stage 3 professionals most likely to learn change process: getting buy-in, leveraging early adopters, securing resources, stakeholder communication, data collection, institutionalizing practices · [src:S01](../../INBOX/hi/ia med.md)
- **P180** · `tension` · Algorithm bias must be addressed at Stage 3; AI systems may have been developed with limited input from some patient populations · [src:S01](../../INBOX/hi/ia med.md)
- **P181** · `definition` · Stage 4 Development of Field/Health Care: theme = using hard-won authority → create better tomorrow; involves advisory boards, consulting, professional organization leadership, policy lobbying · [src:S01](../../INBOX/hi/ia med.md)
- **P182** · `fact` · APA Office of Health Care Innovation created "Companion Checklist: Evaluation of AI-Enabled Clinical or Administrative Tool" as guide for psychologists integrating AI tools · [src:S01](../../INBOX/hi/ia med.md)
- **P183** · `tension` · Many professional organizations remain oblivious to AI ethical issues (lack of transparency, privacy, accountability, bias, discrimination, safety/security, criminal/malicious use) identified by informatics specialists · [src:S01](../../INBOX/hi/ia med.md)
- **P184** · `definition` · Stage 5 Gadfly (Wise Person) Period: retirement/preferment years; generative without institutional constraints; roles = coach, board member, consultant; push dialogue + challenge thinking · [src:S01](../../INBOX/hi/ia med.md)

### Innovation and the Change Process
- **P185** · `definition` · Innovation = process of bringing new approaches/processes/services/solutions/products/devices with significant positive effect on existing challenges · [src:S01](../../INBOX/hi/ia med.md)
- **P186** · `rule` · Change process 8 steps: (1) establish need for change, (2) assemble leading group, (3) develop + communicate plan, (4) encourage new behaviors + risk taking, (5) communicate with stakeholders, (6) implement + evaluate changes, (7) hardwire new systems, (8) celebrate successes · [src:S01](../../INBOX/hi/ia med.md)
- **P187** · `rule` · Change process begins with "making sense" of need → connect new approach to longstanding values + commitment to excellence so fresh tactic does not seem disassociated from familiar · [src:S01](../../INBOX/hi/ia med.md)
- **P188** · `constraint` · Training required for implementers; "not knowing new technology" must never be depicted as personal limitation — focus on group commitment to quality · [src:S01](../../INBOX/hi/ia med.md)
- **P189** · `rule` · AI-based change should be presented as augmentation to existing practices, not replacement for social connection · [src:S01](../../INBOX/hi/ia med.md)
- **P190** · `rule` · Innovation monitoring requires consistency over time; expect relapses; make it easy for implementers to report problems → address difficulties timely · [src:S01](../../INBOX/hi/ia med.md)
- **P191** · `rule` · Politically wise to frame innovation as pilot study — reminds resistors that adoption depends on demonstrated improvement over existing practice · [src:S01](../../INBOX/hi/ia med.md)
- **P192** · `rule` · Celebrating success includes: sharing outcomes with administrators/stakeholders, annual reports, websites, media, professional meetings, journals → success begets additional achievement · [src:S01](../../INBOX/hi/ia med.md)

### Outlook and Conclusions
- **P193** · `tension` · Need to understand when healthcare provider + AI assistance > unassisted provider or AI alone; concerns about timing of AI assistance, cognitive overload, over-reliance on AI · [src:S01](../../INBOX/hi/ia med.md)
- **P194** · `requirement` · IT/AI basics must be integrated into all leadership-development programs at every career stage regardless of specialty/setting · [src:S01](../../INBOX/hi/ia med.md)
- **P195** · `fact` · AI assistance most effective in data-driven decision-making + administrative tasks; currently lacks emotional intelligence of human connection → leaders must choose wisely which innovations to espouse · [src:S01](../../INBOX/hi/ia med.md)

## Chapter 5 — Implementation Science for AI Projects (Liebe & Hübner)

### Implementation Science as a Framework for AI Integration
- **P196** · `fact` · Few AI applications have progressed beyond experimental use in clinical practice per recent reviews · [src:S01](../../INBOX/hi/ia med.md)
- **P197** · `fact` · AI implementation barriers include: workflow integration, professional acceptance, regulatory requirements, lack of interpretability, model reliability uncertainties, data protection concerns, ethical responsibility · [src:S01](../../INBOX/hi/ia med.md)
- **P198** · `definition` · Implementation science = field dedicated to facilitating structured integration of evidence-based practices (EBPs) into routine healthcare → enhance service quality + effectiveness · [src:S01](../../INBOX/hi/ia med.md)
- **P199** · `fact` · Implementation science acknowledges persistent gap between research findings and practical application; demonstrating effectiveness alone does not ensure adoption · [src:S01](../../INBOX/hi/ia med.md)

### Logic Models in Implementation Science
- **P200** · `definition` · Traditional logic model = structured representation mapping Inputs → Activities → Outputs → Outcomes; helps stakeholders articulate how planned actions → desired short/long-term outcomes · [src:S01](../../INBOX/hi/ia med.md)
