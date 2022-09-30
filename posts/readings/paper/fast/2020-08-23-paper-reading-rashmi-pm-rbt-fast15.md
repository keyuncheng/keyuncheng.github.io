---
title: "Paper Reading: Rashmi PM-RBT FAST'14"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-rashmi-pm-rbt-fast15/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

Having Your Cake and Eating It Too: Jointly Optimal Erasure Codes for I/O, Storage, and Network-bandwidth


Download
------
[FAST, 2015](https://www.usenix.org/system/files/conference/fast15/fast15-paper-rashmi.pdf)


Summary
------

Existing practical MSR codes fails to solve the high I/O overhead during repair. This paper introduces product-matrix-MSR codes that significantly reduces repair I/O, typically 5x, while retaining optimality with respect to storage/reliability/network bandwidth.

PM-RBT: Product-Matrix-Repair-By-Transfer


Details
------

1. PM-MSR codes: a class of linear codes. PM-vanilla codes are not optimal with respect to the amount of data read during reconstruction. Reconstruction vector are mostly non-zero, not sparse, thus introduces high overhead.

2. RBT-helper is introduced. RBT means if a node is used to transfer but without any computation. The methodology behind is: a lower bound on the network transfers is also a lower
bound on the amount of data read. Separates RBT blocks and others. Use the others for the computation.

3. An algorithm is presented for RBT helpers's assignment. It's doing:

* for each block, compute the number of helpers

* selection of the helpers among nodes

* connects the nodes in the digraph by the relationship calculated from previous selection.




Strength
------

Compared with RS,

1. Both PM-vanilla nad PM-RBT, network bandwidth significantly goes lower.

2. PM-RBT Significantly lowers I/O consumed  and the data read during reconstruction of chunks.

3. Similar decoding speed for PM-vanilla nad PM-RBT.

4. **Analysis of the RBT helper selection algorithm**




Weakness
------

N/A


<!-- refs -->
