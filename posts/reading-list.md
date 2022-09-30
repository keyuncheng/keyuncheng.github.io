---
title: 'Reading List'
date: 2019-08-01
permalink: /posts/2019/08/reading-list/
author_profile: false
excerpt: false
tags:
  - reading
---

**Last Modified**: Aug, 2021

---

My reading list includes papers, articles, tutorials, videos, etc. for
research purpose. Items are characterized by their main topics / keywords.

---


## Table of Contents

I use [this](https://ecotrust-canada.github.io/markdown-toc/) to generate the
ToC. Simply copy the contents to it and paste the ToC back.


- [Recent](#recent)
- [To-read](#to-read)
- [Past](#past)
  * [Erasure Coding](#erasure-coding)
    + [Basics](#basics)
    + [Codes](#codes)
    + [Network Coding and Regenerating
      Codes](#network-coding-and-regenerating-codes)
    + [Reliability Analysis](#reliability-analysis)
    + [Techniques](#techniques)
    + [Systems](#systems)
  * [Edge](#edge)
  * [Deduplication](#deduplication)
  * [Consensus](#consensus)
  * [Stream Processing](#stream-processing)
  * [Network Measurement](#network-measurement)
  * [Graph Processing](#graph-processing)
- [TOS (Transaction on Storage) Paper
  List](#tos--transaction-on-storage--paper-list)
    + [Erasure Coding](#erasure-coding-1)
    + [RAID](#raid)
    + [Data Placement](#data-placement)
    + [Flash-memory](#flash-memory)
    + [Backup](#backup)
    + [Storage System](#storage-system)
    + [KV-Store](#kv-store)
    + [Benchmark](#benchmark)
    + [Techniques](#techniques-1)
    + [File System](#file-system)
- [SEC (Symposium on Edge Computing) Paper
  List](#sec--symposium-on-edge-computing--paper-list)


## Recent

Venue | Title | Link / Summary | Keywords
--- | --- | --- | ---
TIT'19 | Rack-Aware Regenerating Codes for Data Centers. | [link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/tit19rrc.pdf) | RRC
ISIT'16 | Double Regenerating Codes for Hierarchical Data Centers | [link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/isit16.pdf) | DRC
TIT'10 | Optimal Exact-Regenerating Codes for Distributed Storage at the MSR and MBR Points via a Product-Matrix Construction | [link](http://www.cs.cmu.edu/~rvinayak/papers/product_matrix_codes.pdf) | Produce Matrix Code
TOS'17 | Optimal Repair Layering for Erasure-Coded Data Centers: From Theory to Practice. | [link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/tos17drc.pdf) | DRC, DoubleR
--- | --- | --- | ---


## To-read

Venue | Title | Link / Summary | Keywords
--- | --- | --- | ---
--- | MBRR | --- | MBRR code construction
ISIT'21 | Generalized Rack-aware Regenerating Codes for Jointly Optimal Node and Rack Repairs | [link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/isit21.pdf) | GRRC
ISIT'20 | Minimum Storage Rack-Aware Regenerating Codes with Exact Repair and Small Sub-Packetization | [link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/isit20msrr.pdf) | MSRR
TIT'16 | Explicit Minimum Storage Regenerating Codes | [link](https://cpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/c/490/files/2015/09/cnstr_long_v7.pdf) | explicit MSR code
ISIT'12 | Regenerating Codes for Errors and Erasures in Distributed Storage | [link](https://arxiv.org/pdf/1202.1050.pdf) | Rashmi RC, [slides in CUHK](https://www.inc.cuhk.edu.hk/sites/default/files/seminars/slides/FINAL_CUHK_TALK_PVK_with_ref.pdf)
Allerton Conf., Urbana-Champaign'09 | Explicit Construction of Optimal Exact Regenerating Codes for Distributed Storage | [link](https://arxiv.org/pdf/0906.4913v2.pdf) | E-RC
TIT'11 | Interference Alignment in Regenerating Codes for Distributed Storage: Necessity and Code Constructions | [link](https://www.cs.cmu.edu/~nihars/publications/IA_in_RC.pdf) | MISER code
ISIT'12 | Regenerating Codes for Errors and Erasures in Distributed Storage | [link](https://arxiv.org/pdf/1202.1050.pdf) | [Slides](http://www.cs.cmu.edu/~rvinayak/papers/slides_errorsInStorage_ISIT12.pdf)
OSDI'14 | f4: Facebook’s Warm BLOB Storage System | [link](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-muralidhar.pdf) | Facebook f4
SOSP'13 | The Google File System | [link](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) | Google File System
OSDI'10 | Availability in Globally Distributed Storage Systems | [link](https://www.usenix.org/legacy/events/osdi10/tech/full_papers/Ford.pdf) | Google Availibility
SIGMOD'1988 | A Case for Redundant Arrays of Inexpensive Disks (RAID)  | [link](https://www.cs.cmu.edu/~garth/RAIDpaper/Patterson88.pdf) | RAID
HotCloud'14 | A day late and a dollar short: the case for research on cloud billing systems | --- | ---
CCS'09 | HAIL: A high-availability and integrity layer for cloud storage. | --- | ---
FAST’12 | BlueSky: A Cloud-Backed File System for the Enterprise | --- | ---
TOS'08 | A nine year study of file system and storage benchmarking. | [Link](https://dl.acm.org/doi/10.1145/1367829.1367831) | ---
FAST’14 | --- | --- | CodFS
FAST'16 | --- | --- | Cocytus
TOS'20 | The Case for Custom Storage Backends in Distributed Storage Systems. | [Link](https://doi.org/10.1145/3386362) | ---
--- | How to share a secret. | --- | A. Shamir.

* [TOS Paper List](#tos--transaction-on-storage--paper-list)


## Past


### Erasure Coding

#### Basics

Venue | Title | Link / Summary | Keywords
--- | --- | --- | ---
SIAM'1960 | Polynomial Codes Over Certain Finite Fields. | [Summary](/posts/2021/06/paper-reading-rs-siam1960/) | RS code original. MUST-READ
Manuscript | An Introduction to Galois Fields and Reed-Solomon Coding | [link](https://people.cs.clemson.edu/~westall/851/rs-code.pdf) | Into to Finite Field and RS code (communication) in Clemenson
Manuscript | Reed-Solomon Codes | [link](https://courses.cs.duke.edu//spring10/cps296.3/rs_scribe.pdf) | Intro to RS code from Duke Univ.
Summary | Concepts that must know | [Summary](/posts/2021/07/blogs-ec-basic-concepts/) | EC basic Concepts and keywords
FAST'09 | A Performance Evaluation and Examination of Open-Source Erasure Coding Libraries For Storage. | [Summary](/posts/2020/08/paper-reading-plank-fast09/) | Plank EC eval
USENIX Login'13 | Erasure Codes for Storage Systems: A Brief Primer. | [Summary](/posts/2020/08/paper-reading-plank-usenixlogin13/) | Plank EC basics
FAST Tutorial'13 | Tutorial: Erasure Coding for Storage Systems. | [Summary](/posts/2020/08/docs-reading-plank-tutorial-fast13/) | Plank EC tutorial
--- | --- | --- | ---


#### Codes

Venue | Title | Link / Summary | Keywords
--- | --- | --- | ---
TOS'09 | GRID codes: Strip-based erasure codes with high fault tolerance for storage systems. | [Summary](/posts/2020/10/paper-reading-grid-codes-tos09/) | GRID codes
FAST'12 | Rethinking Erasure Codes for Cloud File Systems: Minimizing I/O for Recovery and Degraded Reads. | [Summary](/posts/2020/09/paper-reading-khan-fast12/) | Khan
TOS'12 | Generalized X-code: An efficient RAID-6 code for arbitrary size of disk array. | [Summary](/posts/2020/10/paper-reading-generalized-x-code-tos12/) | Generalized X-code
ATC'12 | Erasure Coding in Windows Azure Storage. | [Summary](/posts/2020/08/paper-reading-huang-lrc-atc12/) | Azure LRC
PVLDB'13 | XORing Elephants: Novel Erasure Codes for Big Data. | [Summary](/posts/2020/08/paper-reading-sathiamoorthy-lrc-pvldb13/) | Sathiamoorthy, LRC
TOS'13 | Pyramid Codes: Flexible Schemes to Trade Space for Access Efficiency in Reliable Data Storage Systems. | [Summary](/posts/2020/09/paper-reading-pyramid-codes-tos13/) | Pyramid Codes
TIT'14 | A family of optimal locally recoverable codes. | [Summary](/posts/2020/09/paper-reading-optimal-lrc-tit14/) | Optimal LRC
SIGCOMM’14 | A “Hitchhiker’s” Guide to Fast and Efficient Data Reconstruction in Erasure-coded Data Centers. | [Summary](/posts/2020/08/paper-reading-rashmi-hitchhikker-sigcomm14/) | Rashmi, Hitchhikker’s guide
FAST'14 | STAIR Codes: A General Family of Erasure Codes for Tolerating Device and Sector Failures in Practical Storage Systems. | [Summary](/posts/2020/08/paper-reading-staircodes-fast14/) | STAIR Codes
FAST'15 | Having Your Cake and Eating It Too: Jointly Optimal Erasure Codes for I/O, Storage, and Network-bandwidth. | [Summary](/posts/2020/08/paper-reading-rashmi-pm-rbt-fast15/) | Rashmi, PM-RBT
FAST’16 | Opening the Chrysalis: On the Real Repair Performance of MSR Codes. | [Summary](/posts/2020/08/paper-reading-butterfly-codes-fast16/) | Butterfly codes
FAST’18 | Clay Codes: Moulding MDS Codes to Yield an MSR Code. | [Summary](/posts/2020/08/paper-reading-clay-codes-fast18/) | Clay codes
ATC'18 | On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes. | [Summary](/posts/2020/09/paper-reading-lrc-comparison-atc18/) | compare LRC
HotStorage'20 | SelectiveEC: Selective Reconstruction in Erasure-coded Storage Systems. | [Summary](/posts/2020/08/paper-reading-selectiveec-hotstorage20/) | SelectiveEC
--- | --- | --- | ---


#### Network Coding and Regenerating Codes

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
FAST'11 Poster | Repairing Erasure Codes. | [Link](https://www.usenix.org/legacy/event/fast11/posters_files/Papailiopoulos.pdf) | NC for storage poster
IEEE Survey'11 | A Survey on Network Codes. | [Summary](/posts/2021/06/paper-reading-ncstoragesurvey-ieeesurvery/) | NC for storage survey
TIT'10 | Network Coding for Distributed Storage Systems. | [Summary](/posts/2020/08/paper-reading-ncstorage-tit10/) | network coding for storage, [video](https://www.youtube.com/watch?v=RMRyP6JRKGk), [report](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory-au14/projects/codes-DSS-report.pdf)
PPT | Intro to regenrating codes | [link](https://ewh.ieee.org/r6/scv/mag/MtgSum/Meeting2017_05_2_presentation.pdf) | ---
--- | --- | --- | ---


#### Reliability Analysis

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
SNAPI'07| Outshining Mirrors: MTTDL of Fixed-Order SSPiRAL Layouts | [Link](http://www2.cs.uh.edu/~paris/MYPAPERS/Snapi07.pdf) | ---
I2TS'08 | When MTTDLs Are Not Good Enough: Providing Better Estimates of Disk Array Reliability  | [Link](https://www.cse.scu.edu/~tschwarz/Papers/i2ts08.pdf) | ---
HotStorage'10 | Mean time to meaningless: MTTDL, Markov models, and storage system reliability | [Link](https://www.usenix.org/legacy/event/hotstorage10/tech/full_papers/Greenan.pdf) | MTTDL Meaningless
Summary | Reliability Analysis: MTTDL | [Summary](/posts/2021/07/blogs-mttdl/) | Calculation of MTTDL
--- | --- | --- | ---


#### Techniques

Venue | Title | Link / Summary | Keywords
--- | --- | --- | ---
MSST’12 | On the speedup of single-disk failure recovery in XOR-coded storage systems: Theory and practice. | [Summary](/posts/2020/09/paper-reading-zhu-replace-recovery-msst12/) | Zhu
FAST'15 | A Tale of Two Erasure Codes in HDFS. | [Summary](/posts/2020/09/paper-reading-twoec-fast15/) | ---
OSDI'16 | EC-Cache: Load-Balanced, Low-Latency Cluster Caching with Online Erasure Coding. | [Summary](/posts/2021/02/paper-reading-eccache-osdi16/) | Rashmi, EC-Cache
Eurosys'16 | Partial-Parallel-Repair (PPR): A Distributed Technique for Repairing Erasure Coded Storage. | [Summary](/posts/2020/08/paper-reading-ppr-eurosys16/) | PPR
ATC'17 | Repair Pipelining for Erasure-Coded Storage. | [Summary](/posts/2020/08/paper-reading-repair-pipelining-atc17/) | ECPipe
DSN'19 | Fast Predictive Repair in Erasure-Coded Storage. | [Summary](/posts/2020/08/paper-reading-fpr-dsn19/) | FastPR
FAST'19 | Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques. | [Summary](/posts/2020/08/paper-reading-ec-acceleration-fast19/) | EC Acceleraion
Eurosys'20 | RAIDP: replication with intra-disk parity. | [Summary](/posts/2020/08/paper-reading-raidp-eurosys20/) | RAID-P
--- | --- | --- | ---


#### Systems

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
SoCC'10 | RACS: a case for cloud storage diversity. | [Summary](/posts/2019/07/paper-reading-racs-socc10/) | RACS
Eurosys'11 | DEPSKY: A High-Availability and Integrity Layer for Cloud Storage. | [Summary](/posts/2019/07/paper-reading-depsky-eurosys11/) | Depsky
FAST'12 | NCCloud: A Network-Coding-Based Storage System in a Cloud-of-Clouds. | [Summary](/posts/2019/06/paper-reading-nccloud-fast12/) | NCCloud, network coding
SOSP'13 | SPANStore: Cost-Effective Geo-Replicated Storage Spanning Multiple Cloud Services | [Summary](/posts/2021/02/paper-reading-spanstore-sosp13/) | SPANStore
OSDI'14 | Pelican: A Building Block for Exascale Cold Data Storage. | [Summary](/posts/2021/06/paper-reading-pelican-osdi14/) | Pelican, cold DSS
ATC'14 | SCFS: A Shared Cloud-backed File System. | [Summary](/posts/2021/01/paper-reading-scfs-atc14/) | SCFS, Depsky extension
SoCC'14 | Hybris: Robust Hybrid Cloud Storage. | [Summary](/posts/2021/02/paper-reading-hybris-socc14/) | Hybris
FAST'19 | OpenEC: Toward Unified and Configurable Erasure Coding Management in Distributed Storage Systems. | [Summary](/posts/2020/08/paper-reading-openec-fast19/) | OpenEC
SYSTOR'19 | Kurma: Secure Geo-Distributed Multi-Cloud Storage Gateways. | [Summary](/posts/2021/02/paper-reading-kruma-systor19/) | Kurma
NSDI'20 | Near-Optimal Latency Versus Cost Tradeoffs in Geo-Distributed Storage | [Summary](/posts/2021/06/paper-reading-pando-nsdi20/) | PANDO, consensus, EC
--- | --- | --- | ---


### Edge

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
HotEdge'20 | Sharing and Caring of Data at the Edge. | [Summary](/posts/2021/02/paper-reading-sharing-hotedge20/) | edge storage survey
JPDC'20 | EdgeKV: Decentralized, scalable, and consistent storage for the edge. | [Summary](/posts/2021/06/paper-reading-edgekv-jpdc20/) | EdgeKV
--- | --- | --- | ---

* [SEC Paper List](#sec--symposium-on-edge-computing--paper-list)


### Deduplication

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
ATC'15 | Toward Reliable, Secure, and Cost-Efficient Cloud Storage via Convergent Dispersal. | [Summary](/posts/2019/06/paper-reading-cdstore/) | CDStore
--- | --- | --- | ---


### Consensus

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
ATC'14 | In Search of an Understandable Consensus Algorithm. | [Summary](/posts/2019/07/paper-reading-raft-atc14/) | Raft
--- | --- | --- | ---


### Stream Processing

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
ICDCS'20 | Toward Adaptive Disk Failure Prediction via Stream Mining. | [Summary](/posts/2020/08/paper-reading-streamdfp-icdcs20/) | StreamDFP
--- | --- | --- | ---


### Network Measurement

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
SIGCOMM'18 | SketchLearn: Relieving User Burdens in Approximate Measurement with Automated Statistical Inference. | [Summary](/posts/2020/08/paper-reading-sketchlearn-sigcomm18/) | SketchLearn
--- | --- | --- | ---


### Graph Processing

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
OSDI'16 | Gemini: A Computation-Centric Distributed Graph Processing System. | [Summary](/posts/2020/09/paper-reading-gemini-osdi16/) | Gemini
SIGMOD'19 | Nanosecond Indexing of Graph Data With Hash Maps and VLists. | [Summary](/posts/2020/09/paper-reading-nanosecond-sigmod19/) | Nanosecond
--- | --- | --- | ---


## TOS (Transaction on Storage) Paper List

#### Erasure Coding

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'09 | GRID codes: Strip-based erasure codes with high fault tolerance for storage systems. | [Link](https://dl.acm.org/doi/10.1145/1480439.1480444) | ---
TOS'12 | Generalized X-code: An efficient RAID-6 code for arbitrary size of disk array. | [Link](https://dl.acm.org/doi/10.1145/2339118.2339121) | ---
TOS'13 | Exploiting Redundancies and Deferred Writes to Conserve Energy in Erasure-Coded Storage Clusters. | [Link](https://doi.org/10.1145/2491472.2491473) | ---
TOS'13 | Pyramid Codes: Flexible Schemes to Trade Space for Access Efficiency in Reliable Data Storage Systems. | [Link](https://doi.org/10.1145/2435204.2435207) | ---
TOS'14 | STAIR Codes: A General Family of Erasure Codes for Tolerating Device and Sector Failures. | [Link](https://doi.org/10.1145/2658991) | ---
TOS'14 | Sector-Disk (SD) Erasure Codes for Mixed Failure Modes in RAID Systems. | [Link](https://dl.acm.org/doi/10.1145/2560013) | ---
TOS'15 | Low-Complexity Implementation of RAID Based on Reed-Solomon Codes. | [Link](https://dl.acm.org/doi/10.1145/2700308) | ---
TOS'17 | High-Performance General Functional Regenerating Codes with Near-Optimal Repair Bandwidth. | [Link](https://dl.acm.org/doi/10.1145/3051122) | ---
TOS'17 | Optimal Repair Layering for Erasure-Coded Data Centers: From Theory to Practice. | [Link](https://doi.org/10.1145/3149349) | ---
TOS'17 | Systematic Erasure Codes with Optimal Repair Bandwidth and Storage. | [Link](https://doi.org/10.1145/3109479) | ---
TOS'20 | On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes. | [Link](https://doi.org/10.1145/3381832) | ---
TOS'20 | Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques. | [Link](https://doi.org/10.1145/3375554) | ---
TOS'20 | PBS: An Efficient Erasure-Coded Block Storage System Based on Speculative Partial Writes. | [Link](https://doi.org/10.1145/3365839) | ---
--- | --- | --- | ---


#### RAID

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'05 | Improving storage system availability with D-GRAID. | [Link](https://doi.org/10.1145/1063786.1063787) | ---
TOS'05 | Reliability and security of RAID storage systems and D2D archives using SATA disk drives. | [Link](https://doi.org/10.1145/1044956.1044961) | ---
TOS'07 | PARAID: A gear-shifting power-aware RAID. | [Link](https://dl.acm.org/doi/10.1145/1288783.1289721) | ---
TOS'08 | A new intra-disk redundancy scheme for high-reliability RAID storage systems in the presence of unrecoverable errors. | [Link](https://dl.acm.org/doi/10.1145/1353452.1353453) | ---
TOS'09 | Higher reliability redundant disk arrays: Organization, operation, and coding. | [Link](https://dl.acm.org/doi/10.1145/1629075.1629076) | ---
TOS'10 | Differential RAID: Rethinking RAID for SSD reliability. | [Link](https://dl.acm.org/doi/10.1145/1807060.1807061) | ---
TOS'11 | A Hybrid Approach to Failed Disk Recovery Using RAID-6 Codes: Algorithms and Performance Evaluation. | [Link](https://dl.acm.org/doi/10.1145/2027066.2027071) | ---
TOS'11 | Minimum density RAID-6 codes. | [Link](https://doi.org/10.1145/1970338.1970341) | ---
TOS'11 | Online availability upgrades for parity-based RAIDs through supplementary parity augmentations. | [Link](https://doi.org/10.1145/1970338.1970340) | ---
TOS'11 | Reducing Repair Traffic in P2P Backup Systems: Exact Regenerating Codes on Hierarchical Codes. | [Link](https://doi.org/10.1145/2027066.2027070) | ---
TOS'11 | Disk Scrubbing Versus Intradisk Redundancy for RAID Storage Systems. | [Link](https://doi.org/10.1145/1970348.1970350) | ---
TOS'14 | Beyond MTTDL: A Closed-Form RAID 6 Reliability Equation. | [Link](https://doi.org/10.1145/2577386) | ---
TOS'15 | RAIDShield: Characterizing, Monitoring, and Proactively Protecting Against Disk Failures. | [Link](https://doi.org/10.1145/2820615) | ---
TOS'15 | An Energy-Efficient and Reliable Storage Mechanism for Data-Intensive Academic Archive Systems. | [Link](https://doi.org/10.1145/2720021) | ---
TOS'15 | Rebuttal to “Beyond MTTDL: A Closed-Form RAID-6 Reliability Equation”. | [Link](https://doi.org/10.1145/2700311) | ---
TOS'16 | LoneStar RAID: Massive Array of Offline Disks for Archival Systems. | [Link](https://doi.org/10.1145/2840810) | ---
TOS'16 | H-Scale: A Fast Approach to Scale Disk Arrays via Hybrid Stripe Deployment. | [Link](https://dl.acm.org/doi/10.1145/2822895) | ---
TOS'19 | Determining Data Distribution for Large Disk Enclosures with 3-D Data Templates. | [Link](https://doi.org/10.1145/3342858) | RAID+
--- | --- | --- | ---


#### Data Placement

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'14 | Random Slicing: Efficient and Scalable Data Placement for Large-Scale Storage Systems. | [Link](https://doi.org/10.1145/2632230) | ---
--- | --- | --- | ---


#### Flash-memory

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'18 | An Analysis of Flash Page Reuse With WOM Codes. | [Link](https://doi.org/10.1145/3177886) | ---
--- | --- | --- | ---


#### Backup

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'12 | Efficient cooperative backup with decentralized trust management. | [Link](https://doi.org/10.1145/2339118.2339119) | ---
--- | --- | --- | ---


#### Storage System

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'05 | DISP: Practical, efficient, secure and fault-tolerant distributed data storage. | [Link](https://doi.org/10.1145/1044956.1044960) | ---
TOS'09 | POTSHARDS—a secure, recoverable, long-term archival storage system. | [Link](https://doi.org/10.1145/1534912.1534914) | ---
TOS'11 | PRESIDIO: A Framework for Efficient Archival Data Storage. | [Link](https://doi.org/10.1145/1970348.1970351) | ---
TOS'13 | DepSky: Dependable and Secure Storage in a Cloud-of-Clouds. | [Summary](/posts/2019/07/paper-reading-depsky-eurosys11/) | ---
TOS'17 | Hybris: Robust Hybrid Cloud Storage. | [Summary](/posts/2021/02/paper-reading-racs-socc14/) | ---
TOS'17 | Redundancy Does Not Imply Fault Tolerance: Analysis of Distributed Storage Reactions to File-System Faults. | [Link](https://dl.acm.org/doi/10.1145/3125497) | ---
TOS'19 | Liquid Cloud Storage. | [Link](https://doi.org/10.1145/3281276) | ---
TOS'20 | The Case for Custom Storage Backends in Distributed Storage Systems. | [Link](https://doi.org/10.1145/3386362) | ---
--- | --- | --- | ---


#### KV-Store

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'17 | Efficient and Available In-Memory KV-Store with Hybrid Erasure Coding and Replication. | [Link](https://doi.org/10.1145/3129900) | ---
--- | --- | --- | ---


#### Benchmark

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'07 | Understanding disk failure rates: What does an MTTF of 1,000,000 hours mean to you?. | [Link](https://doi.org/10.1145/1288783.1288785) | ---
TOS'08 | A nine year study of file system and storage benchmarking. | [Link](https://dl.acm.org/doi/10.1145/1367829.1367831) | ---
--- | --- | --- | ---


#### Techniques

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'12 | Efficient software implementations of large finite fields GF(2n) for secure storage applications. | [Link](https://doi.org/10.1145/2093139.2093141) | ---
TOS'16 | Tools for Predicting the Reliability of Large-Scale Storage Systems. | [Link](https://doi.org/10.1145/2911987) | ---
--- | --- | --- | ---


#### File System

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
TOS'14 | A Study of Linux File System Evolution. | [Link](https://doi.org/10.1145/2560012) | ---
TOS'20 | Everyone Loves File: Oracle File Storage Service. | [Link](https://doi.org/10.1145/3377877) | ---
--- | --- | --- | ---


## SEC (Symposium on Edge Computing) Paper List

Venue | Title | Link / Summary | Brief
--- | --- | --- | ---
SEC’17 | EdgeCourier: An Edge-hosted Personal Service for Low-bandwidth Document Synchronization in Mobile Cloud Storage Services | --- | ---
SEC’17 | CloudPath: A Multi-Tier Cloud Computing Framework | --- | ---
SEC’17 | LAVEA: Latency-aware Video Analytics on Edge Computing Platform | --- | ---
SEC’17 | Fast Transparent Virtual Machine Migration in Distributed Edge Clouds | --- | ---
SEC’17 | A Vehicle-based Edge Computing Platform for Transit and Human Mobility Analytics | --- | ---
SEC’18 | VideoEdge: Processing Camera Streams using Hierarchical Clusters | --- | ---
SEC’18 short | Extend Cloud to Edge with KubeEdge | --- | ---
SEC’19 | Sandpaper: mitigating performance interference in CDN edge proxies | --- | ---
SEC’19 | Real-time traffic estimation at vehicular edge nodes | --- | ---
SEC’19 | Infrastructure fault detection and prediction in edge cloud environments | --- | ---
SEC’19 | Why cloud applications are not ready for the edge (yet) | --- | ---
--- | --- | --- | ---
