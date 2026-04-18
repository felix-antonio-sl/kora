# Chapter 8 Abstracting and Refining
Make everything as simple as possible, but not simpler.
Albert Einstein
So far we always increased the refinement (detail) level of our model and we did it via zooming into
processes. There are cases where we need to decrease the refinement level, or, in other words, abstract the
model. This can happen when we realize that there are too many details already squeezed into a single
diagram, making it too crowded and hence less comprehensible. We do not want to delete details of the
model, as they are important for complete system specification. Yet we want then taken out of a specific
crowded diagram. We do this by creating a new OPD at an intermediate detail level by zooming out of
the too detailed OPD and creating one at a higher level of abstraction. In this chapter we focus on this
abstracting process and then discuss and improve a structural view of the system.
## 8.1 In-Zooming: Refining a Process in a New OPD
Reading carefully the sentence:
Regardless of whether the air bags deploy, the SDM [Sensing and Diagnostic Module] transmits
crash information to the vehicle's OnStar module.
It looks like airbags are not really essential in our model. However, examining the sentence further,
we notice that our model is missing a subprocess of transmitting the crash information from the Sensing
and Diagnostic Module to the OnStar Module, which apparently is another part of the ACR System located
inside the Vehicle that we have not yet modeled.
The natural place to add the OnStar Module object and the Crash Info Transmitting process is in the
OPD in Fig. 6.2, which, for the sake of convenience, is shown here again as Fig. 8.1. As we see, this OPD
is already crowded, so adding it OnStar Module as an object and Crash Info Transmitting as a fifth
subprocess inside Automatic Crash Responding would further complicate it, making it even less
comprehensible. An important objective in OPM modeling is to keep each OPD sufficiently clear and
readable in order to avoid overwhelming the diagram reader. Thus, we need to figure out a way to add the
new things without overcomplicating this or any other OPD.
Examining the four subprocesses in Fig. 8.1 we notice that the two middle ones, Message Creating
and Message Sending, are of similar nature to that of Crash Info Transmitting, the new subprocess we
wish to introduce. The solution will therefore be to merge Message Creating and Message Sending into a
new subprocess which we will call Message Handling. Then, we will zoom into this new process in a
new, separate OPD, exposing three subprocesses: Message Creating, Message Sending, and Crash Info
Transmitting. The merging of Message Creating and Message Sending results in process out-zooming, in
which two or more processes are abstracted them into a higher-level process.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 8

Abstracting and Refining
### Figure 8.1
Message Creating and Message Sending are about to be out-zoomed and replaced by Message Handling
Doing so has another advantage: in Fig. 8.2 we define an aggregate object, called In-vehicle ACR
Subsystem as a part of Vehicle. Having done this, we can now model only In-vehicle ACR Subsystem as
part of ACR System rather than modeling the entire Vehicle as part of ACR System. This new In-vehicle
ACR Subsystem object consists of OnStar Module and all the other objects inside Vehicle that are part of
the ACR System. This modification further simplifies the OPD. Figure 8.2 indeed looks simpler than its
previous version in Fig. 8.1.
This simplified version enables us to explicate the relation between Advisor and OnStar Call Center
without overcomplicating it. We add a tagged structural link with the tag operates from, yielding the
following OPL sentence:
Advisor operates from OnStar Call Center.

### Figure 8.2
Abstracting Message Creating and Message Sending from Fig. 8.1 into Message Handling. Link colors
facilitate OPD comprehension and highlight the c of instrument condition links inside the circle
## 8.2 Message Handling In-Zoomed
Figure 8.3 presents the OPD in which Message Handling is zoomed into. We rename Message Creating to
be Crash Info Creating. As the two XOR'ed event links from the moderate and severe states of Crash
Severity, this process is triggered either by a moderate or a severe crash.
Only two of the four values of are modeled in Fig. 8.3: moderate and severe. To remind the diagram
reader that there are additional values that are not shown here, the “at least one other state” symbol—a
small state symbol with ellipsis (three dots)—is added at the bottom of Crash Severity. The corresponding
OPL sentence is:
Crash Severity can be moderate, severe, or at least one other state.

Abstracting and Refining
### Figure 8.3
Zooming into Message Handling
When a process like Message Handling is in-zoomed, there are initially no internal subprocesses, so
all the procedural links that start from or end at the in-zoomed process are placed along that process
ellipse contour. As the modeler specifies the internal subprocesses, each one of these links must be
migrated (in GUI terms, its process end needs to be dragged) to the appropriate subprocess. Gradually, all
the links surrounding the parent, in-zoomed process trickle inwards until none is linked to the parent
process, as shown in Fig. 8.3. This should be done unless the link applies to all the subprocesses inside
the in-zoomed process, in which case it should be left there. A link touching the parent process is
supposed to be linked to each one of the subprocesses inside that process. An example appears in Fig. 8.2,
where crashed Vehicle is instrument to all the four subprocesses inside Automatic Crash Responding.
The Message Creating process creates the informatical object Message, which consists of two parts:
Crash Severity Info and Crash Location. Crash Severity Info is created by the Sensing and Diagnostic
Module, while Crash Location—by the GPS. These two objects are therefore modeled as instruments of
Crash Info Creating. These details of which module creates what part are not modeled at this level; they
would be shown in the next level down, when Message Creating is in-zoomed.

## 8.3 Structural View of the ACR System
As Fig. 8.5 shows, the structure of the ACR System has undergone quite a few changes. I would be
beneficial to examine the entire structure alone without any dynamic aspects of processes and state
transitions. OPCAT provides such an automatic facility. Figure 8.4 shows the automatically-generated
structural view of the ACR System, after manual rearrangements for improved readability. A four-level
hierarchy is exposed, which is also expressed in the following OPL sentences, where the indentation helps
realize the hierarchy.
ACRSystem
OnStar Call Center
In-vehicle ACR
Subsystem
GPS
Sensors Set
Cellular System
2.m
2.m
Side Sensor Front Sensor
Sensing and
Diagnostic Module
OnStar Module
Diagnostics
Unit
Accelerometer
Sensing Unit
ACR System consists of OnStar Call Center, Cellular System, GPS, and In-vehicle ACR Subsystem.
In-vehicle ACR Subsystem consists of Sensing and Diagnostic Module, Cellular System, GPS, OnStar Module,
and Sensors Set.
Sensing and Diagnostic Module consists of Accelerometer, Sensing Unit, and Diagnostics Unit.
Sensors Set consists of 2 to many Front Sensors, 2 to many Side Sensors, and Sensing Unit.
### Figure 8.4
The automatically-generated structural hierarchy of the ACR System
Examining the OPD and the corresponding OPL, two objects stick out as ones in need of remodeling:
GPS and Cellular System. The reason is that each one of these objects is part of both ACR Subsystem and
In-vehicle ACR Subsystem. However, In-vehicle ACR Subsystem is also part of ACR System. While this
is not a contradiction, it is an inconsistency, because GPS and Cellular System are both direct and indirect
parts of ACR System. As we know, neither GPS nor Cellular System in their entirety are parts of the In-
vehicle ACR Subsystem; each has components both inside and outside the vehicle.

Abstracting and Refining
ACR System
OnStar
Call Center
In-vehicle ACR
Subsystem
GPS
Cellular System
In-vehicle GPS Ex-vehicle GPS Ex-vehicle
Cell Phone
Cell System
Sensors Set
2.m
Side Sensor
2.m
Front Sensor
OnStar Module
Sensing and
Diagnostic Module
Accelerometer
Diagnostics
Unit
Sensing Unit
### Figure 8.5
The structural hierarchy of the ACR System after resolving the inconsistencies with GPS and Cellular System
The solution for this inconsistency, presented in Fig. 8.5, is to break each of these two objects into two
parts: GPS is split into In-vehicle GPS and Ex-vehicle GPS, while Cellular System is divided into Cell
Phone and Ex-vehicle Cell System. Both In-vehicle GPS and Cell Phone are parts of In-vehicle ACR
Subsystem, while Ex-vehicle GPS and Ex-vehicle Cell System are both parts of ACR System but not of
the In-vehicle ACR Subsystem.
## 8.4 Summary
While the objective of OPM-based modeling is to go top-down and refine model facts as we go,
to avoid diagram clutter it is sometimes required to abstract two or more processes in the
crowded OPD and create a new OPD at an interim level.
Abstraction can be achieved by process out-zooming: Creating an abstract process, which, when
in-zoomed, will include the out-zoomed subprocesses (and possibly others).
Right after a process is in-zoomed, all the procedural links are still attached to it.

As subprocesses are added, procedural link edges should be dragged from the in-zoomed process
ellipse to the appropriate subprocesses.
Only links that apply to all the subprocesses inside the in-zoomed process should remain
attached to the in-zoomed process.
A structural view is achieved by removing all the processes and the procedural links from the
model.
The structural view enables focusing on the system structure and examining possible structural
improvements.
## 8.5 Problems
During Sorting & Loading, the Airline Personnel carries out Baggage Sorting, changing the
Baggage Holder from security to airline. This Baggage Sorting process can result in correct or
incorrect sorting. If sorting is correct, Loading of the Baggage to the correct Aircraft takes place,
so the Baggage Location changes from origin to aircraft. Otherwise, loading of incorrectly sorted
baggage changes its Baggage Location from origin to other.
1. 2. 3. 4. 5. 6. 7. 8. 9. In the OPD SD 1.1.1 in Fig. 8.6, Sorting & Loading from Fig. 7.4 is in-zoomed. Referring to Fig. 8.6
and Fig 7.4, answer the following questions.
What is “Soring Is Correct?” what is it used for?
Correct Sort Loading is above Incorrect Sort Loading. Does this mean that the former process
will always be performed prior to the latter? Explain.
Can both Correct Sort Loading and Incorrect Sort Loading happen in the same execution of
Sorting & Loading? Explain.
Is it possible that when Baggage Location is other, the Baggage Holder is security?
Under what condition does the process Sorting & Loading takes place? Explain.
Why does only Origin Airport and not Destination Airport appear is the OPD?
In Fig. 7.4, there is a XOR relation to states aircraft and other of Baggage Location. When
Sorting & Loading is in-zoomed in Fig. 8.6, this XOR relation does not show up. Is this OK?
Explain.
Why is the XOR relation to states aircraft and other of Baggage Location needed in Fig. 7.4?
What two instrument links end at the Sorting & Loading? Explain the meaning of this, and why
Aircraft is only linked with Correct Sort Loading?

Abstracting and Refining
### Figure 8.6
SD1.1.1—Sorting & Loading in-zoomed
If the baggage is not located in the destination airport (Baggage Location is other), Lost&Found
Handling occurs. The Lost & Found Desk uses the SITA World Tracer and the IATA Tag to locate
the baggage. If it is located, Corrective Handling takes place, otherwise the passenger is
reimbursed.
In the OPD SD1.2 in Fig. 8.7, Lost&Found Baggage Handling is in-zoomed. Referring to Fig. 8.7,
answer the following questions.
10. 11. 12. 13. 14. What are the attributes of Baggage?
Under what condition does Baggage Locating happen?
What are the instruments of Baggage Locating?
What kind of thing is Baggage Located?
Can Reimbursing and Corrective Handling both happen at the same execution of Lost&Found
Baggage Handling? Explain.
15. What states of what attributes of Baggage does Corrective Handling change? From what state to
what state?

### Figure 8.7
SD1.2—Lost&Found Baggage Handling in-zoomed—the OPD obtained by zooming into the Lost&Found
Baggage Handling process in SD in Fig. 6.5
Part I was an informal introduction to OPM and SysML, in which we used a detailed case study of the
Automatic Crash Response system. We have discussed aspects of OPM and various SysML diagram
kinds. Part II provides a more formal and theory-grounded exposure of OPM and SysML. It covers in an
orderly fashion the ontology, conceptual modeling constructs, and applications. Chapter 9 introduces and
defines what conceptual modeling is and what is its purpose and context. Chapter 10 presents the two
basic building blocks of OPM—objects and processes. In a similar fashion to the way Part I is structured,
Chap. 11 is about the textual modality of OPM—OPL. In Chap. 12 we turn to an orderly study of SysML
with its four pillars and nine kinds of diagrams. The dynamic, time-dependent aspect of systems is the
focus of Chap. 13. This is naturally followed by studying the structural, time-independent system aspect
in Chap. 14. Following Chap. 15, which deals with participation constraints and fork links, in Chap. 16
we introduce the four fundamental structural relations. This concludes Part II. In Part III, titled Structure
and Behavior—Diving In, we turn to elaborate on each of the four fundamental structural relations
separately and continue with whole system aspects, including complexity management and control.
