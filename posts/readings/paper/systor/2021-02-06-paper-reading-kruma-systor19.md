---
title: "Paper Reading: Kruma"
date: 2021-02-06
permalink: /posts/2021/02/paper-reading-kruma-systor19/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - consistency
---

Kurma: Secure Geo-Distributed Multi-Cloud Storage Gateways

Download
------
[SYSTOR, 2019](https://www.fsl.cs.sunysb.edu/docs/nfs4perf/kurma-systor19.pdf)


Summary
------

This paper introduces Kruma, a cloud storage gateway system which allows applications requiring NAS as the storage interface. Kruma replicates metadata across geo-distributed gateways and maintains a unified file-system namespace. Kruma stores encrypted data blocks in clouds and can provide data integrity checking.


Details
------

### Previous works

Selected
  * SCFS provides freshness without using Merkle trees, but requires a trusted and centralized metadata service running on a cloud
  * Hybris targets for KV store and with only one gateway

### Novelty of the paper



### System Architecture

![system-architecture][system-architecture]

* Designed for enterprise uses

* Geo-distributed storage gateways, each for one office/department

### Features

* Support replication, EC, secret sharing

* Geo-distributed storage gateways, each for one office/department
  * Metadata are stored in trusted gateways
  * Each Kurma gateway maintains a copy of the whole filesystem metadata
  * Metadata changes made by a Kurma gateway are asynchronously replicated to all other gateways using Hedwig
  * NFS close-to-open consistency
  * For clients across geo-distributed gateways, Kurma provides FIFO consistency
  * Metadata are stored in ZooKeeper (in-memory store), each gateway maintains a replica of the entire FS metadata in a ZooKeeper instance

* Caching
  * Each gateway has local storage (persistent write-back cache) for cache
  * The cache stores plaintext
  * The cache also maintains additional metadata in stable storage so that dirty data can be recovered after crashes; the metadata includes a list of dirty files and the dirty extents of each file
  * For consistency between local cache and remote data, it compares locally saved remote-time and the latest remote-time from cloud
  * Use Write-back-wait time (WBWT) to sync and async write to cloud

* Security
  * to check data freshness, Kruma broadcasts block version numbers among all gateways.

* File Sharing
  * Metadata changes are broadcasts using Hedwig in a "all-to-all broadcast" manner. Hedwig is a pub-sub system optimized for communication across data-centers, and it protects its communication using SSL.
  * Across gateways, Kurma provides FIFO consistency. E.g. directy operation should be executed before file creation in that directory
  * Kruma add ObjectID to detect conflicts in async operations

* Cloud ranking by latency

Strength
------

* Designed and targeted for enterprise use


Weakness
------

* Extra cost for real deployment (multiple gateways)

* For the cache design
  * Write-back-write-time falls back to sync mode when operating over large files



<!-- refs -->


[system-architecture]: /images/2021-02-06-paper-reading-kruma-systor19/system-architecture.jpg "system-architecture"