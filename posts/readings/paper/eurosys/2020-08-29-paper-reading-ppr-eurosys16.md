---
title: "Paper Reading: PPR Eurosys'16"
date: 2020-08-29
permalink: /posts/2020/08/paper-reading-ppr-eurosys16/
author_profile: false
excerpt: false
tags:
  - repair
  - erasure coding
---

Partial-Parallel-Repair (PPR): A Distributed Technique for Repairing Erasure Coded Storage


Download
------
[EuroSys, 2016](https://engineering.purdue.edu/dcsl/publications/papers/2016/final_erasurecodedrepair_eurosys16_cameraready.pdf)


Summary
------

PPR (partial parallel repair) divides the reconstruction to sub-operations and schedule to nodes. Then a protocol is used to combines the partial results. This approach reduces the network pressure, experiments shows that this approach significantly reduces repair/degraded read time. LRC and Rotated RS are overlayed by PPR in this paper.



Details
------

1. PPR divides reconstruction into several partial parallel repair operations that are performed simultaneously at multiple servers.

2. PPR can be overlaied on top of almost all ECs.

3. Main PPR algorithm: 

* PPR takes a few logical timesteps to complete the reconstruction operation. In each time slop, a set of servers do partial reconstruction. It overlays a tree-like reconstruction structure.

* PPR distributes the reconstruction to multiple servers in parallel.

* In-memory chunk caching. No disk hitting is required if it's cached in memory for some chunks.

4. PPR Protocol to achieve combination of partial results. (Repair Manager - RM). RM distributes the partial decoding coefficients with a repair plan to only k/2 Chunk Servers. Finally, the repair sites aggregates the results by XORing from all k/2 servers. The destination server feedback to RM that it's successful.

* I/O pipeline for k/2 servers.


Strength
------

1. The larger chunk sizes, the better performance main PPR gains.

2. Performance improvement over degraded reads.

3. Computation efficient by parallism.


Weakness
------


1. The extension of the Repair Manager. It's currently centralized, and single instanced. It maybe the bottleneck for large scale DSS.