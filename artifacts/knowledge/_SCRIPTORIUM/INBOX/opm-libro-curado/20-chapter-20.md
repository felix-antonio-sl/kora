# Chapter 20 Generalization and Instantiation
As this term is most commonly used, a generalization is an “all” statement, to the
effect that all objects of a certain general kind possess a certain property.
Lowe (1983)
While discussing aggregation and exhibition, we talked about entire groups of objects or processes—any
scientific paper, any employee, any running. However, what if we wanted to consider the example of a
specific paper, written by a certain John Doe? Or if we wanted to consider a group of employees, namely
managers, who receive a certain salary out of the range of salaries available for the company? Perhaps we
would like to discuss running in a marathon, as opposed to just any kind of running? We need to be able
to pay particular attention to a specialized group, which belongs to a more general group, or even a
specific instance out of a class of objects. As its name clearly points out, generalization-specialization is
the relation between a general and a special case of a thing. Classification-instantiation is the relation
between a class of things and a unique instance from the class. Since these two concepts are important to
systems modeling, we consider them two of the four fundamental relations; and since they are intimately
related, they are discussed and explained together in this chapter.
## 20.1 Generalization-Specialization: Introduction
Let us first consider several simple examples to set the stage for discussing generalization-specialization,
or “gen-spec.”1
### Figure 20.1
Generalization-specialization examples
Person in the left OPD of Fig. 20.1 is the general case, while Man and Woman are its special cases.
Other examples are “Dog and Cat are Pets.”, “Pascal, Java, and C++ are Programming Languages.”,
1The shorthand term “gen-spec” is borrowed from Coad and Yourdon (1991).

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

## 278 Generalization and Instantiation
“Airplane and Car are Vehicles.”, “Flying and Sailing are Transporting.”, and “Ketchup and Mustard are
Condiments.”
Generalization-specialization is a fundamental structural relation between a general
thing G and one or more things S1, S2, … Sn, which are specializations of G.
An alternative way of expressing the OPL sentence might have been “Digital Camera and Analog
Camera specialize Cameras.” However, sticking to the principle of keeping the OPL language as natural
and as simple as possible, OPL uses the clearer and more intuitive reserved phrases “is a” (or “are” for
plural) rather than “specializes” or “specialize” for denoting the gen-spec relation from the reverse, or
bottom-up direction, from the specialized thing—the specialization—to the generalizing thing—the
general. Any number of specializations is possible. The following example is of three specializing
objects.
Cucumber is a Vegetable.
Tomato is a Vegetable.
Carrot is a Vegetable.
We combine the three specialization sentences above into one:
Cucumber, Tomato, and Carrot are Vegetables.
Generalization-specialization is a transitive relation, meaning that if A is a B, and B is a C, then A is a
C. More concretely, consider the following two specialization sentences:
Tomato is a Vegetable.
Vegetable is a Plant.
Since generalization-specialization is transitive, we can deduce that:
Tomato is a Plant.
Generalization-specialization means that a refineable, the general, generalizes two or more refinees,
which are specializations of the general. The generalization-specialization relation binds one or more
specializations with the same perseverance as the general, such that both the general and all its
specializations are objects (in metamodel terms, if the Thing’s Perseverance is persistent) or the general
and all its specializations are processes (if the Thing’s Perseverance is transient).
Graphically, an empty triangle with its apex connecting by a line to the general and the specializations
connecting by lines to the opposite base denotes the generalization-specialization relation link.
UML and SysML use a white (blank) triangle to denote generalization-specialization, (as in OPM),
but in UML and SysML the triangle’s tip is linked directly to the generalizing object, and the white
triangle base is not necessarily horizontal, but rather perpendicular to the line connected to the
specialization. Moreover, similar to the case with aggregation, since there is no fork in UML, each
specialization in a UML class diagram and SysML block definition diagram must have its own symbol.
Since UML and SysML do not have processes in class diagrams, the aggregation and specialization
relations in UML and SysML apply to objects only.
## 20.1.1 Process Specialization
Not only objects are subject to generalization-specialization. The same relation applies to processes as
well. Figure 20.2 shows two simple examples.

### Figure 20.2
Single and plural process specializations
In order to comply with the English grammar, the process specialization sentence is slightly different
than the (object) specialization sentence in that (1) instead of the reserved phrase “is a,” the reserved word
“is” is used, and (2) while the generalizing object is plural, as in Vegetables, in multiple process
specialization sentence it is singular, as in Cooking. Consider the following OPL sentences.
### Figure 20.3
Left: A general pattern of Cooking. Right: The specializations of Cooking Tool, Cooking, and Food, and the
specialized links between these specializations
Specializations of objects and processes can be combined to specify specialized procedural links
between the object and process specializations. Figure 20.3 shows on the left a pattern of Cooking, which
uses Cooking Tool as an instrument and yields Food. On the right are three specializations of Cooking
Tool, Cooking, and Food. Each Cooking Tool specialization is an instrument of a specialization of
Cooking, yielding a specialization of Food.
## 280 Generalization and Instantiation
## 20.1.2 Link Under- and Over-Specification
Link under-specification would occur if on the right OPD of Fig. 20.3 we would have left the two links as
in the OPD on the left and not specify the six procedural links on the right. This would mean that any tool
can be used for any cooking. Link over-specification would occur if, in addition to the six procedural
links in the OPD on the right, we would have added the two links as in the OPD on the left. Both should
be avoided. In under-specification, leaving the single instrument link from Cooking Tool to Cooking on
the right means that any Cooking Tool could be considered as instrument of any Cooking process and to
yield any Food. On the other hand, in over-specification, the two generalizing links, left along with the
six specialized links, become redundant. Under- and over-specification can occur also with structural links.
## 20.2 Inheritance
The most prominent and immediate benefit gained from using the gen-spec relation is the inheritance it
induces.
Inheritance is assignment of OPM elements—things and links—of a general to its
specializations.
In OO design, the meaning of inheritance is that attributes, and to some extent also operations, of the
generalizing object are inherited to the specialized objects. In OPM, the effect of inheritance is stronger,
as, in addition to inheriting features and parts, it includes inheriting structural and procedural links, as
well as states. Through the generalization-specialization relation, each specialization inherits from the
general each of the following four kinds of inheritable elements:
all the parts of a general from its aggregation-participation link,
all the features of the general from its exhibition-characterization link,
all the tagged structural links to which the general connects, and
all the procedural links to which the general connects.
OPM provides the opportunity for multiple inheritance by allowing a thing to inherit from more than
one general each of the refinees—the four inheritable elements (parts, features, tagged structural links,
and procedural links) that exist for that general.
The modeler may override any of the parts of the general, which are by default inherited by the
specialization, by specifying for any participant inherited from a general, a specialization of that
participant with a different name and a different set of states.
## 20.2.1 Creating a General from Candidate Specializations
To create a general from one or more candidate specializations, the inheritable elements common to each
of the candidates migrated “upward” to a generalizing thing. The manipulation of inheritable elements
shall be as follows:
Combine all of the common features and common participants of the specializations into one
newly created general;

Connect the new general using the generalization-specialization relation link to the
specializations;
Remove from the specializations all of the common features and common parts that the
specializations now inherit from the new general; and
Migrate any common tagged structural link and any common procedural link that connects a
thing T to each one of the specializations from the specializations to the general, such that there
will be a single link from T to the general.
## 20.2.2 Feature Inheritance
A general thing inherits its features—attributes and operation—to each one of its specializations. For
example, Fig. 20.4 is an OPD of a Camera, which has two features: The attribute Optical Zoom and the
operation Image Capturing. This OPD has the following corresponding OPL paragraph, where the last
OPL sentence expresses the unidirectional tagged structural relation.
### Figure 20.4
Left Camera and its Analog Camera and Digital Camera specializations
Since Digital Camera and Analog Camera are specializations of Camera, we can replace Camera with
its Digital Camera and its Analog Camera specializations. This has indeed been done in Fig. 20.5, which
demonstrates the basic semantics of inheritance: the specialization—the refinee— inherits features
(attributes and operations) from the general—the refineable.
### Figure 20.5
Digital Camera and Analog Camera are specializations of Camera, therefore each can substitute Camera from
### Figure 20.4
In OPM not only features are inherited; links and states are inherited as well. The inheritor can
therefore replace the ancestor. Digital Camera and Analog Camera inherit not only the features of Camera,
which are the attribute Optical Zoom and the operation Image Capturing; they also inherit the tagged
## 282 Generalization and Instantiation
structural relation uses from Camera to Capturing Medium. Moreover, not only structural relations are
inherited; procedural relations are inherited as well. The inheritor, however, may have more features,
links, or states.
## 20.2.3 Inheritance of Structural Relations
Consider the OPD in Fig. 20.6, in which we specify the parts of Camera and the specializations of
Capturing Medium.
### Figure 20.6
The parts, specializations and features of Camera are specified along with the specializations of Capturing
Medium
This implies that the parts Camera consists of are inherited to the two Camera specializations:
Digital Camera consists of Lens, Body, and Image Capturing Mechanism.
Analog Camera consists of Lens, Body, and Image Capturing Mechanism.
Not only aggregation is inherited. Any tagged structural relation, such as uses, is inherited. Since the
tagged relation uses links Camera to Capturing Medium, when we specify the specializations of both
Camera and Capturing Medium without taking care of the structural relation uses, we introduce link
under-specification. This under-specification, encountered earlier, stems from the fact that the structural
relation uses from Camera to Capturing Medium does not specify which Camera specialization (Analog
Camera or Digital Camera) uses which Capturing Medium specialization (Image Storage Medium or Film).
To set this straight, we specify which Camera specialization uses which Capturing Medium
specialization.

## 20.2.4 State and Link Inheritance
In OPM, states and links are inherited too. Prior to the Image Capturing process in the Camera example,
the Capturing Medium, which the Camera uses, is blank. After the process Image Capturing occurs,
Capturing Medium is recorded. Hence, blank and recorded are two states of Capturing Medium. The OPD
in Fig. 20.7 has two generalization links, one for Camera and the other for Capturing Medium. These two
relations induce the two OPDs in Fig. 20.8.
### Figure 20.7
State inheritance: Film and Image Storage Medium inherit the states and the input and output links to and
from Image Capturing
## 20.3 Specialization Through a Discriminating Attribute
Quite often, a general has specializations that are distinguished from the general in that there is a certain
attribute of the general whose restricted value defines the specialization.
A discriminating attribute is an inherited attribute whose different values define
corresponding specializations.
## 284 Generalization and Instantiation
Figure 20.10 shows an OPD in which Vehicle exhibits the attribute Travelling Medium with values
ground, air, and water surface. Travelling Medium is the discriminating attribute of Vehicle, because the
three values of Travelling Medium define the three specializations of Vehicle. These are Car, Aircraft, and
Ship, with the corresponding Travelling Medium values ground, air, and water surface.
A general may have more than one discriminating attribute. The maximum number of specializations
with more than one discriminating attribute is the Cartesian product of the number of possible values for
each discriminating attribute, where some combination of attribute values may be invalid. For example,
extending the content of Fig. 20.10, another attribute of Vehicle might be Purpose with the two values
civilian and military. Based on these two values, there are two Vehicle specializations: civilian Vehicle and
military Vehicle. Due to multiple inheritance, the result is an inheritance lattice where the number of the
most detailed specializations would be 3 × 2 = 6 as follows: civilian Car, civilian Aircraft, civilian Ship,
military Car, military Aircraft, and military Ship.
### Figure 20.8
State inheritance induced by the OPD in Fig. 20.9. Left: Camera is substituted by Digital Camera, and
Capturing Medium—by Image Storage Medium. Right: Camera is substituted by Analog Camera, and Capturing
Medium—by Film

### Figure 20.10
The discriminating attribute Travelling Medium and its specializations
## 20.4 State-Specified Characterization Link
A state-specified characterization link is an exhibition-characterization link from a
specialization to a specific value of a discriminating attribute of its general, which
expresses the fact that the specialization can have only that value for that
discriminating attribute.
Graphically, the state-specified characterization link is the triangular exhibition-characterization
symbol, with its apex connected to the specialization and its base—to the specific value. Using the state-
specified characterization relation link, the OPD in Fig. 20.11 is significantly more compact than its
equivalent OPD in Fig. 20.10. Here, the discriminating attribute Travelling Medium of Vehicle with values
ground, air, and water surface appears only once, as opposed to four times in Fig. 20.10. The model
expresses Car, Aircraft, and Ship as specializations of Vehicle, connecting each specialization with a state-
specified characterization relation link to the corresponding Travelling Medium value of ground, air, and
water surface, respectively.
## 286 Generalization and Instantiation
### Figure 20.11
State-specified characterization link example
## 20.5 Classification-Instantiation
An instance is an actual thing of some class of things, all having the same set of features, same structure,
and same behavior. For example, Lassie and Blackie in Fig. 20.12 are instances of Dog. Dog is the class
of all the dogs, and Lassie is an actual exemplar of that class. The symbol of instantiation is a black
inverted triangle inside a larger white triangle.
In spoken English, the sentence “Lassie is a dog” is more natural, but the phrase “is a” is reserved for
the specialization sentence, so to avoid conflicts and be explicit, the phrase “is an instance of” links an
instance with its class in an OPL sentence that expresses instantiation. The plural version, used for more
than one instance, is “are instances of,” as in “Bach, Beethoven and Brahms are instances of Composers.”
## 20.5.1 Classes and Instances
The things we have encountered while discussing generalization-specialization are classes of things,
either object classes or process classes. When we talked about objects, we were actually referring to a
typical example of its object class, a pattern of objects from which objects could be generated.
A class is a template of a thing.
An instance of a class is an incarnation of a particular identifiable member of that
class.

The definitions of class and instance are more general than their OO counterparts, as they refer to
things rather than to objects. In metamodel terms, since a Thing is an Object or a Process, Class
specializes into an Object Class and a Process Class. Likewise, Instance specializes into an Object
Instance and a Process Instance: An Object Instance is an incarnation of the pattern specified by the
Object Class and a Process Instance is an incarnation of the pattern specified by the Process Class.
### Figure 20.12
The instantiation symbol links a class (Dog) to one or more of its instances
The template that the class defines includes everything that is inherited. As we have seen, in OPM it
means that not only features, but also structural relations and procedural relations are inherited, and for
object classes states are also inherited. Unlike a specialized class, an instance cannot exhibit any feature
that its class does not exhibit, nor can an instance of an object be at a state that is not a state of its class.
An object instance can be uniquely identified in the system, so at any given point in time it is possible to
observe whether it exists, and if so—what its states and attribute values are.
## 20.5.2 Instantiation Versus Specialization
Generalization-specialization is a transitive structural relation that gives rise to a hierarchy tree. Each
level in the hierarchy contains specializations of the level above it. The “leaves” of that hierarchy are the
instances of the class. Thus we can say that instantiation is a special case of specialization, which, in the
context of the system under study or development, cannot be specialized further. Figure 20.13 shows a
specialization hierarchy that starts with Car as its top level and presents increasingly specialized object
classes until it gets to Jack’s Car. This is the first object that is physical and unique. It has a VIN (vehicle
identification number) that uniquely identifies it, and at any given moment the values or states of all its
attributes, such as Color, Location, Mileage and Speed, can be specified.
Instance is a leaf in the generalization-specialization hierarchy—it is not possible to have
specializations of an instance. Inheritance of features from a class to its instances is exactly the same as
the inheritance of features from a super-class to its sub-class anywhere along the generalization-
specialization hierarchy. The only differences are that (1) an instance cannot have further specializations,
because it is at the bottom of the hierarchy, and (2) only an instance has concrete values of its attributes,
as Fig. 20.13 demonstrates.
## 288 Generalization and Instantiation
### Figure 20.13
The specialization hierarchy of Car all the way to the instance Jack’s Car and its specific attribute values at
the time of observing it
## 20.6 The Relativity of Instance
Like many other concepts we have encountered, the term instance is relative to the system of discourse.
What for a certain system is considered instance of a class, can for another system be just a sub-class of a
super-class. An instance in one system may be a class that has instances or that further recursively
specializes into more refined classes, which ultimately have instances.
To demonstrate this, let us look at a few examples from the world of cars. We have seen that Taurus
## 2015 is an object class of all the instances of cars made by Ford of model Taurus manufactured in the year
2015. Suppose that the system we are now concerned with is a system for comparing and evaluating cars
of model year 2015. One of the instances in this system is Taurus 2015, and it is an instance of the object
class Model Year 2015 Car. Physical cars with specific VIN do not exist and have no meaning in this
system. In the gen-spec hierarchy tree, Taurus 2015 is one of the leaves: it has no further specializations
beneath it.
As another example, consider a national highway system, in which the system architects are interested
in the various types of vehicles that use the roads. What matters to them about the vehicles are their size,
weight, average speed, and average annual distance that each type of vehicle travels. The designers of this
system therefore decided to categorize vehicles into three types: cars, trucks and buses. While these three
types are specializations of vehicle, for the system under consideration they are also the three instances of
the object class vehicle. The architects are not interested in each individual car, bus or truck, so the
number of each vehicle type, its average speed, mileage, etc. are attributes of vehicle that are inherited to
its three instances.

Consider now a different system of the Motor Vehicles Taxation Office in some country, which, for
taxation purpose differentiates between Taxation Classes of Motor Vehicles as follows: Commercial Van,
Sedan, Collector Car, Sports Utility Vehicle, and Luxury Car. For this system, cars are differentiated into
these types based on their Market Value and Application. Furthermore, the system maintains and
constantly updates a list of each Vehicle Manufacturer and each Vehicle Model by Year Model, with an
indication of which Vehicle Model belongs to which Taxation Class. Here, the Taxation Class is an
attribute of Vehicle. Commercial Van, Sedan, etc., are values of the Taxation Class attribute of Vehicle.
The instances of the class Vehicle in this system are the various Year Models, because the system is only
concerned with setting tax levels on cars by Taxation Class and does not care about individual cars.
Finally, consider a car dealership. Here, of course, each individual car has its own record, including its
VIN, make, model, year, owner, etc. This is the “classical” case of instance, similar to the one presented
in Fig. 20.13, where each instance is a physical entity with its unique identifier. However, as we have
seen, instances can be informatical, such as car models, vehicle types or records in a file.
## 20.7 Constraining Attribute Values
A class can be used to constrain the possible range of attribute values. In Fig. 20.14, Adult is a class with
three attributes: Gender, with possible values female and male, Height in cm, with possible values
120..240 (120 through 240), and Weight in Kg, with possible values 40..240. Jack Robinson is an instance
of Adult, with Gender value male, Height value 185 cm, and Weight value 88 Kg. As Fig. 20.14
demonstrates, the name of the instance of Adult, Jack Robinson in this case, can be followed by the
semicolon symbol “:” followed by the name of the class. This is useful when only the instance appears in
an OPD without being attached to this class.
### Figure 20.14
The attribute values of the calss Person are constrained with value ranges (class on left and instance on
right)
## 290 Generalization and Instantiation
## 7.537 gr/cm3. The OPD in Fig. 20.15 presents the class Metal Powder Mixture, indicating that its Specific Weight
attribute value can range from 7.545 to An operational (runtime) instance of Metal Powder
Mixture is Mixture Lot #7545 with Specific Weight attribute value is 7.555 gr/cm3. This value is within the
allowable range.
### Figure 20.15
Constrsaining attribute value. Left: The class and it attribute value range. Right: the instance and its actual
value, which is in the constrained range
The OPL sentence “Mixture Lot #7545 exhibits Specific Weight in gr/cm3.”
, is not present in the OPL of
Fig. 20.15, because that sentence is implicit from the expressed fact “
Mixture Lot #7545 is an instance of
Metal Powder Mixture, and therefore Mixture Lot #7545 inherits this attribute from Metal Powder Mixture.
## 20.8 Process Instances
OPM instantiation applies not just to objects but also to processes. The processes we have encountered so
far are actually process classes: they are patterns of happenings that involve object classes.
A process class is a pattern of happening (the sequence of subprocesses), which
involves object classes that are members of the involved object set of that process
class.
A process occurrence, which follows this pattern and involves particular object instances in its preprocess
and postprocess object sets, is a process instance. Hence, a process instance shall be a particular
occurrence of a process class to which that instance belongs. Any process instance is therefore associated
with a distinct set of preprocess and postprocess object instance sets.
A process instance is a particular occurrence of a process class to which that instance
belongs.
The power of the process class concept is that it enables the modeling of a process as a template or a
protocol for some transformation that a class of objects undergoes. That transformation includes neither
the spatio-temporal framework nor the particular set of object instances with which the process instance is

associated; these can be identified only when we are at the instance level, or operational level of the
system.
### Figure 20.16
Movie Showing as an example of a process class (left) and its instace (right)
A process instance is a concrete occurrence of a process class, whose preprocess and postprocess
object sets are sets of object instances. In particular, a process instance has a time stamp, a specific date
and time at which the process started or ended. Figure 20.16 depicts on the left Movie Showing as an
example of a process class, with Movie, and Theatre as instruments of this process class, Date & Time as
its attribute, and Audience as the class’ affectee. In the OPD on the right, Gone With The Wind Premiere
Gala Movie Showing is a process instance of the Movie Showing process class. All the instances are
greyed out to distinguish them from their classes. Gone With The Wind is an instance of Movie, Atlanta
Theatre is an instance of Theatre, Atlanta Audience is an instance of Audience, and Dec. 15 1939 8PM
(Dirks 2015) is the value of Date & Time at which the process instance took place. The same objects
instance can participate in two or more process instances. For example, the same is an instance of Movie,
identified by its name as Gone With The Wind, can participate in all the process instances of Gone With
The Wind Movie Showing (other than the premier gala one), but each Atlanta Audience is a different
instance of Audience, since it is comprised of a different set of movie goers.
## 292 Generalization and Instantiation
## 20.9 Summary
Generalization-specialization is the relation between a general thing and a specialization of that
thing.
Classification-instantiation is the relation between a class of things and a unique instance that
belongs that class.
Generalization-specialization gives rise to inheritance from the generalized thing to the
specialized one(s).
Inheritance is of features (attributes and operations), structural relations and procedural relations.
For objects, states are inherited too.
OPM processes specialize in a manner similar to objects.
States of specialized objects can override inherited states.
A class is a template, from which things that instantiate the class can be generated as members of
that class.
Instance is a relative term. A specialization in one system can be an instance in another.
A process instance is a particular occurrence of a process at a given point in time and whose
involved object set is a set of object instances.
## 20.10 Problems
1. 2. 3. 4. 5. Provide two examples of object specializations and two of process specializations. Specify them
in OPDs and OPL.
Create a specialization hierarchy of sports games, which would include as a minimum volleyball,
basketball, soccer, football, tennis, and baseball. Apply OPM to show what features are common
and inherited, and what are game-specific.
Repeat the previous problem for a specialization hierarchy of track and field sport types, which
would include at least three types of running, three types of swimming and three types of
throwing.
Considering the inheritance of procedural links, are the effect links redundant? Why or why not?
Draw the OPD expressed in the OPL paragraph below.
Pilot, Sailor, and Driver are Occupations.
Airplane, Vessel, and Truck are Transportation Systems.
Flying, Sailing, and Driving are Transporting.
6. Complete the OPD from the previous question with the following model facts: (1) Pilot, Sailor,
and Driver handle Flying, Sailing, and Driving, respectively. (2) Flying, Sailing, and Driving
require Airplane, Vessel, and Truck, respectively.

7. 8. 9. Give examples of two systems where instances in the first system are specializations in the
second. Draw the OPD and write the OPL of these systems.
The main types of welding are: (1) Gas—Uses gas flame over metals until molten puddle is
formed. Most popular fuels used with oxygen include acetylene and hydrogen. (2) Arc—Two
metals are joined by generating an electric arc between a covered metal electrode and the base
metal. (3) Oxygen and Arc Cutting—Metal cutting in welding is the severing or removal of
metal by a flame or arc. Use OPM to describe these welding types.
Specify three instances of electrical appliances at your home. For each one describe its object
class with at least three levels of aggregation-participation hierarchy and the operations it
performs. Use the instantiation symbol to denote your appliance and provide an attribute that
uniquely identifies it.
