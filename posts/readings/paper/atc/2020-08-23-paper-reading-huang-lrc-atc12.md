---
title: "Paper Reading: Huang LRC ATC'12"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-huang-lrc-atc12/
author_profile: false
excerpt: false
tags:
  - Erasure Coding
  - Windows Azure
---


Erasure Coding in Windows Azure Storage


Download
------
[ATC, 2012](https://www.cs.princeton.edu/courses/archive/spring13/cos598C/atc12-final181.pdf)


Summary
------

This paper introduces well known Local Reconstruction Codes (LRC). "LRC reduces the number of erasure coding fragments that need to be read when reconstructing data fragments that are offline, while still keeping the storage overhead low." This paper also introduces LRC in WAS (Windows Azure Storage).



Details
------

### Background

1. Previously Azure uses 3 replica, (n, k) = (12, 4); RS code has to collect 12 copies, performance bounded by single node. 3 replica is commonly accepted industry standard.

### Approach

1. LRC: *k* data fragments, *l* groups, *r* global parities. *n* total number of fragments, *n = k + l + r*. Storage overhead: *1 + (l + r) / k*

2. It's done by reading less fragments. It's more efficient if reconstructing a data fragment **only by reading the fragments in a group, as well as the global parity**. But it definitely introduces additional more parity fragments.

3. LRC is not MDS code, but it targets at low reconstruction cost. Some of the 4 failure patterns are not recoverable, like the example (6,2,2). If in 4 fragments, 3 data fragments and one parity are all failed, the group is not recoverable, since the remaining parity can't be used to reconstruct the remaining 3 at all.

4. LRC of (6,2,2) tolerates arbitrary 3 fragments failure, and it allows local group repair with single node failure. This is called Maximally Recoverable Property, it tolerates (r + 1) failures.

5. (To read in more detail later) Reliability Analysis. 

6. In large I/Os, the latency is mostly bottlenecked by network and disk bandwidth. Thus, reducing the read fragments will significantly improves the reconstruction performance.

7. WAS chooses LRC (12, 2, 2) and compared with RS (12, 4).




Strength
------

1. LRC saves significant I/Os and bandwidth during reconstruction when compared to RS.


Weakness
------

1. Non MDS in theory. Additional storage overhead is introduced for the same fault tolerance.

2. LRC is optimized for reconstructing data fragments but not parity. In terms of parity reconstruction, Weaver codes, HoVer codes and Stepped Combination codes can be more efficient. (It's desiable to tradeoff the parity reconstruction)


<!-- refs -->