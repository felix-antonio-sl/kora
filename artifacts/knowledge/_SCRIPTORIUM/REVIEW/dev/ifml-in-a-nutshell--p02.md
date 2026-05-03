---
_manifest:
  urn: urn:dev:kb:ifml-in-a-nutshell-p02
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
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:dev:kb:ifml-in-a-nutshell
---

# IFML in a Nutshell - Parte 02

## Running Example

We return to the running example of the e-mail management application started in chapter 3 to show how to model the organization of the interface.
When the user accesses the application, the interface presents by default the functionality for accessing mailboxes and managing messages, as shown in Figure 4.18.
An equivalent interface is available for contact management, which is accessed upon request. Its organization is shown in Figure 4.19.
The application lets the user always switch from one view to the other by means of a menu, as shown in Figure 4.20.
The message management interface comprises an area for working with mailboxes and messages. This area is displayed by default, as shown in Figure 4.18. If the user activates the compose command, the mailbox and message area is replaced with a message composer interface, shown in Figure 4.21. Similarly, if the user activates the “Settings” command, a pop-up panel for editing options and preferences is displayed, as shown in Figure 4.22.
The area for working with mailboxes and messages displays a search panel, a toolbar, and a mailbox/message display region, as visible in Figure 4.18. When a message is selected, the message list is replaced with the visualization of the message content, as shown in Figure 4.23.
The message search box alternates between two interfaces for searching: a simple keyword input field, visible in Figure 4.18, and an advanced search form with multiple fields, shown in Figure 4.24.
Figure 4.25 shows an excerpt of the IFML model that specifies the organization of the interface of the e-mail application sketched in Figures 4.18–4.24. The top ViewContainer (“Mail”) hosts two alternative subcontainers: one for message management and one for contact management. For brevity, we illustrate only the internal structure of the default ViewContainer (“Messages”). Its structure comprises two ViewContainers that are displayed together: “MessageSearch” and “MessageManagement.”
The “MessageSearch” ViewContainer comprises two mutually exclusive landmark subcontainers: “Search” (shown by default) and “FullSearch.” The “MessageManagement” ViewContainer comprises three mutually exclusive landmark subcontainers: “MailBox” (the default), “Settings,” and “MessageWriter.” The “MailBox” ViewContainer consists of the “Message Toolbar” and the “MessageViewer” containers displayed simultaneously. Finally, the “MessageViewer” ViewContainer comprises the “MessageList” and the “MessageDetails” subcontainers, which are visualized in alternative.

## Modeling interface content and navigation

ViewElements are distinguished in ViewContainers (already treated in chapter 4) and ViewComponents, which are the main subject of this chapter.
Events and InteractionFlows have been already introduced in chapter 4 but acquire a more interesting meaning in content and navigation modeling. They enable the specification content-dependent navigation, that is, a form of interaction that exploits the objects of the domain model. The simplest example of content-dependent navigation is the selection of items from a list. The user accesses a ViewComponent that displays a list of objects, selects one, and accesses another ViewComponent that displays detailed information about the chosen object.
On the one hand, content-dependent navigation is similar to content-independent navigation, described in chapter 4:

- It involves a source and a destination element and is expressed by means of an Event and of a NavigationFlow.

- On the other hand, it has important differences: typically the source and target of the navigation are ViewComponents (and not ViewContainers). Furthermore, the target ViewComponent normally depends on some data provided by the source ViewComponent; this dependency is expressed by associating one or more ParameterBinding specifications to the NavigationFlow.

The specification of ViewComponents can be done at different levels of precision:

- At the most abstract level, a ViewComponent is just a “box with a name,” as in the preliminary examples introduced in chapter 2 (e.g., see Figure 2.2). Its meaning is conveyed only by the name, without further details except for the optional specification of subcomponents specified with the IFML ViewComponentPart construct. Using this level of abstraction keeps the specification very general and easy to produce but may overlook important information needed for model checking and code generation.
- At an intermediate level of abstraction, IFML allows a standard way of binding ViewComponents to elements of the domain model. This is extremely useful to express, for example, that a ViewComponent “Index of Products” actually derives its content from the instances of a “Product” class of the domain model. This additional knowledge can be used for checking the consistency between the IFML model and the domain model and for automatically generating the data query that extracts the content of the “Index of Products” ViewComponent.
- At the most refined level, the ViewComponent construct can be extended with specialized subclasses to express specific ways in which content is presented or exploited to enable user interaction. For example, a List ViewComponent can be defined to represent a specific ViewComponent aimed at publishing an ordered set of objects from which the user can select one item. Extended components may have domain-dependent properties and thus enable deep model checking and full code generation.

In this chapter we discuss both the basic IFML notion of ViewComponent and the extensions already defined in the standard. In chapter 7 we illustrate how the designer can introduce novel extensions, using web and mobile application development as examples.

## What ViewContainers Contain: ViewComponents

A ViewContainer may comprise ViewComponents.

**ViewComponent**

A ViewComponent is any element that can display content in the user interface or accept input from the user.

Examples of ViewComponents are interface elements for visualizing the data of one object, for displaying a list of objects, data entry forms for accepting user input, and grid controls for displaying and editing data tables. A ViewComponent may have an internal structure consisting of one or more ViewComponentParts.

**ViewComponentPart**

A ViewComponentPart is an interface element or a structural property that may not live outside the context of ViewComponent.

The meanings of ViewComponent and of ViewComponentPart are left purposely broad. Their semantics are defined by the designer and conveyed by the component/part name. Figure 5.1 shows the graphic representation of ViewComponents and some exemplary renderings. As can be noted, at the highest level of abstraction only the name of the component is used to suggest the intended meaning.

## Events and Navigation Flows with ViewComponents

ViewComponents and ViewComponentParts can support interaction. This capacity is denoted by associating them with Events, which in turn enable NavigationFlows. Figure 5.2 shows an example of an interactive ViewComponent. The “ProductList” ViewComponent is associated with an Event “SelectProduct,” which is the source of a NavigationFlow leading to the “ProductDetails” ViewComponent. The meaning of this design pattern is that “ProductList” publishes a list of objects from which the user can select. The selection event triggers an interaction, whose effect is showing the information of the chosen object in the “ProductDetails” ViewComponent.
In content-based navigation, the source and destination ViewComponents can be positioned in different ViewContainers, as shown in Figure 5.2. In this case, the navigation event has the effect of showing the target ViewContainer and of triggering the computation of the ViewComponents present in it. The display of the target ViewContainer may impact the visualization of the source ViewContainer in one of two ways:
- If the source and target ViewContainers are mutually exclusive (either directly or because they are nested within mutually exclusive ViewContainers), the target replaces the source.

- Otherwise the target is displayed in addition to the source.

For example, Figure 5.3 shows the ViewComponents, Event, and NavigationFlow of Figure 5.2, but this time both the source and target ViewComponent are in the same ViewContainer. This indicates that the choice of one product in the list causes the display of the details in the same ViewContainer.

## Content Dependencies: Data Binding

ViewComponents publish content in the interface. It is therefore necessary to specify the source of the published content. This aspect is represented by means of the ContentBinding specification.

**ContentBinding**

A ContentBinding is a very general representation of the content source of a ViewComponent; its only attribute is the URI of the resource from which the content may be obtained.

Figure 5.4 shows a simple example of ContentBinding: the “FeedReader” ViewComponent is associated with a ContentBinding specification that references the URL of the feed provider.
To represent the common situation in which the content published by a ViewComponent originates from the objects of the domain model or from an external service, the ContentBinding concept is refined in two specializations: DataBinding and DynamicBehavior.

**DataBinding**

A DataBinding represents the provenance of content from objects of the domain model; it is characterized by features that specify the type of data, the criterion for selecting instances, and the attributes relevant for publication.

More precisely, a DataBinding is associated with:

- a reference to a domain model concept (depending on the type of domain model, the referenced concept can be a UML classifier—which may represent a class in the domain model, an XML file, a table in a database, etc.—or another element);

- a ConditionalExpression, which determines the specific instances to be extracted from the content source;
- one or more VisualizationAttributes, used by the ViewComponent to locate the data shown in the interface, such as an object attribute, a database column or an XML element or attribute; and

- an optional OrderBy ViewComponentPart, which lists one or more sorting criteria consisting of an attribute name and a sort direction (ASC or DESC for ascending or descending, respectively).

Figure 5.5 shows an example of a simple DataBinding. The “MessageList” ViewComponent draws its content from the “MailMessage” entity of the domain model. The DataBinding neither specifies which instances are to be published nor the attributes to be visualized, and so these aspects are left unspecified.
Figure 5.6 refines the example of Figure 5.5. The DataBinding contains an OCL ConditionalExpression “self.isRead = false,” which specifies that only the instances of the entity “MailMessage” with the attribute “isRead” equal to false should be published. The VisualizationAttributes ViewComponentPart specifies that the attributes “subject” and “date” should be used to display the objects, and the OrderBy ViewComponentPart indicates that they are sorted in descending order of date.
Note that because the conditional expression is defined within the DataBinding ViewComponentPart, the context of the expression is implicitly set to “MailMessage” (i.e., the object referenced by the DataBinding).

The DataBinding represents the association of a ViewComponent to the content elements in a declarative way, which facilitates the generation of the data extraction queries. An alternative way of expressing the content of a ViewComponent is through the DynamicBehavior element.

**DynamicBehavior**

A DynamicBehavior represents the data access of a ViewComponent in an operational way (e.g., through the invocation of a service or method that returns content).

For instance, a DynamicBehavior can be expressed by referencing any UMLBehavior or UMLBehavioralFeature.

Figure 5.7 shows an example of DynamicBehavior used to specify that the “TweetList” ViewComponent exploits the web API of an external service to publish content.

## Input-Output Dependencies: Parameter Binding

Content-dependent navigation allows expressing the very common situation in which one component displays content that depends on some previous interaction performed by the user. Examples are the display of the data of an object previously selected from a list, the display of the result list of a keyword search, and the drill-down into a hierarchy.

All these situations require expressing an input–output dependency between ViewComponents. The ViewComponent target of the navigation requires input provided by the source ViewComponent for retrieving the content to publish. An input–output dependency is described by means of the ParameterBinding construct.

**ParameterBinding and ParameterBindingGroup**

A ParameterBinding specifies that the value of one parameter, typically the output of some ViewComponent, is associated with that of another parameter, typically the input of another ViewComponent. When the input–output dependency involves several parameters at the same time, ParameterBinding elements are grouped into a ParameterBindingGroup.

Figure 5.8 shows an example of an input–output dependency. The “MessageList” ViewComponent displays the messages of the specific mailbox selected by the user in the “MBoxList” ViewComponent. The NavigationFlow is associated with a ParameterBindingGroup that contains the declaration of an input–output dependency: the value of the parameter “SelectedMailBox” (output of the “MBoxList” ViewComponent) is associated with the value of the parameter “MailBox” (input of the “MessageList” ViewComponent). The value of the “MailBox” parameter is used in the ConditionalExpression of the “MessageList” ViewComponent, specified by the following OCL expression:
```ocl
self.MailMessageGroup = MailBox
```
The OCL expression specifies that the instances of “MailMessage” to retrieve are those associated by the relationship role “MailMessageGroup” with the object identified by the value of the parameter “MailBox.” The pattern of Figure 5.8 provides an example of a ConditionalExpression that exploits an association in the domain model.
The transfer of parameters necessary for satisfying the input–output dependencies between correlated components does not always requires user intervention.
Figure 5.9 shows an example of such a situation. When one contact is selected in the “ContactList” ViewComponent, the details of the selected object are displayed in the “ContactInfo” ViewComponent. In addition, further information about the same object is displayed, namely, the list of addresses and e-mails in the “Addresses” and “Emails” ViewComponents respectively. These two components are displayed simultaneously with the “ContactInfo” ViewComponent after the selection from the list without any further user interaction. The input parameter needed for computing their content (the ID of the selected contact) is provided by a ParameterBinding associated with the DataFlows from the “ContactInfo” ViewComponent to the “Addresses” and “Emails” ViewComponents.

**DataFlow**

A DataFlow is an InteractionFlow that specifies that some parameters are supplied from a source to a target element, without any user’s interaction; the involved parameters are specified by means of a ParameterBindingGroup associated with the DataFlow.

DataFlows emanate directly from ViewComponents rather than from Events and are denoted with dashed arrows to distinguish them from NavigationFlows.

## Extending IFML with Specialized ViewComponents and Events

The examples of the previous sections introduced a rather rudimentary notion of ViewComponent. So far this concept is little more than a box. Its meaning is conveyed only by the name assigned to it by the designer. In this way, however, the model usability and semantics cannot be improved much. If “all boxes are equal,” tools could not check the correctness of the models or support the designer with useful inferences and shortcuts.
To allow deeper model checking and improve model usability, IFML supports the extension of the basic ViewComponents with user-defined specializations. Figure 5.10 illustrates the extensions of the base ViewComponent construct already provided in the IFML standard, which are still quite general. More extensions will be introduced in chapter 7 for web and mobile applications.
The List and Details ViewComponents just add a stereotype to the basic ViewComponent concept. The Form ViewComponent also adds novel ViewComponentParts (SimpleField and SelectionField).

### Data Publishing Extensions

IFML component extensions are represented in the model by stereotypes added to a ViewComponent. For the sake of conformance to the IFML standard, we use textual stereotyping, which is quite cumbersome for ViewComponents, especially when their names are long. However, a tool may replace the textual notation of stereotypes with a more concise representation to save screen space (e.g., small icons, font colors, textures).

**List ViewComponent**

A List ViewComponent is a ViewComponent used to display a list of objects retrieved through a ContentBinding. When the List ViewComponent is associated with an Event, it means that each object displayed by the component can be used to trigger the Event. Firing the Event causes the passing of the chosen instances as a parameter value to a target IFML element.

**Details ViewComponent**

A Details ViewComponent is a ViewComponent used to display the attribute values of one object retrieved through a ContentBinding. When the Details ViewComponent is associated with an Event, it means that the instance displayed by the component can be used to trigger the Event. Firing the Event causes the passing of the displayed instance as a parameter value to a target IFML element.

Figure 5.11 shows an example of List and Details ViewComponents connected with an event and a navigation flow. The “MessageList” publishes the list of all “MailMessage” instances. The “select” event indicates that the “MessageList” ViewComponent supports interaction (i.e., the user can click on one of the displayed object and trigger the event). The firing of the event produces the display of the “Message” Details ViewComponent, which receives as input the chosen “MailMessage” object.
The selection from a list is an event frequently associated with ViewComponents. It thus has a specific representation in IFML as an extension of the base Event concept, shown in Figure 5.11 (and previously in Figures 5.2, 5.3, 5.8, 5.9).

**SelectEvent**

A SelectEvent is a kind of Event that supports the selection of one or more elements from a set. When triggered, it causes the selected value(s) to be passed as a Parameter to the target of its associated NavigationFlow.

In chapter 6 we will introduce another refinement of the Event, the “select all” event, which is used to express an Event that supports the selection of all elements of a set.
Figure 5.12 shows an example that illustrates how adding more semantics to the model via IFML extensions can improve usability. The model representation is more concise than that of Figure 5.11, but the usage of extensions with precise semantics easily allows a tool (or a human reader) to infer that the two models are equivalent. Indeed, the List ViewComponent publishes a set of instances of the “MailMessage” class, the Details ViewComponent publishes one instance of the same class, and the “select” Event actually allows the user to select one item from the source ViewComponent and pass it to the target ViewComponent. Thus the designer could draw the more concise variant of Figure 5.12, sparing the effort of expressing the inferable ParameterBinding and ConditionalExpression.
The selection from a list can also include multiple items, as supported by the multichoice list ViewComponent.

**MultiChoiceList**

The MultiChoice List enables the selection and submission of multiple instances. It supports multiple event types. The standard select event expresses the selection of one element of the list, while the checking and unchecking events express the application or removal of a selection ticker on any element in the list. The set selection event denotes the submission of the entire set of objects, and the submit event denotes the submission of the currently selected objects.

An example of a multichoice list is shown in Figure 5.31 and in the multiple-object deletion pattern discussed in chapter 8.

### Data Entry Extensions

Besides content publishing, IFML extensions can also be used to express data entry. This is done using the Form ViewComponent extension.

**Form**

A Form is a ViewComponent that represents a data entry form.

A form comprises one or more ViewComponentParts that represent input fields (and thus are tagged with the Field stereotype).

**Field**

A Field is a subelement of a Form that denotes a typed value acquired from or displayed to the user.

Fields also represent Parameters for passing their values to other IFML elements. There are two kinds of fields: SimpleFields and SelectionFields.

**SimpleField**

A SimpleField is a kind of Field that captures a typed value. Such a value is typically entered by the user but can also be designated read-only or even hidden. The value of a SimpleField is an output Parameter that can be passed to other ViewElements or Actions.

As customary in data entry applications, form fields could also allow a quicker and more controlled type of interaction (e.g., the selection of values from a predefined set). This feature is captured by the SelectionField element.

**SelectionField**

A SelectionField is a kind of Field that enables the choice of one or more values from a predefined set.

Figure 5.13 shows an example of a Form with two SimpleFields and one SelectionField.
The mock-up rendition of Figure 5.13 hints at the fact that the type of the field can be used by the developer or by a code generation tool to produce the most appropriate interaction widget within the form.
Both simple and selection fields can be preloaded with values. Each Field also defines an input parameter of the Form that contains it so that its value can be preloaded with a value supplied by another IFML element. Alternatively, the provenance of the Field content can be expressed with a ContentBinding, if the content is extracted from domain model objects. Preloaded Fields behave as follow: a preloaded SimpleField displays a value to the user, who can overwrite it; a preloaded SelectionField displays multiple values to the user, who can choose the one(s) to submit. Each field also defines an output parameter of the Form that contains it, which assumes as value the entered value (for a SimpleField) or the selected value(s) (for a SelectionField) provided by the user.

Forms support interaction for submitting the content of their Fields. The basic data submission activity of the user can be represented by an extension of the generic Event construct called SubmitEvent.

**SubmitEvent**

A SubmitEvent is a kind of event that denotes the submission of one or more values. It triggers the Parameter passing from the ViewComponent owning the event to the ViewComponent or Action target of the NavigationFlow outgoing from the event.

Figure 5.14 shows an example of Form ViewComponent with one SimpleField and one SubmitEvent (note that the SubmitEvent is represented by an “enter button” icon). The “MessageKeywordSearch” Form ViewComponent is associated with the “SearchKey” SimpleField and with the “Search mail” SubmitEvent. The latter triggers an interaction that leads to the display of the “MessageList” ViewComponent, which publishes the messages that contain the search keyword in their title. The OCL expression that selects the set of instances whose title contains the input keyword is:
```ocl
if (keyword.size <= title.size) then
 Sequence(1..title.size- Keyword.size) -> exists(i|
 title.substring(i,i+Keyword.size) = Keyword)
 else
 false
```
which checks that the input keyword is a substring of the message title.

## Content and Navigation Patterns and Practices

As already mentioned in chapter 4, interface design patterns are IFML models that embody the solution to recurrent interface design problems. In the following, we discuss useful patterns that emerge frequently during the design of the content and interactivity of the user interface. The patterns described in this chapter are high level and platform independent. Platform-specific patterns are discussed in chapter 7.
We start by introducing content and navigation patterns, reusable models that effectively addresses a recurrent set of requirements in the design of the content and navigation in user interfaces. We prefix the name of platform-independent content and navigation patterns with CN.

### PATTERN CN-MD: Master Detail and PATTERN CN-MMD: Master Multidetail

The master detail pattern is the simplest data access pattern, already exemplified in Figure 5.11. A List ViewComponent is used to present some instances (the so-called master list), and a selection Event permits the user to access the details of one instance at a time. The master multidetail variant occurs when the object selected in the master list is published with more than one ViewComponents, as shown in Figure 5.9.

### PATTERN CN-MLMD: Multilevel Master Detail

This pattern, sometimes also called “cascaded index,” consists of a sequence of List ViewComponents defined over distinct classes, such that each List specifies a change of focus from one object (selected from the index) to the set of objects related to it via an association role. In the end, a single object is shown in a Details ViewComponent, or several objects are shown in a List ViewComponent. A typical usage of the pattern exploits one or more data access classes to build a navigation path to the instances of a core class. For example, Figure 2.2 provides an example of the multilevel master detail pattern exploiting the instances of the “Category” access class to access the instances of the “Product” core class.

### PATTERN CN-DEF: Default Selection

A usability principle suggests maximizing the stability of the interface by avoiding abrupt and far reaching changes of the view when they are not necessary. The default selection pattern helps improve the stability of interfaces that show pieces of correlated content and allow the user to make choices.

The basic master detail pattern and the multilevel master detail pattern exhibit possibly unwanted interface instability, as visible in Figure 5.3. When the ViewContainer is initially accessed, the first List ViewComponent is computed and appears rendered in the interface. However, the Details or List ViewComponent, which depends on a parameter value supplied by a user selection, cannot be computed, and thus the interface contains an “empty hole” corresponding to it. When the user selects one item from the list, then the missing parameter value becomes available and the content of the second ViewComponent can be computed, thus filling the hole but producing a possibly unwanted instability of the interface.
The default selection pattern resolves this problem by simulating a user selection at the initial access of the ViewContainer. A default value is chosen from the source ViewComponent and used to define the value of the parameter needed for computing the target ViewComponent. In this way, the user sees a stable interface initialized with a system-defined object or list, which the user can subsequently change by using the provided interactive events.
Figure 5.15 shows the notation for expressing the default selection pattern.
Besides the NavigationFlow outgoing from the select event, the pattern also includes a DataFlow, which expresses a parameter passing rule for supplying a default value when the page is accessed, in absence of user interaction.

## Data Entry Patterns

Data entry is one of the most important activities supported by the front end and one where usability requirements are most stringent. In the next sections, we illustrate some cross-platform patterns generally applicable to data entry interfaces, based on the usage of Form ViewComponents. We prefix the name of platform-independent data entry patterns with DE.

### PATTERN DE-FRM: Multifield Forms

The basic data entry pattern consists of a Form ViewComponent with several fields corresponding to such elements as the properties of an object to be created or updated, the criteria for searching a repository, or the parameter values to be sent to an external service.

Figure 5.16 shows an example of multi-field form for composing an e-mail message.
As Figure 5.16 illustrates, assigning a type with the fields adds useful information to the model. For example, a code generator may render a text editing field by means of a rich text editing widget or a Blob field with a file chooser window. Other examples are Boolean fields rendered as radio buttons and date fields rendered as calendars. We will show how to extend Fields to specify several usability hints in chapter 8.

### PATTERN DE-PLDF: Preloaded Field

In many situations, the data entered in a form modify or add to existing information. Examples include updating the description of a product in an online e-commerce web site or changing one’s profile in a social network. In each case, preloading fields with content augments the usability of the interface and reduces data entry errors.

Figure 5.17 shows the pattern for preloading a SimpleField and a SelectionField in two different ways. The “Categories” SelectionField incorporates a DataBinding element, which specifies that the values are extracted from the “name” attribute of the “Category” objects of the domain model. Conversely, the “Description” SimpleField is preloaded by means of a ParameterBinding associated with the DataFlow connecting the “ProductDetails” Form and the “UpdateProduct” ViewComponents. In this way, the text of the description attribute of the product object in display is also used to provide an initial value to the homonymous field in the Form.

Figure 5.18 shows another example of field preloading: a form for replying to an existing e-mail message, in which the fields of the new message are partly preloaded with the values of the original message. The “Reply” event associates the subject of the original message to the subject of the new message prefixed with the string “Re: ,” copies the recipient of the original message into the sender of the new message, and pulls the body of the original message into the body of the new message.

### PATTERN DE-PASF: Preassigned Selection Field

This design pattern helps when the user’s selection among a number of different choices can be inferred from available information (e.g., from profile data, previous choices, or the interaction context). In this case, the value of a SelectionField can be initialized with a ParameterBinding, as shown in Figure 5.19.
The “SignUp” ViewContainer shown in Figure 5.19 contains a “UserCountry” Details ViewComponent that retrieves the default country for a user by querying the Locale contextVariable and exposes an OutputParameter UserCountry. Such a piece of information is passed to the form “SignUp” as input parameter CountryPreselect to set the value of the “Country” SelectionField. Note the use of a DataFlow from the Details to the Form because no interaction is required except the association of the parameter with the SelectionField parameter value.

### PATTERN DE-DLKP: Data Lookup

This design pattern is useful when the data entry task involves a complex form with choices among many options, such as in the case of form filling with large product catalogues. In this case, a SelectionField can be conveniently supported by a data lookup ViewContainer, which contains a data access pattern such as a master details.

Figure 5.20 shows an example of data lookup. The “FillRequest” Form contains a SimpleField “ProductCode” that must be filled with the code of a product. An event “Pick” opens a ViewContainer (e,g, a modal window) whereby the user can navigate the product taxonomy and select the desired code. The product code chosen with the data lookup is assigned to the SimpleField “ProductCode” using a ParameterBinding.

### PATTERN DE-CSF: Cascade Selection Fields

The cascade selection field pattern is useful when the data entry task involves entering a set of selections that have some kind of dependency. The typical example is a form for entering user information, where the address is incrementally built by selecting the country, the state or province, and then the city. If this step by step selection is performed within a form with selection fields, the fields need to be dynamically updated according to the selection at the previous step. In this case, the list of states or provinces depends on the selected country, and the list of cities depends on the selected province. Figure 5.21 shows the IFML model that exemplifies this behavior. The selection of an element in the “Country” SelectionField triggers the calculation of the list of associated states to be shown in the “State” SelectionField.

### PATTERN DE-WIZ: Wizard

The wizard design pattern supports the partition of a data entry procedure into logical steps that must be followed in a predetermined sequence. Depending on the step reached, the user can move forward or backward without losing the partial selections made up to that point. Figure 5.22 shows a three-step wizard.
Notice that at each step the Form ViewComponent shows one Field, the one pertinent to the current step, and caches the values of the inputs of all steps in Parameters. The events and navigation flows for moving from one step to another are associated with a ParameterBinding that carries the current values of all the fields to keep track of interactions performed in previous steps. In this way, the user can go back and forth and—at the end—all the collected values are correctly submitted.

An alternative equivalent design can be that of associating a single copy of all the wizard parameters with the enclosing ViewContainer and updating such global parameters at each previous/next event.

## Search Patterns

Search patterns address recurrent problems in which user input must be matched against some content to retrieve relevant information. We prefix the name of platform-independent content search patterns with CS.

### PATTERN CS-SRC: Basic Search

The basic search pattern has already been exemplified in Figure 5.14, where a Form ViewComponent with one SimpleField is used to input a search key. This key is used as the value of a parameter in the ConditionalExpression of a List ViewComponent that displays all the instances of a class that contain the keyword. A variant of the pattern that searches the keyword in multiple attributes of the target class is obtained using disjunctive subclauses in the ConditionalExpression:
```ocl
if (keyword.size <= title.size) then
 Sequence(1..title.size - Keyword.size) -> c(i|
 title.substring(i, i + Keyword.size) = Keyword)
 else
 false
```
OR
```ocl
if (keyword.size <= body.size) then
 Sequence(1..body.size - Keyword.size) -> exists(i|
 body.substring(i, i + Keyword.size) = Keyword)
 else
 false
```
With the above expression, the keyword is searched in the title or in the body of a message.

### PATTERN CS-MCS: Multicriteria Search

The advanced multicriteria search pattern uses a Form ViewComponent with multiple Fields to express a composite search criterion. Figure 5.23 shows an example of multicriteria search pattern. The “Message full search” Form contains multiple Field elements for the user to fill. A ParameterBindingGroup assigns the field values to the parameters in the ConditionalExpression of the “MessageList” ViewComponent.

### PATTERN CS-FSR: Faceted Search

Faceted search is a modality of information retrieval particularly well suited to structured multidimensional data. It is used to allow the progressive refinement of the search results by restricting the objects that match the query based on their properties, called facets. By selecting one or more values of some of the facets, the result set is narrowed down to only those objects that possess the selected values. Figure 5.24 shows an example of faceted search applied to bibliography information retrieval.
The model of Figure 5.24 consists of a ViewContainer (“FacetedSearch”), which comprises a Form for entering the search keywords, a List for showing the query matches (“Results”), and two MultiChoice Lists (“Years” and “Venues”) for selecting facet values and restricting the result set. At the first access of the ViewContainer, no keyword has been provided yet by the user, and thus the ConditionalExpression of the “Results” List evaluates to false and the ViewComponent is not displayed. The same holds for the “Years” and “Venues” ViewComponents (their ConditionalExpressions are not entirely shown in Figure 5.24 for space reasons, but they retrieve the documents that match the input keyword). When the user submits a keyword and triggers the “Search” event, the ConditionalExpressions of the “Results,” “Years,” and “Venues” ViewComponents are evaluated and the content of these ViewComponents is populated with the matching documents. The VisualizationAttributes of the “Years” and “Venues” ViewComponents comprise a single attribute, whose distinct values are displayed as facets1. Checking or unchecking the values of the facets triggers the corresponding events shown in Figure 5.24, which causes the binding of the “Years” and “Venues” parameters. As a consequence, the ConditionalExpression of the “Results” ViewComponent is evaluated using those parameters, which—if not empty—can lead to the restriction of the result set.
