---
title: "Paper Reading: Hybris"
date: 2021-02-03
permalink: /posts/2021/02/paper-reading-hybris-socc14/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - metadata 
---

Hybris: Robust Hybrid Cloud Storage


Download
------
[SoCC, 2014](http://vukolic.com/hybris-socc2014.pdf)


Summary
------

This paper introduces Hybris KV Store, which tolerates up to *f* malicious clouds with *f + 1* write replication across clouds, and read involving a single cloud. Previous works requires *3f + 1* clouds to mask *f* potentially malicious clouds, which is much higher cost than *f + 1*. Hybris leverages strong metadata consistency to guarantee data consistency.


Details
------

### Previous works

ICStore, SpanStore: limited to tolerating cloud outages instead of malicious behaviours in clouds (data corruption). Actually Hybris's solution is just trying to compare the size of the value *s* to prevent DoS attacks.

DepSky, SCFS: requiring *3f + 1* clouds to mask *f* faulty clouds, which is costly in practice.

metadata management: existing works scatter metadata across public clouds, increasing the difficulty of storage management.

### Novelty of the paper

1. the first *robust* hybrid multi-cloud storage system - allows tolerating malicious clouds at the price of tolerating only cloud outages.
  * Hybris stores metadata on private premises, which allows control over data and improves system performance in terms of latency and storage costs.
  * Hybris clients are built on top of ZooKeeper coordination services - as ZooKeeper clients

2. Consistency
  * Hybris treats cloud inconsistencies as cloud failures by relying on strong metadata consistency


### System Architecture

![system-architecture][system-architecture]

  * Metadata is stored within the key component of Hybris Reliable MetaData Service (RMDS)
  * Data is distributed into public clouds, with data caching using Memcached on private premises
  * Hybris client is responsible for interaction with (untrusted) public clouds, RMDS and caching services.
  * System model: dual fault model - (i) the processes on private premises (i.e., in the private cloud) can fail by crashing, and (ii) model public clouds as potentially malicious processes.
  * Multi-writer and multi-reader KV store.
  * Rank clouds by latency


### Protocols

PUT: using timestamp and expiration to guarantee the PUT operation is durable (all data are written to cloud with *f + 1* acks), and finally update metatada on RMDS.

GET: the client selects the first cloud c1 from cloudList
  * Relying on Zookeeper for proactive metadata updates
  * At any point of time, if there is any update to the data, the client cancels all pending downloads, and repeat the procedure of get from *f + 1* clouds.

With Erasure Coding: *2f + k* clouds


### Optimizations

* Caching: write through cache and cache-on-read policies
  * write to cloud and write to cache in parallel
  * read from cache first (also need to calculate hash)


Strength
------

* Hosts and manages metadata over private premises (deployment)

* Distributed memory caching decreases Hybris latency by an order of magnitude when cache is large enough compared to object size. 

Weakness
------

* Hybris restricts the metadata services to a single geographical location (maybe a cluster)



<!-- refs -->


[system-architecture]: /images/2021-02-03-paper-reading-hybris-socc14/system-architecture.jpg "system-architecture"