# Chapter 11 Object-Process Language: The Text
Among general-purpose modeling languages dominate the graphical ones such as
UML; textual modeling languages are not as popular though they have a big
potential.
Mazanec and Macek (2012)
OPM is bimodal: it employs both the visual (graphical) modality—OPD, and the verbal (textual)
modality—OPL. The textual OPL representation of the OPM model has both human-oriented and
machine-oriented goals. This chapter is devoted to presenting OPL and discussing its merits.
## 11.1 OPL: The Textual Modality
To enhance OPM’s expressive power, we associate with each OPD a collection of sentences in Object-
Process Language (OPL) as a textual, natural interpretation of the OPD’s graphic representation.
Object-Process Language (OPL) is a subset of English that expresses textually the
OPM model that the OPD set expresses graphically.
OPL is the textual counterpart of the graphic OPM system specification. It is extracted from the
diagrammatic description in the OPD set. Using a tool such as OPCAT, OPL is an automatically
generated textual description of the system in a subset of natural English. Devoid of the idiosyncrasies
and excessive cryptic details that characterize programming languages, OPL sentences are understandable
to people without technical or programming experience.
A model fact is a relation between two or more things in an OPM model.
Each model fact is expressed in the OPM model in two modalities: in the graphic modality in one or
more OPDs, and in the textual modality in an OPM sentence for each graphical expression of that model
fact.
Each OPD element (thing or link) has a graphic symbol. An OPD construct is a syntactically valid
combination of OPM graphic symbols, which expresses a model fact. That model fact is equivalently
expressed by a sentence or part of a sentence in Object-Process Language (OPL) text. This is summarized
in the following set of definitions.
A model fact is expressed graphically by an OPD construct and textually by an equivalent OPL
sentence or sentence part.
An OPD element is the graphical expression of a thing or a link.
An OPD construct is a collection of connected OPD elements.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 11

Object-Process Language: The Text
## 11.2 The Dual Purpose of OPL
OPL serves two goals, oriented to two directions: humans and machines.
## 11.2.1 The Human-Oriented OPL Goal
The human-oriented OPL goal is to convert the set of OPDs comprising the OPM model into a natural
language text that can be used to express and communicate analysis and design results among the various
stakeholders involved in the system under construction. Users include domain experts and their
executives on the customer side of the system under development, as well as architects and modelers on
the supplier side of the same system.
OPL enables involving the customer-side stakeholders, who are often non-technical, in the
requirements elicitation and initial conceptual modeling of the system under development. Engaging these
stakeholders as active participants helps streamline requirements, obtain stakeholders buy-in, and detect
errors soon after their inadvertent introduction.
Usually, these stakeholders do not have a command of programming languages, and it is not realistic
to expect them to read diagrams in a conceptual modeling language, let alone program code. Being used
to reading text (or viewing high-level slide presentations) rather than relating to diagrams, they (or their
engineers or lawyers) are likely to prefer reading text over examining and interpreting OPDs. For them,
OPL serves the purpose of verification and validation of the requirements, which are usually provided
initially in text and then modeled in OPM. This requirement model helps identify gaps and
inconsistencies so requirements can be improved and be acceptable to both sides—the customer and the
contractor or developer.
For the system architects and modelers on the supplier side, the bimodal representation of the OPM
model is instrumental in getting immediate feedback on each graphic editing operation, enabling them to
spot modeling errors as soon as they are made, before they propagate and start to cause damage whose
magnitude increases exponentially with the error detection latency. Moreover, novice OPM users can
experience steep learning curve by quickly gaining familiarity with the semantics of the OPM graphic
modality by inspecting the text and corresponding graphic in tandem.
Since textual documents are still the prominent way for communicating requirements and
specifications of systems among parties, a formal textual modality that is generated “for free” and always
matches the graphical specification is of great value. There are various other ways beside text to define
and specify requirements including storyboards and mockups, which are gaining popularity in the
software industry where people have decreasing patience neither for tiring text documents nor for
complex conceptual models. The formal OPM model can serve as a basis for generating such popular
means. Indeed, work in this direction has started by creating an animated cartoon from the simulated
animation of OPM models in OPCAT (Bolshchikov et al. 2015).
## 11.2.2 The Machine-Oriented OPL Goal
The machine-oriented OPL goal has to do with its formality. OPL provides a firm basis for automatically
generating the designed application—the infrastructure needed to continue the application development.

OPL is defined formally using a context-free grammar, so the OPL text file can serve as a basis for
generating application artifacts that include executable code and database schema. This approach enables
round-trip engineering, in which changes in the analysis, design and specification are almost
automatically reflected in the final application. These traits make the combination of the graphic-oriented
OPD and its equivalent text-based OPL counterpart an ideal infrastructure for systems specification.
## 11.3 The Graphics-Text Equivalence OPM Principle
The default OPL is English, but any natural language can serve as a basis for OPL. Since the OPD is
based on graphics and iconic symbols, it can serve as a common platform for translation among OPLs in
various natural languages.
At each point in time during the modeling (when there are no unlinked things in the model), one can
precisely reconstruct the OPD from its OPL paragraph and vice versa. This is expressed in the following
graphics-text equivalence OPM principle.
An OPL paragraph of an OPD is a collection of OPL sentences that express textually
the same model facts that this OPD expresses graphically.
The Graphics-Text Equivalence OPM Principle
Any model fact expressed graphically in an OPD is also expressed textually in the corresponding
OPL paragraph.
The OPD set is complete graphical representation of the OPM model. It is the set of (hierarchically
organized) OPDs that together specify all the model facts in the OPM model.
An OPL specification (OPL Spec) of an OPM model is the collection of all the unique
OPL sentences that express textually all the model facts that the OPD set expresses
graphically.
## 11.4 Metamodel of OPM Model Structure
While a comprehensive metamodel of OPM appears in an annex of ISO 19450 (see Chap. 24), in Fig.
## 11.1 we provide a high-level model of the structure of an OPM model that puts the above definitions in
context. A model of a model is a metamodel. Therefore, this OPM model is a metamodel. Using OPM to
specify the structure of an OPM model of a system, it depicts the conceptual aspects of OPM as parallel
hierarchies of the graphic and textual OPM modalities and their correspondence to produce equivalent
model expressions. This OPD is the system diagram (SD, or SD0)—the top-level diagram (level zero) of
the entire OPM metamodel.

Object-Process Language: The Text
+
can be in-zoomed to create
specifies
OPM
Model
System
graphically specifies
OPD
Set
textually specifies
OPL
Spec
+ +
graphically specifies
OPL
OPD
textually specifies
Paragraph
OPD
Construct
graphically specifies
+
textually specifies
OPL
Sentence
Link Set
Punctuation
Mark
+
3..*
Phrase
Word
+
graphically specifies
Reserved
Phrase
textually specifies
+
2..*
Link
Thing Set
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
Thing Set consists of 2 to many Things.
Link Set consists of at least one Link.
Thing exhibits Name.
OPL Sentence consists of 3 to many Phrases and at least one Punctuation
Mark.
Phrase consists of at least one Word.
OPL Reserved Phrase and Name of Thing are Phrases.
Link graphically specifies Reserved Phrase.
Reserved Phrase textually specifies Link.
Thing can be in-zoomed to create OPD
### Figure 11.1
Metamodel (OPM model) of an OPM model structure

The two objects at the top of the OPD in Fig. 11.1 are OPM Model and System, connected with a
unidirectional tagged structural link from the former to the latter, yielding the OPL sentence OPM Model
specifies System. Further, OPM Model consists of OPD Set and OPL Spec. These are the two
complementary modalities—the graphical and the textual. From this point on, the OPD shows two
parallel hierarchies—the graphical and the textual—where going down entails increased level of detail.
The graphical hierarchy is OPD Set, OPD, OPD Construct, and (at the same level) Link Set and Thing
Set. The textual hierarchy that is parallel to the graphical OPD Set and OPD is OPL Paragraph and OPL
Sentence. An OPD and its corresponding OPL Paragraph are collections of model facts that a modeler
places into the same diagram—the same model context. At the next refinement level in this hierarchy, an
OPD Construct is the graphical counterpart of its corresponding textual OPL Sentence, and again, both
express the same model fact. Then, Link, which is a graphic element, is paralleled by Reserved OPL
Phrase, since the latter textually specifies the former, as in the reserved OPL phrase consists of, which is
the textual counterpart of the aggregation-participation symbol, , and in affects, which is the textual
counterpart of the effect link, .
## 11.5 Reserved and Non-Reserved OPL Phrases
While OPL is a subset of English, it is formal. The formal syntax for OPL is expressed by a context-free
grammar in Extended Backus-Naur Form (EBNF) in Annex A of ISO 19450 Publically Available
Specification (see section 24.4.1). The EBNF OPL specification comprises about 400 production rules
occupying 12 pages. Using EBNF, a set of production rules unambiguously defines how OPL sentences
are to be constructed and parsed. Figure 11.2 presents three production rules as examples of expressing
the OPL syntax in EBNF. Each production rule has a right hand side and a left hand side, separated by the
= sign. The first production rule specifies that an OPL paragraph comprises one or more OPL sentences,
separated by a “new line” symbol. The second production rule specifies that an OPL sentences comprises
an OPL formal sentence followed by a full stop (“.”) symbol. The third production rule specifies that an
OPL formal sentence can be of one of four types: a thing description sentence, a procedural sentence, a
structural sentence, or a context management sentence.
In programming languages, the analogues of words are tokens—the atomic units resulting from lexical
analysis. In most programming languages, spaces separates tokens apart. Tokens are input to the next
process, parsing. OPL sentences are obviously far more readable than a script of any computer programming
language. These sentences are carefully designed using a subset of English to convey a clear and
straightforward meaning through well-phrased and humanly understandable constructs. Yet, using the
OPL EBNF-based formal syntax definition, OPL sentences can undergo parsing just like commands or
lines in a programming language. As in programming languages, parsing an OPL sentence yields phrases.
A phrase is a combination of one or more words, separated by spaces, which constitutes a logical
entity, but not a complete sentence. OPL phrases can be reserved and non-reserved. Any OPL sentence
consists of non-reserved OPL phrases—domain- or system-specific words or word combinations—which
the system architect or modeler uses, and reserved OPL phrases, which link the non-reserved phrases and
provide for creating a sentence in a natural language.

Object-Process Language: The Text
### Figure 11.2
Three exemplary production rules expressing the OPL syntax in EBNF
An OPL phrase is a sequence of one or more words in an OPL sentence.
A non-reserved OPL phrase is a modeler-defined OPL phrase that expresses a
system- or domain-specific OPM model entity or relation name.
Non-reserved OPL phrases are names of OPM objects, processes, and states that the modeler assigns
while creating the OPDs that comprise the OPM model. Non-reserved OPL phrases also include less
frequently used ones, such as (user defined) tagged structural relations and participation constraints.
A reserved OPL phrase is an OPL phrase built into the OPL EBNF syntax definition
that connects two or more non-reserved OPL phrases.
Reserved OPL phrases are parts of the sentence syntax that express relations or connections between
non-reserved OPL phrases, or constrains on them. Examples of reserved OPL phrases are “requires”,
“yields”, “consumes” “and”, “or”, “affects”, “exactly one of”, “at least one”, and “consists of”. These
definitions of reserved and non-reserved phrases stipulate that the former are the mortar that “glues” and
holds together in a meaningful way the model building blocks—the non-reserved phrases that express
system-specific terms.
The following bolding OPL convention helps distinguish between the two kinds of OPL phrases.
The Bolding OPL Convention
Non-reserved OPL phrases appear in Arial bold font, while reserved OPL phrases appear in Arial
non-bold font. Punctuation marks are bolded.
For example, the OPL phrase “Automatic Crash Responding” in the OPL sentence “Automatic Crash
Responding affects Vehicle Occupants Group.” is non-reserved and therefore appears in Arial bold font.
The non-bold phrases, such as “and”, “or”, “affects”, “exactly one of”, and “consists of”, are reserved OPL
phrases.
A CASE tool implementation needs to automatically translate the model facts expressed by the OPD
constructs into OPL sentences. To further help distinguish between things, such tools should use colors in
fonts of phrases that match their colors in the OPD. For objects, the default color in OPCAT is green, for
processes—blue, for states—brown, and non-reserved OPL phrase are in black font. If your book version

enables seeing colors, Fig. 10.6, which is an OPCAT-generated OPM model of the process test system,
exemplifies this coloring convention.
## 11.6 Motivation for OPM’s Bimodal Expression
A legitimate question that can be raised with respect to OPL is why is text needed in addition to the
diagram if we have a good graphic representation of our model? One may indeed wonder why two
modalities are needed. According to the graphics-text equivalence OPM principle, the text and the
graphics express the same contents, so there is a 100% redundancy in terms of information content! Isn’t
this a waste of resources? Wouldn’t it make more sense to stick to just one modality—either graphics or
text—and leave the other out?
## 11.6.1 The Dual-Channel Assumption
The graphics-text equivalence is a major source of OPM’s expressive power. OPL text complements the
OPD graphics. This duality implements the dual-channel assumption (Clark and Paivio 1991; Baddeley
1992). This is one of three major research-supported cognitive assumptions (Mayer 2003; Mayer and
Moreno 2003), which stipulates that humans possess separate channels and mechanisms for processing
visual and verbal representations. The combination of OPD and OPL caters directly to this dual-channel
assumption (Dori 2008). Some humans are more visually inclined, while others are more text-oriented.
The text and the graphics reinforce each other while the model creator or the model readers try to make
sense of the semantics that model elements convey in various combinations.
The cognitive-physiological basis for this principle is that the human mind is geared to accept both
visual-pictorial-graphic signals and audio-verbal-written signals. Graphics and text trigger different areas
in the brain. Popularly, this is often referred to as the left brain/right brain functions. Indeed, the left
hemisphere is dominant in language, processing what one hears and handling most of the duties of
speaking. The right hemisphere is mainly in charge of spatial abilities, face recognition, comprehending
visual imagery and making sense of what we see. Thus, catering to “both sides of the brain” through
language and pictures is more likely to get the message—the conceptual model—across. Accordingly, a
model that can be presented bimodally in both graphic and text is preferred over a model that can be
presented in only one of the modalities. Almost all conceptual modeling languages are either textual or
graphical, but not both. OPM is the first to combine the two modalities (USPTO 7,099,809, 2006).
## 11.6.2 Benefits of the Bimodal Representation
Individuals have different preferences regarding the way they read and write specifications. Usually,
engineering-oriented people (sometimes considered to be “left-brainers”) prefer diagrams, while business-
oriented people (“right-brainers”) favor text. Moreover, even for the same individual, the content may
sometimes become clearer by looking at one modality while at other times the complementary modality is
more helpful. The fact that OPL is a subset of English, the lingua franca natural language, makes it
readable and understandable to people without the need to learn any programming or pseudo-code-like

Object-Process Language: The Text
language. The syntax and semantics of OPL are well defined, eliminating the ambiguity that is often
inherent in natural languages.
The syntax of OPL is designed such that the resulting text constitutes plain natural, albeit syntactically
restricted, English sentences. Therefore, the bimodal graphics-text representation of the OPM model helps
involve non-technical stakeholders in the requirements elicitation and initial conceptual modeling of the
system under development. This involvement of such stakeholders engages them as active participants
and helps detect errors soon after their inadvertent introduction.
For example, suppose that instead of using the bidirectional arrow , which is the effect link, the
modeler of Fig. 1.3, would use by mistake the unidirectional arrow , which is the result link, from the
process Automatic Crash Responding to the object Vehicle Occupants Group to express the fact that
Automatic Crash Responding affects Vehicle Occupants Group. In this case, the following OPL sentence
would have been created:
Automatic Crash Responding yields Vehicle Occupants Group.
Obviously, this sentence, while syntactically correct, makes no sense. The modeler or the customer’s
representative participating in the modeling session would likely detect it on the spot. The detected error
can then immediately be rectified and the correction can be verified by simply reading the newly created
OPL sentence.
Any natural (and artificial) language can be selected as the target language to which the OPD
constructs are converted. Moreover, the graphic representation is language-neutral and can therefore serve
as a means for translating from one language to another.
## 11.6.3 Engaging the Customer: The Social Aspect
Using an OPM-supporting software product, OPL sentences are constructed automatically in real time in
response to inputting OPD graphic symbols on the screen. This capability of any team member to provide
immediate feedback about facts being modeled during the modeling process is of utmost importance, as it
provides for immediate system interpretation of the human developer’s intents.
The simplicity and straightforwardness of this real-time response to the modeler’s graphic input in the
form of a subset of English is highly valuable; not only does it provide for the ability to catch errors as
soon as they are made, it also enables the active participation of the system’s customer in the modeling
session, where she or he can provide immediate feedback as the modeling progresses. Hence, the value of
such participation is beyond just spotting errors upon their creation; it is a social process that involves the
customer-side stakeholders early-on in the design, justifiably making them feel that they are part of the
decision-making process and mitigating resistance to change, a common known human characteristic.
The system’s OPL specification resulting from an OPD set is thus amenable to being scrutinized,
modified, and ultimately confirmed by the customer or domain experts acting on his behalf, who need not
be software experts.
The provision of having representatives of the customer working should-to-shoulder with the
developers increases the likelihood of pinpointing and catching design errors as soon as they are created,
resulting in significant saving of time, money, and troubles down the road. This real-time feedback is
indispensable not just in spotting errors but also in correcting them at an early stage of the system

lifecycle, before they had a chance to propagate and cause costly damage. Any graphics edit (addition or
removal of an element) changes the OPL script. Changes can be implemented until a satisfactory result is
obtained and the customer can “sign” on the model as the blueprint of the system to be developed.
## 11.6.4 Closing the Requirements-Design Gap
The capability to directly and precisely translate analysis and design results to a subset of natural
language has a tremendous advantage. As noted, prospective users and customers may be more
comfortable with reading text than with interpreting OPDs, let alone deciphering program code. This way,
the OPL text and its OPD graphic equivalent help close the gap between the original requirement
specification, which is currently still expressed as free prose, and the actual system specification as
expressed by the resulting OPM model. While OPL sentences are easily comprehensible to humans and
thus document the system “for free,” the ability to parse them provides a firm basis for automated tasks
such as executable code generation, simulation, initial user interface generation, and database schema
definition.
## 11.7 Tesperanto: A Human Readable Auto-generated Text
OPL consists of short, often disconnected sentences. While each OPL sentence is a syntactically and
semantically correct English sentence, lack of fluency from one OPL sentence to the next prevents OPL
from becoming a descent substitute for the free text that dominates real-life requirements and other
technical specifications, such as international standards. Indeed, being mechanical and repetitive, with no
text fluency, long OPL text is not natural for human reading. This has motivated the development of
Tesperanto (Blekhman and Dori 2013) as the next level of automatic model-based text-from-graphics
generation on top of, or instead of OPL.
### Figure 11.3
OPM model of Gas Metal Arc based Welding. Top: OPD. Bottom left: OPL. Bottom right: Tesperanto
Tesperanto is an enhancement of OPL that follows OPM’s gradual presentation principles, which
cater to humans’ cognitive limited capacity. It includes heuristics for sentence length adjustments,
synonyms, word ordering, phrase recurrence control, and other algorithms aimed at making the

Object-Process Language: The Text
Tesperanto text look less mechanistic and more human readable. Figure 11.3 is an OPM model of Gas
Metal Arc based Welding. The OPD at the top is automatically translated to both OPL and Tesperanto in
the bottom left and right, respectively. This simple example demonstrates the differences in fluency of
reading OPL vs. Tesperanto. While both text-from-graphics translations faithfully reflect the formal and
verified OPM graphic model, Tesperanto is more humanly readable and less boring, repetitive, and
mechanical. For example, while in the OPL the process Welding is repeated four times, once for each kind
of procedural relation, in the Tesperanto translation it only appears once. Since Tesperanto is still
evolving as a subject of research, it is not further used in this book.
## 11.8 Summary
Object-Process Language (OPL) is a subset of English that expresses textually the OPM model
that the OPD set expresses graphically.
The formal syntax for OPL is expressed by a context-free grammar in Extended Backus-Naur
Form (EBNF) in Annex A of ISO 19450 Publically Available Specification (PAS).
A model fact is a relation between two or more things in an OPM model.
An OPD element is the graphical expression of a thing or a link.
An OPD construct is a collection of connected OPD elements.
OPL serves two goals, oriented to two directions: humans and machines.
The human-oriented OPL goal is to convert the set of OPDs comprising the OPM model into a
natural language text.
The machine-oriented OPL goal is to provide a firm basis for automatically generating the
infrastructure for the application development.
An OPL paragraph of an OPD is a collection of OPL sentences that express textually the same
model facts that this OPD expresses graphically.
The graphics-text equivalence OPM principle: Any model fact expressed graphically in an OPD
is also expressed textually in the corresponding OPL paragraph.
A metamodel is a model of a model.
The metamodel of the structure of an OPM system model shows two parallel hierarchies—the
hierarchy of graphic objects and the corresponding hierarchy of text objects.
An OPL specification of an OPM model is the collection of OPL sentences that express textually
all the model facts that the OPD set expresses graphically.
An OPL phrase is a sequence of one or more words.
A non-reserved OPL phrase is a modeler-defined OPL phrase that expresses a system- or
domain-specific OPM model entity or relation name.
A reserved OPL phrase is an OPL phrase built into the OPL EBNF syntax definition that
connects two or more non-reserved OPL phrases.

The dual-channel assumption is that humans possess separate systems for processing visual and
verbal representations.
The syntax and semantics of OPL are defined as a subset of English, eliminating the ambiguity
that is often inherent in natural languages.
Tesperanto is the next generation of OPL.
## 11.9 Problems
1. 2. 3. 4. 5. 6. 7. What are the pros and cons of having a textual system model specification modality alongside
the graphical modality?
If you were to design a new modeling language with the constraint that it can use only one
modality, which one would you choose? Why?
Which of the following three definitions of “meta”, taken from dictionary.com, fits metamodel?
A prefix appearing in loanwords from Greek, with the meanings “after,” “along with,” “beyond,”
“among,” “behind,” and productive in English on the Greek model: metacarpus; metagenesis.
A prefix added to the name of a subject and designating another subject that analyzes the
original one but at a more abstract, higher level: metaphilosophy; metalinguistics.
A prefix added to the name of something that consciously references or comments upon its own
subject or features: a meta-painting of an artist painting a canvas, metacognition; meta-analysis.
Copy three OPL sentences from this chapter and reverse their bolding, that is, make each bold
word not bold and vice versa. What version do you prefer—the original or the reversed? Why?
