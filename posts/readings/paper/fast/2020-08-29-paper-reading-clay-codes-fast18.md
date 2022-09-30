---
title: "Paper Reading: Clay Codes FAST'18"
date: 2020-08-29
permalink: /posts/2020/08/paper-reading-clay-codes-fast18/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

Clay Codes: Moulding MDS Codes to Yield an MSR Code

Download
------
[FAST, 2018](https://www.usenix.org/system/files/conference/fast18/fast18-vajha.pdf)


Summary
------

This paper introduces Coupling-layer (Clay) Codes that mixed the MDS code and MRS code. It provides a simplified implementation of decode/repair that MRS can't achieve in real world. It provides the first implementation of an MSR code with low storage overhead, simutaneously optimality of repair bandwidth, sub-packetization level and disk I/O, uniform repair performance and support multiple node repairs .The authors also modify Ceph to support vector code.


Details
------


The contribution of this work includes:

1. Use uncoupled code to generate coupled layer that is an MSR code. It uses a pair of coordinates to represent a layer in Clay Code, then it pairs the vertices and the data as a cube like structure. The transformation of uncoupled layer to Clay code is simple matrix transformation (PFT and PRT).

2. A special decode algorithm for Clay Code allows 2 nodes failure.

3. Implementation in Ceph.

* Pairwise transform from uncoupled layer to Clay layers.

* Encode/Decode for p-OSD in Ceph.


Strength
------

Clay Code is the first implementation of MRS code in real world environment by transforming MDS, thus allowing the benefits introduced by MRS code.




Weakness
------

N/A


<!-- refs -->
