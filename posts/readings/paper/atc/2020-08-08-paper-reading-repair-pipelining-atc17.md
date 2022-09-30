---
title: "Paper Reading: Repair Pipelining ATC'17"
date: 2020-08-08
permalink: /posts/2020/08/paper-reading-repair-pipelining-atc17/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - erasure coding
  - repair
---

Repair Pipelining for Erasure-Coded Storage


Download
------
[ATC, 2017](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/atc17.pdf)


Summary
------

This paper presents a pipeling repair approach for EC. It's by pipelining the repair of failed data in small-sized units across storage nodes. Repair time reduced approximately to normal read time to the same amount of data in similar environment.


Details
------

- Recovery types: degraded reads and full-node recovery. Hetereogeneous environments are also addressed.
- Protype ECPipe deployed on HDFS and benchmarked on AWS
- Architecture: Requestor and Helper. Coordinator manages the repair operations.

Comparison: Conventional RS (log(k)). and PPR (log2(k+1)). RS: helpers not utilized. PPR: still not balanced between requestors and helpers.

Goal: Further minimize repair time for transient failures. Designed for single block failure per stripe. For multiple blocks failure in a stripe, go back to the conventional one.

Approach: breaks a block's repair to a set of slices repair, parallize the slices repair. Overhead introduced by issuing many slices per block are discussed. The overall pipeline performance is bounded by the worse link/helper.


Full Node recovery: greedy approach for the selection of helpers, that is selecting the least selected helpers to do recovery.

Heterogeneity: optimal path selection for repair paths. Algorithm introduced: Weighted path selection



Strength
------

- O(N) to O(Log(N)) improvement over repair operations. Single block repair reaches almost network bounded.



Weakness
------

- Extension to general storage systems with EC


<!-- refs -->
