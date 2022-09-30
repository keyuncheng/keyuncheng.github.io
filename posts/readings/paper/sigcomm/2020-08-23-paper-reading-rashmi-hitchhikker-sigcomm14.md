---
title: "Paper Reading: Rashmi, Hitchhikker’s guide SIGCOMM'14"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-rashmi-hitchhikker-sigcomm14/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

A “Hitchhiker’s” Guide to Fast and Efficient Data Reconstruction in Erasure-coded Data Centers



Download
------
[SIGCOMM, 2014](http://www.cs.cmu.edu/~rvinayak/papers/Hitchhiker_SIGCOMM14.pdf)


Summary
------

This paper introduces Hitchhiker, an EC storage system that with no additional storage but achieves 25% network traffic saving and 45% disk I/O. The implementation in HDFS shows 35% reduction in network traffic, 36% reduction in computation time and 32% data read time during reconstruction.  



Details
------


1. Three versions of Hitchhiker are introduced.

* Hitchhiker-XOR

Encode: divide the stripe to 2 sub-stripes *a* and *b*. For each, different calculation of parity is introduced.

Decode: three steps to get sub-stripe *b* and then *a*.

* Hitchhiker-XOR+

Encode: One additional XOR compared with Hitchhiker-XOR.

Decode: Similar to Hitchhiker-XOR.

This method requires underlying RS to have all-XOR-parity property.

* Hitchhiker-nonXOR

Not fully XORed, but free the restriction of underlying RS to have all-XOR-parity property.

Encode: All XORs.

Decode: 1 additional multiplication in step 3.

2. Hop and Couple feature in Disk for efficiency. This technique aims to minimize the
degree of discontinuity in disk reads during the reconstruction of data units. The hop-and-couple technique couples a byte with another byte within the same unit that is a certain distance ahead. the *hop distance* can be greater than 1. Coupled bytes are encoded together.

3. Evaluation. (n, k) = (10, 4), block size: 256MB, buffer size: 1MB. The metric is time for processing a block. 

* Computation time: For any data block, Hitchhiker shows faster reconstruction than RS.

* Read time for degraded reads. Hitchhiker reads from more machines, but read half for most of the machines, thus shows less read latency.

4. Tradeoffs

* Connecting to more than k machines introduces potential read latency.

* Choice of hop-length. It may introduces reconstruction of unnecessary coupled bytes during reconstruction of a byte.

* **72.1%** higher encoding time, since for each stripe, nearly two times for sub-stripes. To improve other metrics, Hitchhiker sacrifies encoding time.


Strength
------

* No additional storage introduced.

* Better repair performance (disk I/O and repair traffic).


Weakness
------

* 72% much higher encoding time. Write performance are not analyzed.


<!-- refs -->
