# Chapter 23 Logical Operators and Probabilities
Logic and probability theory are two of the main tools in the formal study of
reasoning, and have been fruitfully applied in areas as diverse as philosophy,
artificial intelligence, cognitive science and mathematics.
Stanford Encyclopedia of Philosophy (2013)
Logical operators, including AND, NOT, OR, and XOR (exclusive OR) enable modeling complex
conditions on performance of processes. Using XOR, OPM can also assign probabilities to such outcomes
as creating one of several possible objects, or an object in a specific state. We discuss these in this
chapter.
## 23.1 Logical AND Procedural Links
Two or more procedural links of the same kind that originate from, or arrive at, different points along the
process ellipse circumference (the process context), have the semantics of the logical AND operator.
Graphically, the links with AND semantics do not touch each other on the process contour. We have been
using this operator all along as the default without explicitly stating this, as it seems natural. Indeed,
textually, the OPL reserved phrase “and” is used to express the logical AND.
The next three examples show the use of AND in various procedural links. In the OPD in Fig. 23.1
(right), the Safe Opening process requires both Safe Owner A and Safe Owner B. In Fig. 23.1 (left),
opening the Safe requires all three keys.
### Figure 23.1
Logical AND used with agent and instrument links

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

Logical Operators and Probabilities
In Fig. 23.2 (left), Meal Preparing yields all three of the dishes. In Fig. 23.2 (right), Meal Eating
consumes all three dishes.
### Figure 23.2
Logical AND used with result and consumption links
In the OPD on the left of Fig. 23.3, Interest Rate Changing affects the three objects Exchange Rate,
Price Index, and Interest Rate. In the OPD on the right, all three effects of Interest Rate Raising on
Exchange Rate, Price Index, and Interest Rate are made explicit via three pairs of in-out-specified effect
links.
### Figure 23.3
Logical AND used with effect link and with in-out specified link pairs

## 23.2 Logical NOT
“NOT” is a unary logical operator which simply reverses the state of any Boolean object (see Sect. 7.1):
A binary input of “yes” (positive, 1…) is converted to “no” (negative, 0…), and vice versa. There are
several ways to implement NOT in OPM. One is with the flip-flop mechanism, described in Sect. 19.5.
Another way is to use states as constraints or conditions for process execution. If, for example, we want to
model that a process P executes if and only if substance S is NOT present, we model the object S with
two implicit states: existent and non-existent. We link the non-existent state to P with an instrument link
or an instrument condition link, so P can execute only if S is in its non-e, i.e., when it does not exist.
### Figure 23.4
The mRNA Decay and Nuclear Import Process (Somekh et al. 2014) showing the use of NOT via existent and
non-existent states of molecules
The mRNA Decay and Nuclear Import Process is the in-zoomed process in Fig. 23.4 (Somekh et al.
2014). This OPD shows how the existent and non-existent states of molecules are used to implement
“NOT”. For example, the existent state of the complex CCR4Not (no pun intended), depicted at the
bottom right corner, is linked to Decaysome Import—the third subprocess from the top, so only if
CCR4Not exists can this subprocess take place. However, in this case there are six other substances (such
as Edc3) that can each enable the process, and they are linked with an OR logical operator (discussed
below), so only lack of all the seven substances would prevent CCR4Not occurring. If the non-e (short for

Logical Operators and Probabilities
non-existent) state of CCR4Not would be linked with a condition link to Decaysome Import, that would
mean (disregarding other links) that the absence of CCR4Not is the condition for the occurrence of
Decaysome Import.
A link fan is a set of f (f ≥2) procedural links of the same kind that originate from a
common point, or arrive at a common point, on the same object or process.
The convergent end of a link fan is the end that is common to the f fan links.
The divergent end of a link fan is the end that is not common to the f fan links.
## 23.3 Logical XOR and OR Link Fans
In order to express OR and XOR graphically, we use link fans.
The convergent end is attached to one thing, while the divergent end is attached to f things, where f is
the size of the link fan set—the number of links in the fan. A link can be a member of both a divergent
fan on its source and a convergent fan on its target.
Since the links are procedural, one end is attached to object and the other to processes or vice versa.
Formally, the attribute value of the Perseverance of the Thing attached to the link fan’s convergent end is
the opposite of the attribute value of the Perseverance of the f Things attached to the link fan’s divergent
end. Thus, as the OPD in Fig. 23.5 shows, if the attribute value of the Perseverance of the thing attached
to the link fan’s convergent end is dynamic (transient), then the thing is a Process. In this case, the
attribute value of the Perseverance of the f Things attached to the link fan's divergent end is static
(persistent), implying that these f things are all Objects.
## 23.3.1 The Logical XOR Operator
The semantics of the logical XOR operator is that exactly one of the f things connected to the divergent
end of the link fan is transformed, enables, or occurs. If the divergent link end is attached to f objects,
then exactly one object is transformed by the process at the convergent end of the link fan, or enables that
process. If the divergent link end is attached to f processes, then exactly one process occurs.
This use of the XOR operator in OPM is in line with the definition of XOR in digital systems, but it
may be different from some interpretations of the binary XOR operator with multiple inputs, where the
output is 1 for an odd number of inputs and 0 for an even number of inputs. Graphically, a single dashed
arc across the f links of the link fan whose focal point is at the convergent end of contact denotes the XOR
operator (see Fig. 23.5 left).
The syntax of a link fan of f things with XOR semantics is different for f = 2 and for f > 2. For f = 2,
the reserved idiom (split reserved phrase) “either … or” is used. Since this idiom in natural English is
reserved for expressing selection of exactly one of two (but not many) items, for f > 2, the reserved phrase
“exactly one of” is used. For example, since in Fig. 23.5 (left) the link fan comprises 2 agent links, f = 2, so
the OPL sentence is:
Either Safe Owner A or Safe Owner B handle Safe Opening.

Suppose an agent link to a third safe owner, Safe Owner C, is added to the fan, making f = 3. The OPL
sentence then becomes:
Exactly one of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening.
Safe can be closed or open.
Safe can be closed or open.
Either Safe Owner A or Safe Owner B handle Safe
At least one of Safe Owner A and Safe Owner B handle
Opening.
Safe Opening.
Safe Opening changes Safe from closed to open.
Safe Opening changes Safe from closed to open.
### Figure 23.5
Agent link fan examples expressing logical XOR (left) and logical OR (right)
## 23.3.2 The Logical OR Operator
The semantics of the logical OR operator is that at least one of the f things connected to the divergent end
of the link fan is transformed, enables, or occurs. If the divergent link end is attached to f objects, then at
least one object is transformed by the process at the convergent end of the link fan, or enables that
process. If the divergent link end is attached to f processes, then at least one process occurs. This use of
the OR operator in OPM is in line with the binary OR operator with two or more inputs.
Graphically, a double dashed arc across the f links of the link fan whose focal point is at the
convergent end of contact denotes the OR operator (see Fig. 23.5 right).
The syntax of a link fan of f things with OR semantics is similar for f = 2 and f > 2. For both, the
reserved phrase “At least one of” is used. For example, in Fig. 23.5 (right), where the link fan comprises 2
agent links, the OPL sentence is:
At least one of Safe Owner A or Safe Owner B handles Safe Opening.
Suppose an agent link to a third safe owner, Safe Owner C, is added to the fan, making f=3. The OPL
sentence then becomes:
At least one of Safe Owner A, Safe Owner B, or Safe Owner C handles Safe Opening

Logical Operators and Probabilities
## 23.4 Diverging and Converging XOR and OR Links
A converging fan is a link fan whose links point to its convergent end.
A diverging fan is a link fan whose links point to its divergent end.
Table 23.1 presents a summary of XOR and OR converging consumption and result links for f>2,
showing in the top row that a converging consumption link fan is formed when the source things are
objects and the destination thing is a process. In a converging result link fan, the source things are
processes and the destination thing is an object. Conversely, as Table 23.2 shows, when the source thing
is an object and the destination things are processes, we get a diverging consumption link fan, while
when the source thing is a process and the destination things are objects, a diverging result link fan is
formed.
Table 23.1 Summary of XOR and OR converging fans for consumption and result links

Table 23.2 Summary of XOR and OR diverging fans for consumption and result links
XOR OR
Diverging
consumption
link fan
Exactly one of P, Q , or R consumes B. At least one of P, Q , or R consumes B.
Diverging
result link
fan
P yields exactly one of A, B, or C. P yields at least one of A, B, or C.
An effect link is bidirectional, so the things linked by an effect link fan are both source and destination
at the same time, voiding the definitions of convergent and divergent link fans. Instead, as Table 23.3
shows, the distinction occurs with respect to multiple objects or multiple processes that a link fan
connects.
Table 23.3 Summary of XOR and OR joint effect link fans

Logical Operators and Probabilities
Since an enabler is an object, both agent and instrument link fans can be diverging, with multiple
processes as targets, as shown in Table 23.4, or converging, with multiple enablers as sources, as shown
in Table 23.5.
Table 23.4 Diverging agent and instrument link fans
Table 23.5 Converging agent and instrument link fans

Invocation link fans can also be diverging or converging for both XOR and OR, as shown in Table 23.6,
where the semantics of questionable combinations is specified.
Table 23.6 Invocation link fans
## 23.5 Combinatorial XOR and Combinatorial OR
The XOR and OR logic presented so far implies the selection of exactly one (for XOR) or at least one (for
OR). In cases where the fan size f > 2, we can generalize the XOR and OR logic to combinatorial XOR
and combinatorial OR logic. We extend the logic from 1 to any number m links (up to one less than f ) by
replacing “one” in the OPL sentence by m, where m < f.
## 23.5.1 Combinatorial XOR
Consider the following OPL sentence, which extends the model in Fig. 23.5.
Exactly one of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening.

Logical Operators and Probabilities
Safe can be closed or open.
Safe can be closed or open.
Exactly 2 of Safe Owner A, Safe Owner B, or Safe
At least 2 of Safe Owner A, Safe Owner B, or Safe
Owner C handle Safe Opening.
Owner C handle Safe Opening.
Safe Opening changes Safe from closed to open.
Safe Opening changes Safe from closed to open.
### Figure 23.6
Example of combinatorial XOR (left) and combinatorial OR (right)
The link fan size here is f = 3. If we want to model that exactly two safe owners are needed to open the
safe, instead of “one” we write m = 2, effectively introducing a combinatorial number of possibilities, in
this case “3 choose 2”, 3
## 2 3:
Exactly 2 of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening.
In the OPD, we add the number m outside and next to the XOR arc, as demonstrated by the number 2
recorded in the OPD on the left of Fig. 23.6.
In general, in combinatorial XOR we constrain the model to select exactly m of f links, we use the
reserved phrase “exactly m of” where m < f , and the number of possibilities is .
## 23.5.2 Combinatorial OR
Similar to the combinatorial XOR, we generalize the OR logic to combinatorial OR. We do so by
extending the logic from 1 to any number m (up to one less than f ) links by replacing “at least one of” in
an OPL sentence by “ at least m of”, where m < f. Using again the OPL sentence above, which extends
the model in Fig. 23.5, where the link fan size is f = 3, instead of “one” we can write m = 2, effectively
introducing a sum combinatorial number of possibilities.
At least 2 of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening.
In this case, the number of possibilities is 3

## 3 = 3+1=4. In the OPD, we add the number m outside
and next to the OR arc, as demonstrated by the number 2 recorded in the OPD on the right of Fig. 23.6.
In general, for constraining the model to select at least m of f links, we use the reserved phrase “at
least m of” where m < f, and the number of possibilities is 1
.

## 23.6 State-Specified XOR and OR Link Fans
Each one of the link fans described above has a corresponding state-specified version, where the source
and destination may be specific object states or objects without a state specification. Combinations of
state-specified and stateless links as destinations of a link fan may occur. Figure 23.7 shows on the left a
XOR state-specified instrument link fan and on the right an OR mixed result link fan where the links are
state-specified for objects A and C but not for B.
Exactly one of P, Q, or R requires s2 B. P yields at least one of s3 A, B, or s5 C.
### Figure 23.7
State-specified XOR (left) and OR (right) link examples
Two or more processes can have the same state as their source. For example, as the OPD on the right
hand side of Fig. 23.8 shows, either P1 or P2 (but not both) can consume B when it is at state s1: Either P1
or P2 consumes s1 B. If there are more than two processes, the OPL sentence becomes: Exactly one of P1,
P2, or P3 consumes s1 B. A similar situation occurs with state change in the OPD on the right of Fig.
23.8: Either P1 or P2 changes B from s1 to s2. And for more than two processes: Exactly one of P1, P2, or P3
changes B from s1 to s2.
### Figure 23.8
Left: P1 XOR P2 can consume B when it is at state s1. Right: P1 XOR P2 can change B from s1 to s2
## 23.6.1 Control-Modified Link Fans
Each one of the XOR link fans for consumption, result, effect, and enabling links and their state-specified
versions has a corresponding control-modified link fan: an event link fan and a condition link fan. Table

Logical Operators and Probabilities
## 23.7 presents the event and condition effect link fans, as representatives of the basic (non-state-specified)
links version of the modified link fans.
Table 23.7 Event and condition XOR effect link fans
## 23.6.2 State-Specified Control-Modified Link Fans
Each one of the control-modified link fans, except the control-modified effect link fan, has a
corresponding state-specified control-modified link fan. Since these state-specified versions are more
complicated than their non-state-specified version, Table 23.8 presents the OPD and OPL of the state-
specified cases, and below each such case—the OPL sentence for the corresponding stateless case.
Each XOR link fan in Table 23.7 and in Table 23.8 has its OR counterpart (designated by a double
dashed arc) with a corresponding OPL sentence in which the reserved phrase “at least” replaces “exactly”.
## 23.7 Multiple Control Links Have OR Semantics
Event triggers a process independently of any other event link that might be linked to the same process.
Therefore, two or more event links attached to a process have the logical OR semantics. Cancelling in
### Figure 23.9
can be initiated (triggered) by Bad Weather Forecast or by Artist Sickness. There is no need for
both to coexist. In fact, the likelihood that these two objects will be created in the system at the same
point in time is practically zero. Therefore, the OPD on the right of Fig. 23.9 is correct. The one on the
left is a case when the event that initiates the Cancelling is Bad Weather Forecast, but if that is the case,
Artist Sickness is also required. The OPD in the middle is the complementary case: the event that initiates
the Cancelling is Artist Sickness, but if that is the case, Bad Weather Forecast is also required.
In a similar way, if more than one condition link is the target of a process P with AND semantics, then
all of the conditions must be true in order for P not to be skipped. Suppose the conditions are C1, C2, and
C3. Suffice it that one condition is not fulfilled to cause P to be skipped: C1 or C2 or C3. Hence, while
the AND semantics holds from the viewpoint of the requirement for process performance, from the skip
semantics viewpoint, we are looking at OR semantics. If we want to model that any non-empty subset of
the conditions is sufficient, we need to use the OR link fan, as was done in the model in Fig. 23.5.

Table 23.8 State-specified and stateless XOR control-modified link fans
Link fan kind Event control modifier Condition control modifier
State-specified
consumption
link fan
Exactly one of P, Q, or R occurs if B is s2, in
S2 B initiates exactly one of P, Q, or R, which
which case the occurring process consumes B,
otherwise these processes are skipped.
consumes the initiated process.
The stateless case:
The stateless case:
B initiates exactly one of P, Q, or R, which
Exactly one of P, Q, or R occurs if B exists, in
which case the occurring process consumes B,
consumes the initiated process.
otherwise these processes are skipped.
State-specified
agent link fan
S2 B initiates and handles exactly one of P,
B handles exactly one of P, Q, or R if B is s2,
Q, or R.
otherwise these processes are skipped.
The stateless case:
The stateless case:
B initiates and handles exactly one of P, Q,
B handles exactly one of P, Q, or R if B exists,
or R.
otherwise these processes are skipped.
State-specified
instrument
link fan
S2 B initiates exactly one of P, Q, or R, which
Exactly one of P, Q, or R requires that B is s2,
requires s2 B.
otherwise these processes are skipped.
The stateless case:
The stateless case:
S2 B initiates exactly one of P, Q, or R, which
Exactly one of P, Q, or R requires that B is s2,
requires B.
otherwise these processes are skipped.

Logical Operators and Probabilities
### Figure 23.9
Event link has OR semantics (right) since they are unlikely to happen at the same moment
Link Probabilities and Probabilistic Link Fans
## 23.8 A process P with a result link that yields a stateful object B with n states, s1 through sn, without specifying
a particular state, as in the OPD on the left of Fig. 23.9, mean that the probability of generating B at any
one particular state shall be 1/n. In this case, the single result link to the object replaces the result link fan
to each of its states, so the OPD on the left of Fig. 23.9 is equivalent to and, being simpler than the one on
the right, is the preferred version.
In the left OPD of Fig. 23.10, the result link from P to B, which has 3 states, means that P with equal probability, Pr = 1/3, for being created at each one of the three states.
will create B
### Figure 23.10
Equivalence between result link and a set of XOR state-specified result links

P yields s1 B with probability 0.32, s2 B with
P yields A with probability 0.3, B with probability q, or sc1 C
probability 0.24, or s3 B with probability 0.44.
with probability 0.7–q.
The analogous deterministic case:
The analogous deterministic case:
P yields exactly one of s1 B, s2 B, or s3 B.
P yields exactly one of A, B, or sc1 C.
### Figure 23.11
Probabilistic state-specified object creation examples
Generally, probabilities of following a specific link in a link fan are not equal.
Link probability is an optional attribute value assigned to a procedural link in a XOR
diverging link fan that specifies the probability of following that particular link among
the possible links in the fan link.
A probabilistic link fan is a link fan with a probability value assigned to each of its
links, such that the sum of the probability values of all the links is exactly 1.
Graphically, in a probabilistic link fan, a probability value in the form , where is the link
probability numeric value or a parameter, such that ∑ 1. This symbol, which appears along
each one of the f links in the probabilistic link fan, denotes the probability that the system execution
control mechanism will select that particular link and follow that path.
The corresponding OPL sentence is the XOR diverging link fan OPL sentence without link
probabilities omitting the phrase “exactly one of…” and adding instead the phrase “…with probability ”
following each participating thing name with a probability annotation .
Figure 23.11 shows two probabilistic state-specified object creation examples and their deterministic
OPL analogues. In the OPD on the left, process P can create object B in three possible states, s1, s2, or
s3, with corresponding probabilities 0.32, 0.24, and 0.44 (totaling 1), as indicated along each result link of
the result link fan. In the OPD on the right, P can create one of the objects A, B, or sc1 C, i.e., C at state
sc1, with the probabilities 0.3, q, and 0.7–q (totaling 1), respectively.
For a process P with a result link that yields a stateful object B with states s1 through sn, and with
initial state si, P creates B at state si with probability 1. If B has m < n initial states, P shall create B at one
of the initial states with probability 1/m.
For a probabilistic result link fan, any one of the resultees may be an object without or with a specified
state. For all the link fans comprising other procedural link kinds (including those with the event and

Logical Operators and Probabilities
condition control modifiers), where the targets of the links in the link fan are processes, the source may be
an object or a specified state of an object.
### Figure 23.12
Objects with and without specified states as resultees and consumees of a probabilistic link fan
### Figure 23.13
Examples of various probabilistic state-specified change: from a state to one of two final states (left),
probabilistic result to one of three final states (middle), and probabilistic change from one state to another (right)
The OPD on the left hand side of Fig. 23.12 shows a probabilistic result link fan in which P yields one
of the objects A or B, or C at state sc1, or D at state sd1 or sd2, each with its specified probabilities. The
OPD in the middle of Fig. 23.12 shows a probabilistic consumption link fan in which A is consumed, with

specified probabilities, by one of the processes P or Q or R. The OPD in the bottom expresses the same,
with the additional fact that A must be at state s2.
Figure 23.13 presents examples of various probabilistic state-specified transformations. On the left is
a state change from a state to one of two final states. In the middle—probabilistic creation (result), and on
the right—probabilistic change from one state to another.
## 23.9 Summary
Logical operators, including AND, OR, and XOR (exclusive OR) enable modeling complex
conditions on performance of processes.
Two or more procedural links of the same kind that originate from, or arrive at, different points
along the process ellipse circumference (the process context), have the semantics of the logical
AND operator.
A link fan is a set of f ≥2 procedural links of the same kind that originate from a common point,
or arrive at a common point, on the same object or process.
The convergent end of a link fan is the end that is common to the f fan links.
The divergent end of a link fan is the end that is not common to the f fan links.
A link fan with a single dashed arc denotes the logical XOR operator.
A link fan with a double dashed arc denotes the logical OR operator.
A converging fan is a link fan whose links point to its convergent end.
A diverging fan is a link fan whose links point to its divergent end.
Each one of the XOR link fans for consumption, result, effect, and enabling links and their state-
specified versions has a corresponding control-modified link fan: an event link fan and a
condition link fan.
Link probability is an optional attribute value assigned to a procedural link in a XOR diverging
link fan that specifies the probability of following that particular link among the possible links in
the fan link.
A probabilistic link fan is a link fan with a probability value assigned to each of its links, such
that the sum of the probability values of all the links is exactly 1.
## 23.10 Problems
1. 2. Combine the two OPD in Fig. 23.1 to express that each one of the two safe owners must have all
the three keys to open the safe.
Combine the two OPD in Fig. 23.2 to express that the chef prepares either entrée or starter and
dessert, and the diner eats whatever is prepared.

3. 4. 5. 6. Logical Operators and Probabilities
In the top-left and bottom-right OPDs in Table 23.1 replace the thing manes with content that
will yield sense-making OPL sentences.
Repeat the previous question for Table 23.2.
Do the same for one OPD in each one of Tables 23.3, 23.4, and 23.5.
Chose any three OPDs from the last three questions and add probabilities to them. If needed,
modify them.
