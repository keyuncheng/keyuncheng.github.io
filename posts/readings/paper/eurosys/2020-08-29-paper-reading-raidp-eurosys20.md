---
title: "Paper Reading: RAID-P Eurosys'20"
date: 2020-08-29
permalink: /posts/2020/08/paper-reading-raidp-eurosys20/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

RAIDP: replication with intra-disk parity


Download
------
[EuroSys, 2020](https://dl.acm.org/doi/pdf/10.1145/3342195.3387546)


Summary
------

Note: I can't find the pdf of paper public online. I refer to the slides from [Eurosys'20](https://www.eurosys2020.org/wp-content/uploads/2020/04/slides/426_rosenfeld_slides.pdf) and the slides from [Jingwei's github](https://github.com/jingwei87/reading/blob/master/slides/YanjingRen/RG-EuroSys20-RAIDP.pdf)


This work summaries how to quickly recover from two simutaneous disk failures, e.g. **3-replica** without restoring to the third replica for warm data. It introduces RAID-P, with intra-disk parity. It saves 33% storage spaces compared with 3-replica but with better performance while writing, also saves network bandwidth for writes. The performance of read is not really affected.


Details
------

* Super chunk's distribution. Divide each disk to N-1 super chunks. Any two disks shares a superchunk's copy. No same superchunk's are saved on each disk. Additional disk Lstor is used to save parity of each superchunk.

* Superchunk should be 2-replicated. Lstor fails separatedly, and needs to be cheap and fast.

* Assumes one/two disks failes, use remaining chunks to recover, since there should be at least one replica from existing nodes.

* 3K LoCs in Hadoop, Lstors are simulated in memory.



Strength
------

1. Similar fault tolerance with 3-way replica

2. up to 33% write performance improvement when writing new data compared with HDFS.

3. 33% less storage, since it's indeed 2-way replica for each superchunk.

4. Recovery is efficient thant EC.

5. Memory simulated Lstor.


Weakness
------

I need to look into the detail of the [thesis](http://www.cs.technion.ac.il/users/wwwb/cgi-bin/tr-get.cgi/2015/MSC/MSC-2015-06.pdf) to find it's weakness.
