---
title: "Paper Reading: OpenEC FAST'19"
date: 2020-08-08
permalink: /posts/2020/08/paper-reading-openec-fast19/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - erasure coding
---

OpenEC: Toward Unified and Configurable Erasure Coding Management in Distributed Storage Systems


Download
------
[FAST, 2019](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/fast19.pdf)


Summary
------

This paper presents OpenEC, a unified framework for deploying configurable erasure coding solutions to existing distributed storage systems. OpenEC is deployed to HDFS, and can optimize EC performance.


Details
------

Problems to solve: how to easily deploy configurable new EC techs to existing distributed storage systems. General framework exists but functionalities are limited to existing ECs, existing storage systems are highly coupled with tight dependencies in workflow and ECs.

Solutions:
- ECDAG (direct acyclic graph), describes the workflows of coding operations of a coding group. Encoding and decoding are both associated with a ECDAG. Implement ECDAG with Join, BindX, BindY.

System architecture:
Top: OECClient -> Agent -> HDFS Client. Agents are controlled by a separate controller. Controller creates and manages ECDAGs.


Strength
------

- General framework for new ECs
- Can be easily deployed on HDFS with limited code modifications. Performance evaluated on AWS EC2
- Performance improvement


Weakness
------


<!-- refs -->
