---
_manifest:
  urn: urn:dev:kb:ifml-in-a-nutshell-p04
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
    shard_index: 4
    shard_count: 4
    shard_root_urn: urn:dev:kb:ifml-in-a-nutshell
---

# IFML in a Nutshell - Parte 04

## Web Extensions

Web applications have brought several new concepts and an almost completely new terminology to user interface development. These are based on the fusion of previously segregated areas such as hypertext, multimedia, and form-based GUIs. The fundamental concepts of a web application are pages and links, which are borrowed from hypertext documents. Both can be viewed as specializations of core IFML concepts.

### Container Extensions: Pages, Areas, and Site Views

In this section, we introduce IFML extensions that make the specification of the web interface composition patterns introduced in chapter 4 adhere more closely to the terminology and characteristics of web applications. The basic unit of dialogue with the user in a web application is a page, a ViewContainer produced statically by a human editor or generated automatically at the server side by a program (a page template or a server-side script). As user interfaces, pages embed navigation commands; as resources of a document system, they have a human readable address, called uniform resource locator (URL). Web applications offer service to multiple users over a multitier, client-server architecture; therefore they are concerned with the security of data transmission, achieved by delivering the interface over the HTTPS protocol, and with the control of access, achieved by enforcing user’s authentication, identification, and permission control.

**Page**

A page is an extension of ViewContainer that denotes an addressable web interface unit.
As already mentioned in chapter 4, pages in a large web application can be arranged hierarchically to facilitate user navigation.

**Area**

An Area is an extension of a disjunctive (XOR) ViewContainer that denotes a collection of pages or other areas, grouped according to an application-specific purpose.
Examples of areas in an e-commerce web application can be products, special deals, shipping rates and conditions, and returns and complaints.

As noted in chapter 4, web applications often offer different viewpoints on the same content to different classes of users. This characteristic can be captured by associating a ViewPoint with a specific type of ViewContainer called SiteView.

**SiteView**

A SiteView is an extension of a disjunctive (XOR) ViewContainer that denotes web application areas and pages grouped together according to an application-specific purpose, typically because they serve the needs of a UserRole.

In summary, a web application can be modeled as a collection of pages logically grouped into Areas and SiteViews. Pages are presented to the user one at a time. This is expressed by the disjunctive form of the enclosing ViewContainer. To express the requirements of a multiuser application, SiteViews, Areas, and Pages can be treated as resources of a role-based access control (RBAC) system. As such they can be associated with a ViewPoint, which in turn is associated with a Context, which is described, for instance, by a UserRole context dimension. The SiteView constitutes the typical item referenced by a ViewPoint. Appropriate activation rules can be defined for specifying that the SiteView is enabled for a given UserRole.
The definition of activation rules upon a SiteView/Area/Page denotes the access permission to that particular object for the specified UserRole. A SiteView/Area/Page not associated with any role is treated as public and can be accessed even when the UserRole is undetermined. In an e-commerce application, for example, different SiteViews could be associated with the UserRoles named “registered customer,” “product content manager,” and “sales manager.” A public SiteView could be addressed to nonregistered customers.
A SiteView/Area/Page has the following characteristics, which extend the standard properties of IFML ViewContainers to cope with specific web application features:
- URL label: A string denoting the (fixed part of) the SiteView/Area/Page address. If the page is implemented with a dynamic template, the URL label is typically concatenated with the parameters for the computation of its content. The URLs of a SiteView and of an Area are an alias for the home page of the SiteView and the default page of the Area.
- Security: If the property value is “secured,” all the pages of the Area or SiteView, or the individual Page, are served under the secure HTTPS protocol.
- Protection: If the property value is “protected,” all the pages of the Area or SiteView, or the individual Page, are subject to access control. The access control rule is expressed by the association of the SiteView/Area/Page with one or more UserRoles through an ActivationExpression.
Notice that the association of a UserRole with multiple levels of nesting components—such as Pages, Areas, and SiteViews—is purposely redundant and enables the incremental expression of access control rules. For example, access to a SiteView could be granted in general to the UserRoles Role1 and Role2. However, an Area or Page of the SiteView could be associated with a more restrictive ViewPoint that overrides the general one (e.g., to grant access only to Role1).
An important concept in a Web application is that of the home page, the page served to a user when accessing the application without requesting a specific resource.
Figure 7.7 reconsiders an example of web application interface organization already specified in chapter 4 using only the standard IFML concepts, and illustrates it with the concrete syntax of the described web extensions. Stereotypes are used to denote SiteViews and Pages and to identify the home page of a SiteView, as well as to determine whether the ViewContainer is Public or Protected. An ActivationExpression (e.g., Context.UserRole=”Editor”) is employed to specify that a SiteView is accessible only by a specific UserRole.

### Event and Interaction Flow Extensions

Interaction in web applications occurs in two ways: by submitting the content of a form and by clicking on hypertext anchors. The standard IFML extensions Forms and SubmitEvent already capture the essential characteristics of web forms. The IFML NavigationFlow faithfully mirrors the concept of hypertext link but may be extended to reflect the terminology and properties of web links.

**Link**

A WebNavigationFlow is an extension of a NavigationFlow that incorporates additional properties specific to hypertext links on the web.
A WebNavigationFlow can be endowed with properties specific to web navigation:
- Rel: specifies the relationship between the current document and the linked document; its values are codified by the HTML standard.
- Target: specifies where to open the linked document, typically in a browser window; the browser window can be the same one as the original document or a new window.
Figure 7.8 shows as example of usage of the WebNavigationFlow extension used to open the licensing information in a new browser window. It also informs search engines of the nature of the linked document via the WebNavigationFlow outgoing from the technical manual to the licensing information.
The WebNavigationFlow extension shows a typical issue in the design of extensions: the tradeoff between platform independence and utility. The Rel and Target properties are clearly dependent on the version of HTML, which is an implementation language. However, a code generator could exploit the additional platform-dependent information to inject the proper attribute values in possibly thousands of automatically generated HTML links, which is an extremely useful feature. An alternative approach would factor out implementation-dependent properties from the model extensions and weave them into the code generator. However, since the values of the properties can be set by each WebNavigationFlow, in this example we prefer utility over purity and make them definable directly in the model extensions.

### Component Extensions

The List component in the IFML standard offers a minimalistic functionality that can be extended to support more realistic interfaces.

##### Dynamically-sorted list

As illustrated in chapter 5, the OrderBy ViewComponentPart can be used to enable sorting of the items in a List ViewComponent. This compenent defines the sorting criteria (attribute plus sort direction).
Figure 7.9 shows an example taken from the running case.
The “MailBoxes” List ViewComponent has an OrderBy part that sorts instances by name, whereas the “MessageList” ViewComponent sorts its DataBinding instances by date.
The OrderBy ViewComponentPart is specified at design time and thus does not model a situation in which the user can change the sorting of data at runtime. This additional behavior, popular in both web and desktop applications, can be achieved by introducing an extension of the List ViewComponent called DynamicSortedList.

**DynamicSortedList**

The DynamicSortedList is an extension of the List ViewComponent that allows the user to sort data using visualization attributes. The DynamicSortedList has a one-to-many association, named “SortAttributes,” with the metaclass “VisualizationAttribute,” which denotes the subset of the visualization attributes usable for sorting.
Figure 7.10 shows a variant of the pattern of Figure 7.9, which uses a DynamicSortedList for displaying the list of messages. Note that the default ordering of instances can be defined through an OrderBy ViewComponentPart, which the user can override by exploiting the SortAttributes specified in the component.

##### Scrollable list

A very popular behavior in web applications is the paging of long lists of elements into fixed-size blocks, with commands for scrolling. This is often used, for example, as the base of search engine interfaces. A variant is the scrolling of blocks consisting of individual objects, as found, for instance, in image galleries.

**ScrollableList**

The ScrollableList is an extension of the List ViewComponent that allows the user access ordered DataBinding instances grouped in blocks. The ScrollableList ViewComponent has an attribute called “block size” that specifies how many instances constitute a block. It also has an implicit parameter (named current), which holds the block currently in view, and implicit events for moving to the first, last, i-th, next, and previous block.
Figure 7.11 revises the search pattern introduced in chapter 5 to cater to the scrolling of paged results.

##### Nested list

The multilevel master detail pattern illustrated in chapter 5 can be compacted into a ViewComponent, by nesting one list inside another.

**NestedList**

The NestedList is an extension of the List ViewComponent that denotes the nesting of multiple lists, one inside another.
The data model of the NestedList comprises one top-level DataBinding, which typically refers to a class of the domain model. Within the top level DataBinding, one or more first-level NestedDataBindings can be specified that refer to one of the association roles of the class referenced in the top-level DataBinding. Each first-level NestedDataBinding in turn can comprise one or more second-level NestedDataBinding. A second-level NestedDataBinding refers to one of the association roles of the class target of the association role used in the first-level NestedDataBinding. Figure 7.12 shows an example of usage of the NestedList ViewComponent.
The product catalog consists of a three-level nested list. At the top level, categories are displayed. At the next level, the products of each category are listed. At the innermost level, two separate nested lists are presented: the accessories of a product and the other products frequently sold with it. When the user selects a product at the second or third level and an accessory at the third level, the chosen object is displayed either in the “ProductDescription” or in the “AccessoryDescription” ViewContainer.

## Mobile Extensions

Mobile applications have rich interfaces that resemble on a smaller scale those of full-fledged desktop applications. Mobility and the availability of sensors, such as cameras and GPS, introduce features that are best captured by providing extensions of the IFML core specialized for mobile application development.

### Context Extensions

The context assumes a particular relevance in mobile applications, which must exploit all the available information to deliver the most efficient interface. Therefore, the context must gather all the dimensions that characterize the user intent, the capacity of the access device and of the communication network, and the environment surrounding the user.
Various dimensions of the context relevant to mobile applications have been catalogued and characterized in several standards and standard proposals, briefly overviewed in the bibliographic notes at the end of this chapter. In this section, we exemplify the most interesting ContextDimensions and ContextVariables that characterize mobile application usage. The illustration is not meant to be exhaustive. Rather, its aim is exemplifying how the contextual features can be represented as IFML extensions and used to model the effect of context on the user interface. The main aspects of the Context are listed below. Some of them have to be considered as ContextDimensions (and thus allow the selection of a Context or another), while other are ContextVariables (thus enabling the use of their value as parameters within the IFML models.
- Device: this family of context features can be exploited to specify the adaptation of the interface to different device characteristics, most notably the size and resolution of the screen. These features are usually exploited as ContextDimensions:
 - DiagonalSize: the physical size of the screen, measured as the screen’s diagonal;
 - SizeCategory: for convenience, screen sizes can be grouped in classes that can be treated homogenously (e.g., SMALL, NORMAL, LARGE, EXTRA LARGE); and
 - DensityCategory: for convenience, screen density measures can also be grouped in classes treated homogenously (e.g., LOW, MEDIUM, HIGH, EXTRA HIGH).
The following information becomes handy as ContextVariables, so as to calibrate precisely the UI rendering based on some calculation over the size data:
- PixelSize: the actual horizontal and vertical size of the screen, measured in pixels;
- Density: the quantity of pixels per unit area measured in dpi (dots per inch).
Other characteristics of the device may be considered, such as internal memory size, processing power, and battery status. However, they are less frequently used in the design of applications.
- Network connectivity: this dimension can be used to adapt the quantity or quality of content published in the interface, based on the capacity of the network link (e.g., replacing the display of a large media file with a lighter preview when bandwidth is limited). The relevant ContextDimension is ConnectivityType, which denotes the kind of network available; it can have such values as NONE, BLUETOOTH, NFC, ETHERNET, MOBILE (E, G, 3G, 4G, …), WIFI, and WIMAX;
- Position: this family of features can be used to adapt the interface to the presumed activity of the user (e.g., simplifying the interaction commands when the user is moving) or to publish content that depends on the location (e.g., local news or alerts). The ContextDimensions related to position are:
 - SensorStatus: denotes the activity status of the position engine of the device. It can have values such as: ACTIVE, INACTIVE.
 - Activity: denotes the physical user’s activity inferred by the sensor data; possible values are: still, walking, running, cycling, and in-vehicle.
The ContextVariables that can be exploited when the SensorStatus is ACTIVE are:
- Location: denotes the position of the device, expressed in latitude and longitude coordinates;
- Accuracy: denotes the accuracy of the position.
- Speed: denotes the ground speed of the device.
- Altitude: denotes the altitude above sea level of the device.

### Containers Extensions

As shown in chapter 4, the composition of mobile application interfaces can be expressed properly with the core IFML concepts of ViewContainers and ViewComponents. However, a characteristic trait of mobile interfaces—also present in desktop applications although less pervasively—is the utilization of predefined ViewContainers devoted to specific functionalities. These system-level containers provide economy of space and enforce a consistent usage of common features. Examples are the “Notifications” area or the “Settings” panel. These special ViewContainers can be distinguished (e.g., by stereotyping them as «system»).

**System ViewContainer**

A ViewContainer stereotyped as «system» denotes a fixed region of the interface, managed by the operating system or by another interface framework in a cross-application way.
Figure 7.13 shows an example of the usage of system ViewContainers by revisiting the e-mail application running example with a simplified composition of the interface more suited to a small screen. A system-level ViewContainers is employed to deliver notifications, which are typically placed in a fixed position within the header region of the interface. Another system ViewContainer, “Settings,” is also used to denote that the standard “Settings” command and window of the operating system are exploited to open the configuration functionality of the e-mail application in the interface region normally devoted to this task for all the applications.
Flexible layouts, another pattern using ViewContainers, are very useful for mobile applications.

### Component and Event Extensions

Like ViewContainers, ViewComponents can be predefined in the system as default interface elements that provide basic functionality in a consistent manner to the application developer. An example is the media gallery present in most mobile platforms. The «system» stereotype can be applied also to ViewComponents to highlight that the interface uses the components built into the system.

### Cameras and Sensors

Mobile applications can interact with one or more cameras onboard the device. The basic interaction with the camera requires modeling the ViewContainer for visualizing the camera image and commands, the invocation of an Action for taking the picture, the asynchronous event that notifies that the photo has been taken, and the visualization of the image in the system-level media gallery.
Figure 7.14 shows an example of usage of the camera and of the system-level media gallery. The “PhotoShooter” ViewContainer comprises a system ViewContainer “CameraCanvas,” which denotes the camera image viewer. The “Settings” event opens a modal window for editing the camera parameters, and the “Shoot” event permits the user to take a picture. When the image becomes available, a viewer is activated, from which an event permits the user to open the photo in the system media gallery. The internal viewer is modeled as a scrollable list, with block size = 1 to show one image at a time, and an OrderBy ViewComponentPart with a sorting criterion by timestamp to present the most recent photo first.

### Communication

Mobile devices communicate in a variety of ways with other fixed or mobile devices that can be discovered dynamically. The aspects of communication that may affect the interface are:
- Connectivity update notifications: they signal the change of the available communication channels and can be captured as system events that express an update of one or more ContextDimensions; and
- Devices in range: other devices can enter or leave the communication range. This feature can be modeled as a system event that signals the discovery of a device. Data transfer activities can be modeled as Actions that encapsulate the details of the protocol used to manage the conversation.
Figure 7.15 shows an example of communication-enabled interface: the usage of near field communication (NFC) for exchanging the contact details of the user.
The application consists of two parts, a sender and a receiver. The “NFCCardSender” interface is minimal, because NFC normally requires the communicating devices to be very close and thus there is little space for user’s interaction. The interface presents the personal data to the user who can confirm his intent to make them available to NFC devices in range. The “SendViaNFC” Action abstracts the steps necessary to build up the NFC record and notify the device that it is ready to be dispatched.
The “NFCCardReceiver” ViewContainer models the application on the side of the receiver. The reception of the NFC payload is modeled as an asynchronous event that abstracts the system process of parsing NFC messages and triggering the registered applications that handle them. The interface is again very basic: the user can confirm and save the data or discard the message.

Figure 7.16 shows an example of adaptation of the interface composition to the network type.
The interface for reading a message is implemented in two versions. One version presents a message with all its attachments downloaded automatically. The second interface requires an explicit user command for downloading an attachment, and the attachments are downloaded and shown one at a time using a ScrollableList. The choice of which alternative interface to use is conditioned by means of an ActivationExpression, illustrated in chapter 5, that tests the type of connectivity available based on the ContextVariable ConnectivityType. On-demand attachment visualization is selected when the connection type is “MOBILE” to reduce bandwidth consumption and interface latency.

### Position

Location awareness enables devices to establish their position so that mobile applications can provide users with location-specific services and information, set alerts when other devices enter or leave a determined region, and adapt the interface to the current user’s physical activity, such as walking, running, or driving.
Figure 7.17 shows an example of the usage of the position sensor.
The “Start” event in the “Tracker” ViewContainer allows the user to activate the continuous position tracking system of the device. The Form ViewComponent enables the specification of the position tracking parameters, such as accuracy and frequency, which are communicated to the system service via the “ActivatePositionUpdates” Action. After activating the tracking system, the application starts listening to incoming asynchronous SystemEvents, which provide updates of the current position at the established frequency. Such events carry parameters indicating the timestamp of the recording and the geographical coordinates, and trigger a background action that stores such data as “Point” objects. The list of recorded points is visualized in the “TrackingPoints” List ViewComponent. At any moment, the user can clear the list of recordings, save the recorded points as a track object, or stop the position tracking system.

### Maps

Maps are a powerful interface over geographic data. The integration of digital maps into user interfaces has become very popular with the advent of the web. Mobile applications add a special flavor to map-based interfaces by combining the dynamic position of the user with the representation of topographic data. Digital maps have become a commodity supported by many proprietary and open-source services. This rich offer boosts the development of map-enabled applications on top of off-the-shelf functionality, for:
- connecting to the mapping service and downloading map tiles for display on the device screen with controls such as pan and zoom for moving the map and zooming in or out;
- setting the map type, choosing among several alternatives, such as normal, satellite, hybrid, and 3D; and
- initializing and changing the viewpoint over the map (also called “camera,” to highlight that the map view is modeled as a camera looking down on a flat plane); the rendering of the map is governed by such properties as location, zoom, bearing, and tilt.
A simple way of modeling the map view is to extend the concept of ViewContainer to denote an off-the-shelf map visualization interface. Application-specific content and events can then be added to such an extended ViewContainer as further ViewElements and Events.

**MapView**

A MapView is an extension of ViewContainer that denotes a map view. It supports the events for panning and zooming and for changing the map type and the camera parameters.

Content—both static and interactive—overlaid on the map can be modeled by extending the ViewComponent concept. For example, the «marker» stereotype can be added to Details and List to denote that the DataBinding instances have a position and are rendered on the map as interactive markers.

**Marker**

A Marker is an extension of ViewComponent usable in MapView containers that denotes that the underlying DataBinding instances possess a location attribute that is displayable in a map view. It supports the events for selecting, dragging, and dropping.

Another useful way to present an ordered set of locations is the path visualization.

**Path**

A Path is an extension of the List ViewComponent usable in MapView containers that presents underlying DataBinding instances (that must possess a location attribute) as a polyline in a map view. It supports events for selecting the entire path or a single point on it.
Figure 7.18 elaborates the example of Figure 7.17 to show the usage of the MapView ViewContainer and of the map-specific extensions of the List ViewComponent.
The plain visualization of the tracked points exemplified in Figure 7.17 is replaced by two alternative map-based displays modes. The recorded points are viewable either as a set of markers or as path on the map.

### Gestures

Touch screens enable the use of gestures for the direct manipulation of screen objects. The gestures supported by touch devices include touch, double touch, press, swipe, fling, drag, pinch in and out, and several more. These gestures have well-defined semantics and consolidated conventions to which the interface design must conform to provide a consistent user experience. They can be represented in IFML by extending the core Event concept.
Figure 7.19 shows an example that uses the touch and press events. The distinction between these two gestures allow a finer control over the effect of acting upon the screen objects, much in the same way as mouse click and double click do in desktop applications.
Figure 7.19 revisits the master detail pattern to highlight the usage of touch gestures. The conventions illustrated in the example adhere to the best practices in popular mobile operating systems, such as Android 4. In a master detail interface, the touch gesture activates the default action on the object (in this case, the opening of the details view). The press gesture instead activates the selection mode, whereby one or more objects can be chosen with a touch event, and a toolbar of commands is displayed to act upon the selected object(s). This behavior is represented in Figure 7.19 by using the «press» and «touch» event extensions and by conditioning the effect of the touch event based on the existence of at least one previously selected object. Other gestural conventions can be represented in a similar way.

## Multiscreen Extensions

Single screen applications are conceived to work for a single class of access devices, with homogeneous capabilities. They define the composition of the interface at design time by specifying the hierarchy of ViewContainers and the disjunctive or conjunctive nesting of containers. Multiscreen applications are instead designed to work on different devices, possibly with different screen characteristics. A goal for their development is to define the interface layout in a flexible way so that it can adapt dynamically to the size, orientation, and density of the screen.
Figure 7.20 shows an application for updating the device settings, designed to adapt to cellular phone small screens and to tablet wider screens. The interface supports two main tasks: picking the desired preference from a list, with the “Preferences” List ViewComponent, and editing its value, with the “PreferenceEditor” Form ViewComponent. The two ViewComponents that address such tasks communicate parameters to the “UpdatePreference” Action through their outgoing NavigationFlows and the ParameterBindingGroups associated with them.
The flexible interface composition is expressed by means of the “Settings” ViewContainer, which hosts two distinct subcontainers: “Tablet Settings,” in which the two ViewComponents are kept together, and “Phone Settings,” in which they are visualized one at a time. The ActivationExpression of the subcontainers ensures that the proper composition pattern is activated based on the device information taken from the Context.
Figure 7.21 shows a mock-up of the interface composition adapted to the type of the screen.
Note that the model of Figure 7.20 duplicates the ViewComponents, Events, InteractionFlows, and Actions that specify the content and behavior of the interface in the two configurations. This duplication, which puts an unnecessary burden on the designer and may result in misalignment errors, can be avoided with the use of modules (explained in chapter 8).

## List of IFML design patterns

The name of a pattern is structured as XY-Z, where:

- X is the category of pattern. For instance, interface organization patterns start with the letter “O,” and content and navigation patterns are prefixed with “CN.”
- Y is the deployment platform where the pattern originated or is most frequently found. For instance, desktop patterns are labeled with “D,” web with “W,” mobile with “M.” The prefix is omitted for patterns that apply equally well to multiple platforms and for which there is no clearly prevalent platform.
- Z is a mnemonic label identifying the specific pattern.

### Interface Organization Patterns
| Code| Title| Description|
|-|-|-|
| OD-SWA| Simple work area| Distinguishes a work area where the main tasks of the application are performed along with one or more service areas|
| OD-MWA| Multiview work area| Extension of OD-SWA for multiple alternative views of the item in the work area|
| OD-CWA| Composite work area| Splits the work area into subregions devoted to different perspectives of the item, presented simultaneously|
| OD-MCWA| Multiview composite work area| Combines the decomposition of the work area into alternative perspectives and simultaneous partial views|
| OW-MFE| Multiple front ends on the same domain model| Provides different interfaces for different user roles upon the same information|
| OW-LWSA| Large web sites organized into areas| Applications that exhibit a hierarchical structure, whereby the pages of the site are clustered into sections dealing with a homogeneous subject|
| OM-MSL| Mobile screen layout| Maps the interface to a top-level grid that contains three regions: the header, the content area, and the footer|

### Content and Navigation Patterns
| Code| Title| Description|
|-|-|-|
| CN-MD and CN-MMD| Master detail and Master multidetail| Presents some items, and a selection permits the user to access the details of one instance at a time|
| CN-MLMD| Multilevel master detail| Also called a cascaded index; consists of a sequence of lists over distinct classes, such that each list specifies a change of focus from one object, selected from the index to the set of objects related to it via an association role; in the end, a single object is shown|
| CN-DEF| Default selection| Simulates a user choice at the initial access of a list, thus selecting a default instance|
| CN-SOT| Single object toolbar| Content-dependent toolbar that supports commands upon one object|
| CN-MOT| Multiple object toolbar| Content-dependent toolbar with commands that can be applied to multiple objects|
| CN-DT| Dynamic toolbar| Toolbar with commands that may vary at runtime based on the status of the interaction|
| CN-MSC| Multistep commands| Commands that involve multiple interaction steps|
| CN-CII| Commands with inline input| Collapses in the toolbar several steps needed to perform an action|
| CN-CIM&B| Content-independent navigation bar and menu| Groups commands that do not act upon specific objects but shortcut the navigation or help the user go back quickly|
| CN-UP| Up navigation| Refers to some hierarchical structure associated with the interface; it leads the user to the superior element in the view hierarchy|
| CN-BACK| Back navigation| “Back” refers to the chronology of user interaction; it leads back to the last visited ViewElement|
| CN-BREAD| Breadcrumbs| A navigation aid that shows the user location in the application interface|
| CN-PG| Paging| Displays a block of objects at a time and allows the user to scroll rapidly through the collection|
| CN-PR| Collection preview| Used with CN-PG, provides a preview of the object’s location in the sequence and of what comes before and after|
| CN-ALPHA| Alphabetical filter| Provides an alphabetic filter to partition the collection into chunks|

### Data Entry Patterns
| Code| Title| Description|
|-|-|-|
| DE-FRM| Multifield forms| Form for submitting information through several fields|
| DE-PLDF| Preloaded field| Variant of DE-FRM where some fields are preloaded with an existing value|
| DE-PASF| Pre-assigned selection field| Form where the value of a selection field is preselected|
| DE-DLKP| Data lookup| Data entry task that involves looking up information for filling in the fields|
| DE-CSF| Cascade selection fields| The data entry task involves entering a set of selections that have some kind of dependency on one another|
| DE-WIZ| Wizard| Partition of a data entry procedure into logical steps that must be followed in a determined sequence|
| DE-TDFP| Type-dependent field properties| Provides data entry facilities for form fields of specific data types|
| DE-RTE| Rich text editing| Provides an enriched text field in the shape of a microapplication that embodies the commands applicable to the text|
| DE-AUTO| Input auto-completion| Automatically provides suggestions for completing the input based on what the user has already typed in a field|
| DE-DYN| Dynamic selection fields| Occurs when the application requires the user to input data that have dependencies|
| DE-INPL| In-place editing| Allows the user to edit content without abandoning the current view to access a data entry form|
| DE-VAL| User input validation| Checks the correctness of the user input against validation rules and returns appropriate notification message(s)|

### Content Search Patterns
| Code| Title| Description|
|-|-|-|
| CS-SRC| Basic search| Keyword search upon a collection of items|
| CS-MCS| Multicriteria search| Composite search criteria upon a collection of items|
| CS-FSR| Faceted search| Allows the progressive refinement of search results upon structured multidimensional data, by restricting the objects that match the query based on their property values|
| CS-RSRC| Restricted search| Restricts the search focus to specific subcollections when searching large collections|
| CS-SRCS| Search suggestions| Exploits the auto-completion pattern and requires the logging of keywords previously inserted by the users; logged keywords matching the current user input are shown sorted by frequency|
| GEO-LAS| Location-aware search| Enables search of items that are related and close to the current user position|

### Content Management Patterns
| Code| Title| Description|
|-|-|-|
| CM-OCR| Object creation| Enables the creation of a new object in a data storage|
| CM-OACR| Object and association creation| Creates a new object and sets its associations to other objects|
| CM-ODL| Object deletion| Deletes one or more objects of a given class|
| CM-CODL| Cascaded deletion| Removes a specific object and all the objects associated with it via one or more associations|
| CM-OM| Object modification| Updates one or more objects of a given class|
| CM-AM| Association management| Used to create, replace, or delete instances of an association, by connecting or disconnecting some objects of the source and target classes|
| CM-NOTIF| Notification| The interface is updated (typically asynchronously) by the occurrence of a system generated event|
| CM-CBCM| Class-based content management| Addresses the creation, modification and deletion of an object and its association instances|
| CM-PBCM| Page-based content management| Supports blogs and page-based content management systems; management of whole pages is allowed|

### Identification and Authorization Patterns
| Code| Title| Description|
|-|-|-|
| IA-LOGIN| Login| Recognizes and checks the validity of a user-provided identity|
| IA-LOGOUT| Logout| Clears user’s authenticated identity preserved in the application navigation context upon explicit user request|
| IA-CEX| Context expiration notification| The authenticated identity of the user is cleared by the system for security reasons or because of timeout|
| IA-SPLOG| Login to a specific ViewContainer| Recognizes and checks the validity of a user-provided identity and enables access to a specific part of the user interface|
| IA-ROLE| User role display and switching| Displays the user role and allows change of role|
| IA-RBP and IA-NRBP| (Negative) role-based permissions for view elements| Implements (possibly negative) access permissions at the view level that depend on the user’s role|
| IA-OBP| Object-based permissions| Access control is expressed over the content objects and personalization associations in the content model|
| IA-PRO| User profile display and management| Shows and enables the editing of application-dependent information associated with the identity of an authenticated user|
| IA-IPSI| In-place sign-in| When the user attempts to trigger an action, the user is warned of the need to sign in and then routed to the login form|

### Session Management Patterns
| Code| Title| Description|
|-|-|-|
| SES-CR| Creating session data from persistent data| Stores information in the navigation session by collecting them from a persistent data source|
| SES-PER| Persisting session data| Creates persistent data from user navigation session data|
| SES-EXC| Session data expiration catching| Handles the asynchronous notification of the expiry of the session to the user interface by causing an automatic refresh of the content|

### Social Functions Patterns
| Code| Title| Description|
|-|-|-|
| SOC-AW| Activity wall| Logs the social activity typical of a social network platform|
| SOC-SH| Sharing, liking, and commenting| Enables posting, commenting, liking, and sharing content produced by other community members|
| SOC-FR| Friendship management| Manages a symmetric (friendship) or asymmetric (following) association between users|
