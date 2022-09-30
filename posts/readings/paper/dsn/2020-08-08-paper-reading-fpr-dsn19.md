---
title: "Paper Reading: Fast Predictive Repair DSN'19"
date: 2020-08-08
permalink: /posts/2020/08/paper-reading-fpr-dsn19/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - erasure coding
  - repair
---

Fast Predictive Repair in Erasure-Coded Storage


Download
------
[DSN, 2019](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/dsn19.pdf)


Summary
------

This paper presents a predictive repair pipelining techniques called FastPR for districuted storage systems with erasure coding. It carefully couples the migration and reconstruction of the chunks of the STF (Soon-To-Fail). Two repair scenarios scatter-repair and hot-standby-repair are mainly addressed. Parallization in migration and reconstruction results in 30% repair speed improvement over reactive repair.


Details
------

- Collect disk status from SMART
- Workflow
    - Migration: collect chunks from STF nodes to new healthy nodes
    - Reconstruction: follows reactive repair. Reconstruct chunks from STF nodes.
- Theoretical prove of speed improvement.
- Finding reconstruction set, and schedule repair.
- System architecture: Coordinator over Agents.


Strength
------

- 30% speed improvement over reactive repair.
- Easily depolyable on HDFS without changing HDFS code base



Weakness
------


<!-- refs -->
