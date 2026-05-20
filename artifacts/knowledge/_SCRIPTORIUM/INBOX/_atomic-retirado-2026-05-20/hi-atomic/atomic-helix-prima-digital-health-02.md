---
_manifest:
  urn: urn:hi:kb:atomic-helix-prima-digital-health-02
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: 'artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/Digital Health: From Assumptions
      to Implementations.md — atomizacion HELIX PRIMA (Rivas/Boillat, Springer 2023);
      output de /atomize 2026-04-10'
version: 1.0.0
status: borrador
tags:
- atomic
- digital-health
- rivas-boillat
- springer-2023
- helix-prima
- hi
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 200
      producer: urn:kora:artefacto:atomize
      source_corpus: 'Rivas H, Boillat T (eds). Digital Health: From Assumptions to
        Implementations, 2nd Ed. Springer 2023. ISBN 978-3-031-17666-1'
      segmented: true
      segment_role: segment
      hand_edited: true
      segment_index: 2
      segment_count: 4
---

# HELIX PRIMA - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/Digital Health: From Assumptions to Implementations.md`
- Proposiciones: `200`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/04`
- Rango: `P201-P400`

## Indice de fuentes

- `S01` · [Digital Health: From Assumptions to Implementations.md](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 02 del corpus atomizado.

- **P201** · `fact` · Traditional CAD research began in 1960s → FDA approval for mammography CAD in 1998 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P202** · `fact` · By 2016, CAD applied to 92% of screening mammograms in US → `Gao et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P203** · `fact` · Traditional CAD disadvantages: high development cost, high false positives, increased unnecessary biopsies, limited to specific injuries · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P204** · `fact` · "Third wave of AI" using DL shows promising improvements over traditional CAD → `Fujita 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P205** · `fact` · ML community primarily uses Python; key DL libraries: Tensorflow (Google), Pytorch (Facebook), Scikit Learn · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P206** · `requirement` · CV algorithm deployment requires integration into API framework · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P207** · `requirement` · Software architecture must include connection to PACS to access medical images in automated/secure/protocolized way · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P208** · `fact` · Chest X-ray CV tool outputs must be available within minutes (emergency/hospitalized patient context) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P209** · `fact` · Mammography/MRI CV algorithms can process studies in scheduled batch on subsequent days · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P210** · `rule` · CV tool UI should be integrated into applications physicians use regularly (EHR, PHR, radiology information systems) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P211** · `fact` · Acceptance remains biggest barrier to AI adoption; lack of trust due to "black box" nature · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P212** · `fact` · Specialists fear being replaced by AI → concrete engagement actions needed (assertive communication, training, change management) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P213** · `fact` · AI not expected to replace experts in near future; specialists unwilling to adopt AI will be replaced by those who do · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P214** · `fact` · Introducing CV into healthcare requires software development, health informatics, UX analysis, interoperability, infrastructure, coaching, monitoring · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 4.6 Current State
- **P215** · `fact` · van Leeuwen et al. 2021 survey found 100 AI solutions with CE mark approved for clinical use in Europe (radiology) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P216** · `fact` · >65% of 100 CE-marked AI radiology products introduced to market between January 2018-April 2020 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P217** · `fact` · AI radiology product deployment/pricing strategies not yet converged to preferred standard · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P218** · `fact` · Subscription/license models more prevalent than pay-per-use (56/100 vs 28/100) for AI radiology products · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P219** · `fact` · Only 36/100 CE-marked AI radiology products had peer-reviewed evidence for efficacy · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P220** · `fact` · Similar AI products certified under different regulatory classes (e.g., class I self-certification vs class II external audit) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P221** · `fact` · Most AI radiology products perform single specific task; only stroke/oncology have "suites" covering whole diagnostic path · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P222** · `fact` · Radiology departments forced to interact with multiple AI vendors → overhead of sales, contracts, training, integration · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 4.7 Future Directions
- **P223** · `fact` · Future efforts focused on solving minority misrepresentation in datasets + unintended labeling errors from NLP mining of radiological reports · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P224** · `fact` · AI utility in medical imaging will increase as CV systems incorporate fusion of different data modalities · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P225** · `fact` · Increase in non-interpretative CV solutions expected: report worklist management, image correction, synthesis · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P226** · `fact` · CV adoption worldwide depends on prior digitization of health information systems, especially in less developed countries · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P227** · `fact` · Real importance lies not in creating AI products but ensuring people have access to them → `Myers 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch5 — Technology-driven Solutions in Mental Health and Physical Well-being (AlGurg, Nawaz, Albanna)

### 5.1 Introduction
- **P228** · `fact` · Global burden mental disorders estimated ~$16 trillion by 2030 → `Patel et al. 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P229** · `fact` · Digital health sector received >$57.2 billion invested worldwide by 2021 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 5.2 Challenges in Mental Healthcare
- **P230** · `fact` · COVID-19 significantly impacted mental well-being of children, adolescents, families · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P231** · `fact` · <50% adolescents with mental disorders receive treatment → `Costello et al. 2014` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P232** · `fact` · >50% youth with depression receive no intervention · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P233** · `fact` · USA requires training many more mental health professionals to meet demand · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P234** · `fact` · WHO identified lack of funding/services as key barrier to addressing mental health gap · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 5.3 Role of Digital Mental Healthcare
- **P235** · `fact` · Enhancing screening at Primary Health Centers with apps = feasible, may reduce time/increase accessibility → `Diez-Canseco et al. 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P236** · `fact` · Tate et al. used Swedish registry + ML to predict adolescent mental health; random forest AUC=0.739 (95% CI 0.708-0.769) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P237** · `fact` · Tate et al. SVM model AUC=0.735 (95% CI 0.707-0.764) for adolescent mental health prediction · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P238** · `constraint` · Tate et al. models not suitable for clinical use; serve as model for future studies · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P239** · `definition` · Autism Spectrum Disorder (ASD) = heterogeneous developmental disorder · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P240** · `fact` · Chen et al. used rs-fMRI from ABIDE dataset; matched ASD children (n=126) vs typically developing (n=126); reported high accuracy with ML · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P241** · `fact` · Kosmicki et al. used ML on ADOS data → ~98% accuracy classifying ASD with abbreviated behavior set · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P242** · `fact` · Shahamiri et al. mobile app + CNN trained on ASD database → higher accuracy/sensitivity/specificity than usual ASD screening · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P243** · `constraint` · AI for ASD screening = infancy stage; high psychometric properties but feasibility/real-world applicability challenges remain → `Song et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P244** · `fact` · Mobile technologies/apps have important role augmenting or providing stand-alone treatment for anxiety disorders → `Silk et al. 2011` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P245** · `fact` · Anxiety Coach = empirically supported app developed by Mayo Clinic for anxiety assessment/education · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P246** · `fact` · VR can simulate anxiety-provoking situations as treatment modality; biological data comparable to real-life → `Kothgassner et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P247** · `fact` · VR exposure shows lower refusal rate than in vivo exposure for mental health interventions → `Garcia-Palacios et al. 2007` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P248** · `fact` · COVID-19 pandemic led to rapid expansion of digital mental health services · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P249** · `fact` · Pandemic caused rapid increase in mental health services within weeks of onset → `Sharma et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P250** · `fact` · Individually tailored web-based CBT program demonstrated preliminary effectiveness reducing stress/anxiety during COVID-19 → `Aminoff et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 5.4 Physical Well-being
- **P251** · `fact` · Up to 50% cancer patients suffer from mental illness · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P252** · `fact` · Treating depression in cancer patients shown to improve survival time · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P253** · `fact` · Risk of heart attack >2x in patients with depression vs general population → `Rosenstein 2011` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P254** · `fact` · Depression increases risk of death in cardiac disease patients · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P255** · `fact` · New Zealand cohort study (>2M citizens, 3 decades): mental disorders associated with subsequent physical disease onset, accumulation of diagnoses, increased costs, early mortality → `Richmond-Rakerd et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P256** · `definition` · WHO: "Health = state of complete physical, mental, social well-being, not merely absence of disease or infirmity" · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P257** · `fact` · Mindfulness training associated with improved mental health in high-stress career populations · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P258** · `fact` · Growing evidence of endocrine function changes after meditation → improved mental health outcomes → `Pascoe et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P259** · `fact` · Poor sleep impacts psychiatric conditions; affects development/maintenance of mental health problems from poor cognition to depression/GAD → `Scott et al. 2017` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P260** · `fact` · Lack of sleep associated with heart disease and type 2 diabetes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P261** · `fact` · CDC: 1/3 US adults get less than recommended sleep per night · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P262** · `fact` · COVID-19 pandemic: 1 in 3 individuals reported sleep problems → `Alimoradi et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P263** · `fact` · Sleep deprivation strongly associated with immune system dysregulation → `Garbarino et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P264** · `fact` · Obesity linked to comorbid conditions: diabetes, cancer risk, heart disease, stroke, osteoarthritis, sleep apnea, liver/pulmonary disease · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P265** · `fact` · Among low-SES families, food insecurity co-occurred with maternal depression → `Melchior et al. 2009` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P266** · `fact` · Short sleep duration/poor sleep quality = risk factors for obesity → `Beccuti & Pannain 2011` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P267** · `fact` · Sleep deprivation increases food consumption without parallel increase in energy expenditure → `Grandner et al. 2014` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P268** · `fact` · Sleep deprivation creates preference for high-calorie foods with poor nutritional value → weight gain risk → `Greer et al. 2013` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P269** · `fact` · Lack of calcium, magnesium, vitamins A/C/D/E/K associated with sleep problems → `Ikonte et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P270** · `fact` · >350,000 digital health apps available on market as of 2021 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P271** · `fact` · Wearable tech enables accurate measurement of heart rate, exercise time, distance, estimated caloric expenditure · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P272** · `constraint` · Digital health impact on physical well-being hampered by non-technical barriers: lack of transparency, privacy concerns, digital literacy gap · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P273** · `fact` · Users reengaging with health app after break usually restart from beginning rather than continuing → `Azumio dataset` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P274** · `fact` · Long-term wearable tech users tend to be surrounded by fitness-oriented people, less active on social media showcasing activities · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P275** · `fact` · People using smart scales regularly tend to have greater weight loss · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P276** · `fact` · Sunrise system = coin-sized device attached to chin for ambulatory OSA diagnosis outside sleep center → `Pépin et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P277** · `fact` · Sunrise system identifies obstructive/mixed apneas, hypopneas, respiratory effort-related arousals by analyzing mandibular movement patterns · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 5.4.9 Chatbots
- **P278** · `definition` · Chatbot = "conversational agent" — program supporting/engaging humans via sound or text techniques · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P279** · `fact` · ESTORE chatbot utilizes text-messaging + voice assistant to provide mental health support to older adults → `El Kamali et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P280** · `fact` · "Rupert" food diary coaching chatbot encourages reduced meat consumption + increased fruit/vegetable intake · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P281** · `fact` · 82% Rupert app users reported it helped them think about/be aware of their consumption → `Casas et al. 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 5.5 Conclusion and Path Forward
- **P282** · `fact` · >350,000 digital health apps available; wearable tech enables accurate health monitoring · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P283** · `constraint` · Non-technical barriers (transparency, privacy, digital literacy) hamper digital health physical well-being impact · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch6 — Present Capabilities of AI in Surgical Oncology (Narayan)

### 6.1 Introduction
- **P284** · `definition` · AI = any platform simulating human thought/behavior including problem-solving, image/word recognition, pattern-based conclusions → `Hashimoto et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P285** · `definition` · ML = sub-category of AI; programs build own knowledgebase from increasing data → more precise conclusions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P286** · `fact` · Term "artificial intelligence" coined 1956 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P287** · `fact` · From PubMed inception (1996) to April 1 2022, >300 articles published using AI for surgical oncology clinical questions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 6.2 The Use of AI in Surgical Oncology
- **P288** · `definition` · Supervised ML = develops algorithm from training + testing dataset to predict output of interest · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P289** · `rule` · Supervised ML: larger proportion → training set, remainder → testing set (e.g., 90% vs 10%) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P290** · `definition` · Internal validation set = subjects from same dataset; external validation set = subjects from new dataset not used for training · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P291** · `definition` · Unsupervised ML = algorithms identifying patterns within dataset without labeled outputs · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P292** · `definition` · Reinforcement ML = algorithm iterates performance on pre-specified task as more data introduced; learns from successes/mistakes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P293** · `fact` · Laukhtina et al. used LASSO regression → nomogram predicting cancer-specific survival for metastatic renal cell carcinoma; 613 patients; c-index=0.644 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P294** · `definition` · Random forest = supervised ML creating decision tree with features → cumulative probability of outcome; performs classification and/or regression · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P295** · `fact` · Rahman et al. used random forest to predict 5-year survival among 2931 gastric adenocarcinoma patients; time-dependent AUC=0.80; c-index=0.76 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P296** · `definition` · K-clustering = supervised learning evaluating training data geometrically → categorizes testing data by Euclidean distance · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P297** · `fact` · Yin et al. 14,134 cancer patients across 5 Chinese institutions; k-clustering on 17 nutritional features; AUC=0.941 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P298** · `definition` · Support vector machines = supervised learning using classification/regression to cluster data relative to hyperplanes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P299** · `definition` · Neural networks / DL = ML techniques modeled after human nervous system: input layer + output layer + hidden layer(s) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P300** · `definition` · CNN = convolutional neural network with many arrays; RNN = recurrent neural network · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P301** · `fact` · Liu et al. used 16-layer CNN → nomogram predicting malignancy of solitary pulmonary nodule; AUC=0.916 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P302** · `definition` · CV = AI modality analyzing images/videos to identify patterns related to outcome · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P303** · `definition` · Radiomics = CV subset identifying texture features on images often imperceptible to human eyes → associations with outcomes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P304** · `fact` · Radiomics features quantified via RGB color extraction + statistical measures: mean, SD/variance, skewness, kurtosis, entropy, energy, contrast, homogeneity, correlation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P305** · `fact` · Creasy et al. (Memorial Sloan Kettering) used radiomics to predict volumetric response to neoadjuvant chemo in 157 colorectal liver metastasis patients; mean absolute prediction error=21.5% · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P306** · `definition` · NLP = AI technique seeking associations between syntax/semantics of words and outcomes of interest → `Nadkarni et al. 2011` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P307** · `fact` · Patel et al. (University of Chicago) used NLP on 10,196 average-risk colonoscopy reports → relationship between proximal serrated polyp detection rate and median withdrawal time · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P308** · `fact` · Yang et al. developed NLP platform identifying muscle-invasive bladder cancer from VA CPRS; accuracy=94% · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 6.3 Limitations on AI in Surgical Oncology Research
- **P309** · `constraint` · Few published AI models accessible open-source; lack of internal validation at new institutions limits generalizability · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P310** · `fact` · Northcutt et al. found average error rate 3.3% across 10 most commonly used CV datasets · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P311** · `fact` · One mammogram image dataset used for algorithm training had >15% mislabeled images → `Kay et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P312** · `constraint` · AI models require updates as standards of practice evolve; rapid change in systemic regimens necessitates frequent updates · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P313** · `definition` · Time drift = failure of established models to keep up with practice changes (e.g., ICD-9 → ICD-10) → `Ross 2022` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 6.4 Conclusion
- **P314** · `rule` · AI models function best as supplement to clinical decision-making, not replacement for diagnosis/prognosis · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P315** · `obligation` · Clinicians must be driving force for incorporating/supervising AI models in clinical practice · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch7 — ML for Decision Support Systems: Prediction of Clinical Deterioration (Shamout)

### 7.1 Introduction
- **P316** · `definition` · CDSS = Clinical Decision Support Systems informing decision-making of medical practitioners in patient care (since 1970s) → `Mould et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P317** · `definition` · Clinical deterioration = worsening of patient condition on hospital wards; defined by adverse events (unintended injury/complication → disability, death, prolonged stay) → `Jones et al. 2013` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P318** · `fact` · CDSS value recognized in improving patient safety/minimizing medical errors in early 2000s → `Donaldson et al. 2000` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P319** · `definition` · Knowledge-based CDSS = reason based on expert medical knowledge; use IF-THEN rule-based logic; knowledge base must be constantly maintained · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P320** · `definition` · Non-knowledge-based CDSS = use AI/ML/DL pattern recognition; require large datasets for model training; need retrospective + prospective validation before deployment · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P321** · `fact` · Delayed recognition of deterioration associated with human-related monitoring failures → `Van Galen et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P322** · `scope` · EWS systems predict whether adverse event likely within future N-hour window from assessment time (e.g., 24h) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 7.2 Classical Early Warning Score Systems
- **P323** · `definition` · Classical EWS = "track-and-trigger" systems assigning scores to physiological variables: heart rate, respiratory rate, temperature, blood pressure, oxygen saturation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P324** · `fact` · First physiological EWS system introduced 1997 by Morgan et al. · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P325** · `rule` · EWS aggregate score = sum of individual scores; alerts clinicians for deterioration signs preceding adverse events · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P326** · `rule` · NEWS2: heart rate ≥131 bpm → score=3; heart rate ≤30 → score=3 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P327** · `rule` · NEWS2: systolic BP ≤90 mmHg → score=3; systolic BP ≥220 mmHg → score=3 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P328** · `rule` · NEWS2: temperature ≤35.0°C → score=3; temperature ≥39.1°C → score=2 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P329** · `rule` · NEWS2: respiratory rate ≤8 breaths/min → score=3; respiratory rate ≥25 → score=3 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P330** · `rule` · NEWS2: O2 saturation Scale 1 ≤91% → score=3; ≥96% → score=0 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P331** · `rule` · NEWS2: O2 saturation Scale 2 (hypercapnic respiratory failure) ≤83% → score=3; ≥97% on oxygen → score=3 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P332** · `rule` · NEWS2: ACVPU score CVPU → score=3; Alert → score=0 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P333** · `rule` · NEWS2: supplementary oxygen Yes → score=2; No → score=0 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P334** · `fact` · ViEWS introduced 2010 by Prytherch et al.; served as template for NEWS (UK, 2012) and NEWS2 (2017) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P335** · `fact` · ViEWS authors explored adding +1 point for age ≥65 → no significant AUROC improvement · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P336** · `fact` · AEWS proposed 2019 by Shamout et al.; age-specific alerting ranges for composite outcome (mortality, cardiac arrest, unplanned ICU admission within 24h) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P337** · `fact` · AEWS showed performance benefits specifically in younger patients · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P338** · `constraint` · Classical EWS limitations: discard temporal info, single measurement set, no patient-specific info (sex, comorbidities), simple weighted-sum inference · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P339** · `constraint` · EWS normality ranges difficult to maintain/update especially when based on human judgment/heuristics · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P340** · `fact` · Two EWS systems evaluated in Malawi cohort → both showed performance drop; disease/population differences significantly influence EWS performance → `Wheeler et al. 2013` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 7.3 Modern Computational Approaches for Early Warning
- **P341** · `fact` · First laboratory-based EWS (2005): binary logistic regression + 7 lab tests → predict in-hospital mortality → `Prytherch et al. 2005` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P342** · `fact` · LDTEWS (2013) = decision tree analysis for females/males separately; tabularized for pen-and-paper use → `Jarvis et al.` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P343** · `fact` · LDTEWS:NEWS (2018) = weighted sum of LDTEWS (lab) + NEWS (vitals) with linear decay weight; excluded if >5 days prior → `Redfern et al.` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P344** · `fact` · LDTEWS:NEWS performed better than NEWS alone · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P345** · `definition` · DEWS = Deep interpretable Early Warning System; attention-based recurrent deep neural network for clinical deterioration prediction → `Shamout et al. 2019c` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P346** · `fact` · DEWS predicts composite outcome: in-hospital mortality / cardiac arrest / unplanned ICU admission within 24h · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P347** · `fact` · DEWS uses Gaussian process regression to sample posterior mean/variance at regular intervals from sparse vital-sign sequences · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P348** · `fact` · DEWS attention layer assigns importance score (0-1) to each timestep → interpretability · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P349** · `fact` · DEWS outperforms baselines in discriminative ability + decreases trigger rate at fixed sensitivity · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P350** · `fact` · Shamout et al. COVID-19 prognostic system: CNN processes chest X-rays + gradient boosting on clinical data → fused via weighted averaging; multi-task predicting deterioration within 24/48/72/96h; developed at NYU Langone Health · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P351** · `fact` · COVID-19 prognostic system predicts composite outcome: mortality / intubation / ICU admission in emergency department · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P352** · `fact` · All classical EWS systems (NEWS, AEWS, LDTEWS, LDTEWS:NEWS) significantly underperformed in COVID-19 cohort → `Youssef et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P353** · `constraint` · ML/DL models require large amounts of labeled data; data may be noisy; collection not viable in low-resource settings without digitized EHR · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P354** · `constraint` · ML models prone to dataset bias → biased models in practice; model fairness = growing research area · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P355** · `constraint` · ML-based EWS output overall risk score only; lack clinical response plan compared to classical EWS · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 7.4 Future Outlook
- **P356** · `fact` · Systematic review (Alam et al. 2014): 7 studies on EWS clinical impact; only 2 showed significant mortality reduction · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P357** · `fact` · EWS deployment led to increased collection of vital-sign measurements in 2/7 studies · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P358** · `fact` · Scoping review (Muralitharan et al. 2021): 24 ML-based EWS studies; 23 retrospective, only 1 prospective · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P359** · `fact` · Single prospective ML-EWS study: random forest classifier, 178 patients → significant improvement detecting early deterioration signs → `Olsen et al. 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P360** · `obligation` · Need more prospective validation studies to leverage positive clinical impact of EWS systems · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P361** · `scope` · Next-generation EWS should process diverse modalities: imaging, wearables data, genomic data, family history — not just vital signs · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P362** · `constraint` · Most deterioration prediction algorithms developed in silo for particular cohort/outcome → narrow AI; need standardization toward general CDSS · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 7.5 Conclusion
- **P363** · `fact` · CDSS value for patient safety recognized since early 2000s; modern ML approaches show promise but need prospective validation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch8 — Mixed and Augmented Reality in Healthcare (Wrzesinska)

### 8.1 Introduction
- **P364** · `definition` · MR = Mixed Reality; physical + digital objects interact in real time; mix of AR + VR in 2D or 3D · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P365** · `fact` · Paul Milgram (1994) described MR as scale of reality — virtual continuum covering every state between real and virtual worlds · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P366** · `fact` · MR already used in education, military training, remote working, architecture, interior design, product content management · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P367** · `fact` · Global MR market CAGR predicted 47.9% during 2020-2025 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P368** · `fact` · Medical holography market projected: USD 500M (2021) → >USD 2B (2026) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.2 Possible Use of Mixed Reality in Medicine
- **P369** · `definition` · Smart glasses = web-connected wearable computing devices allowing transmission/projection of data in field of vision · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P370** · `fact` · Google Glass = one of first smart glass models used in medicine; wireless, short learning curve, runs Android · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P371** · `fact` · Muensterer (pediatric surgeon) wore Google Glass 4 consecutive weeks at LMU Munich Children's Hospital → `Muensterer et al. 2014` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P372** · `fact` · Jeroudi et al. compared ECG interpretation accuracy via Google Glass vs paper; users not satisfied with images vs paper version · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P373** · `fact` · Yale team used Google Glass for teleconferencing in emergency medicine triage during mass accidents → `Cicero et al. 2015` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P374** · `fact` · Microsoft HoloLens = most commonly used MR platform; projects holographic 3D images; runs Windows OS; weight=566g · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P375** · `fact` · Imperial College London pilot: HoloLens2 during COVID-19 rounds; total exposure reduction=222.98 h/week; ~3100 fewer PPE items/week → `Martin et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P376** · `fact` · Imperial College London study: 75% staff said HoloLens easy to navigate; >70% comfortable to wear; rounds less time-consuming · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P377** · `fact` · Levy et al. (London) COVID-19 study: no patient claimed MR headset disturbed medical care or interaction with staff · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P378** · `fact` · MR 3D holograms helpful to evaluate pulmonary lesions in COVID-19 patients, especially by less experienced doctors · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.3 AR and MR in Surgery
- **P379** · `fact` · Smart glasses react to voice commands, eye movements, gestures → hands-free = especially helpful in surgery/sterile field · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P380** · `fact` · Wu et al. used Google Glass for ultrasound-guided central venous access → fewer additional head movements · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P381** · `fact` · MR holographic images = cheaper + faster than 3D printing for surgical planning; surgeon interacts in real time while remaining sterile · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P382** · `fact` · MR surgical holograms work with DICOM standard imaging: CT, MRI, angiography, 3D ultrasonography · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P383** · `fact` · HoloLens applied in orthopedic, plastic, neuro, oncological surgery and more · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P384** · `fact` · Brun et al.: first preoperative planning with MR for congenital heart disease; rated highly by all users · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P385** · `fact` · MR in liver anatomy: decreases time to correctly identify lesions; increases accuracy for some localizations → `Pelanis 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P386** · `fact` · Wierzbicki et al. (Cracow): HoloLens 2 used for irreversible electroporation / microwave ablation of unresectable pancreatic/liver tumors · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P387** · `fact` · 3D MR reconstructions most advantageous for trainees / less-experienced doctors · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P388** · `fact` · Augmedics Xvision Spine system = wireless AR surgical navigation for pedicle screw insertion; visualizes spine anatomy through skin/tissue → `Molina et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P389** · `fact` · Gregory et al. shared reverse shoulder arthroplasty procedure video via HoloLens in real time with 4 specialists · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P390** · `fact` · Boilat & Rivas developed Digital Checklist Box (DCB): AR-projected WHO surgical safety checklist onto draped patient · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.4 MR in Endovascular Procedures
- **P391** · `constraint` · Major challenge of endovascular procedures = working with 2D images of 3D anatomy; multiple angiographic images → radiation/contrast exposure concerns · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P392** · `fact` · Opolski et al.: 15 percutaneous coronary interventions for chronic total occlusions with MR assist → lower contrast exposure · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P393** · `fact` · Wrzesinska used HoloLens during EVAR; Carna Life Holo app; one of first holographic visualization implementations during EVAR worldwide · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P394** · `fact` · EVAR involves radiation + iodine contrast agent (can cause acute kidney injury); fenestrated/branched stent-grafts = even more radiation/contrast/time · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P395** · `fact` · Garcia-Vazquez et al. proposed MR guidance system for EVAR with HoloLens + electromagnetic tracking using aortic aneurysm phantom · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P396** · `fact` · RealView Imaging (Israel) = first medical holographic system projecting 3D holograms in air without glasses; FDA cleared for clinical use · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P397** · `fact` · Bruckheimer feasibility study: RealView system during cardiac catheterization; 8 patients; all landmarks identified, no adverse events · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.5 MR in Education
- **P398** · `fact` · Case Western Reserve University: medical students study anatomy via MR + HoloLens; compared to cadaver classes → no statistical difference in exam scores → `Stojanovska et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P399** · `fact` · Prospective anatomy study: MR learning platform shortened study time vs cadaveric dissection; no difference in exam scores → `Ruthberg et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P400** · `fact` · Kumar et al. used HoloLens + virtual face models for plastic surgery training → `Kumar et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
