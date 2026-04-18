# Chapter 1 Ready to Start Modeling?
…all models are wrong; the practical question is how wrong do they have
to be to not be useful.
Box and Draper (1987)
With diagrams the meaning is obvious, because once you understand how
the basic elements of the diagrams fit together, the meaning literally
stares you in the face.
Steve Cook (1999)
We live in a world of interconnected systems. In fact, as humans, each of us is a highly complex system
living in a host of socio-political-technological systems that are no less complex. In order to understand and
design complex systems, it is necessary to have a methodology and a language for building models that can
express what these systems do, why they do it, how they do it, and what they need in order to do it. While
the visual and intuitive nature of diagrams has made them widely used means for building models of
systems, natural language text is also an important way of conveying complex ideas. Formal diagrams are a
graphic language in that they contain interconnected symbols, expressing meaningful facts and statements
about the world. Combining graphics with text reinforces our ability to specify complex ideas in science and
engineering.
## 1.1 The Automatic Crash Response System
We introduce conceptual modeling using OPM, and later SysML, using a running example of specifying the
GM OnStar Automatic Crash Response (ACR) system. The specification that we model provided below
was taken almost literally from an early version of OnStar Technology’s description on the OnStar company
website.

OnStar’s in-vehicle safety, security, and information services use Global Positioning System (GPS)
satellite and cellular technology to link the vehicle and driver to the OnStar Center. At the OnStar
Center, advisors offer real-time, personalized help 24 hours a day, 365 days a year. …
The accelerometer located within the Sensing and Diagnostic Module (SDM) measures the crash’s
severity. In the event of a moderate-to-severe frontal or side-impact crash, data is transmitted
from the affected sensors to the SDM. The SDM sensor also can identify a rear impact of
1http://cms.cerritos.edu/auto/basic-its/ost.htm.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_1

Ready to Start Modeling?
sufficient severity. Regardless of whether the air bags deploy, the SDM transmits crash
information to the vehicle’s OnStar module.
Within seconds of a moderate-to-severe crash, the OnStar module will send a message to the
OnStar Call Center (OCC) through a cellular connection, informing the advisor that a crash has
occurred. A voice connection between the advisor and the vehicle occupants is established. The
advisor can then conference in 911 [emergency] dispatch or a public safety answering point
(PSAP), which determines if emergency services are necessary. If there is no response from the
occupants, the advisor can provide the emergency dispatcher with the crash information from
the SDM that reveals the severity of the crash. The dispatcher can identify what emergency
services may be appropriate. Using the Global Positioning System (GPS) satellite, OnStar advisors
are able to tell emergency workers the location of the vehicle.
The “big picture” that emerges from this system description is that the ACR system aims to provide
an automatic response in case of a severe car crash. In the following sections we methodically model this
system using OPM and then SysML.
## 1.2 The Function-as-a-Seed OPM Principle
In order to start an OPM model of a system, the first step is to determine the function of the system. The
function is the main process of the system, which is designed to deliver value—benefit at cost—to the
system beneficiary. The system beneficiaries are the person or people who get value from using the system.
Identifying the system’s function is critical, as it expresses the motivation for engineering the system. This
function will be the top-level process of our OPM model. Determining the system’s function is not just
important and recommended, it is also a basic principle, known as the function-as-a-seed OPM principle:2
The Function-as-a-Seed OPM Principle
Modeling a system starts by defining, naming, and depicting the function of the system, which is
also its top-level process.
The term “function-as-a-seed” underscores the centrality of starting off the modeling process in a way
that focuses on the function of the system; that is, the value that the system provides to its beneficiary. As
the next few chapters show, this function is the seed from which the entire model gradually evolves. This
guideline may be counterintuitive, since many engineers tend to start with the form—the objects, the
substance of which the system is comprised—rather than the function, which is the process due to which
beneficiaries would use the system in the first place. Function delivers value, while form draws cost that
must be paid to achieve that system’s function.
Given the centrality of the system’s function, it is worth contemplating what this function really is and
what it should best be called so everybody involved in the modeling will be on the same page. An
appropriate function clarifies and emphasizes the central goal of the system being modeled. Deliberation
2This is the first of 13 OPM principles, which are listed throughout the book in a frame and also appear at the end of
the book for quick reference after Chap. 24 under the heading “OPM Principles at a Glance”.

regarding the function often provokes a debate between the system architecture team members at this
early stage, but this is highly valuable. Such discussions frequently expose differences and often even
misconceptions among the participants regarding the system that they set out to architect, model, and
design. Thus, agreement on the system’s function and its most appropriate name increases the likelihood
of ending up with a useful model.
## 1.3 Identifying the System’s Function
The OnStar system description above makes it clear that the main function of the system—its purpose and
the value it delivers—is to automatically provide response in case of a car crash. Therefore, we call this
function Automatic Crash Responding, and this is the top-level process of the system we are about to start
modeling. OPM has just one type of diagram, which is called the object-process diagram (OPD). Any OPD
is built using two OPM building blocks: objects and processes.
An object is a thing that exists or might exist.
While objects exist, processes happen or occur, and they transform objects by generating, consuming,
or affecting them.
A process is a thing that transforms an object.
Collectively, objects and processes are called things.
A thing is an object or a process.
We start by modeling the system diagram—the top-level object-process diagram (OPD)—in our OPM
model. The OPM symbol for a process is an ellipse with the process name recorded within it.
### Figure 1.1
Automatic Crash Responding modeled as a process

Ready to Start Modeling?
Figure 1.1 describes the Automatic Crash Responding process in OPM notation using OPCAT,3 an
OPM-based modeling software environment such as OPCAT (Dori et al. 2003). It is highly recommended
that the reader installs OPCAT and follows the modeling activities presented here.
Based on the definition of a process as a thing that transforms an object, no process is meaningful
unless it transforms at least one object. That object is known as the transformee of the transforming
process or the operand of the system’s function.
## 1.4 Identifying the System’s Beneficiary
A man-made, artificial system is designed to benefit at least some of its stakeholders. The stakeholders that
benefit are the system’s beneficiaries. The beneficiary of the Automatic Crash Responding process, which is
also the transformee in our case, is the driver and any additional passengers who occupy the crashed vehicle.
This group of people is the object Vehicle Occupants Group. Figure 1.2 shows the OPD of Fig. 1.1 updated
with this object. The OPM symbol for object is a rectangle with the object name recorded within it. This is
also the standard symbol used in UML—the Unified Modeling Language (OMG UML 2011I, 2011S)—and
SysML, where it is referred to as a block.
### Figure 1.2
Vehicle Occupants Group is added as an object to the Automatic Crash Responding process
## 1.5 A Process Transforms an Object
We have defined an object as a thing that exists or might exist. Our object, the Vehicle Occupants Group,
does exist, as it did prior to the occurrence of the Automatic Crash Responding process. So what
3The object-process diagrams (OPDs) in this book were drawn using OPCAT, a software environment that enables
OPM-based modeling. OPCAT can be downloaded and installed free from http://esml.iem.technion.ac.il/, a website
that also contains an OPCAT hands-on tutorial and many articles on OPM. OPCAT tutorial is also found on that site.

transformation does the Vehicle Occupants Group undergo? To answer this question, we examine the
following definition of transformation.
Transformation is the creation (generation, construction) or consumption
(elimination, destruction) of an object or an effect (change of state) of an existing
object.
In our case, the state of the Vehicle Occupants Group has clearly changed. In other words, the Vehicle
Occupants Group has been affected by, and consequently benefited from, the occurrence of the
Automatic Crash Responding process. To express the fact that the Automatic Crash Responding process
affects (changes the state of) the Vehicle Occupants Group object, we insert a link between the process
and the object. The link, shown in Fig. 1.3, is the effect link—a bidirectional arrow, —between the
affecting (state-changing) process and the affected object; that is, the object whose state has changed as a
result of the process occurring.
### Figure 1.3
An effect link is added between the Automatic Crash Responding process and the Vehicle Occupants
Group object, indicating that the process affected (changed the state of) the object
Our model currently contains three elements. The first is the Automatic Crash Responding process,
the second is the object Vehicle Occupants Group, and the third is the link between the process and the
object.
## 1.6 Summary
We have started modeling the Automatic Crash Responding system using OPM.
OPM has a single diagram type: the object-process diagram (OPD).
OPM is built of objects, which exist, and of processes, which transform objects.
Object transformation is object creation, object consumption, or object change.

Ready to Start Modeling?
We recognize processes—Automatic Crash Responding in our example—as stand-alone OPM
building blocks that are separate from objects.
Objects and processes enable concurrent modeling of the system’s structure and behavior in the
same OPD.
Transformation is object creation, consumption, or state change.
## 1.7 Problems
An engineering student was asked to sketch a graphical representation of the system of garbage recycling
came up with the sketch in Fig. 1.4.
### Figure 1.4
The Recycling System—a graphic representation
1. 2. 3. 4. What things in the sketch represent objects?
What things in the sketch represent processes?
What elements in the sketch represent relations?
Are there concepts in the sketch that do not fall in any of the above categories? If so what are
they? What should they be called?
The baggage handling system case study that we start evolving below will serve as the basis for
problems at the end of each chapter. You can do the modeling manually, but it is strongly advised
that you use an OPM modeling software package such as OPCAT (downloadable from
http://esml.iem.technion.ac.il/).
A passenger arriving at an airport deposits her baggage with the airline she is flying with. A
baggage handling system manages the transfer of the baggage to the passenger’s destination.
5. 6. 7. What is the function of the system? Phrase it as an OPM process name.
Draw the function as the main process in a new OPD.
Identify the main beneficiary of the system.

8. Add the beneficiary to the OPD as an object and link it to the process defined as the system’s
9. 10.
function.
Identify the operand of the system’s function.
Add the operand to the OPD and link it to the process.
Identify other main objects that the process affects, add them to the OPD, and link them to the
process.
