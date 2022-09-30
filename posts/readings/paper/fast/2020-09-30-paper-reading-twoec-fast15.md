---
title: "Paper Reading: A Tale of Two Erasure Codes FAST'12"
date: 2020-09-30
permalink: /posts/2020/09/paper-reading-twoec-fast15/

author_profile: false
excerpt: false
tags:
  - erasure coding
  - Locally repairable codes
---

A Tale of Two Erasure Codes in HDFS


Download
------
[FAST, 2015](https://www.usenix.org/system/files/conference/fast15/fast15-paper-xia.pdf)


Summary
------
This paper presents an erasure-coded storage system that uses two different erasure
codes and dynamically adapts to workload changes, one for fast repair and another for reduce storage overhead. The system applies to Product Code and LRC. Experiments shows improvements of recovery while maintaining low storage overhead.


Details
------

1. System name: Hadoop Adaptively-Coded Distributed File System (HACFS), an extension to HDFS-RAID module, it outperformns solo use of RS or LRC.

2. System Design:
  * System states and transition
    * Global state (system storage bound).
    * read counter for data
    when the above two states changes, the adaptive coding scheme applies: (fast) <=> (compact). Not bounded or read cold: compact; otherwise: fast
  * Adaptive Coding
    * encode/decode
    * Upcode: transform data from fast code to compact code. (parity) => (parity)
    * Downcode: transform data from compact code back to fast code (for fast read). (data, parity) => (parity)
  * Erasure codes applied
    * Product code: e.g. PC_fast = PC(2*5), single block failure can be recovered requiring only two blocks from the same column. PC_compact = PC(6*5). PC_fast <=> PC_compact is introduced
    * LRC: LRC_fast = LRC(12, 6, 2); LRC_compact = LRC(12, 2, 2). 6 to 2: XOR the parities; 2 to 6: use 4 data block + 2 local parities to reconstruct 6.

3. Evaluation

Testbed: 11 nodes with (24 core, 96GB Mem, 1Gbps network)
* comparing with solo use of RS(6,3), RS(10, 4), LRC(12, 2, 2)

* Reconstruction time for disk/Node failure: 14-43% for Product Code and up to 32% for LRC.
* Storage overhead: LRC is 4 - 10% better than HACFS.
* Degrade read: around 20% to 50% improvements over existing single ec systems.
* Encoding cost: 3-28% lower than the single node system.

Strength
------

1. Adaptive scheme for hot/cold data while considering the total storage volume.


Weakness
------

1. Need to design fast and compact scheme for each input erasure codes, if the conversion time is huge, then it should be out-performed by single mode ec.


<!-- refs -->
