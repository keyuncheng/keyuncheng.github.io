---
title: "Paper Reading: HotStorage'20 Sharing and Caring"
date: 2021-02-25
permalink: /posts/2021/02/paper-reading-sharing-hotedge20/
author_profile: false
excerpt: false
tags:
  - Edge Computing
  - Storage
---


Sharing and Caring of Data at the Edge


Download
------
[HotEdge, 2020](https://www.usenix.org/system/files/hotedge20_paper_trivedi.pdf)


Summary
------

This paper studies edge computing, including the edge enviroment / architecture, edge applications, existing (storage) solutions, and challenges. This paper also brings an initial design of Griffin, a shared stoarge devices for the edge. A set of open topics are raised for discussion and follow-ups.



Details
------

### Architecture

![system-architecture][system-architecture]



1. Features of edge
  * Distributed, Heterogeneous, dynamic architecture

2. Applications on edge
  * ML
  * Games
  * autonomous driving
  * Stream processing
  * Analytics
  * Caching

3. Challenges

* Expressive APIs
* Data Locality
* Impacts of heterogeneous environment
  * Load balancing
* Mobility of clients
* Failure protection
* Scalability
* Flexible consistency model for vaious applications
* Monitoring
  * Architecture, system status

### Open issues (Picked from Sec 5 from the paper)

* How to do benchmark

* How to do resource provisioning on edge

* Data management

* How to efficiently monitor the edge and end devices



## paper collections

### introduction to edge computing

* The Emergence of Edge Computing.

* ETSI. Multi-access Edge Computing (MEC): Framework and Reference Architecture.


### Systems

* (SEC’17) CloudPath: A Multi-Tier Cloud Computing Framework.

* (CAN'16, DataBox, proposal) Personal data management with the databox: What’s inside the box?

* (HotEdge'18, proposal) ECO: Harmonizing edge and cloud with ml/dl orchestration.

* (HotEdge'18) Datafog: Towards a holistic data management platform for the iot age at the network edge.

* Cassandra: a decentralized structured storage system.


#### General Architecture

* (HotEdge'19) An edge-based framework for cooperation in internet of things applications.

#### ML and DL

* (HotEdge'18) MODI: Mobile deep inference made efficient by edge computing.

* (HotEdge'18) esgd: Communication efficient distributed deep learning on the edge.

* Exploring the use of synthetic gradients for distributed deep learning across cloud and edge resources. 

#### Videos

* (SEC'17) Parkmaster: an in-vehicle, edge-based video analytics service for detecting open parking spaces in urban environments.

* (SEC'18) Videoedge: Processing camera streams using hierarchical clusters.

* (SEC'18) Application-aware iot camera virtualization for video analytics edge computing.

* (SEC'18) Edgebox: Live edge video analytics for near real-time event detection.

#### Games

* Cloudfog: Leveraging fog to extend cloud gaming for thin-client mmog with high quality of service.

#### VR

* (SEC'17) Towards efficient edge cloud augmentation for virtual reality mmogs.

#### Stream Processing

* Distributed data stream processing and edge computing.



#### Collaboration

* Decaf: Iterative collaborative processing over the edge


### Parameter Server

* (OSDI'14 Parameter Server) Scaling distributed machine learning with the parameter server.

### Serverless computing

* The rise of serverless computing. 

* Serverless is more: From paas to present cloud computing.

* (OSDI'18) Pocket: Elastic ephemeral storage for serverless analytics.


### Database

* Edgedb: An efficient time-series database for edge computing.

* (TC'13 Google DB) Spanner: Google’s globally distributed database.


### Techniques

* Incremental deployment and migration of geo-distributed situation awareness applications in the fog.

* Latency mitigation strategies.

* (TMC'18) Uloof: A user level online offloading framework for mobile edge computing.

* (WF-IoT'13) Geelytics: Geo-distributed edge analytics for large scale iot systems based on dynamic topology

* (INFOCOMM'18) Service entity placement for social virtual reality applications in edge computing. 

#### Caching

* Precog: refetching for image recognition applications at the edge.

* Cachier: Edge-caching for recognition applications.

* (HotEdge'18) Towards a solution to the red wedding problem.

* (SIGMOD'18) Dpaxos: Managing data closer to users for low-latency and mobile applications

#### Load-balancing

* (SoCC'18) Fast and accurate load balancing for geo-distributed storage systems.

* (EDBT'18) Global-scale placement of transactional data stores.

#### Consistency

* (SOSP'13)  Consistency-based service level agreements for cloud storage.

* Consistency models for cloud-based online games: The storage system’s perspective.

* Cloudcraft: Cloud-based data management for mmorpgs.

* (HotEdge'18) Toward session consistency for the edge.

* (DEBS'18) Fogstore: A geo-distributed key-value store guaranteeing low latency for strongly consistent access. 

#### Synchronization

* (IoT'18)  An architecture for iot clock synchronization.

#### Heterogeneous

*  (IoTDI'19) Heteroedge: Taming the heterogeneity of edge computing system in social sensing.



### Analysis

* The case for vm-based cloudlets in mobile computing.

* A survey of multi-access edge computing in 5g and beyond: Fundamentals, technology integration, and state-of-the-art.

* Performance Analysis of Object Store Systems in a Fog and Edge Computing Infrastructure

* (SEC'19) Why cloud applications are not ready for the edge (yet).


### Benchmark

* (SoCC'10, Cloud YCSB) Benchmarking cloud serving systems with ycsb

* (SEC'17) Defog: Fog computing benchmarks.

* (SEC'18) Cavbench: A benchmark suite for connected and autonomous vehicles


### Industry

1. Azure IoT Edge. [Link](https://azure.microsoft.com/en-us/services/iot-edge/)

2. AWS IoT for the Edge. [Link](https://aws.amazon.com/iot/solutions/iot-edge/)

3. Google Cloud IoT. [Link](https://cloud.google.com/solutions/iot)



Strength
------

N/A


Weakness
------

N/A




<!-- refs -->

[system-architecture]: /images/2021-02-25-paper-reading-sharing-hotedge20/system-architecture.png "system-architecture"