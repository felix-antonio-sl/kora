---
_manifest:
  urn: urn:salud:kb:dbt-oxford-implementation-p02
  provenance:
    author: Michaela A. Swales (ed.)
    date: '2018'
    source: source/salud/dbt/dbt-oxford.md
version: 1.0.0
status: publicado
tags:
- dbt
- dialectical-behaviour-therapy
- implementation
- dissemination
- fidelity
- adherence
- quality-assurance
- programme-development
lang: en
extensions:
  kora:
    family: note
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:dbt-oxford-implementation
---

# The Oxford Handbook of DBT — Implementation - Parte 02

## Technology-Augmented DBT

**Authors:** Anita Lungu, Chelsey R. Wilks, Marsha M. Linehan

### Rationale for Computerized Psychotherapy

WHO (2013): 50% of severe mental health patients in high-income countries, 85% in low/middle-income countries, do not receive treatment. Half the world has one psychiatrist per 200,000+ people.

Computerized treatments (CTs) advantages: no training required post-development, consistent fidelity, easy replication/updating, geographic independence, lower cost, reduced stigma (users disclose sensitive information more readily to computers), rapid propagation of treatment changes.

CT evidence: large effect sizes for anxiety disorders, medium for depression; drop-out rates (2-29%) comparable to face-to-face therapy. Over 90% of CBT RCTs excluded suicidal individuals; 74% excluded addictive behaviour -- DBT uniquely positioned to fill this gap.

### DBT's Structural Compatibility with Technology

**Modularity at multiple levels:**
- Treatment functions (5): capability, motivation, generalization, therapist motivation, environment structuring
- Treatment modes (4): individual therapy, skills group, coaching, consultation team
- Skills content: acceptance modules (mindfulness, distress tolerance) + change modules (emotion regulation, interpersonal effectiveness), each subdivided into individual skills
- Session structure: standardized workflow (mindfulness practice, homework review, new skill teaching, practice, homework assignment)
- Protocol integration: ancillary evidence-based protocols (e.g., prolonged exposure for PTSD) slot into DBT hierarchy when indicated

Each module can potentially be delivered via different technology: teleconferencing for skills groups, call centres for coaching, videoconferencing for consultation teams, apps for motivation enhancement.

**Algorithmic characteristics:** Chain analysis, missing links analysis, Opposite Action skill, Check the Facts, DEAR MAN GIVE FAST -- all follow decision-tree logic translatable to computerized algorithms.

### Persuasive Technology Framework

Fogg (2003) and Oinas-Kukkonen & Harjumaa (2008) framework applied to DBT:

| Category | Strategies | DBT Application |
|---|---|---|
| Primary task support | Reduction, tunnelling, tailoring, personalization, self-monitoring, simulation, rehearsal | Inserting homework into calendar; VR for opposite action/exposure; guided skill practice sequences |
| Dialogue support | Praise, rewards, reminders, suggestion, similarity, liking, social role | Post-session encouragement; daily mindfulness reminders; skill-practice prompts via SMS/email |
| System credibility | Trustworthiness, expertise, authority, third-party endorsement, verifiability | Treatment developer delivering content; academic institution branding; research evidence citation |
| Social influence | Social learning, comparison, normative influence, facilitation, cooperation, competition, recognition | Observational learning from video vignettes; peer support via social media (especially adolescents) |

Two types of technology-assisted persuasion:
- **Computer-mediated:** Humans persuading via technology (text messaging, email for coaching, content reinforcement)
- **Human-computer:** Technology alone persuading (automated reminders, app-guided skill practice)

### Patient-Environment Interaction

Mobile devices generate passive behavioural data: social network patterns, activity levels, voice tone, locations frequented. With patient consent, augments therapist assessment of environmental context. Enables: change detection, risk alerts, chain analysis enrichment with objective data. Ethical concerns around big data/privacy require careful consideration.

### Technology and Behavioural Analysis

Technology can enhance chain analysis by: supplying environmental information from device records; prompting patient self-guided chain analysis upon strong emotion detection or at scheduled times; storing chain sequences to illustrate change trajectories; identifying high-impact links across multiple chains; alerting when environmental variables align with prior problematic patterns.

### Existing DBT Technology Tools

**DBT Skills DVDs (Linehan, 2006-2007):** Video teaching of DBT skills. RCT (n=30, within-subject): viewing Opposite Action skill video increased skill knowledge and expectations of positive outcomes vs. control.

**DBT Coach app:** Assesses emotional intensity, guides through Opposite Action skill steps, includes follow-up reassessment. Quasi-experimental evaluation (n=22, 10-14 days): high acceptability, decreased depression and general distress. Extended version (all four modules, n=16): high acceptability/usability; reduced NSSI but no other significant clinical associations.

**Commercial DBT apps:** ~13 apps available covering diary cards, skills coaching, skill training. Prices: free to US$22.99. None formally evaluated for usability, acceptability, or clinical efficacy.

### iDBT for Emotion Regulation (iDBT-ER)

Computerized transdiagnostic DBT skills training. 8-week online programme for individuals with mood/anxiety disorders above emotion dysregulation threshold (DERS). No therapist contact except brief phone for suicide risk assessment.

**Design features:**
- Welcome/orientation/commitment video by treatment developer
- Session structure mirrors standard DBT: mindfulness practice, homework review with missing-links analysis, new skill teaching via 5-10 min video segments, practice activities, homework assignment with barrier troubleshooting
- Daily between-session reminders (SMS/email) for mindfulness and skills practice
- Electronic daily diary card
- Self-referencing activities (personalizing skill application areas)
- Modelling via video vignettes; behavioural rehearsal activities
- Elaborative rehearsal (interactive exercises connecting new content to prior knowledge)
- Planning/scheduling activities for generalization

**Pilot results (N=34):** Significant reductions in emotion dysregulation, anxiety, depression, general distress. Increases in mindfulness and skills practice. Drop-out: 17.6% (defined as 3+ weeks without login). Safe to administer; suicide risk protocol activated only a few times, no additional intervention needed.

**Technical stack:** Vimeo (video hosting), Articulate Storyline (e-learning development), Articulate Online LMS (delivery platform).

### iDBT for Suicidal and Heavy Episodic Drinkers

Modified iDBT-ER for high-risk populations (suicidal + problematic alcohol use) -- populations typically excluded from online CBT trials.

**Key modifications:**
- New skills: "Dialectical Drinking" and "Wise Mind Goals" teaching abstinence violation effect, motivational interviewing, goal setting (replacing rigid abstinence focus with personalized drinking goals)
- Human-in-the-loop safety protocol: clinicians contact clients (1) during first week, (2) when suicide risk escalates, (3) when urge to quit increases. "Caring emails" sent when clients unreachable

### Future Directions

- Identify active treatment ingredients for maximally efficient technology delivery
- Mechanism-of-action research to determine what components to computerize
- Determine optimal technology-face-to-face complementarity ratios
- Real-time data collection and evaluation tools for outpatient care
- Open-source data sharing and collaboration between developers and users
- VR applications for exposure-based interventions within DBT hierarchy
- Passive mobile sensing for risk detection and environmental assessment
- Machine learning for pattern identification across behavioural chains
