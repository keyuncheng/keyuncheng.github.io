---
title: "Docs Reading: Plank EC Tutorial FAST'13"
date: 2020-08-15
permalink: /posts/2020/08/docs-reading-plank-tutorial-fast13/
author_profile: false
excerpt: false
tags:
  - docs reading
  - storage
  - erasure coding
---

Tutorial: Erasure Coding for Storage Systems


Download
------
[FAST, 2013](http://web.eecs.utk.edu/~jplank/plank/papers/FAST-2013-Tutorial.html)


Summary
------

These slides introduces the basics of ECs, including the concepts, algorithms of various ECs.




Details
------

Plank's

1. Concepts
	* systematic ECs: in (n, k), k nodes stores data and m = n - k stores coding info, and thus called coding/parity disks.
	* Non-systematic EC: n nodes only stores coding info.
	* MDS: m disks fault tolerance.
	* Horizontal code: Storage nodes and coding/parity nodes.
	* Vertical code: Each node stores data/encoding
	* Stripe: The min collection of bits that encode and decode together. (n, m, k), r, w. A system stripe groups theoretical stripes for performance.
		* reason: w is often small, grouping theoretical stripes increases performance

2. Generator matrices
	* calculation of coding matrix via GM and data matrix
		* non-systematric EC: I is not included in GM
	* An example of RAID-6. P = dn XOR dn-1 ...XOR d0, Q = COEFFn * dn XOR COEFFn-1 * dn-1 ... COEFF0 * d0
	* RDP RAID-6
	* Decoding through survivors: data = B^-1 * suvivors

3. RS code
	* MDS code
	* n <= 2^w
	* Create two sets X, Y, calculate matrix coefficients through a_ij = 1 / (x_i + y_j). Cauchy generator matrix was used in the example, which has the property that any k * k submatrix is invertible, thus allow decoding.

4. Cauchy RS code (use only XOR)
	* representation of a number of GF(2^w) in bit vector and w * w matrix. matrix representation allows matrix * vector = vector and matrix * matrix = matrix

5. Linux RAID-6, enables fast encoding.

6. EVENODD, w = 1, r = k - 1, k must be a prime. No matrix multiplications, simply diagonal XORs

7. RDP, k = r, k+1 must be a prime. Get rid of S. It achieves the theroretical min of XOR operations.

8. (Not understand yet) X-code. Veritical code, n = r, n must be prime.


Cheng Huang's

Cheng introduced additional codes, including pyramic codes, LRC for Windows Azure, SD codes, regenerating codes like SRC, etc..





Strength
------


N/A



Weakness
------


N/A


<!-- refs -->