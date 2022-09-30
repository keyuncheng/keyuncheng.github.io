---
title: "Paper Reading: ECWide FAST'12"
date: 2021-07-18
permalink: /posts/2021/07/2021-07-18-paper-reading-ecwide/

author_profile: false
excerpt: false
tags:
  - erasure coding
  - wide stripe
  - locality
---

Exploiting Combined Locality for Wide-Stripe Erasure Coding in Distributed Storage


Download
------
[FAST, 2021](https://www.usenix.org/system/files/fast21-hu.pdf)


Summary
------

This paper proposed Combined Locality and the system ECWide for hierarchical distributed storage systems that adopts wide-stripe erasure coding. Given large n, k in a wide-stripe settings, the repair penality is much higher as repairing any single chunk or node failure requires assistance from at least k nodes. ECWide combined two types of locality based schemes, parity locality (LRC) and topological locality (hierarchical DSS) to minimize the **repair bandwidth**. This paper also proposes multi-node encoding within a rack to parallelize encoding, and inner-rack update scheme to accelerate update speed. Experiments over Amazon EC2 based on comparisons between LRC, Topological locality and Combined locality in a simulated hierarchical DSS has shown that, Combined locality outperforms both locality based schemes.  


Details
------

* Background
  * Wide-stripe: extreme low storage redundancy, but high repair penality
  * Hierarchical DSS: rack-based
  * introduce locality based schemes
    * parity locality: LRC, 4 schemes are considered: Azure-LRC, Xorbas,, Optimal LRC Azure-LRC+1
  * Objective: reduce repair bandwidth
  
* Combined Locality: include parity chunks / nodes in hierarchical data centers, and try to optimize the repair bandwidth given fixed number of tolerated failure nodes and number of racks

* It analyzes the redundancy trade-off between redundancy and cross-rack repair bandwidth (in number of chunks)

* It adopts MTTDL for the reliability analysis. It analyzes a set of configurations of LRC, RS, CL by varying failure rates, and network bandwidth among storage nodes.

* It views full-node repair as multiple single-chunk repair, and thus try to parallelize the repair operations

* It proposes in-rack multi-node encoding (parallelization), and inner-rack parity update to improve update efficiency.

* The prototype includes ECWide-C (DSS) and ECWide-H (Memcached) standing for cold and hot storage.

* Experiments on AWS EC2 with a simulated hierarchical datacenters (node as gateway and bandwidth control) 



Strength
------

* first work to systematically addresses the wide-stripe repair problem by combined locality




Weakness
------

* The global chunks repair problem is ignored in this work. It only considers the repair for data chunks and local parities. Penality of repairing global parities is high.

* How exactly wide-stripe can be used for hot storage systems (KV-store and others) remains unexplored.



<!-- refs -->
