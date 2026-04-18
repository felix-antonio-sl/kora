# Codex Asclepius
<!-- /atomize · 653 proposiciones · 882 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICIÓN, HECHO...), o por entidad -->

<!-- Part I — Introduction -->

## Chapter 1 — Introduction: AI for Improving Healthcare

### AI and Digital Transformation
- [P001] **HECHO** — AI developments are entrenched in digitalization; AI and digitalization shape each other
- [P002] **HECHO** — Without massive EHR adoption hosting digital structured data, no broad-scale analysis of patient demographics, biomarkers, diagnoses, treatments would be possible
- [P003] **DEFINICIÓN** — Learning Health System (LHS) = epitome of striving for improvement of patient services through data; analysis (not always AI-based) is LHS engine
- [P004] **HECHO** — Milestones of digitalization: democratization of information/knowledge, real-time knowledge development, enhanced visualization, cognitive support, connectivity, mobility [1]
- [P005] **DEFINICIÓN** — Democratization of information/knowledge = process of opening previously secluded information to broad public via internet and open-access policies
- [P006] **⚠ TENSIÓN** — DL models simultaneously enable and undermine transparency → black box phenomenon; clinicians cannot explain AI predictions to patients
- [P007] **DEFINICIÓN** — XAI (Explainable AI) = methods developed to achieve greater insight into mechanisms of deep AI models

### Recent Applications from the Real World
- [P008] **HECHO** — AI tools performed equally or superior to human experts in cardiological imaging (scoping review) [2]
- [P009] **HECHO** — DL methods matched human sensitivity and surpassed specificity for lung cancer detection on CT images (scoping review) [3]
- [P010] **HECHO** — In population-wide mammography screening, AI decreased radiologist workload while enhancing screening performance [4]
- [P011] **HECHO** — LLMs became popular in early 2020s for workflow improvement, safer patient care, knowledge extraction
- [P012] **HECHO** — AI-enabled workflow for patient portal messages contributed to time reduction before qualified clinician review [5]
- [P013] **HECHO** — Pipeline using GPT for PubMed literature retrieval + ranking + summarization yielded good results for relevance, quality, accuracy [6]
- [P014] **HECHO** — ChatGPT + Pinecone algorithm extracted knowledge from NIH National Standards for Diabetes Self-Management Education; expert-reviewed tool achieved very high accuracy for patient health literacy [7]
- [P015] **ALCANCE** — AI applications in healthcare cover: operational efficiency, decision support, diagnostic accuracy, advanced interaction, communication, logistical support, workload relief, professional development (scoping review) [8]
- [P016] **REQUISITO** — AI performance and safe use must be evaluated in RCTs and realistic experiments to prove accuracy, sensitivity, specificity, and added value vs. usual procedures

### A Short History of AI in Medicine
- [P017] **HECHO** — AI in medicine started with knowledge-based approach: rules + facts → inference; 1970s database of pharmaceutical/chemical relations deduced drug interactions from pharmacokinetic/pharmacodynamic relationships [9]
- [P018] **HECHO** — MYCIN = expert system for infectious disease diagnosis and therapy selection; incorporated rule acquisition, explanation component, consultation module for physicians [10]
- [P019] **HECHO** — GoCom system recommended medication management of multimorbid patients based on goal-oriented input from clinical guidelines + medical ontologies [11]
- [P020] **HECHO** — Ontology-based CDSS for diabetes used fuzzy rules from AACE/ACE guidelines to propose individual HbA1c target values and recommend antidiabetic medication [12]
- [P021] **HECHO** — Knowledge-based approaches (ontologies, semantic web, decision tables, rules, logic, probabilistic models) remain active research field [13]
- [P022] **HECHO** — ML rooted in: Turing's learning machine concept, perceptron algorithm for binary classification (1940s-1950s), backpropagation idea (1980s) [14]
- [P023] **HECHO** — ML application in healthcare was difficult due to lack of large-scale digital data; now evolving exponentially with EHRs, PACS, observational health data
- [P024] **HECHO** — Crucial parallel trends: rise of DL (neural networks with multiple layers) [15], pretrained AI models, increased computational power, HPC clusters, in-memory computing (e.g., SAP HANA)
- [P025] **⚠ TENSIÓN** — Knowledge-based vs. ML approaches sometimes regarded as opposites (evidence from RCTs vs. observational data), but both strive for knowledge → complementary rather than contrary

### What Is Intelligence?
- [P026] **DEFINICIÓN** — Cattell-Horn-Carroll (CHC) theory: fluid intelligence (inductive/deductive reasoning) + crystallized intelligence (acquired knowledge); Horn added perception/processing, short-term memory, long-term storage/retrieval, speed of processing; Carroll arranged into 3-strata hierarchy with "general intelligence" at top [16]
- [P027] **HECHO** — Human intelligence is agreed to be multidimensional phenomenon [17]
- [P028] **DEFINICIÓN** — Gardner (1983) "Frames of Mind: Theory of Multiple Intelligences" = linguistic, musical, spatial, mathematical-logical, bodily-kinesthetic, personal intelligence; speaks of intelligences in plural [18]
- [P029] **DEFINICIÓN** — Sternberg's meta-intelligence = creative, analytical, practical, wisdom-based approaches collaborate/interact; meta-components: (1) recognize problem, (2) define problem, (3) allocate resources, (4) mentally represent, (5) formulate strategy, (6) monitor strategy, (7) evaluate strategy [19]
- [P030] **DEFINICIÓN** — Human intelligence (Gignac & Szodorai) = maximal capacity to achieve novel goal successfully using perceptual-cognitive processes [17]
- [P031] **DEFINICIÓN** — Artificial intelligence (Gignac & Szodorai) = maximal capacity of artificial system to successfully achieve novel goal through computational algorithms [17]
- [P032] **DEFINICIÓN** — Human learning (Gignac & Szodorai) = demonstrable change in probability/intensity of specific behavior, underpinned by neurological processes and cognitive strategies in response to stimuli [17]
- [P033] **DEFINICIÓN** — Artificial learning (Gignac & Szodorai) = demonstrable change in probability/intensity of specific response/decision-making potential, underpinned by computational algorithms and data [17]
- [P034] **DEFINICIÓN** — Transfer learning = pretrain networks on large unspecific dataset when target dataset is small; meta learning = training procedure for various tasks; autonomous learning = training model of world unsupervised (without labeled data) [20]
- [P035] **HECHO** — AI assistance increased performance of junior readers assessing radiographic knee osteoarthritis images; improved interobserver agreement across all experience levels [21]

### The Promise of Augmenting Human Capacity
- [P036] **HECHO** — Isaac Asimov coined "robotics"; in "Intelligences Together" (1986) criticized trope that AI will inevitably replace humans; argued AI + HI differ and should combine [22]
- [P037] **REGLA** — Value proposition of AI in medicine/healthcare = augment human capacity rather than automate processes and outcomes; especially when clinician is personally liable for decisions
- [P038] **HECHO** — Humans are imperfect: limited attention, memory, reaction time due to sensory, cognitive, time constraints → quest to counterbalance human deficits with intelligent algorithms and vice versa
- [P039] **HECHO** — AI-human partnering improved detection of artery occlusions from CT angiography: sensitivity, specificity, accuracy all improved with AI assistance [23]
- [P040] **HECHO** — AI support improved diagnostic skills of readers irrespective of specialty, beyond what self-training alone achieved [24]
- [P041] **HECHO** — AI support significantly decreased reporting times → improved diagnostic efficiency [25]
- [P042] **REQUISITO** — Need for studies investigating AI-human partnering at cognitive model level incorporating theories of decision-making and mediators (attention, reaction time) [26]
- [P043] **HECHO** — De-professionalization/de-skilling fear contradicted by experienced AI-using clinicians who regarded AI recommendation as complementary view, not undermining profession [27]
- [P044] **⚠ TENSIÓN** — Clinical decision-making: clinicians = "ecologically bound" (selected cues from patient + environment); ML models = "de-bounding" (correlations from large datasets without clinical context) → distinct paths, can reach same conclusions [26]
- [P045] **HECHO** — In supervised ML, humans label training data → forced collaboration; feedback on model output enables mutual augmentation
- [P046] **HECHO** — Robot-assisted surgery most frequently applied for radical prostatectomy worldwide; ≥ 10 AI use cases including haptic feedback for suture breakage, augmented reality for tumor identification, predicting continence [28]
- [P047] **HECHO** — Smart insulin pumps predict glucose level and adjust pump activity based on physical activity level → help type 1 diabetes patients avoid hypoglycemia during exercise [29]
- [P048] **ALCANCE** — Data quality criteria: accuracy (correctness, timeliness, validity), completeness (relevance, no missing values), redundancy (minimality, conciseness, normalization), readability (comprehensibility, clarity), accessibility, consistency (cohesion, no contradictions), usefulness, trust (reliability, data security) [31]

### The Risks of AI
- [P049] **REGLA** — Only high-quality data yield high-quality AI models; data quality cannot be taken for granted, particularly for secondary data use from EHRs
- [P050] **REQUISITO** — Data must be interoperable (structural + semantic) to merge into big data lakes; AI models claiming generalizability require representative multi-center data
- [P051] **HECHO** — Skin lesion AI models require diverse skin types/colors in dataset; correctness of manual data labels susceptible to human errors, prejudices, predilections
- [P052] **RESTRICCIÓN** — Low data quality → AI models insufficient, possibly biased, may perpetuate inequalities at large scale
- [P053] **HECHO** — Data imbalance had stronger deteriorating effect on model performance than data size (accuracy saturated with size) [32]
- [P054] **DEFINICIÓN** — Automation bias = overreliance, under-reliance, or reduced vigilance for errors when using automated systems [26]
- [P055] **HECHO** — Overreliance associated with: high trust in system, lack of self-confidence, time pressure, cognitive overload, demanding tasks [33, 34]
- [P056] **HECHO** — Automation bias → errors of commission (following incorrect algorithmic decision) or errors of omission (not performing task because AI did not suggest it) [33]
- [P057] **HECHO** — Clinicians with low diagnostic skills, no special training, high perceived benefit from CDSS showed trend of automation bias; profession and gender influenced acceptance of wrong recommendations [35]
- [P058] **DEFINICIÓN** — Perfect automation schema = exaggerated high-performance expectations ascribed to AI vs. humans; disappointment → loss of trust; overconfidence → automation bias [36]
- [P059] **HECHO** — Generative AI risk: ChatGPT known to fabricate DOI numbers; ~1/3 of clinical decisions deemed synthetic wound images to be real (clinicians with ≥ moderate knowledge) [37]
- [P060] **DEFINICIÓN** — SHAP (SHapley Additive exPlanation) = model-agnostic method from coalitional game theory showing feature importance for prediction; applies to logistic regression, boosted trees, transformer NLP [38]
- [P061] **DEFINICIÓN** — Grad-CAM (Gradient-weighted Class Activation Mapping) = method showing main activation of algorithm in image via heatmaps [39]
- [P062] **HECHO** — Diagnostic performance of domain experts benefits from XAI (heatmaps juxtaposed with medical images) compared to simple AI [40]
- [P063] **⚠ TENSIÓN** — Alternative view: accuracy of data models more important than full explainability [41]; focus should be on reliability (robust + valid results) [42]; patients not interested in technical intricacies but clinical implications [43]
- [P064] **HECHO** — Risk of skill decay over time using AI may go unnoticed; tasks demanding greater cognitive workload most affected; well-developed clinical skills = antidote against automation bias [44, 35]
- [P065] **REQUISITO** — Regulations/frameworks addressing data protection, security, accountability, liability are of special interest to AI given large sensitive datasets

### From Theory to Practice
- [P066] **HECHO** — SCCM (Society of Critical Care Medicine) established data science campaign for critical care; Panel on Data Harmonization/Sharing defined core data elements using LOINC, OMOP, HL7 FHIR [45]
- [P067] **HECHO** — STANDING Together = international collaboration recommending procedures to assess/declare limitations and biases of datasets; 18 core topics including dataset summary, identity, access, sampling, ethics, governance [46]
- [P068] **HECHO** — CFIR (Consolidated Framework for Implementation Research) + ERIC (Expert Recommendations for Implementing Change) used as templates for AI implementation in radiotherapy; barriers: lack of AI knowledge, lacking trust, low data confidence, lack of stakeholder involvement, research-practice gap [48]
- [P069] **DEFINICIÓN** — TUCAPA scheme of AI literacy: TU = technological understanding, CA = critical appraisal, PA = practical application [49]
- [P070] **HECHO** — Ng et al. extended AI literacy: technical concepts, appraisal, validation, ethics; 3 user levels: consumer, translator, developer [50]
- [P071] **ALCANCE** — Consumer competencies: explain AI/ML, confusion matrix, limitations, accountability, evidence levels; Translator: supervised/unsupervised training, information governance, bias mitigation, clinical endpoints; Developer: training paradigms, synthetic data, interpretable engineering, algorithm analysis [50]
- [P072] **HECHO** — Scoping review identified 3 AI curricula pillars: "AI use", "interpreting results from AI", "explaining results from AI" [51]

### Outlook and Conclusions
- [P073] **REGLA** — Bridging AI and HI requires respecting existence of two distinct worlds; avoid anthropomorphisms (e.g., "hallucinations" instead of "errors")
- [P074] **REGLA** — AI methods/applications must be leveraged under umbrella of human oversight; may stem from ML/data-driven or knowledge-based approaches, or integrate both
- [P075] **REGLA** — Bridging AI + HI denotes deliberating/agreeing on human regulations and frameworks for avoiding detrimental and unethical consequences of AI

## Chapter 2 — Principles of AI and Big Data in Healthcare

### Definitions and Core Concepts
- [P076] **DEFINICIÓN** — AI encompasses computational methods/algorithms designed to perform tasks requiring human intelligence: learning from data, recognizing patterns, making decisions [29]
- [P077] **DEFINICIÓN** — ML = subset of AI; algorithms learn patterns from data, make predictions/decisions without explicit programming; types: supervised, unsupervised, reinforcement learning [3]
- [P078] **DEFINICIÓN** — DL = specialized branch of ML using artificial neural networks with multiple layers; captures complex nonlinear relationships in large unstructured datasets [6]
- [P079] **DEFINICIÓN** — NLP = enables machines to understand, interpret, generate human language; essential for clinical documentation analysis, voice-enabled interfaces [26, 27]
- [P080] **DEFINICIÓN** — Computer vision = AI systems extracting meaningful information from medical images for diagnostics and image-guided procedures [6, 13]
- [P081] **DEFINICIÓN** — Big Data in healthcare = datasets of substantial volume, velocity, variety, complexity (EHRs, imaging archives, genomic sequences, wearable sensor data); exceed traditional analytical capabilities [23]

### Historical Context
- [P082] **HECHO** — MYCIN (1970s) = first notable healthcare AI system; recommended antibiotics based on patient symptoms + lab results [22]
- [P083] **HECHO** — Late 1990s-early 2000s: pivot to data-driven learning as EHRs became ubiquitous; ML classifiers predicted hospital readmission and sepsis risk [3]
- [P084] **HECHO** — 2010s: major inflection with GPU-accelerated DL; CNNs demonstrated radiologist-level accuracy in image classification across radiology, dermatology, pathology [6]
- [P085] **HECHO** — Transformer architectures + self-attention [24] enabled large-scale language/vision models; foundation models BioBERT, Med-PaLM achieved near-expert-level on QA tasks
- [P086] **HECHO** — GANs and diffusion models produce high-fidelity synthetic medical images addressing data scarcity, class imbalance, privacy preservation

### Rule-Based Versus Data-Driven AI
- [P087] **DEFINICIÓN** — Rule-based AI = explicit instructions/rules coded by experts; logical pathways for decision-making; limited by inability to adapt without manual intervention [22]
- [P088] **DEFINICIÓN** — Data-driven AI = ML algorithms identifying patterns from large complex datasets; learns continuously; includes supervised, unsupervised, reinforcement learning [3]
- [P089] **⚠ TENSIÓN** — Rule-based systems offer high transparency but limited adaptability; data-driven (especially DL) perceived as "black boxes" with thousands/millions of parameters → prompted XAI research [1]
- [P090] **DEFINICIÓN** — Hybrid AI = combines rule-based (safety/interpretability) + ML (adaptability); example: TREWS (Targeted Real-time Early Warning System) for sepsis at Johns Hopkins — physiological thresholds trigger alert (rule-based), gradient-boosting model recalibrates risk (data-driven) [12]

### Embodied and Disembodied AI
- [P091] **DEFINICIÓN** — Embodied AI = AI integrated into physical/robotic platforms interacting physically with environment (surgical assistants, rehabilitation devices, patient-care robots)
- [P092] **HECHO** — da Vinci Surgical System = exemplar of embodied AI; enhances surgeon precision, stability, dexterity in minimally invasive surgery [21]
- [P093] **DEFINICIÓN** — Disembodied AI = software-based, no physical presence (virtual assistants, predictive analytics in EHR, CDSS); delivers predictions/recommendations via digital interfaces [3]
- [P094] **HECHO** — Smart insulin pumps blur embodied/disembodied divide: on-body sensors (CGM) + embedded control algorithms, cloud-updated and app-controlled [5]

### From Traditional Statistics to Machine Learning
- [P095] **HECHO** — Traditional statistical methods (linear/logistic regression, decision trees, survival analysis) assume specific data distributions, require predefined hypotheses → highly interpretable but limited for high-dimensional/unstructured data [11]
- [P096] **RESTRICCIÓN** — Traditional methods face limitations with medical images, genomic sequences, free-text clinical notes, EHRs that violate linearity, independence, normality assumptions [3]
- [P097] **HECHO** — Traditional ML (random forests, SVMs, gradient boosting) require less computational power and smaller datasets than DL; more feasible for many clinical tasks [14]
- [P098] **HECHO** — CNNs achieved human-level or superhuman performance detecting lung tumors (CT), breast cancer (mammograms), diabetic retinopathy (retinal scans) [6, 13]

### Generative AI in Healthcare
- [P099] **DEFINICIÓN** — Generative AI = techniques generating new data instances resembling real-world training data; prominent models: GANs, VAEs (variational autoencoders), transformer-based models
- [P100] **HECHO** — GANs employ generator + discriminator in adversarial training → produce synthetic medical images, clinical scenarios, textual data
- [P101] **HECHO** — GANs generate synthetic medical images enhancing training datasets → improved performance/robustness of diagnostic AI; beneficial when real data limited, sensitive, costly [28]
- [P102] **HECHO** — Generative AI in drug discovery: AI-driven molecular modeling → rapid identification/synthesis of novel compounds, significantly reducing time and cost [30]
- [P103] **HECHO** — 2023: FDA released draft guidance on synthetic data for medical-device algorithms; emphasized provenance, fidelity testing, disclosure requirements [8]
- [P104] **RESTRICCIÓN** — Generative AI risks: data bias, ethical oversight gaps, model explainability concerns; synthetic data may perpetuate disparities; must clearly delineate real vs. generated data [4, 25]

### Data-Driven AI: Algorithms, Data, and Explainability
- [P105] **DEFINICIÓN** — XAI techniques LIME (Local Interpretable Model-agnostic Explanations) and SHAP gained prominence for elucidating AI decision-making in healthcare [1]
- [P106] **HECHO** — MitPlan (Michalowski et al.) = AI-driven system for multimorbid patients; offers "Level 3" explanations: why action chosen, why modifications made, how cost/adherence influenced choices → improved physician understanding + trust [17]
- [P107] **HECHO** — LLM Meditron70B tested for auto-generating treatment explanations; matched quality of manually curated explanations in evidence reflection and self-containment; but risk of hallucinations/clinical inaccuracies requiring oversight [18]
- [P108] **REGLA** — Explainability must be actionable, clinically relevant, context-aware; especially in multimorbidity where CDSS must reconcile overlapping/conflicting guidelines
- [P109] **REQUISITO** — FDA increasingly emphasizes explainability + transparency as critical factors evaluating AI-based medical devices/software [9]

### Ethical Considerations and Human Oversight
- [P110] **REQUISITO** — Robust data governance frameworks, secure data handling, clear informed consent processes essential to mitigate privacy risks in AI [25]
- [P111] **HECHO** — AI-driven predictive algorithms shown to exhibit biases systematically disadvantaging racial/socioeconomic groups when training data reflect inequalities [19]
- [P112] **HECHO** — EU AI Act [7] classifies most medical AI as "high-risk" → mandates rigorous quality-management systems, post-market monitoring, transparency artefacts
- [P113] **OBLIGACIÓN** — Ultimate responsibility for patient care must remain with healthcare professionals; human oversight safeguards against AI errors, biases, ethical missteps [23]

### Illustrative Case Studies
- [P114] **HECHO** — CNN-based tools achieved remarkable accuracy detecting breast cancer lesions from mammograms, identifying subtle features humans might overlook [16]
- [P115] **REGLA** — AI radiology tools designed to augment not replace radiologists; provide second opinions or highlight regions of interest for closer review [1]
- [P116] **HECHO** — Hospitals implementing AI-driven early warning systems significantly reduced adverse clinical events via timely alerts → proactive rather than reactive care [3, 20]
- [P117] **HECHO** — ML models analyzing genomic data predict individual responses to therapies, identify genetic predispositions, tailor interventions to genetic makeup [2]
- [P118] **HECHO** — AI models used to predict response to trastuzumab in HER2-positive breast cancer [6]; flag CYP2C19 variants influencing clopidogrel response [3]

### Outlook and Conclusions
- [P119] **HECHO** — Multimodal foundation models fusing imaging, text, waveforms, genomics (e.g., GPT-4-based Med-PaLM Multimodal) promise unified reasoning across disparate data sources
- [P120] **REQUISITO** — Success of multimodal models hinges on federated-learning protocols, synthetic-data safeguards, transparent evaluation benchmarks reflecting real-world diversity
- [P121] **REQUISITO** — AI in healthcare can only be realized through conscientious, transparent, human-centered whole-person integration prioritizing patient/family/community well-being

## Chapter 3 — Human Intelligence and the Caring Imperative

### Principles of Human Decision
- [P122] **DEFINICIÓN** — Expected utility theory = decisions made through purely rational deliberation aiming to maximize expected utility of outcome
- [P123] **DEFINICIÓN** — Prospect theory (Kahneman & Tversky) = people avoid losses in risky decisions; losses perceived as having more significant consequences than equivalent gains; 2 behaviors: risk aversion (gains) + risk seeking (losses) [1]
- [P124] **HECHO** — Framing (gain vs. loss) significantly influences decision-making behavior; heuristics simplify complex facts along with subjective probabilities and values [1, 2]
- [P125] **DEFINICIÓN** — 3 key heuristics: (1) representativeness (probability based on stereotype), (2) availability (frequency/size of class), (3) anchoring (predictions based on reference points) [2]
- [P126] **HECHO** — Dual-system model: System I = fast, automatic, unconscious; System II = slow, effortful, intentional, conscious; only System II accesses capacity-limited working memory [4]
- [P127] **HECHO** — Experts reach conclusions quickly/intuitively (System I); novices require more time analytically (System II); experts may struggle with novel situations requiring adaptation of fast processes [4]

### Translating Principles into Healthcare
- [P128] **DEFINICIÓN** — Regret theory = decisions based on utility appraisal + anticipation of feelings of regret/rejoicing when comparing outcomes of alternative choices [6]
- [P129] **HECHO** — Regret (System I proxy) + utility (System II proxy) model explained physicians treating only patients with very high pulmonary embolism probability → anticipated regret of causing bleeding through anticoagulants; interaction of System I/II → undertreatment or overtreatment [7]
- [P130] **HECHO** — Prospect theory applied to healthcare: loss-aversion framing made individuals accept COVID-19 measures (distancing, vaccination) more readily when messaging emphasized avoiding losses [5]

### Evidence-Based Practice
- [P131] **DEFINICIÓN** — Evidence-based medicine (EBM) = relies on data from epidemiological/biostatistical analyses of patient/population studies; contrasts with habit/tradition; synthesizes findings via meta-analyses into decision aids (odds ratios) [8]
- [P132] **HECHO** — EBM was instrumental in establishing Cochrane Collaboration; evidence-based practice provides common foundation for interprofessional communication, decision-making, sharing responsibilities [8]
- [P133] **REGLA** — Evidence-based practice aims to provide best rational basis (evidence) for decision-making while incorporating personal experience and patient values/preferences
- [P134] **HECHO** — LLMs tested for evidence tasks (PICO extraction, RCT synthesis, simplifying medical texts) show considerable potential but reveal limitations in factual consistency and domain accuracy → human expert oversight still necessary [10]

### Further Concepts: Social and Emotional Intelligence
- [P135] **DEFINICIÓN** — Social intelligence (1920s-1930s) = "ability to understand and manage people" [11]; distinct from academic intelligence; comprises social understanding, social memory, social knowledge [12]
- [P136] **DEFINICIÓN** — Emotional intelligence = "ability to reason about and use emotions to enhance thought"; capacity to perceive, monitor, discriminate, manage own and others' emotions [13]
- [P137] **HECHO** — Problem-solving skills in nurses influenced by perceived academic achievement, solution-focused thinking, and emotional intelligence [14]
- [P138] **HECHO** — Emotional intelligence components (well-being, self-control, emotionality, sociability) improve nurse work performance: well-being + sociability → task + contextual performance; self-control → task performance; emotionality + sociability → reduced counterproductive behaviors [15]
- [P139] **HECHO** — Physician emotional intelligence + patient follow-up visits → patient trust; patient-physician relationship mediates trust → satisfaction [16]
- [P140] **HECHO** — Emotional intelligence is developable state rather than innate trait; social perspective-taking training improves EI over ~6 months of practice [18]
- [P141] **HECHO** — LLM experiment on video-based emotional intelligence: humans used non-verbal info + context + temporal dynamics + cultural background; LLM relied on specific utterances, interpreted literally, but identified tone/atmosphere/central figures [19]
- [P142] **HECHO** — LLM performed above population norm in Emotional Awareness test; considered for training tool for mental health patients with emotional awareness impairments [20]

### The Patient-Provider-Technology Relationship
- [P143] **DEFINICIÓN** — Emanuel & Emanuel 4 models of patient-physician relationship: (1) paternalistic (guardian), (2) informative (engineer), (3) interpretative (consultant), (4) deliberative (friend) [21]
- [P144] **REGLA** — Paternalistic model generally considered least appropriate in modern medicine/nursing except when patient explicitly requests provider act on their behalf; undermines patient autonomy [21]
- [P145] **DEFINICIÓN** — Narrative medicine = formal approach harnessing patients' stories for diagnostic/treatment purposes using cognitive, symbolic, affective means; sharing illness narrative can be therapeutic; providers + patients collaboratively uncover meaning behind signs, symptoms, values [22]
- [P146] **DEFINICIÓN** — Compassion = "attitude of active regard for another's welfare with imaginative awareness and emotional response" [23]; develops when considered core value + sufficient energy/capacity + sustained patient-provider connection
- [P147] **HECHO** — Introduction of AI transforms dyadic patient-provider relationship → triad; AI can influence provider, patient individually, or overall dynamic of relationship

### AI Affecting the Provider
- [P148] **DEFINICIÓN** — From physician perspective, AI can serve as tool, assistant, or peer [24]; as peer → greatest influence on provider; provider must make AI role transparent to patient
- [P149] **⚠ TENSIÓN** — Debate: young providers/novices benefit as AI helps develop skills vs. experienced practitioners better evaluate/appraise AI output → tailoring AI support to different expertise levels advisable [24]
- [P150] **HECHO** — Less qualified diagnosticians more prone to automation bias, accepting incorrect AI recommendations more readily than skilled colleagues [26]
- [P151] **HECHO** — Correct AI support = most powerful driver enhancing human diagnostic accuracy; incorrect AI support significantly impairs diagnostic judgment; AI model impact > diagnostic performance + training + work experience [27]

### AI Affecting the Patient
- [P152] **⚠ TENSIÓN** — AI-enabled chatbots for patient counselling = double-edged sword: available 24/7 (helpful) but may build illusion of unjustified reality; LLMs can fabricate patient stories → dangerous for vulnerable patients (e.g., cancer) [29]
- [P153] **OBLIGACIÓN** — Overseeing chatbots and AI tools used by patients/consumers becomes imperative; AI-knowledgeable providers must guide patients to use right tools in right situation

### AI and Technology Shaping the Patient-Provider Relationship
- [P154] **REGLA** — Medicine/healthcare = both art and science (Saunders [30]); AI should shape scientific aspect rather than art component; art of medicine incorporates rules of thumb beyond objective scientific knowledge
- [P155] **⚠ TENSIÓN** — Concern AI could dictate treatments without considering patient priorities/value-plurality → revert to paternalistic practices, undermining autonomy of both providers and patients [31]
- [P156] **⚠ TENSIÓN** — AI promised as time saver for physicians → more empathetic relationships; but no guarantee extra time used for empathy; may be redirected to increase patient throughput [32]
- [P157] **REGLA** — In provider-patient-AI triangle, AI must prove trustworthiness via reliability (explainability + validity) or high accuracy/certainty; AI becomes meaningful if it preserves good human-to-human empathetic relationship and respects autonomy; AI should not interfere with practicing medicine as art [33]

### When AI "Outperforms" Humans
- [P158] **HECHO** — AI outperformed clinicians without pertinent formal qualification in clinically less demanding diagnostic task (maceration detection) [34]
- [P159] **HECHO** — AI outperformed clinical experts in medical licensing exam [35]
- [P160] **HECHO** — Clinical expertise = formal qualification + training + high self-confidence in clinical capacity; work experience and job title may play minor/no role [34]
- [P161] **HECHO** — Complex real-world task study (information-gathering + guideline adherence + robustness to info order/quantity): medical doctors achieved significantly higher accuracy in 3/4 conditions; LLMs only matched humans for simplest condition (appendicitis) [35]
- [P162] **HECHO** — No LLM provided clinically meaningful recommendations for required combination of treatments; LLM accuracy did not increase with more information; changing information order changed LLM diagnostic accuracy [35]
- [P163] **RESTRICCIÓN** — Most AI vs. human studies rely on single specialized task paradigm; complex multi-task real-world scenarios reveal different (human-favoring) results

### Conclusions: The Caring Imperative
- [P164] **OBLIGACIÓN** — Medical/nursing schools must adopt AI courses or blend AI knowledge with traditional courses; professional associations obligated to offer continuing AI education as field evolves
- [P165] **REGLA** — Caring imperative should guide AI course development and implementation; patient well-being remains at core of medicine, nursing, healthcare
- [P166] **HECHO** — Human experts possess singular capability of providing care in authentic and holistic manner; does not preclude AI tool use but professionals must be well equipped for new challenges

<!-- Part II — Innovation and AI Strategies -->

## Chapter 4 — Leadership for Innovation in AI (McBride)

### Introduction
- [P167] **DEFINICIÓN** — Leadership = inspiring/catalyzing others → achieve institutional mission + shared goals in evolving context by designing new ways of achieving long-held values
- [P168] **DEFINICIÓN** — Leadership incorporates 3 views: (a) personal = ability to inspire/catalyze others; (b) institutional mission = meeting goals/outcomes; (c) future-readiness = innovatively addressing challenges from evolving context
- [P169] **HECHO** — Leadership not defined by administrative title but as complex skill set exercised in service to purpose by all licensed healthcare professionals
- [P170] **HECHO** — Non-specialist healthcare leaders most likely to decide whether AI solutions get developed, implemented, evaluated, sustained
- [P171] **HECHO** — Benner's From Novice to Expert (1984) established journey from novice → competent → proficient → expert post-licensure

### Career Stages
- [P172] **DEFINICIÓN** — 5 career stages (Dalton/Thompson/Price 1977 + McBride adaptation): (1) Preparation, (2) Independent Contributions, (3) Development of Home Setting, (4) Development of Field/Health Care, (5) Gadfly (Wise Person) Period
- [P173] **DEFINICIÓN** — Stage 1 Preparation: central activity = learning; primary relationship = student; theme = assimilating values + knowledge + clinical/inquiry skills
- [P174] **REQUISITO** — IT/AI basics in Preparation stage include: information literacy, computer competencies, information management systems, data analysis, evidence-based information access, data for R&D, virtual assistants, cybersecurity
- [P175] **HECHO** — TIGER framework provides globally-accepted core competencies in health informatics for nursing; authors note competencies must evolve → continuous learning required
- [P176] **HECHO** — ACGME Clinical Informatics Milestones track informatics abilities Level 1-5 (novice → expert) for specialty/subspecialty residents/fellows
- [P177] **DEFINICIÓN** — Stage 2 Independent Contributions: focus = fledgling abilities → competence; theme = dealing with gap between ideals learned and work-setting realities; involves team building + learning organizational strengths
- [P178] **DEFINICIÓN** — Stage 3 Development of Home Setting: focus shifts personal development → organizational development + enhancement of others; theme = building home setting's image/infrastructure/resources; moving from competence → expertise
- [P179] **HECHO** — Stage 3 professionals most likely to learn change process: getting buy-in, leveraging early adopters, securing resources, stakeholder communication, data collection, institutionalizing practices
- [P180] **⚠ TENSIÓN** — Algorithm bias must be addressed at Stage 3; AI systems may have been developed with limited input from some patient populations
- [P181] **DEFINICIÓN** — Stage 4 Development of Field/Health Care: theme = using hard-won authority → create better tomorrow; involves advisory boards, consulting, professional organization leadership, policy lobbying
- [P182] **HECHO** — APA Office of Health Care Innovation created "Companion Checklist: Evaluation of AI-Enabled Clinical or Administrative Tool" as guide for psychologists integrating AI tools
- [P183] **⚠ TENSIÓN** — Many professional organizations remain oblivious to AI ethical issues (lack of transparency, privacy, accountability, bias, discrimination, safety/security, criminal/malicious use) identified by informatics specialists
- [P184] **DEFINICIÓN** — Stage 5 Gadfly (Wise Person) Period: retirement/preferment years; generative without institutional constraints; roles = coach, board member, consultant; push dialogue + challenge thinking

### Innovation and the Change Process
- [P185] **DEFINICIÓN** — Innovation = process of bringing new approaches/processes/services/solutions/products/devices with significant positive effect on existing challenges
- [P186] **REGLA** — Change process 8 steps: (1) establish need for change, (2) assemble leading group, (3) develop + communicate plan, (4) encourage new behaviors + risk taking, (5) communicate with stakeholders, (6) implement + evaluate changes, (7) hardwire new systems, (8) celebrate successes
- [P187] **REGLA** — Change process begins with "making sense" of need → connect new approach to longstanding values + commitment to excellence so fresh tactic does not seem disassociated from familiar
- [P188] **RESTRICCIÓN** — Training required for implementers; "not knowing new technology" must never be depicted as personal limitation — focus on group commitment to quality
- [P189] **REGLA** — AI-based change should be presented as augmentation to existing practices, not replacement for social connection
- [P190] **REGLA** — Innovation monitoring requires consistency over time; expect relapses; make it easy for implementers to report problems → address difficulties timely
- [P191] **REGLA** — Politically wise to frame innovation as pilot study — reminds resistors that adoption depends on demonstrated improvement over existing practice
- [P192] **REGLA** — Celebrating success includes: sharing outcomes with administrators/stakeholders, annual reports, websites, media, professional meetings, journals → success begets additional achievement

### Outlook and Conclusions
- [P193] **⚠ TENSIÓN** — Need to understand when healthcare provider + AI assistance > unassisted provider or AI alone; concerns about timing of AI assistance, cognitive overload, over-reliance on AI
- [P194] **REQUISITO** — IT/AI basics must be integrated into all leadership-development programs at every career stage regardless of specialty/setting
- [P195] **HECHO** — AI assistance most effective in data-driven decision-making + administrative tasks; currently lacks emotional intelligence of human connection → leaders must choose wisely which innovations to espouse

## Chapter 5 — Implementation Science for AI Projects (Liebe & Hübner)

### Implementation Science as a Framework for AI Integration
- [P196] **HECHO** — Few AI applications have progressed beyond experimental use in clinical practice per recent reviews
- [P197] **HECHO** — AI implementation barriers include: workflow integration, professional acceptance, regulatory requirements, lack of interpretability, model reliability uncertainties, data protection concerns, ethical responsibility
- [P198] **DEFINICIÓN** — Implementation science = field dedicated to facilitating structured integration of evidence-based practices (EBPs) into routine healthcare → enhance service quality + effectiveness
- [P199] **HECHO** — Implementation science acknowledges persistent gap between research findings and practical application; demonstrating effectiveness alone does not ensure adoption

### Logic Models in Implementation Science
- [P200] **DEFINICIÓN** — Traditional logic model = structured representation mapping Inputs → Activities → Outputs → Outcomes; helps stakeholders articulate how planned actions → desired short/long-term outcomes
- [P201] **DEFINICIÓN** — Logic model maps assumed theory of change = causal pathway by which intervention expected to bring about change
- [P202] **HECHO** — Logic models can be read upstream (end → beginning) instead of downstream (beginning → end), focusing on desired results and tracing path back to roots of success
- [P203] **HECHO** — Logic models serve as "blueprint" of initiative, enhancing stakeholder communication + guiding systematic evaluation from process/usage measures (outputs) → outcomes

### Transition to the IRLM
- [P204] **DEFINICIÓN** — IRLM (Implementation Research Logic Model) = integrated model combining determinants + implementation strategies + mechanisms of change + outcomes in one framework; extends traditional logic model
- [P205] **HECHO** — IRLM developed because projects sometimes used multiple disparate models, failed to justify how context + actions + results fit together
- [P206] **HECHO** — IRLM adds rigor/transparency by making causal pathways + assumptions explicit → improves scientific rigor, reproducibility, ability to test how/why implementation succeeds
- [P207] **DEFINICIÓN** — IRLM Determinants = contextual factors (barriers/facilitators) influencing implementation success; e.g., organizational structures, provider readiness, patient engagement, resource constraints, stakeholder commitment, workflow alignment
- [P208] **DEFINICIÓN** — IRLM Implementation Strategies = targeted actions to facilitate implementation by addressing barriers + leveraging facilitators; each strategy should correspond to specific determinant
- [P209] **HECHO** — Powell et al. (2015) provide refined compilation of 73 implementation strategies based on expert consensus (ERIC project)
- [P210] **REGLA** — IRLM requires specifying who implements strategies, what actions taken, why — ensuring clear evidence-based rationale for each approach
- [P211] **DEFINICIÓN** — IRLM Mechanisms = processes/mediators/events explaining how implementation strategy → change; clarify causal link between strategy and intended outcomes
- [P212] **HECHO** — Mechanisms can manifest as shifts in determinant factors (e.g., improved organizational climate) or proximal changes (e.g., evolving user attitudes)
- [P213] **HECHO** — Fogg Behavior Model: motivation + ability + triggers → behavior change; applicable as theoretical underpinning for mechanism design in IRLM
- [P214] **DEFINICIÓN** — IRLM Outcomes = 3 categories: (a) implementation outcomes (adoption rates, fidelity, acceptability), (b) service outcomes (efficiency, quality of care, safety), (c) recipient/clinical outcomes (diagnostics, treatment, hospitalizations)

### Key Components of the IRLM
- [P215] **DEFINICIÓN** — IRLM determinants at 3 levels: patient/workforce level, organizational level, macro level
- [P216] **HECHO** — Patient/workforce determinants: trust in AI-driven care (explainability, alignment with human decision-making, AI literacy, data security fears) + clinician AI literacy/trust (training gaps, liability/responsibility concerns)
- [P217] **HECHO** — Organizational determinants: workflow compatibility/EHR interoperability (bias, privacy, security risks) + leadership/institutional commitment (governance policies, AI-friendly infrastructure)
- [P218] **HECHO** — Macro determinants: regulatory uncertainty/liability risks + economic incentives/reimbursement models
- [P219] **HECHO** — Patient/workforce strategies: AI literacy + patient engagement programs (transparency, informed consent) + clinician AI education + decision-support training (simulations)
- [P220] **HECHO** — Organizational strategies: seamless AI integration into clinical workflows (EHR embedding, decision-support pathways) + strong leadership/AI governance policies (multidisciplinary task forces)
- [P221] **HECHO** — Macro strategies: regulatory standardization/liability frameworks + financial incentives/reimbursement mechanisms (value-based incentives)
- [P222] **HECHO** — Patient/workforce mechanisms: increased transparency → trust-building + cognitive alignment → decision augmentation (AI insights aligned with medical reasoning)
- [P223] **HECHO** — Organizational mechanisms: reduced cognitive load + workflow efficiency (AI embedded in EHR) + AI accountability → institutional trust (clear governance → reduced liability concerns)
- [P224] **HECHO** — Macro mechanisms: legal certainty + risk mitigation (regulatory standardization) + economic feasibility/sustainability (reimbursement models)
- [P225] **HECHO** — Implementation outcomes: patient acceptance of AI tools + clinician adoption/sustained use + successful AI system integration + AI governance/compliance adherence + regulatory approval/legal acceptance + economic viability/financial sustainability
- [P226] **HECHO** — Service outcomes: improved patient engagement/self-management + reduced clinician workload/burnout + increased hospital workflow efficiency + higher clinical decision-making accuracy + improved population health monitoring/early disease detection + enhanced healthcare system responsiveness
- [P227] **HECHO** — Recipient outcomes: better health outcomes/quality of life + increased clinician decision confidence/decreased interrater variability + reduction in medical errors/adverse events + better patient-provider communication/shared decision-making + reduction in healthcare disparities + sustainable health system cost reduction
- [P228] **REGLA** — IRLM structured mapping = testable hypothesis: "Implementing Strategy X to address Barrier Y → triggers Mechanism Z → leads to Outcome O"
- [P229] **HECHO** — ML prediction model outperformed statistical scores predicting major adverse events in cardiac ICU (death, resuscitated cardiac arrest, cardiogenic shock) → helped risk stratification
- [P230] **HECHO** — LLM generated better material for patient education + shared decision-making compared to existing sources
- [P231] **HECHO** — Cost simulation for colorectal cancer: AI screening → reduced incidence/mortality rates → cost reductions

### Practical Example: IRLM Applied to Healthcare AI Implementation
- [P232] **HECHO** — Baxter et al. case study: ML model predicting hospital readmissions from age, diagnoses, lab values, medication types, length of stay, past ED visits, past hospitalizations; outperformed widely-used risk score
- [P233] **HECHO** — Baxter et al. determinants: workflow variability, clinician unawareness of tool, hesitancy due to reliance on older risk score, questioned tool relevance, need for training
- [P234] **HECHO** — Baxter et al. strategies: early stakeholder engagement + targeted training + workflow integration → improve clinician acceptance + seamless adoption
- [P235] **HECHO** — Baxter et al. mechanism: closing knowledge gaps + improving workflow compatibility → improved clinician confidence + sustained use
- [P236] **HECHO** — Baxter et al. expected outcome: higher AI model adoption in routine care → reduced hospital readmissions + improved patient outcomes

### Complementary Role of Other Implementation Frameworks
- [P237] **DEFINICIÓN** — NASSS framework examines why digital health innovations fail to scale; focuses on technological complexity, stakeholder dynamics, systemic barriers
- [P238] **DEFINICIÓN** — CFIR (Consolidated Framework for Implementation Research) identifies key implementation determinants: organizational readiness + external influences; useful for understanding barriers/facilitators
- [P239] **DEFINICIÓN** — RE-AIM framework evaluates implementation across: Reach, Adoption, long-term sustainability; broader perspective on intervention impact
- [P240] **REGLA** — NASSS/CFIR/RE-AIM complement (not exclude) logic models; they bridge contextual analysis with structured implementation planning; IRLM translates their insights → actionable strategies

### Human-Centered Implementation Science
- [P241] **DEFINICIÓN** — Human-centered implementation science extends user-centricity into integration/uptake process; prioritizes user needs, workflow integration, training, organizational culture equally with technical installation
- [P242] **REGLA** — Principle 1 "Meeting Users Where They Are": adapt AI to fit existing routines/systems, not expect users to radically change; embed AI alerts into EHR interface; time outputs to clinical decision points; maintain clinician autonomy — AI supports, not overrides judgment
- [P243] **HECHO** — AI tools not woven into clinicians' normal processes quickly fall by wayside (known barrier)
- [P244] **REGLA** — Principle 2 "Training and Support": implementation plans must include robust education/training (formal sessions + quick reference guides + responsive IT support); goal = build user confidence + competence; ongoing support via helpdesk/regular check-ins
- [P245] **HECHO** — AI sepsis early warning system deployment: comprehensive training + communication about AI purpose/workflow essential for frontline staff preparation + smooth adoption
- [P246] **REGLA** — Principle 3 "Champion Engagement + Leadership Buy-In": identify/empower clinical champions (respected end-users who advocate for AI tool); champions communicate benefits to peers + mentor colleagues; organizational leadership support signals change is valued + allocates resources
- [P247] **REGLA** — Principle 4 "Iterative Adaptation + Feedback Loops": treat deployment as iterative process not one-time event; collect user feedback + performance data systematically; use debrief meetings after pilot phases, monitor usage patterns/outcomes, establish accessible feedback channels (surveys)
- [P248] **HECHO** — In one AI deployment, regular meetings with nurses/physicians identified workflow misalignments → modifications in alert escalation pathways to fit clinical roles

### Outlook and Conclusions
- [P249] **⚠ TENSIÓN** — AI applications appear so stunning that attention solely rests on what application achieves + how much better single-task performance vs humans; context/user-driven mindset needed to lead implementation → clinically meaningful success
- [P250] **HECHO** — Past decades witnessed great failures putting grand technology plans into practice (e.g., national eHealth strategies); AI applications carry larger portion of risks including failure risks vs previous technologies
- [P251] **REGLA** — AI applications require environment to be factored in during implementation; measures may be similar to other technologies but impact more crucial due to potential AI harms + benefits
- [P252] **REQUISITO** — Strong need to evaluate overall AI system performance guided by logical models + their pathways toward system impact; context + human-centered designs + ethical considerations = bridge between artificial and human intelligence during implementation/evaluation

<!-- Part III — Case Studies -->

## Chapter 6 — Artificial Intelligence in Dermatology

### Literature Review: AI in Dermatology Over the Past Decade
- [P253] **HECHO** — DL outperformed 136/157 dermatologists in head-to-head dermoscopic melanoma classification task
- [P254] **HECHO** — Esteva et al. (2017) trained CNN on 129,450 clinical images across 2,032 diseases; performed on par with 21 board-certified dermatologists classifying 2 critical skin cancer types
- [P255] **HECHO** — Tschandl et al. (2019) showed ML algorithms outperformed human experts classifying pigmented skin lesions
- [P256] **⚠ TENSIÓN** — AI models face challenges with out-of-distribution images → reduced reliability outside training distribution
- [P257] **HECHO** — AI-assisted tele-dermatology diagnosis improved diagnostic accuracy by up to 12% and reduced unnecessary referrals/biopsies
- [P258] **HECHO** — AI-assisted diagnosis increases agreement between primary care physicians and reference dermatologists

### Use Case: MoleMe
- [P259] **DEFINICIÓN** — MoleMe = AI-powered skin monitoring app launched 2019 in Taiwan by dermatologists + AI researchers; analyzes moles/lesions for early malignancy signs
- [P260] **HECHO** — MoleMe used by > 200,000 users
- [P261] **HECHO** — MoleMe AI core trained on > 30,000 consumer-taken mole images; risk ground truth determined by board-certified dermatologists
- [P262] **HECHO** — Each original image spawned into 20 derived images (different lighting, background hues, sizes, angles) → robust to skin tones + photo-taking skill variation
- [P263] **HECHO** — MoleMe classifies lesions into benign / suspicious / malignant categories
- [P264] **HECHO** — MoleMe integrates telemedicine for remote dermatologist consultations
- [P265] **HECHO** — MoleMe AUC = 0.94 (ROC curve), published in British Journal of Dermatology; outperforms most GPs classifying cutaneous pigmented lesions
- [P266] **HECHO** — MoleMe sensitivity = 0.96, specificity = 0.87
- [P267] **HECHO** — > 90% users satisfied with MoleMe usability + positive impact on daily life
- [P268] **RESTRICCIÓN** — AI-powered medical tools must undergo rigorous validation, clinical testing, approval before deployment; regulatory frameworks favour high-resource environments → barriers for LMICs
- [P269] **⚠ TENSIÓN** — Most AI training data comes from western countries; most dermatology textbook skin images = Type I (white) skin → perpetuates health inequities
- [P270] **REQUISITO** — AI models need sufficient external validations during evaluation to avoid overfitting
- [P271] **REQUISITO** — MoleMe should integrate into pre-visit process of primary care practices for full potential

### Comparative Analysis of AI Dermatology Tools
- [P272] **HECHO** — MoleMe: AI diagnosis=Yes, mobile app=Yes, teledermatology=Yes, regulatory approval=Pending, data training diversity=Moderate
- [P273] **HECHO** — DermEngine: AI diagnosis=Yes, mobile app=Yes, teledermatology=Yes, regulatory approval=Approved, data training diversity=High
- [P274] **HECHO** — SkinVision: AI diagnosis=Yes, mobile app=Yes, teledermatology=No, regulatory approval=Approved, data training diversity=Moderate
- [P275] **HECHO** — MoleMe = only tool of 3 with teledermatology + pending regulatory approval; DermEngine = only tool with high data training diversity

### 4-Stage AI Evolution in Dermatology
- [P276] **DEFINICIÓN** — Stage 1: Predictive (Perception) AI = analyzes medical images to detect patterns + classify skin conditions using DL on large datasets
- [P277] **⚠ TENSIÓN** — Patients require AI to surpass dermatologist-level accuracy or healthcare cost to be unbearable before accepting AI-only assessments
- [P278] **DEFINICIÓN** — Stage 2: Generative AI = GANs + GPT synthesize realistic skin lesion images, enrich training datasets, mitigate annotated image scarcity for underrepresented skin tones
- [P279] **HECHO** — Generative AI enables simulation of disease progression (e.g., nevi → melanoma evolution) for training + patient education
- [P280] **HECHO** — LLMs (ChatGPT) show promise providing secondary opinions on dermatological diagnosis/treatments; limitations persist in medication coding + specificity
- [P281] **DEFINICIÓN** — Stage 3: Agentic AI = shift from passive decision-support → systems autonomously guiding clinical workflows, synthesizing multimodal patient data with minimal human intervention
- [P282] **⚠ TENSIÓN** — Agentic AI deployment must balance efficiency vs care quality, broader access vs preservation of patient-clinician relationships
- [P283] **DEFINICIÓN** — Stage 4: Physical AI = humanoid robots conducting dermatological assessments via advanced image recognition + tactile sensing
- [P284] **HECHO** — Automated robotic devices already explored for hair transplant + energy-based treatments (laser resurfacing, mole removal)
- [P285] **⚠ TENSIÓN** — Psychological acceptance of humanoid robots limited by "uncanny valley effect"

### Ethical and Systematic Considerations
- [P286] **REQUISITO** — AI models trained on inclusive datasets (various skin tones) → more effective global diagnoses (Han et al. 2018)
- [P287] **REGLA** — AI should augment, not replace, human judgement in healthcare (Topol 2019)
- [P288] **REGLA** — "Smarter healthcare systems" should allow AI to continuously learn from EHRs, personalizing care delivery (Norgeot et al. 2019)
- [P289] **⚠ TENSIÓN** — Tele-dermatology AI raises ethical challenges: exacerbation of health disparities due to lack of standardized regulations / informed consent protocols
- [P290] **OBLIGACIÓN** — Ethical principles for AI in dermatology: fairness, inclusivity, transparency, accountability, privacy

## Chapter 7 — AI and CareSmart Assistive Technologies for Long-Term Care

### Introduction
- [P291] **HECHO** — Market research predicts savings up to 8 billion EUR over next decade in AI-based dementia diagnoses alone
- [P292] **HECHO** — AI for elder care first developed in 1990s with first automated monitoring systems for older adults
- [P293] **ALCANCE** — AI in long-term care (LTC) comprises: decision support for medical diagnosis, automated patient data analysis for early detection, robotics as conversational agents, monitoring/surveillance for aging in place
- [P294] **DEFINICIÓN** — AI ageism = bias + exclusions in AI that disadvantage older adults through algorithms/datasets, stereotypes in AI development, lack of aging representation in AI discussions
- [P295] **HECHO** — AI facial recognition systems more prone to errors with faces of older adults
- [P296] **DEFINICIÓN** — Techno-solutionism = assumption that social/structural challenges in care can be fixed through technological innovation alone
- [P297] **⚠ TENSIÓN** — AI implementation in LTC requires careful contextualization; existing applications/guidelines remain too abstract for genuine contextualization

### ALGOCARE Project
- [P298] **HECHO** — ALGOCARE project followed 3 AI technologies from development → implementation in nursing homes: fall-detection sensor, social robot Pepper, robotic seal Paro
- [P299] **HECHO** — Data collected Jul-Oct 2022 + Nov 2023-Jan 2024; studied facilities housed ~100-150 residents
- [P300] **HECHO** — 37 semi-structured interviews conducted: 10 care residents, 14 care staff, 2 care management, 11 AI developers
- [P301] **HECHO** — ~24 hours participant observations performed focusing on daily routines + technology interactions
- [P302] **HECHO** — Analysis conducted using MAXQDA 2022, open coding + situational analysis by 4 researchers

### AI-Based Fall Detection Sensors
- [P303] **HECHO** — ALGOCARE fall detection system used 3D sensors gathering depth data about older adults' movement in rooms; ML algorithms processed data to identify objects/individuals/movements
- [P304] **⚠ TENSIÓN** — Daily activities (sitting on chair, tying shoelaces, fitness exercises) falsely identified as falls → unnecessary alarms disrupting resident lives + care routines
- [P305] **⚠ TENSIÓN** — Major challenge: unavailability of training data on older adults' falls; real-world data hard to collect due to restricted access to diverse older populations
- [P306] **HECHO** — AI developers used synthetic data (motion capture suits worn by developers) as alternative to real-world fall data → separation between AI development + LTC reality
- [P307] **⚠ TENSIÓN** — Synthetic data creation excluded older adults from development process → voices/needs relatively absent in AI development

### The Humanoid Robot Pepper
- [P308] **DEFINICIÓN** — Pepper = 1.2m-tall social robot with human-like body, moveable arms/fingers, wheels; uses microphones, sensors, 3D cameras for navigation/speech/hearing/object+face detection; chest-integrated tablet; produced since 2014
- [P309] **HECHO** — Mishra et al. (2024) tested Pepper functions → found issues with face recognition, navigation, conversation accuracy
- [P310] **HECHO** — Stommel et al. observed miscommunication in all 36 interviews with older adults using Pepper, particularly "trouble hearing" → repetition + frustration
- [P311] **⚠ TENSIÓN** — Pepper adjusted entertainment content based on estimated age + facial expressions → decisions made for older adults rather than by them; positioned older adults as passive users
- [P312] **HECHO** — Pepper use did not ease caregiver workload; required additional staff time/resources to facilitate resident-robot interactions

### The Robot Seal Paro
- [P313] **DEFINICIÓN** — Paro = robotic seal; development began 1993 as activation therapy for older adults, often used with dementia patients; responds to touch + speech; example of emotional robotics
- [P314] **HECHO** — Paro design chosen as baby seal because unfamiliar animals accepted more easily; features: light sensors, touch sensors (head/whiskers/flippers/back/belly), anti-bacterial white coat, "baby face" with large eyes
- [P315] **HECHO** — In Japan > 60% Paro robots owned by private customers; in Europe + US mostly used in public LTC settings
- [P316] **HECHO** — Paro acquisition cost ~6,000 EUR + training costs for care staff
- [P317] **⚠ TENSIÓN** — Paro challenges: infection concerns (non-removable/non-washable fur passed between residents), stigma of interacting with animal robot perceived as "toylike" → infantilization, negative emotional responses (fear/anger)
- [P318] **HECHO** — Paro hardly used during Covid-19 peak phase; care staff feared cross-infection between residents via robot
- [P319] **HECHO** — Paro fur turned yellow over time from repeated disinfectant wipe use
- [P320] **HECHO** — Care staff used Paro to engage older residents in dialogues about past experiences + provided information about how system worked

### Pathways Towards AI-Enriched Long-Term Care
- [P321] **REQUISITO** — Pathway 1: Actively involve older adults in AI development; participatory/responsible innovation strategies not yet fully developed/contextualized for LTC sector
- [P322] **⚠ TENSIÓN** — AI developers used synthetic data / existing datasets as cheaper alternatives → hardly engaged with LTC sector, little knowledge about actual settings → stereotypical assumptions about older adults
- [P323] **REQUISITO** — Pathway 2: Acknowledge both human + technological vulnerabilities; AI technologies need care too (maintenance, cleaning, updates)
- [P324] **HECHO** — AI unlikely to ease LTC staff shortages in short run; effective AI-enriched care requires resources, competences, budgets for everyday AI-care practices
- [P325] **REQUISITO** — Pathway 3: Foster meaningful connections via shared learning spaces where technology developers, care staff, older adults exchange knowledge
- [P326] **REGLA** — AI in LTC = not technological optimization alone; requires social, material, ethical considerations; AI should be part of care network, not replacement for human care
- [P327] **HECHO** — ALGOCARE project funded by Vienna Science and Technology Fund (WWTF) + State of Lower Austria, project ICT20-055

## Chapter 8 — Generative AI to Assist Physicians (Rutledge)

### Introduction
- [P328] **DEFINICIÓN** — Generative AI / LLMs = AI applications using generative methods based on large language models
- [P329] **HECHO** — Pre-LLM AI methods (rule-based expert systems, Bayesian networks, ML) suffered "cliff effect" when confronted with inputs not explicitly in knowledge representation
- [P330] **HECHO** — Largest LLMs embed vast information array → respond appropriately to virtually any human expression
- [P331] **DEFINICIÓN** — Hallucination = LLM fills knowledge gaps with reasonable-sounding output lacking direct support; analogous to confabulation in Korsakoff syndrome

### Foundation Model LLMs Versus Medical LLMs
- [P332] **DEFINICIÓN** — Foundation model LLMs = models with trillions of parameters trained on comprehensive collections of essentially all available electronic documents
- [P333] **HECHO** — Foundation model LLMs (early 2025): Anthropic Claude, OpenAI GPT, Google Gemini, Meta LLaMA, Mistral
- [P334] **HECHO** — Foundation models perform surprisingly well on medical problems despite no specific medical curation
- [P335] **HECHO** — Hallucinations occur where gaps in knowledge exist; medical applications demand minimal confabulation rate
- [P336] **HECHO** — Medical LLMs refine base models with curated reliable medical data to improve scope + minimize confabulation
- [P337] **HECHO** — Medical LLM examples: Google Med-PaLM (medical reasoning/Q&A), Nuance DAX Copilot + AWS Healthscribe (medical scribing → EHR notes), Hippocratic AI (medical conversations), Clinical Camel (open-source on LLaMA)
- [P338] **⚠ TENSIÓN** — Medical LLMs tailored to specific clinical task may be less performant at interpreting patient interview language because underlying foundation model is smaller

### Administrative Simplification — Claims Coding
- [P339] **HECHO** — Fathom + Nym Health use clinical language understanding to fully automate CPT/HCPCS procedure code generation and verify ICD-10 codes support selected procedures
- [P340] **HECHO** — Claims-coding applications trained specifically on structured coding systems (CPT, ICD-10) can use smaller open-source foundation models with incremental training

### Administrative Simplification — Managing Message Queues
- [P341] **HECHO** — Stanford study used Epic MyChart + GPT-3.5 Turbo (triage) + GPT-4 (draft responses); categories = general, results, medications, paperwork
- [P342] **HECHO** — AI draft response used 20% of time; did not reduce average clinician response time
- [P343] **⚠ TENSIÓN** — Clinician reactions heterogeneous: some valued reduced cognitive effort + patient-friendly language; others found AI responses too lengthy / contained irrelevant information
- [P344] **HECHO** — Successful AI message response implementation may require fine-tuning to match each clinician's desired response characteristics

### Clinical Documentation — Chart Review and Summarization
- [P345] **HECHO** — AI-authored summaries of prior medical records = similar quality to clinician summaries but less likely to omit important information + more patient-friendly language
- [P346] **HECHO** — Breast cancer study: AI-generated + AI-assisted summaries better than human summaries; human = 26 min effort vs AI-generated = 1.7 min
- [P347] **HECHO** — Health systems implementing ambient listening medical scribes as first AI use in clinical workflow → reduced after-hours documentation ("pajama time"), reduced cognitive effort

### Clinical Documentation — Ambient Listening
- [P348] **DEFINICIÓN** — Ambient listening = recording + processing audio of doctor-patient encounter → extract relevant clinical features → generate clinical note documenting subjective history + objective findings
- [P349] **HECHO** — Commercial ambient listening applications: Abridge AI, Augmedix, Robin Healthcare, IKS Health
- [P350] **⚠ TENSIÓN** — AI scribes may misinterpret medical terms, omit critical details, fail to capture key clinical findings; larger concern = doctors relying on AI notes without reviewing for gaps
- [P351] **REQUISITO** — AI scribes require very high note completeness/accuracy rate + very low hallucination rate; further studies needed to confirm performance

### Differential Diagnosis
- [P352] **HECHO** — Largest LLMs have sufficient embedded medical knowledge to independently review clinical findings → suggest likely diagnoses; diagnostic performance consistently better than experts
- [P353] **HECHO** — GPT-4 achieved 96% accuracy diagnosing common ambulatory care cases vs 72% for doctors
- [P354] **HECHO** — GPT-4 included correct diagnosis in top-10 differential for 61% of complex cases vs medical residents 44% vs medical faculty 49%
- [P355] **HECHO** — Studies used foundation LLM models (GPT-4) not fine-tuned for medical applications; medical LLMs have not yet demonstrated significantly better diagnostic performance
- [P356] **⚠ TENSIÓN** — Unclear if advances in medical LLMs will outpace advances in general-purpose LLMs; for interpreting patient dialog, general-purpose LLMs are exceptionally capable

### Will AI Replace Doctors?
- [P357] **HECHO** — LLMs fall short at taking patient history: when interacting directly with patients, fail to identify all relevant features → diagnostic performance drops
- [P358] **RESTRICCIÓN** — LLMs lack planning capability to systematically pursue structured inquiry areas (congenital, inflammatory, toxic, traumatic, neoplastic, degenerative etiologies) as physicians do
- [P359] **HECHO** — Without planning abilities, LLMs ask about features present in most likely explanations only, missing systematic coverage
- [P360] **RESTRICCIÓN** — Treatment planning requires considering: confirmatory vs exclusionary testing, observation vs therapeutic trial, cost barriers, patient preferences → beyond current LLM capability
- [P361] **HECHO** — AI not ready to replace doctors but can operate in supervisory capacity: identify care gaps, suggest alternative diagnoses, expand differential, provide background suggestions

### An AI-Based Physician Assistant
- [P362] **DEFINICIÓN** — Dr. A.I. = GPT-4-based virtual physician assistant on HealthTap; conducts pre-visit patient interview via API, generates draft clinical note for doctor
- [P363] **REGLA** — Dr. A.I. does not offer patient any diagnoses or treatment plans; asks questions until no more value, fixed question limit reached, or patient ends interview
- [P364] **HECHO** — Dr. A.I. builds + stores computed differential diagnosis but does not show differential to doctor

### An AI-Based Physician Assistant — Evaluation
- [P365] **HECHO** — Dr. A.I. evaluation: doctor's 1st ICD-10 diagnosis found in Dr. A.I. top-10 differential = 88% (109/124), top-3 = 81% (100/124), top-1 = 62% (77/124)
- [P366] **HECHO** — Doctor's 2nd ICD-10 diagnosis found in Dr. A.I. top-10 = 80% (45/56), top-3 = 61% (34/56), top-1 = 23% (13/56)
- [P367] **HECHO** — Doctor's 3rd-7th ICD-10 diagnoses found in Dr. A.I. top-10 = 46% (25/55), top-3 = 27% (15/55), top-1 = 4% (2/55)
- [P368] **HECHO** — GPT-4-based patient interview diagnoses correspond to high degree with diagnoses assessed by doctors who evaluated patients

### Outlook and Conclusions
- [P369] **REGLA** — GPT-4 cannot be used in medical settings without direct human supervision for foreseeable future
- [P370] **HECHO** — Rapid adoption already occurring: administrative applications, clinical summarization, ambient listening
- [P371] **RESTRICCIÓN** — AI replacing doctors requires: planning capability, understanding individual patient preferences, empathetic/compassionate support for physical/mental distress → remains far off

## Chapter 9 — AI Supporting Nursing Documentation, Workflows and Patient Care (Hovenga)

### Introduction: Artificial Intelligence and Nursing Practice
- [P372] **HECHO** — AI evolution began simultaneously with computing technologies; AI technologies most commonly relate to data + information processing, a core nursing/midwifery function
- [P373] **REGLA** — AI needs big, accurate, complete, unbiased data to provide meaningful results
- [P374] **REQUISITO** — Nursing documentation must adopt global standard language + data structures for point-of-care data to serve as source data for AI applications
- [P375] **ALCANCE** — AI support for nursing covers: patient safety, workflows, demonstrating nursing value, decision support algorithms, resource management, data analytics, continuity of care, cross-organization research, interoperability, person-centred outcomes

### An Important AI Pre-requisite: Quality Data
- [P376] **DEFINICIÓN** — Data quality characteristics = accuracy, consistency, validity, timeliness, accessibility, reliability, completeness, uniqueness, comprehensiveness
- [P377] **REQUISITO** — Generating large datasets for AI requires system interoperability → compliance with agreed technical standards
- [P378] **HECHO** — Author advocates ISO 18104 standard categorial structure to represent nursing practice in terminological systems; linkable to any standard nursing terminology (SNT)
- [P379] **HECHO** — ISO 18104 categories can relate to clinical knowledge models (archetypes) structured per ISO 13606-2:2019 standard in next-generation EHR systems
- [P380] **HECHO** — Model attributes bound to SNTs → used as standard nursing data value sets → optimizes semantic interoperability

### AI Sciences and Technologies
- [P381] **DEFINICIÓN** — AI capabilities stack (Peter & Riemer, 7 levels): 1) pattern recognition, 2) classification, 3) prediction, 4) recommendation, 5) automation, 6) content generation, 7) user interaction (chatbots/avatars)
- [P382] **DEFINICIÓN** — Robot (ISO 8373) = programmed actuated mechanism with degree of autonomy to perform locomotion, manipulation, or positioning; includes control system
- [P383] **⚠ TENSIÓN** — Scanning big data to distinguish/segment based on common elements may produce biased/inaccurate results if data not representative of domain as whole
- [P384] **⚠ TENSIÓN** — Generative AI risks production of deepfakes; recommendation systems risk "group think" based on frequent concept use preventing innovation
- [P385] **REQUISITO** — Computer processing optimal when data standardized at back end; requires cognizance of data supply chain (collection → processing → transfer → linkage → storage → retrieval)

### Use of AI Technologies and Risk Mitigation
- [P386] **HECHO** — Clinical data aggregated/processed for: best practice determination, outcomes monitoring, public health, health system performance reporting
- [P387] **REQUISITO** — Data sharing between systems requires system interoperability + federated clinical data repositories (CDR) operating in coordinated fashion
- [P388] **HECHO** — Data must be labelled/standardized; receiving system must interpret/compute data without losing original meaning (semantics)
- [P389] **HECHO** — Data expressivity = ability to communicate key concepts in contextual computable form; requires evidence-based models per ISO 13606 Part 2 / openEHR specifications
- [P390] **HECHO** — Interoperability standards in use: HL7 FHIR, openEHR archetypes, OMOP CDM

### Foundational Data Concepts and Interoperability
- [P391] **DEFINICIÓN** — Data = re-interpretable representations of information in formalized manner suitable for communication/interpretation/processing (ISO/IEC 11179)
- [P392] **DEFINICIÓN** — Data elements = descriptors of things/concepts/codes; range from atomic to most general level of granularity
- [P393] **HECHO** — Interoperability today achieved via: FHIR, openEHR archetypes, OMOP CDM
- [P394] **HECHO** — openEHR archetypes = object models incorporating context; can model agent behaviours; gathering momentum for next-generation systems
- [P395] **HECHO** — AI use of clinical data requires access to large number of data points available through openEHR methodologies or large proprietary vendors using cloud + AI capabilities
- [P396] **REQUISITO** — Nursing data needs well-defined data models with data elements having defined meaning + format; adoptions require national (ideally global) governance strategies
- [P397] **HECHO** — Degree of interoperability depends on combination of information interchange schema + computing foundations → flow-on impact on trustworthiness of data used by AI
- [P398] **REGLA** — Health professionals remain responsible for actions taken irrespective of advice from any AI system
- [P399] **HECHO** — FDA (US) / TGA (Australia) endorsement of clinical AI applications improves trustworthiness; greater accuracy tolerance acceptable when data used only for administrative purposes
- [P400] **HECHO** — Legacy systems = outdated hardware/software/formats still critically supporting operations; continuing use creates technology debt requiring future reworking
- [P401] **⚠ TENSIÓN** — HIE protocols = short-term fix preventing optimum use of new AI technologies; non-use of SNT prevents nursing from demonstrating service value or using AI effectively

### AI Supporting Nursing Practice — Nursing Documentation and AI Support
- [P402] **REQUISITO** — Nursing documentation via care plans using SNTs = prerequisite to make nursing contribution visible statistically + identify best practice → evidence-based practice standards
- [P403] **HECHO** — "If you can't name it, you can't control it, finance it, research it, teach it, or put it into public policy" (Clark & Lang 1992)
- [P404] **⚠ TENSIÓN** — Some large proprietary EMR systems only provide checklists to nurses (not care plans); few systems have sufficiently large nursing datasets for AI use
- [P405] **HECHO** — Nursing activity recognition systems can automate documentation + extract key clinical info → generate personalized care plans → more time for patient-centred activities
- [P406] **HECHO** — Documentation time significantly increased in US following widespread EHR introduction
- [P407] **REQUISITO** — Next-generation systems need platform supporting model-based patient information abstraction; databases must store scalable data from multiple integrated EHRs compliant with FAIR principles (findable, accessible, interoperable, reusable)
- [P408] **HECHO** — ChatGPT-based LLM integrated into nursing information system in ICU + general ward → significant reduction in documentation time + improved workflow/accuracy + reduced errors
- [P409] **HECHO** — Santos et al. used validated framework prompt → ChatGPT generated nursing care plan suggestions → demonstrated potential as decision support for optimizing cancer care

### Nursing Workflows in a Variety of Settings
- [P410] **DEFINICIÓN** — Nursing workflow = result of multiple factors: technologies in use, communication processes, staff skill mix, location/availability of supplies, equipment, utility room locations, service delivery models
- [P411] **HECHO** — Scoping review found AI (ML + NLP) → better patient monitoring, better clinical decision making, more efficient resource use, individualized treatment programs
- [P412] **HECHO** — AI may reduce human error, automate data entry, enable nurses to spend more time interacting directly with patients

### Nursing Use of Robotics
- [P413] **HECHO** — Nurses tend to favour adopting robotic technologies
- [P414] **DEFINICIÓN** — MINA = Multi-purpose Intelligent Nurse Aid; assists patient mobility, walking support, teleoperation → reduces physical burden on nurses
- [P415] **HECHO** — During COVID-19 pandemic, robots reduced human exposure to infection via remote operations
- [P416] **HECHO** — Patent study: robots for nursing care proliferating; ethnographic study found nursing care robot design largely influenced by sci-fi/cartoon context rather than thoughtful professional discussion
- [P417] **HECHO** — In aged care, humanoid robots provide social/emotional support → alleviate loneliness, improve quality of life
- [P418] **HECHO** — Socially Assistive Robots (SARs) show promise in nursing; nursing home administrators show growing interest but concerns about cost, human interaction, efficacy remain
- [P419] **REQUISITO** — Compassionate care by humanoid robots requires nursing leadership translating nursing + communication + computer science + engineering concepts into robotic care representations
- [P420] **HECHO** — Systematic review: most robotic systems in development/testing phases; nurses need education to work with robotic designers/engineers
- [P421] **HECHO** — Robotics cost-effective long-term: high initial investment offset by automation + reduced manual labor; returns = increased productivity, reduced labour costs, improved quality control, enhanced safety
- [P422] **⚠ TENSIÓN** — Robot integration may cause perceived/real loss of human touch critical in nursing/midwifery; technical limitations + data-driven ethical/privacy concerns + resistance to adoption
- [P423] **HECHO** — Hybrid care models proposed: robots handle routine tasks, humans manage emotionally complex interactions → balance efficiency with empathy
- [P424] **REQUISITO** — Stakeholder engagement (nurses, midwives, patients) during design/deployment of robotic systems is crucial; phased deployment via pilot programs recommended before scaling

### Patient Care and Ethical Considerations
- [P425] **REGLA** — "Primary rule for good policy, law and ethics is sound understanding of scientific data" (Kirby 1989)
- [P426] **HECHO** — WHO 6 ethical principles for AI in healthcare: 1) protect human autonomy, 2) promote well-being/safety/public interest, 3) ensure transparency/explainability/intelligibility, 4) foster responsibility/accountability, 5) ensure inclusiveness/equity, 6) promote responsive/sustainable AI
- [P427] **HECHO** — Australian Medical Association (AMA) + Australian College of Nursing (ACN) each developed position statements for AI
- [P428] **⚠ TENSIÓN** — Delicate balance between AI's transformative potential for patient care vs imperatives of data privacy, ethics, managing data bias, equitable healthcare access
- [P429] **REQUISITO** — AI tools must comply with ISO/IEC 27559:2022 standard = framework for data de-identification mitigating re-identification risks + managing lifecycle of de-identified data
- [P430] **REGLA** — Governance separation between demographic data (identity management) and health data enables ethical data use + allows re-identification when desired for health improvement
- [P431] **REQUISITO** — Transparency required regarding who may access which data for what purposes
- [P432] **OBLIGACIÓN** — Nursing profession must be well represented in every entity/group/committee with mandate to manage AI in healthcare system
- [P433] **REQUISITO** — Nurses need to engage with "roboethics" discourse; introduction of robotics to nursing practice introduces ontological + ethical issues requiring full exploration

### Outlook and Conclusions
- [P434] **HECHO** — AI use to support nursing practice is in its infancy; strong need for nurses/midwives to build communities driving AI research globally
- [P435] **REQUISITO** — When nursing practice area identified as repetitive/time-consuming → consider which combination of AI functionalities (pattern recognition, historical data, prediction, recommendation) best suited to provide support
- [P436] **REQUISITO** — Nurses/midwives must develop ability to decompose tasks + workflows as precursor to exploring AI potential; operational research capability needed for multidisciplinary AI collaboration
- [P437] **REQUISITO** — All users of AI technologies need to be educationally prepared

<!-- Part IV — Challenges and Background -->

## Chapter 10 — Navigating Data Diversity and Equity in Healthcare with AI

### Health Equity
- [P438] **DEFINICIÓN** — Health equity = treating individuals according to their specific health needs/resources, accounting for differences in starting positions
- [P439] **DEFINICIÓN** — Equality = granting same chances/services/resources to all; equity = compensating avoidable differences based on individual social situation
- [P440] **DEFINICIÓN** — Health differences = natural (genetic/physiological) variation; health disparities = man-made, result of systemic/structural inequalities
- [P441] **DEFINICIÓN** — Social determinants of health = non-medical factors (age, gender, ethnicity, socio-economic status) shaping individual health + access to healthcare
- [P442] **HECHO** — Health disparities affect individual opportunities for social participation → matter of social justice, not only medicine

### Bias
- [P443] **DEFINICIÓN** — 3-level bias taxonomy: (1) data bias, (2) algorithmic bias, (3) outcome bias
- [P444] **DEFINICIÓN** — Data bias = training/analysis data inadequately represents population; algorithmic bias = parameters/target variables exclude certain groups; outcome bias = consequence of data/algorithmic bias on clinical decisions
- [P445] **DEFINICIÓN** — Signal problem = signals from certain individuals/groups not detected by algorithm → not represented in model
- [P446] **DEFINICIÓN** — Bias cascade = data bias → algorithmic bias → outcome bias propagating sequentially through pipeline
- [P447] **HECHO** — Friedman & Nissenbaum (1996) distinguished preexisting bias (social practices/attitudes), technical bias (computer system mechanisms), emergent bias (outcomes of analysis)
- [P448] **HECHO** — Obermeyer et al. (2019) found US healthcare algorithm used health costs as main risk parameter → African-Americans assigned lower risk labels because less costs historically invested in them due to structural discrimination
- [P449] **HECHO** — Obermeyer study = exemplar of bias cascade: biased data (cost disparities) → biased algorithm (cost-based risk) → biased outcome (services withheld from African-Americans despite health need)
- [P450] **DEFINICIÓN** — Ontic occlusion = data model ignores trait → individuals with that trait become invisible → exclusion from data causes social exclusion from healthcare services
- [P451] **DEFINICIÓN** — Epistemic injustice in AI = distorted representation of groups in data models → health needs ignored → health disparities exacerbated
- [P452] **DEFINICIÓN** — Algorithmovigilance = strategies for evaluating, monitoring, preventing negative outcomes of AI-based treatments (analogous to pharmacovigilance)
- [P453] **⚠ TENSIÓN** — Bias not only technical; systemic factors + human-algorithm interaction (e.g., variable selection) also cause bias → debiasing must target social practices + structural factors

### Technical Approaches
- [P454] **DEFINICIÓN** — Algorithmic fairness = strategies for bias mitigation in ML applied at pre-processing, in-processing, post-processing phases
- [P455] **DEFINICIÓN** — Importance weighting (pre-processing) = data from underrepresented groups assigned stronger weight/significance in analysis
- [P456] **DEFINICIÓN** — Resampling (pre-processing) = correcting original data by obtaining more diverse subsamples accounting for minority groups
- [P457] **DEFINICIÓN** — Relabeling (pre-processing) = changing ground truth labels to reduce bias
- [P458] **DEFINICIÓN** — Perturbation (pre-processing) = adjusting attribute values so distributions closer together while preserving ranking; iterative until bias < defined threshold
- [P459] **DEFINICIÓN** — In-processing: modify loss function by adding regulation term → penalizes discriminatory error margins; or apply constraints defining max bias level during training
- [P460] **DEFINICIÓN** — Adversarial learning (in-processing) = classification model predicts ground truth while adversary model exploits fairness issues
- [P461] **DEFINICIÓN** — Adjusted learning (in-processing) = external decision makers intervene; classification model learns to abstain from predictions in specific cases
- [P462] **RESTRICCIÓN** — In-processing + post-processing bias mitigation may reduce overall model performance/accuracy
- [P463] **DEFINICIÓN** — Post-processing bias mitigation = modifying output of already-trained models via input correction, classifier correction, or output correction (modifying predicted labels)

### Non-technical Approaches
- [P464] **DEFINICIÓN** — HCAI (Human-Centered AI) = shift focus from algorithms to humans/needs/values; evaluate AI by impact on users + society, not only algorithmic performance
- [P465] **REGLA** — HCAI principle: high automatization must go hand-in-hand with high human control; applications must be reliable, safe, trustworthy
- [P466] **DEFINICIÓN** — Thick data = approach acknowledging social embeddedness of data genesis/collection; data needs contextualization with social background + practices
- [P467] **HECHO** — Thick data operationalized via ethnographic approaches: interviews, social media analysis, stakeholder workshops → contextualizes health data to overcome signal problem
- [P468] **HECHO** — EU AI Act (AIA) adopted 2024 by all EU member states; classifies AI in 3 risk classes (low → high); goes beyond medical product regulation to cover non-medical apps (e.g., ChatGPT)
- [P469] **HECHO** — US: HHS + Office of National Coordinator implemented regulations targeting AI-driven discrimination in healthcare, focusing on algorithmic transparency; supplements FDA regulation under FDCA
- [P470] **⚠ TENSIÓN** — Defining "diversity" per use case is difficult; regulations for data diversity must balance with existing data protection laws (GDPR in EU, HIPAA in US) that limit health data collection
- [P471] **⚠ TENSIÓN** — Horizontal legislation (AIA) intersecting vertical regulation (MDR) → risk of conflicts or unnecessary duplication

## Chapter 11 — Regulatory Frameworks for AI: Legal and Ethical Perspective

### Transparency and Informed Consent
- [P472] **HECHO** — Many AI applications (especially deep learning) function as "black boxes" → healthcare professionals cannot explain decisions → patients cannot make informed choices
- [P473] **⚠ TENSIÓN** — Adaptive AI systems continuously evolve after approval → informed consent once given may no longer be valid if assessment patterns shift
- [P474] **REQUISITO** — Informed consent requires patients comprehend what they agree to; if AI decision-making lacks transparency, this fundamental requirement is undermined

### Bias and Fair Decision-Making
- [P475] **HECHO** — AI-assisted skin cancer diagnoses less accurate for individuals with darker skin tones; ER algorithms may unintentionally reinforce social inequalities
- [P476] **REGLA** — If biases in training data not actively identified/corrected → certain patient groups face systematic disadvantages + research findings lack generalizability

### Liability for AI-Supported Decisions
- [P477] **⚠ TENSIÓN** — AI introduces liability uncertainty: unclear whether responsibility for incorrect diagnoses lies with medical staff, healthcare institutions, or manufacturer
- [P478] **REGLA** — Medical professionals remain responsible for critically evaluating AI-supported recommendations; manufacturers/facilities accountable for system reliability
- [P479] **⚠ TENSIÓN** — Adaptive AI systems evolving after market introduction → liability allocation unclear; absence of clear legal guidelines creates implementation obstacles

### AI and the Role of the Healthcare Professions
- [P480] **REQUISITO** — Healthcare professionals must grasp how algorithms function, critically assess outputs, incorporate into interdisciplinary decision-making

### Data Protection and Research
- [P481] **⚠ TENSIÓN** — Distinction between clinical care and data-driven research increasingly blurred; AI systems evolve through continuous application → patient data used to refine algorithms without explicit consent
- [P482] **⚠ TENSIÓN** — AI models demand extensive/diverse datasets for reliability vs. strict data protection laws limit collection/use of personal data → conflict intensifies in international cross-border research

### Regulatory Framework Conditions in the EU
- [P483] **HECHO** — EU AI regulation = 3 pillars: (1) AI Act (cross-industry safety/transparency/risk), (2) GDPR (data protection), (3) MDR (sector-specific medical devices) + non-binding ethical guidelines

### AI Act: Risk-Based Regulation of AI
- [P484] **HECHO** — EU AI Act = first comprehensive AI regulatory framework in EU; classifies AI systems into 4 risk levels (minimal → high-risk)
- [P485] **ALCANCE** — Most healthcare AI systems fall under high-risk category (assist diagnoses, influence treatment, intervene in medical processes) → strict traceability/transparency/accountability requirements
- [P486] **REQUISITO** — AI Act mandates explainability: medical professionals must understand reasoning behind AI-generated diagnoses/recommendations
- [P487] **OBLIGACIÓN** — AI Act requires developers ensure training data is diverse, representative, robust; mandates mechanisms for bias detection, reduction, regular validation of training datasets
- [P488] **REQUISITO** — High-risk adaptive/self-learning AI must remain under human oversight; no uncontrolled modifications; professionals must be able to review/adjust/override AI decisions
- [P489] **PLAZO** — AI Act provisions implemented gradually starting 2026

### GDPR: Requirements for the Handling of Health Data
- [P490] **REGLA** — GDPR Article 9: health data = specially protected category; processing restricted unless explicit/informed/voluntary consent obtained or legal exemption applies
- [P491] **RESTRICCIÓN** — GDPR purpose limitation restricts data use to clearly defined/legitimate purposes → challenges if AI models need to expand scope or retrain with new datasets
- [P492] **RESTRICCIÓN** — GDPR data minimization requires processing only essential data → conflicts with need for large/diverse AI training datasets
- [P493] **REQUISITO** — GDPR transparency: data controllers must inform individuals how/why data processed, especially in automated decision-making; complex for deep learning systems
- [P494] **REGLA** — GDPR: personal data from EU citizens may only be shared with third countries (e.g., US) if adequate protection level ensured → limits international research collaboration data exchange
- [P495] **HECHO** — Pseudonymization + anonymization used to comply with GDPR while preserving AI training data quality

### MDR: Requirements for AI-Supported Medical Devices
- [P496] **DEFINICIÓN** — MDR risk-based classification: Class I (low risk, admin software, minimal regulation), Class IIa/IIb (medium-high risk, diagnostic/therapy/monitoring, extensive scrutiny), Class III (high risk, independent decisions/active intervention, comprehensive clinical evaluation required)
- [P497] **REGLA** — MDR: manufacturers must demonstrate safety/effectiveness via technical documentation + clinical evaluation + risk management protocols regardless of risk class
- [P498] **REGLA** — MDR: Class I devices → self-declaration by manufacturer; Class IIa+ → conformity assessment by notified body (external accredited inspector)
- [P499] **OBLIGACIÓN** — MDR mandates post-market surveillance (PMS) for continued safety/performance of AI medical devices; especially critical for adaptive AI with continuous learning
- [P500] **REQUISITO** — MDR: adaptive AI deployed post-market must remain compliant with regulatory standards; requires ongoing testing + regular reassessments if significant modifications occur

### Ethical Guidelines for AI in the EU
- [P501] **HECHO** — EU ethical guidelines for trustworthy AI are non-binding but set best practices; emphasize human-centric design, fairness/non-discrimination, accountability, data protection/transparency
- [P502] **REGLA** — AI Act prohibits autonomous decision-making in high-risk AI; ethical guidelines go further → AI must not create dependency or reduce medical staff responsibility
- [P503] **HECHO** — Many EU companies voluntarily follow ALTAI (Assessment List for Trustworthy AI) or participate in EU AI Alliance to implement ethical standards

### Medical Device Regulations and the Role of the FDA
- [P504] **DEFINICIÓN** — SaMD (Software as a Medical Device) = stand-alone AI applications (diagnostic algorithms, therapy planning); SiMD (Software in a Medical Device) = software integrated into physical devices (imaging, surgical assistance)
- [P505] **HECHO** — FDA = primary US regulatory authority for AI healthcare applications; oversees approval/monitoring of SaMD + SiMD
- [P506] **HECHO** — FDA categorizes AI medical devices by risk/clinical significance: low-risk (admin software, general standards only) → higher-risk (diagnosis/treatment, formal approval) → high-risk (cancer detection, surgical assistance, rigorous testing)
- [P507] **DEFINICIÓN** — FDA Predetermined Change Control Plan = manufacturers pre-register planned modifications → post-approval algorithm updates without full re-review per change
- [P508] **⚠ TENSIÓN** — FDA Predetermined Change Control Plan accelerates AI development but raises concerns about long-term oversight/traceability vs. EU AI Act mandates continuous validation of learning systems

### Data Protection Framework Conditions (US)
- [P509] **ALCANCE** — HIPAA governs Protected Health Information (PHI); applies only to "Covered Entities" (hospitals, insurers, healthcare providers) → many AI developers/tech companies (health apps, wearables, AI diagnostics) not subject to HIPAA
- [P510] **HECHO** — HIPAA allows broader/more flexible data use than GDPR: health data can be leveraged for AI model development/optimization without same restrictions as EU
- [P511] **HECHO** — US lacks uniform federal data protection framework; state-level laws (CCPA, CPRA in California) grant additional consumer rights but apply only within their state → inconsistent landscape

### Ethical Guidelines and Voluntary Self-Regulation (US)
- [P512] **HECHO** — NIST AI Risk Management Framework offers recommendations on fairness/transparency/security but carries no legal weight
- [P513] **HECHO** — Biden administration Blueprint for an AI Bill of Rights promoted human-centric AI principles (data protection, security, non-discrimination) but served only as guidance, no legal obligations

### Comparison: Regulatory Approach
- [P514] **HECHO** — EU = preventive, risk-based, uniform framework (AI Act + MDR + GDPR); US = sector-specific, market-driven, flexible (FDA + HIPAA)
- [P515] **HECHO** — EU: manufacturers liable for high-risk AI, unclear for evolving AI; US: doctors/hospitals liable for AI errors, manufacturers only for clear product defects
- [P516] **HECHO** — EU mandates transparency/explainability for high-risk AI; US has no legal transparency mandate → voluntary industry self-regulation
- [P517] **⚠ TENSIÓN** — EU rigorous compliance process slows innovation; US flexible system accelerates deployment but → greater uncertainty for patients/providers (no consistent bias mitigation/monitoring requirements)

### Data Protection Comparison
- [P518] **HECHO** — GDPR data minimization + purpose limitation restrict AI training; HIPAA applies only to covered entities → many tech companies processing health data not subject to HIPAA
- [P519] **⚠ TENSIÓN** — GDPR opening clauses allow EU member states supplementary regulations → further fragmentation within EU despite uniform framework design
- [P520] **⚠ TENSIÓN** — International health data exchange hampered: EU entities must comply with strict GDPR; US lacks equivalent comprehensive framework → legal discrepancies hinder cross-border research + may disadvantage EU companies globally

### Liability for AI Decisions
- [P521] **REGLA** — EU: primary liability on manufacturers of high-risk AI (AI Act + MDR); doctors must independently verify AI recommendations; uncertainty if self-learning AI alters decisions post-market → unclear if re-certification required
- [P522] **REGLA** — US: no specific AI liability regulation; governed by general product liability + medical malpractice; doctors primarily liable for adopting incorrect AI recommendation; manufacturers liable only if clear product defect demonstrated
- [P523] **HECHO** — FDA Predetermined Change Control Plan allows post-approval AI model updates without full re-evaluation → approved AI may change decision-making without new regulatory review

### Outlook and Future Challenges
- [P524] **⚠ TENSIÓN** — EU AI Act uncertainty: how much can approved AI system evolve before requiring recertification; practical implementation challenges remain
- [P525] **DEFINICIÓN** — Regulatory sandboxes = controlled environments where new AI technologies tested before final market approval; proposed solution for balancing innovation + oversight
- [P526] **HECHO** — XAI (Explainable AI) increasingly important for regulatory compliance with accountability + patient education requirements
- [P527] **HECHO** — Federated learning + privacy-preserving AI models = potential solutions for leveraging large health datasets while complying with privacy regulations
- [P528] **⚠ TENSIÓN** — GDPR national opening clauses → member states impose varying requirements on medical data processing → AI companies in some EU countries have easier access to health data than others
- [P529] **⚠ TENSIÓN** — Divergent regulatory requirements across EU, US, China, Japan complicate development/deployment of globally applicable AI solutions; lack of equivalent international guidelines hinders parallel approvals
- [P530] **REQUISITO** — Future EU regulation may need greater coordination between AI Act, MDR, GDPR to reduce overlaps/contradictions; adapting data protection to learning AI systems = central focus (purpose limitation + subsequent health data use)

## Chapter 12 — Ethical Theories for AI in Healthcare

### Ethics Concepts and Theories
- [P531] **DEFINICIÓN** — Common morality = rules about right/wrong conduct widely accepted across cultures and moral traditions; includes prohibitions against lying, stealing, causing harm
- [P532] **DEFINICIÓN** — Utilitarianism = moral worth of actions determined by consequences/outcomes; action ethical if benefits exceed harms; derives from John Stuart Mill
- [P533] **HECHO** — Public health policies often rely on utilitarian framework, e.g., promoting vaccines with side effects for few while benefiting many
- [P534] **REGLA** — Utilitarian approach to AI requires critical examination of both favorable and adverse consequences, including over-reliance on AI and biased outcomes affecting marginalized groups
- [P535] **DEFINICIÓN** — Deontology = adherence to moral duties/rules; certain actions inherently right or wrong regardless of consequences; derives from Immanuel Kant
- [P536] **OBLIGACIÓN** — Deontological approach: healthcare providers must ensure patients fully informed about AI role in care, potential benefits/risks, even if AI improves diagnostic accuracy
- [P537] **DEFINICIÓN** — Virtue ethics = emphasizes character and desirable moral qualities of decision-makers; shifts focus from rigid rules or consequences; derives from Aristotle
- [P538] **REGLA** — Virtue ethics requires cultivating compassion, integrity, fairness in healthcare professionals navigating AI; physician must consider ethical implications of AI recommendations on patient well-being
- [P539] **DEFINICIÓN** — Principlism (Four Principles Approach) = framework derived from Beauchamp & Childress combining 4 principles: beneficence, non-maleficence, respect for autonomy, justice/fairness
- [P540] **DEFINICIÓN** — Beneficence = moral obligation to act to benefit others
- [P541] **DEFINICIÓN** — Non-maleficence = moral obligation to avoid or prevent harm to others
- [P542] **DEFINICIÓN** — Respect for autonomy = obligation to honor individual's right to determine what is in their best interests
- [P543] **DEFINICIÓN** — Justice/Fairness = obligation to ensure benefits and burdens distributed fairly; equals treated equally, unequals treated appropriately per norms of just society

### Ethical Concerns Associated with AI in Healthcare
- [P544] **DEFINICIÓN** — Patient-centered care = providing care respectful of and responsive to individual patient preferences, needs, values; patient values guide all clinical decisions (Institute of Medicine / National Academy of Medicine)
- [P545] **HECHO** — Community-centered care requires consideration of social determinants of health (SDOH) and community values for policy-making when adopting AI tools
- [P546] **DEFINICIÓN** — Equity (AHRQ) = providing care that does not vary in quality because of gender, ethnicity, geographic location, socioeconomic status
- [P547] **HECHO** — AI systems trained on data not fairly representing diverse populations may perpetuate/exacerbate health disparities; studies show humans inherit AI biases
- [P548] **OBLIGACIÓN** — Patients must be informed when AI influences their care; clinician obligated to advise patient of AI recommendation and ensure patient understands reasons for accepting/rejecting it
- [P549] **⚠ TENSIÓN** — Current consent processes may be inadequate when patients/providers do not fully understand AI technology involved
- [P550] **HECHO** — PHI in electronic databases presents potential for accidental/criminal release; very limited effective regulatory oversight of AI data security at present

### Accuracy and Interpretability
- [P551] **HECHO** — AI can fabricate data appearing authentic (hallucinations), use wrong data, or ignore relevant data → flawed outputs with potential for harm
- [P552] **HECHO** — Consensus: AI not ready for unsupervised use in most clinical settings due to inability to reliably identify errors or prevent hallucinations
- [P553] **DEFINICIÓN** — Interpretability = ease with which humans can understand and rely on AI recommendations/decisions; sine qua non for trust and usability in clinical setting

### Accountability and Responsibility
- [P554] **HECHO** — Parties involved with AI in clinical setting: healthcare providers, AI developers (individual/corporate), implementing institutions; clear lines of accountability essential for patient safety
- [P555] **REGLA** — Clinician who relies on AI must own responsibility for ethical/legal ramifications of AI-based decisions
- [P556] **OBLIGACIÓN** — AI developers bear responsibility for ensuring technologies safe, reliable, free from bias, used appropriately; must conduct rigorous testing, maintain transparency, regularly update systems
- [P557] **REQUISITO** — Governments/regulators must establish clear regulatory frameworks defining roles/responsibilities of stakeholders in AI development and deployment; address data privacy, algorithmic transparency, liability
- [P558] **REQUISITO** — Education/training for clinicians on technical aspects of AI models and ethical implications must be provided
- [P559] **REQUISITO** — Collaboration between AI developers, healthcare providers, patients, ethicists, business interests, regulatory bodies must be required to facilitate accountability

### Erosion of Trust and the Clinician Patient Relationship
- [P560] **⚠ TENSIÓN** — AI integration risks diminishing personal aspect of healthcare; patients may feel interacting with machines rather than human caregivers → reduced open communication
- [P561] **⚠ TENSIÓN** — Reliance on AI may lead to complacency among healthcare professionals, undermining cognitive/procedural skills, clinical judgment and expertise

### Evaluate AI's Impact on Patient Care
- [P562] **HECHO** — Most successful AI diagnostic uses: assessing visual images (radiologic, ophthalmologic, dermatologic); AI can match/surpass radiologists in certain contexts
- [P563] **RESTRICCIÓN** — AI image interpretation not yet at accuracy/reliability level to dispense with human clinician oversight; cognitive diagnosis AI not nearly as evolved
- [P564] **HECHO** — AI can personalize treatment plans using medical records, genetic information, lifestyle factors, personal health monitoring devices

### Monitoring AI in Healthcare
- [P565] **REQUISITO** — Continuous AI oversight via: regular audits of algorithms/transformers, monitoring discrepancies between AI recommendations and actual outcomes, human oversight in decision-making
- [P566] **REQUISITO** — Clear performance metrics must be established for assessing reliability/accuracy of AI recommendations over time
- [P567] **REQUISITO** — AI developers must provide clear documentation of data/methodologies used to train AI systems and how systems arrive at conclusions; accessible to healthcare professionals
- [P568] **REQUISITO** — Feedback loops allowing healthcare professionals to report adverse outcomes/concerns about AI systems must be implemented

### Guidelines to Effect Ethically Responsible Use of AI
- [P569] **HECHO** — WHO (2021) released draft report outlining 6 core principles for ethical AI use in health, emphasizing fairness, transparency, accountability
- [P570] **DEFINICIÓN** — WHO 6 core principles: (1) protect autonomy; (2) promote human well-being, safety, public interest; (3) ensure transparency, explainability, intelligibility; (4) foster responsibility/accountability; (5) ensure inclusiveness/equity; (6) promote responsive/sustainable AI
- [P571] **HECHO** — FDA established frameworks for regulating AI/ML software as medical devices: premarket assessment, post-market surveillance, focus on accurate/reliable results
- [P572] **HECHO** — EU GDPR establishes principles for data protection/privacy impacting AI in healthcare: informed consent, data minimization, individual rights
- [P573] **HECHO** — No comprehensive standardized ethics guidelines specifically tailored to unique challenges of AI in healthcare exist yet

### Proposed Ethical Guidelines for AI in Healthcare
- [P574] **REGLA** — Guideline 1 (Transparency): AI algorithms must be transparent; clear documentation of data used, rationale behind recommendations, limitations
- [P575] **REGLA** — Guideline 2 (Accountability): Healthcare providers, AI developers, organizations must be held responsible/accountable for AI system outcomes
- [P576] **REGLA** — Guideline 3 (Fairness/Equity): AI must minimize bias, ensure equitable access; requires diverse training data reflecting patient demographics + monitoring for disparities
- [P577] **REGLA** — Guideline 4 (Informed Consent): Patients must be fully informed about AI use in care, risks, benefits, data usage; consent processes must be clear/understandable
- [P578] **REGLA** — Guideline 5 (Data Privacy/Security): Robust measures required to protect patient data — secure storage, anonymization, strict access controls, compliance with privacy regulations
- [P579] **REGLA** — Guideline 6 (Continuous Monitoring): AI systems subject to ongoing evaluation — regular audits, safety assessments, updates reflecting latest medical knowledge
- [P580] **REGLA** — Guideline 7 (Stakeholder Engagement): Wide range of stakeholders (patients, providers, developers, ethicists, regulators, policymakers) must be engaged in guideline development
- [P581] **REGLA** — Guideline 8 (Training/Education): Healthcare professionals must receive training on ethical implications of AI — technical understanding + moral/social responsibilities
- [P582] **REGLA** — Guideline 9 (Institutional Policies): Healthcare organizations must develop internal policies aligned with ethical guidelines; establish ethics committees to review AI projects
- [P583] **REGLA** — Guideline 10 (Regulatory Frameworks): Governments/regulatory bodies must create comprehensive legal frameworks — standards for AI, compliance monitoring, accountability enforcement

### Monitoring Ethical Guidelines
- [P584] **REQUISITO** — Independent oversight bodies must be established to oversee AI implementations: review compliance, conduct audits, address ethical concerns with appropriate authority
- [P585] **REQUISITO** — Feedback mechanisms: channels for providers/patients to report AI concerns fostering transparency/accountability
- [P586] **REQUISITO** — Public reporting: regular reports on AI outcomes, biases, ethical considerations including metrics on patient care impact
- [P587] **REQUISITO** — Performance metrics assessing patient safety, treatment efficacy, equity, transparency must be established for AI evaluation
- [P588] **REQUISITO** — Patient/provider surveys must be conducted regularly to assess experiences with AI technologies
- [P589] **REQUISITO** — Longitudinal studies needed to assess AI impact on patient care over time, identifying trends/benefits/ethical issues

### Four-Box Approach
- [P590] **DEFINICIÓN** — Four-Box Approach = ethical analysis tool for AI concerns combining Beauchamp & Childress 4 principles + WHO 6 core principles; adapted from Jonsen et al.
- [P591] **ALCANCE** — Box 1 (Technical Indications) addresses beneficence/non-maleficence: AI ethics issue identification, goals, alternatives, success probabilities, least harmful option
- [P592] **ALCANCE** — Box 2 (Preferences of Patient or Other Beneficiary) addresses autonomy: POB informed of benefits/risks/alternatives, decisional capacity, preferred option, valid reasons to override
- [P593] **ALCANCE** — Box 3 (Quality of Outcomes) addresses beneficence/non-maleficence/autonomy: prospects with/without tool, bias detection (conscious/unconscious/unknown + power relationships), quality-of-outcome assessments
- [P594] **ALCANCE** — Box 4 (Contextual Features) addresses justice/fairness: conflicts of interest, cost-effectiveness, third-party stakes, resource allocation, legal/regulatory/research/public health factors
- [P595] **RESTRICCIÓN** — Four-Box Approach is suggested, not rigorously vetted in practice

<!-- Part V — Conclusions and Outlook -->

## Chapter 13 — Data as Bridge Builders (Hübner et al.)

### Data: A Short Summary of the Previous Chapters
- [P596] **DEFINICIÓN** — Dataware = data as fourth pillar of digitalization alongside hardware, software, peopleware; data serve as representatives of physical world and essence of AI model training
- [P597] **HECHO** — AI converging from human heuristics/explicit knowledge → data-driven methods; ML/deep learning = prevailing paradigm where learning through algorithms and data = agency of acting intelligently
- [P598] **HECHO** — In augmentation scenario humans produce/procure real-world data per standards, label data for supervised AI, assess dataset limitations/biases, check outputs
- [P599] **⚠ TENSIÓN** — "Datafication" misconceived as losing human touch of caring; describing entities through data does not preclude emotional/empathetic treatment
- [P600] **HECHO** — Data = asset of organization; medical/nursing knowledge developed upon it; asset management = obligation of new leadership
- [P601] **REQUISITO** — When buying AI tools, thorough understanding of underlying data and quality essential to appraise limitations/benefits; when developing models, high-quality data = key determinant of success
- [P602] **HECHO** — Interoperability embraces technical aspects (protocols), semantic aspects (terminology/coding), data model aspects (properties, structure, interrelationships)
- [P603] **HECHO** — Data biases cause invalid AI models and exacerbate health disparities; result from incorrect, inconsistent, irrelevant data, meaningless variables, missing data
- [P604] **HECHO** — In supervised learning, human expert data labeling is cumbersome and error-prone; biases must be accompanied by metadata describing provenance/formation
- [P605] **OBLIGACIÓN** — Healthcare professionals must evolve from passive consumers to active participants in data evaluation; liability for diagnostic/treatment/care decisions puts them in "driver's seat"
- [P606] **HECHO** — When non-anonymized data processed, informed consent required by law in many countries (absent legal base for processing); data protection laws directly impact opportunities for AI model training
- [P607] **⚠ TENSIÓN** — Breakneck speed of AI developments often exceeds time needed for ethical discourses and laws to be put in place

### The Nature of Medical and Health Data
- [P608] **REGLA** — "More data → better models" demonstrated outside healthcare; routine patient data different due to sensitivity restrictions limiting sheer number
- [P609] **RESTRICCIÓN** — EU GDPR: access to non-anonymized personal data only permitted by law or via patient informed consent; data use beyond original purpose requires patient permission
- [P610] **RESTRICCIÓN** — US HIPAA protects patient health information in corresponding way to GDPR
- [P611] **HECHO** — Rare diseases inherently limit available data volume; manual expert labeling costs/time can also lead to small datasets
- [P612] **DEFINICIÓN** — Overfitting (small dataset problem) = learning from noise/details specific to dataset → poor performance on new unseen data
- [P613] **DEFINICIÓN** — Lack of generalization (small dataset problem) = model does not capture diversity/variability of underlying data distribution → less effective in real-world applications
- [P614] **DEFINICIÓN** — Bias in dataset (small dataset problem) = skewed/discriminatory models → poor performance on new/unseen data
- [P615] **DEFINICIÓN** — Limited feature representation (small dataset problem) = important features/patterns missing → incomplete models
- [P616] **DEFINICIÓN** — Unreliable evaluation metrics (small dataset problem) = standard metrics (accuracy, loss) may not reliably reflect actual model performance → unclear performance
- [P617] **HECHO** — Mitigation methods for small datasets: transfer learning (pre-training on large general datasets like ImageNet), data augmentation including synthetic data, cross-validation
- [P618] **HECHO** — Data spread across departments/institutions/regions/countries not interoperable = additional cause of small effective datasets
- [P619] **HECHO** — Common international health IT standards: HL7 FHIR, openEHR; terminologies: SNOMED CT
- [P620] **DEFINICIÓN** — OMOP = Observational Medical Outcomes Partnership; aims to standardize healthcare data for large-scale observational studies by creating consistent format from diverse sources (EHRs, claims, registries)
- [P621] **DEFINICIÓN** — OMOP CDM = Common Data Model defining standardized structure for healthcare data: tables for conditions, drugs, procedures, measurements, observations, devices, specimens, visits, provider
- [P622] **HECHO** — OMOP CDM comprises: standardized clinical data, standardized health system, standardized health economics, standardized vocabulary, standardized derived data, standardized metadata, results schema
- [P623] **HECHO** — OMOP employs standardized vocabularies: SNOMED CT for clinical terms, LOINC for laboratory tests
- [P624] **HECHO** — Once OMOP CDM-compliant data available, open-source tools for data quality/characterization can be applied for exploratory and hypothesis-driven analyses
- [P625] **DEFINICIÓN** — FAIR = Findable, Accessible, Interoperable, Reusable; principles for standardization, interoperability, good organization of data
- [P626] **DEFINICIÓN** — Findable = datasets registered with unique identifiers and indexed in searchable databases; example: DRYAD repository
- [P627] **DEFINICIÓN** — Accessible = crucial health data available when needed while respecting privacy/security regulations; example: HIPAA/GDPR implementations
- [P628] **DEFINICIÓN** — Interoperable = implementing standardized data formats and healthcare communication protocols; example: HL7 FHIR, SNOMED CT
- [P629] **DEFINICIÓN** — Reusable = datasets under open licenses with detailed documentation/metadata on collection methods and context; example: DRYAD repository
- [P630] **HECHO** — FAIRification process = centerpiece of research data management; applies to metadata, data, supporting infrastructures (e.g., search engines)
- [P631] **HECHO** — Findability/accessibility implemented at metadata level; interoperability/reuse requirements address data level

### Data Quality Is First
- [P632] **DEFINICIÓN** — Accuracy = degree data correctly describes real-world object/event; expressed as structural accuracy (syntactic + semantic) and time-related accuracy (currency, volatility, timeliness)
- [P633] **HECHO** — Accuracy metric: percentage of data entries without errors
- [P634] **DEFINICIÓN** — Completeness = extent data are of sufficient breadth, depth, scope for task at hand; missing values/tuples/attributes/relations; temporal dimension = completability
- [P635] **HECHO** — Completeness metric: ratio of filled data fields vs total fields or percentage of missing values; completability measured by growth rate of completeness over time
- [P636] **DEFINICIÓN** — Accessibility (data quality) = ease with which data can be obtained and used legally/ethically
- [P637] **HECHO** — Accessibility metric: subjective ease of access or amount of effort/time to retrieve data
- [P638] **DEFINICIÓN** — Consistency = compliance with semantic rules defined over data items; absence of contradictions within dataset or among different datasets
- [P639] **HECHO** — Consistency metric: rate of data entries without logical/matched consistency with related data fields or datasets
- [P640] **HECHO** — Additional data quality characteristics: redundancy (minimality, conciseness, normalization), readability (comprehensibility, clarity), usefulness (user advantages), trust (reliability, data security)
- [P641] **REGLA** — Data quality not free nor pure technical task; ensuring/improving it = critical organizational and leadership task relying on data governance policies
- [P642] **HECHO** — Data governance policies should draw on FAIR principles and OMOP CDM; embrace data quality culture, assessment/auditing, documentation, monitoring
- [P643] **DEFINICIÓN** — Data stewards = role embracing structural/procedural aspects of data management: acquisition, storage, aggregation, de-identification, data provision; conceptualized in data governance policies
- [P644] **HECHO** — Data steward role gaining increasing relevance with advent of data-driven AI and large data volumes; some recommendations speak of "FAIR data steward"
- [P645] **HECHO** — Clinical experts produce/collect/label data for AI training, perform quality control with analytical software, do plausibility checks of AI output with critical datasets

### Conclusions and Outlook
- [P646] **HECHO** — Medical/healthcare datasets can be rather small vs other domains; inherent reasons (rare diseases) + changeable reasons (lack of interoperability)
- [P647] **DEFINICIÓN** — EHDS (European Health Data Space) = EU initiative for use/exchange of electronic health data across EU; stimulates primary use (healthcare delivery, cross-border sharing) and secondary use (research, innovation, AI)
- [P648] **PLAZO** — EHDS Regulation entered into force March 2025
- [P649] **PLAZO** — EHDS primary use scenarios implementation planned for 2029
- [P650] **PLAZO** — EHDS secondary use scenarios implementation planned for 2031
- [P651] **HECHO** — EHDS regards individuals as gatekeepers for access, control, sharing of their electronic health data
- [P652] **HECHO** — EHDS = example of opening health data on very large scale in trustworthy manner, offering opportunities for AI based on truly big data
- [P653] **HECHO** — Data in dual role as representatives of real world and fuel for AI constitute bridge between artificial intelligence and human intelligence
