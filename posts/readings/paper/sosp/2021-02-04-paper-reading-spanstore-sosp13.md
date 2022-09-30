---
title: "Paper Reading: SPANStore"
date: 2021-02-04
permalink: /posts/2021/02/paper-reading-spanstore-sosp13/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - consistency
---

SPANStore: Cost-Effective Geo-Replicated Storage Spanning Multiple Cloud Services


Download
------
[SOSP, 2013](https://web.eecs.umich.edu/~harshavm/papers/sosp13.pdf)


Summary
------

This paper present SPANStore, a KV store that exports a unified view of storage services in geographically distributed data centers. The three principles in SPANStores includes: geo-distributed storage clouds, trade-off geo-distributed replication for latency goals and data propagation costs for fault tolerance, implementation to minimize the usage of computation resources.


Details
------

### Drawbacks of previous works

1. almost every storage service offers an isolated pool of storage in each of its data centers, leaving replication across data centers to applications.

2. replication of data to all datacenters is costly and may be inefficient. 

### Novelty of the paper

1. SPANStore spans data centers across multiple cloud providers due to the associated performance and cost benefits.

2. SPANStore determines where to replicate every object and how to perform this replication.
  * workload, latency

3. Implementation of locking for consistency requires minimized computation resources.

### System Architecture

![system-architecture][system-architecture]

* Data centers

* Local (on-prem) DS for SPANStore VMs for in-memory metadata services


### Replication policies

Placement Manager(PMan)
  * Inputs: latency (application, data) and prices
  * Propagates metadata/data to clouds

Consistency
  * Configurable: strong/eventual
  * Same as DepSky


### Consistency

* asymmetric quotum sets

### Locking

* Two Phase locking
  * Acquiring version from Storage Services, and add lock
  * Relay data to a set of additional VMs and write to Storage Services at the back (for eventual consistency)
  * ACK

### Workload

* For each epoch, the replication policy updates


Strength
------

* Flexible replication policies with minimization of costs and latency, which is the core and goal of this work.

Weakness
------

* Possible SPOF of PMan


<!-- refs -->


[system-architecture]: /images/2021-02-04-paper-reading-spanstore-sosp13/system-architecture.jpg "system-architecture"