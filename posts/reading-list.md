## About

My reading list includes papers, articles, books, tutorials, videos, etc. for
research purposes. Items are characterized by their topics/keywords.

---


## Table of Contents

[TOC]


## Recent

[SDN](#software-defined-network-sdn)

## Categories

### Networking

#### Software Defined Network (SDN)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
Book | Software-Defined-Networks: A Systems Approach | Reading notes: [Ch.1](/posts/readings/book/sdn-system/sdn-system-ch1), [Ch.2](/posts/readings/book/sdn-system/sdn-system-ch2), [Ch.3](/posts/readings/book/sdn-system/sdn-system-ch3), [Ch.4](/posts/readings/book/sdn-system/sdn-system-ch4), [Ch.5](/posts/readings/book/sdn-system/sdn-system-ch5), [Ch.6](/posts/readings/book/sdn-system/sdn-system-ch6), [Ch.7](/posts/readings/book/sdn-system/sdn-system-ch7) | SDN Book
SIGCOMM'18 | B4: Experience with a Globally-Deployed Software Defined WAN. | [Summary](/posts/readings/paper/sigcomm/sigcomm18b4/) (Not done) | B4
NSDI'14 | Network Virtualization in Multi-tenant Datacenters. | [Summary](/posts/readings/paper/nsdi/nsdi14virtualization/) (Not done) | Network Virtualization
SIGCOMM'13 | Achieving High Utilization with Software-Driven WAN. | [Summary](/posts/readings/paper/sigcomm/sigcomm13wan/) (Not done) | Software-Driven WAN
SIGCOMM'08 | OpenFlow: Enabling Innovation in Campus Networks. | [Summary](/posts/readings/paper/sigcomm/sigcomm08openflow/) (Not done) | OpenFlow


### Erasure Coding

#### Basics

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SIAM'1960 | Polynomial Codes Over Certain Finite Fields. | [Summary](/posts/2021/06/paper-reading-rs-siam1960/) | RS code original. MUST-READ
Manuscript | An Introduction to Galois Fields and Reed-Solomon Coding | [link](https://people.cs.clemson.edu/~westall/851/rs-code.pdf) | Into to Finite Field and RS code (communication) in Clemenson
Manuscript | Reed-Solomon Codes | [link](https://courses.cs.duke.edu//spring10/cps296.3/rs_scribe.pdf) | Intro to RS code from Duke Univ.
Summary | Concepts that must know | [Summary](/posts/2021/07/blogs-ec-basic-concepts/) | EC basic Concepts and keywords
FAST'09 | A Performance Evaluation and Examination of Open-Source Erasure Coding Libraries For Storage. | [Summary](/posts/2020/08/paper-reading-plank-fast09/) | Plank EC eval
USENIX Login'13 | Erasure Codes for Storage Systems: A Brief Primer. | [Summary](/posts/2020/08/paper-reading-plank-usenixlogin13/) | Plank EC basics
FAST Tutorial'13 | Tutorial: Erasure Coding for Storage Systems. | [Summary](/posts/2020/08/docs-reading-plank-tutorial-fast13/) | Plank EC tutorial


#### Erasure Codes

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
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


#### Network Coding and Regenerating Codes

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
FAST'11 Poster | Repairing Erasure Codes. | [Link](https://www.usenix.org/legacy/event/fast11/posters_files/Papailiopoulos.pdf) | NC for storage poster
IEEE Survey'11 | A Survey on Network Codes. | [Summary](/posts/2021/06/paper-reading-ncstoragesurvey-ieeesurvery/) | NC for storage survey
TIT'10 | Network Coding for Distributed Storage Systems. | [Summary](/posts/2020/08/paper-reading-ncstorage-tit10/) | network coding for storage, [video](https://www.youtube.com/watch?v=RMRyP6JRKGk), [report](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory-au14/projects/codes-DSS-report.pdf)
PPT | Intro to regenrating codes | [link](https://ewh.ieee.org/r6/scv/mag/MtgSum/Meeting2017_05_2_presentation.pdf) | ---

#### Redundancy Transitioning

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
OSDI'22 | Tiger: disk-adaptive redundancy without placement restrictions | [Summary](/posts/readings/paper/osdi/osdi22-tiger) | Tiger (Rashmi)
ISIT'22 | Bandwidth Cost of Code Conversions in the Split Regime | :---: | Convertible codes under split regime (Rashmi)
INFOCOM'22 | Optimal Data Placement for Stripe Merging in Locally Repairable Codes. | [Summary](/posts/readings/paper/infocom/infocom22-lrc) | LRC stripe merging (Wu) (LRC transition bandwidth)
ISIT'21 | Bandwidth Cost of Code Conversions in Distributed Storage: Fundamental Limits and Optimal Constructions | :---: | Convertible codes: bandwidth (Rashmi)
ICDCS'21 | StripeMerge: Efficient Wide-Stripe Generation for Large-Scale Erasure-Coded Storage. | [Summary](/posts/readings/paper/icdcs/icdcs21-stripemerge) | StripeMerge (Yao)
OSDI'20 | Pacemaker: avoiding HeART attacks in storage clusters with disk-adaptive redundancy | [Summary](/posts/readings/paper/osdi/osdi20-pacemaker) | PaceMaker (Rashmi)
SRDS'20 | Enabling I/O-Efficient Redundancy Transitioning in Erasure-Coded KV Stores via Elastic Reed-Solomon Codes. | [Summary](/posts/readings/paper/srds/srds20-elastic-rs) | Elastic RS (Wu)
INFOCOM'20 | On the Optimal Repair-Scaling Trade-off in Locally Repairable Codes. | [Summary](/posts/readings/paper/infocom/infocom20-lrc-tradeoff) | LRC Repair-Scaling Tradeoff (Wu)
IEEE Access'20 | Efficient Storage Scaling for MBR and MSR Codes | [Summary](/posts/readings/paper/ieeeaccess/ieeeaccess20-rc-scaling) | MSR scaling (Zhang)
ITCS'20 | Convertible Codes: New Class of Codes for Efficient Conversion of Coded Data in Distributed Storage | [Summary](/posts/readings/paper/itcs/itcs20-convertible-codes) | Convertible Codes (Rashmi)
ISIT'20 | Access-optimal Linear MDS Convertible Codes for All Parameters | [Summary](/posts/readings/paper/isit/isit20-access-optimal-convertible-codes) | Access-optimal Convertible Codes (Rashmi)
FAST'19 | Cluster storage systems gotta have HeART: improving storage efficiency by exploiting disk-reliability heterogeneity | [Summary](/posts/readings/paper/fast/fast19-heart) | HeART (Rashmi)
SoCC'19 | Coupling Decentralized Key-Value Stores with Erasure Coding | [Summary](/posts/readings/paper/socc/socc19-echash) | ECHash (Hu) (Optimizing scaling throughput for KVStore)
ISIT'18 | Generalized Optimal Storage Scaling via Network Coding | [Summary](/posts/readings/paper/isit/isit18-nc-scaling) | Scaling via Network Coding (Hu)
INFOCOM'18 | Toward Optimal Storage Scaling via Network Coding: From Theory to Practice | [Summary](/posts/readings/paper/infocom/infocom18-ncscale) | NCScale (Hu) (storage scaling)
TPDS'16 | I/O-Efficient Scaling Schemes for Distributed Storage Systems with CRS Codes | :---: | CRS Scaling (Wu)
DSN'15, TPDS'17 | Enabling Efficient and Reliable Transition from Replication to Erasure Coding for Clustered File Systems. | :---: | Rep to EC Transition (Li Runhui)
FAST'15 | A Tale of Two Erasure Codes in HDFS | [Summary](/posts/2020/09/paper-reading-twoec-fast15/) | A tale of two erasure codes
TC'15 | Accelerate RDP RAID-6 Scaling by Reducing Disk I/Os and XOR Operations | :---: | RDP RAID-6 Scaling (Zhang)
TPDS'14 | An Efficient Scaling Scheme for RS-Coded Storage Clusters | [Summary](/posts/readings/paper/tpds/tpds14-scalers) | Scale-RS (Huang) (RS scaling)
ICPP'12 | GSR: A Global Stripe-Based Redistribution Approach to Accelerate RAID-5 Scaling | :---: | GSR RAID-5 Scaling (C. Wu)
FAST'11 | Accelerate RAID Scaling by Minimizing Data Migration | :---: | FastScale (Zheng)


#### Data Placement

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ICPP'22 | Repair-Optimal Data Placement for Locally Repairable Codes with Optimal Minimum Hamming Distance | [Summary](/posts/readings/paper/icpp/icpp22-optimallrc) | LRC (Wu)

#### Reliability Analysis

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SNAPI'07| Outshining Mirrors: MTTDL of Fixed-Order SSPiRAL Layouts | [Link](http://www2.cs.uh.edu/~paris/MYPAPERS/Snapi07.pdf) | ---
I2TS'08 | When MTTDLs Are Not Good Enough: Providing Better Estimates of Disk Array Reliability  | [Link](https://www.cse.scu.edu/~tschwarz/Papers/i2ts08.pdf) | ---
HotStorage'10 | Mean time to meaningless: MTTDL, Markov models, and storage system reliability | [Link](https://www.usenix.org/legacy/event/hotstorage10/tech/full_papers/Greenan.pdf) | MTTDL Meaningless
Summary | Reliability Analysis: MTTDL | [Summary](/posts/2021/07/blogs-mttdl/) | Calculation of MTTDL


#### Techniques

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
MSST’12 | On the speedup of single-disk failure recovery in XOR-coded storage systems: Theory and practice. | [Summary](/posts/2020/09/paper-reading-zhu-replace-recovery-msst12/) | Zhu
FAST'15 | A Tale of Two Erasure Codes in HDFS. | [Summary](/posts/2020/09/paper-reading-twoec-fast15/) | ---
OSDI'16 | EC-Cache: Load-Balanced, Low-Latency Cluster Caching with Online Erasure Coding. | [Summary](/posts/2021/02/paper-reading-eccache-osdi16/) | Rashmi, EC-Cache
Eurosys'16 | Partial-Parallel-Repair (PPR): A Distributed Technique for Repairing Erasure Coded Storage. | [Summary](/posts/2020/08/paper-reading-ppr-eurosys16/) | PPR
ATC'17 | Repair Pipelining for Erasure-Coded Storage. | [Summary](/posts/2020/08/paper-reading-repair-pipelining-atc17/) | ECPipe
DSN'19 | Fast Predictive Repair in Erasure-Coded Storage. | [Summary](/posts/2020/08/paper-reading-fpr-dsn19/) | FastPR
FAST'19 | Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques. | [Summary](/posts/2020/08/paper-reading-ec-acceleration-fast19/) | EC Acceleraion
Eurosys'20 | RAIDP: replication with intra-disk parity. | [Summary](/posts/2020/08/paper-reading-raidp-eurosys20/) | RAID-P
IWQoS'21 | EC-Scheduler: A Load-Balanced Scheduler to Accelerate the Straggler Recovery for Erasure Coded Storage Systems | [Summary](/posts/readings/paper/iwqos/iwqos21-ecscheduler) | EC repair, load balancing, heterogeneous



#### Systems

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
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


### Edge

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
HotEdge'20 | Sharing and Caring of Data at the Edge. | [Summary](/posts/2021/02/paper-reading-sharing-hotedge20/) | edge storage survey
JPDC'20 | EdgeKV: Decentralized, scalable, and consistent storage for the edge. | [Summary](/posts/2021/06/paper-reading-edgekv-jpdc20/) | EdgeKV


* [SEC Paper List](#sec--symposium-on-edge-computing--paper-list)


### Deduplication

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'15 | Toward Reliable, Secure, and Cost-Efficient Cloud Storage via Convergent Dispersal. | [Summary](/posts/2019/06/paper-reading-cdstore/) | CDStore


### Consensus

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'14 | In Search of an Understandable Consensus Algorithm. | [Summary](/posts/2019/07/paper-reading-raft-atc14/) | Raft


### Stream Processing

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ICDCS'20 | Toward Adaptive Disk Failure Prediction via Stream Mining. | [Summary](/posts/2020/08/paper-reading-streamdfp-icdcs20/) | StreamDFP


### Network Measurement

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SIGCOMM'18 | SketchLearn: Relieving User Burdens in Approximate Measurement with Automated Statistical Inference. | [Summary](/posts/2020/08/paper-reading-sketchlearn-sigcomm18/) | SketchLearn


### Graph Processing

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
OSDI'16 | Gemini: A Computation-Centric Distributed Graph Processing System. | [Summary](/posts/2020/09/paper-reading-gemini-osdi16/) | Gemini
SIGMOD'19 | Nanosecond Indexing of Graph Data With Hash Maps and VLists. | [Summary](/posts/2020/09/paper-reading-nanosecond-sigmod19/) | Nanosecond


### Scheduling

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SOSP'1973 | Polynomial Complete Scheduling Problems | [Summary](/posts/readings/paper/sosp/sosp1973-scheduling) | Scheduling proof
COMMACM'1974 | Scheduling independent tasks to reduce mean finishing time | [Summary](/posts/readings/paper/commacm/commacm1974-scheduling) | Scheduling algorithms
JACM'1976 | Exact and Approximate Algorithms for Scheduling Nonidentical Processors | [Summary](/posts/readings/paper/jacm/jacm1976-scheduling) | Scheduling algorithms
JACM'1977 | Heuristic Algorithms for Scheduling Independent Tasks on Nonidentical Processors | [Summary](/posts/readings/paper/jacm/jacm1977-scheduling) | Performance analysis on scheduling heuristics
MP'1990 | Approximation Algorithms for Scheduling Unrelated Parallel Machines | [Summary](/posts/readings/paper/mp/mp1990-scheduling) | Scheduling algorithms and proofs


### Bipartite Graph

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
JALG'06 | Semi-matchings for bipartite graphs and load balancing | [Summary](/posts/readings/paper/jalg/jalg05-semi-matching) | Semi-matching on unweighted bipartite
IPL'06 | An approximation algorithm for the load-balanced semi-matching problem in weighted bipartite graphs | [Summary](/posts/readings/paper/ipl/ipl06-semi-matching) | Semi-matching for jobs with identical processing times
IPL'09 | A note on "An approximation algorithm for the load-balanced semi-matching problem in weighted bipartite graphs" | [Summary](/posts/readings/paper/ipl/ipl09-semi-matching-correction) | Corrections of bounds for IPL'06
IPSJ'07 | Optimal Balanced Semi-Matchings for Weighted Bipartite Graphs | [Summary](/posts/readings/paper/ipsj/ipsj07-matching) | Optimal Semi-matching proof



### TOS (Transaction on Storage) Paper List

#### Erasure Coding

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
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


#### RAID

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
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


#### Data Placement

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'14 | Random Slicing: Efficient and Scalable Data Placement for Large-Scale Storage Systems. | [Link](https://doi.org/10.1145/2632230) | ---


#### Flash-memory

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'18 | An Analysis of Flash Page Reuse With WOM Codes. | [Link](https://doi.org/10.1145/3177886) | ---


#### Backup

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'12 | Efficient cooperative backup with decentralized trust management. | [Link](https://doi.org/10.1145/2339118.2339119) | ---


#### Storage System

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'05 | DISP: Practical, efficient, secure and fault-tolerant distributed data storage. | [Link](https://doi.org/10.1145/1044956.1044960) | ---
TOS'09 | POTSHARDS—a secure, recoverable, long-term archival storage system. | [Link](https://doi.org/10.1145/1534912.1534914) | ---
TOS'11 | PRESIDIO: A Framework for Efficient Archival Data Storage. | [Link](https://doi.org/10.1145/1970348.1970351) | ---
TOS'13 | DepSky: Dependable and Secure Storage in a Cloud-of-Clouds. | [Summary](/posts/2019/07/paper-reading-depsky-eurosys11/) | ---
TOS'17 | Hybris: Robust Hybrid Cloud Storage. | [Summary](/posts/2021/02/paper-reading-racs-socc14/) | ---
TOS'17 | Redundancy Does Not Imply Fault Tolerance: Analysis of Distributed Storage Reactions to File-System Faults. | [Link](https://dl.acm.org/doi/10.1145/3125497) | ---
TOS'19 | Liquid Cloud Storage. | [Link](https://doi.org/10.1145/3281276) | ---
TOS'20 | The Case for Custom Storage Backends in Distributed Storage Systems. | [Link](https://doi.org/10.1145/3386362) | ---


#### KV-Store

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'17 | Efficient and Available In-Memory KV-Store with Hybrid Erasure Coding and Replication. | [Link](https://doi.org/10.1145/3129900) | ---


#### Benchmark

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'07 | Understanding disk failure rates: What does an MTTF of 1,000,000 hours mean to you?. | [Link](https://doi.org/10.1145/1288783.1288785) | ---
TOS'08 | A nine year study of file system and storage benchmarking. | [Link](https://dl.acm.org/doi/10.1145/1367829.1367831) | ---


#### Techniques

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'12 | Efficient software implementations of large finite fields GF(2n) for secure storage applications. | [Link](https://doi.org/10.1145/2093139.2093141) | ---
TOS'16 | Tools for Predicting the Reliability of Large-Scale Storage Systems. | [Link](https://doi.org/10.1145/2911987) | ---


#### File System

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'14 | A Study of Linux File System Evolution. | [Link](https://doi.org/10.1145/2560012) | ---
TOS'20 | Everyone Loves File: Oracle File Storage Service. | [Link](https://doi.org/10.1145/3377877) | ---


### SEC (Symposium on Edge Computing) Paper List

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
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
