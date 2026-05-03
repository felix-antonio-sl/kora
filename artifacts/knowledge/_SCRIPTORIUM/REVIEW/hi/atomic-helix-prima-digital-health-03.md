---
_manifest:
  urn: urn:hi:kb:atomic-helix-prima-digital-health-03
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
      segment_index: 3
      segment_count: 4
---

# HELIX PRIMA - Segmento 03

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/Digital Health: From Assumptions to Implementations.md`
- Proposiciones: `200`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `03/04`
- Rango: `P401-P600`

## Indice de fuentes

- `S01` · [Digital Health: From Assumptions to Implementations.md](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 03 del corpus atomizado.

- **P401** · `fact` · Telementoring via AR/MR allows trainees to perform procedures monitored remotely by supervisor regardless of distance → `Mitsuno et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P402** · `fact` · MR simulation-based training confirmed safe/effective; reduces complication rate; results similar to traditional training at lower cost → `Barsom et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.6 Patients Also Can Use MR
- **P403** · `scope` · Patient MR applications include: pain management, rehabilitation, pharmacological treatment planning, chronic disease management, telemedicine, patient education · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 8.7 Challenges
- **P404** · `constraint` · Most AR/MR devices not certified as medical devices; medical applications often require certification; legislation process slow · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P405** · `constraint` · Data protection issues = main inhibitory factor for MR implementation in clinical use · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P406** · `fact` · North American region holds largest market share in medical holography · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P407** · `constraint` · Google Glass battery life = 40 min; Microsoft HoloLens battery = up to 5.5h (~3h active use); poor battery life = barrier · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P408** · `constraint` · Technical limitations of MR/VR: brightness, panel resolution, vergence-accommodation conflict → `Zhan et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P409** · `fact` · HoloLens: user controls information amount for tolerable cognitive load; image quality/stability do not cause motion sickness · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P410** · `constraint` · MR cost = significant gap between research and clinical implementation; MR/AR applications cost less than 3D printing · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P411** · `fact` · Younger generation practitioners more willing to try new technologies than older doctors; risk-averse medical mindset inhibits MR adoption · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P412** · `scope` · MR smart glasses healthcare applications: reading/interacting with data, communication/teleconsultation, video recording/streaming, workflow/documentation, patient empowerment, education, safety/efficiency · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch9 — Why Healthcare Needs Blockchain (Southey, Zarrebini)

### 9.1 The Promise of Blockchain for Healthcare
- **P413** · `definition` · Blockchain = shared read-write database where value objects exchanged/recorded between ≥2 parties without trusted intermediary · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P414** · `definition` · Blockchain network embeds agreed rules of interaction; protocol acts as governance structure underpinning value exchanges · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P415** · `fact` · Blockchain enables disparate non-trusting entities to trade value objects peer-to-peer by trusting underlying code instead of central authority · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P416** · `rule` · Changes to blockchain governance rules generally require majority vote to amend protocol · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P417** · `definition` · Digital assets on blockchain housed permanently at specific address; private key proves ownership required for transfer · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P418** · `definition` · Blockchain state = snapshot of mini-economy showing current ownership; each new state cryptographically linked to previous state · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P419** · `rule` · Confirmation of new blockchain state achievable only through network consensus · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P420** · `definition` · Blockchain Trilemma (Vitalik Buterin) = trade-off between decentralisation, security, scalability · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P421** · `fact` · Private permissioned blockchains prioritise scalability but limit decentralisation/security; use semi-trusted consortium consensus without crypto-economic incentives · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P422** · `fact` · Permissionless blockchains have larger networks with unknown/untrusted entities; use consensus mechanisms issuing cryptocurrencies as rewards · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P423** · `fact` · Bitcoin mining: cost of computing to control ledger far exceeds reward for honest behavior → miners incentivised to validate only valid transactions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P424** · `fact` · Private permissioned blockchain can achieve acceptable ledger integrity without crypto-incentivisation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P425** · `fact` · Blockchain recipients can self-verify author/content of transferred data, confirmed unaltered by network consensus · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P426** · `fact` · Large data volumes inefficient to store on-chain; digital hash recorded as transaction provides shared unalterable audit log · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P427** · `fact` · Single patient generates ~80 MB data/year in imaging + EMR (2017 estimates) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P428** · `fact` · RBC Capital Markets projects healthcare data compound annual growth rate reaches 36% by 2025 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P429** · `fact` · ~30% of world's data volume generated by healthcare industry · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P430** · `fact` · IT investment in healthcare among lowest of all industries (IDC/Seagate report) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P431** · `fact` · EY (2019) estimated UK NHS data value = GBP 9.6 billion/year · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P432** · `fact` · Global Big Data in healthcare estimated to reach $78.03 billion by 2027 → `Emergen Research` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P433** · `fact` · Healthcare systems inherently complex with myriad stakeholders whose interests not always aligned · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P434** · `fact` · Healthcare increasingly adopting patient-centric approach, changing power dynamic in ecosystem · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P435** · `fact` · Healthcare generally lags other industries in technology adoption · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P436** · `tension` · Healthcare industry centralising data in hands of multinationals despite increasing appetite for patient self-sovereignty/patient-owned data · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P437** · `fact` · Primary currency fuelling healthcare care delivery success/failure = data · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P438** · `fact` · ~500,000 deaths worldwide attributable to drug use; >70% related to opioids; >30% of those caused by overdose → `WHO` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P439** · `fact` · U.S. payers spend >$2 billion/year maintaining provider databases; most credentialing processes take >120 days → `PwC/NAMSS` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P440** · `fact` · Estimated loss of $200 million globally through counterfeit medications · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P441** · `fact` · Penn Medicine study: ~70% of CBD extracts sold online are mislabelled · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P442** · `fact` · JAMA study: 40% of CBD products online have drug concentration different from label; 26% had higher concentration; some contained THC sufficient to fail drug test · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P443** · `fact` · BIS Research: blockchain integration in healthcare could save >$100 billion/year by 2025 in IT, operations, support, personnel, data breach costs · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P444** · `fact` · Blockchain can provide significant benefits in clinical trial recruitment + enhance data provenance/security → `Zhuang et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P445** · `scope` · Blockchains not ideal for high-volume data storage; usefulness for EHR sharing lies in storing access records, not records themselves · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P446** · `fact` · Blockchain server can verify data integrity + log access for later audit · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P447** · `definition` · WEF (2021) framework for data economy: core principles = managing functional architecture of data exchange, governance, incentivisation of data sharing · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P448** · `fact` · Value derived from acquiring/combining data, low-latency access to high-quality data, extracting meaningful insights · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P449** · `fact` · Data economy incentives include policy/regulatory frameworks + monetary/non-monetary incentives (reciprocity, innovation opportunity, data credits) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P450** · `fact` · Big Data validated >200 novel biomarkers predicting cardiovascular risk · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P451** · `fact` · Big Data investigated variation of 174,000 observed national prescribing patterns vs national guidelines for COPD · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P452** · `fact` · Big Data compared ~8,000 treatment outcomes for leukaemia by age, uncovering major unmet treatment need · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P453** · `fact` · >700 million records mined to develop new cancer risk-stratification algorithms · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P454** · `fact` · Healthcare data types: clinical, financial, operational, regulatory; owners/users include patients, providers, insurers, tech companies, manufacturers, payors, regulators · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P455** · `fact` · Patient recruitment for clinical trials known to be challenging; most trials not meeting recruitment requirements on time · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 9.2 Current Landscape of Blockchain in Healthcare
- **P456** · `fact` · Research identified 75 companies claiming blockchain as part of healthcare solution · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P457** · `fact` · 75% of blockchain healthcare companies established in 2016/2017, correlating with ICO craze · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P458** · `fact` · ~2/3 of identified blockchain healthcare companies still active; ~1/3 inactive · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P459** · `fact` · Apparent drop-off in blockchain healthcare funding after 2017 likely due to ICO reputation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P460** · `fact` · SEC deemed many blockchain "utility tokens" to be securities · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P461** · `fact` · CoinMarketCap review (Fang 2021) identified 10 commercially successful blockchain healthcare projects; majority in personal health tracking · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P462** · `rule` · Understanding tokenomic models critical to long-term success of blockchain healthcare projects · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P463** · `fact` · Table 9.2 lists 49 active blockchain healthcare companies across EHR, supply chain, credentialing, clinical trials, security, genomics, payments domains → `Catena.MBA 2022` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 9.3 Future Vision for Healthcare Blockchains
- **P464** · `fact` · EU Blockchain Observatory Forum survey: highest-value use cases = data transparency (91.1%), pharma supply chains (88.2%), data immutability (85.3%) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P465** · `fact` · EU survey continued: medical records sharing (79.4%), secure payment transactions (76.5%), record accuracy (73.5%), data interoperability (70.6%) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P466** · `fact` · Healthcare professional knowledge requirements rising exponentially; increased need for multidisciplinary cross-collaboration · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P467** · `fact` · Healthcare complexity renders systems more prone to errors → `Braithwaite et al. 2017` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P468** · `fact` · Patient trust in virtual care services reduced compared to traditional environments → `Hasselgren et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P469** · `fact` · Current health technologies struggle with interoperability; perceived usability remains challenge → `Son et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P470** · `constraint` · GDPR creates concerns for immutable ledgers in healthcare; GDPR-compliant blockchain solutions exist · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P471** · `fact` · "Garbage in, garbage out" applies to health data on blockchain; inaccuracies carried forward → `Wong et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P472** · `obligation` · Allen et al. (2020) recommend developing scenario-based ethical dilemmas across blockchain healthcare uses · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P473** · `fact` · Federated Learning may enable privacy-preserving dataset sharing → `Li et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P474** · `fact` · Technology change = 75% cultural + 25% technical · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P475** · `fact` · 30% of world's data currently locked in silos preventing treatment innovations/better health outcomes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P476** · `fact` · Blockchain represents coopetitive model relying on stakeholders seeing greater benefit in sharing common infrastructure · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P477** · `fact` · Blockchain = governance technology; building rules of engagement equally important as technology choices · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P478** · `fact` · Blockchain Research Institute (Canada) template: principles = Think "We" vs "I", evangelise new perspective, identify Minimally Viable Ecosystem/Network · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch10 — Nudging to Change, the Role of Digital Health (Purohit et al.)

### 10.1 Introduction
- **P479** · `fact` · Most diseases preventable by assisting people to change habitual risky behaviors → `Kelly 2000` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P480** · `fact` · Risky health behaviors negatively associated with health: sedentary lifestyle, smoking, unhealthy eating, binge drinking · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P481** · `fact` · Millions of premature deaths preventable if individuals stop smoking; smoking causes lung cancer + increases pulmonary/cardiovascular disease risk · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 10.2 Background
- **P482** · `definition` · Nudge = any aspect of choice architecture that changes behavior predictably without prohibiting options or significantly changing incentives → `Sunstein/Thaler 2008` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P483** · `definition` · Digital nudge = nudge provided through digital technology employing UI design elements to influence decisions/behaviors without restricting choice → `Weinmann et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P484** · `fact` · Mobile phones compelling behavior change support systems due to: (1) gathering contextual/biometric data, (2) 24/7 reachability, (3) push notification capability · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P485** · `definition` · Teachable moments = naturally occurring health events thought to motivate individuals to adopt risk-reducing behaviors spontaneously → `Purohit/Holzer 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P486** · `fact` · Most digital nudge studies do not address timing explicitly despite "just-in-time" technology potential · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P487** · `fact` · Ford et al. (2010): real-time feedback during meals helped obese adolescents eat more slowly → weight loss · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P488** · `fact` · Intille et al. (2003): dietary behavior change information provided on PDA at time of purchase to motivate incremental change · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P489** · `fact` · Digital nudges delivered via mobile can be more fine-tuned than traditional nudges to fit optimal timing through adequate identification of user context · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 10.3 Digital Nudging Strategies
- **P490** · `definition` · Default nudge = predefined option chosen by system designer exploiting status quo bias · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P491** · `fact` · Organ donor list increased 60% in countries where organ donation is default opt-out vs national average 38% in opt-in countries → `Thaler et al. 2014` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P492** · `fact` · Default permanent flu vaccine appointments increased vaccination possibility → `Lehmann et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P493** · `fact` · Defaults produce large effects because individuals lack explicit preferences for every possible good/service · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P494** · `definition` · Reminder nudge = brings choice to user's attention via visual/sound/haptic cue (e.g., push notification) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P495** · `definition` · Feedback nudge = informs users about task performance to raise awareness/rectify misconceptions about problematic behavior · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P496** · `fact` · Feedback nudge can be tailored/personalized to individual to solve heterogeneity problem · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P497** · `definition` · Social nudge = informs individuals about what others are doing; establishes social norms users motivated to follow (peer comparison) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P498** · `definition` · Framing nudge = deliberate phrasing of information presentation to encourage target behavior; people respond differently to loss vs gain framing → `Tversky/Kahneman 1985` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P499** · `definition` · Suggesting alternatives nudge = providing individuals about to make decision with alternatives they might not have considered · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P500** · `definition` · Positioning nudge = changing visual presentation of options exploiting status-quo bias; more salient options chosen more often · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P501** · `fact` · Repositioning food choices to make nutritious food more prominent increased sales in physical settings → `Ensaff et al. 2015` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P502** · `fact` · Wyse et al. positioned nutritious food at top of online food ordering platform → increased selection of nutritious food · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 10.4 Digital Nudges in the Continuum of Care
- **P503** · `definition` · Continuum of care = provision of healthcare over time through 5 phases: prevention, pre-acute, acute, post-acute, chronic home-care · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P504** · `fact` · Milkman et al. used text-based framing nudges → increased influenza vaccination rate by 5% when reminded twice + informed appointment already booked · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P505** · `fact` · Xu et al. employed feedback nudges to improve dietary behavior/physical activity for patients at high risk for type 2 diabetes · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P506** · `fact` · Boillat et al. proposed smart glasses for surgical time-out checklist → 100% completion rate + 18% decrease in average checklist duration · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P507** · `fact` · Gamification elements (competition, awards, timely feedback) = digital nudges integrated into game mechanics; used for motor training in stroke patients · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P508** · `fact` · Immersive VR therapy based on gamification can benefit balance problems in chronic ischemic stroke → `Cortes-Perez et al. 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P509** · `fact` · Perez-Marcos et al. (2017): gamification-based games for functional training of upper limb after brain damage · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P510** · `fact` · Elderly heart attack patients significantly motivated to increase physical activity with loss-framed incentives + personalized goals using wearable device → `Chokshi et al. 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P511** · `fact` · Horne et al. (2022): 12-month RCT showed AI-formulated digital nudges via email/SMS/voice calls → nudge group adhered to medicine significantly more than control group · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P512** · `rule` · Thaler's ethical nudge guidelines: nudges should be (1) transparent, (2) easy to opt-out, (3) designed for user wellbeing → `Thaler 2018` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P513** · `fact` · Transparency has two aspects: goal of nudge should not be deceitful + mechanism must be transparent including data usage/privacy · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P514** · `fact` · Individuals being nudged often unaware of nudge or psychological mechanisms employed by choice architect · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 10.5 Landscape of Digital Nudging in Digital Health
- **P515** · `fact` · JMIR scoping review searched for "nudging"/"nudges"/"nudge"/"digital nudges"; yielded 150 articles; 19 included · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P516** · `fact` · Among 19 included studies, 30 nudges used; 7 studies employed ≥2 nudging techniques · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P517** · `fact` · Most common digital nudges in review = feedback + reminders; applied in prevention + post-acute care · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P518** · `fact` · No studies in review investigated default nudges · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P519** · `fact` · No studies in review investigated nudges for acute care phase · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P520** · `fact` · Digital nudging studies in digital health increased >160% since 2018 · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P521** · `fact` · Most reviewed papers focus on increasing desired behavior; nudges not used to solely reduce unwanted behavior · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P522** · `fact` · Only 1/19 reviewed studies explicitly discussed ethical considerations while designing intervention → `Neto et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P523** · `fact` · Feedback/reminder nudges inherently transparent in objective; framing/default/social comparison nudges inherently not transparent · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P524** · `constraint` · Scoping review limited to JMIR database + mainly focused on digital nudging for patients, not clinicians · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P525** · `fact` · Challenges in nudging away from undesired behavior: identification of behavior + providing adequate feedback on negative behavior · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P526** · `fact` · Rise of feedback nudges driven by wide adoption of smart devices enabling tracking of motion, steps, heart rate · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P527** · `fact` · Opting out challenging for default/framing/positioning nudges compared to feedback nudges · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P528** · `fact` · Unintended nudges (positioning/defaults) unavoidable in system design; challenge = ensuring design decisions aligned with patient welfare, not dark patterns · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 10.6 Conclusion
- **P529** · `fact` · Current research mainly focuses on feedback/reminder nudges for prevention + post-acute care; several effective strategies (defaults) absent from literature · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P530** · `obligation` · Development/promotion of ethical analysis grid crucial to guide practitioners/researchers in designing effective + ethical nudges for digital health · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch11 — The Role of Design in Healthcare Innovation and Future Digital Health (Montana-Hoyos et al.)

### 11.1 Introduction
- **P531** · `fact` · WHO (2014) estimated worldwide shortage ~4.3 million health workers · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P532** · `fact` · Post-COVID-19 pandemic health worker shortage now estimated at 18 million → `WHO 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P533** · `fact` · Digital health = cultural transformation where disruptive technologies provide digital/objective data → equal doctor-patient relationship with shared decision-making → `Mesko et al. 2017` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P534** · `fact` · Development/acceptance/performance of digital health interventions largely dependent on good design · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.2 Towards a Definition of Design
- **P535** · `definition` · Design = both action (creative thinking/problem-solving process) and result (outcome of that process) · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P536** · `definition` · Affordance = property where physical characteristics of object/environment influence its function → `Butler et al. 2003` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P537** · `definition` · Co-design (= generative design/co-creation/participatory design) = process of exploratory research + developmental design to define/address problem together with end user · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P538** · `definition` · Design Thinking = iterative process: empathise → define needs → ideate → prototype → test; unlike co-design, not dependent on creating solution with end user · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P539** · `fact` · Design has syntactic (how made), pragmatic (how used), semantic (how perceived/communicated) functions → `Boucharenc 2008; Bonollo 2010` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.3 The Role of Design in Healthcare Innovation
- **P540** · `fact` · Traditional healthcare = "doctor hero" scenario; patients not involved in decision making about own health/disease management · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P541** · `fact` · Design has direct effect on how patients/caregivers feel; intentional design → patients feel more at ease/calm/secure → `Solis 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P542** · `fact` · Designers navigate healthcare system as relative outsiders to understand parameters/conditions for solution development → `Park 2020` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P543** · `fact` · People involved in change from start more likely to feel ownership → less likely to oppose agreed solution → `Design Commission 2013` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.4 Design in Healthcare Innovation and Digital Health
- **P544** · `definition` · Health (WHO 2022) = state of complete physical, social, mental well-being, not merely absence of disease/infirmity · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P545** · `fact` · Lack of user engagement in proposed digital health solutions = area where design role in healthcare innovation became necessary · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P546** · `fact` · Matthews (2015): Design in healthcare improves safety, dignity, efficiency, sustainability · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P547** · `fact` · COVID-19 pandemic (2020) caused global collapse of healthcare services delivery, revealing need for drastic innovation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P548** · `fact` · Complexity of healthcare challenges demands profound system innovation; design plays critical role in engaging multidisciplinary teams → `Patricio et al. 2019` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.5 Design and Hospitals of the Future
- **P549** · `fact` · Growing number of inpatient services being pushed to home/outpatient ambulatory facilities; complex/very ill patients continue needing acute inpatient services → `Deloitte 2017` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P550** · `fact` · Hospitals experimenting with: customized patient rooms (digital screens), automation/robotics, digital patient experience (AI/ML), centralized clinical command centers · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P551** · `definition` · Scenarios = projection of concrete narrative description of user activity during specific task, sufficiently detailed for design implications → `Carroll 1997` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P552** · `fact` · Chamorro-Koc et al. (2012): scenarios employed to understand everyday practices + reveal stakeholder relationships in service provision · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.6 Design Narratives and Design Fiction
- **P553** · `definition` · Design fiction = deliberate use of diegetic prototypes to suspend disbelief about change; term coined 2005 by Bruce Sterling · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P554** · `fact` · Design fiction established field of design research for creating/imagining/visualizing possible futures → `Grand/Wiedmer 2010` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P555** · `fact` · Design fiction enables co-creation processes exploring applications + implications of interactions with future/emerging technologies · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.7 Future Healthcare Innovation and Digital Health Design Projects
- **P556** · `fact` · Buckminster Fuller (1982): "You never change things by fighting existing reality. To change something, build new model that makes existing model obsolete" · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P557** · `fact` · 2013 futuristic ICU project: user-centred design at Calvary John James Hospital + Canberra Hospital proposed fully integrated ICU bedspace using witricity + holograms → `Montana-Hoyos et al. 2016` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P558** · `definition` · Witricity = wireless power transfer developed by MIT researchers → `Gozalvez 2007` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P559** · `fact` · Witricity in ICU could eliminate "spaghetti syndrome" (multiple chords/tubes/cables) common in hospitals · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P560** · `fact` · HealthPod (2016): digital health intervention co-designed with patients/students/medical staff for GP clinic data collection improvement · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P561** · `fact` · GP clinic datasets often incomplete (missing demographics, height, weight, behavioral risk factors) → `Volker et al. 2014` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P562** · `fact` · HealthPod = patient kiosk with custom-built program feeding into clinic database + graphical UI; generated physical report card · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P563** · `fact` · Design fiction projects (2018+): students analysed emerging technologies to create 2050 life scenarios including 4D printing, bio-printing, emotion sensing AI, electronic tattoos · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P564** · `fact` · E-tattoos = new generation thin adhesive surfaces behaving like skin with embedded electronics; potential future wearables · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P565** · `fact` · Pediatric pain currently assessed by 1-10 scale or happy-to-sad faces; tiredness/emotions may influence nurse/clinician accuracy · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P566** · `fact` · TAME = Pediatric Pain Metric device using sensors (temperature, tremors, heart rate) + screen for simple visualization of pain/anxiety level → `Chamorro-Koc et al. 2021` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P567** · `fact` · COVID restrictions prevented hospital observations; design thinking enabled alternative remote data collection via photo ethnography + retrospective interviews · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P568** · `fact` · VR used as diversional therapy for pain management; Desselle et al. (2020) designed VR for anxiety/pain management of burns patients · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P569** · `fact` · TAME demonstrated scenario where technology affordances applied to humanise empathy building, not centred on technology functionality alone · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P570** · `fact` · Hospitals of Future envisioned as smart environments: error-free, effective, patient-centered → `Pickering et al. 2012` · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P571** · `fact` · Technology innovation in healthcare lags implementation mainly due to sector being highly regulated · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P572** · `fact` · COVID pandemic accelerated move to digital/virtual meetings; aging population migrated to telehealth/phone/videoconference consultations · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 11.8 Conclusions
- **P573** · `fact` · Blockchain/cryptocurrencies/Metaverse opening possibilities for completely digital immersive world including NFTs, DAOs · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P574** · `fact` · Potential digital health benefits: democratization/wider coverage of basic health services, "hospital at home" opportunities, focus on preventive healthcare · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P575** · `tension` · Potential digital health risks: exclusion due to "digital divide" especially aging population, remote areas, people purposely isolated from digital world · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P576** · `fact` · Design = conscious intention to modify environment to benefit human progress + increase social good · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P577** · `fact` · Design works with ambiguity + transdisciplinary teams; enables exploration of person-centred future digital health solutions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P578** · `fact` · Design contributes to quality improvement in healthcare by catalysing innovation; co-creation with stakeholders/policymakers addresses gaps between technology innovation + regulatory reform · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P579** · `fact` · Design champions humanisation of technology through person-centred approach ensuring future technologies conceptualised with end-users · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

## Ch12 — Medical Schools and Digital Health (Boillat, Otaki, Kellett)

### 12.1 Introduction
- **P580** · `definition` · Digital therapeutics (DTx) = delivery of evidence-based therapeutic interventions via qualified software programs to prevent/manage/treat medical conditions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P581** · `fact` · DTx received FDA approval; some health insurance companies prescribe/reimburse them · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P582** · `fact` · VR successfully used in clinical settings to fight phobias, stress, anxiety, eating disorders · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P583** · `fact` · VR used to reduce chronic/acute pain among adults and children · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P584** · `fact` · Activity trackers detected Atrial Fibrillation in clinical trials involving ~500,000 participants · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P585** · `fact` · DHT run on devices not designed exclusively for healthcare → complicates safe leveraging by professionals · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P586** · `fact` · Patients use DHT to collect physical activity, sleep patterns, heart rate variability data that physicians cannot leverage due to lack of training · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P587** · `fact` · Scoping review found most DHT studies in medical schools focused on medical informatics/EHR; only 9% covered telehealth, 3% covered mHealth · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P588** · `fact` · >50% medical students perceive their DHT competences as poor/very poor · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 12.2 Background: Some Data
- **P589** · `fact` · Systematic analysis of 60 curricula (top 10 medical schools per continent, Times Higher Education) found only 4 schools teaching digital health elements · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P590** · `fact` · Stanford University most active with 3 DHT offerings through Byers Center for Biodesign · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P591** · `fact` · Stanford Biodesign for Digital Health = quarter-long course requiring multidisciplinary teams (medicine + bioengineering) to identify needs/prototype DHT solutions · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P592** · `fact` · Stanford Biodesign Innovation = 2-quarter course; medicine/bioengineering/mechanical engineering/IT students identify unmet health needs · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P593** · `fact` · Stanford Biodesign programs are elective, carry 3-4 credits, use problem-based approach · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P594** · `fact` · Johns Hopkins offers DHT extra-curricular classes via dual MBA/MD Design Lab teaching human-centered approaches · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P595** · `fact` · Johns Hopkins Technology Ventures FastForward provides accelerator programs, seed funding, mentorship · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P596** · `fact` · Yale course "New Ventures in Healthcare and Life Sciences" covers digital health/medical devices from needfinding to prototyping/commercialization · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P597** · `fact` · University of Zurich = only non-American institution offering e-health/telemedicine and AI in medicine courses as electives for 2nd-year medical students · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P598** · `fact` · One university piloted digital health program with 10 medical students; 22 teaching units covering telemedicine/health economics/AR/VR/mHealth/wearables/health innovation · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
- **P599** · `fact` · Systematic analysis of American medical schools identified 7 additional universities with DHT offerings; only 1 had teaching integrated in medical curriculum · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)

### 12.3 Why Should Medical Schools Teach Digital Health?
- **P600** · `fact` · Flexner Report (1910) = transformative turning point in medical education, emphasized incorporating scientific theory into curricula · [src:S01](../../INBOX/hi/Digital Health: From Assumptions to Implementations.md)
