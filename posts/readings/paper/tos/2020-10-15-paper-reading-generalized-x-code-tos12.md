---
title: "Paper Reading: Generalized X-Code TOS'12"
date: 2020-10-15
permalink: /posts/2020/10/paper-reading-generalized-x-code-tos12/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

Generalized X-Code: An Efﬁcient RAID-6 Code for Arbitrary Size
of Disk Array


Download
------
[TOS, 2012](https://dl.acm.org/doi/10.1145/2339118.2339121)


Summary
------

In generalized X-code, redundant elements are moved along their cal-
culation diagonals in X-code onto two speciﬁc disks and change two data elements
into redundant elements. It adapts to arbitrary size of the disk array as well. 



Details
------

1. Horizontal code: redundant elements and data elements are stored on different disks within a stripe.

Veritical code: redundant elements and data elements can be stored on any disk within a stripe.

2. Motivation: 1. Horizontal code cannot attain a theoretical optimal
updating complexity of two; 2. the size of disk array in vertical code must be a prime number; 3. for vertical code, adding new disks requires changing all the diagonals, which means all the redundant elements need to be recalculated.


3. Generalized X-code
* Tradition horizontal code: redundant elements are allocated to two columns
* X-code: redundant elements are allocated to the last two rows
* Generalized X-code: redundant elements from the last two rows are moved to the last two columns

Encoding: p0: XOR all data, p1: special element introduced in each data element

Decoding: same as original. If the (p-1/2)th disk fails, special element should be recovered during decoding.


4. Evaluation:
* Generalized X-code achieves theoreticaly optimal encoding complexity for arbitrary
size of data disk array, and optimal update complexity for single data element.

* Decoding complexity: RDP exhibits the best, Generalized X-code does better than EVENODD.


Strength
------

1. As a vertical code, Generalized X-code doesnot require the size of the disk array as prime number. The number of disk should be prime though.

2. It make sure that it tolerates any two 2 disks' failure.




Weakness
------

1. It's not MDS code





<!-- refs -->