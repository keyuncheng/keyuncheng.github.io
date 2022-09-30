---
title: "Paper Reading: STAIR Codes FAST'14"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-staircodes-fast14/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

STAIR Codes: A General Family of Erasure Codes for Tolerating Device
and Sector Failures in Practical Storage Systems


Download
------
[FAST, 2014](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/fast14stair.pdf)


Summary
------


Sector Disk codes considers the coverage of sector failures, thus it's available with limited configurations. This paper introduces a general erasure code called STAIR codes which tolerates both device and sector failures. By the special upstair/downstair encoding, the STAIR codes provides better computation efficiency than traditional SD codes.


Details
------

* Traditional EC and RAID overkill parity divices to tolerate partial device failures.

* SD code doesnot allow some mixed failures 

STAIR code assumption: in each devide, several sectors failure are allowed. Then the construction of STAIR codes can be based on existing erasure codes.

* use a sector failure vector *e* to define a pattern that how sector failure occurs. e = (e0, e1, ..., em - 1).


1. Two phase encoding

* Phase 1: use input data to generate "row" parity symbol. It's an intermediate parity symbol, since it's only encoded from the same row of data.

* Phase 2: use intermediate parity symbol to calculate global parity symbol. Phase 1 intermediate symbols will be discarded.

* Note that Phase 1 and 2 can be systematic MDS codes.

Upstair decoding: Augmented virtual stripes from existing stripes.


2. Upstair Encoding. Set outside global parity symbols to 0, and use upstair decoding method. The parities are built from bottom to top.

3. Downstair Encoding. Top to bottom, right to left. Start with C_row and generate m + m' symbols. Then encode via C_col to get new intermediate symbols. Continue until all symbols are generated.

* Encoding complexity analysis. For given configuration, pre-compute the Mult-XORs, then choose the encoding method with the fewest computation costs.




Strength
------

1. Encoding speed of STAIR in experiment is much faster than disk write. Reason: STAIR codes reuses encoded parity information in two-steps encoding by upstair/downstair.

2. Decoding speed is faster than SD codes by 102.99% in avg.




Weakness
------

N/A


<!-- refs -->
