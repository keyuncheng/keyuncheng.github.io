---
title: "Paper Reading: Plank USENIX Login'13"
date: 2020-08-15
permalink: /posts/2020/08/paper-reading-plank-usenixlogin13/
author_profile: false
excerpt: false
tags:
  - Storage
  - Erasure Coding
  - Theory
---

Erasure Codes for Storage Systems: A Brief Primer


Download
------
[USENIX Login, 2013](http://web.eecs.utk.edu/~jplank/plank/papers/Login-2013.pdf)


Summary
------

The core technology for disk failure protection is erasure coding. Plank presents a primer on EC and the application to storage systems. Recent research on EC are presented. This paper describes various types of disk failures and ECs. The goal of ECs is to tolerate broader classes of storage failures with less extra storage. 


Details
------

1. An overview of EC.
	* Concepts: Data disk, coding disk, (n, k), MDS code, strips, stripes.
	* Coding words are linear combinations of data words.
	* Encoding: multiplication and addition of data words. Decoding: solving a set of liniear equations with Gaussian elimination/matrix inversion I^-1
	* Operations: Galois Field GF(2^w). Addition = XOR, when number of bits w = 1, multiplication = AND. Larger value of w allows for richer ECs, but more complex operations.
	* The ith words on disks are encoded and decoded together independently.
	* Balanced stripes and ad hoc stripes.

2. ECs
	* RAID-1, replication
	* RAID-4 and RAID-5. In RAID-4, the identity of each disk is fixed, while in RAID-5 identities are rotated.
	* RAID-6. Tolerates two disks failure. The calculation of P disk (the same as RAID-4/5) and Q disk (addition, multiplication) are introduced.
	* RS, a general code, easy to define for n, k. More details of RS are introduced in a lot of articles, papers. The core is to construct the distribution matrix., the n * m part.
	* Array Codes, which requires XOR operations only.

3. Computation
	* Vector instructions in modern CPU has lower the burden of GF arithmatic.

4. Recent works
	* Recovery disk I/O reduction. RDP codes saves 25% overhead from a simple EC.
	* Regeneration codes. Target to minimize I/O for regenration the new contents for the failed nodes.
	* Non MDS codes. It represents non-optimal storage saving but commonly with performance improvements. Examples are like flat-XOR, LRC code, Sector Disk(SD) codes.



Strength
------


N/A


Weakness
------


N/A


<!-- refs -->