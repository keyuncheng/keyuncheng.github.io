---
title: "Paper Reading: Pelican OSDI'14"
date: 2021-06-14
permalink: /posts/2021/06/paper-reading-pelican-osdi14/
author_profile: false
excerpt: false
tags:
  - storage system
  - cold data
  - cost saving

---

Pelican: A Building Block for Exascale Cold Data Storage

Download
------

[OSDI, 2014](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-balakrishnan.pdf)


Summary
------

This paper presents Pelican, a rack-scale prototype storage unit as a building block for exabyte-scale cold storage for the cloud. The design of Pelican, including hardware configurations and software stack are tailor-made for cold data workload. The contribution of this paper is (i) it presents right-provisioning of Pelican's hardware configurations, allowing Pelican to have good performance but with disks partially active to reduce power consumption, (ii) it describes the Pelican software stack that provides good performance (low latency and high throughput) given hardware restrictions, by Pelican's data layout algorithm and IO scheduling, (iii) it describes Pelican's prototype very clearly, from hardware configuration to software stack deployment, and evaluates the performance with a rack-scale simulator using cross-validation.


Details
------

### Related / Previous works

* Amazon Galcier, Facebook cold data storage SKU (proprietary at that time)

* Modify disk IO handling to increase disk inactivity

* Write-offloading to allow disk inactivity: Pergamum

* Massive Arrays Of Idle Disks (MAID) systems: support peak performance

* Power propotional systems: Rabbit, Sierra


### Novelty of the paper

1. It presents the hardware configurations tailor-made for cold data storage

2. It presents the right-provisioning of hardware configuration
  * Domain as constraints: resource domain (power domain, cooling domain), failure domain
  * grouping of disks reduces the complexity of handling individual disks, and allows easier maintance for data layout and IO scheduling
  * Partial running of disks to save power, while preserving good performance: only allow several groups running (spinning) concurrently
  * The problem is formulated as an optimization problem (maximize non domain-colliding groups)

3. Pelican presents data layout for fault-tolerance with erasure coding (Cauchy RS(18,15))
  * A group with size > 18 (24) such that disk failure within the group can be repaired into the disks within the group (6)
  * define mutually-colliding groups and maximize the remaining mutually-disjoint groups
  * switching groups will cause spin-up and spin-down of two groups
  
4. Pelican schedules IO efficiently for the queries within individual groups to minimize the impact of spin-up latency
  * one scheduler for each class of domain
  * It considers the rebuild operation which may affects the throughput 

5. evaluation with simulation
  * workload: read dominant, but a full-parameter sweep with possible worloads, randomly distributed into each block, 24h
  * metrics: completion time, response time, service time, average reject rate, throughput
  * it also considers cost of faireness of the scheduling, power consumption, capacity utilization

Extra:  
* metadata service: *catelog*




Strength
------


Weakness
------

* Hardware and software are tightly coupled, and not easily generalized

* High reject rate when work rate gets higher, which seens not tolerable (Fig. 6)

* significant reduction of performance with repair traffic, even though it's concurrent(Fig. 7 (b))

* How metadata service is maintained by *catelog*?




<!-- refs -->


[system-architecture]: /images/2021-02-05-paper-reading-eccache-osdi16/system-architecture.jpg "system-architecture"