---
title: "Paper Reading: Sathiamoorthy LRC PVLDB'13"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-sathiamoorthy-lrc-pvldb13/
author_profile: false
excerpt: false
tags:
  - Erasure Coding
---


XORing Elephants: Novel Erasure Codes for Big Data


Download
------
[PVLDB, 2013](http://smahesh.com/HadoopUSC/Xorbas.pdf)


Summary
------

This paper introduces Locally Repairable Code (different from Huang's work). With implementation over HDFS called HDFS-Xorbas, compared with RS, with 14% additional storage, the experiments shows approximately 2 times disk repair I/O and repair network traffic. Compared with MDS code, it introduces logarithmic locality and distance asymptotically equal to that of MDS code.


Details
------

1. Minimum Code Distance: minimum number of erasures of coded blocks after which the file can't be retrieved. For MDS code, distance is n - k + 1. If (n, k) = (10, 4), 5 blocks causes a data loss.

2. Block locality. Block locality *r* means each block can be a function of r other blocks. For small locality, even n, k grow, we can still reconstruct the data by small *r*. MDS code have *r* >= k.
  * LRC is near-MDS code, with logarithmic block locality compared with MDS code, tradeoff storage overhead to get repair speed, bandwidth efficiency.

3. Implementation in HDFS-Xorbas. Implement additional local parity / implied parity block, thus allows less blocks for repair. E.g. (10, 4) introduces 3 local parities, 2 for each 5 data blocks and 1 for 4 parities.

4. In encoding, Xorbas calculates all parity blocks through its MapReduce encoder. All blocks are spread across the cluster according to Hadoop's configured block placement policy.

5. Decoding. It has two decoders, the light-decoder for single block failure and heavy-decoder when light-decoder fails. MapReduce also applies for decoding jobs.

6. Reliability Analysis. MTTDL (mean-time to data loss) is introduces, and can be affected by (1) number of blocks failure and (2) block repair speed. The value of MTTDL is computed by a standard Markov model. The failure and repair rates = forward/backward rates. The stripe MTTDL = avg time from 0 state to fail state. Stats shows that two 0's increasement of MTTDL shows reliability compared with RS and 3-way's replica.

7. For the evaluation, three stats are compared; (1) HDFS Bytes read, (2) Network traffic, (3)
Repair time for each failure occurance.

Strength
------


1. Stats shows that LRC introduces approximately 2 times disk repair I/O and repair traffic, with marginally suboptimal storage.



Weakness
------


<!-- refs -->