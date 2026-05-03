---
_manifest:
  urn: urn:dev:kb:ifml-in-a-nutshell
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/dev/ifml-in-a-nutshell-fx.md —
      guia condensada de IFML (Interaction Flow Modeling Language) para modelado de
      front-end independiente de tecnologia
version: 1.0.0
status: borrador
tags:
- ifml
- interaction-flow
- modeling-language
- frontend
- omg
lang: es
extensions:
  kora:
    family: guide
    shard_index: 1
    shard_count: 4
    shard_root_urn: urn:dev:kb:ifml-in-a-nutshell
---

# IFML in a Nutshell


## Introduction

### 1.1. What IFML is About

IFML supports the specification of the front end of applications independently of the technological details of their realization. It addresses the following questions of front-end modeling:
- The composition of the view: What are the visualization units that compose the interface, how are they organized, and which ones are displayed simultaneously and which in mutual exclusion?
- The content of the view: What content elements are displayed from the application to the user, and what input is acquired from the user and supplied to the application?
- The commands: What interaction events are supported?
- The actions: What business components are triggered by the events?
- The effects of interaction: What is the effect of events and action execution on the state of the interface?
- The parameter binding: What data items are communicated between the elements of the user interface and the triggered actions?

IFML expresses the abovementioned aspects using a visual modeling language based on the OMG standards. Its technical foundations lie on the OMG Model Driven Architecture (MDA) framework. This grants seamless integration with the specifications of the other layers of the software system. The specification consists of five main technical artifacts:
- The IFML metamodel specifies the structure and semantics of the IFML constructs using the OMG Meta Object Facility (MOF).
- The IFML Unified Modeling Language (UML) profile defines a UML-based syntax for expressing IFML models. In particular, the UML Profile for IFML is based on the use of UML components (both basic components and packaging components), classes, and other concepts, which may concur with hierarchical structures or dependencies.
- The IFML visual syntax offers a concrete representation based on a unique diagram. This compacts all aspects of the user interface that are otherwise expressed separately with UML class diagrams, state machine, and composite structure diagrams.
- The IFML textual syntax offers a textual alternative, equivalent to the visual syntax, for expressing IFML models.
- The IFML XMI provides a model exchange format for tool portability.

This book adopts the IFML visual syntax as a concrete vehicle for conveying the user interaction models because it is close to UML—and thus familiar to developers—and because it is very compact.

### 1.2. The IFML Design Principles

Designing a modeling language for the front end is a complex and multidisciplinary task where many perspectives intersect. A good modeling language should pay attention to coverage (i.e., the ability to represent complex application front ends but also to model usability and understandability). The latter goals require addressing all the factors that contribute to make a modeling language quick to learn, simple to use, easy to implement by tool vendors, and open to extensibility. The design of IFML adheres as much as possible to the following “golden” rules:
- Conciseness: the number of diagram types and concepts needed to express the salient interface and interaction design decisions is kept to the minimum. In particular, the IFML visual syntax conveys the front-end model using a single diagram. This design simplifies the model editing and maintenance processes, because references between different types of diagrams need not be maintained and only the internal coherence among the various elements of a single type of diagram must be preserved.
- Inference from the context: whenever something can be deduced from existing parts of the model, inference rules at the modeling level automatically apply default modeling patterns and details, avoiding the need for modelers to specify redundant information. For example, parameter passing rules between different model elements, which are ubiquitous and cumbersome to specify, are inferred from the context as often as possible.
- Extensibility: adaptation to novel requirements, interaction modalities, and technologies must be planned in the language design. IFML builds upon a small set of core concepts that capture the essence of interaction: the interface (containers), stimuli (events), content (components and data binding), and dynamics (flows and actions). By design, these concepts are meant to be extended to mirror the evolution of technologies and devices. Thus, IFML incorporates standard means for defining new concepts, such as novel interface components or event types. The OMG standard already comprises examples of extensions, and this book illustrates many more cases that ease the specification of web, desktop, and mobile applications. Time and practice will show if the core of IFML is sufficiently technology neutral to enable extension to novel interaction paradigms that are possibly very different from the ones for which the language was initially conceived.
- Implementability: models that lack adequate tool support and cannot be used to produce the code are quickly abandoned. IFML is a platform-independent language but has been designed with executability in mind. This is obtained through model transformations and code generators to ensure that models can be mapped easily into executable applications for various platforms and devices. Chapters 10 and 11 present some techniques for implementing IFML specifications in several platforms, discuss the tool support requested in general for making the language usable, and illustrate one specific tool that enables automation of the design process and code generation.
- Not everything in the model: sometimes the hardest choice in language design is what to leave out. IFML purposely ignores presentation aspects, because presentation is adversarial to abstraction (in graphic design, every pixel is important). It also delegates to external models the specification of aspects that, although relevant to the user interface, are not properly part of it. For example, the internal functioning of the actions triggered by the GUI can be described using an action model. If the action is the invocation of an object’s method, this can be described by referencing a method in a UML class; if the action is the invocation of an orchestration of web services, this can be described using a SoaML1 diagram; if the action is described by a complex behavior, this can be obtained by referencing a whole UML dynamic diagram (e.g., a sequence diagram or activity diagram). The content model underlying the application can be described with any structural diagram, such as a UML class diagram, a Common Warehouse Metamodel (CWM) diagram,2 an Entity-Relationship diagram, or an ontology.

## IFML in a Nutshell

To understand the aim and scope of IFML better, it may be useful to refer to the well-known Model–View–Controller (MVC) software architecture of an interactive application,1 shown in Figure 2.1. MVC distinguishes the application’s internal status and business logic (Model), their representation in the user interface (View), and the rules governing the response to the user’s interaction (Controller).

IFML mainly describes the view (i.e., the content of the front end and the user interaction mechanisms available in the interface). More precisely, IFML covers various aspects of the user interface:
- View structure: It expresses the general organization of the interface in terms of ViewContainers, along with their nesting relationships, visibility, and reachability.
- View content: It specifies what ViewContainers actually contain in terms of ViewComponents (i.e., elements for content display and data entry). ViewComponents that display content are further characterized by a ContentBinding, which expresses the source of the published content.
- Events: They are the occurrences that affect the state of the user interface. They can be produced by a user’s interaction, by the application itself, or by an external system.
- Event transitions: They specify the consequences of an event on the user interface, which can be a change of the ViewContainer, an update of the content on display, the triggering of an action, or a mixture of these effects.
- Parameter binding: It clarifies the input–output dependencies between ViewComponents, view containers, and actions.

For the sake of conciseness, IFML condenses all these perspectives within only one diagram type called an Interaction Flow Diagram. This is in contrast to other modeling languages such as UML, which rely on multiple diagrams for conveying the various facets of an application.

Besides describing the view part of the application, an IFML Interaction Flow Diagram also provides the hooks to connect it with the model and controller parts:
- With respect to the controller, IFML represents the effects of the user’s interactions. It defines the events produced in the view and the course of action taken by the controller in response to them, such as triggering a business component and updating the view.
- With respect to the model, IFML describes the data binding between the interface elements and the objects that embody the state of the application, as well the actions that are triggered by the user’s interactions.

Figure 2.2 shows as an initial example the IFML model of a simple interface: the view structure consists of three ViewContainers (“ProductCategories,” “ProductOfCategory,” and “ProductInformation”), which reflect the top-level organization of the GUI in three distinct pages. The model shows the content of each ViewContainer. For example, the “ProductCategories” ViewContainer comprises one ViewComponent called “CategoryList.” This notation represents the content of the respective page in the GUI (i.e., a list of product categories). Events are represented in IFML as circles. The “SelectCategory” event specifies that the “CategoryList” component is interactive. In the GUI, the user can select one of the categories to access a list of its products. The effect of the “SelectCategory” event is represented by the arrow emanating from it (called InteractionFlow in IFML), which specifies that the triggering of the event causes the display of the “ProductOfCategory” ViewContainer and the rendering of its “ProductList” ViewComponent (i.e., the list of products of the selected category). The input–output dependency between the “CategoryList” and the “ProductList” ViewComponents is represented as a parameter binding (the IFML ParameterBindingGroup element in Figure 2.2). The value of the “SelectedCategory” parameter, which denotes the object selected by the user in the “CategoryList” ViewComponent, is associated with the value of the input parameter “Category,” which is requested for the computation of the “ProductList” ViewComponent.

### Overview of IFML Main Concepts

An IFML diagram consists of one or more top-level ViewContainers (i.e., interface elements that comprise components for displaying content and supporting interactions).

Figure 2.3 contrasts two different organizations of the GUI: (a) an e-mail application (desktop or rich Internet application) consisting of a top-level container with embedded sub-containers at different levels, and (b) an e-commerce web site that organizes the user interface into different independent view containers corresponding to page templates.

Each view container can be internally structured in a hierarchy of subcontainers. For example, in a desktop or rich Internet application, the main window can contain multiple tabbed frames, which in turn may contain several nested panes. The child view containers nested within a parent view container can be displayed simultaneously (e.g., an object pane and a property pane) or in mutual exclusion (e.g., two alternative tabs). In the case of mutually exclusive (XOR) containers, one could be the default container, which is displayed by default when the parent container is accessed. The meaning of a container can be specified more precisely by adding a stereotype to the general-purpose construct. For instance, a ViewContainer can be tagged as «window», as in the case of the “Mail” ViewContainer in Figure 2.4, to hint at the nature of its expected implementation.

In Figure 2.4, the “Mail” top-level container comprises two subcontainers, displayed alternatively: one for messages and one for contacts. When the top level container is accessed, the interface displays the “Messages” ViewContainer by default.

A ViewContainer can contain ViewComponents, which denote the publication of content (e.g., a list of objects) or the input of data (e.g., entry forms).

Figure 2.5 shows the notation for embedding ViewComponents within ViewContainers. The “Search” ViewContainer comprises a “MessageKeywordSearch” ViewComponent that represents a form for searching; the “MailBox” ViewContainer comprises a “MessageList” ViewComponent that denotes a list of objects.

A ViewComponent can have input and output parameters. For example, a ViewComponent that shows the details of an object has an input parameter corresponding to the identifier of the object to display. a data entry form exposes as output parameters the values submitted by the user. and a list of items exports as output parameter the item selected by the user.

A ViewContainer and a ViewComponent can be associated with events to express that they support user interaction. For example, a ViewComponent can represent a list associated with an event for selecting one or more items, a form associated with an event for input submission, or an image gallery associated with an event for scrolling though the gallery. IFML events are mapped to interactors2 in the implemented application. The way in which such interactors are rendered depends on the specific platform for which the application is deployed and is not captured by IFML. Rather, it is delegated to transformation rules from a platform-independent model (PIM) to a platform-specific model (PSM). For example, the scrolling of an image gallery may be implemented as a link in an HTML application and as a swipe gesture handler in a mobile phone application.

The effect of an event is represented by an interaction flow, which connects the event to the ViewContainer or ViewComponent affected by the event. For example, in an HTML web application the event produced by the selection of one item from a list may cause the display of a new page with the details of the selected object. This effect is represented by an interaction flow connecting the event associated with the list component in a top-level ViewContainer (the web page) with the ViewComponent representing the object detail, which is positioned in a different ViewContainer (the target web page). The interaction flow expresses a change of state of the user interface. The occurrence of the event causes a transition from a source to a target web page.

For example, in Figure 2.6 the “MailBoxList” ViewComponent shows the list of available mailboxes and is associated with the “MailBoxSelection” event, whereby the user can open the “MailBox” ViewContainer and access the messages of the mailbox selected in the “MessageList” ViewComponent .

An event can also cause the triggering of an action, which is executed prior to updating the state of the user interface. The effect of an event firing an action is represented by an interaction flow connecting the event to an action symbol (represented by a hexagon). For example, in a mail management application, the user can select several messages from a list and choose to delete them. The selection event triggers a delete action, after which the ViewContainer is displayed again with an updated list. The result of action execution is represented by an interaction flow that connects the action to the affected ViewContainer or ViewComponent.

In Figure 2.7, the “Message toolbar” ViewContainer is associated with the events for deleting, archiving, and reporting mail messages. Such events are connected by a flow to an action symbol (a labeled hexagonal icon), which represents the business operation. The outgoing flow of the action points to the ViewContainer displayed after the action is executed; if the outgoing flow of an action is omitted, this means that the same ViewContainer from which the action was activated remains in view (as illustrated by the “Archive” and “Report” actions in Figure 2.7).

The model of Figure 2.7 does not express the objects on which the business actions operate. Such an input–output dependency between view elements (ViewContainers and ViewComponents) or between view elements and actions requires the specification of parameter bindings associated with interaction flows. More specifically, two kinds of interaction flows can host parameter bindings: navigation flows, which represent navigation between view elements, and data flows, which express data transfer only but are not produced by user interaction. Parameter binding rules are represented by annotations attached to navigation and data flows, as shown in Figure 2.8.

In Figure 2.7, the “MessageToolbar” ViewContainer has an input parameter “MessageSet” whose value is set to the messages selected from the “MessageList” ViewComponent when the user triggers the “MessageSelection” event. Another parameter binding rule is associated with the Delete, Archive and Report events; the value of the “MessageSet” parameter is bound to the “InputMessages” parameter of the triggered action.

### Role of IFML in the Development Process

The development of interactive applications is typically managed with agile approaches, which traverse several cycles of “problem discovery” / “design refinement” / “implementation.” Each iteration of the development process generates a prototype or a partial version of the system. Such an incremental lifecycle is particularly appropriate for modern web and mobile applications, which must be deployed quickly and change frequently during their lifetime to adapt to user requirements. Figure 2.9 schematizes a possible development process and positions IFML within the flow of activities.

Requirements specification collects and formalizes the information about the application domain and expected functions. The input is the set of business requirements that motivate the application development and all the available information on the technical, organizational, and managerial context. The output is a functional specifications document comprising:
- the identification of the user roles and of the use cases associated with each role;
- a data dictionary of the essential domain concepts and of their semantic relationships; and
- the workflow embodied in each use case, which shows how the main actors (the user, the application, and possibly external services) interact during the execution of the use case.

In addition, nonfunctional requirements must also be specified, including performance, scalability, availability, security, and maintainability. When the application is directed to the general public, requirements about the look and feel and the usability of the interfaces assume special prominence among the nonfunctional requirements. User-centered design practices that rely on the construction of realistic mock-ups of the application functionality can be applied. These mock-ups can be used for the early validation of the interface concepts and then serve as the basis for creating more detailed and technical specifications during the front-end modeling phase.

Domain modeling3 organizes the main information objects identified during requirements specification into a comprehensive and coherent domain model. Domain modeling specifies the main information assets identified during requirements specification into a domain model, which is a (typically visual) representation of the essential objects, their attributes and associations. The first conceptual data modeling language, the Entity-Relationship model, was proposed in 1976, and ever since new modeling languages have been proposed, including UML. At the same time, modeling practices and guidelines have been consolidated; in particular, domain modeling for interactive applications exploits suitable design patterns, discussed in chapter 3. The entities and associations of the domain model identified during domain modeling are referenced in the front-end design models, to describe what pieces of data are published in the interface.

Front-end modeling maps the information delivery and data manipulation functionality dictated by the requirements use cases into a front-end model. Front-end modeling operates at the conceptual level, where IFML comes into play. The designer may use IFML to specify the organization of the front end in one or more top-level view containers, the internal structure of each view container in terms of subcontainers, the components that form the content of each view container, the events exposed by the view containers and components, and how such events trigger business actions and update the interface.

Business logic modeling specifies the business objects and the methods necessary to support the identified use cases. UML static and dynamic diagrams are normally employed to highlight the interfaces of objects and the flow of messages. Process-oriented notations—such as UML activity and sequence diagrams, BPMN process models, and BPEL service orchestrations—provide a convenient way to represent the workflow across objects and services. The actions specified in the business logic design can be referenced in the front-end model to show which operations can be triggered by interacting with the interface.

Data, front-end, and business-logic design are interdependent activities executed iteratively. The precedence order of Figure 2.9 is only illustrative. In some organizations, work could start from the design of the front end and the data objects and actions could be discovered at a later stage by analyzing what information is published in the interface and what operations are requested to support the interactions.

Architecture design is the process of defining the hardware, network, and software components that make up the architecture on which the application delivers its services to users. The goal of architecture design is to find the mix of these components that best meets the application requirements in terms of performance, security, availability, and scalability, and at the same time respects the technical and economic constraints of the project. The inputs of architecture design are the nonfunctional requirements and the constraints identified during business requirements collection and formalized in the requirements specifications. The output may be any specification that addresses the topology of the architecture in terms of processors, processes, and connections, such as UML deployment diagrams.

Implementation is the activity of producing the software modules that transform the data, business logic, and interface design into an application running on the selected architecture. Data implementation maps the domain model onto one or more data sources by associating the conceptual-level constructs with the logical data structures (e.g., entities and relationships to relational tables). Business logic implementation creates the software components needed to support the identified use cases. The implementation of individual components may benefit from the adoption of software frameworks, which organize the way in which fine-grain components are orchestrated and assembled into larger and more reusable functional units and also cater to nonfunctional requirements like performance, scalability, security, and availability. Business logic may also reside in external services, in which case implementation must address the orchestration of calls to remote components such as web APIs (Application Programming Interfaces). Interface implementation translates the conceptual-level ViewContainers and ViewComponents into the proper constructs in the selected implementation platform. ViewContainers may interoperate with business objects deployed either in the client layer or in the server layer.

Testing and evaluation verify the conformance of the implemented application to the functional and nonfunctional requirements. The most relevant concerns for interactive applications testing are:
- Functional testing: the application behavior is verified with respect to the functional requirements. Functional testing can be broken down into the classical activities of module testing, integration testing, and system testing.
- Usability testing: the nonfunctional requirements of ease of use, communication effectiveness, and adherence to consolidated usability standards are verified against the produced front end.
- Performance testing: the throughput and response time of the application must be evaluated in average and peak workload conditions. In case of inadequate level of service, the deployment architecture, including the external services, must be monitored and analyzed to identify and remove bottlenecks.

Deployment is the activity of installing the developed modules on top of the selected architecture. Deployment involves the data layer, the software gateways to the external services, and the business and presentation layer, where the interface modules and the business objects must be installed.

Maintenance and evolution encompass all the modifications applied after the application has been deployed in the production environment. Differently from the other phases of development, maintenance and evolution are applied to an existing system, which includes both the running application and its related documentation.

IFML models are the result of front-end design, but their production has important implications for other development activities as well.
- Domain modeling may specify entities and associations whose purpose is to aid the categorization and retrieval of the main business objects for a better user experience. We discuss this practice in chapter 3.
- Business logic modeling identifies the available operations and defines their possible outcomes and output, which affect the status of the interface. Chapter 6 discusses the interplay between front-end and business-logic modeling.
- Implementation may exploit model transformations and code generation to produce prototypes of the user interface or even fully functional code. In chapter 10 we discuss how to implement IFML models manually in some representative software platforms, and then in chapter 11 we exemplify the automation of the development activities achieved with model-driven tools.
- Testing and evaluation can be anticipated and performed on the IFML models rather than on the final code. Model checking may discover inconsistencies in the design of the front end (e.g., unreachable statuses of the interface) and suggest ways to refactor the user interface for better usability (e.g., recommend uniform design patterns for the different types of user interactions, such as searching, browsing, creating. modifying, and deleting objects).
- Finally, maintenance and evolution benefit most from the existence of a conceptual model of the application. Requests for changes are analyzed and turned into changes at the design level. Then, changes at the conceptual level are propagated to the implementation, possibly with the help of model-to-code transformation rules. This approach smoothly incorporates change management into the mainstream production lifecycle and greatly reduces the risk of breaking the software engineering process due to the application of changes solely at the implementation level.

### A Complete Example

As a conclusion to this brief introduction of IFML, we present a simple, yet complete, example. The application is an online store where the user can browse products, such as books, music, and software, and add products to his shopping cart, as shown by the UML use case diagram of Figure 2.10.

The application has a web front end. In the “Browse books” use case, the user accesses a home page that contains a list of product categories. Clicking on a product category such as “Books” leads to a page displaying the summary data about all the items of that category. Clicking on a “See more” associated with one item’s summary opens a page where the full details of the selected object are presented. Figure 2.11 shows the mock-ups of the application front end supporting the “Browse books” use case.

When looking at the details of an item, the user can press the “Add to cart” button to add the item to his virtual shopping cart. A modal window appears where the user can specify the quantity of goods he wants to purchase. After submitting the desired quantity, a confirmation pop-up window is presented to acknowledge the addition of the product to the cart. Figure 2.12 shows the mock-ups of the interface supporting the “Manage cart” use case.

The IFML model of the Bookstore application contains the five ViewContainers shown in Figure 2.13.

The ViewContainers are annotated with stereotypes (such as H, for “Home,” L for “Landmark,” and “Modal” and “Modeless”) that further specify their properties. These are discussed in chapter 4.

The ViewContainers definition is refined by specifying the ViewComponents they comprise, as illustrated in Figure 2.14.

Interactivity is represented by adding the relevant events and specifying the interaction flows they trigger, along with the parameter binding between the source and the target components of the interaction flows. The model of Figure 2.15 shows that the “CategoryList” ViewComponent supports an interactive event “SelectCategory,” whereby the user can choose a category from the index. As a result, the “ProductOfCategory” page is displayed, and the “ProductList” ViewComponent shows the items corresponding to the chosen category. The input–output dependency between the “CategoryList” and the “ProductList” ViewComponents is represented by the parameter binding group, which associates the “SelectedCategory” output parameter of the source component with the “Category” input parameter of the target component. The same modeling pattern is used to express the interaction for selecting a product from the “ProductList” component and then accessing its data in the “ProductDetails” component.

Some event may trigger the execution of a piece of business logic. As an example, Figure 2.12 and Figure 2.16 show the activation of an action for inserting items in the shopping cart. After the user presses the “Add to cart” button associated with the “ProductDetails” component, a modal window appears asking for the quantity of items desired. The quantity submission event triggers the execution of the “Add to cart” action. The “Quantity” value from the Form ViewComponent and the “DisplayedProduct” parameter from the “ProductDetails” ViewComponent are submitted as input parameters to the “Add to cart” action. Once the action is completed, a confirmation window is displayed.

Notice that the binding of the “Quantity” output parameter is associated with an interaction flow, which denotes the effect of a submit event that requires the user’s interaction. Conversely, the binding of the “DisplayedProduct” parameter is associated with a data flow, which merely expresses an input–output dependency automatically performed by the system and not triggered by a user’s interaction.

## Interface Organization

The specification of the interface in IFML is organized hierarchically using modularization constructs called ViewContainers.

### ViewContainers
A ViewContainer is an element of the interface that aggregates other view containers and/or view components displaying content.
In practice, a ViewContainer may represent a physical interface artifact such as a window or a page of a web application. But it can also denote a purely logical aggregation of other view containers, such as a section of a large web portal constituted by several pages dealing with a homogeneous subject.
ViewContainers support navigation, which is the change of focus from one container to another. To specify that a ViewContainer is the source of a navigation command, it is necessary to associate it with an event.

### Events
An Event is an occurrence that can affect the state of the application by causing navigation and/or passing parameters. Events may be produced by a user interaction (ViewElementEvent), by an action when it finishes its execution normally or exceptionally (ActionEvent), or by the system in the form of notifications (SystemEvent).
A ViewElementEvent is an Event that may be triggered by the user while interacting with ViewContainers, ViewComponents, and parts thereof called ViewComponentParts.
The effect of user interaction—that is, the target ViewContainer displayed after a ViewElementEvent has occurred—is specified by means of a NavigationFlow, denoted as a directed arc connecting the event symbol to the target view container.

### NavigationFlow
A NavigationFlow represents the navigation or the change of the view element in focus, the triggering of an Action, or the reaction to a SystemEvent. NavigationFlows are activated when Events are triggered. They connect Events owned by ViewContainers, ViewComponents, ViewComponentParts, or Actions with other ViewContainers, ViewComponents, ViewComponentParts, or Actions.
Figure 4.1 shows a very simple IFML model exemplifying these concepts, together with a hypothetical rendition.
“Source” and “Target” are ViewContainers, denoted as UML classifiers. “ClickMe” is an Event, represented as a circle associated with the owning ViewContainer. The NavigationFlow, denoted by an unlabeled directed arrow, connects the event named “ClickMe” of the “Source” ViewContainer to the “Target” ViewContainer, indicating that the occurrence of the “ClickMe” event causes the display of the “Target” ViewContainer.
Notice that some model features, such as the name of the ViewContainers and of the Event, are purposely shown also in the rendition. This is to highlight that the model features can be employed to create the implementation. For example, the name of the ViewContainer could be used to produce the title of a window or the name and URL of a web page, and the name of an Event could be exploited to create the text of a hyperlink anchor or a button label.

## View Container Nesting

Most interfaces organize the content and interaction commands presented to the user into a regular structure to enhance usability. For example, many web pages have a central content area and one or two columns for collateral items such as menus, search bars, and ads. Window-based interfaces split the work area into several panels and use tabbing to present alternative views of the work items.
IFML models the structure of the interface by means of nested ViewContainers. Nested ViewContainers express the organization of the interface at a conceptual level but necessarily have an interpretation that depends on the platform where the interface is deployed. Two typical situations arise:
- In window-based platforms, such as Java Swing or Windows.NET, the interface is normally hosted within one top-level container.
- In a pure HTML web application, the interface is normally fragmented across a set of independent page templates, which means that there is no top-level ViewContainer. Rather, one ViewContainer is elected as the one accessed by default (the so-called “Home Page”).
The advent of rich Internet applications has blurred the distinction between window-based and page-based interfaces, so it is not uncommon to see interfaces that have an organization that stands in the middle between the two extremes. This is in line with the single page development paradigm.
In the rest of this section, we proceed in the explanation of the features of ViewContainers from a platform-independent perspective. We will come back to the influence of platform-dependent features on design when discussing interface design patterns later in this chapter. In chapter 7, we will present some extensions to IFML conceived for desktop, web, and mobile development, which customize the terminology and concepts of IFML to make the language closer to the expectations of developers of these popular classes of solutions.
Nested ViewContainers may be in conjunctive form, which means that they are displayed together, or in disjunctive form, which means that the display of one ViewContainer replaces another ViewContainer. The property of disjunctiveness is explicitly associated with the enclosing container with the notation shown in Figure 4.2: a XOR label before the name of the ViewContainer. By default, ViewContainers display their inner ViewContainers in conjunctive form.
Figure 4.3 shows an example of disjunctive ViewContainers from the e-mail application used as a running example. The interface consists of a top-level ViewContainer from which the user can access either the “MailMessages” ViewContainer or the “Contacts” ViewContainer.

## View Container Navigation

ViewContainers support a basic form of navigation, which we call content-independent navigation to mark the distinction with the content-dependent navigation described in chapter 5.
Content-independent navigation is expressed by associating a navigation event to a ViewContainer and by specifying the target of the navigation with an InteractionFlow. An example of this design pattern was illustrated in Figure 4.1.
The meaning of content-independence is that user interaction does not depend on the content of the source and destination ViewContainers. In implementation terms, it is not necessary to associate parameter values with the interaction in order to compute the content of the target ViewContainer. This behavior is in contrast to content-dependent navigation, discussed in chapter 5.

## View Container Relevance and Visibility

ViewContainers are characterized by some distinguishing properties that highlight their “importance” in the organization of the interface.

### Default ViewContainers
The default property characterizes the ViewContainer presented by default when its enclosing ViewContainer is accessed.
Default view containers are denoted by a “D” within square brackets placed at the top-left corner of the view container.

### Landmark ViewContainers
The landmark property characterizes a ViewContainer that is reachable from all the other ViewContainers nested within its enclosing ViewContainer (i.e., from its sibling ViewContainers) and from their subcontainers.
Landmark view containers are denoted by an “L” within square brackets placed at the top-left corner of the view container.
Figure 4.4 shows an example of the landmark and default properties in the e-mail application. When the user starts the application the “Mail” ViewContainer is accessed. The default subcontainer “MailMessages” is displayed, whereas the alternative ViewContainer “Contacts” remains hidden. Both “MailMessages” and “Contacts” are defined as landmarks, which means it is always possible to access the one that is not in view from the one that is in view.
The landmark property is an example of a construct introduced for model usability. It does not augment the expressive power of IFML, because the access to ViewContainers can be represented explicitly with navigation flows, but reduces the burden of model specification and augments the readability of diagrams. Figure 4.5 illustrates on a small scale example why this is true. It shows two equivalent IFML diagrams. In the diagram on the left, the ViewContainers nested inside the Top ViewContainer are marked as landmarks, which means that every ViewContainer is the target of an implicit navigation flow pointing to it from the sibling ViewContainers. The diagram on the right explicitly shows these navigation flows and the events triggering the navigation. The meaning conveyed by the diagram on the left is that a landmark ViewContainer can be reached from any other ViewContainer of the enclosing module. If an interface contains many containers, the landmark property significantly reduces the number of events and navigation flows to be drawn and makes the diagram much more readable.
Figure 4.6 shows an example with nested ViewContainers. ViewContainer “One” is landmark and thus accessible from its sibling ViewContainers and their children (i.e., from the ViewContainers “Two,” “Three,” and “Four”). The same applies to ViewContainer “Two.” Again, the use of the landmark property avoids cluttering the diagram with many events and navigation flows.

## Windows

IFML provides a set of specializations of the ViewContainer concept that allow one to represent more precisely the behavior of the container-level navigation.

### Window
A Window is a specific kind of ViewContainer that represents a window in a user interface. A Window ViewContainer can be tagged as Modal or Modeless depending on its behavior with respect to the user interaction. A Modal window opens as a new window and disables the interaction with the background window(s) of the application; a Modeless window opens as a new window and still allows interaction with the other pieces of the user interface.
Navigation from a source window to a target window (not tagged as Modal or Modeless) implies that the source window disappears and is replaced by the target. If the target Window is tagged as Modal or Modeless instead, the new window will be superimposed onto the old one and will behave as modal or modeless respectively. Window, Modal, and Modeless specializations can be specified as stereotypes of the ViewContainer classifier, as shown in Figure 4.7.
Navigation between Windows “Step 1” and “Step 2” implies that “Step 2” substitute “Step 1” on the screen. Navigations from “Submission” to “Confirmation” and “ToolsMenu” will open the two new windows in front of the old one and will respectively grant modal and modeless behavior.

## Context and Viewpoint

The composition of the interface is not necessarily a static concept. Many applications update the interface organization and content at runtime, based on information about the context of the user interaction. For example, a mobile application can deliver alerts based on the current position of the user, and a web-based portal may exploit the information of the personalization subschema, introduced in chapter 3, for publishing user profile data and personalized recommendations.
To support the dynamic adaptation of the interface, IFML comprises concepts that capture both the design-time adaptation requirements set by the developer and the runtime values set by the application, which are necessary for deciding which adaptations to apply based on the interaction context of the user. The notion of context provided by IFML is purposely very broad. It may encompass aspects such as the identity, role, geographic position, or device of the user.

### Context and ContextDimension
The Context is a descriptor of the runtime aspects of the system that determine how the user interface is adapted. A ContextDimension is a component of the Context.
IFML comes with various predefined extensions of the ContextDimension concept.

### UserRole, Device, and Position
The UserRole represents the role currently played by the user in the application. It comprises the attributes that the user’s profile should satisfy to enable the context.
Device represents the characteristics that a device possesses.
Position represents the availability of location and orientation information of the device used to access the application.
The predefined Context and ContextDimension elements can be extended to represent finer-grain or other context perspectives, such as network connectivity or temporal aspects.
The requirements for a Context to be active are expressed by OCL expressions, called ActivationExpressions.

### ActivationExpression
An ActivationExpression is a Boolean condition that determines whether the associated Context (or other IFML element) is active (if the condition is true) or inactive (if the condition is false).
Figure 4.8 shows the IFML notation for an ActivationExpression that specifies when a Context is active. The specific context is represented as an instance (“AdminMobileContext”) of a classifier stereotyped as «context». The ActivationExpression is expressed as a stereotyped annotation associated to the Context instance.
The example of Figure 4.8 assumes that the “UserRole” ContextDimension has an attribute called “RoleName” that specifies the role that the user should fulfill in a role-based access control (RBAC) system. It also assumes that the “Device” ContextDimension has two attributes. “Type” identifies the class of device, while “Size” indicates the dimensions of the screen. The specification of Figure 4.8 therefore mandates that the “CustomerMobileContext” is enabled when the user’s access device is a small screen tablet and the role granted after login is that of a registered customer.
The evaluation of an ActivationExpression associated with a context requires that the values of the relevant ContextDimensions be recorded at runtime. Such runtime values can be represented in IFML as ContextVariables.

### ContextVariable
A ContextVariable is a runtime variable that holds information about the usage context. It specializes into SimpleContextVariable (of a primitive value type) and DataContextVariable (referencing a DataBinding).
ContextVariables enable a form of fine-grain interface adaption, as we will see in chapters 7, 8, and 9. They can be used in ActivationExpressions associated with ViewElements to condition their visibility based on the situation. Another, coarser-grain form of interface adaptation is achieved by using ViewPoints, which denote whole application designs tailored for a specific context.

### Viewpoint
A ViewPoint is the specification of an entire interface model that is active only when a specific Context is enabled.
The enablement of the ViewPoint is dynamic and governed by the ActivationExpression associated with the Context. When the ActivationExpression is satisfied, the Context becomes active and so does the associated ViewPoint with all the ViewElements and Events contained in it.
Figure 4.9 shows an example of ViewPoint specification. Two ViewPoints are defined (“Admin” and “Editor”) that contain different interface models for the two distinct roles. They are associated with the contexts that specify the activation requirements of the ViewPoints.
In summary, the ContextDimensions express the enabling dimensions of the Context, and an ActivationExpression can be used to dictate the required values for such ContextDimensions. The actual runtime values for a specific user are represented by ContextVariables. When the relevant runtime values of the ContextVariables match the required values for the ContextDimensions in the ActivationExpression, the Context is enabled. The enabled Context in turn identifies the ViewPoint (i.e., the variant of the interface) to be used. Finer-grain adaptation can be achieved using ContextVariables in ActivationExpressions associated with individual element of the interface.
The values of the ContextVariables can also be used to publish or to put to work the content of the personalization schema
- A ContextVariable holding the user’s identity (e.g., the “username” attribute) permits the application to look up the appropriate instance of the “User” class of the personalization subschema, retrieve profile data and personal objects from the database, and publish them in the interface.
- A ContextVariable holding the role of an authenticated user can be used to look up the appropriate instance of the “Group” class in the personalization subschema, retrieve the permissions of the user, and adapt the interface content and actions to such permissions.
In chapter 7, we put these concepts to work in various examples of the adaptation of the interface for web and mobile applications. In chapter 8, we discuss how to set the ContextVariables explicitly based on user interaction (e.g., as the effect of a login Action) and how to use them in applications exploiting the identity and role of the user.

## User Interaction Patterns

The proper organization of the interface is paramount for getting a good and user-friendly experience. IFML allows the designer to express such an organization at a conceptual level before committing to the implementation architecture. To support the design of the interface structure, we introduce a set of guidelines based on user interaction patterns, reusable models that effectively address a recurrent set of requirements in the design of user interfaces. When most users become accustomed to a successful pattern, new applications tend to implement the same design to reduce the learning curve and induce a sense of familiarity. User interaction patterns are classified into various categories, based on the concern addressed.
We will use a pattern naming convention to help designers immediately identify the purpose of a pattern. The name of a pattern is structured as XY-Z, where:
- X is the category of pattern. For instance, interface organization patterns start with the letter “O.”
- D is the deployment platform. For instance, desktop patterns are labeled with “D,” web with “W,” and mobile with “M.” The letter “G” (for “general”) is reserved for cross-platform patterns that apply irrespective of the deployment platform.
- Z is a mnemonic label identifying the specific pattern.
For instance, a pattern could be named OD-SWA (as in the first example described in section 4.8.1.1).

## Interface Organization Patterns and Practices

An interface organization pattern is a user interaction pattern that focuses on the hierarchical structure of the user interface. Different interface organization patterns have emerged for different classes of applications and for the various delivery platforms and access devices. This section reports some of the best-known patterns in this category, classified by platform (desktop, web, and mobile). Other categories of patterns are presented in the next chapters.

### Desktop Interface Organization Patterns

In desktop applications—and more recently in single-page rich Internet applications—the entire user interface is hosted within a single topmost ViewContainer, which has an articulated internal structure based on a hierarchy of nested ViewContainers.

##### PATTERN OD-SWA: Simple work area

A typical functional division distinguishes a work area where the main tasks of the application are performed from one or more service areas, including ViewContainers either hosting commands (e.g., menu bars, tool bars) or supporting auxiliary tasks (e.g., console or error message panels, status bars).
Figure 4.10 shows the IFML model of the simple work area interface organization pattern with an example application (a text editor). The pattern simply comprises a top-level ViewContainer with embedded nested sub-ViewContainers.

##### PATTERN OD-MWA: Multiview work area

When the task supported by the application and the data or the objects to be manipulated grow in complexity, the simple work area organization can be refined. One extension is to allow for multiple alternative views of the object/data/task in the work area, as represented by View1 and View2 in Figure 4.11.
Figure 4.11 shows an example of the multiview work area interface organization. An image editor has a normal view shown by default (called “Home”) and a zoom view used for adjusting the zoom level of the image (called “View”).

##### PATTERN OD-CWA: Composite work area

An alternative way of breaking down complexity is to split the work area into subregions devoted to different subtasks or perspectives of the object/data/task, presented simultaneously to allow the user to switch without losing the focus on the item under consideration. In such a case, one subregion often hosts the principal representation of the object/data/task and the other regions support collateral properties or subtasks.
Figure 4.12 shows an example of a composite work area interface with an example application: a document editor, featuring the main work area with a set of associated panels plus a set of menu bars.

##### PATTERN OD-MCWA: Multiview composite work area

The decomposition of the work area into alternative perspectives and simultaneous partial views can be combined to achieve a nested structure that best fits the specific requirements of the task supported by the application. For example, the work area could be partitioned into partial views displayed simultaneously, and the main view could be organized into multiple perspectives. Another option could have the work area supporting alternative perspectives, each one composed of several partial views appropriate to a perspective, displayed simultaneously.
Figure 4.13 shows an example of a multiview composite work area: a programming language IDE has an editing and a debug view, the latter composed of several parts.

### Web Interface Organization Patterns

In web applications, the typical organization of the interface allocates functionality to multiple pages, either produced statically or generated dynamically by page templates or server side scripts. In this case, nested ViewContainers are still useful and can fulfill a twofold role. As with desktop applications, they may express the allocation of content and navigation within regions of a page (e.g., as is possible with HTML frames or through the use of JavaScript). In contrast to desktop applications, they may express the logical clustering of multiple pages that have some common characteristics, for the purpose of modularizing the web application and supporting cross-site navigation mechanisms.

##### PATTERN OW-MFE: Multiple front-ends on the same domain model

In many cases, the web is used as a technical architecture to deliver a set of applications on top of the same data, represented in the domain model. A classical case is that of content management systems (CMS). These applications support two roles, as shown in Figure 4.14: the content editor and the reader, which have different use cases and must be served by distinct front ends acting upon the same data. In such a scenario, the pages constituting the two applications could be clustered into two distinct top-level containers, one for the editor and one for the reader.
Such an organization brings several benefits:
- It expresses a functional modularization of the front end that could be exploited, for example, to partition the implementation effort across different teams.
- It allows ViewContainers to be used as resources in a role-based access control policy. Users with role “editor” will access the pages of the “Editor” ViewContainer, whereas users with role “reader” will access the pages of the “Reader” ViewContainer.
- It enables a better management of the implementation artifacts, including the deployment at different web addresses and the separation of graphic resource files.
Figure 4.15 shows an example of multiple front ends interface composition pattern applied to a content management application serving the roles and use cases illustrated in Figure 4.14. A top-level ViewContainer “Login” denotes a public page for logging into the application, common to both roles. Then two nested ViewContainers comprise the ViewContainers that denote the web pages specific to the use cases of each role.
The dynamic activation of the appropriate interface after a user request based on his role can be specified using the Context and Viewpoints introduced in chapter 3. For each role, a Context with the appropriate ActivationExpression on the “UserRole” ContextDimension can be defined and associated with a ViewPoint that comprises the ViewContainers of Figure 4.15 appropriate for that role.

##### PATTERN OW-LWSA: Large web sites organized into areas

ViewContainers also come handy for expressing the logical organization of many real-world web applications that exhibit a hierarchical structure whereby the pages of the site are clustered into sections dealing with a homogeneous subject. Nested ViewContainers can play the role of “site areas,” recursively structured into other subareas and/or pages. Most real-life web sites exhibit an organization into areas. For example, Figure 4.16 shows an interface fragment taken from a web site whose pages include a navigation bar with anchors pointing to the various areas of the site.
In chapter 7, we will exploit the native extension mechanism of IFML to introduce specializations of the ViewContainer concept that make the specification of web interface organization patterns more expressive.

### Mobile Interface Organization Patterns

Mobile interface organization must account for the reduced screen space of portable devices and for the usage context, whereby users often access the application in unconformable conditions, such as while standing or walking. Therefore, a consistent usage of the scarce screen space is the number one rule of interface organization to reduce the learning curve and minimize the interactions needed to perform tasks. This requirement constrains the top-level organization, which repeats consistently across mobile operating systems and individual applications.
In this section, we introduce only one high-level interface organization pattern. We defer to chapters 7 and 8 the illustration of several other design patters for mobile applications based on the interplay between the organization of the main interface containers and the content components.

##### PATTERN OM-MSL: Mobile screen layout

The basic organization of the interface of mobile applications maps the interface to a top-level grid that contains three regions: the header, the content area, and the footer, as shown in Figure 4.17.
The header is normally used for command menus and notifications. Part of the header may be reserved for operating-system notifications and therefore remains fixed across all applications. The content area normally has a simple layout that limits the use of multiple perspectives and nested panes to a minimum and exploits scrolling along one dimension to accommodate content that overflows the size of the screen. The footer region is normally allocated to system-level commands, such as general or application-specific settings menus.
This essential design pattern can be articulated in a variety of more specific forms depending on the device capacity, the content type, and the application requirements. Chapters 7 and 8 provide many examples of IFML extensions that make the models of mobile applications more expressive and introduce several design patterns that recur in different classes of mobile applications.
