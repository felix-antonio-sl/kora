# Chapter 22 OPM Operational Semantics and
Control Links
Control Flow Semantics presents a unified, formal treatment of the semantics of a
wide spectrum of control flow notions as found in sequential, concurrent, logic,
object-oriented, and functional programming languages.
de Bakker and de Vink (1996)
To control the flow of system execution, OPM has precise operational semantics, based on the event-
condition-action paradigm and expressed by modifying the procedural links with control modifiers—
event and condition symbols. This is the focus of this chapter.
## 22.1 The Event-Condition-Action Control Mechanism
The OPM process activation mechanism is the way OPM deploys the event-condition-action (ECA)
paradigm, mentioned in Dittrich et al. (1995) to structure active rules in event driven architecture and
active database systems. ECA follows the rule “On event if condition then action,” namely, if an event
occurs, and an associated condition is fulfilled at the time of the event occurrence, then the associated
action is triggered. In OPM terminology, action is an OPM process. Such a rule traditionally consisted of
three parts, which are listed below along with their OPM interpretations.
The event part specifies the object—the trigger, or the object’s state or value that triggers the
process.
carried out; in OPM the condition is evaluated on the preprocess object set.
The ECA paradigm provide the basis for OPM operational semantics and flow of execution control.
At the point in time of object creation, or appearance of the object from the system’s perspective, or
entrance of an object to a particular state, an event occurs.
The object or object state involved in the event can be the source of a procedural link. At runtime, i.e.,
at the instance level during the system’s execution, the occurrence of that event initiates evaluation of the

The condition part is a logical test that, if satisfied or evaluates to true, enables the action to be
The action part consists of updates or invocations on the local data; in OPM this amounts to
activating the process, which, upon completion, transforms one or more objects.
An event is a point in time at which something significant to the system execution
happens.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

OPM Operational Semantics and Control Links
precondition for every process to which the object is a source of the link, and the event ceases to exist. If
and only if the evaluation reveals satisfaction of the precondition, then the process starts executing.
Events can occur also through the end of a subprocess inside an in-zoomed process, as well as through
invocation link and exception link, which occur between processes. Thus, according to the event-
condition-action paradigm, starting the performance of a process (the “action”) has two prerequisites: (1)
an initiating event (the “event”), and (2) satisfaction of a precondition (the “condition”). Events and
preconditions in concert specify OPM flow of execution control for process performance. The flow of
execution control is the consequence of successive event-condition-action sequences that begin with
initiation of the system function by an external event and end when the system function either completes
executing successfully or terminates abnormally.
## 22.2 Precondition, Preprocess and Postprocess Object Sets
Every process has a preprocess object set with at least one object, possibly in a specified state. The
preprocess object set of a process determines the precondition that must be satisfied before performance
of that process starts. The preprocess object set may simply include the existence of one or more objects,
possibly in specified states, but it can also be complex and include compound logical expressions using
logical AND, OR, and XOR operators. Typical objects in a preprocess object set are transformees—
consumees and/or affectees, and enablers. Some of these objects may have a further stipulation regarding
flow of execution control, expressed as a condition link, which, as explained below, provides for skipping
the process if its precondition is not satisfied.
The postprocess object set determines the process postcondition that the process completion satisfies.
Typical objects in a postprocess object set are resultees and affectees.
The intersection of the preprocess object set and the postprocess object set of the same process
includes the process enablers and affectees. Consumees are only members of the preprocess object set,
while resultees are only members of the postprocess object set.
The involved object set is the union of the preprocess and postprocess object sets. If the involved
object set has only one object, it must be a transformee, otherwise it does not conform to the OPM
definition of process as a thing that transforms at least one object. Therefore, in a complete OPM model,
each process must be linked with at least one transformee, and an OPM modeling tool should check this
as a basic part of its model validation.
## 22.3 Kinds of Control Links
As part of the event-condition-action paradigm underlying OPM’s operational semantics, an event link, a
condition link, and an exception link express an event, a condition, and a time exception, respectively.
These three link kinds are OPM’s control links. Control links occur either between an object and a
process or between two processes.

Event and condition links do not exist independently. Rather, they are modified versions of the
various procedural links. Each procedural link from an object or a state to a process (i.e., object or state in
the preprocess object state) has a corresponding event link and a corresponding condition link.
A control modifier is one of the two letter symbols e and c, added to a procedural link,
which add to the semantics of that link the event and condition semantics, respectively.
A control link is a procedural link with the addition of a control modifier.
There is no result event link or result condition link, since these are outgoing procedural links, relating
to the postprocess object set. When a process completes, it creates the postprocess object set without
further condition. Hence, assuming that the process terminates successfully, creation of resultees and
change of affectees are automatic and unconditional.
## 22.4 Event Links
A process event semantics is the initiation of that process, which triggers evaluation of
that process’ precondition.
An event link is a procedural link with the control modifier e, indicating the addition
of event semantics to the link’s destination process.
An event link specifies a source event and a destination process—the process that is initiated upon the
event occurrence. The event occurrence triggers evaluation of the process’ precondition. Satisfying the
precondition allows process performance (execution) to proceed, rendering the process active. If the
process precondition is not satisfied, then process performance shall not occur. Regardless of whether the
evaluation is successful or not, being a point in time, the event is lost. If the process precondition is not
satisfied, process initiation shall not occur until another event activates the process.
## 22.4.1 Initiating a Non-first Subprocess via an Event Link
If an event link is attached to a process P, and P is in-zoomed, like all the other procedural links attached
to P, the event link migrates automatically to the first (top-most) subprocess—the one that executes first.
The modeler must be very cautious when modeling an event link that is attached to any subprocess other
than the first one, because this is akin to interfering with the inner operation of a black box! While trying
to trigger a non-first subprocess, one or more of that subprocess’ preconditions may not be met because
previous subprocesses were skipped. For example, if in Fig. 6.2 the event link is attached to Message
Creating rather than to Crash Severity Measuring, the latter process is skipped, so Crash Severity remains
none, and therefore Message Creating will be skipped too. Moreover, since there is no Message, Help
Sending is also skipped, leaving Vehicle Occupants Group at their initial possibly injured state, rather
than being helped.

OPM Operational Semantics and Control Links
## 22.4.2 Enabling and Transforming Event Links
There are two kinds of transforming event links (Table 22.1) and two enabling event links (Table 22.2).
Table 22.1. Enabling event link summary
Name Semantics Sample OPD & OPL Source Destination
Agent
event link
The agent—a human—both
initiates and enables the
process. The agent must be
present throughout the
process duration.
initiating
agent
initiated
process
Miner initiates and handles Copper
Mining.
Instrument
event link
The object initiates the
process as an instrument, so
it does not change, but it
must exist throughout the
process duration.
initiating
instrument
initiated
process
Drill initiates Copper Mining, which
requires Drill.
Table 22.2. Transforming event link summary
Name Semantics Sample OPD & OPL Source Destination
Consumption
event link
The object initiates the process,
which, if performed, consumes
the object. initiating
consumee
Food initiates Eating, which
initiated process,
which consumes
the initiating
consumee
consumes Food.
Effect event
link
The object initiates the process,
which, if performed, affects the
object. The event link is the
link from the object to the
process; the link from the
process to the object is not an
event link.
initiating
affectee
is abstracted as:
initiated process,
which affects the
initiating affectee
Copper initiates Purifying,
which affects Copper.

## 22.4.3 State-Specified Enabling and Transforming Event Links
Table 22.3 describes the two state-specified enabling event links—one for agent, the other for instrument.
There are four kinds of state-specified transforming event links. These are summarized in Table 22.4.
Table 22.3 State-specified enabling event link summary
## 22.4.4 Invocation Links
Process invocation is an event by which a process initiates a process. An invocation link connects a
source process to the destination process that it initiates, signifying that when the source process
completes successfully, it immediately initiates the destination process—the process at the destination end
of the invocation link. In a normal or expected flow of execution control, the source process does not
initiate the new process if the former does not complete successfully. It is up to the modeler to take care
of modeling what should happen with any process that aborts, e.g., due to a time exception.
Since by definition an OPM process transforms an object, the invocation link semantically implies the
creation of an interim object by the invoking source process that the subsequent invoked destination
process immediately consumes. As discussed in Sect. 10.10.3 in an OPM model, an invocation link may
replace a transient, short-lived physical or informatical object that a source process creates to initiate the
destination process, which immediately consumes the transient object. The physical object Spark in Fig.
## 10.11 is one example; Record ID in a query is another.

OPM Operational Semantics and Control Links
Graphically, a lightening symbol jagged (and possibly curved) line from the invoking source process
to the invoked destination process ending with a closed arrowhead at the invoked process denotes an
invocation link. This is the symbol of the common invocation link.
Table 22.4 State-specified transforming event link summary

Table 22.5 Invocation link summary
There is a second kind of invocation link—self-invocation link, which enables modeling invocation of
a process by itself: Upon process completion, the process immediately invokes itself. A self-invocation
link is symbolized by a pair of invocation links, originating at the process and joining head to tail before
ending back at the original process shall denote the self-invocation link. Invocation links are summarized
in Table 22.5. If a waiting period is needed between two consecutive invocations, a Waiting process with
specified time constraints (see below) can be inserted as a destination from the invoking process and as a
target back to the same process. An invocation link from the last subprocess to its parent in-zoomed
process can be used to create loops.
## 22.5 Condition Links
A process condition semantics is skipping the execution of that process if its
precondition is not met.
A condition link is a procedural link with the control modifier c, indicating the
addition of condition semantics to the link’s destination process.
A condition link provides a bypass mechanism, which enables system execution control to skip, or
bypass, the destination process if its precondition satisfaction evaluation fails. Without the condition link
bypass mechanism, failure to satisfy the precondition causes the process to wait for another event.

OPM Operational Semantics and Control Links
Upon the arrival of the new event, that process precondition is evaluated again, and if it is satisfied,
the process starts executing, otherwise it is again waiting for the next event. This can cause the control to
get stuck indefinitely in that process in an infinite loop. Using the condition link prevents such situations.
As discussed in Sect. 21.17, as is the case with all control links, if a condition link is attached to a
process P, and P is in-zoomed, the condition link migrates automatically to the first subprocess (or two or
more first concurrent subprocesses) of P. The modeler may move the link from that first subprocess to
another subprocess or add another link from the same source to one or more subprocesses other than the
first one.
## 22.5.1 Skipping Takes Precedence Over Waiting
A preprocess object set may include both condition links and non-condition links, i.e. procedural links
without the condition control modifier. The distinguishing aspect of condition links is their skip
semantics—skipping or bypassing a process if the source object operational instance of the condition link
does not exist or is not a the required state. Without the condition control modifier, the non-existence of
an operational instance of the procedural link source object causes the process to wait for another event
and operational instances of all source objects to exist, possibly in a specified state, thus satisfying the
precondition.
Meeting all the conditions associated with all the objects or states in the preprocess object set
connected with condition links is necessary to satisfy the precondition and start the process. If the
preprocess object set has one or more objects or states connected with non-condition links and one or
more objects or states connected with condition links, a conflict may arise between the wait semantics
induced by the non-condition link(s) and the skip semantics induced by the condition link(s). To resolve
the conflict, the skip semantics is defined to be stronger than wait semantics, as stated by the following
skip semantics precedence OPM principle.
The Skip Semantics Precedence OPM Principle
Skip semantics takes precedence over wait semantics.
Even if just one of the conditions associated with the condition links connecting with the process does
not exist, the precondition satisfaction evaluation shall fail, execution control skips the process, and an
event occurs that initiates the next sequential process (or the next two or more parallel processes).
Conditions associated with condition links are the first to be considered during precondition
evaluation, because if they are not met, the process being considered for execution is skipped, regardless
of the evaluation result of the remaining part of its precondition. If the skipped process is within an in-
zoom context and there is a subsequent process in this context, execution control initiates that next
process, otherwise execution control transfers back to the in-zoomed process.
There are two kinds of basic condition links: condition transforming links and condition enabling links.
## 22.5.2 Condition Transforming Links
A condition consumption link connects a consumee to a process with the addition of the control modifier
c. Table 22.6 summarizes the basic condition transforming links.

Table 22.6 Condition transforming link summary
Name Semantics Sample OPD & OPL Source Destination
Condition
consumption
link
If an object instance
exists and the rest of the
process precondition is
satisfied, then the
process performs and
consumes the object
instance, otherwise
execution control
advances to initiate the
next process.
Conditioning
object
Conditioned
process
Process occurs if Object exists, in
which case Process consumes
Object, otherwise Process is
skipped.
Condition
effect link
If an object instance
exists and the rest of the
process precondition is
satisfied, then the
process performs and
affects the object
instance, otherwise
execution control
advances to initiate the
next process.
Conditioning
object
Conditioned
process
Process occurs if Object exists, in
which case Process affects
Object, otherwise Process is
skipped.
If at runtime (i.e., during execution of the system model) a consumee instance exists when an event
initiates the process, then the presence of that consumee instance satisfies the process precondition with
respect to that object. If evaluation of the entire precondition, which accounts for the entire preprocess
object set (of which the consumee is a part) is satisfied, the process starts and consumes that consumee
instance. However, if a consumee instance does not exist when an event initiates the process, then,
regardless of the rest of the preprocess object set, the process precondition evaluation fails, and the flow
of execution control bypasses (skips) the process without executing that process.
A condition effect link like its regular, non-condition effect link counterpart, connects an affectee to a
process, with the addition of the control modifier c. If at runtime an affectee instance exists when an event
initiates the process, then the presence of that affectee instance satisfies the process precondition with
respect to that object. As with the condition consumption link, if evaluation of the entire precondition,
which accounts for the entire preprocess object set (of which the affectee is a part) is satisfied, the process
starts and affects that affectee instance, but if not, then the process precondition evaluation fails, and the
flow of execution control bypasses the process without executing that process.
## 22.5.3 Condition Enabling Links
There are two kinds of basic (non-state-specified) condition enabling links: condition agent link and
condition instrument link. A condition agent link is an agent link from an agent to a process with the

OPM Operational Semantics and Control Links
addition of the control modifier c. If at runtime an agent instance exists when an event initiates the
process, then the presence of that agent instance satisfies the process precondition with respect to that
object. If evaluation of the remaining precondition is satisfied as well, the process starts and that agent
handles its performance. However, if an agent instance does not exist when an event initiates the process,
then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’ the
process without process performance.
A condition instrument link is an instrument link from an instrument to a process, annotated with the
control modifier c. If at runtime an instrument instance exists when an event initiates the process, then
the presence of that instrument instance satisfies the process precondition with respect to that object. If
evaluation of the entire preprocess object set satisfies the precondition, the process starts. However, if an
instrument instance does not exist when an event initiates the process, then the process precondition
evaluation fails and the flow of execution control bypasses, or ‘skips’ the process without process
performance (Table 22.7).
Table 22.7 Condition enabling link summary
Figure 22.1 is an OPD with a condition instrument link from Nearby Mobile Device to Cellular
Network Signal Amplifying, which occurs only if an environmental object Nearby Mobile Device exists
and is otherwise skipped, as there is no point in amplifying if no device is nearby. Table 22.6 summarizes
the basic condition transforming links.

### Figure 22.1
Condition instrument link (with partial OPL)
## 22.5.4 Condition State-Specified Transforming Links
Like their event state-specified transforming link counterparts, there are four kinds of condition state-
specified transforming links. These are summarized in Table 22.8.
## 22.5.5 Condition State-Specified Enabling Links
Like their regular, non-state-specified counterparts, there are two state-specified enabling links: state-
specified agent link and state-specified instrument link.
A condition state-specified agent link is a state-specified agent link, annotated with the control
modifier c, from a specified state of an agent to a process. If at runtime an instance of the agent exists, or
is present, at the specified state when an event initiates the process, then this satisfies the process
precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the
precondition, the process starts and that agent has to be present to handle it until it ends. Otherwise, the
process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, performing
the process.
A condition state-specified instrument link is a state-specified instrument link,
annotated with the control modifier c, from a specified state of an instrument to a
process.

Name Condition
state-
specified
consumption
link
Condition
input-
output-
specified
effect link
Condition
input-
specified
effect link
OPM Operational Semantics and Control Links
Table 22.8 Condition state-specified transforming link summary
Semantics Sample OPD & PL Source Destination
The process performs
if the object is in the
state from which the
link originates,
otherwise the process
is skipped. conditioning
specified
state of the
object
conditioned
process
Testing occurs if Raw Material Sample is
pre-approved, in which case Raw
Material Sample is consumed, otherwise
Testing is skipped.
The process performs
if the object is in the
input state (from
which the link
originates) and
changes the object
from its input state to
its output state,
otherwise the process
is skipped.
conditioning
specified
input state
of the object
conditioned
process
Testing occurs if Raw Material is pre-
tested, in which case Testing changes
Raw Material from pre-tested to tested,
otherwise Testing is skipped.
The process performs
if the object is in the
input state (from
which the link
originates) and
changes the object
from its input state to
any one of its states,
otherwise the process
is skipped.
conditioning
specified
input state
of the object
conditioned
process
Delivery Attempting occurs if Message is
created, in which case Delivery
Attempting changes Message from
created, otherwise Delivery Attempting
is skipped.
Dori – Model-Based Systems Engineering with OPM and SysML
Condition
output-
specified
effect link
The process performs
if the object is in the
input state (from
which the link
originates) and
changes the object
from its input state to
any one of its states,
otherwise the process
is skipped.
conditioning
object
Stress Testing occurs if Suspicious
Component exists, in which case Stress
Testing changes Suspicious
Component to stress-tested, otherwise
Stress Testing is skipped.
Table 22.9 Condition state-specified enabling link summary

conditioned
process

OPM Operational Semantics and Control Links
If at runtime an instance of the instrument exists and is at the specified state when an event initiates
the process, then the process precondition is satisfied with respect to that object. If evaluation of the entire
preprocess object set satisfies the precondition, the process starts and that instrument must remain existent
and at the same state throughout the duration of the process
If at runtime an instance of the instrument does not exist or exists at a different state than the one
attached to the link source, then the process precondition with respect to that object is not satisfied, the
process precondition evaluation fails, and the flow of execution control bypasses performing the process.
Table 22.9 summarizes the condition state-specified enabling links.
## 22.6 Exception Links
Exception links enable modeling what to do in case of exception in the time execution of a process below
a minimal threshold or above a maximal one.
## 22.6.1 Process Time Duration and Its Distribution
Process may have a Duration property (metamodel attribute) with a value expressed in time units, which
shall be compatible with ISO 80000-3:2006—Quantities and units—Part 3: Space and time, which is part
of the group of ISO/IEC 80000 standards that form the International System of Quantities. Units of time
can be milliseconds [ms], seconds [sec], minutes [min], hours [hr], days [dy], weeks [wk], months [mo], or
years [yr]. Duration may specialize into Minimal Duration, Expected Duration, and Maximal Duration.
Minimal Duration and Maximal Duration designate the minimum and maximum allowable time for process
completion. Time duration is an optional, and, as Fig. 22.2 shows, the modeler can choose to indicate
only the expected (nominal) time, minimal and maximal, or all three durations.
### Figure 22.2
Three ways to indicate process duration: Left—expected (nominal) time only, middle—minimal and maximal,
right—minimal, expected, and maximal time durations
The value of the process’ Expected Duration is the statistical mean of the duration of that process.
Duration optionally exhibits the Duration Distribution attribute with a value identifying the name and
parameters for a probability distribution function associated with the process duration or a non-analytical
distribution. At run-time, the value of Duration is determined separately for each process instance (i.e., for
each individual process occurrence) by sampling from the process Duration Distribution. The Duration
property provides for defining exception links. There are two kinds of exception link: overtime exception
link and undertime exception link.

## 22.6.2 Overtime Exception Link
The overtime exception link connects the source process with a destination overtime handling process to
specify that if at runtime, the performance time of the source process instance exceeds its Maximal
Duration value, then an event initiates the destination process, which is an overtime handling process.
A maximal-timed process is a process for which the modeler determines a maximal
duration.
An overtime handling process is a time exception process that determines what to do
in case the time performance of a maximal-timed process exceeds its maximal
allowable time.
An overtime exception link is a procedural link from a maximal-timed process to an
overtime handling process, indicating that if the duration of a maximal-timed process
exceeds its maximal duration, then the overtime exception process is initiated.
The control modifier for the overtime exception link is a single slanted short bar crossing the link near
the overtime exception process (see Fig. 22.3 for the control modifier of the undertime exception link,
which is a pair of such bars).
## 22.6.3 Undertime Exception Link
The undertime exception link connects the source process with a destination undertime handling process
to specify that if at runtime the performance time of the source process instance is below its Minimal
Duration value, then an event initiates the destination process, which is an undertime handling process.
A minimal-timed process is a process for which the modeler determines a minimal
duration.
An undertime handling process is a time exception process that determines what to do
in case the time performance of a minimal timed process falls short of its minimal
duration.
An undertime exception link is a procedural link from a minimal-timed process to an
undertime exception process, indicating that if the time performance of a timed
process falls short of its minimal allowable time, the undertime exception process is
initiated.
The control modifier for the undertime exception link is a pair of parallel slanted close short bars
crossing the link near the overtime exception process. Figure 22.3 is an example of Undertime Exception
Handling. Here, {instance id=2} is a particular instance (occurrence) of Processing, whose Duration is 3.4
min. Since this value is less than 30.0 min—the minimal time duration defined for the process class
Processing, Undertime Exception Handling takes place.

OPM Operational Semantics and Control Links
### Figure 22.3
Undertime exception example
A source process may have both overtime and undertime links, each connected to a different
destination time exception handling process. Suppose in the example in Fig. 22.3 we add an Overtime
Exception Handling process, then the additional OPL sentence would be:
Overtime Exception Handling occurs if duration of Processing exceeds 60.0 min.
Unlike most procedural links, which connect an object and a process, but similar to the invocation
link, the two time exception links are procedural links that connect two processes directly. An implicit
interim object Overtime Exception Message or Undertime Exception Message is created by the OPM’s
process execution mechanism upon realizing that the process failed to terminate by the maximal allotted
time or ended prematurely, falling short of the minimal allotted time, respectively. Since the OPM
operational mechanism creates and immediately consumes these objects, their depiction is not explicit in
the model. This is similar to the invocation link, which suppresses the creation of an interim object by the
source process and its immediate consumption by the destination process. Table 22.10 summarizes the
two time exception links.
The exceptions these links handle relate only to time, but they can also be used for modeling
execution exceptions. For instance, if a process with minimal time duration attached to an undertime
exception link is skipped, which means its duration was 0, then the exception handling process is
initiated.
## 22.7 Transformation Rate
Often the need arises to model consumption of a consumee or effect on an affectee or creation of a
resultee not as a one-time event but rather as a continuous process or a discrete process with a quantity
larger than 1, transformed over time. We have defined property as an attribute of an OPM element. For
example, Perseverance is a property of OPM Thing. If the value of that property is persistent, the Thing
is an Object; if it is transient—it is a Process. In other words, we can say that a property is an attribute at
the metamodel level, where Thing and Link are OPM Elements. Perseverance is an example of a property
of a Thing. Transformation Rate is a property of a (transforming) Link.

Table 22.10 Time exception links summary
Transformation rate is a property of a procedural link connecting a transformee B
and a process P whose value is the rate of transformation of B by P.
Just as transformation specializes into consumption, effect, and result, so does transformation rate.
Consumption rate is the transformation rate of a consumption link connecting a
consumee B and a process P whose value is the rate of consumption of B by P.
Yield rate is the transformation rate of a result link connecting a resultee B and a
process P whose value is the rate of creation of B by P.
Effect rate is the transformation rate of an effect link connecting an affectee B and a
process P whose value is the rate of affecting B by P.

OPM Operational Semantics and Control Links
### Figure 22.4
Consumption rate and yield rate example
Effect rate can be expressed more specifically as state change rate.
State change rate is the transformation rate of an in-out link pair whose input and
output links connect the input state bi and output state bo of an affectee B to a process
P, whose value is the rate of changing the state of B by P from bi to bo.
Figure 22.4 provides an example of consumption rate and yield rate. The modeler may create an
exception if the quantity of the resultee or the consumee is less than the rate times the expected process
duration.
## 22.8 Computing with OPM
OPM models can be used to carry out numeric calculations. The atomic processes for calculations are the
four basic arithmetic operations Adding, Subtracting, Multiplying, and Dividing. These are used to devise
more involved calculations such as Averaging, Geometric Mean Computing, etc. Care must be exercised
with operations that are not commutative, like Dividing, where the roles of the Dividend and the Divisor
must be explicit in order to get the correct Quotient. Since the mathematical expressions are much more
compact and understood, once a sufficiently low level of computing is reached, the actual formulae can
be recorded as parts of the calculating process names.
As an industrial example, suppose for the system in Fig. 22.4 we wish to compute the value of
residue—the final value of Length of Steel Rod in meters after it has been cut. This is modeled in Fig.
## 22.5 by the process Residue Length Computing and Fig. 22.6, where Residue Length Computing is in-
zoomed. The initial Length of the Steel Rod, il, is 3.00 m. The Machining process, which lasts 3 hr,
consumes the Steel Rod at a consumption rate of 0.66 m/hr.

### Figure 22.5
SD of the Machining system with Residue Length Computing as an operation of Machining
### Figure 22.6
SD1 of the Machining system from Fig. 22.5, in which Residue Length Computing is in-zoomed

OPM Operational Semantics and Control Links
The Machining process generates Shaft at a yield rate of 3 units/hr, therefore in 3 hours we get 9
Shafts, as indicated by the participation constraint near Shaft. The length of each Shaft is 0.22 m and the
Size of the Shaft Batch (cut during 3 hr) is 9. All these data are provided in the model in Fig. 22.5.
Zooming into Residue Length Computing in Fig. 22.6, we see that it has two subprocesses. The first is
Used Length Computing (u=s*l) and the second—Residue Computing (residue=il–u). The names of the
processes contain in parentheses the arithmetic expressions to be carried out by each process. The
expression on the first subprocess computes u, the value of Used Length of Rod, as u=s*l. It takes s=9 as
the value of the Size of the Shaft Batch and l=0.22 m as the Length of each Shaft. The product, u=s*l
=9*0.22 =1.98 m, is the input for the next subprocess, in which the model computes residue=il-u, since the
length of the residue is the difference between il, the value of the initial Length of the Rod, 3.00 m, and u,
the value of Used Length of Rod, so residue=il–u=3.00–0.22=1.02 m. Different parameter values will, of
course, yield different results. This example demonstrates how OPM enables mixing conceptual modeling
with quantitative modeling which provides reasoning for the various mathematical steps involved in the
computation.
## 22.9 Sets and Iterations
A set is a collection of object instances of the same class.
An example of set is provided in Fig. 22.7. Shaft Batch is a set of nine object instances from the class
Shaft, so creating Shaft Batch implies iteration of Machining nine times, each time producing one Shaft.
This is a short formal way in OPM to model iteration: Whenever a process is attached with two
procedural links of the same kind such that one is a link to a set of n members and the other to a member
of the set, the semantics is iteration.
In our example, the two links are result links: one result link is from Machining to the set Shaft Batch,
and the other—from Machining to Shaft. The semantics of this template is iteration nine times of creating
Shaft. This is made more explicit when we zoom into Machining in SD1, expressing the fact that Cutting
and Lathing are performed sequentially and iteratively nine times to yield the nine Shafts. Each
Machining occurrence is a process instance of Machining, within which Cutting and Lathing occur to
create each of the nine instances of Shaft.
Iteration can combine any subset of the procedural links. Iteration can, of course, be applied to
informatical objects as well, providing a convenient, short way to model iterations, for example, in
algorithms, and serve, among many other control constructs (such as Boolean objects), for automated
code generation.
## 22.10 Operational Semantics in In-Zoomed Process Contexts
In-zooming of a process specifies transfer of execution control to subprocesses at the next detail level.
Executing a process with an in-zoomed context recursively transfers execution control to the top-most

subprocess(es) within the context of the deepest process. Control returns to the in-zoomed process after
its last subprocess completes its execution (Fig. 22.8).
### Figure 22.7
SD of Machining, where Shaft Batch is a set of 9 object instances from the class Shaft, so creating Shaft
Batch implies iteration of Machining nine times, each time producing one Shaft
### Figure 22.8
SD1 of Machining, in which Machining is in-zoomed, expressing the fact that Cutting and Lathing are
performed sequentially and iteratively 9 times to yield the nine Shafts
## 22.10.1 Implicit Invocation Link
An implicit invocation link is a link that is not visible graphically but is implied from
the vertical layout of processes within the context of an in-zoomed process.
Similar to its explicit counterpart, the implicit invocation link signifies initiation of a subsequent
process or concurrently beginning processes. Since invocation is an event, satisfaction of the precondition
for each subprocess is necessary to allow that subprocess to start executing.

OPM Operational Semantics and Control Links
An implicit invocation link can be (1) from a process to its first (or several) subprocess(es), (2) from a
subprocess to one or more subprocesses just below it along the time line inside the context of an in-
zoomed process, or (3) from the last in-zoomed subprocess(es) to their enclosing, context defining
process.
Specifically, (1) upon arriving at an in-zoomed process context, control immediately transfers to the
subprocess (es) with the highest ellipse (oval) top-most point within this in-zoomed process context. The
implicit invocation link from an in-zoomed process to its top-most subprocess transfers execution control.
(2) Along the process timeline, the completion of a source subprocess (or the last subprocess to finish
executing in the case of two or more subprocesses that started concurrently) immediately initiates the
subsequent subprocess(es) using the implicit invocation link. (3) Upon completion of performing the
subprocess with an ellipse top-most point that is lowest within this in-zoomed process context, execution
control returns to the in-zoomed process.
When two or more subprocesses have their top-most ellipse points at the same height, then an implicit
invocation link initiates each process and they start in parallel upon individual precondition satisfaction.
The process that completes last initiates the next subprocess or set of parallel subprocesses.
In the OPD on the left hand side of Fig. 22.9, Cleaning invokes Coating, so Cleaning affects Product
first and then Coating affects Product. The invocation link dictates this process sequence. In the
equivalent OPD on the right hand side of Fig. 22.9, Finishing zooms into Cleaning and Coating, with the
former’s ellipse top point above the latter’s, so when Finishing starts, control immediately transfers to
Cleaning, and when Cleaning ends, the implicit invocation link invokes Coating. The two OPDs are
semantically equivalent, but the one on the left does not have Finishing as an enclosing context, making it
less expressive from a system viewpoint while using two links more than the OPD on the left.
### Figure 22.9
Invocation link (left) and implicit invocation link (right)
## 22.10.2 Implicit Parallel Invocation Link Set
Graphically, when the ellipse top points of two or more subprocesses within the scope of an in-zoomed
process are at the same height (with possible allowable tolerance), these subprocesses are initiated and
begin in parallel, and each starts executing subject to the satisfaction of its precondition. In this situation,
there is a set of implicit invocation links from the source in-zoomed process to each one of the parallel
subprocesses. Process synchronization is such that when the last one of these subprocesses ends,
execution control initiates the next subprocess(es). If there are two or more subprocesses with a lower

ellipse top point at the same height, the control initiates them in parallel. If there are no more
subprocesses to invoke, control returns to the in-zoomed refineable process.
Figure 22.10 shows subprocesses of Processing with the following partial order: A, (B, C), D, (E, F,
G). B and C start upon completion of A. D starts upon completion of the longer process from among B and
C. E, F, and G start upon completion of D. Execution control returns to Processing upon completion of
the longest process from among E, F, and G.
.
### Figure 22.10
Partial subprocesses order and implicit parallel invocation link set
Table 22.11 summarizes the implicit invocation link kinds.
## 22.10.3 Link Distribution Across Context
Graphically, a procedural link attached to the contour of an in-zoomed process has distributive semantics.
Leaving a link attached to the contour of the in-zoomed process means that the link is distributed and
attached to each one of the subprocesses. The contour of the in-zoomed process has semantics analogous
to that of algebraic parentheses following a multiplication symbol, which distribute the multiplication
operator to the expressions inside the parentheses.
In Fig. 22.11, the OPDs on the left and right are equivalent, but the one on the left is clearer and less
cluttered. An agent link from A to P means that A handles the subprocesses P1, P2, and P3. An instrument
link from B to P means that the subprocesses P1, P2, and P3 require B. Analogously in algebra, suppose
the agent (or instrument) link was a multiplication operator, A was a multiplier and in-zooming was
addition, such that P = P1 + P2 + P3, and P was a multiplicand, then A*P = A*(P1 + P2 + P3) = A*P1 +
A*P2 + A*P3.
If an enabler connects to the outer contour of an in-zoomed contour it must connect to at least one of
its subprocesses. Consumption and result links must not be attached to the outer contour of an in-zoomed
process because this violates temporal logical conditions. With a distributed consumption link, an attempt
would be made to consume an already-consumed object by a subprocesses that is not the first to perform.
Similarly, a distributed result link would attempt to create an already existing object instance. The
modeler needs to be careful when more than one process creates the same object, i.e. more than one
instance of the object exists, or two or more processes affect or consume the same object. OPM modeling
tools need to track the number of instances of an object.

OPM Operational Semantics and Control Links
Table 22.11 Implicit invocation link summary
In Fig. 22.12, the OPD on the left contains invalid consumption and result links, as annotated in the
OPL. The consumption link gives rise to the OPL sentence “P consumes C.” The reason is that applying
link distribution, the consequence is the three OPL sentences “P1 consumes C.”, “P2 consumes C.”, and
“P3 consumes C.”. However, since P1 consumes C first according to its temporal order, the same instance
of C does not exist when P2 or P3 performs, and therefore neither P2 nor P3 can consume C again.
Similarly, the same instance of B results only once. The OPD on the right depicts valid links since they
specify which of the subprocesses of P consumes C (it is P1) and which one yields B (P2).
Since attaching a consumption or result link to an in-zoomed process is invalid, when a process is in-
zoomed, all the consumption and result links that were attached to it shall be attached initially or by
default to its first subprocess. It is the modeler’s responsibility to move the links to subsequent
subprocesses as needed.

### Figure 22.11
Link distribution across in-zooming context. Left: the shorter, correct version. Right: the equivalent loinger
version
### Figure 22.12
Link distribution restriction for consumption and result links
As soon as the modeler in-zooms P in Fig. 22.12 and inserts P1 into its context, the modeling tool
should migrate the destination end of the consumption link emanating from C from P to P1. Similarly, the
source end of the result link to B should also migrate from P to P1. When the modeler adds P2, the
modeler may migrate the destination end of the consumption link and/or the source end of the result link
from P1 to P2, as Fig. 22.12 shows.

OPM Operational Semantics and Control Links
## 22.10.4 Split State-Specified Link Pairs
When a process that changes an object from an input state to an output state is in-zoomed, the OPD, either
in-diagram or new-diagram, becomes underspecified. To restore specification, the modeler must attach
both the state-specified input link and the state-specified output link to one of the subprocesses in a
temporally-feasible manner.
A split in-out-specified link pair of process P is an input-output specified link pair
whose input and output link constituents connect different subprocesses of P.
A split input link is the input link of the split in-out-specified link pair.
A split output link is the output link of the split in-out-specified link pair.
In Fig. 22.13, the OPD in the middle is underspecified because if P1 changes A from s1 to s2, P2
cannot do this again, but it can go the other way—change A from s2 back to s1, but neither is explicitly
specified. P1 can change A from s1, i.e., take it out of s1 and leave it in transition between s1 and s2. In-
between P1 and P2 there may be one or more other interim subprocesses, during which A is still in that
transition. P2 then changes A to s2. The OPD on the right models this case (without interim
subprocesses), creating a split input link from s1 of A to P1 and a split output link from P2 to s2.
### Figure 22.13
Split state-specified transforming link resolve underspecification
Table 22.12 summarizes the split input-output specified effect link pair. There are no control-modified
versions of the split input-specified effect link, because this can cause the of effect link semantics to be
distorted. For example, if in Fig. 22.13 P1 is skipped, A stays in s1, so if P2 is not skipped, A was not
taken out of s1, so it cannot change to s2 according to the semantics of the effect link.

Table 22.12 Split input-output specified effect link pair
## 22.11 Involved Object Set Instance Transformations
As a consequence of link distribution, the following constraints apply to operational instances of
transformees.
Each consumee instance in the preprocess object set of a process shall cease to exist at the beginning
of the most detailed subprocess of the process that consumes the instance, so that instance is not a
member of the postprocess object set of that process.
Each affectee instance in the preprocess object set of a process that changes that instance as a
consequence of the process performance shall exit from its input state at the beginning of the deepest
(most detailed) subprocess that changes the affectee.
Each affectee instance in the postprocess object set of a process that changes that operational
instance as a consequence of the process performance shall enter its output state at the completion of
the deepest subprocess that changes the affectee.
Each resultee instance in the postprocess object set of a process shall be created and begin to exist at
the completion of the most detailed subprocess that yields the resultee instance.
A stateful object B for which the execution of process P has the effect of changing the state of B, exits
from the input state at the beginning of the most detailed subprocess of P that changes B, and enters the
output state at the end of the same subprocess of P or some subsequent subprocess of P. Since process P
execution takes a positive amount of time, that object B is in transition between states, from its input state
to its output state: it has left its input state but has not yet arrived at its output state.

OPM Operational Semantics and Control Links
## 22.12 UML’s Object Constraint Language (OCL)
The OPM Parameterized Participation Constraint (PPC) mini-language described in Sect. 17.3 is
somewhat reminiscent of Object Constrain Language (OCL), developed by Warmer and Kleppe (1998).
OCL is “a precise text language that provides constraint and object query expressions that cannot be
expressed by diagrammatic notation.” The current OMG OCL version (OMG OCL 2014), explains the
motivation for developing OCL by arguing that “a UML diagram, such as a class diagram, is typically
not refined enough to provide all the relevant aspects of a specification. There is, among other things, a
need to describe additional constraints about the objects in the model. Such constraints are often
described in natural language. Practice has shown that this will always result in ambiguities. … OCL has
been developed to fill this gap. It is a formal language that remains easy to read and write.”
Comparing OPM’s PPC mini-language to OCL, we note that while OCL is a complete language
whose current OMG 2014 specification holds 262 pages, the PPC mini-language can be specified in a few
pages. It is expressed in the OPD and translated as part of the OPL, and unlike OCL it does not provide
for querying. With respect to the claim that OCL “remains easy to read and write” let us consider the
constraint example provided in OMG OCL (2014, p. 20):
Married people are of age >= 18. The OCL syntax for this constraint is as follows.
context Person
inv: (self.wife->notEmpty() implies self.wife.age >= 18)
and (self.husband->notEmpty() implies self.husband.age >= 18)
The corresponding OPM model is provided in Fig. 22.14. The OPL of this model seems to be a bit
more humanly comprehensible than the OCL specification above.
### Figure 22.14
The OPM model of the constraint “Married people are of age >= 18”

## 22.13 Summary
An event is a point in time at which something significant to the system execution happens.
Events and preconditions in concert specify OPM flow of execution control for process
performance according to the event-condition-action paradigm.
The event-condition-action paradigm stipulates that starting the performance of a process (the
“ ”
action ) has two prerequisites: an initiating event and satisfaction of a precondition derived
from the preprocess object set.
A control modifier is one of the two letter symbols e and c, added to a procedural link, which
add to the semantics of that link the event and condition semantics, respectively.
A control link is a procedural link with the addition of a control modifier.
An event link is a procedural link with the control modifier e, indicating initiation of the link’s
destination process, triggering that process’ precondition evaluation.
A condition link is a procedural link with the control modifier c, indicating that if the
precondition of the link’s destination process is not met, then that process is skipped.
The skip semantics precedence OPM principle states that skip semantics, induced by a control
link, takes precedence over wait semantics, induced by a non-control link.
A maximal-timed process is a process for which the modeler determines a maximal duration.
An overtime handling process is a time exception process that determines what to do in case the
time performance of a maximal-timed process exceeds its maximal allowable time.
An overtime exception link is a procedural link from a maximal-timed process to an overtime
handling process, indicating that if the duration of a maximal-timed process exceeds its maximal
duration, then the overtime exception process is initiated.
A minimal-timed process is a process for which the modeler determines a minimal duration.
An undertime handling process is a time exception process that determines what to do in case
the time performance of a minimal timed process falls short of its minimal duration.
An undertime exception link is a procedural link from a minimal-timed process to an undertime
exception process, indicating that if the time performance of a timed process falls short of its
minimal allowable time, the undertime exception process is initiated.

OPM Operational Semantics and Control Links
## 22.14 Problems
1. 2. 3. 4. 5. 6. 7. 8. 9. 10. Why is the event link in Fig. 3.5 needed?
What is the role of the condition link in in Fig. 6.1?
Explain why in Fig. 7.1 two condition links are needed.
Use Fig. 21.15 as a template and replace B, P, P1 and P2 in it with meaningful things.
Explain why each one of the five entries in Table 21.1 marked “invalid” is indeed invalid.
Explain why in Fig. 21.13 P123 (the set TO of thing to out-zoom) cannot contain P4 and BK
only.
What thing must be added to P4 and BK such that TO becomes valid?
Assuming TO is the set as you suggested in the previous question, draw the resulting
SD1.1[new].
Create the OPM model of uninterrupted irrigating by water as a consumee for the process
irrigating. The consumee has an attribute quantity [liter] with value 1000 and the consumption
link has a consumption rate [liter/sec] with value 50.
Create the OPM model of the following system. Gasoline and Diesel Oil are resultees of the
process Refining, which consumes Crude Oil. The resultees Gasoline and Diesel Oil each have an
attribute Volume [m3]. The Refining to Gasoline result link has yield rate [m3/hour] with value
## 1000 and the Refining to Diesel Oil result link has yield rate [m3/hour] with value 800. Assuming
there is enough Crude Oil, if Refining activates and performs for 10 hours, it will yield 10,000
[m3] of Gasoline and 8,000 [m3] of Crude Oil.
