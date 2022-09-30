---
title: "Paper Reading: EdgeKV JPDC'20"
date: 2021-06-04
permalink: /posts/2021/06/paper-reading-edgekv-jpdc20/
author_profile: false
excerpt: false
tags:
  - edge
  - storage system
  - kv store
---

EdgeKV: Decentralized, scalable, and consistent storage for the edge


Download
------
[JPDC, 2020](https://www.sciencedirect.com/science/article/pii/S0743731520302884)


Summary
------

This paper presents a general purpose decentralized KV-store EdgeKV for the edge. EdgeKV provides (i) strong consistency (compared with eventual consistency), (ii) fault-tolerance by replication, (iii) two levels of data locality (local and global). This paper shows the modular design of prototype, including the functionality of each module, inter-module communication. Experiments shows the scalability of the system (number of clients and requests), and energy efficiency as future work.



Details
------

### System Architecture

![system-architecture][system-architecture]

local layer: a group consists of some edge nodes sharing the same states and kv-pairs (replication). Consistency guaranteed with: Raft. Local groups are independent.

global layer: A gateway node is responsible for forwarding the data from local group to other remote groups, in a word, routing. Such design makes the architecture flexible to heterogeneous settings. The internal mechanism under local group can be hidden.

Distributed Hash Table: hash(key) returns the group of the KV-pair to be stored.

Modules: Remote Procedure Call (RPC) interface, placement protocol, resource finder, replication manager, and storage.

Client -> closest Edge Node through RPC (KV and operation) -> where to execute in current edge node -> placement of KV -> destination local group executes the KV operation, and replicate the KV to storage 

The **replication manager** implements Raft internally for consistency using **etcd**.

### Implementation

Language: Go

Benchmark: YCSB

Emulator: Distem network emulator

Testbed: Grid'5000 (15000 cores and 800 compute nodes, 8 sites in France)

### Evaluation

YCSB workload "A", "update-heavy" with 50% read, 50% write, 10000 KV pairs, each client runs 100 YCSB workers

Setup: 3 local groups, each with 3 servers, 3 clients for each group, with each running 100 threads to simulate requests.

![evaluation-architecture][evaluation-architecture]

* use Distem to emulate the virtualized edge nodes and network topology
  * edge <-> client: 5ms
  * edge <-> edge: 2ms
  * client <-> cloud: 50ms

* Didn't use public clouds for the cloud setting (global layer)

* metrics: operation response time, throughput
  * comparison: local request vs global requests, EdgeKV and Cloud only

* parameters varied: percentage of global request, request distribution, number of clients within a local group



Strength
------

* Simple design



Weakness
------

* The global node is only used for routing - the resources are not utilized
  * caching, offload less important computation or archived data for storage to global node are possible

* Possible single point of failure at global layer

* Routing overhead is not discussed

* failover of the system (how to do journaling)

* In their implementation, they don't do caching neither at local groups nor global layer.

* Inter-group fault-tolerance can be introduced.

* data security is not discussed




<!-- refs -->

[system-architecture]: /images/2021-06-04-paper-reading-edgekv-jpdc20/system-architecture.jpg "system-architecture"
[evaluation-architecture]: /images/2021-06-04-paper-reading-edgekv-jpdc20/evaluation-architecture.jpg "system-architecture"