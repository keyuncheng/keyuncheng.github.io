---
title: "Paper Reading: PANDO NSDI'20"
date: 2021-06-17
permalink: /posts/2021/06/paper-reading-pando-nsdi20/
author_profile: false
excerpt: false
tags:
  - storage system
  - erasure coding
  - consensus
  - hot data

---

Near-Optimal Latency Versus Cost Tradeoffs in Geo-Distributed Storage

Download
------

[NSDI, 2020](https://www.usenix.org/system/files/nsdi20-paper-uluyol.pdf)


Summary
------

This paper shows that existing distributed storage systems with strong consistency guarantee are not optimal in latency-cost tradeoff. It also presents PANDO, a strong-consistent distributed storage system, which achieves lower latency by reducing the total number of round-trips of communication for r/w operations with Paxos consensus algorithm, and utilizes erasure-coding (RS) for reducing storage costs, rather than previous works which adopts replication. Under the assumption that r/w conflicts are rare, experiments show that PANDO approximately achieves the lower bound of r-latency / storage costs as well as r/w latency.

Details
------

* Key ideas:
  * Scenario: hot data, Google Docs, ShareLaTeX that have strong consistency requirements over wide-area network / geo-distributed storage, while supporting fault-tolerance and cost saving
  * Main issues in previous works:
    * STOA: EPaxos with replication, both latency and storage  lower bound are far from theoretical lower bound as proposed.
      * note: the computation bound are calculated by solving a set of interger programs
      * EPaxos only requires one round of communication between frontend and the nearestby majority of replicas
      * problems: storage overhead by replication, and given fixed cost, read latency significantly higher than the achievable lower bound
    * Why not Raft or leader based solution? Cost of leader migration and least requisition is too high.
    * Why EC? The computation cost (CPU) of erasure coding with ISA-L is negligible compared with communication cost and storage overhead, this is the core reason to use EC rather than replication. See Figure 14 for illustration.
  * Proposed idea: extend one of several one-round variants of Paxos to work on erasure-coded data, or take a classical two-round Paxos and address latency problem directly.
    * existing work: RS-Paxos
      * problem: r/w latency is twice of EPaxos's because of EC.
  * Solution:
    * Shrinking Phase 1 quorums: reuse read quorums
    * partially delegating write logic: offload Paxos's write logic to a deligate, with the heterogenity settings
    * Use smaller quorums except failure or conflict
    * Make use leader when write conflicts
  * Evaluation: compare with EPaxos, RS-Paxos and their extensions
    * Deployment: Geo-distributed over Azure
    * Metrics: Latency, storage overhead and GapVolume, a metric that evaluates how close each approach is to the lower bound, throughput
    * They also evaluate application workload via GitLab ops.


Strength
------

* Consensus + EC for hot storage, and proven to close to theoretical latency/storage overhead lower-bound


Weakness
------

* This paper didn't mention the recovery if some node fails, or node maintance.

* This paper mentions few about the metadata handling.

(Question: ) Besides RS, are other erasure codes compatible with the system? What about larger n, k?




<!-- refs -->


[system-architecture]: /images/2021-02-05-paper-reading-eccache-osdi16/system-architecture.jpg "system-architecture"