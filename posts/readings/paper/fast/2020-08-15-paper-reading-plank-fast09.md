---
title: "Paper Reading: Plank FAST'09"
date: 2020-08-15
permalink: /posts/2020/08/paper-reading-plank-fast09/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - erasure coding
---

A Performance Evaluation and Examination of Open-Source Erasure Coding Libraries For Storage


Download
------
[FAST, 2009](http://web.eecs.utk.edu/~jplank/plank/papers/FAST-2009.pdf)


Summary
------

This papers compares different EC implementations to discern whether theory matches practice. It also demostrates how parameter selection affects the EC's performance. It also provides a reference for EC code designers about the potential research directions. Five ECs, including Classic Reed-Solomon
codes, Cauchy Reed-Solomon codes, EVENODD, Row Diagonal Parity (RDP) and Minimal Density RAID-6 codes are compared. 


Details
------

1. Introduction to ECs
	* RS (Vandermonde matrices)
	* Cauchy RS (Cauchy matrices), change matrix multiplication to XORs. Convert w bit words to w * w matrices. Researches on constructing GM with fewer 1s.
	* EVENODD and RDP, developed for RAID-6. RDP acheves optimal encoding and decoding performance when k = w or k + 1 = w. when (w - k) increases, the performance decreased.
	* Minimal Density RAID-6. When k <= w, the remaining w rows in GM must have at least kw + k + 1 ones, when achieves the lower bound, we call Minimal Density code. Minimal Density achieves near-optimal performance when individual pieces of data are modified, bettern than RDP/EVENODD.
	* Anvin's RAID-6 optimizations. The encoding speed is improved compared with standard RS.

2. Libraries compared
	* Luby
	* Zfec
	* Jerasure
	* Cleversafe
	* EVENODD/RDP

Experiments
	* Encoding/Decoding. n different disks. Each piece of n = m + k resides in 1 disk.
	* Fixed size data buffer/coding buffer. A data buffer consists of k blocks, coding buffer with m blocks.
	* A block consists of s strips, each strip partitioned into words with size w. Data buffer size: kswPS. PS represents a theoretical stripe.

3. Encoding: Data stripe encode to Coding stripe one by one.
	* Experiments are conducted with a Macbook and a Dell workstation. memcpy() and XOR speeds are benchmarked.
	* Test with a 256MB video file. Variables: data buffer size. Time recording: gettimeofday()
		* Results shows that the size of data buffer impacts performance.

3.1 Parameter Space
	* Test cases: RAID-6 (6,2), (14, 2), (12, 4), (10, 6), file: 1GB random file, w are different for each library.

3.2 Impact of packet size: high packet size performs better. A maximum of performance when the code makes the best use of L1 cache. Smaller packets are necessary for most of the stripes to fit into cache.

3.3 Overall Encoding performance
	* Packet size: optimal for each lib
	* The overall performance will be greately affected by w.
	* RDP performs best, suffers while w increases.
	* Jerasure performs good, Luby and Cleversafe not that good, reason: implementation of GS not optimized
	* RS RAID-6 performs good.

4. Decoding
	* random m data drives for failure

4.1 Results
	* Macbook matches the theory closely
	* Minimal Density code benefits greately from Code-Specific Hybrid Reconstruction in Jerasure.
	* The performance can be compared with the number of XOR's.

5. XOR Units.
	* Compared 32-bit/64-bit for XOR units.
	* Tested with RDP, w = 6, word size: char, short, int, long(64-bit system with 8 bytes)


6. Conclusion
	* RAID-6. With Jerarues's improvement over decoding, RAID-6 performs the best.
	* For non-RAID-6, CRS performs better than RS.
	* Param choices: w; packet size.
	* More experiments should be conducted beyong RAID-6.



Strength
------

N/A




Weakness
------

N/A


<!-- refs -->
