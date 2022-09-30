---
title: "Paper Reading: SCFS ATC'14"
date: 2021-01-29
permalink: /posts/2021/01/paper-reading-scfs-atc14/
author_profile: false
excerpt: false
tags:
  - Multi-cloud storage
  - File System
---


SCFS: A Shared Cloud-backed File System

Download
------
[ATC, 2014](http://www.di.fc.ul.pt/~bessani/publications/usenix14-scfs.pdf)


Summary
------

This paper presents a multi-cloud-backed file system SCFS. The main idea of this work is to provide confidentiality, integrity and availability of data and file services without complete trust of individual cloud providers, and without executing specific codes on storage clouds. SCFS provides strong consistency on file accesses and also provide a backplane to support multiple cloud interfaces. It adopts classical ideas of file system / cloud storage system, including consistency-on-close sematics, metadata and data seperation. SCFS follows some design principles like pay-per-ownership, versioning. SCFS seperates the metadata and lock management coordinator, instead of embedding into the system itself. The client-side data and metadata caching boosts the read/write performance significantly.


Details
------

### System Architecture

![system-architecture][system-architecture]

1. Implementation
  * SCFA-Agent: User-space file system based on FUSE-J (Java).
  * Coordination services: external (e.g. DepSpace, ZooKeeper) to manage metadata and locks
  * Storage Backend: Amazon S3 only (one single cloud), DepSky (multi-cloud)


### Features

* Versioning (follow DepSky)

* **Strong consistency by consistency-on-close** (when a file is closed, it's contents should be updated to the cloud, and observable to all users), which is different from eventual consistency of cloud storage providers

* Consistency
  * Metadata consistency is provided by **external coordinators** with complex replication protocols to ensure fault tolerance, and operations with sync power.
  * Algorithm in SCFS for strong consistency is the same as DepSky-A (Write hash(data) and store in Metastore, read hash and calculate hash(date-read))

* R/W as a complete object in cloud (instead of reading blocks by blocks)
  * Good for small sized files

* **Two levels of cache**
  * Client side local cache (data and metadata)， LRU cache like
  * Client memory holding opened files (data and metadata). This is efficient for sync to local and cloud. sync to cloud is **only executed by close() operations**
  * The filesize should fit the cache size in memory (as partial read/write is not available at least shown in paper) 

* GC
  * runs as a process in isolation at each SCFS Agent

* SCFS ACL
  * setfacl/getfacl (client based and file based)

* Private Name Spaces (user name based)
  * user locks
  * traces shows that PNS significantly reduces metadata for shared files

* Implementation
  * blocking and non-blocking(enqueue closed files to sync to cloud, but the file locks in coordinator are not released until sync completes), which leads to a tradeoff between client-side performance and consistency
  * non-sharing implementation


### Evaluation

* benchmark
  * Filebench (USENIX Login'16), Benchmarking (HotOS'11)
  * baseline: LocalFS(FUSE-J based local FS), S3FS, S3QL, Dropbox
  * variants: blocking/non-blocking, sharing/non-sharing, AWS only/4 public clouds (with at lease one r/w siginificantly faster than AWS)

* Ovservations
  * Blocking significantly slower than non-blocking
  * locking service with manipulation over lock files (retrieve/update the lock remotely from coordinator) affects the results. Storing the locks locally could make write much more responsive
  * Comparation with Dropbox for data sharing (latency of blocking is much smaller than non-blocking, because of the way they do benchmark: overall_time = read + wait(for another writer write))
  * Metadata cache improves overall r/w performance, but increasing the size does not bring much more benefit.
  * Operation Costs are also estimated and evaluated.

Strength
------

1. it utilizes coordinators for metadata and locks consistency with r/w performance drop as the tradeoff

2. local cache of data and metadata and non-blocking write feature improves client response speed

3. Utilizes DepSky as the storage backend

4. It tries to compare existing public file storage solutions

5. It targets at small sized files (KBs to <= 10 MBs)


Weakness
------

1. Common problems for client-side only deployment (refer to those in [DepSky](/posts/2019/07/paper-reading-depsky-eurosys11/))

2. The two layered cache design does not work for medium/large-sized files handling
  * It requires fiting the complete file to memory buffer, as partial read/write is not supported

3. (engineering)Scheduling of non-blocking file-sync is not supported
  * The implementations assumes immediate writes to cloud after close

4. metadata and lock management completely rely on the coordinator

5. Lack of failure recovery (one possible solutions is by journaling and logging)


<!-- refs -->

[system-architecture]: /images/2021-01-29-paper-reading-scfs-atc14/system-architecture.png "system-architecture"