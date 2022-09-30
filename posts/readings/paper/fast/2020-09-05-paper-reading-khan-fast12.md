---
title: "Paper Reading: Khan FAST'12"
date: 2020-09-05
permalink: /posts/2020/09/paper-reading-khan-fast12/

author_profile: false
excerpt: false
tags:
  - erasure coding
---

Rethinking Erasure Codes for Cloud File Systems: Minimizing I/O for Recovery and Degraded Reads


Download
------
[FAST, 2012](https://www.cs.jhu.edu/~okhan/fast12.pdf)


Summary
------

This paper introduces an algorithm to find the optimal number of codeword symbols for recovery, and schedules the repair that using the minimum amount of data. Rotated RS is introduced which speeds up the degraded reads.


Details
------

1. Optimal Recovery of XOR-based Erasure codes
  * For m = 2, the optimal recovery will be XOR of data disks + P drive
  * Reading from P drive in practice requires more I/O than is necessary. There are savings can be exploited when multiple symbols are to repair in the same stripe

2. Algorithm to determine the minimum number of symbols for recovery.
  * Computational very expensive, but running time maybe low in practice
  * Goal: select one equation in decoding equations to minimize the symbols to read
  * Convert the equations to **a weighted graph**; node: represent each decoding equation in set form as *nr-element* str string; edge: bitwise OR between a node and the edge
  * **Program Dijkstra's algorithm** to determine shortest graph and prune the graph

3. Rotated RS
  * MDS code
  * Optimized for degraded reads
  * The computation of parity P differs from RS, as (2^j)^i for the first parity *P*.
  * From the illustration of the example, to repair a single data (block) failure, which is the degraded read, the penalty is 5 symbols for RS, but 2 symbols for Rotated RS.

4. Analysis
  * Under a certain (n, k), the number of symbols to reconstruct a disk for various XOR-based EC
  * Density of Generator matrices for various XOR-based EC
  * Penalty analysis of degraded reads with various data symbols to read

5. Evaluation
  * Comparison of I/O between Generalized RDP and other codes
  * Degraded reads: Rotated RS outperforms other codes, since other codes needs to read completely k nodes




Strength
------

1. Provides a solution to determine the minimum # of symbols for recovery by tree graph construction and finding shortest path

2. Rotated RS for faster degraded read.


Weakness
------

MDS code only, extension to non-MDS (mentioned at the end of paper)


<!-- refs -->
