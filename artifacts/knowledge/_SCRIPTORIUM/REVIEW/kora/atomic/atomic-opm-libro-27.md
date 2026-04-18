---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-27
  provenance:
    created_by: atomize
    created_at: '2026-04-18'
    source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
version: 1.0.0
status: draft
tags:
- atomic
- knowledge
- opm-libro
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:skill:atomize:1.0.0
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 3
      segmented: true
      segment_role: segment
      segment_index: 27
      segment_count: 32
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-27
---

# Atomic opm-libro - Segmento 27

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `3`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `27/32`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro (Parte 27)

- **P113** · `requirement` · Suppose that the system we are now concerned with is a system for comparing and evaluating cars of model year 2015. One of the instances in this system is Taurus 2015, and it is an instance of the object class Model Year 2015 Car. Physical cars with specific VIN do not exist and have no meaning in this system. In the gen-spec hierarchy tree, Taurus 2015 is one of the leaves: it has no further specializations beneath it. As another example, consider a national highway system, in which the system architects are interested in the various types of vehicles that use the roads. What matters to them about the vehicles are their size, weight, average speed, and average annual distance that each type of vehicle travels. The designers of this system therefore decided to categorize vehicles into three types: cars, trucks and buses. While these three types are specializations of vehicle, for the system under consideration they are also the three instances of the object class vehicle. The architects are not interested in each individual car, bus or truck, so the number of each vehicle type, its average speed, mileage, etc. are attributes of vehicle that are inherited to its three instances. Dori – Model-Based Systems Engineering with OPM and SysML 289 Consider now a different system of the Motor Vehicles Taxation Office in some country, which, for taxation purpose differentiates between Taxation Classes of Motor Vehicles as follows: Commercial Van, Sedan, Collector Car, Sports Utility Vehicle, and Luxury Car. For this system, cars are differentiated into these types based on their Market Value and Application. Furthermore, the system maintains and constantly updates a list of each Vehicle Manufacturer and each Vehicle Model by Year Model, with an indication of which Vehicle Model belongs to which Taxation Class. Here, the Taxation Class is an attribute of Vehicle. Commercial Van, Sedan, etc., are values of the Taxation Class attribute of Vehicle. The instances of the class Vehicle in this system are the various Year Models, because the system is only concerned with setting tax levels on cars by Taxation Class and does not care about individual cars. Finally, consider a car dealership. Here, of course, each individual car has its own record, including its VIN, make, model, year, owner, etc. This is the “classical” case of instance, similar to the one presented in Fig. 20.13, where each instance is a physical entity with its unique identifier. However, as we have seen, instances can be informatical, such as car models, vehicle types or records in a file. 20.7 Constraining Attribute Values A class can be used to constrain the possible range of attribute values. In Fig. 20.14, Adult is a class with three attributes: Gender, with possible values female and male, Height in cm, with possible values 120..240 (120 through 240), and Weight in Kg, with possible values 40..240. Jack Robinson is an instance of Adult, with Gender value male, Height value 185 cm, and Weight value 88 Kg. As Fig. 20.14 demonstrates, the name of the instance of Adult, Jack Robinson in this case, can be followed by the semicolon symbol “:” followed by the name of the class. This is useful when only the instance appears in an OPD without being attached to this class. Fig. 20.14 The attribute values of the calss Person are constrained with value ranges (class on left and instance on right) 290 Generalization and Instantiation 7.537 gr/cm3. The OPD in Fig. 20.15 presents the class Metal Powder Mixture, indicating that its Specific Weight attribute value can range from 7.545 to An operational (runtime) instance of Metal Powder Mixture is Mixture Lot #7545 with Specific Weight attribute value is 7.555 gr/cm3. This value is within the allowable range. Fig. 20.15 Constrsaining attribute value. Left: The class and it attribute value range. Right: the instance and its actual value, which is in the constrained range The OPL sentence “Mixture Lot #7545 exhibits Specific Weight in gr/cm3.” , is not present in the OPL of Fig. 20.15, because that sentence is implicit from the expressed fact “ Mixture Lot #7545 is an instance of Metal Powder Mixture, and therefore Mixture Lot #7545 inherits this attribute from Metal Powder Mixture. 20.8 Process Instances OPM instantiation applies not just to objects but also to processes. The processes we have encountered so far are actually process classes: they are patterns of happenings that involve object classes. A process class is a pattern of happening (the sequence of subprocesses), which involves object classes that are members of the involved object set of that process class. A process occurrence, which follows this pattern and involves particular object instances in its preprocess and postprocess object sets, is a process instance. Hence, a process instance shall be a particular occurrence of a process class to which that instance belongs. Any process instance is therefore associated with a distinct set of preprocess and postprocess object instance sets. A process instance is a particular occurrence of a process class to which that instance belongs. The power of the process class concept is that it enables the modeling of a process as a template or a protocol for some transformation that a class of objects undergoes. That transformation includes neither the spatio-temporal framework nor the particular set of object instances with which the process instance is Dori – Model-Based Systems Engineering with OPM and SysML 291 associated; these can be identified only when we are at the instance level, or operational level of the system. Fig. 20.16 Movie Showing as an example of a process class (left) and its instace (right) A process instance is a concrete occurrence of a process class, whose preprocess and postprocess object sets are sets of object instances. In particular, a process instance has a time stamp, a specific date and time at which the process started or ended. Figure 20.16 depicts on the left Movie Showing as an example of a process class, with Movie, and Theatre as instruments of this process class, Date & Time as its attribute, and Audience as the class’ affectee. In the OPD on the right, Gone With The Wind Premiere Gala Movie Showing is a process instance of the Movie Showing process class. All the instances are greyed out to distinguish them from their classes. Gone With The Wind is an instance of Movie, Atlanta Theatre is an instance of Theatre, Atlanta Audience is an instance of Audience, and Dec. 15 1939 8PM (Dirks 2015) is the value of Date & Time at which the process instance took place. The same objects instance can participate in two or more process instances. For example, the same is an instance of Movie, identified by its name as Gone With The Wind, can participate in all the process instances of Gone With The Wind Movie Showing (other than the premier gala one), but each Atlanta Audience is a different instance of Audience, since it is comprised of a different set of movie goers. 292 Generalization and Instantiation 20.9 Summary Generalization-specialization is the relation between a general thing and a specialization of that thing. Classification-instantiation is the relation between a class of things and a unique instance that belongs that class. Generalization-specialization gives rise to inheritance from the generalized thing to the specialized one(s). Inheritance is of features (attributes and operations), structural relations and procedural relations. For objects, states are inherited too. OPM processes specialize in a manner similar to objects. States of specialized objects can override inherited states. A class is a template, from which things that instantiate the class can be generated as members of that class. Instance is a relative term. A specialization in one system can be an instance in another. A process instance is a particular occurrence of a process at a given point in time and whose involved object set is a set of object instances. 20.10 Problems · [src:S01:L8355-L8455](../../../INBOX/opm-libro.txt#L8355-L8455)
- **P114** · `constraint` · 2. 3. 4. 5. Provide two examples of object specializations and two of process specializations. Specify them in OPDs and OPL. Create a specialization hierarchy of sports games, which would include as a minimum volleyball, basketball, soccer, football, tennis, and baseball. Apply OPM to show what features are common and inherited, and what are game-specific. Repeat the previous problem for a specialization hierarchy of track and field sport types, which would include at least three types of running, three types of swimming and three types of throwing. Considering the inheritance of procedural links, are the effect links redundant? Why or why not? Draw the OPD expressed in the OPL paragraph below. Pilot, Sailor, and Driver are Occupations. Airplane, Vessel, and Truck are Transportation Systems. Flying, Sailing, and Driving are Transporting. · [src:S01:L8456-L8468](../../../INBOX/opm-libro.txt#L8456-L8468)
- **P115** · `constraint` · Complete the OPD from the previous question with the following model facts: (1) Pilot, Sailor, and Driver handle Flying, Sailing, and Driving, respectively. (2) Flying, Sailing, and Driving require Airplane, Vessel, and Truck, respectively. Dori – Model-Based Systems Engineering with OPM and SysML 293 · [src:S01:L8469-L8473](../../../INBOX/opm-libro.txt#L8469-L8473)
