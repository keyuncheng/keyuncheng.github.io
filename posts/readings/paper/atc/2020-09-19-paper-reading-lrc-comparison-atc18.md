---
title: "Paper Reading: LRC Comparison ATC'18"
date: 2020-09-19
permalink: /posts/2020/09/paper-reading-lrc-comparison-atc18/
author_profile: false
excerpt: false
tags:
  - Erasure Coding
  - Locally repairable codes
  - Comparison
---


On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes

Download
------
[ATC, 2018](https://www.usenix.org/system/files/conference/atc18/atc18-kolosov.pdf)


Summary
------

This paper conducts a theoretical comparison between different existing LRC approaches, including Azure LRC, Xorbas, Optimal LRC, in light of two metrics: ARC (average repair cost), NRC (normalized repair cost) and average degreaded read cost. The results shows the tradeoff between objectives of these codes and how the codes optimize their objectives. This paper also analyse these codes in Ceph deployed in AWS EC2. The experiments shows that the prediction of recovery (number of blocks to be repaired) is accurate, and the prediction provides a good estimate of the time required for reconstruction.



Details
------

### Background

1. LRC codes
  * data-LRCs. Azure LRC and Pyramid codes are data-LRCs. Only the data block and local parities can be repaired locally. Global parities should be repaired with k blocks.
  * full-LRCs. Xorbas, Optimal-LRC are full-LRCs. The glocal parities can be repaired locally as well. Optimal-LRC requires n mod (r + 1) != 1. The storage overhead is slightly higher, and the code minimum distance is higher than data-LRCs. Gophan has provided an upper bound for the full-LRC code minimum distance, and shows that Optimal-LRC achieves this upper bound.

2. Problem
  * comparison between different LRC codes are not straightforward, regarding r and l.
  * r can't serve as a metric to be compared

3. Metrics
  * ARC. ARC does not take into account the higher overhead of some of these codes, which implies that more blocks will have to be repaired in the event of a node failure.
  * NRC. NRC = ARC * n / k.
  * Average degraded read cost, as repairing data blocks only.

4. Codes being compared
  * Xorbas (only in theoretical analysis, not in experiments)
  * Azure-LRC
  * Azure-LRC+1. Adding one local parity to the global parities, calculated by XORing all global parities. Can be directly appied to Azure-LRC and Pyramid codes.
  * Optimal-LRC. The author proposed a new code construction for all admissible parameters. It's discussed in another paper (Optimal LRC codes for all lenghts n ≤ q) from him.

5. Theoretical Comparison
  * For the same (n, k,r), there is always one full-LRC with a lower NRC than that of Azure-LRC. However, in most settings, the reduction in NRC is coupled with a reduction in d.
  * Adding a local parity to global parity always reduces the repair cost, with additional storage overhead.
  * Azure-LRC and Optimal-LRC are most flexible in (n, k).

6. Experimental Comparison
  * In Ceph. It is the only open-source distributed storage system that implements LRCs as part of its main distribution. LRC as a plugin in Ceph.
  * Optimal-LRC implementation. They implemented Optimal-LRC in Ceph, but haven't release the source code yet.
  * For a given (n, k,r) combination, both ARC and NRC can predict which code will incur the the highest and lowest repair costs. At the same time, they are both inaccurate in their prediction of the actual repair cost.
  * Their results show that the reduction in the amount of data read for repair does not directly translate to a reduction in repair time. This is the result of additional bottlenecks in the system. Overall, the full-LRCs achieves the greatest reduction in repair time.
  * This paper also compares the results for LRCs in different zones, with local groups in each zone, and repaired locally. Data-LRCs and full-LRCs are expected to achieve the highest benefit in large-scale deployments, where sufficient I/O parallelism can be achieved within a single zone



Strength
------

1. This paper tries to analyse all existing LRCs with proposed metrics in theoretical ways, and shows that LRC reduces the repair cost in real setup.


Weakness
------

N/A for this paper. It's more a comparison.



<!-- refs -->