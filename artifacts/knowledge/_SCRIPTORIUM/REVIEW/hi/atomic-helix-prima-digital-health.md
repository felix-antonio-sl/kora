---
_manifest:
  urn: "urn:hi:kb:atomic-helix-prima-digital-health"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/Digital Health: From Assumptions to Implementations.md — atomizacion HELIX PRIMA (Rivas/Boillat, Springer 2023); output de /atomize 2026-04-10"
version: "1.0.0"
status: borrador
tags: [atomic, digital-health, rivas-boillat, springer-2023, helix-prima, hi]
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 741
      producer: "urn:kora:artefacto:atomize"
      source_corpus: "Rivas H, Boillat T (eds). Digital Health: From Assumptions to Implementations, 2nd Ed. Springer 2023. ISBN 978-3-031-17666-1"
---

# HELIX PRIMA
<!-- /atomize · 741 proposiciones · ~280 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICIÓN, HECHO...), o por entidad -->
<!-- Source: Rivas H, Boillat T (eds). Digital Health: From Assumptions to Implementations, 2nd Ed. Springer 2023. ISBN 978-3-031-17666-1 -->

## Ch1 — An Introduction to Digital Health: Current and Future Trends (Rivas, Boillat)

### 1.1 Introduction
- [P001] **DEFINICIÓN** — WHO defines digital health = "use of ICT in support of health/health-related fields"
- [P002] **ALCANCE** — DHT encompass EMR, telehealth, mHealth, wearables, AR, VR, blockchain, AI
- [P003] **HECHO** — Generation Z (born after 1996) = first true digital citizens
- [P004] **HECHO** — Apple Watch sold >100 million units by 2021
- [P005] **HECHO** — Apple Watch detected atrial fibrillation in clinical trial with ~500,000 participants → `Perez et al. 2019`
- [P006] **HECHO** — US telehealth delivery volume increased 38x between 2019-2020 amid COVID-19
- [P007] **HECHO** — 80% AI algorithms for health applications FDA-approved between 2018-2021
- [P008] **HECHO** — FDA created Digital Health Center of Excellence in 2020
- [P009] **DEFINICIÓN** — Healthcare 1.0 = traditional patient encounter, diagnosis, treatment
- [P010] **DEFINICIÓN** — Healthcare 2.0 = relies on medical equipment (ultrasound, CT, surgical/life support)
- [P011] **DEFINICIÓN** — Healthcare 3.0 = EMR, patient portals, telemedicine, virtual visits
- [P012] **DEFINICIÓN** — Healthcare 4.0 = IoT, wearables, cloud computing, AI → personalized medicine
- [P013] **HECHO** — From Healthcare 3.0 upward, technologies become increasingly less industry-specific
- [P014] **HECHO** — Before Healthcare 4.0, hospitals/clinics were innovation-driven forces
- [P015] **HECHO** — Healthcare 4.0 demand comes from patients/medical professionals, not institutions
- [P016] **DEFINICIÓN** — "Consumerization"/"bottom-up innovation" = customers push industry to adopt new technology → `Moschella et al. 2014`
- [P017] **HECHO** — Many patients collect health data (food tracking, activity trackers) hospitals cannot access or trust

### 1.2 Current Trends
- [P018] **DEFINICIÓN** — Quadruple Aim framework: (1) individual experience of care, (2) health of populations, (3) reducing per capita cost, (4) experience of providing care → `Bodenheimer and Sinsky 2014`
- [P019] **HECHO** — Triple Aim initially developed by Berwick et al. 2008; 4th dimension added 2014
- [P020] **HECHO** — 4th Quadruple Aim dimension includes work recognition, dignity, respect, education, training, tools, financial support for medical staff

### 1.2.1 Social Media, Mobile Health, Wearables
- [P021] **HECHO** — Dr. Mikhail "Mike" Varshavski videos viewed >1.2 billion times on YouTube since 2016
- [P022] **HECHO** — During early COVID-19 months, physicians used social media to fight misinformation with scientific evidence
- [P023] **HECHO** — Smartphones used by >6 billion people worldwide (2021)
- [P024] **DEFINICIÓN** — WHO defines mHealth = "medical/public health practice supported by mobile devices (phones, patient monitoring devices, PDAs, wireless devices)"
- [P025] **HECHO** — mHealth apps: 318,000 in 2017, 350,000 in 2020 (Android + Apple stores)
- [P026] **HECHO** — 100,000 new mHealth apps published in 2019 alone → high turnover/market saturation
- [P027] **HECHO** — mHealth apps evolving from general fitness/diet tracking → disease-specific (mental health, diabetes, hypertension, women's health)
- [P028] **HECHO** — mHealth apps shifted from passive data collection/monitoring → active behavioral interventions
- [P029] **HECHO** — Customized text messages shown efficient for coronary heart disease patients to reduce smoking/increase physical activity → `Chow et al. 2015`
- [P030] **HECHO** — Swiss startup developed mobile app measuring blood pressure from phone camera data → `Schoettker et al. 2020`
- [P031] **HECHO** — FDA approved <1% of mHealth apps for clinical use
- [P032] **HECHO** — Most health app innovators/entrepreneurs target "wellness market" to bypass FDA regulation
- [P033] **HECHO** — Out of 3,296 mHealth apps analyzed, only 11 had been evaluated for effectiveness → `Buechi et al. 2017`
- [P034] **DEFINICIÓN** — Wearable = device whose embedded sensors/analytic algorithms track, analyze, guide wearer behavior → `Schull 2016`
- [P035] **HECHO** — Apple Watch atrial fibrillation trial: 400,000 participants, published in NEJM
- [P036] **HECHO** — Wearable sensors now include oxygen saturation, ECG, blood pressure monitoring
- [P037] **HECHO** — Wearables showed potential for remote monitoring of mildly symptomatic COVID-19 patients
- [P038] **HECHO** — Google Glass used to help autistic children recognize emotions via facial expression analysis → `Daniels et al. 2018`
- [P039] **HECHO** — Chronic diseases (obesity, cancer, diabetes) + lifestyle choices account for majority of healthcare costs in developing countries
- [P040] **HECHO** — ML algorithms + data science leveraged to predict early obesity from medical visit data → `Triantafyllidis et al. 2020`
- [P041] **HECHO** — ML + mHealth enables skin cancer screening from mobile device photo → identify malignant vs benign moles → `SkinVision`

### 1.2.3 Telemedicine, EMR, Provider Wellbeing
- [P042] **HECHO** — COVID-19 changed traditional care delivery model requiring in-person physician visits
- [P043] **HECHO** — Pre-identified barriers to telemedicine (e.g., breakdown in patient-physician relationship) had lower impact than expected → `Hollander and Carr 2020`
- [P044] **HECHO** — Hospitals integrated telemedicine into portals: search specialist, book appointment, run teleconsultation, receive e-prescription, access discharge report
- [P045] **⚠ TENSIÓN** — EMR negatively impacts medical professionals' wellbeing due to poor usability, but enables better data access/sharing/analysis → better care
- [P046] **HECHO** — Telemedicine allows physicians to sort patients more efficiently, redirect to specialists → `Mahtta et al. 2021`
- [P047] **HECHO** — DHT used during COVID-19 to measure care provider stress, identify burnout/breakdown risk → `Goodday et al. 2021`

### 1.3 Future Trends
- [P048] **HECHO** — Future activity trackers will collect blood glucose, detect toxins, vitamins, micronutrients, perform molecular diagnostics via biosensors
- [P049] **DEFINICIÓN** — PMR/PHR = Personal Medical/Health Records capturing health data entered by individuals, providing centralized easy-to-access care information → `Tang et al. 2006`
- [P050] **HECHO** — Amazon and Microsoft developed centralized PMR shareable with hospitals/clinics in some countries
- [P051] **HECHO** — Researchers exploring blockchain for decentralized, traceable health record solutions → `Chen et al. 2019`
- [P052] **HECHO** — FabRx M3DIMAKER = non-proprietary FDA-certified 3D printer for drugs, recently commercialized
- [P053] **HECHO** — Average US hospital has 16 different EMR systems → `Sullivan 2018`
- [P054] **HECHO** — Tech companies now hire chief medical officers to identify clinical needs/constraints

## Ch2 — How Mobile Technologies Are Changing Life of Physicians and Patients in Hospitals (Ehrler, Blondon)

### 2.1 Introduction
- [P055] **HECHO** — Patients with chronic conditions can spend ≤2h/day dealing with health issues → `Jowsey et al. 2012`
- [P056] **HECHO** — Mobile devices reach people of lower socio-economic status who have more prevalent chronic diseases
- [P057] **DEFINICIÓN** — WHO eHealth observatory defines mHealth = "medical/public health practice supported by mobile devices"
- [P058] **DEFINICIÓN** — Telemedicine subcategory of mHealth = "communication/consultation between health professionals about patients using voice, text, data, imaging, video functions of mobile device"
- [P059] **HECHO** — Early EMR systems kept paper-record billing/legal approach rather than being designed for clinician workflows → `Evans 2016`
- [P060] **HECHO** — Clinicians forced to adapt workflow to electronic tools rather than tools adapting to needs → `Sieck et al. 2020`

### 2.2 At An Institutional Level
- [P061] **REQUISITO** — CIS must support deployment of multiple client apps without jeopardizing data integrity
- [P062] **REQUISITO** — CIS APIs should comply with FHIR or IHE profiles to ensure compatibility across care network
- [P063] **REGLA** — Business logic should be minimized in front-end → ensure coherent behavior across apps using back-end services
- [P064] **REGLA** — Numerous small-sized loosely coupled business services (microservices) preferred for system agility
- [P065] **HECHO** — Many actual CIS architectures are monolithic or rely on enterprise service bus → maladapted for rich app ecosystem
- [P066] **HECHO** — Strava publicly exposed users' geolocalization data → military patrol routes/bases revealed
- [P067] **HECHO** — Trust/security concerns are barrier for mobile technology use, especially among older patients → `Wilson et al. 2021`
- [P068] **HECHO** — COVID-19 contact-tracing/symptom-tracking apps met high public suspicion
- [P069] **REQUISITO** — Hospital-recommended apps must guarantee patient trust via clear disclaimer specifying data access/duration
- [P070] **RESTRICCIÓN** — Secured patient data storage usually prevents use of cloud solutions if storage not in same country as service provider
- [P071] **REQUISITO** — Patient accounts require dual-factor authentication (password + SMS challenge) with identity validation process
- [P072] **HECHO** — Mobile devices portable → easily stolen/lost/left in public area → patient data confidentiality risk
- [P073] **DEFINICIÓN** — BYOD = Bring Your Own Device strategy → reduces cost of device maintenance, eliminates need for multiple devices
- [P074] **RESTRICCIÓN** — BYOD devices connected to public networks → require strong security safeguards
- [P075] **REGLA** — No sensitive data can be stored on BYOD device in case of theft
- [P076] **REQUISITO** — External cybersecurity audit required for apps accessible from external network

### 2.3 At the Provider's Level
- [P077] **HECHO** — EHR digitalization caused loss of mobility previously existing with paper records + increased documentation time → `Ammenwerth and Spotl 2009`
- [P078] **HECHO** — Increased documentation requirements → time-consuming process → can lead to provider exhaustion/burnout → `Tajirian et al. 2020`
- [P079] **HECHO** — Computers on wheels prohibited in protective isolation rooms for immunocompromised patients → `Jen et al. 2016`
- [P080] **HECHO** — Bedside mobile documentation avoids transcription errors, reduces delays entering vital signs, decreases documentation interruptions
- [P081] **HECHO** — CIS interfaces designed for desktop cannot be visualized without change on mobile screens
- [P082] **REGLA** — Mobile interfaces must tailor information per user type; desktop CIS can apply one-system-for-all
- [P083] **HECHO** — Ehrler et al. 2015: data entry error rates ranged 0.7% (most reliable design) to 18.5% (least reliable) across different vital sign entry interfaces
- [P084] **REGLA** — User-centered design with close collaboration with care-provider users = key process for mobile device usability
- [P085] **HECHO** — "Bedside" app at University Hospitals of Geneva designed for nurses to document short structured data (vital signs) at bedside
- [P086] **HECHO** — Camera scanning patient bracelets ensures correct chart access → reduces wrong-chart risk
- [P087] **RESTRICCIÓN** — Relying on device sensors often opens security breaches; data transferred through cloud solutions with own data management policies
- [P088] **DEFINICIÓN** — Alert fatigue = user becomes less responsive to alerts when alerts too numerous/overwhelming → `Backman et al. 2017`
- [P089] **HECHO** — Mobile devices allow targeted alerts to individual clinicians → decrease risk of alert fatigue
- [P090] **HECHO** — Excessive EHR emails from patients contribute to provider burnout → `Gardner et al. 2019`

### 2.4 At the Patient's Level
- [P091] **HECHO** — Patient empowerment associated with improved health outcomes, lower adverse events
- [P092] **HECHO** — Patients using multiple health apps face fragmented data in silos, no interoperability, no unified health overview
- [P093] **HECHO** — Multiple mHealth apps often possess separate authentication systems, do not communicate with each other
- [P094] **HECHO** — Interoperability issues limit implementation of AI tools for patient guidance/analysis
- [P095] **HECHO** — Apps not adapted for patients with multiple chronic diseases → contradictory recommendations possible
- [P096] **HECHO** — Technology acceptance model links intention to use with perceived usefulness + ease of use → `Holden and Karsh 2010`
- [P097] **HECHO** — Patients' needs for digital health support change over time → tools should be adaptive, not static
- [P098] **HECHO** — Electronic patient records being implemented in Switzerland → patients control access, share with family/providers
- [P099] **DEFINICIÓN** — PGHD = Patient-Generated Health Data including clinical parameters, patient-reported outcomes, data from family/caregivers → `ONC, Shapiro et al. 2012`
- [P100] **HECHO** — Providers worry about receiving too much PGHD, not having time to process/manage → liability concerns for missed abnormal findings
- [P101] **HECHO** — In 2019, University Hospitals of Geneva created mHealth/consumer health committee with physicians, nurses, patients, legal, cybersecurity, informatics
- [P102] **REGLA** — App assessments limited to 1 year or until next major app change; legal constraints require yearly revision of assessment criteria
- [P103] **HECHO** — Country boundaries imposed by differing legal criteria for mobile apps from one country to another

## Ch3 — The Future of Telemedicine After Covid-19 (Rivas)

### 3.1 The Calm Before the Storm
- [P104] **DEFINICIÓN** — American Telemedicine Association defines telemedicine = remote delivery of healthcare services/clinical information using telecommunications technology
- [P105] **HECHO** — Telemedicine includes telegraphic transmission, ECG electronic transmission, phone calls, diagnostic imaging transfer, NASA astronaut health monitoring
- [P106] **HECHO** — Pre-COVID-19 telemedicine barriers: reimbursement challenges, obsolete legislation, state/board license limitations, lack of awareness, privacy/security fears
- [P107] **HECHO** — Most prevalent barrier to telemedicine adoption = fixed mindset of care practitioners + risk aversion toward innovation
- [P108] **HECHO** — ≤78% of doctor visits can be handled safely/effectively using some form of telemedicine → `ATA`
- [P109] **HECHO** — ≤40% of emergency room visits suitable for telemedicine
- [P110] **HECHO** — Medical specialties suited for telemedicine: psychiatry, endocrinology, rheumatology, gastroenterology
- [P111] **HECHO** — Surgical specialties have inherent challenges for telemedicine implementation
- [P112] **HECHO** — US pre-COVID barriers to telemedicine: legislation, licensure barriers, insurance, reimbursement challenges
- [P113] **⚠ TENSIÓN** — Patients always pushed for/welcomed telemedicine innovation vs care providers/payers/regulators were risk-averse
- [P114] **HECHO** — Global telemedicine market pre-COVID-19 estimated ~$50 billion USD

### 3.2 The Perfect Storm and Its Surge
- [P115] **HECHO** — COVID-19 pandemic rendered telemedicine ideal for extending care with no infectious contagion risk
- [P116] **HECHO** — During COVID-19 regulators removed restrictions → care providers could practice across states/borders
- [P117] **HECHO** — US Centers for Medicare & Medicaid Services expanded reimbursable telehealth codes for 2021 physician fee schedule
- [P118] **HECHO** — Medical specialty societies endorsed telemedicine practices, promoted research/education
- [P119] **HECHO** — Medical educators adopted telepresence teaching + identified need for telemedicine in medical school curriculum
- [P120] **HECHO** — Digital health investment grew ≥3x vs 2017 levels during pandemic

### 3.3 The Quiet After the Storm
- [P121] **HECHO** — US telemedicine use in April 2020 = 78x pre-pandemic period → `McKinsey`
- [P122] **HECHO** — Post-spike telemedicine use stabilized at ~38% across all medical specialties
- [P123] **HECHO** — 32% of office/outpatient visits occurred via telehealth in April 2020
- [P124] **HECHO** — Post-stabilization telehealth utilization ranged 13%-17% across all specialties
- [P125] **HECHO** — Consumer willingness to use telemedicine: 11% pre-pandemic → 76% post-pandemic
- [P126] **HECHO** — Pre-pandemic telemedicine case mix = urgent low-complexity issues (colds, sore throats, UTIs, rashes)
- [P127] **HECHO** — Post-pandemic virtual care expanded to preventive health, wellness, chronic disease management, behavioral health therapy
- [P128] **HECHO** — 1/3 of consumers more likely to choose care providers allowing wearable data sharing
- [P129] **HECHO** — Very little type I evidence that wearable devices improve clinical outcomes
- [P130] **HECHO** — US post-COVID: state licensing limitations temporarily removed → physicians could treat patients in all US states/territories
- [P131] **HECHO** — In-person supervision of physician extenders relaxed → remote supervision via videoconference allowed
- [P132] **HECHO** — Most emergency telemedicine regulatory changes were temporary; severe limitations like state licensing barriers expected to return
- [P133] **HECHO** — VC investment in digital health H1 2021 = ~$15B > full year 2020 ($14.6B) ≈ 2x 2019 ($7.7B)
- [P134] **HECHO** — H1 2021 digital health investment expected to double by end of 2021

### 3.4 The Future of Telemedicine and Final Thoughts
- [P135] **HECHO** — Patient-centered telemedicine strategies should be designed by multidisciplinary teams including engineers, designers, computer scientists, entrepreneurs, investors, regulators, payers
- [P136] **REGLA** — Only innovations making economic sense will achieve universal adoption/sustainability → `Rivas 2018`
- [P137] **REQUISITO** — Achievable reimbursement strategies required for telemedicine/digital health maintenance
- [P138] **HECHO** — Telemedicine represents ~$250 billion economic opportunity
- [P139] **HECHO** — All insurance plans expected to include virtual care/digital health coverage with telemedicine incentives
- [P140] **HECHO** — Blockchain expected to maintain security/privacy of all personal health information

## Ch4 — Introducing Computer Vision into Healthcare Workflows (Mosquera et al.)

### 4.1 Introduction
- [P141] **HECHO** — Medical imaging existed since X-ray research by Wilhelm Roentgen and Nikola Tesla, late XIX century
- [P142] **HECHO** — Precision medicine demands greater diagnostic precision in medical image analysis
- [P143] **HECHO** — Increased imaging workload on physicians = driving force behind CV/AI application in medical imaging

### 4.2 Computer Vision
- [P144] **DEFINICIÓN** — CV = set of methods/algorithms that acquire, process, analyze, understand real-world images, simulating human visual perception
- [P145] **DEFINICIÓN** — Image classification = assigning single label to image (e.g., chest X-ray pathological vs normal)
- [P146] **DEFINICIÓN** — Object detection = locating/classifying multiple objects of multiple classes in image
- [P147] **DEFINICIÓN** — Segmentation = assigning class to each pixel; includes semantic segmentation + instance segmentation
- [P148] **HECHO** — 2012 ImageNet competition (ILSVRC): convolutional network far surpassed previous image classification performance → `Krizhevsky et al. 2012`
- [P149] **HECHO** — DL enabled CV to advance at unprecedented speed, solving pattern recognition tasks previously unautomatable

### 4.3 Algorithm Development: Datasets and Robust Models
- [P150] **REQUISITO** — AI for medical imaging requires ethical committee approval + deidentification strategies for data privacy compliance
- [P151] **HECHO** — Most healthcare systems not adequately prepared to collect large amounts of medical images; data stored in disparate silos
- [P152] **HECHO** — Fully supervised AI methods require images associated with ground-truth diagnosis
- [P153] **HECHO** — Ground-truth annotation ranges from whole-image classification labels → bounding boxes → manual delineation (segmentation)
- [P154] **HECHO** — Stronger labels (bounding boxes/masks) → same screening performance achievable with smaller training dataset, but more annotation effort per image
- [P155] **HECHO** — Trade-off exists between label quality and feasibility (better labels require more resources)
- [P156] **DEFINICIÓN** — Transfer learning = algorithm first trained on large unrelated dataset (e.g., ImageNet), then fine-tuned on dataset of interest (e.g., medical)
- [P157] **HECHO** — Synthetic data techniques: data augmentation, GANs reduce costs of data collection/labeling
- [P158] **HECHO** — Vision transformers = recent technique not using CNNs, explored as alternative for medical imaging → `Matsoukas et al. 2021`
- [P159] **HECHO** — Medical image dataset size typically hundreds of GB to TB
- [P160] **HECHO** — GPUs crucial for training DL algorithms in reasonable time; enable parallel processing
- [P161] **DEFINICIÓN** — Domain shift = variation in target domain (real-world data) relative to source domain (training data) → performance decrease
- [P162] **HECHO** — Model trained for skin cancer detection on fair-skin datasets expected to perform worse on intermediate/dark skin tones
- [P163] **DEFINICIÓN** — Algorithmic bias = algorithm learns/reproduces/amplifies habitual human biases
- [P164] **HECHO** — Biased models can cause underdiagnosis, overdiagnosis, disparate resource allocation → increase social disparities
- [P165] **DEFINICIÓN** — Federated learning = learn common robust model through distributed computing/model aggregation, no data transferred outside hospital
- [P166] **HECHO** — Federated learning applied for brain segmentation + disease-related biomarker discovery → `Li et al. 2019, 2020`
- [P167] **⚠ TENSIÓN** — Federated learning reports trade-off between model performance and privacy protection

### 4.4 Validation Studies: Diagnostic Performance to Clinical Effectiveness
- [P168] **HECHO** — Gap exists between "algorithm development lab" and final healthcare application domain → hinders clinical implementation
- [P169] **HECHO** — Research images (high quality, preselected, reviewed) contrast with healthcare process images (heterogeneous, messy, unstructured)
- [P170] **HECHO** — Knowing accurate prediction/diagnosis does not necessarily imply appropriate actions taken → algorithm may have null clinical impact despite good diagnostic performance
- [P171] **HECHO** — Difficulty moving from medical evidence → care practice predates AI, remains major challenge
- [P172] **HECHO** — AI evaluation process analogized to drug evaluation: progressive controlled exit from lab → routine clinical practice
- [P173] **HECHO** — Most important ethical challenge of AI in health = understanding of ethical challenges constantly changing
- [P174] **HECHO** — Algorithms can be trained to pursue economic interests (e.g., recommending tests by cost/profitability) over patient care
- [P175] **HECHO** — If algorithm recommendation harms patient → unclear whether developing company or medical staff is liable
- [P176] **HECHO** — AI algorithms require large amounts of data from multiple sources → new confidentiality challenges beyond EMR
- [P177] **REQUISITO** — Medical imaging AI requires research protocols approved by Institutional Review Board
- [P178] **HECHO** — FDA authorization of AI systems increased recently but without usual pre-market requirements
- [P179] **HECHO** — AI systems undergo modifications once implemented → dynamic nature limits full regulatory approvals
- [P180] **HECHO** — FATML initiative = fairness, accountability, transparency in ML
- [P181] **HECHO** — FUTURE-AI recommendations = fairness, universality, traceability, usability, robustness, explainability in AI → `Lekadir et al. 2021`
- [P182] **HECHO** — RSNA published CLAIM checklist for AI in Medical Imaging → `Mongan et al. 2020`
- [P183] **DEFINICIÓN** — Interpretability = ease with which person understands relation between model features/variables and predictions
- [P184] **HECHO** — DL models have hidden layers → difficult for humans to understand predictions = "black box" problem
- [P185] **HECHO** — Possible inverse nonlinear relationship between interpretability and predictive performance → `DARPA 2016`
- [P186] **HECHO** — Model-agnostic interpretability methods (e.g., class activation maps) operate at model input/output level, easier to implement
- [P187] **DEFINICIÓN** — Transparency in AI = (1) model development/training process accessible/auditable; (2) degree of access to model internal information
- [P188] **HECHO** — Transparent model may not be more interpretable → in complex models, providing code may not solve interpretability problem
- [P189] **REGLA** — AI tools for imaging should be tested by randomized controlled clinical trials for highest-quality evidence
- [P190] **HECHO** — AI algorithms affect medical decisions more substantially than classic diagnostic tests → further justifies rigorous RCT evaluation
- [P191] **HECHO** — Randomized clinical trials of AI scarce at time of writing
- [P192] **HECHO** — Challenge in AI trials: difficult to measure clinical outcomes vs intermediate/process events
- [P193] **HECHO** — Research designs focused on fixed-parameter (locked) algorithms, not algorithms learning during study → adds methodological challenges
- [P194] **HECHO** — SPIRIT-AI + CONSORT-AI = guidelines for designing/reporting interventions using AI algorithms, developed via Delphi method

### 4.5 Integration to Health Information Systems
- [P195] **HECHO** — AI in medical imaging particularly explored in radiology, pathology, ophthalmology
- [P196] **HECHO** — AI pattern recognition can detect clinically meaningful information sometimes imperceptible to human eyes
- [P197] **DEFINICIÓN** — CDSS = tools designed to sift vast digital data, suggest treatment next steps, alert providers to available information, spot dangerous drug interactions
- [P198] **DEFINICIÓN** — CADe = computer-aided detection: detects anomalies/pathologies, marks areas to attract operator attention, does not analyze etiology
- [P199] **DEFINICIÓN** — CADx = computer-aided diagnosis: adds evaluation of finding to detection, suggests specific/differential diagnoses
- [P200] **DEFINICIÓN** — CADt = computer-aided triage/notification: selects/classifies patients to prioritize reading/attention, optimizes resource use
- [P201] **HECHO** — Traditional CAD research began in 1960s → FDA approval for mammography CAD in 1998
- [P202] **HECHO** — By 2016, CAD applied to 92% of screening mammograms in US → `Gao et al. 2019`
- [P203] **HECHO** — Traditional CAD disadvantages: high development cost, high false positives, increased unnecessary biopsies, limited to specific injuries
- [P204] **HECHO** — "Third wave of AI" using DL shows promising improvements over traditional CAD → `Fujita 2020`
- [P205] **HECHO** — ML community primarily uses Python; key DL libraries: Tensorflow (Google), Pytorch (Facebook), Scikit Learn
- [P206] **REQUISITO** — CV algorithm deployment requires integration into API framework
- [P207] **REQUISITO** — Software architecture must include connection to PACS to access medical images in automated/secure/protocolized way
- [P208] **HECHO** — Chest X-ray CV tool outputs must be available within minutes (emergency/hospitalized patient context)
- [P209] **HECHO** — Mammography/MRI CV algorithms can process studies in scheduled batch on subsequent days
- [P210] **REGLA** — CV tool UI should be integrated into applications physicians use regularly (EHR, PHR, radiology information systems)
- [P211] **HECHO** — Acceptance remains biggest barrier to AI adoption; lack of trust due to "black box" nature
- [P212] **HECHO** — Specialists fear being replaced by AI → concrete engagement actions needed (assertive communication, training, change management)
- [P213] **HECHO** — AI not expected to replace experts in near future; specialists unwilling to adopt AI will be replaced by those who do
- [P214] **HECHO** — Introducing CV into healthcare requires software development, health informatics, UX analysis, interoperability, infrastructure, coaching, monitoring

### 4.6 Current State
- [P215] **HECHO** — van Leeuwen et al. 2021 survey found 100 AI solutions with CE mark approved for clinical use in Europe (radiology)
- [P216] **HECHO** — >65% of 100 CE-marked AI radiology products introduced to market between January 2018-April 2020
- [P217] **HECHO** — AI radiology product deployment/pricing strategies not yet converged to preferred standard
- [P218] **HECHO** — Subscription/license models more prevalent than pay-per-use (56/100 vs 28/100) for AI radiology products
- [P219] **HECHO** — Only 36/100 CE-marked AI radiology products had peer-reviewed evidence for efficacy
- [P220] **HECHO** — Similar AI products certified under different regulatory classes (e.g., class I self-certification vs class II external audit)
- [P221] **HECHO** — Most AI radiology products perform single specific task; only stroke/oncology have "suites" covering whole diagnostic path
- [P222] **HECHO** — Radiology departments forced to interact with multiple AI vendors → overhead of sales, contracts, training, integration

### 4.7 Future Directions
- [P223] **HECHO** — Future efforts focused on solving minority misrepresentation in datasets + unintended labeling errors from NLP mining of radiological reports
- [P224] **HECHO** — AI utility in medical imaging will increase as CV systems incorporate fusion of different data modalities
- [P225] **HECHO** — Increase in non-interpretative CV solutions expected: report worklist management, image correction, synthesis
- [P226] **HECHO** — CV adoption worldwide depends on prior digitization of health information systems, especially in less developed countries
- [P227] **HECHO** — Real importance lies not in creating AI products but ensuring people have access to them → `Myers 2020`

## Ch5 — Technology-driven Solutions in Mental Health and Physical Well-being (AlGurg, Nawaz, Albanna)

### 5.1 Introduction
- [P228] **HECHO** — Global burden mental disorders estimated ~$16 trillion by 2030 → `Patel et al. 2018`
- [P229] **HECHO** — Digital health sector received >$57.2 billion invested worldwide by 2021

### 5.2 Challenges in Mental Healthcare
- [P230] **HECHO** — COVID-19 significantly impacted mental well-being of children, adolescents, families
- [P231] **HECHO** — <50% adolescents with mental disorders receive treatment → `Costello et al. 2014`
- [P232] **HECHO** — >50% youth with depression receive no intervention
- [P233] **HECHO** — USA requires training many more mental health professionals to meet demand
- [P234] **HECHO** — WHO identified lack of funding/services as key barrier to addressing mental health gap

### 5.3 Role of Digital Mental Healthcare
- [P235] **HECHO** — Enhancing screening at Primary Health Centers with apps = feasible, may reduce time/increase accessibility → `Diez-Canseco et al. 2018`
- [P236] **HECHO** — Tate et al. used Swedish registry + ML to predict adolescent mental health; random forest AUC=0.739 (95% CI 0.708-0.769)
- [P237] **HECHO** — Tate et al. SVM model AUC=0.735 (95% CI 0.707-0.764) for adolescent mental health prediction
- [P238] **RESTRICCIÓN** — Tate et al. models not suitable for clinical use; serve as model for future studies
- [P239] **DEFINICIÓN** — Autism Spectrum Disorder (ASD) = heterogeneous developmental disorder
- [P240] **HECHO** — Chen et al. used rs-fMRI from ABIDE dataset; matched ASD children (n=126) vs typically developing (n=126); reported high accuracy with ML
- [P241] **HECHO** — Kosmicki et al. used ML on ADOS data → ~98% accuracy classifying ASD with abbreviated behavior set
- [P242] **HECHO** — Shahamiri et al. mobile app + CNN trained on ASD database → higher accuracy/sensitivity/specificity than usual ASD screening
- [P243] **RESTRICCIÓN** — AI for ASD screening = infancy stage; high psychometric properties but feasibility/real-world applicability challenges remain → `Song et al. 2019`
- [P244] **HECHO** — Mobile technologies/apps have important role augmenting or providing stand-alone treatment for anxiety disorders → `Silk et al. 2011`
- [P245] **HECHO** — Anxiety Coach = empirically supported app developed by Mayo Clinic for anxiety assessment/education
- [P246] **HECHO** — VR can simulate anxiety-provoking situations as treatment modality; biological data comparable to real-life → `Kothgassner et al. 2016`
- [P247] **HECHO** — VR exposure shows lower refusal rate than in vivo exposure for mental health interventions → `Garcia-Palacios et al. 2007`
- [P248] **HECHO** — COVID-19 pandemic led to rapid expansion of digital mental health services
- [P249] **HECHO** — Pandemic caused rapid increase in mental health services within weeks of onset → `Sharma et al. 2020`
- [P250] **HECHO** — Individually tailored web-based CBT program demonstrated preliminary effectiveness reducing stress/anxiety during COVID-19 → `Aminoff et al. 2021`

### 5.4 Physical Well-being
- [P251] **HECHO** — Up to 50% cancer patients suffer from mental illness
- [P252] **HECHO** — Treating depression in cancer patients shown to improve survival time
- [P253] **HECHO** — Risk of heart attack >2x in patients with depression vs general population → `Rosenstein 2011`
- [P254] **HECHO** — Depression increases risk of death in cardiac disease patients
- [P255] **HECHO** — New Zealand cohort study (>2M citizens, 3 decades): mental disorders associated with subsequent physical disease onset, accumulation of diagnoses, increased costs, early mortality → `Richmond-Rakerd et al. 2021`
- [P256] **DEFINICIÓN** — WHO: "Health = state of complete physical, mental, social well-being, not merely absence of disease or infirmity"
- [P257] **HECHO** — Mindfulness training associated with improved mental health in high-stress career populations
- [P258] **HECHO** — Growing evidence of endocrine function changes after meditation → improved mental health outcomes → `Pascoe et al. 2020`
- [P259] **HECHO** — Poor sleep impacts psychiatric conditions; affects development/maintenance of mental health problems from poor cognition to depression/GAD → `Scott et al. 2017`
- [P260] **HECHO** — Lack of sleep associated with heart disease and type 2 diabetes
- [P261] **HECHO** — CDC: 1/3 US adults get less than recommended sleep per night
- [P262] **HECHO** — COVID-19 pandemic: 1 in 3 individuals reported sleep problems → `Alimoradi et al. 2021`
- [P263] **HECHO** — Sleep deprivation strongly associated with immune system dysregulation → `Garbarino et al. 2021`
- [P264] **HECHO** — Obesity linked to comorbid conditions: diabetes, cancer risk, heart disease, stroke, osteoarthritis, sleep apnea, liver/pulmonary disease
- [P265] **HECHO** — Among low-SES families, food insecurity co-occurred with maternal depression → `Melchior et al. 2009`
- [P266] **HECHO** — Short sleep duration/poor sleep quality = risk factors for obesity → `Beccuti & Pannain 2011`
- [P267] **HECHO** — Sleep deprivation increases food consumption without parallel increase in energy expenditure → `Grandner et al. 2014`
- [P268] **HECHO** — Sleep deprivation creates preference for high-calorie foods with poor nutritional value → weight gain risk → `Greer et al. 2013`
- [P269] **HECHO** — Lack of calcium, magnesium, vitamins A/C/D/E/K associated with sleep problems → `Ikonte et al. 2019`
- [P270] **HECHO** — >350,000 digital health apps available on market as of 2021
- [P271] **HECHO** — Wearable tech enables accurate measurement of heart rate, exercise time, distance, estimated caloric expenditure
- [P272] **RESTRICCIÓN** — Digital health impact on physical well-being hampered by non-technical barriers: lack of transparency, privacy concerns, digital literacy gap
- [P273] **HECHO** — Users reengaging with health app after break usually restart from beginning rather than continuing → `Azumio dataset`
- [P274] **HECHO** — Long-term wearable tech users tend to be surrounded by fitness-oriented people, less active on social media showcasing activities
- [P275] **HECHO** — People using smart scales regularly tend to have greater weight loss
- [P276] **HECHO** — Sunrise system = coin-sized device attached to chin for ambulatory OSA diagnosis outside sleep center → `Pépin et al. 2020`
- [P277] **HECHO** — Sunrise system identifies obstructive/mixed apneas, hypopneas, respiratory effort-related arousals by analyzing mandibular movement patterns

### 5.4.9 Chatbots
- [P278] **DEFINICIÓN** — Chatbot = "conversational agent" — program supporting/engaging humans via sound or text techniques
- [P279] **HECHO** — ESTORE chatbot utilizes text-messaging + voice assistant to provide mental health support to older adults → `El Kamali et al. 2020`
- [P280] **HECHO** — "Rupert" food diary coaching chatbot encourages reduced meat consumption + increased fruit/vegetable intake
- [P281] **HECHO** — 82% Rupert app users reported it helped them think about/be aware of their consumption → `Casas et al. 2018`

### 5.5 Conclusion and Path Forward
- [P282] **HECHO** — >350,000 digital health apps available; wearable tech enables accurate health monitoring
- [P283] **RESTRICCIÓN** — Non-technical barriers (transparency, privacy, digital literacy) hamper digital health physical well-being impact

## Ch6 — Present Capabilities of AI in Surgical Oncology (Narayan)

### 6.1 Introduction
- [P284] **DEFINICIÓN** — AI = any platform simulating human thought/behavior including problem-solving, image/word recognition, pattern-based conclusions → `Hashimoto et al. 2020`
- [P285] **DEFINICIÓN** — ML = sub-category of AI; programs build own knowledgebase from increasing data → more precise conclusions
- [P286] **HECHO** — Term "artificial intelligence" coined 1956
- [P287] **HECHO** — From PubMed inception (1996) to April 1 2022, >300 articles published using AI for surgical oncology clinical questions

### 6.2 The Use of AI in Surgical Oncology
- [P288] **DEFINICIÓN** — Supervised ML = develops algorithm from training + testing dataset to predict output of interest
- [P289] **REGLA** — Supervised ML: larger proportion → training set, remainder → testing set (e.g., 90% vs 10%)
- [P290] **DEFINICIÓN** — Internal validation set = subjects from same dataset; external validation set = subjects from new dataset not used for training
- [P291] **DEFINICIÓN** — Unsupervised ML = algorithms identifying patterns within dataset without labeled outputs
- [P292] **DEFINICIÓN** — Reinforcement ML = algorithm iterates performance on pre-specified task as more data introduced; learns from successes/mistakes
- [P293] **HECHO** — Laukhtina et al. used LASSO regression → nomogram predicting cancer-specific survival for metastatic renal cell carcinoma; 613 patients; c-index=0.644
- [P294] **DEFINICIÓN** — Random forest = supervised ML creating decision tree with features → cumulative probability of outcome; performs classification and/or regression
- [P295] **HECHO** — Rahman et al. used random forest to predict 5-year survival among 2931 gastric adenocarcinoma patients; time-dependent AUC=0.80; c-index=0.76
- [P296] **DEFINICIÓN** — K-clustering = supervised learning evaluating training data geometrically → categorizes testing data by Euclidean distance
- [P297] **HECHO** — Yin et al. 14,134 cancer patients across 5 Chinese institutions; k-clustering on 17 nutritional features; AUC=0.941
- [P298] **DEFINICIÓN** — Support vector machines = supervised learning using classification/regression to cluster data relative to hyperplanes
- [P299] **DEFINICIÓN** — Neural networks / DL = ML techniques modeled after human nervous system: input layer + output layer + hidden layer(s)
- [P300] **DEFINICIÓN** — CNN = convolutional neural network with many arrays; RNN = recurrent neural network
- [P301] **HECHO** — Liu et al. used 16-layer CNN → nomogram predicting malignancy of solitary pulmonary nodule; AUC=0.916
- [P302] **DEFINICIÓN** — CV = AI modality analyzing images/videos to identify patterns related to outcome
- [P303] **DEFINICIÓN** — Radiomics = CV subset identifying texture features on images often imperceptible to human eyes → associations with outcomes
- [P304] **HECHO** — Radiomics features quantified via RGB color extraction + statistical measures: mean, SD/variance, skewness, kurtosis, entropy, energy, contrast, homogeneity, correlation
- [P305] **HECHO** — Creasy et al. (Memorial Sloan Kettering) used radiomics to predict volumetric response to neoadjuvant chemo in 157 colorectal liver metastasis patients; mean absolute prediction error=21.5%
- [P306] **DEFINICIÓN** — NLP = AI technique seeking associations between syntax/semantics of words and outcomes of interest → `Nadkarni et al. 2011`
- [P307] **HECHO** — Patel et al. (University of Chicago) used NLP on 10,196 average-risk colonoscopy reports → relationship between proximal serrated polyp detection rate and median withdrawal time
- [P308] **HECHO** — Yang et al. developed NLP platform identifying muscle-invasive bladder cancer from VA CPRS; accuracy=94%

### 6.3 Limitations on AI in Surgical Oncology Research
- [P309] **RESTRICCIÓN** — Few published AI models accessible open-source; lack of internal validation at new institutions limits generalizability
- [P310] **HECHO** — Northcutt et al. found average error rate 3.3% across 10 most commonly used CV datasets
- [P311] **HECHO** — One mammogram image dataset used for algorithm training had >15% mislabeled images → `Kay et al. 2021`
- [P312] **RESTRICCIÓN** — AI models require updates as standards of practice evolve; rapid change in systemic regimens necessitates frequent updates
- [P313] **DEFINICIÓN** — Time drift = failure of established models to keep up with practice changes (e.g., ICD-9 → ICD-10) → `Ross 2022`

### 6.4 Conclusion
- [P314] **REGLA** — AI models function best as supplement to clinical decision-making, not replacement for diagnosis/prognosis
- [P315] **OBLIGACIÓN** — Clinicians must be driving force for incorporating/supervising AI models in clinical practice

## Ch7 — ML for Decision Support Systems: Prediction of Clinical Deterioration (Shamout)

### 7.1 Introduction
- [P316] **DEFINICIÓN** — CDSS = Clinical Decision Support Systems informing decision-making of medical practitioners in patient care (since 1970s) → `Mould et al. 2016`
- [P317] **DEFINICIÓN** — Clinical deterioration = worsening of patient condition on hospital wards; defined by adverse events (unintended injury/complication → disability, death, prolonged stay) → `Jones et al. 2013`
- [P318] **HECHO** — CDSS value recognized in improving patient safety/minimizing medical errors in early 2000s → `Donaldson et al. 2000`
- [P319] **DEFINICIÓN** — Knowledge-based CDSS = reason based on expert medical knowledge; use IF-THEN rule-based logic; knowledge base must be constantly maintained
- [P320] **DEFINICIÓN** — Non-knowledge-based CDSS = use AI/ML/DL pattern recognition; require large datasets for model training; need retrospective + prospective validation before deployment
- [P321] **HECHO** — Delayed recognition of deterioration associated with human-related monitoring failures → `Van Galen et al. 2016`
- [P322] **ALCANCE** — EWS systems predict whether adverse event likely within future N-hour window from assessment time (e.g., 24h)

### 7.2 Classical Early Warning Score Systems
- [P323] **DEFINICIÓN** — Classical EWS = "track-and-trigger" systems assigning scores to physiological variables: heart rate, respiratory rate, temperature, blood pressure, oxygen saturation
- [P324] **HECHO** — First physiological EWS system introduced 1997 by Morgan et al.
- [P325] **REGLA** — EWS aggregate score = sum of individual scores; alerts clinicians for deterioration signs preceding adverse events
- [P326] **REGLA** — NEWS2: heart rate ≥131 bpm → score=3; heart rate ≤30 → score=3
- [P327] **REGLA** — NEWS2: systolic BP ≤90 mmHg → score=3; systolic BP ≥220 mmHg → score=3
- [P328] **REGLA** — NEWS2: temperature ≤35.0°C → score=3; temperature ≥39.1°C → score=2
- [P329] **REGLA** — NEWS2: respiratory rate ≤8 breaths/min → score=3; respiratory rate ≥25 → score=3
- [P330] **REGLA** — NEWS2: O2 saturation Scale 1 ≤91% → score=3; ≥96% → score=0
- [P331] **REGLA** — NEWS2: O2 saturation Scale 2 (hypercapnic respiratory failure) ≤83% → score=3; ≥97% on oxygen → score=3
- [P332] **REGLA** — NEWS2: ACVPU score CVPU → score=3; Alert → score=0
- [P333] **REGLA** — NEWS2: supplementary oxygen Yes → score=2; No → score=0
- [P334] **HECHO** — ViEWS introduced 2010 by Prytherch et al.; served as template for NEWS (UK, 2012) and NEWS2 (2017)
- [P335] **HECHO** — ViEWS authors explored adding +1 point for age ≥65 → no significant AUROC improvement
- [P336] **HECHO** — AEWS proposed 2019 by Shamout et al.; age-specific alerting ranges for composite outcome (mortality, cardiac arrest, unplanned ICU admission within 24h)
- [P337] **HECHO** — AEWS showed performance benefits specifically in younger patients
- [P338] **RESTRICCIÓN** — Classical EWS limitations: discard temporal info, single measurement set, no patient-specific info (sex, comorbidities), simple weighted-sum inference
- [P339] **RESTRICCIÓN** — EWS normality ranges difficult to maintain/update especially when based on human judgment/heuristics
- [P340] **HECHO** — Two EWS systems evaluated in Malawi cohort → both showed performance drop; disease/population differences significantly influence EWS performance → `Wheeler et al. 2013`

### 7.3 Modern Computational Approaches for Early Warning
- [P341] **HECHO** — First laboratory-based EWS (2005): binary logistic regression + 7 lab tests → predict in-hospital mortality → `Prytherch et al. 2005`
- [P342] **HECHO** — LDTEWS (2013) = decision tree analysis for females/males separately; tabularized for pen-and-paper use → `Jarvis et al.`
- [P343] **HECHO** — LDTEWS:NEWS (2018) = weighted sum of LDTEWS (lab) + NEWS (vitals) with linear decay weight; excluded if >5 days prior → `Redfern et al.`
- [P344] **HECHO** — LDTEWS:NEWS performed better than NEWS alone
- [P345] **DEFINICIÓN** — DEWS = Deep interpretable Early Warning System; attention-based recurrent deep neural network for clinical deterioration prediction → `Shamout et al. 2019c`
- [P346] **HECHO** — DEWS predicts composite outcome: in-hospital mortality / cardiac arrest / unplanned ICU admission within 24h
- [P347] **HECHO** — DEWS uses Gaussian process regression to sample posterior mean/variance at regular intervals from sparse vital-sign sequences
- [P348] **HECHO** — DEWS attention layer assigns importance score (0-1) to each timestep → interpretability
- [P349] **HECHO** — DEWS outperforms baselines in discriminative ability + decreases trigger rate at fixed sensitivity
- [P350] **HECHO** — Shamout et al. COVID-19 prognostic system: CNN processes chest X-rays + gradient boosting on clinical data → fused via weighted averaging; multi-task predicting deterioration within 24/48/72/96h; developed at NYU Langone Health
- [P351] **HECHO** — COVID-19 prognostic system predicts composite outcome: mortality / intubation / ICU admission in emergency department
- [P352] **HECHO** — All classical EWS systems (NEWS, AEWS, LDTEWS, LDTEWS:NEWS) significantly underperformed in COVID-19 cohort → `Youssef et al. 2021`
- [P353] **RESTRICCIÓN** — ML/DL models require large amounts of labeled data; data may be noisy; collection not viable in low-resource settings without digitized EHR
- [P354] **RESTRICCIÓN** — ML models prone to dataset bias → biased models in practice; model fairness = growing research area
- [P355] **RESTRICCIÓN** — ML-based EWS output overall risk score only; lack clinical response plan compared to classical EWS

### 7.4 Future Outlook
- [P356] **HECHO** — Systematic review (Alam et al. 2014): 7 studies on EWS clinical impact; only 2 showed significant mortality reduction
- [P357] **HECHO** — EWS deployment led to increased collection of vital-sign measurements in 2/7 studies
- [P358] **HECHO** — Scoping review (Muralitharan et al. 2021): 24 ML-based EWS studies; 23 retrospective, only 1 prospective
- [P359] **HECHO** — Single prospective ML-EWS study: random forest classifier, 178 patients → significant improvement detecting early deterioration signs → `Olsen et al. 2018`
- [P360] **OBLIGACIÓN** — Need more prospective validation studies to leverage positive clinical impact of EWS systems
- [P361] **ALCANCE** — Next-generation EWS should process diverse modalities: imaging, wearables data, genomic data, family history — not just vital signs
- [P362] **RESTRICCIÓN** — Most deterioration prediction algorithms developed in silo for particular cohort/outcome → narrow AI; need standardization toward general CDSS

### 7.5 Conclusion
- [P363] **HECHO** — CDSS value for patient safety recognized since early 2000s; modern ML approaches show promise but need prospective validation

## Ch8 — Mixed and Augmented Reality in Healthcare (Wrzesinska)

### 8.1 Introduction
- [P364] **DEFINICIÓN** — MR = Mixed Reality; physical + digital objects interact in real time; mix of AR + VR in 2D or 3D
- [P365] **HECHO** — Paul Milgram (1994) described MR as scale of reality — virtual continuum covering every state between real and virtual worlds
- [P366] **HECHO** — MR already used in education, military training, remote working, architecture, interior design, product content management
- [P367] **HECHO** — Global MR market CAGR predicted 47.9% during 2020-2025
- [P368] **HECHO** — Medical holography market projected: USD 500M (2021) → >USD 2B (2026)

### 8.2 Possible Use of Mixed Reality in Medicine
- [P369] **DEFINICIÓN** — Smart glasses = web-connected wearable computing devices allowing transmission/projection of data in field of vision
- [P370] **HECHO** — Google Glass = one of first smart glass models used in medicine; wireless, short learning curve, runs Android
- [P371] **HECHO** — Muensterer (pediatric surgeon) wore Google Glass 4 consecutive weeks at LMU Munich Children's Hospital → `Muensterer et al. 2014`
- [P372] **HECHO** — Jeroudi et al. compared ECG interpretation accuracy via Google Glass vs paper; users not satisfied with images vs paper version
- [P373] **HECHO** — Yale team used Google Glass for teleconferencing in emergency medicine triage during mass accidents → `Cicero et al. 2015`
- [P374] **HECHO** — Microsoft HoloLens = most commonly used MR platform; projects holographic 3D images; runs Windows OS; weight=566g
- [P375] **HECHO** — Imperial College London pilot: HoloLens2 during COVID-19 rounds; total exposure reduction=222.98 h/week; ~3100 fewer PPE items/week → `Martin et al. 2020`
- [P376] **HECHO** — Imperial College London study: 75% staff said HoloLens easy to navigate; >70% comfortable to wear; rounds less time-consuming
- [P377] **HECHO** — Levy et al. (London) COVID-19 study: no patient claimed MR headset disturbed medical care or interaction with staff
- [P378] **HECHO** — MR 3D holograms helpful to evaluate pulmonary lesions in COVID-19 patients, especially by less experienced doctors

### 8.3 AR and MR in Surgery
- [P379] **HECHO** — Smart glasses react to voice commands, eye movements, gestures → hands-free = especially helpful in surgery/sterile field
- [P380] **HECHO** — Wu et al. used Google Glass for ultrasound-guided central venous access → fewer additional head movements
- [P381] **HECHO** — MR holographic images = cheaper + faster than 3D printing for surgical planning; surgeon interacts in real time while remaining sterile
- [P382] **HECHO** — MR surgical holograms work with DICOM standard imaging: CT, MRI, angiography, 3D ultrasonography
- [P383] **HECHO** — HoloLens applied in orthopedic, plastic, neuro, oncological surgery and more
- [P384] **HECHO** — Brun et al.: first preoperative planning with MR for congenital heart disease; rated highly by all users
- [P385] **HECHO** — MR in liver anatomy: decreases time to correctly identify lesions; increases accuracy for some localizations → `Pelanis 2020`
- [P386] **HECHO** — Wierzbicki et al. (Cracow): HoloLens 2 used for irreversible electroporation / microwave ablation of unresectable pancreatic/liver tumors
- [P387] **HECHO** — 3D MR reconstructions most advantageous for trainees / less-experienced doctors
- [P388] **HECHO** — Augmedics Xvision Spine system = wireless AR surgical navigation for pedicle screw insertion; visualizes spine anatomy through skin/tissue → `Molina et al. 2019`
- [P389] **HECHO** — Gregory et al. shared reverse shoulder arthroplasty procedure video via HoloLens in real time with 4 specialists
- [P390] **HECHO** — Boilat & Rivas developed Digital Checklist Box (DCB): AR-projected WHO surgical safety checklist onto draped patient

### 8.4 MR in Endovascular Procedures
- [P391] **RESTRICCIÓN** — Major challenge of endovascular procedures = working with 2D images of 3D anatomy; multiple angiographic images → radiation/contrast exposure concerns
- [P392] **HECHO** — Opolski et al.: 15 percutaneous coronary interventions for chronic total occlusions with MR assist → lower contrast exposure
- [P393] **HECHO** — Wrzesinska used HoloLens during EVAR; Carna Life Holo app; one of first holographic visualization implementations during EVAR worldwide
- [P394] **HECHO** — EVAR involves radiation + iodine contrast agent (can cause acute kidney injury); fenestrated/branched stent-grafts = even more radiation/contrast/time
- [P395] **HECHO** — Garcia-Vazquez et al. proposed MR guidance system for EVAR with HoloLens + electromagnetic tracking using aortic aneurysm phantom
- [P396] **HECHO** — RealView Imaging (Israel) = first medical holographic system projecting 3D holograms in air without glasses; FDA cleared for clinical use
- [P397] **HECHO** — Bruckheimer feasibility study: RealView system during cardiac catheterization; 8 patients; all landmarks identified, no adverse events

### 8.5 MR in Education
- [P398] **HECHO** — Case Western Reserve University: medical students study anatomy via MR + HoloLens; compared to cadaver classes → no statistical difference in exam scores → `Stojanovska et al. 2019`
- [P399] **HECHO** — Prospective anatomy study: MR learning platform shortened study time vs cadaveric dissection; no difference in exam scores → `Ruthberg et al. 2020`
- [P400] **HECHO** — Kumar et al. used HoloLens + virtual face models for plastic surgery training → `Kumar et al. 2021`
- [P401] **HECHO** — Telementoring via AR/MR allows trainees to perform procedures monitored remotely by supervisor regardless of distance → `Mitsuno et al. 2019`
- [P402] **HECHO** — MR simulation-based training confirmed safe/effective; reduces complication rate; results similar to traditional training at lower cost → `Barsom et al. 2016`

### 8.6 Patients Also Can Use MR
- [P403] **ALCANCE** — Patient MR applications include: pain management, rehabilitation, pharmacological treatment planning, chronic disease management, telemedicine, patient education

### 8.7 Challenges
- [P404] **RESTRICCIÓN** — Most AR/MR devices not certified as medical devices; medical applications often require certification; legislation process slow
- [P405] **RESTRICCIÓN** — Data protection issues = main inhibitory factor for MR implementation in clinical use
- [P406] **HECHO** — North American region holds largest market share in medical holography
- [P407] **RESTRICCIÓN** — Google Glass battery life = 40 min; Microsoft HoloLens battery = up to 5.5h (~3h active use); poor battery life = barrier
- [P408] **RESTRICCIÓN** — Technical limitations of MR/VR: brightness, panel resolution, vergence-accommodation conflict → `Zhan et al. 2020`
- [P409] **HECHO** — HoloLens: user controls information amount for tolerable cognitive load; image quality/stability do not cause motion sickness
- [P410] **RESTRICCIÓN** — MR cost = significant gap between research and clinical implementation; MR/AR applications cost less than 3D printing
- [P411] **HECHO** — Younger generation practitioners more willing to try new technologies than older doctors; risk-averse medical mindset inhibits MR adoption
- [P412] **ALCANCE** — MR smart glasses healthcare applications: reading/interacting with data, communication/teleconsultation, video recording/streaming, workflow/documentation, patient empowerment, education, safety/efficiency

## Ch9 — Why Healthcare Needs Blockchain (Southey, Zarrebini)

### 9.1 The Promise of Blockchain for Healthcare
- [P413] **DEFINICIÓN** — Blockchain = shared read-write database where value objects exchanged/recorded between ≥2 parties without trusted intermediary
- [P414] **DEFINICIÓN** — Blockchain network embeds agreed rules of interaction; protocol acts as governance structure underpinning value exchanges
- [P415] **HECHO** — Blockchain enables disparate non-trusting entities to trade value objects peer-to-peer by trusting underlying code instead of central authority
- [P416] **REGLA** — Changes to blockchain governance rules generally require majority vote to amend protocol
- [P417] **DEFINICIÓN** — Digital assets on blockchain housed permanently at specific address; private key proves ownership required for transfer
- [P418] **DEFINICIÓN** — Blockchain state = snapshot of mini-economy showing current ownership; each new state cryptographically linked to previous state
- [P419] **REGLA** — Confirmation of new blockchain state achievable only through network consensus
- [P420] **DEFINICIÓN** — Blockchain Trilemma (Vitalik Buterin) = trade-off between decentralisation, security, scalability
- [P421] **HECHO** — Private permissioned blockchains prioritise scalability but limit decentralisation/security; use semi-trusted consortium consensus without crypto-economic incentives
- [P422] **HECHO** — Permissionless blockchains have larger networks with unknown/untrusted entities; use consensus mechanisms issuing cryptocurrencies as rewards
- [P423] **HECHO** — Bitcoin mining: cost of computing to control ledger far exceeds reward for honest behavior → miners incentivised to validate only valid transactions
- [P424] **HECHO** — Private permissioned blockchain can achieve acceptable ledger integrity without crypto-incentivisation
- [P425] **HECHO** — Blockchain recipients can self-verify author/content of transferred data, confirmed unaltered by network consensus
- [P426] **HECHO** — Large data volumes inefficient to store on-chain; digital hash recorded as transaction provides shared unalterable audit log
- [P427] **HECHO** — Single patient generates ~80 MB data/year in imaging + EMR (2017 estimates)
- [P428] **HECHO** — RBC Capital Markets projects healthcare data compound annual growth rate reaches 36% by 2025
- [P429] **HECHO** — ~30% of world's data volume generated by healthcare industry
- [P430] **HECHO** — IT investment in healthcare among lowest of all industries (IDC/Seagate report)
- [P431] **HECHO** — EY (2019) estimated UK NHS data value = GBP 9.6 billion/year
- [P432] **HECHO** — Global Big Data in healthcare estimated to reach $78.03 billion by 2027 → `Emergen Research`
- [P433] **HECHO** — Healthcare systems inherently complex with myriad stakeholders whose interests not always aligned
- [P434] **HECHO** — Healthcare increasingly adopting patient-centric approach, changing power dynamic in ecosystem
- [P435] **HECHO** — Healthcare generally lags other industries in technology adoption
- [P436] **⚠ TENSIÓN** — Healthcare industry centralising data in hands of multinationals despite increasing appetite for patient self-sovereignty/patient-owned data
- [P437] **HECHO** — Primary currency fuelling healthcare care delivery success/failure = data
- [P438] **HECHO** — ~500,000 deaths worldwide attributable to drug use; >70% related to opioids; >30% of those caused by overdose → `WHO`
- [P439] **HECHO** — U.S. payers spend >$2 billion/year maintaining provider databases; most credentialing processes take >120 days → `PwC/NAMSS`
- [P440] **HECHO** — Estimated loss of $200 million globally through counterfeit medications
- [P441] **HECHO** — Penn Medicine study: ~70% of CBD extracts sold online are mislabelled
- [P442] **HECHO** — JAMA study: 40% of CBD products online have drug concentration different from label; 26% had higher concentration; some contained THC sufficient to fail drug test
- [P443] **HECHO** — BIS Research: blockchain integration in healthcare could save >$100 billion/year by 2025 in IT, operations, support, personnel, data breach costs
- [P444] **HECHO** — Blockchain can provide significant benefits in clinical trial recruitment + enhance data provenance/security → `Zhuang et al. 2019`
- [P445] **ALCANCE** — Blockchains not ideal for high-volume data storage; usefulness for EHR sharing lies in storing access records, not records themselves
- [P446] **HECHO** — Blockchain server can verify data integrity + log access for later audit
- [P447] **DEFINICIÓN** — WEF (2021) framework for data economy: core principles = managing functional architecture of data exchange, governance, incentivisation of data sharing
- [P448] **HECHO** — Value derived from acquiring/combining data, low-latency access to high-quality data, extracting meaningful insights
- [P449] **HECHO** — Data economy incentives include policy/regulatory frameworks + monetary/non-monetary incentives (reciprocity, innovation opportunity, data credits)
- [P450] **HECHO** — Big Data validated >200 novel biomarkers predicting cardiovascular risk
- [P451] **HECHO** — Big Data investigated variation of 174,000 observed national prescribing patterns vs national guidelines for COPD
- [P452] **HECHO** — Big Data compared ~8,000 treatment outcomes for leukaemia by age, uncovering major unmet treatment need
- [P453] **HECHO** — >700 million records mined to develop new cancer risk-stratification algorithms
- [P454] **HECHO** — Healthcare data types: clinical, financial, operational, regulatory; owners/users include patients, providers, insurers, tech companies, manufacturers, payors, regulators
- [P455] **HECHO** — Patient recruitment for clinical trials known to be challenging; most trials not meeting recruitment requirements on time

### 9.2 Current Landscape of Blockchain in Healthcare
- [P456] **HECHO** — Research identified 75 companies claiming blockchain as part of healthcare solution
- [P457] **HECHO** — 75% of blockchain healthcare companies established in 2016/2017, correlating with ICO craze
- [P458] **HECHO** — ~2/3 of identified blockchain healthcare companies still active; ~1/3 inactive
- [P459] **HECHO** — Apparent drop-off in blockchain healthcare funding after 2017 likely due to ICO reputation
- [P460] **HECHO** — SEC deemed many blockchain "utility tokens" to be securities
- [P461] **HECHO** — CoinMarketCap review (Fang 2021) identified 10 commercially successful blockchain healthcare projects; majority in personal health tracking
- [P462] **REGLA** — Understanding tokenomic models critical to long-term success of blockchain healthcare projects
- [P463] **HECHO** — Table 9.2 lists 49 active blockchain healthcare companies across EHR, supply chain, credentialing, clinical trials, security, genomics, payments domains → `Catena.MBA 2022`

### 9.3 Future Vision for Healthcare Blockchains
- [P464] **HECHO** — EU Blockchain Observatory Forum survey: highest-value use cases = data transparency (91.1%), pharma supply chains (88.2%), data immutability (85.3%)
- [P465] **HECHO** — EU survey continued: medical records sharing (79.4%), secure payment transactions (76.5%), record accuracy (73.5%), data interoperability (70.6%)
- [P466] **HECHO** — Healthcare professional knowledge requirements rising exponentially; increased need for multidisciplinary cross-collaboration
- [P467] **HECHO** — Healthcare complexity renders systems more prone to errors → `Braithwaite et al. 2017`
- [P468] **HECHO** — Patient trust in virtual care services reduced compared to traditional environments → `Hasselgren et al. 2020`
- [P469] **HECHO** — Current health technologies struggle with interoperability; perceived usability remains challenge → `Son et al. 2021`
- [P470] **RESTRICCIÓN** — GDPR creates concerns for immutable ledgers in healthcare; GDPR-compliant blockchain solutions exist
- [P471] **HECHO** — "Garbage in, garbage out" applies to health data on blockchain; inaccuracies carried forward → `Wong et al. 2019`
- [P472] **OBLIGACIÓN** — Allen et al. (2020) recommend developing scenario-based ethical dilemmas across blockchain healthcare uses
- [P473] **HECHO** — Federated Learning may enable privacy-preserving dataset sharing → `Li et al. 2021`
- [P474] **HECHO** — Technology change = 75% cultural + 25% technical
- [P475] **HECHO** — 30% of world's data currently locked in silos preventing treatment innovations/better health outcomes
- [P476] **HECHO** — Blockchain represents coopetitive model relying on stakeholders seeing greater benefit in sharing common infrastructure
- [P477] **HECHO** — Blockchain = governance technology; building rules of engagement equally important as technology choices
- [P478] **HECHO** — Blockchain Research Institute (Canada) template: principles = Think "We" vs "I", evangelise new perspective, identify Minimally Viable Ecosystem/Network

## Ch10 — Nudging to Change, the Role of Digital Health (Purohit et al.)

### 10.1 Introduction
- [P479] **HECHO** — Most diseases preventable by assisting people to change habitual risky behaviors → `Kelly 2000`
- [P480] **HECHO** — Risky health behaviors negatively associated with health: sedentary lifestyle, smoking, unhealthy eating, binge drinking
- [P481] **HECHO** — Millions of premature deaths preventable if individuals stop smoking; smoking causes lung cancer + increases pulmonary/cardiovascular disease risk

### 10.2 Background
- [P482] **DEFINICIÓN** — Nudge = any aspect of choice architecture that changes behavior predictably without prohibiting options or significantly changing incentives → `Sunstein/Thaler 2008`
- [P483] **DEFINICIÓN** — Digital nudge = nudge provided through digital technology employing UI design elements to influence decisions/behaviors without restricting choice → `Weinmann et al. 2016`
- [P484] **HECHO** — Mobile phones compelling behavior change support systems due to: (1) gathering contextual/biometric data, (2) 24/7 reachability, (3) push notification capability
- [P485] **DEFINICIÓN** — Teachable moments = naturally occurring health events thought to motivate individuals to adopt risk-reducing behaviors spontaneously → `Purohit/Holzer 2019`
- [P486] **HECHO** — Most digital nudge studies do not address timing explicitly despite "just-in-time" technology potential
- [P487] **HECHO** — Ford et al. (2010): real-time feedback during meals helped obese adolescents eat more slowly → weight loss
- [P488] **HECHO** — Intille et al. (2003): dietary behavior change information provided on PDA at time of purchase to motivate incremental change
- [P489] **HECHO** — Digital nudges delivered via mobile can be more fine-tuned than traditional nudges to fit optimal timing through adequate identification of user context

### 10.3 Digital Nudging Strategies
- [P490] **DEFINICIÓN** — Default nudge = predefined option chosen by system designer exploiting status quo bias
- [P491] **HECHO** — Organ donor list increased 60% in countries where organ donation is default opt-out vs national average 38% in opt-in countries → `Thaler et al. 2014`
- [P492] **HECHO** — Default permanent flu vaccine appointments increased vaccination possibility → `Lehmann et al. 2016`
- [P493] **HECHO** — Defaults produce large effects because individuals lack explicit preferences for every possible good/service
- [P494] **DEFINICIÓN** — Reminder nudge = brings choice to user's attention via visual/sound/haptic cue (e.g., push notification)
- [P495] **DEFINICIÓN** — Feedback nudge = informs users about task performance to raise awareness/rectify misconceptions about problematic behavior
- [P496] **HECHO** — Feedback nudge can be tailored/personalized to individual to solve heterogeneity problem
- [P497] **DEFINICIÓN** — Social nudge = informs individuals about what others are doing; establishes social norms users motivated to follow (peer comparison)
- [P498] **DEFINICIÓN** — Framing nudge = deliberate phrasing of information presentation to encourage target behavior; people respond differently to loss vs gain framing → `Tversky/Kahneman 1985`
- [P499] **DEFINICIÓN** — Suggesting alternatives nudge = providing individuals about to make decision with alternatives they might not have considered
- [P500] **DEFINICIÓN** — Positioning nudge = changing visual presentation of options exploiting status-quo bias; more salient options chosen more often
- [P501] **HECHO** — Repositioning food choices to make nutritious food more prominent increased sales in physical settings → `Ensaff et al. 2015`
- [P502] **HECHO** — Wyse et al. positioned nutritious food at top of online food ordering platform → increased selection of nutritious food

### 10.4 Digital Nudges in the Continuum of Care
- [P503] **DEFINICIÓN** — Continuum of care = provision of healthcare over time through 5 phases: prevention, pre-acute, acute, post-acute, chronic home-care
- [P504] **HECHO** — Milkman et al. used text-based framing nudges → increased influenza vaccination rate by 5% when reminded twice + informed appointment already booked
- [P505] **HECHO** — Xu et al. employed feedback nudges to improve dietary behavior/physical activity for patients at high risk for type 2 diabetes
- [P506] **HECHO** — Boillat et al. proposed smart glasses for surgical time-out checklist → 100% completion rate + 18% decrease in average checklist duration
- [P507] **HECHO** — Gamification elements (competition, awards, timely feedback) = digital nudges integrated into game mechanics; used for motor training in stroke patients
- [P508] **HECHO** — Immersive VR therapy based on gamification can benefit balance problems in chronic ischemic stroke → `Cortes-Perez et al. 2020`
- [P509] **HECHO** — Perez-Marcos et al. (2017): gamification-based games for functional training of upper limb after brain damage
- [P510] **HECHO** — Elderly heart attack patients significantly motivated to increase physical activity with loss-framed incentives + personalized goals using wearable device → `Chokshi et al. 2018`
- [P511] **HECHO** — Horne et al. (2022): 12-month RCT showed AI-formulated digital nudges via email/SMS/voice calls → nudge group adhered to medicine significantly more than control group
- [P512] **REGLA** — Thaler's ethical nudge guidelines: nudges should be (1) transparent, (2) easy to opt-out, (3) designed for user wellbeing → `Thaler 2018`
- [P513] **HECHO** — Transparency has two aspects: goal of nudge should not be deceitful + mechanism must be transparent including data usage/privacy
- [P514] **HECHO** — Individuals being nudged often unaware of nudge or psychological mechanisms employed by choice architect

### 10.5 Landscape of Digital Nudging in Digital Health
- [P515] **HECHO** — JMIR scoping review searched for "nudging"/"nudges"/"nudge"/"digital nudges"; yielded 150 articles; 19 included
- [P516] **HECHO** — Among 19 included studies, 30 nudges used; 7 studies employed ≥2 nudging techniques
- [P517] **HECHO** — Most common digital nudges in review = feedback + reminders; applied in prevention + post-acute care
- [P518] **HECHO** — No studies in review investigated default nudges
- [P519] **HECHO** — No studies in review investigated nudges for acute care phase
- [P520] **HECHO** — Digital nudging studies in digital health increased >160% since 2018
- [P521] **HECHO** — Most reviewed papers focus on increasing desired behavior; nudges not used to solely reduce unwanted behavior
- [P522] **HECHO** — Only 1/19 reviewed studies explicitly discussed ethical considerations while designing intervention → `Neto et al. 2021`
- [P523] **HECHO** — Feedback/reminder nudges inherently transparent in objective; framing/default/social comparison nudges inherently not transparent
- [P524] **RESTRICCIÓN** — Scoping review limited to JMIR database + mainly focused on digital nudging for patients, not clinicians
- [P525] **HECHO** — Challenges in nudging away from undesired behavior: identification of behavior + providing adequate feedback on negative behavior
- [P526] **HECHO** — Rise of feedback nudges driven by wide adoption of smart devices enabling tracking of motion, steps, heart rate
- [P527] **HECHO** — Opting out challenging for default/framing/positioning nudges compared to feedback nudges
- [P528] **HECHO** — Unintended nudges (positioning/defaults) unavoidable in system design; challenge = ensuring design decisions aligned with patient welfare, not dark patterns

### 10.6 Conclusion
- [P529] **HECHO** — Current research mainly focuses on feedback/reminder nudges for prevention + post-acute care; several effective strategies (defaults) absent from literature
- [P530] **OBLIGACIÓN** — Development/promotion of ethical analysis grid crucial to guide practitioners/researchers in designing effective + ethical nudges for digital health

## Ch11 — The Role of Design in Healthcare Innovation and Future Digital Health (Montana-Hoyos et al.)

### 11.1 Introduction
- [P531] **HECHO** — WHO (2014) estimated worldwide shortage ~4.3 million health workers
- [P532] **HECHO** — Post-COVID-19 pandemic health worker shortage now estimated at 18 million → `WHO 2021`
- [P533] **HECHO** — Digital health = cultural transformation where disruptive technologies provide digital/objective data → equal doctor-patient relationship with shared decision-making → `Mesko et al. 2017`
- [P534] **HECHO** — Development/acceptance/performance of digital health interventions largely dependent on good design

### 11.2 Towards a Definition of Design
- [P535] **DEFINICIÓN** — Design = both action (creative thinking/problem-solving process) and result (outcome of that process)
- [P536] **DEFINICIÓN** — Affordance = property where physical characteristics of object/environment influence its function → `Butler et al. 2003`
- [P537] **DEFINICIÓN** — Co-design (= generative design/co-creation/participatory design) = process of exploratory research + developmental design to define/address problem together with end user
- [P538] **DEFINICIÓN** — Design Thinking = iterative process: empathise → define needs → ideate → prototype → test; unlike co-design, not dependent on creating solution with end user
- [P539] **HECHO** — Design has syntactic (how made), pragmatic (how used), semantic (how perceived/communicated) functions → `Boucharenc 2008; Bonollo 2010`

### 11.3 The Role of Design in Healthcare Innovation
- [P540] **HECHO** — Traditional healthcare = "doctor hero" scenario; patients not involved in decision making about own health/disease management
- [P541] **HECHO** — Design has direct effect on how patients/caregivers feel; intentional design → patients feel more at ease/calm/secure → `Solis 2020`
- [P542] **HECHO** — Designers navigate healthcare system as relative outsiders to understand parameters/conditions for solution development → `Park 2020`
- [P543] **HECHO** — People involved in change from start more likely to feel ownership → less likely to oppose agreed solution → `Design Commission 2013`

### 11.4 Design in Healthcare Innovation and Digital Health
- [P544] **DEFINICIÓN** — Health (WHO 2022) = state of complete physical, social, mental well-being, not merely absence of disease/infirmity
- [P545] **HECHO** — Lack of user engagement in proposed digital health solutions = area where design role in healthcare innovation became necessary
- [P546] **HECHO** — Matthews (2015): Design in healthcare improves safety, dignity, efficiency, sustainability
- [P547] **HECHO** — COVID-19 pandemic (2020) caused global collapse of healthcare services delivery, revealing need for drastic innovation
- [P548] **HECHO** — Complexity of healthcare challenges demands profound system innovation; design plays critical role in engaging multidisciplinary teams → `Patricio et al. 2019`

### 11.5 Design and Hospitals of the Future
- [P549] **HECHO** — Growing number of inpatient services being pushed to home/outpatient ambulatory facilities; complex/very ill patients continue needing acute inpatient services → `Deloitte 2017`
- [P550] **HECHO** — Hospitals experimenting with: customized patient rooms (digital screens), automation/robotics, digital patient experience (AI/ML), centralized clinical command centers
- [P551] **DEFINICIÓN** — Scenarios = projection of concrete narrative description of user activity during specific task, sufficiently detailed for design implications → `Carroll 1997`
- [P552] **HECHO** — Chamorro-Koc et al. (2012): scenarios employed to understand everyday practices + reveal stakeholder relationships in service provision

### 11.6 Design Narratives and Design Fiction
- [P553] **DEFINICIÓN** — Design fiction = deliberate use of diegetic prototypes to suspend disbelief about change; term coined 2005 by Bruce Sterling
- [P554] **HECHO** — Design fiction established field of design research for creating/imagining/visualizing possible futures → `Grand/Wiedmer 2010`
- [P555] **HECHO** — Design fiction enables co-creation processes exploring applications + implications of interactions with future/emerging technologies

### 11.7 Future Healthcare Innovation and Digital Health Design Projects
- [P556] **HECHO** — Buckminster Fuller (1982): "You never change things by fighting existing reality. To change something, build new model that makes existing model obsolete"
- [P557] **HECHO** — 2013 futuristic ICU project: user-centred design at Calvary John James Hospital + Canberra Hospital proposed fully integrated ICU bedspace using witricity + holograms → `Montana-Hoyos et al. 2016`
- [P558] **DEFINICIÓN** — Witricity = wireless power transfer developed by MIT researchers → `Gozalvez 2007`
- [P559] **HECHO** — Witricity in ICU could eliminate "spaghetti syndrome" (multiple chords/tubes/cables) common in hospitals
- [P560] **HECHO** — HealthPod (2016): digital health intervention co-designed with patients/students/medical staff for GP clinic data collection improvement
- [P561] **HECHO** — GP clinic datasets often incomplete (missing demographics, height, weight, behavioral risk factors) → `Volker et al. 2014`
- [P562] **HECHO** — HealthPod = patient kiosk with custom-built program feeding into clinic database + graphical UI; generated physical report card
- [P563] **HECHO** — Design fiction projects (2018+): students analysed emerging technologies to create 2050 life scenarios including 4D printing, bio-printing, emotion sensing AI, electronic tattoos
- [P564] **HECHO** — E-tattoos = new generation thin adhesive surfaces behaving like skin with embedded electronics; potential future wearables
- [P565] **HECHO** — Pediatric pain currently assessed by 1-10 scale or happy-to-sad faces; tiredness/emotions may influence nurse/clinician accuracy
- [P566] **HECHO** — TAME = Pediatric Pain Metric device using sensors (temperature, tremors, heart rate) + screen for simple visualization of pain/anxiety level → `Chamorro-Koc et al. 2021`
- [P567] **HECHO** — COVID restrictions prevented hospital observations; design thinking enabled alternative remote data collection via photo ethnography + retrospective interviews
- [P568] **HECHO** — VR used as diversional therapy for pain management; Desselle et al. (2020) designed VR for anxiety/pain management of burns patients
- [P569] **HECHO** — TAME demonstrated scenario where technology affordances applied to humanise empathy building, not centred on technology functionality alone
- [P570] **HECHO** — Hospitals of Future envisioned as smart environments: error-free, effective, patient-centered → `Pickering et al. 2012`
- [P571] **HECHO** — Technology innovation in healthcare lags implementation mainly due to sector being highly regulated
- [P572] **HECHO** — COVID pandemic accelerated move to digital/virtual meetings; aging population migrated to telehealth/phone/videoconference consultations

### 11.8 Conclusions
- [P573] **HECHO** — Blockchain/cryptocurrencies/Metaverse opening possibilities for completely digital immersive world including NFTs, DAOs
- [P574] **HECHO** — Potential digital health benefits: democratization/wider coverage of basic health services, "hospital at home" opportunities, focus on preventive healthcare
- [P575] **⚠ TENSIÓN** — Potential digital health risks: exclusion due to "digital divide" especially aging population, remote areas, people purposely isolated from digital world
- [P576] **HECHO** — Design = conscious intention to modify environment to benefit human progress + increase social good
- [P577] **HECHO** — Design works with ambiguity + transdisciplinary teams; enables exploration of person-centred future digital health solutions
- [P578] **HECHO** — Design contributes to quality improvement in healthcare by catalysing innovation; co-creation with stakeholders/policymakers addresses gaps between technology innovation + regulatory reform
- [P579] **HECHO** — Design champions humanisation of technology through person-centred approach ensuring future technologies conceptualised with end-users

## Ch12 — Medical Schools and Digital Health (Boillat, Otaki, Kellett)

### 12.1 Introduction
- [P580] **DEFINICIÓN** — Digital therapeutics (DTx) = delivery of evidence-based therapeutic interventions via qualified software programs to prevent/manage/treat medical conditions
- [P581] **HECHO** — DTx received FDA approval; some health insurance companies prescribe/reimburse them
- [P582] **HECHO** — VR successfully used in clinical settings to fight phobias, stress, anxiety, eating disorders
- [P583] **HECHO** — VR used to reduce chronic/acute pain among adults and children
- [P584] **HECHO** — Activity trackers detected Atrial Fibrillation in clinical trials involving ~500,000 participants
- [P585] **HECHO** — DHT run on devices not designed exclusively for healthcare → complicates safe leveraging by professionals
- [P586] **HECHO** — Patients use DHT to collect physical activity, sleep patterns, heart rate variability data that physicians cannot leverage due to lack of training
- [P587] **HECHO** — Scoping review found most DHT studies in medical schools focused on medical informatics/EHR; only 9% covered telehealth, 3% covered mHealth
- [P588] **HECHO** — >50% medical students perceive their DHT competences as poor/very poor

### 12.2 Background: Some Data
- [P589] **HECHO** — Systematic analysis of 60 curricula (top 10 medical schools per continent, Times Higher Education) found only 4 schools teaching digital health elements
- [P590] **HECHO** — Stanford University most active with 3 DHT offerings through Byers Center for Biodesign
- [P591] **HECHO** — Stanford Biodesign for Digital Health = quarter-long course requiring multidisciplinary teams (medicine + bioengineering) to identify needs/prototype DHT solutions
- [P592] **HECHO** — Stanford Biodesign Innovation = 2-quarter course; medicine/bioengineering/mechanical engineering/IT students identify unmet health needs
- [P593] **HECHO** — Stanford Biodesign programs are elective, carry 3-4 credits, use problem-based approach
- [P594] **HECHO** — Johns Hopkins offers DHT extra-curricular classes via dual MBA/MD Design Lab teaching human-centered approaches
- [P595] **HECHO** — Johns Hopkins Technology Ventures FastForward provides accelerator programs, seed funding, mentorship
- [P596] **HECHO** — Yale course "New Ventures in Healthcare and Life Sciences" covers digital health/medical devices from needfinding to prototyping/commercialization
- [P597] **HECHO** — University of Zurich = only non-American institution offering e-health/telemedicine and AI in medicine courses as electives for 2nd-year medical students
- [P598] **HECHO** — One university piloted digital health program with 10 medical students; 22 teaching units covering telemedicine/health economics/AR/VR/mHealth/wearables/health innovation
- [P599] **HECHO** — Systematic analysis of American medical schools identified 7 additional universities with DHT offerings; only 1 had teaching integrated in medical curriculum

### 12.3 Why Should Medical Schools Teach Digital Health?
- [P600] **HECHO** — Flexner Report (1910) = transformative turning point in medical education, emphasized incorporating scientific theory into curricula
- [P601] **HECHO** — Abraham Flexner was nonphysician professional educator who explored state/quality of medical education across US/Canada
- [P602] **HECHO** — Flexner Report made biomedical model hallmark of modern medical education but emphasis on rational world eroded physician-as-trusted-healer concept
- [P603] **HECHO** — AMA launched Accelerating Change in Medical Education initiative in 2013 to support US healthcare transition from acute to chronic care
- [P604] **DEFINICIÓN** — Health System Science (HSS) framework = competences 21st-century medical students/trainees/physicians should acquire; complements basic + clinical sciences via systems thinking
- [P605] **HECHO** — HSS framework has 4 domains: (1) teaming, (2) leadership, (3) change agency/management/advocacy, (4) ethical/legal matters; core = patient/family/community
- [P606] **HECHO** — Clinical informatics/health technology = sub-domain under HSS domain 3; common topics: EMR, data analysis, digital libraries, decision support tools
- [P607] **RESTRICCIÓN** — DHT definition broad/subjective → technologies/concepts covered vary by institution depending on competence, vision, population needs
- [P608] **RESTRICCIÓN** — DHT lecturers must understand both hardware technicality and medical applicability; such multidisciplinary profiles are scarce
- [P609] **RESTRICCIÓN** — Many medical schools/teaching hospitals rely on outdated computing systems → system integration difficult, interoperability reduced
- [P610] **HECHO** — Medical schools often lack state-of-the-art equipment (AR/VR headsets, 3D printers) and personnel to maintain them

### 12.4 Incorporating DHT: Challenges
- [P611] **HECHO** — Introduction of DHT in medical school curricula brings multi-dimensional challenges beyond scheduling/assessment

### 12.5 Next Steps: Course Curriculum
- [P612] **HECHO** — MBRU course "Innovation and Technologies for Health Sciences" taught to 1st-year medical students, Dubai, UAE
- [P613] **HECHO** — MBRU DHT course = 6 weekly sessions of 50 min each; delivery modes: lectures, tutorials, case studies
- [P614] **HECHO** — MBRU DHT course focuses on technology functionalities from medical professional perspective, not solely on technologies themselves
- [P615] **HECHO** — Students complete "3-2-1 feedback form" after each lecture: 3 new things learned, 2 things that caught attention, 1 further question
- [P616] **HECHO** — Week 1: Digital Health — covers limitations of non-digital healthcare, introduces EMR, defines digital health, key components of healthcare system
- [P617] **HECHO** — Week 2: Persuasive Computing/mHealth — covers non-communicable diseases, BJ Fogg behavioral change model, mobile device role in behavioral change
- [P618] **HECHO** — Week 3: Wearable Technologies — covers types of wearables, Quality of Life, activity tracker mechanics, body sensors/smart clothing/smart jewelry/bio-tattoos
- [P619] **HECHO** — Week 4: AR/VR — case study of smart glasses for surgical safety checklists, define/contrast AR and VR, benefits/limitations
- [P620] **HECHO** — Week 5: AI in Medicine — covers AI history, ML to DL concepts, supervised/unsupervised algorithms, benefits/limitations
- [P621] **HECHO** — Week 6: Future of Care Delivery — patient journey mapping, AI-based chatbots/telehealth, 3D printing, drones

### 12.6 Discussion and Conclusion
- [P622] **HECHO** — DHT are consumer products developed by technology companies with different manufacturing/testing/certification/sales channels compared to medical devices
- [P623] **HECHO** — In 2020, ~100,000 new digital health apps released on app stores
- [P624] **HECHO** — Activity tracker price range: $5 ("no-name") to $749 (Apple Watch)
- [P625] **HECHO** — Some private institutions (e.g., ORCHA) help patients/physicians select digital apps based on evaluation thoroughness
- [P626] **REQUISITO** — Profound restructuring of medical curriculum required, integrating technologies as core pillar — not just limited credit hours as elective under HSS
- [P627] **HECHO** — Texas A&M graduates "Physicianeers" via collaboration between College of Engineering, College of Medicine, state hospital; graduates receive master's in engineering + Doctor of Medicine
- [P628] **HECHO** — Duke University offers dual MD-MEng program via Pratt School of Engineering + School of Medicine
- [P629] **HECHO** — In US, only 1-2% of graduating engineers apply to medical school; biological sciences majors form overwhelming majority
- [P630] **REQUISITO** — Both engineering and medical colleges should engage in awareness/promotional campaigns to explain value of engineer-to-physician path

## Ch13 — Opportunities and Challenges of Digital Global Health (Ishii-Rousseau, Seino)

### 13.1 Introduction
- [P631] **DEFINICIÓN** — Global health = multidisciplinary field aiming to achieve equitable healthcare access for all, predominantly operating in LMICs
- [P632] **HECHO** — Traditional global health innovation centralized on delivery of care rather than novel technologies from high-resource settings
- [P633] **HECHO** — UN SDGs emerged in 2015; World Bank Human Capital Index (HCI) emerged in 2018 → frameworks for tackling shared global challenges
- [P634] **HECHO** — High expectations for digital solutions in LMICs, especially with emergence of low-cost mobile-based technologies
- [P635] **HECHO** — Significant health inequities persist in 21st century; challenges include cardiovascular disease, injuries, cancer, infectious disease, mental illness in LMICs
- [P636] **HECHO** — Purpose of digital innovation in global health = enhance healthcare access/patient-centric care, not replace or displace
- [P637] **HECHO** — Mobile phones regarded as key for "next billion" global citizens to go online
- [P638] **HECHO** — 5G theoretically increases network speed from 4G's 300 Mbps to ~10-30 Gbps
- [P639] **HECHO** — 5G features: ultra-fast Internet, low-latency, decreased energy usage, improved reliability → expands digitization of every industry
- [P640] **HECHO** — "Non-cellular" 5G can realize low-cost, high-functioning, seamless, decentralized environment for digital health innovation
- [P641] **HECHO** — Health has yet to be effectively integrated in IT circuit despite rapid digitization of other sectors
- [P642] **HECHO** — Global health settings have not fully benefited from affordable health apps due to challenges in smartphone/broadband availability

### 13.2 Opportunities for Digitization in Global Health
- [P643] **HECHO** — Digitization in global health shown effective in: medication management, emergency response, vaccinations, safer sexual practices, disease surveillance, clinical imaging
- [P644] **HECHO** — Digital health contributed to enhanced facility triage/management, reduced emergency response delays, improved vaccine coverage, lowered costs
- [P645] **HECHO** — COVID-19 exacerbated need for digital health deployment in LMICs with large regional discrepancies in health resource availability
- [P646] **HECHO** — Scoping review recommended national scaling up of pilot projects while evaluating costs for nationwide implementation/ROI
- [P647] **HECHO** — LMICs encouraged to provide evidence on health digitization → enabling frameworks to decrease risks/amplify investment impact
- [P648] **HECHO** — Digital health interventions empower LMICs to leapfrog and accelerate development in self-sufficient manner
- [P649] **HECHO** — Uganda Ministry of Health launched HMIS to accumulate/analyze health data from public/private health facilities
- [P650] **HECHO** — Similar systems in South Africa, Kenya, Tanzania, Zambia, Mozambique, Nigeria showed improved patient data retrieval/reporting
- [P651] **HECHO** — Health IT proven to improve quality of care/efficiency through adherence to diagnosis guidelines/protocols in India
- [P652] **HECHO** — Uganda digital pathology platform automates diagnosis/classification of cervical cancer from pap smear images
- [P653] **HECHO** — Uganda mobile ambulance service dispatch system reduces time/cost/errors in delivering patient care
- [P654] **HECHO** — UNICEF-backed clinical data ecosystem by Global Auto Systems deployed across 4 hospitals in Uganda
- [P655] **HECHO** — WHO Table 13.1: Infectious disease → digital solution = real-time disease monitoring/rapid emergency communication
- [P656] **HECHO** — WHO Table 13.1: Health access inequities → digital solution = low-cost secure telehealth + data analysis for discrepancies
- [P657] **HECHO** — WHO Table 13.1: Health worker shortages → digital solution = low-cost educational/data sharing platforms + telehealth
- [P658] **HECHO** — WHO Table 13.1: Non-communicable diseases → digital solution = mobile delivery of healthier life habits/routines
- [P659] **HECHO** — WHO Table 13.1: Climate change → digital solution = low-cost diagnostic tools + dashboards for climate-health transparency
- [P660] **HECHO** — WHO Table 13.1: Conflict/misinformation → digital solution = telemedicine/mobility tools for swift healthcare delivery
- [P661] **HECHO** — Cost-effective mHealth/DHT deployment areas: patient data management (EHR, biometrics, blockchain), improved clinical care (AI imaging, NLP), innovative care delivery (drones, digital mobility)
- [P662] **HECHO** — Drone delivery (Zipline, Matternet) deployed for urgent blood supplies, prescription medicine, vaccines, AEDs in low-resource areas
- [P663] **HECHO** — Telemedicine kits (Ghana Healthcenter Telemedicine, VSee) include tablets/stethoscopes/oximeters/ultrasounds for full exams in inaccessible zones
- [P664] **HECHO** — Possible Health EHR = public-private partnership using open-source components for patient tracking/clinical protocols/pharmacy/lab/imaging
- [P665] **HECHO** — Allm Inc. = secure smart device platform for doctor-to-doctor patient data sharing/handoff/care coordination
- [P666] **HECHO** — NEC/Simprints = biometric child fingerprint identification via smart devices for vaccination administration
- [P667] **HECHO** — Blockchain solutions (Factom, MIT MedRec) = decentralized ledger for proof of work/identification, smart contracts
- [P668] **HECHO** — WHO compiles Compendium of Innovative Health Technologies for Low-Resource Settings since 2011
- [P669] **RESTRICCIÓN** — Implementation challenges in digitizing healthcare include environmental/infrastructural, financial, educational, cultural, political hurdles
- [P670] **⚠ TENSIÓN** — If unanswered, digitization challenges could exacerbate existing ethnic, socioeconomic, gender inequities

### 13.3 Implementation Challenges for Digital Global Health
- [P671] **HECHO** — Digital health implementation causes "chicken or egg" dilemma: digital solutions aid creation of baselines needed to justify their own implementation
- [P672] **HECHO** — USAID typology of innovation permits flexibility to pivot quickly when discrepancy exists between technology and ground needs
- [P673] **REQUISITO** — Local academia, public/private sector, non-profit sector must be included early in digital health transformation discussions in LMICs
- [P674] **HECHO** — 7 implementation challenges in digital global health: (1) lack of resources, (2) lack of specialists, (3) lack of urgency, (4) lack of training, (5) lack of standardization, (6) lack of monitoring/evaluation, (7) lack of optimism
- [P675] **HECHO** — MIT Critical Data consortium's "Ecosystem as a Service (EaaS)" approach provides low-cost sustainable solution for digital health capacity building
- [P676] **HECHO** — Developed countries shifted from computer-based to smart device/cloud-based health technologies → continuously widening capacity divide with LMICs
- [P677] **HECHO** — 2021 report: Sub-Saharan Africa worst for fixed-line broadband cost; majority of countries categorized highly expensive (monthly average 370-710 USD per broadband package)
- [P678] **HECHO** — Mexico = 2nd largest economy in Latin America, classified upper middle-income by World Bank
- [P679] **HECHO** — Mexico 2020: 93 per 100 capita subscribed to mobile cellular services
- [P680] **HECHO** — Mexico 2019: 69% rural population lacked Internet access; only 60-70% urban population connected
- [P681] **HECHO** — Only 1 private university in Mexico found with capacity to provide AI/data science education
- [P682] **HECHO** — Mexican specialists attribute situation to lack of sufficient evidence to convince government officials + low knowledge about digital health
- [P683] **HECHO** — MIT Critical Data consortium collaborating with Mexican researchers on data science/digital health
- [P684] **RESTRICCIÓN** — Governments identified as key financier of digital health transformation; private sector CSR contributions also increased
- [P685] **REQUISITO** — Sustainable digital health financing requires combination of government, private sector, donor efforts + discussions on exit strategies for donor reliance
- [P686] **DEFINICIÓN** — "Accompagnateur" = innovative Community Health Worker (CHW) process for healthcare delivery spearheaded by Partners in Health (PIH)
- [P687] **RESTRICCIÓN** — Developing countries often supported by donor countries/overseas institutions advised by international agencies → limited local input
- [P688] **REQUISITO** — Health systems/technology must reflect specific clinical/cultural needs of populations served; local researchers must play greater role

### 13.4 Future Directions
- [P689] **HECHO** — Digital health adoption in global health settings will likely persist/increase over next decade
- [P690] **RESTRICCIÓN** — Risk of LMICs facing interoperability/data sharing challenges currently seen in high-income countries
- [P691] **REGLA** — Accompaniment Approach step 1: Learn from locals — understand best practices, bottlenecks, priority needs; seek guidance from most marginalized communities
- [P692] **REGLA** — Accompaniment Approach step 2: Find local/global partners — stimulate local economies, enable sustainable capacity building/knowledge transfer
- [P693] **REGLA** — Accompaniment Approach step 3: Discuss strategies with policymakers early → aids leapfrogging, coordinates siloed efforts
- [P694] **REGLA** — Accompaniment Approach step 4: Co-invest with governments for sustainability/national growth
- [P695] **REGLA** — Accompaniment Approach step 5: Evaluate/disseminate best practices → pooling/open-sourcing information creates ecosystem for digital global health
- [P696] **HECHO** — Medicine/treatment adherence long-standing issue in India, especially among younger populations
- [P697] **HECHO** — India 2015 study: drug adherence for hypertension more common among patients closer to health facilities
- [P698] **HECHO** — India 2020 study: antiretroviral drug adherence higher among patients with familial support
- [P699] **HECHO** — India PM Narendra Modi announced target to eliminate TB by 2025, 5 years ahead of global target of 2030
- [P700] **HECHO** — India established National Strategic Plan (NSP) for TB 2020-2025 with revised actions
- [P701] **HECHO** — India has highest TB burden globally; ~40% population infected
- [P702] **HECHO** — mHealth solutions (SMS/voice call reminders via low-cost mobile phones) proven useful in improving drug adherence in India
- [P703] **HECHO** — SMS/voice call reminder systems show promise for surveillance/treatment of other diseases even in areas with low bandwidth/low smartphone penetration

### 13.5 Conclusion
- [P704] **HECHO** — Digital health adoption in global health will persist; local context/partnership critical for success

## Ch14 — Future Landscape in Digital Health (Rivas, Boillat)

### 14.1 Introduction
- [P705] **HECHO** — In 2011 StarCraft cyber tournament awarded 25 bitcoins to losers; those bitcoins later worth >$1,000,000 — illustrating unpredictability of value/technology forecasts

### 14.2 The Future Landscape of Digital Health
- [P706] **HECHO** — Healthcare innovations adopted slower than most other industries; reasons include need for long-term clinical trials, application to human beings
- [P707] **HECHO** — Most important reason for slow healthcare innovation adoption = prevalent risk-aversion mindset ingrained in physicians/care providers
- [P708] **ALCANCE** — Future healthcare framework organized around 3 cornerstones: discovery/research, education, clinical care
- [P709] **HECHO** — Digital health uniquely portable → can provide extensive access to care to masses
- [P710] **HECHO** — In near future, most/all clinical trials will include digital health; many well-designed trials will not require subjects to visit clinic/hospital
- [P711] **HECHO** — COVID-19 pandemic dramatically removed barriers to digital health innovation by even strictest regulators
- [P712] **HECHO** — Cloud security concerns lessened by use of regional servers within national boundaries
- [P713] **HECHO** — Nations with fewer resources/regulations continue to be better implementers of innovation
- [P714] **HECHO** — In few years, most medical/nursing/allied health schools will have core curricula including digital health with relevance equal to anatomy/physiology
- [P715] **HECHO** — Most digital health innovations directed toward diagnostic/screening devices = miniaturization of vital signs monitoring into wearable devices
- [P716] **HECHO** — Latest activity trackers embed ECG, oxygen saturation, blood pressure monitoring; few are medical-grade or as accurate as conventional counterparts
- [P717] **HECHO** — To bypass FDA regulations, most digital health innovations marketed as wellness devices for larger direct-to-consumer market
- [P718] **HECHO** — Highest exponential growth/evolution in clinical care expected from genomics, ML, autonomous robotics
- [P719] **HECHO** — Future: people will be genomically predesigned/screened/selected before birth; extensive genomic assessment at birth will identify potential lifelong ailments
- [P720] **HECHO** — Continuous monitoring via implantable/wearable devices will autonomously implement interventions per ML algorithms throughout life
- [P721] **HECHO** — Clinical decision support systems, CV, computer-assisted diagnosis via deep neural networks will be prevalent in all societies including resource-limited ones
- [P722] **HECHO** — New medical specialties predicted: Genomic Planners, Genomic Curators, Genomic Editors, Tissue Engineers, Healthcare Designers, Brain Computer Interface Specialists
- [P723] **HECHO** — Flourishing professions predicted: Geneticists, AI Medical Informaticians

### 14.3 Delivery of Care in the Future of Digital Health
- [P724] **HECHO** — Surgery will always exist (trauma, obstetrics, some cancers); digital surgeons will prevail; first implementations = master-slave robotic platforms 20 years ago
- [P725] **HECHO** — ML algorithms will augment surgeons' cognitive/technical capabilities until fully autonomous surgical platforms take over
- [P726] **HECHO** — Future health system = continuum of care where notion of "patients" and "hospitals" does not exist per se; individuals replace patients
- [P727] **HECHO** — At birth, each baby's genome sequenced/analyzed → transferred to Personal Medical Record (PMR); PMR owned by individual
- [P728] **HECHO** — PMR stored in secured cloud; blockchain ensures data not altered
- [P729] **HECHO** — PMR linked to AI algorithms that learn person's lifestyle → identify deviation/abnormal behavior → automatically send worrisome data to health center
- [P730] **HECHO** — Health centers = centralized hubs for health tests/data analysis; rely on AI/robots; employ medical professionals for tasks machines cannot/should not do
- [P731] **HECHO** — Hospitals will still exist but limited to specific tasks (surgery, obstetrics)
- [P732] **HECHO** — Personalized digital interventions sent to reduce illness risk, sourced from PMR genetic data + wearable/mobile app data
- [P733] **HECHO** — Innovative insurance/revenue models will engage individuals/physicians in shaping better lifestyles/promoting wellness/disease prevention
- [P734] **HECHO** — Physicians who do not embrace DHT/AI may be replaced by those who do; transition will be generational and geographic
- [P735] **HECHO** — Digital native generations of patients/medical providers will lead DHT adoption; small visionary countries will lead at national level
- [P736] **HECHO** — UAE incorporated Ministers of AI, Happiness, Future into government cabinets → enables innovation at larger scale
- [P737] **HECHO** — Singapore/Kuwait may attempt to obtain genomic profiles of entire population
- [P738] **⚠ TENSIÓN** — Larger countries where most innovations created (e.g., US) will be implementation laggards due to regulation, litigation, risk-averse healthcare culture

### 14.4 Final Words
- [P739] **HECHO** — Digital health will soon become essential part of core model of healthcare; all DHT will intertwine/become invisible part of routine medical practice
- [P740] **HECHO** — AI and genomics may provide most value of all DHT; simple technologies (mobile phones, wearables, social media, telemedicine) will become omnipresent
- [P741] **HECHO** — Core model of medical practice will maintain quintessential relationship between care receivers/providers but will transform in time/space
