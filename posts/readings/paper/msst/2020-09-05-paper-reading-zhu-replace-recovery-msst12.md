---
title: "Paper Reading: Zhu's replace recovery MSST'12"
date: 2020-09-05
permalink: /posts/2020/09/paper-reading-zhu-replace-recovery-msst12/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

On the speedup of single-disk failure recovery in XOR-coded storage systems: Theory and practice


Download
------
[MSST, 2012](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/msst12.pdf)


Summary
------

This paper introduces a replace recovery algorithm by a hill-climbing search for optimal recovery solution to shortern the recovery time. This paper aimed at arbitrary XOR-based ECs. Implementation and experiments are conducted atop of network storage system, and proved that such algorithm shows less recovery time than conventional reconvery.


Details
------

1. Targets
  * XOR-based ECs, including Cauchy RS code, RDP, EVENODD, X-Code; Storage nodes requires no computation capabilities
  * Single disk / node failure

2. BGs
  * XOR based ECs
  * Hybrid Recovery in XOR-based codes: uses a combination of row and diagonal parity sets of data and parity symbols for recovery. "The core idea of hybrid recovery is to find the set of maximum overlapping symbols to minimize the number of read symbols for recovery"
  * Enumerate ALL posibilities given generator matrix

3. Proposed simplified recovery model
  * Choose parity symbols to miminize data symbols for one stripe repair
  * Search efficiency, which means reducing the solution space

4. Replace Recovery Algirithm
  * Targets: minimize # of read symbols for recovery
  * Iteratively finding the set of parity symbols
  * Time complexity: *O(mw^3)*, polynomial to w
  * Can be generalized to heterogeneous disks

5. Implementation
  * Multi-threading for repair for stripes
  * Replace repair and conventional repair for RDP, EVENODD, X-CODE, STAR, CRS.

6. Experiments
  * Testbed built on top of NCFS
  * RDP: Time reduced: replace repair(20.9% - 23.9%), theoretical optimum: 25%, very closed.
  * In multi-server implementation, still sees the improvement of recovery speed.




Strength
------

* This paper introduces a simplified recovery model: finding the set of parity symbols to minimize # of read data symbols, thus speed up the recovery

* The introduced replace recovery algorithm reduces the search space of read symbols (data symbols), thus speed up the finding of solution compared with conventional enumeration search



Weakness
------

N/A


<!-- refs -->
