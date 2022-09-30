---
title: "Paper Reading: DEPSKY Eurosys'11"
date: 2019-07-01
permalink: /posts/2019/07/paper-reading-depsky-eurosys11/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - cryptography
---

DEPSKY: A High-Availability and Integrity Layer for Cloud Storage

Last updated: 28-01-2021

Download
------
[EuroSys, 2011](http://www.di.fc.ul.pt/~bessani/publications/eurosys11-depsky.pdf)


Summary
------

This paper presents DEPSKY, a system that improves the availability, integrity and confidentiality of information in clouds through encryption, encoding and replication of the data on cloud-of-clouds. They proposed Byzantine quorum system protocols named **DepSky-A and Depsky-CA**, which improve the availability and the access latency compared with individual clouds. Depsky presents a single-writer multi-reader read/write register abstraction atop of multiple clouds. The **estimated** monetary costs of using DEPSKY is twice the cost of using a single cloud, which is acceptable as stated. DEPSKY doesnot require server (storage node) to execute any additional code, but still being efficient by requiring only two communication round-trips for each operation (read / write).


Details
------


### System Architecture


![depsky-architect][depsky-architect]

1. DEPSKY is implemented in Java as a software library in the **client side only**.
  * Data unit manager, system core (functions), cloud provider drivers (including local storage)
  * Client invoke cloud operations (put, get, delete, etc..)


### Data model

![depsky-data-model][depsky-data-model]


1. Three levels of data abstraction in DEPSKY data model.
  * *Conceptual data unit*, which the algorithm work. Support creation, destruction.
  * *Generic data unit* (or *container*) in an *abstract storage cloud*. Seperates data and metadata.
  * *Data unit implementation* with container translated into the specific constructions supported by each cloud provider.

2. metadata: multiple versions, arbitrary sizes


### System Model

1. Single writer, multiple readers.
  * "Presented" do not support concurrent write.
  * How to support concurrent write? *low contension lock*: a zero byte file *lock-ID-T*, with a safety margin "theta", concerning the synchronized clocks between multiple writers


### Algorithms for r/w

Assumption:
  * All clouds supports basic operations (create, put, get, delete, list, etc.)

1. DEPSKY-A

(1) write: 
  * Query metadata from all nodes, pick the largest version number
  * calculate hash for the data being written, and append to the data
    * format: **plain text**
  * write data to all clouds
  * update metadata
  * write metadata to all clouds (the last step to guarantee "metadatacomes after data")
(2) read
  * read metadata from all nodes
  * call read(max_version) from all clouds in parallel
    * as soon as it gets the data from the fastest node, and verify the correctness of data by checking the hash, **call cancel_pending for other nodes**(even it's still transmitting)

2. DEPSKY-CA (Intergrates DEPSKY-A with additional cryptographic and coding functions)
  * Add erasure coding (RS) and secret sharing scheme
  * data[i] = encode(encrypt(raw_data, secret_key)) + share(secret_key)[i]
  * read: gets fastest f + 1 copies of data


### Optimization

* read optimization: sort the clouds based on some criteria (latency, access monetary costs, etc.)


### Other protocols

1. Create/delete data unit from clouds

2. GC (delete old versions behind)

3. Cloud reconfiguration
  * repetitively read all data units from clouds, create data unit on the new cloud, and write the data unit to the new cloud
  * delete the data unit from the cloud that is not being used


### Evaluation

* Estimation
  * Cost reduction: about two times the cost of using a single cloud using Depsky-CA, thus "extra costs due to replication are affordable".

* Evaluation
  * Use PlanetLab to run several clients accessing clouds
  * DEPSKY-A presents the best "latency" of all but one setups. Reason: it measures overall time, including metadata reading from multiple clouds and data reading **ONLY from one cloud**. The overall speed is closely related to the fastest second cloud provider. **Variance of the results are very high**, when accessing data around the world.
  * Observation: the fastest metadata replier is not the fastest data replier. Possible reason: data providers have different capability to handle small files (metadata).
  * read speed is bounded by the best cloud r speed, write speed is bounded by the worse cloud w speed.



Strength
------

* No "server side" deployment required.

* First single-writer-multi-reader register implementation supporting coding and confidentiality.

* Extensive evaluation of the (heterogenious) multi-cloud system

Weakness
------

1. Common problems for client-side only deployment
  * Computation required: EC, hashing, etc, although in the paper, EC and secret sharing is not the bottleneck.
  * Overall throughput maybe bounded by the client
    * read: the data is read from ALL nodes in parallel, the performance maybe bounded by the client bandwidth.
      * Read optimization (sorting the clouds) takes effect in heterogenious deployment.
    * write: the *writeQuorum* function requires ACKs from n - f nodes. In actual implementation, write can also be parallelized. 

2. Lock scheme
  * Single write only.
  * Require coordinator system (ZooKeeper, DepSpace, etc.) to coordinate multiple writes

3. Passive system status management
    * Monitoring of cloud status (engineering problem)
    * System failures (repairing) should be handled manually
      * e.g. handling for failed write, auto recovery when some of the clouds fail

5. engineering related
  * storage interfaces
  * no centralized metadata store for file listing


<!-- refs -->

[depsky-architect]: /images/2019-07-01-paper-reading-depsky/depsky-architect.jpg "depsky-architect"

[depsky-data-model]: /images/2019-07-01-paper-reading-depsky/depsky-data-model.jpg "depsky-data-model"