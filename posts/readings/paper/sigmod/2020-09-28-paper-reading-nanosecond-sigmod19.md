---
title: "Paper Reading: Nanosecond Indexing SIGMOD'19"
date: 2020-09-28
permalink: /posts/2020/09/paper-reading-nanosecond-sigmod19/
author_profile: false
excerpt: false
tags:
  - graph processing
  - Indexing

---

Nanosecond Indexing of Graph Data With Hash Maps and VLists


Download
------

[SIGMOD, 2019](https://dl.acm.org/doi/10.1145/3299869.3314044)


Summary
------

This paper introduces a new indexing structure on top of LinkedIn for in-memory social graph databases. The system's novelty is the processing speed for queries, low r/w latency, consistency and simplicity. The storage layout including the indexing structure, VList, Hashmap are introduced. Evaluation shows the system significantly increases read performance with nanoseconds for subgraph lookup and materialization, while with acceptable write performance. 

Details
------

1. Problems
  * Processing second degree network is difficult. Random multi-hop query workloads stress
the indexing system.
  * Live updates make denormalization or maintenance of materialized views difficult, especially for multi-hops.
  * Previous system requires reader and writer to share a process, so isolation failure is occurred.

2. System
  * Graph: RDF
  * Nodes and edges are stored in an immutable log in shared memory.
  * Index data: HashMap stores offset to the filtered log as VList.
  * VList doesn't overwrite old data. Write will dynamically update the VList size by appending chunks.
  * 2-level indexing: intermediate S to P store is introduced (if S is large)
  * Consistency: The order of read and write and the relation with VList Size.

3. Evaluation and Analysis
  * Lookup: Small data: tens of nanoseconds, stable; Large: increases as HashMap size grows, because of worse use of cache.
  * the time to materialize is mostly unaffected by the data size. Large data sets the materialize time is relatively constant.
  * Pipelining helps little
  * Write speed acceptable


Strength
------

1. Very fast online read because of r/w isolation

2. Simple data structure: VList and HashMap for indexing and materialization


Weakness
------

1. Write performance not increases. (as mentioned by author)

2. Can the idea of r/w consistensy and/or indexing be applied to property graph?

