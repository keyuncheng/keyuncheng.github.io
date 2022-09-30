---
title: "Paper Reading: Butterfly Codes FAST'16"
date: 2020-08-29
permalink: /posts/2020/08/paper-reading-butterfly-codes-fast16/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

Opening the Chrysalis: On the Real Repair Performance of MSR Codes

Download
------
[FAST, 2016](https://www.usenix.org/system/files/conference/fast16/fast16-papers-pamies-juarez.pdf)


Summary
------


This paper introduces Butterfly codes, systematic code with optimal repair I/O. By carefully integrating the code into districuted system, Butterfly codes achieves theoretically optimal repair performance of MSR codes.



Details
------

The implementation uses a newer reconstruction of the code, thus allows simpler implementation.

1. Encoder. The sub-boolean matrix A and B are constructed recursively with input data vector codes

2. Decoder. It proves to allows 2 nodes failure. 4 samples are illustrated.

* One data column is lost. The first D0 and remaining D1-Dk-1

* H and B parity column

3. HDFS implementation. Details are of the implementation, including communication, memory management not listed here.

4. Ceph implementation as a plug-in.




Strength
------

From HDFS and Ceph's test over AWS EC2, it shows:

1. increased repair throughput compared with RS.

2. MSR codes over GF(2) achieve low CPU usage. But some params like stripe size affects the performance.

3. With careful implementation, MSR codes reduces the repair traffic by 2x to traditional erasure codes. 




Weakness
------

N/A


<!-- refs -->
