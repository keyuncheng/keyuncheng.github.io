---
title: "Paper Reading: Acceleration of EC FAST'19"
date: 2020-08-29
permalink: /posts/2020/08/paper-reading-ec-acceleration-fast19/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques


Download
------
[FAST, 2019](https://www.usenix.org/system/files/fast19-zhou.pdf)


Summary
------

This paper integrates various optimization for ECs as a computation train. The procedure is: use a bitmatrix to produce the computation schedule (XOR level vectorization, XOR reduction and caching). Results also suggest that vectorizing XOR is a better choice than directly vectorizing finite field operations.


Details
------

1. Encoding by bitmatrix. Finite field operations in GF(2^w) can be implemented using bit vectors and matrices.

* Normalization of parity coding matrix to make it more suitable for computation.

* Reusing parity computation to reduce overall computation. Introduced by Plank

* Maximum caldinality unweighted/weighted matching algorithm

* Caching optimization

* Vectorized XOR

2. Performance of individual techniques are compared. It shows that V-XOR appears to be able to provide the most significant performance improvement, with avg 130.04%. But it's completely different computation chain at all. The remaining techs have improvements ranging from 4.81% to 36.63% individually.

3. Different 8 combinations of stratigies under optimized BM are compared. Total number of XORs for each combination of acceleration methods with different *(n, k, w)* are compared.

* A cost function regards to total number of XORs, total operations, weighted version of the two numbers are calculated.

4. The overall procedure:

* Perform a suitable optimization algorithm
	* Bitmatrix normalization
	* use selective matching with cache-friendly order to get the computation schedule, then do vectorized XORs 


Strength
------

1. This paper compares the proposed approach with various ECs, and Vectorized XORs
	* Encoding: for some (n, k, m), the proposed method shows slightly higher improvement.
	* Decoding: The proposed method provides (also slightly) better decoding throughput compared with vectorized XORs and GFs

2. Individual methods are considered more important compared with the combined optimal one.



Weakness
------

N/A


<!-- refs -->
