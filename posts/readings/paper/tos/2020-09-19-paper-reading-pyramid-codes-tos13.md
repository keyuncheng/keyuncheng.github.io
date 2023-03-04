---
title: "Paper Reading: Pyramid Codes TOS'13"
date: 2020-09-19
permalink: /posts/2020/09/paper-reading-pyramid-codes-tos13/
author_profile: false
excerpt: false
tags:
  - erasure coding
  - LRC
---

Pyramid Codes: Flexible Schemes to Trade Space


Download
------
[TOS, 2013](http://personal.cityu.edu.hk/mchen88/papers/pyramid.ToS.13.pdf)


Summary
------

This paper introduces Pyramid Codes (Basic and Generalized), using storage overhead to tradeoff repair cost, with 50% reduction in read cost with 11% additional storage overhead. This paper also introduces MR (Maximally Recoverable) property, and show that Generalized Pyramid codes satisfy MR.

Details
------

Other non-MDS codes: LDPC, Weaver, flat XOR, simple regenerating codes.

(page 5) the definition of ERC scheme (erasure-resilient coding), systematic, and MDS.

Basic PC, named BPC code construciton. This is very similar to LRC, except that the global parity chunks are computed the same way as MDS (RS) code.

Generalized PC. It requires expanding the generator matrix to satisfy MR property. The paper introduces the algorithm for constructing the GPC (the generator matrix). The critical step is to find the *g_m*, such that it's not orthogonal to any row vector (the null space is the row vector). For all submatrix of generator matrix, to have MR property, any row * *g_m* != 0

Comparison between BPC and GPC: GPC provides higher fault tolerance than the BPC, while keeping (n, k, r) the same.

On-demand block reconstruction algorithm, an example shows the reconstruction step in detail, and shows the reconstruction cost as well.


Strength
------

* Tradeoff storage spaces for repair cost and efficiency.


Weakness
------

* To recover the "global redundant blocks", full k node recovery is required. This part is not illustrated in detail in this paper.



<!-- refs -->