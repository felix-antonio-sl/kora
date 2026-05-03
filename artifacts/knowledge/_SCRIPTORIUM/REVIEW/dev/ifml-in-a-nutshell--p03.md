---
_manifest:
  urn: urn:dev:kb:ifml-in-a-nutshell-p03
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
    shard_index: 3
    shard_count: 4
    shard_root_urn: urn:dev:kb:ifml-in-a-nutshell
---

# IFML in a Nutshell - Parte 03

## Running Example

As already mentioned in chapter 4, the e-mail application interface consists of a top-level ViewContainer, which is logically divided into two alternative subcontainers: one for managing mail messages (open by default when the application is accessed) and one for managing contacts.
The “Messages” ViewContainer, visible in Figure 5.25, displays the list of the available mailboxes, which is presented in conjunction with the messages contained in a mailbox or with the interface for composing a message or for editing the mail settings. Selecting a mailbox causes the messages it contains to appear in the central part of the interface (the MailBox sub-ViewContainer). Entering the application causes the selection of a default mailbox in accordance with PATTERN CN-DEF: default selection.
Figure 5.26 shows the ViewComponents, Event, and NavigationFlow that model the selection and display of a mailbox.
Access to the messages can also occur through a search functionality displayed together with the mailbox list. An input field supports simple keyword based search. With a click, the user can access an alternative full-search input form that allows the entry of various criteria, as shown in Figure 5.27.
Figure 5.28 shows the model of the two alternate search functions. A modeless ViewContainer is used to denote that the full search form opens in a modeless window, as shown in Figure 5.27. The forms “Message Keyword search” and “Full Search” contain the fields shown in Figure 5.14 and Figure 5.23, respectively. The “Message List” ViewComponent has three ConditionalExpressions. Each expression is reached by a navigation flow, one for each of the ways in which it can be accessed. At every user interaction, only the expression that is the target of the current user navigation will be evaluated. The condition expressions are visible in Figure 5.14, Figure 5.23, and Figure 5.26.
For brevity, Figure 5.28 omits representation of the ParameterBindingGroup elements associated with the events “Select Mailbox,” “Search mail,” and “Search mail full.”
Figure 5.28 also shows a refinement of the “MailBox” ViewContainer, which unveils its internal organization into the sub-ViewContainers necessary to alternate between the visualization of a message list and that of a single message. The “MessageList” ViewComponent supports interaction with mail messages individually or in sets. On the entire set of messages, the “MarkAllAsRead” event permits the user to update all the messages in the current MailBox, setting their status to “read” (see Figure 5.29).
As shown in Figure 5.30, the “MessageList” ViewComponent also supports a second kind of interaction, the selection of a subset of messages. When at least one message is selected, a ViewContainer is displayed (“MessageToolbar”), which permits the user to perform several actions on the selected message(s), including archiving, deleting, moving to a MailBox/Tag, and reporting as spam.
When one or more messages are selected in the “MessageList” ViewComponent, the “MessageToolbar” view container appears, which allows the user to perform several actions on the selected messages. If all messages are deselected, such a view container disappears
In summary, the “MessageList” ViewComponent supports three types of interactive events:

1. An event for selecting the entire set of messages and triggering an action upon them, marking all messages as read (Figure 5.29);
2. Two events for checking/unchecking messages (Figure 5.30);
3. An event for selecting an individual message and opening it for reading.

The Events of the “MessageList” ViewComponent are modeled in Figure 5.31 and Figure 5.33.
The “SelectMultiple” checking event marks one or more messages in the current mailbox and produces the display of the “MessageToolbar” ViewContainer, which remains active while at least one message is selected. The “Deselect” unchecking event allows the user to deselect messages, which updates the value of the “MessageSet” parameter. Notice that the checking and unchecking events are triggered every time one element is checked or unchecked in the list. The “SelectMultiple” event has a ParameterBinding, which associates the (possibly empty) set of currently selected messages with an input parameter of the “MessageToolbar” ViewContainer. The “MessageToolbar” ViewContainer is also associated with an ActivationExpression, which verifies that at least one message is selected. The “SelectOne” SelectEvent enables the selection of a single message from the mailbox and causes the details of the message to be displayed, as shown in the mock-up of Figure 5.32.
This functionality is modeled in Figure 5.33 with a SelectEvent associated with the “MessageList” ViewComponent, which causes the setting of the “MessageSet” parameter and the display of the “MessageReader” ViewComponent. Such a component permits the user to access one specific message at a time. Its visualization replaces the “MessageList” ViewContainer, as denote by the XOR nesting of the children ViewContainers “MessageList” and “MessageDetails” within “MessageViewer,” shown in Figure 5.31 and Figure 5.33.
We conclude this elaborate example with a model of the functionality for composing messages. The interface for composing a message can be accessed in two ways: by clicking on the “Compose” link anywhere in the message management interface (to write a new message) and by selecting one of the various commands available in the message reader interface (for replying to or forwarding an existing message). Consequently, the model should support both the content-independent and the content-dependent navigation to the message composer. Figure 5.34 shows the mock-ups of the two ways for accessing the message composer functionality; notice that the content of the message editing fields and the navigation events available differ in the two cases.
Figure 5.31 and Figure 5.33 show the model of content-independent navigation that permits the user to access the message writing functionality. The “MessageWriter” ViewContainer is marked as landmark, and therefore it is accessible from all the other ViewContainers of the “MessageManagement” ViewContainer. It contains the “MessageComposer” ViewComponent, modeled as a form with different fields corresponding to the main attributes and relationships of the domain model class “Message”: To, Cc, Bcc, Subject, Body, and Attachment. When the “MessageWriter” ViewComponent is accessed in the content-independent navigation case, the form fields are not preloaded and the user can fill them freely, as shown in the left part of Figure 5.34.
Conversely, Figure 5.35 shows the model expressing the access to the message composer functionality as a consequence of content-dependent navigation. The “MessageReader” ViewComponent is associated with three events (“Reply,” “ReplyToAll,” and “Forward”) that allow the user to navigate to the “MessageWriter” ViewContainer and access the “MessageComposer” Form. The “ReplyToAll” event is active only when the message displayed in the “MessageReader” ViewComponent has more than one recipients, as expressed by the activation expression associated with the “ReplyToAll” event.
The “Reply,” “ReplyToAll,” and “Forward” events are associated with a ParameterBindingGroup, which conveys the properties of the original message displayed in the “MessageReader” ViewComponent. These properties are used to preload the fields of the “MessageComposer” Form as shown in the mock-up in Figure 5.34 (right). Each form field is associated with a parameter of the same name, which takes a value from the proper attribute of the original message as expressed by the ParameterBindingGroup:
- The “Reply” and “ReplyAll” events associate the subject of the original message with the subject of the new message (prefixed with the string “Re: “), the recipient of the original message with the sender of the new message, the body and the cc recipients of the original message to the body and cc recipients of the new message.

- The “Forward” event associates the subject of the original message with the subject of the new message (prefixed with the string “Fw: ”) and the body of the original message with the body the new message.

The “MessageComposer” Form supports two SubmitEvents (“Send” and “Save”) for sending and for saving without sending the message, respectively.

The “MessageComposer” Form, whose mock-up appears in Figure 5.34, also supports a kind of stateful interaction. Besides the events “AddCc,” “AddBcc,” “AddAttachment”—which are available irrespective of the kind of response the user is editing—the events “Reply,” “ReplyToAll,” and “Forward,” allow switching the response type. However, only two out the three events are active at a time depending on the current state of the editing. For example, when the user is editing a “ReplyToAll” message, only the “Reply,” and “Forward” events are active. This is conveyed by the “State” parameter of the Form and by the three ActivationExpressions associated with the events, as shown in Figure 5.36. The ActivationExpressions check for the value of the parameter “State,” which is set appropriately by each of the “Reply,” “ReplyToAll,” and “Forward” events, so that only the events appropriate to the current editing context are active.
Another example of a conditional event is the “EditSubject” Event. The event for editing the subject field is disabled when the value of the “State” parameter is “Forward.”

## Modeling business actions

Taking the Model–View–Controller pattern as a high-level conceptual description of the way in which an interactive application works, the view allows the user to trigger events, which are handled by the controller. The controller dispatches each event to the proper element in the model, which performs the business action implied by the event. This can result in the update of the application status. At the end of the cycle, the view is updated to display the current status to the user for the next round of interaction. This typical roundtrip is shown in Figure 6.1.
The model could be logically regarded as responsible for two distinct aspects: exposing the business actions that embody the service requested by the user and maintaining the status of the application, which displays in the view.

In chapter 3, we discussed how to construct a domain model that specifies the objects of the application model. In chapter 4, we described how to define the general structure of the application interface. Chapter 5 illustrated how to express the publication of the domain objects in the interface.
The focus of this chapter is on the business logic of the application, be it embedded in methods of the application domain objects, described by suitable UML behavioral diagrams, or delegated to external objects and services.

The goal of IFML is not modeling the internal functioning of the application business logic. Rather the objective is to express the interplay between the interface and the business logic. This is done by:

- Showing that an event triggers a business action, which may imply also the specification of some input–output dependency between the interface and the business logic; and

- Showing that the interface can receive and respond to events generated by “the system,” be it a business component of the application or an external service. In this case, IFML also permits the designer to describe the input–output dependency between the information carried by a system event and the affected elements of the interface.

IFML does not replace the behavior specification languages that are normally employed to describe the algorithmic aspects of the business logic. IFML business actions are black boxes that show the minimal amount of information needed to specify the abovementioned aspects. The designer is free to focus on such black boxes and describe their internal functioning using the behavioral language of choice. To support this kind of refinement, an action in IFML can reference a behavior in an external model.

## Actions

Actions

An Action represents a reference to some business logic triggered by an Event.

Actions may reside on the server or on the client side. The elementary design pattern for triggering actions is represented in Figure 6.2.
The model contains a source ViewContainer and ViewComponent, with an Event connected via an InteractionFlow to an Action (shown as a named hexagon). The Action is itself connected to a target ViewComponent through an outgoing flow by an event typically representing the completion of the Action. ParameterBinding elements are used to denote the input–output dependency between the source ViewComponent and the Action, and between the Action and the target ViewComponent.

For example, the source ViewComponent could be a form for entering a flight request. The Action could be a flight brokering business component that takes as input the form data, checks availability and price at different flight operators, and produces the best offers as output. The target ViewComponent could be a List showing the retrieved options to the user.

The pattern of Figure 6.2 assumes that the action always terminates with the same event, after which the same target ViewContainer is displayed. However, in many situations, invoking a piece of business logic may result in various alternative outcomes lead to different termination events. Therefore, Actions may trigger different Events, called ActionEvents, as the result of the normal termination of computation or to signal the occurrence of exceptions.

ActionEvents

An ActionEvent is an Event that may be produced by an Action to signal normal or exceptional termination.

Figure 6.3 shows the typical usage of multiple ActionEvents. The Action can terminate in normal or exceptional conditions, and the ActionEvents and associated InteractionFlows express the course of action taken in the two cases. For example, the source ViewComponent could be a form for signing up an application to an external service, and the Action could be a validation business component, taking as input the form data, validating it, and producing a limited-time service token. In case of normal termination, the target ViewComponent could be a Details component showing the newly generated token and the service terms and conditions to the user. Exceptional termination may also occur (e.g., when the user’s request does not meet the conditions for obtaining an access token). In this case, the target ViewComponent could be a Details component showing the reasons of failure to the user.
The source and the target ViewComponent of an action invocation need not be distinct. For example, Figure 6.4 shows a model of an interface for deleting objects from a list. The source ViewComponent allows the user to select an object for deletion. After the deletion, the same ViewComponent is presented again with its content updated.
Figure 6.4 also shows two shortcuts for simplifying the ActionEvent notation. When no outgoing InteractionFlow and no ActionEvent are associated with the Action, it is assumed that the target is the smallest ViewContainer comprising the source ViewElement from which the Action has been activated.

## Notification

The influence of business logic on the interface manifests not only when the user takes the initiative but also as a consequence of a system-initiated action. This situation requires modeling the notification of an occurrence from the application back end of an external system to the user interface. In this case, the IFML model does not represent the initiation and execution of the action but only its ultimate effect, which is captured by a SystemEvent.

**SystemEvent and SystemFlow**

A SystemEvent is an Event produced by the system that triggers a computation reflected in the user interface. Examples of SystemEvents are time events (which are triggered after an elapsed frame of time), system alerts (such as a database connection loss), or message receipt notifications.

A SystemFlow is an InteractionFlow that connects a SystemEvent to a ViewElement to identify the element affected by the occurrence of the SystemEvent.

The cause of a SystemEvent may be left unspecified in the model, although it is also possible to express a condition whose occurrence triggers the SystemEvent. Such a condition is represented by means of a TriggeringExpression.

**TriggeringExpression**

A TriggeringExpression is an expression that determines when or under what conditions a SystemEvent should be triggered.

The notification PATTERN A-notif, introduced later in this chapter, contains an example of a SystemEvent, a SystemFlow, and a TriggeringExpression.

## Business Action Patterns

Several design patterns embody the solution to recurrent problems in the design of the interplay between the user interface and the business logic. We call such platform-independent patterns action patterns and prefix their name with an “A.”

### Content Management Patterns

The most important action patterns relate to the management of the objects of the domain model. Such content management patterns all have a similar structure. They exploit an Action endowed with the input parameters necessary to create, delete, or modify objects and association instances, and with output parameters that characterize the effect of the performed content update. The role of the interface is that of supplying the input and of visualizing the output to the user as a confirmation that the action has been executed and the application state updated.

### PATTERN A-OCR: Object Creation

The object creation pattern enables the creation of a new object. The pattern relies on an Action characterized by:

- a reference to the dynamic behavior that the action must perform; and

- a set of input parameters, used to initialize the attributes of the object to be created.

The input of the Action is typically supplied by a ParameterBindingGroup associated with a NavigationFlow exiting from a Form ViewComponent. The parameter values are used to construct the new object. If some attributes have no associated input value, they are set to null. The only exception is the object identifier (OID), which is normally treated in an ad hoc way: if no value is supplied, a new unique value is generated by the Action. The behavior of the object creation Action typically consists of invoking a class constructor or a factory method in a creator class. The output produced by the Action is the newly created object, comprising its OID and all its attribute values. The output of the Action is defined only when the operation succeeds and thus can be associated as a ParameterBindingGroup only with the InteractionFlow that denotes normal termination. If no ParameterBindingGroup is specified explicitly, a default output ParameterBinding consisting of the OID of the newly created object is assumed as implicitly associated to the normal termination event.

The example of Figure 6.5 shows the typical object creation pattern, which consist of the combination of an entry Form (“EnterProductData”) providing input to an Action (“CreateProduct”) that creates a new Product by invoking the DynamicBehaviour implemented by a factory method of a creator class. The Form has several fields (e.g., “Code,” “Name,” and “Price”) for entering the respective attribute values. The field values inserted by the user are associated as explicit parameters with the NavigationFlow from the Form to the Action. In the rendition, also shown in Figure 6.5, the SubmitEvent associated with the form is displayed as a submit button, which permits the activation of the Action. The “CreateProduct” Action has two ActionEvents. Normal termination is associated with an InteractionFlow that points to the “NewProductDetails” ViewComponent and with the default output parameter (the OID of the new object). The exceptional termination event is associated with an InteractionFlow that points to a ViewContainer for displaying an error message.

### PATTERN A-OACR: Object and Association Creation

A variant of the object creation pattern can be used to create a new object and set its associations to other objects. Figure 6.6 shows an example of such an object creation and connection pattern.
The “EnterProductData” Form contains an additional SelectionField, corresponding to the association that must be set, namely the association between Product and Category. The Category SelectionField can be preloaded with all the categories as discussed in chapter 5. The NavigationFlow triggered by the SubmitEvent “CreateNewProduct” has one additional ParameterBinding for the identifier of the selected category, which is passed as input to the Action. The Action itself can be specified either by referencing a constructor that sets the proper category for the product or by referencing a behavioral diagram (e.g., a UML sequence or activity diagram) that describes all the steps to be performed for creating the object and connecting it to a category.

### PATTERN A-ODL: Object Deletion

The object deletion pattern is used to eliminate one or more objects of a given class. The pattern requires an Action characterized by:

- a reference to the dynamic behavior that the action must perform, which is typically the invocation of a delete operation of the database; and

- the input parameters necessary to identify the object to delete.

The input to the action is conveyed by a set of ParameterBinding elements. Normally these values are one or more primary keys, although nonkey attribute values can be used as input, and the Action encapsulates the business logic for exploiting such information to retrieve the objects to delete.

At runtime, the user typically chooses either a single object displayed by a Details ViewComponent or selected from a List ViewComponent, or a set of objects chosen from a MultiChoice List ViewComponent. The identifiers of the chosen objects are associated by a ParameterBindingGroup to the NavigationFlow exiting the ViewComponent and pointing to the Action that actually deletes the objects.

Normal termination occurs when all the objects have been deleted. In this case, the Action has no output parameters. Exceptional termination occurs when at least one of the objects has not been deleted. In this case, the Action has an output parameter holding the OIDs of the objects that were not deleted. This can be useful to display the list of items that could not be deleted, together with an error message.

The example of Figure 6.7 illustrates the object deletion pattern applied to a single object. The ViewContainer includes the “ProductsList” ViewComponent connected to the “DeleteProduct” Action. The NavigationFlow has a default parameter holding the OID of the selected product, which is used in the Action. The SelectEvent fires the deletion of the chosen object. If the operation succeeds, the “Products” ViewContainer is redisplayed, but the deleted product no longer appears. In case of failure, a different ViewContainer with an error message is displayed, which may use the information about the object whose deletion failed and any other useful parameter returned by the action (e.g., a human-readable explanation of the failure).
The example of Figure 6.8 shows a variant of the object deletion patterns in which a multichoice list ViewComponent is used to let the user check a set of products and invoke the deletion Action on them. In this case, the default ParameterBinding associated with the “Delete” event of the “ProductList” ViewComponent holds the set of OIDs of the selected objects. These are displayed in the “SelectedProducts” List ViewComponent, which is associated with the “Confirm” event.
The NavigationFlow of the Delete set selection event has as default ParameterBinding that includes the entire set of objects output by the source List ViewComponent (“SelectedProducts” in this case) and triggers the “DelectedProduct” action on all the objects bound to the event.

### PATTERN A-CODL: Cascaded Deletion

The cascaded deletion pattern allows one to remove a specific object and all the objects associated with it via one or more associations. In this case, the action is implemented by a sequence formed by two or more delete operations, one for removing the main object and the others for removing the related objects (at least one). In particular, cascaded deletion is used to propagate the deletion of an object to other dependent objects, which are connected to it by an association with minimum cardinality of 1, and thus could not exist without the object to which they refer. An example of such a situation is illustrated in Figure 6.9, which shows the use of the pattern for deleting an e-mail message and all its attachment. The “MessageDetails” ViewContainer includes a Details ViewComponent (“Message”) showing the message, and a List ViewComponent (“Attachments”) displaying its attachments. The “Message” ViewComponent is associated with an event that triggers the “CascadeDelete” Action, which conceptually consists of a sequence of two operations, deleting both the attachment and the e-mail message. The internal structure of the Action is not specified in IFML and can be described by means of a behavioral diagram. For example, Figure 6.10 specifies the cascade deletion using a UML sequence diagram. An alternative Action design could exploit the native referential integrity mechanism of the underlying data store (for example, the ON DELETE CASCADE clause of SQL foreign key constraints) and delete only the message object, leaving to the database the task of cascading the deletion.
The pattern of Figure 6.9 is a good illustration of the intertwining between the business logic and the interface design. The NavigationFlow denoting the normal termination of the “CascadeDelete” Action does not lead back to the source ViewContainer but instead to the “MessageList” ViewContainer, which is the default subcontainer of the enclosing “MessageDetails” ViewContainer. This is because the object that was displayed in the “MessageDetails” ViewComponent (the deleted message) no longer exists, and it would make no sense to redisplay it. The IFML model is the right place to express this kind of relationship between the semantics of actions and their effect in the interface.
The resulting interaction is shown in the mock-up of Figure 6.11.

### PATTERN A-OM: Object Modification

The object modification pattern is used to update one or more objects of a given class. An object modification pattern uses an Action that is characterized by:

- the reference to the dynamic behavior that the action must perform, which is typically the invocation of a setter method; and

- the input parameters necessary to identify the object(s) to modify and to supply new values to their attributes.

When the user chooses multiple objects at runtime, the same update applies to all the selected objects. The Action must be properly linked to ViewComponents of the interface, to obtain the needed inputs.
- The new attribute values: these are typically defined as a ParameterBindingGroup associated with a NavigationFlow coming from a Form ViewComponent.

- The objects to modify: these are usually specified as a ParameterBindingGroup holding one OID or a set of OIDs.

- As an alternative to the usage of object identifiers as parameters, the objects to modify can be retrieved by the Action based on logical criteria, exploiting the values associated as parameters with InteractionFlows incoming to the Action. In this case, the Action encapsulates the object retrieval business logic.

The normal termination of the Action occurs when all the objects have been successfully modified. In this, case the ActionEvent is associated with a default parameter holding the set of OIDs of the modified objects. An exceptional termination occurs when at least one of the objects could not be modified. In that case, the ActionEvent is associated with a default parameter holding set of OIDs of the objects that were not modified.

The example of Figure 6.12 shows a Form ViewComponent used to supply values to an object modification Action. The “ProductEditor” ViewContainer comprises a Details ViewComponent (“Product”), which shows the name of the product to modify, and a Form (“EnterProductData”), whereby the user can modify the existing product attribute values. A DataFlow from the Details ViewComponent to the Action has a default parameter holding the OID of the product to modify, which is used by the Action to identify the instance to update. The Action is activated by a SubmitEvent associated with the Form. The NavigationFlow has a ParameterBindingGroup element, which associates the value of the fields of the Form with corresponding input parameters of the Action. The normal termination leads to the “UpdatedProduct” ViewContainer, which shows the modified values of the product attributes. The exceptional termination points “back” to the “ProductEditor” ViewContainer, which redisplays the old values.
Note that for classes with many attributes, the specification of the pattern can be cumbersome due to the need to repeat the relevant attributes twice: once as form fields and once in the parameter binding. However, a tool such as the one described in chapter 11 can easily provide a wizard for building the pattern with less effort (e.g., by inserting all the class attributes in the model automatically).
The example of Figure 6.13 illustrates the modification of a set of objects. The “MessageList” multichoice List is associated with a SelectEvent (“MarkAsRead”) for updating the status of the chosen messages, marking them as “read.” The outgoing NavigationFlow of the event is associated with a ParameterBindingGroup that holds the OIDs of the objects selected in the multichoice list and a constant value (“read”) for updating the status of the messages. The operation succeeds if the modification can be applied to all the objects chosen from the list, in which case the normal termination ActionEvent is raised. After this event, the “Messages” ViewContainer is redisplayed, with a notification of the number of marked messages.
The Action fails if the modification cannot be applied to some of the selected messages, which causes the exceptional termination ActionEvent to be raised and an modeless alert window to be displayed.

### PATTERN A-AM: Association Management

An association management pattern is about maintaining the instances of associations specified in the domain model. Specifically, it is used to create/replace/delete instances of an association by connecting and/or disconnecting some objects of the source and target classes. The association management pattern exploits an Action characterized by:

- the reference to the dynamic behavior that the action must perform, which is typically the invocation of a setter method acting on the attribute that implements the association in one or in both classes; and

- input parameters for locating the objects of the source class and of the target class.

The Action is triggered by a NavigationFlow and receives as input pairs of objects of the source and target classes, identified by the ParameterBindingGroup of the NavigationFlow. It provides as output the pairs of OIDs corresponding to the objects of the source and of the target class for which an association instance has been created/replaced/deleted. These values can be used to define a ParameterBindingGroup associated with the normal and exceptional termination ActionEvents. The latter is raised when the management of at least one association instance fails, whereas the normal termination ActionEvent signals that all the association instances have been managed properly.
Figure 6.14 shows an example of the association management pattern for updating the category of a product, which corresponds to a one-to-many association in the domain model. The “Product” Details ViewComponent in the “ProductCategories” ViewContainer displays a current product, as the result of a previous selection in another ViewContainer (not shown in Figure 6.14). The ViewContainer also includes the “CurrentCategory” Details ViewComponent, which displays the category of the displayed product. The primary key of the displayed product—necessary for determining the actual category in the “CurrentCategory” ViewComponent—is supplied by a ParameterBindingGroup associated with the DataFlow from the “Product” to the “CurrentCategory” ViewComponent.
Finally, the “ProductCategories” ViewContainer comprises a List ViewComponent (“Categories”) showing all the categories from which the user can select the desired one and trigger the “Assign” SubmitEvent. This event triggers the Action for updating the relationship instance between the displayed product, whose primary key is supplied by a DataFlow with a ParameterBindingGroup, and the new category selected from the list. The normal termination event of the Action causes the “ProductCategories” ViewContainer to be redisplayed, showing the updated category of the product. In case of abnormal termination, an Alert window is presented before letting the user go back to the original ViewContainer.

### PATTERN A-notif: Notification

This pattern models the case in which the interface is (typically asynchronously) updated by the occurrence of a system generated event. Figure 6.15 shows an example of the notification pattern.
In the e-mail application, actions on messages (such as sending, deleting, and moving to a different folder) are triggered by an Event and executed by an Action at the server side. When the action terminates, the system produces a completion event and sends an asynchronous notification to the interface. The effect of catching a notification event is represented by a SystemEvent, which triggers the display of a “MessageNotification” ViewComponent, as shown in Figure 6.15.
The production of a SystemEvent can be left undetermined, in which case it is assumed that the system sends the event in a completely unspecified manner, or be associated with an Action of the interface model to convey that the notification is connected with the termination of an Action. For example, all the notification events of the e-mail application can be associated with the termination of the respective Action, as shown in Figure 6.16.

## Running Example

The e-mail application allows the users to perform a variety of operations on messages, including composing a new message, replying to a received message, and moving a message to a new or to an existing folder. When one or more messages are selected, they can be moved to another folder by means of the “MoveTo” command.

Figure 6.17 shows the mock-up of interface supporting a command. A ViewContainer is displayed in a new window with the list of available MailBox and Tags. The user can select from such a list the destination Folder to which he wants to move the messages. This functionality can be modeled with an instance of PATTERN A-AM: Association management, shown in Figure 6.18: the “MessageToolbar” ViewContainer is associated with the “MoveTo” Event, which causes the display of the “Chooser” modeless window. This ViewContainer comprises a list for selecting the target folder. The selection event triggers the “MoveTo” Action that performs the command and sends a notification event upon termination, which is captured by the “MessageNotification” ViewComponent in the top-level container (as already illustrated in Figure 6.15).
Note that in this example of association management pattern, the messages to move are associated as a ParameterBinding to a DataFlow that connects the “MessageToolbar” ViewContainer to the Action, whereas the OID of the destination folder is associated by default with the NavigationFlow of the “Select” Event and thus omitted from the diagram.
As visible in the mock-up of Figure 6.17, the window for choosing the target folder also contains a command for creating a new folder that opens a modal window for entering the name and parent folder of the new folder. Figure 6.19 shows the mock-up of this functionality.
The model including the functionality for moving a message to a newly created folder is shown in Figure 6.20. The “CreateNew” event associated with the “Chooser” ViewContainer opens a modal ViewContainer with the form for entering the name of the new folder (using a SimpleField) and selecting the parent folders (using a SelectionField). The “Create” Event in the modal window triggers an Action for creating the new folder and associating it to the specified parent folder and to the messages selected previously. Upon normal termination, the Action emits a notification message.
Besides the commands for moving messages, the toolbar provides functionality for archiving, reporting, and deleting message. Figure 6.21 completes the partial model viewed so far with the remaining Actions.
An additional note concerning the allocation of the business logic to the architectural tiers of the application is needed. So far, the illustration has been purposely neutral as to where an Action is executed within the architecture of the application, because the platform-independent model should not incorporate unnecessary architectural assumptions. However, this does not mean that all actions are executed on the same tier or that only server-side business logic can be modeled. To illustrate this aspect, we conclude the running example with an expansion of the model of the message composition functionality, already described in chapter 5.
The model of the “MessageWriter” ViewComponent can be refined by zooming in inside the “Body” field, which supports client-side business logic (such as rich formatting of the text) and mixed server- and client-side functionality (such as spellchecking). Figure 6.22 shows a mock-up of this functionality.
The embedding of a full-fledged microapplication such as a rich text editor inside a Form ViewComponent can be modeled by replacing the SimpleField with a more complex ViewComponentPart called RichTextEditor, as shown in Figure 6.23. Such ViewComponentPart could support events and further nested ViewComponentParts as required to express its interface. The execution tier of an Action could also be expressed as a stereotype. For example, Figure 6.23 tags the Actions executed at client side with an appropriate stereotype.

## IFML extensions

The IFML standard comes organized as a core set of concepts and a number of extensions that embody general characteristics found in many interactive applications. The extension mechanism applies to all the main concepts of IFML. The extensions included in the standard are:
- ViewContainer extensions: Window
- ViewComponent and ViewComponent Part extensions: Details, Field, Form, List, SelectionField, SimpleField, Slot
- Event extensions: SelectEvent, SubmitEvent, SystemEvent
- ContextDimension extensions: Device, Position, UserRole
- Expression extensions: ValidationRule
Further custom extensions are allowed for the main concepts of IFML: ViewContainers, ViewComponents, ViewComponentParts, Events, and domain and behavior concepts (and their extensions).
The purposes of extensions are manifold:
- Adding expressive power to the modeling language;
- Making the concepts and notation less abstract and closer to the intuition of designers;
- Allowing different specialized concepts to be distinguishable visually, for improved readability of diagrams; and
- Assigning more precise meaning to concepts to enable deeper model checking, formalization of semantics, and executability (through code generation or model interpretation).
Figure 7.1 shows the use of IFML extensions (equipped with customized icons) for making the visual notation more intuitive, enabling model checking, and supporting code generation. This example will be expanded in chapter 11.
The advantages of extensibility persist and even increase when one considers IFML under the perspective of a specific category of applications that exhibit their own interface styles, technological constraints, and sometimes even peculiar terminology or jargon.
This chapter introduces several specializations of IFML that exploit extensibility to capture features found in different classes of applications, including, desktop, web, and mobile applications. The assignment of an extension to a class of application is somewhat arbitrary. The convergence of the implementation languages and platforms makes it impossible to distinguish the features of desktop, web, and mobile application sharply. For a better organization of the chapter, though, we have placed each extension under the category in which it originated or is most often or exclusively used.

## Desktop Extensions

Under the umbrella term of desktop applications we mean applications that allow the most precise control over the user interface, developed with a variety of different technologies, ranging from window-based applications developed in such technologies as Java Swing or Windows Forms to rich Internet applications implemented with JavaScript and HTML 5. Although this equivalence is imprecise from the programming point of view, it is sufficient to identify cross-platform features that are general enough to provide good candidates for IFML extensions.

### Event Extensions

Probably, the most relevant capability of desktop applications is the very detailed management of the events that the user can generate in the interface. Therefore, an important area of extensibility of IFML regards the event types supported by desktop interfaces. These events are so numerous as to make it unfeasible to review all of them and the properties to be modeled for creating an IFML extension. Rather, we will discuss what makes an event type worth an extension and the features that should be modeled as additions to the basic notion of Event. When considering a new event type as a candidate for extension, the following questions should be addressed:
- What ViewElements can the event be associated with? ViewContainers, ViewComponents, ViewComponentParts, a specific extension of such elements, or a mix thereof?
- In there any restriction on the type of ViewElements that can be the target of the InteractionFlow associated with the event?
- What parameters can be associated with the InteractionFlow connected with the event?
Figure 7.2 shows an example of event specialization.

**OnFocusLost**

The OnFocusLost event is an extension of ViewElementEvent that captures the loss of focus of a SimpleField in a Form. The event is triggered when the user moves away from the field (e.g., by using the tab key or by clicking on another field). It can be associated with a SimpleField or with an entire Form. Its outgoing InteractionFlow can have any ViewElement as a target and a ParameterBindingGroup comprising as input parameter the value of the SimpleField or the values of all the SimpleFields of the Form.
Figure 7.2 demonstrates the usage of the OnFocusLost event to invoke Actions. In one case the event is associated with the “Username” field for checking the availability of the username provided by the user. Other OnFocusLost events are associated with other fields for auto-saving the value input by the user when the focus leaves the field.

##### Drag and Drop

The OnFocusLost event and other similar event extensions detect an atomic self-contained user interaction. Desktop applications also support more elaborate behaviors that span a sequence of interactions, such as drag and drop. A drag and drop behavior consists of the correlation of two event types: OnDragStart and OnDrop.

###### OnDragStart and OnDrop

The OnDragStart event is an extension of ViewElementEvent that captures the beginning of a drag interaction. It can be associated with Details or List ViewComponents (and specializations thereof). It has no outgoing InteractionFlow element. It has a mandatory property “OnDropEvent” that denotes an event of type OnDrop, which is the target of the OnDragStart event.
The OnDrop event is an extension of ViewElementEvent that captures the termination of a drop interaction. It can be associated with a Details or List ViewComponent (and specializations thereof). It must appear as the value of the OnDropEvent property of an event of type OnDragStart, which is the source of the OnDrop event. It has one outgoing InteractionFlow element. Such InteractionFlow can have any ViewElement as a target and a DataBindingGroup comprising two input parameters: (1) the value of one or more class instances of the ViewComponent associated with the source OnDragStart event and (2) the value of one or more class instances of the ViewComponent associated with the OnDrop target event.
As shown in Figure 7.3, the drag and drop behavior is modeled with a pair of events: one (OnDragStart) binds to the object(s) that are dragged, and the other (OnDrop) binds to the object(s) on which the dragged item(s) are dropped. These two (sets of) instances can be used as parameter values associated with the InteractionFlow exiting the OnDrop event. In the case of Figure 7.3, one or more messages are dragged from the message list of the currently open mail box and dropped on another mail box. The drop termination event triggers the “MoveTo” Action, which moves the dragged messages to the drop mail box.

### Component Extensions

Container and component extensions add features to the basic IFML ViewElements.

##### Tree explorer

A “classic” component of desktop interfaces is the Tree component, used to display hierarchical data. Essentially, a tree is a special kind of list that displays not only objects but also their containment associations. Therefore, the data model of a tree component consists of a class, which represents the common type of the objects displayed in the tree, and a recursive association, which represents the hierarchy. In the simplest case, interaction with the tree is done by selecting one node at a time.

**Tree ViewComponent**

A Tree is an extension of the List ViewComponent that displays hierarchical data. It owns a DataBinding element that refers to a class of the domain model and a RecursiveNestedDataBinding element that refers to a one-to-many association defined on the instances of the class.
Figure 7.4 shows an example of the Tree component for publishing a selectable list of nested mailboxes. A Selection event allows the user to select one element in the tree and thus display its details.

##### Table

Another popular component of desktop applications is the table editor, also called a record set editor or data grid. The component displays a table of data and allows the user to add and delete rows and edit cell content. The data model of the component is any piece of tabular data. For simplicity we illustrate the case in which instances of a class are used as data, but alternative data bindings can be defined, as already possible with the standard concept of DataBinding. The only constraint is that the rows of the table should correspond to identifiable objects, if one wants to trap events like row deletion and therefore update the underlying data accordingly.
The Table component can be associated with such events as the update of a cell or the insertion and deletion of a row.

**Table ViewComponent**

A Table is an extension of ViewComponent that displays tabular data and allows the user to edit them. It has a DataBinding element that typically refers to a class of the domain model. The attributes of the class are mapped to the columns of the table using the ColumnAttribute ViewComponentPart. The Table component can be associated with events of type CellUpdate, RowInsertion, and RowDeletion.
Figure 7.5 shows an example of usage of the Table component for editing a record set of products. At each cell update, a data update Action “SaveProduct” is invoked with a parameter binding that holds the modified field value. The deletion of a row triggers the deletion of the corresponding class instance, identified by a parameter binding corresponding to the object displayed in the affected table row. The creation of a row invokes the creation of a new object based on the values entered in the Table row by the user. After the execution of the Actions, the Table is redisplayed with the updated content. (Recall that an InteractionFlow pointing to the source element of the action is assumed by default and thus can be omitted from the diagram).
The basic example discussed in this section can be extended, for example, with event types supporting the explicit synchronization of the table content with the data in the data store, such as “Refresh” and “SaveAll,” and with more compact parameters (e.g., representing the content of an entire row or of all the rows of the table).

### Componentpart Extensions

Extensions can also be defined at a finer granularity, such as at the ViewComponentPart level. An example could be an editable selection field that mixes the functionality of SimpleField and SelectionField by allowing the user to edit the value of the input field or choose it from a list of options.

**EditableSelectionField**

An EditableSelectionField extends the Field element and denotes an input field that is both editable and selectable.
Figure 7.6 shows an example of usage of the EditableSelectionField extension. The “ProductCreator” form contains the “Category” EditableSelectionField that allows the user to pick the category from a list of existing categories or invent a new one. The internal business logic of the “CreateProductAndCategory” Action must distinguish whether the category is new and, if so, create the category in addition to the product. Such a behavior can be described in a separate UML diagram associated with the Action.
