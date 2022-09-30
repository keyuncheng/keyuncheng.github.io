---
title: "Paper Reading: Gemini OSDI'16"
date: 2020-09-28
permalink: /posts/2020/09/paper-reading-gemini-osdi16/
author_profile: false
excerpt: false
tags:
  - graph processing

---

Gemini: A Computation-Centric Distributed Graph Processing System


Download
------

[OSDI, 2016](https://www.usenix.org/system/files/conference/osdi16/osdi16-zhu.pdf)


Summary
------

This paper introduces Gemini, a distributed graph processing system that builds scalability (distributed) on top of efficiency (shared-memory). First, the paper analyzes existing shared-memory and distributed graph systems and find the bottleneck is still computation; and argue that the design should pay close attention to the (local) computation overhead. Experiments over 8 node cluster show that Gemini scales similarly but runs much faster compared with existing graph processing systems.


Details
------

1. Dual Update Propagation model
  * Sparse mode: master to mirror -> update neighbors
  * Dense mode: neighbors -> mirror (computation) -> master (lowers the computation overhead on master node)

2. Partitioning: Chunk based. Partition the vertex set to continuous chunks preserves locality.

3. Edges: Using CSR/CSC format for incoming/outcoming edges. Especially, for sparse mode, add an existance bitmap; for dense mode, doubly compressed sparse column.
  * Goal: reduce memory access in processing edges.

4. Locality aware chunking.
  * Powerlaw distribution, load balancing exhibits poor load balance.

5. HPC optimizations

6. Experiments


Strength
------

1. Preserving scalability, while greately reducing the computation time.
  * locality preserved via chunk based partitioning


Weakness
------

1. How about the effect of locality preserved chunking? It's not analyzed in detail in the paper.

