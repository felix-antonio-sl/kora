---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-63
  provenance:
    created_by: atomize
    created_at: '2026-04-18'
    source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
version: 1.0.0
status: draft
tags:
- atomic
- knowledge
- opm-libro-rebuilt
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:skill:atomize:1.0.0
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 42
      segmented: true
      segment_role: segment
      segment_index: 63
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-63
---

# Atomic opm-libro-rebuilt - Segmento 63

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `42`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `63/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 20 Generalization and Instantiation / 20.5.2 Instantiation Versus Specialization

- **P3263** · `fact` · Generalization-specialization is a transitive structural relation that gives rise to a hierarchy tree. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3264** · `fact` · Each level in the hierarchy contains specializations of the level above it. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3265** · `fact` · The “leaves” of that hierarchy are the instances of the class. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3266** · `fact` · Thus we can say that instantiation is a special case of specialization, which, in the context of the system under study or development, cannot be specialized further. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3267** · `constraint` · Figure 20.13 shows a specialization hierarchy that starts with Car as its top level and presents increasingly specialized object classes until it gets to Jack’s Car. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3268** · `fact` · This is the first object that is physical and unique. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3269** · `fact` · It has a VIN (vehicle identification number) that uniquely identifies it, and at any given moment the values or states of all its attributes, such as Color, Location, Mileage and Speed, can be specified. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3270** · `fact` · Instance is a leaf in the generalization-specialization hierarchy—it is not possible to have specializations of an instance. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3271** · `fact` · Inheritance of features from a class to its instances is exactly the same as the inheritance of features from a super-class to its sub-class anywhere along the generalization- specialization hierarchy. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3272** · `constraint` · The only differences are that (1) an instance cannot have further specializations, because it is at the bottom of the hierarchy, and (2) only an instance has concrete values of its attributes, as Fig. 20.13 demonstrates. · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)
- **P3273** · `constraint` · 288 Generalization and Instantiation the time of observing it · [src:S01:L8331-L8347](../../../INBOX/opm-libro.txt#L8331-L8347)

## opm libro · Chapter 20 Generalization and Instantiation / 20.6 The Relativity of Instance

- **P3274** · `fact` · Like many other concepts we have encountered, the term instance is relative to the system of discourse. · [src:S01:L8349-L8354](../../../INBOX/opm-libro.txt#L8349-L8354)
- **P3275** · `fact` · What for a certain system is considered instance of a class, can for another system be just a sub-class of a super-class. · [src:S01:L8349-L8354](../../../INBOX/opm-libro.txt#L8349-L8354)
- **P3276** · `fact` · An instance in one system may be a class that has instances or that further recursively specializes into more refined classes, which ultimately have instances. · [src:S01:L8349-L8354](../../../INBOX/opm-libro.txt#L8349-L8354)
- **P3277** · `fact` · To demonstrate this, let us look at a few examples from the world of cars. · [src:S01:L8349-L8354](../../../INBOX/opm-libro.txt#L8349-L8354)
- **P3278** · `constraint` · We have seen that Taurus 2015 is an object class of all the instances of cars made by Ford of model Taurus manufactured in the year · [src:S01:L8349-L8354](../../../INBOX/opm-libro.txt#L8349-L8354)
- **P3279** · `constraint` · Suppose that the system we are now concerned with is a system for comparing and evaluating cars of model year 2015. One of the instances in this system is Taurus 2015, and it is an instance of the object class Model Year 2015 Car. Physical cars with specific VIN do not exist and have no meaning in this system. In the gen-spec hierarchy tree, Taurus 2015 is one of the leaves: it has no further specializations beneath it. As another example, consider a national highway system, in which the system architects are interested in the various types of vehicles that use the roads. What matters to them about the vehicles are their size, weight, average speed, and average annual distance that each type of vehicle travels. The designers of this system therefore decided to categorize vehicles into three types: cars, trucks and buses. While these three types are specializations of vehicle, for the system under consideration they are also the three instances of the object class vehicle. The architects are not interested in each individual car, bus or truck, so the number of each vehicle type, its average speed, mileage, etc. are attributes of vehicle that are inherited to its three instances. Consider now a different system of the Motor Vehicles Taxation Office in some country, which, for taxation purpose differentiates between Taxation Classes of Motor Vehicles as follows: Commercial Van, Sedan, Collector Car, Sports Utility Vehicle, and Luxury Car. For this system, cars are differentiated into these types based on their Market Value and Application. Furthermore, the system maintains and constantly updates a list of each Vehicle Manufacturer and each Vehicle Model by Year Model, with an indication of which Vehicle Model belongs to which Taxation Class. Here, the Taxation Class is an attribute of Vehicle. Commercial Van, Sedan, etc., are values of the Taxation Class attribute of Vehicle. The instances of the class Vehicle in this system are the various Year Models, because the system is only concerned with setting tax levels on cars by Taxation Class and does not care about individual cars. Finally, consider a car dealership. Here, of course, each individual car has its own record, including its VIN, make, model, year, owner, etc. This is the “classical” case of instance, similar to the one presented in Fig. 20.13, where each instance is a physical entity with its unique identifier. However, as we have seen, instances can be informatical, such as car models, vehicle types or records in a file. · [src:S01:L8355-L8382](../../../INBOX/opm-libro.txt#L8355-L8382)

## opm libro · Chapter 20 Generalization and Instantiation / 20.7 Constraining Attribute Values

- **P3280** · `fact` · A class can be used to constrain the possible range of attribute values. In Fig. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3281** · `constraint` · 20.14, Adult is a class with three attributes: Gender, with possible values female and male, Height in cm, with possible values 120..240 (120 through 240), and Weight in Kg, with possible values 40..240. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3282** · `constraint` · Jack Robinson is an instance of Adult, with Gender value male, Height value 185 cm, and Weight value 88 Kg. As Fig. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3283** · `constraint` · 20.14 demonstrates, the name of the instance of Adult, Jack Robinson in this case, can be followed by the semicolon symbol “:” followed by the name of the class. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3284** · `constraint` · This is useful when only the instance appears in an OPD without being attached to this class. right) 290 Generalization and Instantiation 7.537 gr/cm3. The OPD in Fig. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3285** · `constraint` · 20.15 presents the class Metal Powder Mixture, indicating that its Specific Weight attribute value can range from 7.545 to An operational (runtime) instance of Metal Powder Mixture is Mixture Lot #7545 with Specific Weight attribute value is 7.555 gr/cm3. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)
- **P3286** · `constraint` · This value is within the allowable range. value, which is in the constrained range The OPL sentence “Mixture Lot #7545 exhibits Specific Weight in gr/cm3.” , is not present in the OPL of Mixture Lot #7545 is an instance of Metal Powder Mixture, and therefore Mixture Lot #7545 inherits this attribute from Metal Powder Mixture. · [src:S01:L8384-L8404](../../../INBOX/opm-libro.txt#L8384-L8404)

## opm libro · Chapter 20 Generalization and Instantiation / 20.8 Process Instances

- **P3287** · `fact` · OPM instantiation applies not just to objects but also to processes. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3288** · `fact` · The processes we have encountered so far are actually process classes: they are patterns of happenings that involve object classes. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3289** · `fact` · A process class is a pattern of happening (the sequence of subprocesses), which involves object classes that are members of the involved object set of that process class. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3290** · `fact` · A process occurrence, which follows this pattern and involves particular object instances in its preprocess and postprocess object sets, is a process instance. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3291** · `requirement` · Hence, a process instance shall be a particular occurrence of a process class to which that instance belongs. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3292** · `fact` · Any process instance is therefore associated with a distinct set of preprocess and postprocess object instance sets. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3293** · `fact` · A process instance is a particular occurrence of a process class to which that instance belongs. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3294** · `fact` · The power of the process class concept is that it enables the modeling of a process as a template or a protocol for some transformation that a class of objects undergoes. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3295** · `fact` · That transformation includes neither the spatio-temporal framework nor the particular set of object instances with which the process instance is associated; these can be identified only when we are at the instance level, or operational level of the system. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3296** · `fact` · A process instance is a concrete occurrence of a process class, whose preprocess and postprocess object sets are sets of object instances. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3297** · `fact` · In particular, a process instance has a time stamp, a specific date and time at which the process started or ended. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3298** · `constraint` · Figure 20.16 depicts on the left Movie Showing as an example of a process class, with Movie, and Theatre as instruments of this process class, Date & Time as its attribute, and Audience as the class’ affectee. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3299** · `fact` · In the OPD on the right, Gone With The Wind Premiere Gala Movie Showing is a process instance of the Movie Showing process class. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3300** · `fact` · All the instances are greyed out to distinguish them from their classes. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3301** · `fact` · Gone With The Wind is an instance of Movie, Atlanta Theatre is an instance of Theatre, Atlanta Audience is an instance of Audience, and Dec. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3302** · `constraint` · 15 1939 8PM (Dirks 2015) is the value of Date & Time at which the process instance took place. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3303** · `fact` · The same objects instance can participate in two or more process instances. · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
- **P3304** · `constraint` · For example, the same is an instance of Movie, identified by its name as Gone With The Wind, can participate in all the process instances of Gone With The Wind Movie Showing (other than the premier gala one), but each Atlanta Audience is a different instance of Audience, since it is comprised of a different set of movie goers. 292 Generalization and Instantiation · [src:S01:L8406-L8438](../../../INBOX/opm-libro.txt#L8406-L8438)
