# Chapter 24 Overview of ISO 19450
This book contains a comprehensive coverage of OPM that is compatible with ISO 19450 Publically
Available Specification (PAS) titled “Automation systems and integration—Object-Process
Methodology”, and in French: “Systèmes d’automatisation et intégration—Méthodologie du processus-
objet”. The ISO 19450 PAS has been adopted by the International Organization for Standardization (ISO)
in December 2015 through the work of ISO Technical Committee 184/ Sub-committee 5 (TC184/SC5) after
a six-year effort, mainly by Richard Martin, David Shorter, Alex Blekhman, and this author. This book
was prepared in parallel with the ISO 19450 PAS standard, so the two are almost completely aligned with
each other. Since the standard (formally PAS) must conform to the rules of ISO for standard authoring, it
is structured differently and is not as elaborate as the book. Rather, it is an orderly exposition of OPM that
enables tool developers to use it, along with this book, as a solid basis for developing an ISO 19450-
complaint software tool to support OPM-based conceptual modeling. ISO standards like ISO 19450 PAS
contain normative parts and often also one or more informative parts. To be compliant with the standard,
a normative part must be strictly followed, while an informative part is not mandatory. This book is a
superset of ISO 19450 PAS. About 90% of the material in this book is aligned with ISO 19450. The rest
can be considered as the equivalent of an addition to the informative part of the standard—it should be
followed, but ISO 19450 in its current initial form does not mandate it. This closing chapter describes
briefly the content of the ISO 19450 PAS, where each section is devoted to a summary of one or more
sections of ISO 19450.
## 24.1 The ISO 19450 Introduction
The first paragraph of the ISO 19450 document’s introduction (p.v) is the following.
Object-Process Methodology (OPM) is a compact conceptual approach,
language, and methodology for modelling and knowledge representation of
automation systems. The application of OPM ranges from simple assemblies of
elemental components to complex, multidisciplinary, dynamic systems. OPM is
suitable for implementation and support by tools using information and
computer technology. This document specifies both the language and
methodology aspects of OPM in order to establish a common basis for system
architects, designers, and OPM-compliant tool developers to model all kinds of
systems.
The introduction goes on to discuss the generality and industry- and business-wide applicability of
OPM as a basis for model-based systems engineering:

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

Overview of ISO 19450
OPM notation supports the conceptual modelling of systems with formal syntax
and semantics. This formality serves as the basis for model-based systems
engineering in general, including systems architecting, engineering,
development, life cycle support, communication, and evolution. Furthermore,
the domain-independent nature of OPM opens system modelling to the entire
scientific, commercial and industrial community for developing, investigating
and analysing manufacturing and other industrial and business systems inside
their specific application domains; thereby enabling companies to merge and
provide for interoperability of different skills and competencies into a common
intuitive yet formal framework.
OPM facilitates a common view of the system under construction, test,
integration, and daily maintenance, providing for working in a
multidisciplinary environment. Moreover, using OPM, companies can improve
their overall, big-picture view of the system’s functionality, flexibility in
assignment of personnel to tasks, and managing exceptions and error recovery.
System specification is extensible for any necessary detail, encompassing the
functional, structural and behavioural aspects of a system.
Toward the end of the Introduction section, there is reference to the drafting and authoring of
technical documents in general and international standards in particular:
One particular application of OPM is in the drafting and authoring of technical
standards. OPM helps sketch the implementation of a standard and identify
weaknesses in the standard to reduce, thereby significantly improving the
quality of successive drafts. With OPM, even as the model-based text of a
system expands to include more details, the underlying model keeps
maintaining its high degree of formality and consistency.
The initial motivation for making OPM an ISO standard is to use it as a basis for model-based
standards—the contemplated new generation of ISO standards. Indeed, in Dori et al. (2010) we proposed
a combined, model-based structured graphical and textual meta-standard approach for specification,
verification and validation of complex systems in general and ISO enterprise standards in particular. This
methodology, developed under the auspices of the ISO TC 184/SC 5 OPM Study Group, is designed to
cope with current inconsistencies and incompleteness of technical documents (Blekhman et al., 2011). To
support authors of technical specifications while creating and editing model-based technical documents,
we developed Model-Based Authoring of Specifications Environment (MBASE).
In order to overcome the problem of the difficulty humans have with reading long OPL texts due to its
mechanistic, repetitive nature, the MBASE framework includes Tesperanto (short for Technical
Esperanto)—an evolution of OPL that is still automatically generated from the OPD but is much more
amenable to being read by humans than OPL, even if the text is long (Blekhman and Dori 2013).This
framework has been successfully applied in modeling communication in an operation room (Blekhman
et al. 2015).

Tesperanto can be considered as a textual version of The Imitation Game, better known as Turing
Test—a test proposed in 1951 by Alan Turing, which was designed to settle the issue of machine
intelligence. While in the original Turing Test a human judge has to decide whether she or he is
interacting with a human or a computer, in the textual version of Turing Test, the judge has to decide
whether a given text was written by a computer or by a human. Quite clearly, OPL text, while being
comprised of syntactically correct English sentences will quickly be identified as written by a computer, it
will be more difficult for a human to reveal this when presented with a Tesperanto text.
## 24.2 ISO 19450 Terms, Definitions, and Symbol Sections
Clause 3 of the 19450 PAS includes over 80 definitions of concepts that are used in the standard. These
are ordered alphabetically, with Italicized words in the definitions being themselves terms defined in this
clause. Figure 24.1 is a sample of the ISO 19450 Terms and Definitions Clause, containing some of the
terms starting with the letter p. For example, procedural link is defined at the top of Fig. 24.1 as a
“graphical notation of procedural relation in OPM”. The term procedural relation is in Italics because it is also a
term in its own right, which indeed happens to appear next alphabetically:
## 3.57 procedural relation
connection or association between an object or object state and a process
According to ISO directives, the definitions must be phrased such that if we can substitute an
Italicized term with its definition and still get a legible, sense-making definition. For example, when we
perform the term substitution of procedural relation in the definition of procedural link, we get:
## 3.56 procedural link
graphical notation of connection or association between an object or object state and a process in OPM
This explains why none of the term definitions neither starts with a capital letter nor end with a period.
We can continue with this substitution process twice, first for process:
## 3.56 procedural link
graphical notation of connection or association between an object or object state and a transformation of
one or more objects in the system in OPM
Looking at the definition of transformation, we find:
## 3.77 transformation
creation (generation, construction) or consumption (elimination, destruction) of an object or a change in the
state of an object
So now we get as a definition of procedural link:

Overview of ISO 19450
## 3.56 procedural link
graphical notation of connection or association between an object or object state and a creation
(generation, construction) or consumption (elimination, destruction) of an object or a change in the state of
an object of one or more objects in the system in OPM
### Figure 24.1
Sample of ISO 19450 Terms and Definitions Clause
As we see, this is still working, although, unavoidably, the definition gets longer and longer. This can
go on until all substitution have been made, and the validity check is done by verifying that no cycle has
been created, i.e., the term being defined must not appear anywhere in the definition.
The list of term definitions is followed by Clause 4—Symbols and Clause 5—Conformance. Then
comes Clause 6—Object-Process Methodology principles and concepts, discussed next.
## 24.3 Object-Process Methodology Principles and Concepts
Clause 6 is an overview of OPM. It starts with OPM modeling principles, initially “Modelling as a
purpose-serving activity”, which discusses how to determine the scope of the model:
System function and modelling purpose shall guide the scope and extent of
detail of an OPM model. … The function or benefit expectations of stakeholders
in general and beneficiaries in particular shall identify and prescribe the
modelling purpose. This, in turn, shall determine the scope of the system
model.

The use of “shall” is mandatory and prevalent in standards, as the first line in the quote above
demonstrates; it implies a mandatory, conformance issue. Next, unification of function, structure, and
behaviour is discussed:
… The combination of system structure and behaviour enables the system to
perform a function, which shall deliver the (functional) value of the system to
at least one stakeholder, who is the system’s beneficiary. An OPM model
integrates the functional (utilitarian), structural (static), and behavioural
(dynamic) aspects of a system into a single, unified model. Maintaining focus
from the viewpoint of overall system function, this structure-behaviour
unification provides a coherent single frame of reference for understanding the
system of interest, enhancing its intuitive comprehension while adhering to
formal syntax.
The Clause then goes on to elaborate on the difference between function and behavior, the former
being a subjective, utilitarian aspect, while the latter is the objective dynamic system aspect. With respect
to setting the boundary of the system, 19450 states:
The system’s environment shall be a collection of things, which are outside of
the system but which may interact with the system, possibly changing the
system and its environment. The modeller shall distinguish these
environmental things, which are not part of the system, from systemic things,
which are part of the system. The modeller is not able to architect, design or
manipulate the structure and behaviour of environmental things even though
those environmental things may influence or be influenced by the system.
The last subject in the first subclause of Clause 6 is the clarity-completeness trade-off:
Overwhelming detail and complicatedness are inherent in real-life systems.
Making such systems understandable entails a trade-off that should balance
between two conflicting criteria: clarity and completeness. Clarity shall be the
extent of unambiguous comprehension that the system’s structure and
behaviour models convey. Completeness shall be the extent of specification for
all the system’s details. These two model attributes conflict with each other. On
the one hand, completeness requires the full stipulation of system details. On
the other hand, the need for clarity imposes an upper limit on the extent of
detail within an individual model diagram, after which comprehension
deteriorates because of clutter and overloading.
The next subclause in Clause 6—OPM Fundamental Concepts—presents first the bimodal representation
of OPM—its graphics text equivalence:
An OPM model shall be bimodal with expression in semantically equivalent
graphics and text representations. Each OPM model graphical diagram, i.e. an
Object-Process Diagram (OPD), shall have an equivalent OPM textual
paragraph comprised of one or more OPM language sentences using the Object-
Process Language (OPL).

Overview of ISO 19450
Then OPM elements are defined as things and links. This is the first step in defining the OPM metamodel,
described in ISO 19450, as shown in Fig. 24.2.
In the sequel, the critical difference between a conceptual models and a runtime model is explained,
emphasizing that when constructing OPM models, modelers need to understand the distinction between
the conceptual model they are creating and an operational occurrence of that model that they may use to
assess system behavior. The modeler may simulate system behavior by creating object and process
operational instance occurrences, and then follow the flow of execution control embodied in the
connections and OPM semantic rules.
### Figure 24.2
OPM metamodel overview (Figure 1 in ISO 19450)1
## 24.4 The Four Annexes of ISO 19450
The main ISO 19450 document is 100 pages long. It provides an orderly exposition of OPM that is
coherent with the specifications in this book, although it is less elaborate and does not contain some
details, which can be considered “informative” (see below). The reaming 76 pages of this document
contain four annexes, which together complete the definition of OPM from various angles.
Annex A presents the formal syntax for OPL, in EBNF form. Annex B presents conventions and
patterns commonly used in OPM applications. Annex C presents aspects of OPM as OPM models.
Finally, Annex D summarizes the dynamic and simulation capabilities of OPM.
1The shading like the one in this figure indicates OPDs and excerpts copied from ISO 19450.

Each annex has an attribute whose values are “normative” and “informative”. The term normative in
ISO standards means that this is an abiding operational part of the standard and shall be followed by
whoever claims to conform to the standard.
Conversely “informative” means that this is a non-abiding part of the standard that may be followed
but is not mandatory to claim conformance to the standard. In this sense, all the material in this book that
is not included in the normative parts of ISO 19450 can be aggregated into another informative annex.
Based on Bibliowicz and Dori (2012), a fifth (informative) annex, in which OPDs are defined with a
graph grammar, was planned to be included in ISO 19450. It was finally removed because of technical
problems with the multiple graphical elements that were too difficult to handle with the new ISO
publication system.
## 24.4.1 Annex A: Normative: OPL Formal Syntax in EBNF
A formal grammar is a set of production rules of the form V = w that describe how to form valid
strings from the set of terminals—symbols that comprise the language’s alphabet. The alphabet of OPL is
the set of all the reserved phrases and punctuation marks. In a context-free grammar, every production
rule can be applied regardless of the context of a nonterminal. As discussed in Sect. 11.5, while OPL is a
subset of English, it is formal. The grammar of OPL is context free. The syntax, exemplified in Fig. 24.3,
uses the notation of Extended Backus–Naur Form (EBNF), a notation for expressing the syntax context
free grammar languages. The ISO version of EBNF used in ISO 19450 is specified in ISO 14977:1996.2
The EBNF OPL specification comprises about 400 production rules occupying 12 pages. Here is how
OPL is described in the foreword to the Annex.
2ISO 14977 is a freely available standard that can be downloaded free of charge from http://isotc.iso.org/livelink/
livelink/fetch/2000/2489/Ittf_Home/PubliclyAvailableStandards.htm

Overview of ISO 19450
### Figure 24.3
A sample of the EBNF notation expressing the context-free grammar of OPL
OPL is a dual-purpose language. First, it serves domain experts and system
architects engaged in analyzing and designing a system, such as an electronic
commerce system or a Web-based enterprise resource planning system. Second, it
provides a firm basis for automatically generating the designed application.
OPL is the textual counterpart of the graphic OPM system specification,
corresponding to the diagrammatic description in the OPD set. OPL shall be an
automatically generated textual description of the system in a subset of natural
English. Devoid of the idiosyncrasies and excessive cryptic details that characterize
programming languages, OPL sentences shall be understandable to people without
technical or programming experience.
## 24.4.2 Annex B – Informative: Guidance for OPM
This annex describes several OPM principles that appear in this book, as well as the multiple thing copies
convention, designed to reduce clutter when a link needs to be drawn between two things in an OPD that
are “geographically” remote by allowing duplication of the same thing. To facilitate recognition of the
repetition, the modeler may replace thing symbol by a corresponding duplicate thing symbol—a small
object or process slightly showing behind the repeated thing, as illustrated in Fig. 24.4.

### Figure 24.4
Duplicate object and duplicate process symbols
## 24.4.3 Annex C – Informative: Modeling OPM Using OPM
Annex C is a rather comprehensive, albeit not complete, model of the important concepts of OPM
expressed in OPM. This as a reflexive metamodel—a model of OPM that uses OPM to specify itself
(Reinhartz-Berger and Dori 2005). A key test of a “good” conceptual modeling language is its reflexive
metamodeling capability. As Annex C shows, OPM does it well. The SD in Fig. 24.5 is elaborated in
Annex C with about 20 OPDs.
Annex C also provides a metamodel of Process Performance Controlling—the process of executing a
process that specifies all the details involved in implementing the event-condition-action paradigm using
about 10 OPDs at four levels of detail. Figure 24.6 is SD1 of this system model. A complete and
executable specification of this system, integrated into the reflexive OPM model, can serve as a reliable
and flexible source of an advanced OPM modeling tool implementation.
## 24.4.4 Annex D – Informative: OPM Dynamics and Simulation
Annex D describes the animated execution of an OPM model and ways to specify and denote the
Duration attribute of a Process. The events presented so far were object or state events: they happened
when a specific object became existent or entered a specific state. Among other things, this Annex
specifies timed event, which depends on the arrival of a specific time in the system, as shown in Fig. 22.7.

Overview of ISO 19450
+
+
OPD
Set
OPD
OPD
Construct
Link Set
specifies
OPM
Model
graphically specifies
textually specifies
graphically specifies
textually specifies
graphically specifies
textually specifies
can be in-zoomed to create
Word
+
graphically specifies
textually specifies
OPL
Spec
OPL
Paragraph
OPL
Sentence
Punctuation
Mark
Phrase
Reserved
Phrase
System
+
+
+
3..*
+
Link
Thing Set
2..*
Thing
Name
OPM Model specifies System.
OPM Model consists of OPD Set and OPL Spec.
OPL Spec consists of at least one OPL Paragraph.
OPD Set consists of at least one OPD.
OPD Set graphically specifies OPL Spec.
OPL Spec textually specifies OPD Set.
OPD consists of at least one OPD Construct.
OPL Paragraph consists of at least one OPL Sentence.
OPD graphically specifies OPL Paragraph.
OPL Paragraph textually specifies OPD.
OPD Construct graphically specifies OPL Sentence.
OPL Sentence textually specifies OPD Construct.
OPD Construct consists of Thing Set and Link Set.
Thing Set consists of two to many Things.
Link Set consists of at least one Link.
Thing exhibits Name.
OPL Sentence consists of three to many Phrases and at least one Punctuation Mark.
Phrase consists of at least one Word.
OPL Reserved Phrase and Name of Thing are Phrases.
Link graphically specifies Reserved Phrase.
Reserved Phrase textually specifies Link.
Thing can be in-zoomed to create OPD
### Figure 24.5
Top-level OPD (SD) of a reflective OPM meta model (an OPM model of an OPM model)

### Figure 24.6
Process Performance Controlling from SD in-zoomed in SD1

Overview of ISO 19450
Birth
Person
minor adult
Growing
minor
Age [yr]
minor
adult
adult
e
## 0 <18 >=18
Legal Status
Changing
### Figure 24.7
Legal Status Changing changes Person from minor to adult when Growing changes Age of Person from
<18 to >=18. (Figure D.1 in ISO 19450)
Alternatively, Fig. 24.8 uses the object System Clock, which any system may have, either explicitly as
in this example, or implicitly, to trigger an event when the System Clock, which starts upon Birth, and
when it reaches 18 yr it creates an event that triggers Legal Status Changing.
### Figure 24.8
The System Clock event initiating Legal Status Changing (Figure D.2 in ISO 19450)
