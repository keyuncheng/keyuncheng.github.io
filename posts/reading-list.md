## About

My reading list includes papers, articles, books, tutorials, videos, etc. for
research purposes. Items are characterized by their topics/keywords.

---


## Table of Contents

[TOC]


## Recent

[Blockchain](#blockchain)

## Categories


### Erasure Coding

#### Erasure Coding (basics)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
Summary | Concepts that must know | [Summary](/posts/2021/07/blogs-ec-basic-concepts/) | EC basic concepts and keywords
Manuscript | An Introduction to Galois Fields and Reed-Solomon Coding | [Link](https://people.cs.clemson.edu/~westall/851/rs-code.pdf) | Intro to Finite Field and RS code (communication) in Clemenson Univ.
Manuscript | Reed-Solomon Codes | [Link](https://courses.cs.duke.edu//spring10/cps296.3/rs_scribe.pdf) | Intro to RS codes from Duke Univ.
USENIX Login'13 | Erasure Codes for Storage Systems: A Brief Primer | [Summary](/posts/2020/08/paper-reading-plank-usenixlogin13/) | Plank EC basics
FAST Tutorial'13 | Tutorial: Erasure Coding for Storage Systems | [Summary](/posts/2020/08/docs-reading-plank-tutorial-fast13/) | Plank, EC tutorial
FAST'09 | A Performance Evaluation and Examination of Open-Source Erasure Coding Libraries For Storage | [Summary](/posts/2020/08/paper-reading-plank-fast09/) | Plank, EC computation evaluation


#### Network Coding (basics)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
FAST'11 Poster | Repairing Erasure Codes | [Link](https://www.usenix.org/legacy/event/fast11/posters_files/Papailiopoulos.pdf) | Network coding for storage (poster)
IEEE Survey'11 | A Survey on Network Codes | [Summary](/posts/2021/06/paper-reading-ncstoragesurvey-ieeesurvery/) | Network coding for storage (survey)
TIT'10 | Network Coding for Distributed Storage Systems | [Summary](/posts/2020/08/paper-reading-ncstorage-tit10/) | Network coding for storage [video](https://www.youtube.com/watch?v=RMRyP6JRKGk), [report](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory-au14/projects/codes-DSS-report.pdf)
PPT | Regenerating codes for distributed storage | [Link](https://ewh.ieee.org/r6/scv/mag/MtgSum/Meeting2017_05_2_presentation.pdf) | Network Coding, intro


#### Erasure Codes

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
FAST'23 | Practical Design Considerations for Wide Locally Recoverable Codes (LRCs) | [Summary](/posts/readings/paper/fast/fast23-uniform-cauchy-lrc) | Uniform Cauchy LRC, wide stripe, LRC
SRDS'22 | XHR-Code: An Efficient Wide Stripe Erasure Code to Reduce Cross-Rack Overhead in Cloud Storage Systems | [Summary](/posts/readings/paper/srds/srds22-xhr-code) | XHR-Code, repair, wide stripe, hierarchical settings, multiple failures
MSST'19 | AZ-Code: An Efficient Availability Zone Level Erasure Code to Provide High Fault Tolerance in Cloud Storage Systems | [Link](https://ieeexplore.ieee.org/document/8890228) | AZ-Code
ISIT'18 | Codes with Combined Locality and Regeneration Having Optimal Rate, dmin and Linear Field Size | [Link](https://dl.acm.org/doi/10.1109/ISIT.2018.8437455) | Local Regenerating Codes, LRC, regenerating codes
DSN'18 | Alpha Entanglement Codes: Practical Erasure Codes to Archive Data in Unreliable Environments | [Link](https://ieeexplore.ieee.org/document/8416482) | Alpha Entanglement Codes, multiple failures
ATC'18 | On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes | [Summary](/posts/readings/paper/atc/atc18-lrc-comparison) | LRC,  comparison, Ceph
FAST'18 | RAID+: Deterministic and Balanced Data Distribution for Large Disk Enclosures | [Link](https://www.usenix.org/conference/fast18/presentation/zhang) | RAID+, load balancing
FAST’18 | Clay Codes: Moulding MDS Codes to Yield an MSR Code | [Summary](/posts/2020/08/paper-reading-clay-codes-fast18/) | Clay codes, MSR codes
TIT'17 | Explicit constructions of high-rate MDS array codes with optimal repair bandwidth | [Link](https://ieeexplore.ieee.org/document/7990181) | Ye-Barg codes, MSR codes
ISIT'16 | Double Regenerating Codes for hierarchical data centers | [Link](https://ieeexplore.ieee.org/document/7541298) | DRC, MSR codes, hierarchical settings
STOC'16 | Repairing Reed-solomon codes | [Link](https://dl.acm.org/doi/10.1145/2897518.2897525) | RS codes, repair, sub-packetization
FAST’16 | Opening the Chrysalis: On the Real Repair Performance of MSR Codes | [Summary](/posts/2020/08/paper-reading-butterfly-codes-fast16/) | Butterfly codes, MSR codes
FAST'15 | Having Your Cake and Eating It Too: Jointly Optimal Erasure Codes for I/O, Storage, and Network-bandwidth | [Summary](/posts/2020/08/paper-reading-rashmi-pm-rbt-fast15/) | PM-RBT codes, MSR codes
TOS'14 | Sector-Disk (SD) Erasure Codes for Mixed Failure Modes in RAID Systems | [Link](https://dl.acm.org/doi/10.1145/2560013) | Sector-Disk (SD) codes, sector-disk failures
TIT'14 | A family of optimal locally recoverable codes | [Summary](/posts/2020/09/paper-reading-optimal-lrc-tit14/) | Optimal LRCs, LRC
TIT'14 | Locally Repairable Codes | [Link](https://ieeexplore.ieee.org/abstract/document/6818438) | LRC
TIT'14 | Codes With Local Regeneration and Erasure Correction | [Summary](posts/readings/paper/tit/tit14-lrc-rc) | Local Regenerating Codes, LRC, multiple failures
TIT'14 | Repair locality with multiple erasure tolerance | [Link](https://ieeexplore.ieee.org/iel7/18/4667673/06882150.pdf) | LRC, multiple failures
SIGCOMM’14 | A “Hitchhiker’s” Guide to Fast and Efficient Data Reconstruction in Erasure-coded Data Centers | [Summary](/posts/2020/08/paper-reading-rashmi-hitchhikker-sigcomm14/) | Hitchhikker codes, regenerating codes, piggybacking codes
FAST'14 | STAIR Codes: A General Family of Erasure Codes for Tolerating Device and Sector Failures in Practical Storage Systems | [Summary](/posts/2020/08/paper-reading-staircodes-fast14/) | STAIR Codes, sector-disk failures
PVLDB'13 | XORing Elephants: Novel Erasure Codes for Big Data | [Summary](/posts/readings/paper/pvldb/pvldb13-xorbas) | Xorbas codes, LRC
HotStorage'13 | A Solution to the Network Challenges of Data Recovery in Erasure-coded Distributed Storage Systems: A Study on the Facebook Warehouse Cluster | [Link](https://www.usenix.org/conference/hotstorage13/workshop-program/presentation/rashmi) | Piggybacking codes
TIT'13 | Zigzag Codes: MDS Array Codes With Optimal Rebuilding | [Link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6352912) | Zigzag Codes, regenerating codes
ISIT'13, TIT'17 | A Piggybacking Design Framework for Read-and Download-efficient Distributed Storage Codes | [Link](https://ieeexplore.ieee.org/document/7949040) | Piggybacking codes
TOS'12 | Generalized X-code: An efficient RAID-6 code for arbitrary size of disk array | [Summary](/posts/2020/10/paper-reading-generalized-x-code-tos12/) | Generalized X-codes
TIT'12 | On the Locality of Codeword Symbols | [Link](/posts/readings/paper/tit/tit12-lrc) | Theory of LRCs
ATC'12 | Erasure Coding in Windows Azure Storage | [Summary](/posts/readings/paper/atc/atc12-azurelrc) | Azure-LRC
INFOCOM'12 | Simple regenerating codes: Network coding for cloud storage | [Link](https://ieeexplore.ieee.org/document/6195703) | Simple regenerating code
ISIT'10, TIT'11 | Optimal Exact-Regenerating Codes for Distributed Storage at the MSR and MBR Points via a Product-Matrix Construction | [Link](https://ieeexplore.ieee.org/document/5961826) | Product-Matrix Code
TOS'09 | GRID codes: Strip-based erasure codes with high fault tolerance for storage systems | [Summary](/posts/2020/10/paper-reading-grid-codes-tos09/) | GRID codes
NCA'07 | Pyramid Codes: Flexible Schemes to Trade Space for Access Efficiency in Reliable Data Storage Systems | [Summary](/posts/readings/paper/nca/nca07-pyramid-codes), [Summary (older, for TOS'13)](/posts/2020/09/paper-reading-pyramid-codes-tos13/) | Pyramid Codes, LRC
FAST'04 | Improving Storage System Availability with D-GRAID | [Link](https://www.usenix.org/conference/fast-04/improving-storage-system-availability-d-graid) | D-GRAID codes, RAID
FAST'04 | Row-Diagonal Parity for Double Disk Failure Correction | [Link](https://www.usenix.org/conference/fast-04/row-diagonal-parity-double-disk-failure-correction#:~:text=Row%2DDiagonal%20Parity%20(RDP),both%20during%20construction%20and%20reconstruction.) | RDP codes, array codes, RAID
ATC'1996 | AFRAID - A Frequently Redundant Array of Independent Disks | [Link](https://www.usenix.org/legacy/publications/library/proceedings/sd96/full_papers/wilkes.pdf) | AFRAID, RAID
ISCA'1994, TC'1995 | EVENODD: an optimal scheme for tolerating double disk failures in RAID architectures | [Link](https://dl.acm.org/doi/10.1145/191995.192033) | EVENODD codes, array codes, RAID
SIGMOD'1988 | A Case for Redundant Arrays of Inexpensive Disks (RAID) | [Link](https://dl.acm.org/doi/10.1145/50202.50214) | RAID
SIGMETRICS Perf Eval. Review'1995 | Striping in a RAID level 5 disk array | [Link](https://dl.acm.org/doi/10.1145/223586.223603) | RAID striping, RAID
SIAM'1960 | Polynomial Codes Over Certain Finite Fields | [Summary](/posts/2021/06/paper-reading-rs-siam1960/) | RS codes (the original version)
Monograph from Prof. P. Vijay Kumar | Codes for Distributed Storage | [Link](https://ece.iisc.ac.in/~pvkece/pdfs/CDS_as_Published_FnT.pdf) | EC theory basics and survey (including RS, MSR, LRC, etc.) 



#### Redundancy Transitioning

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ISIT'23 | Locally Repairable Convertible Codes: Erasure Codes for Efficient Repair and Conversion | [Summary](/posts/readings/paper/isit/isit23-lrc-conversion) | LRC conversion, code conversion, LRC
OSDI'22 | Tiger: disk-adaptive redundancy without placement restrictions | [Summary](/posts/readings/paper/osdi/osdi22-tiger) | Tiger, redundancy transitioning, disk heterogeneity
ISIT'22 | Bandwidth Cost of Code Conversions in the Split Regime | [Link](https://arxiv.org/abs/2205.06793) | Convertible codes: bandwidth, code conversion, theory
ISIT'21, TIT'23 | Bandwidth Cost of Code Conversions in Distributed Storage: Fundamental Limits and Optimal Constructions | [Link](https://ieeexplore.ieee.org/document/10097511) | Convertible codes: bandwidth, code conversion, theory
INFOCOM'22 | Optimal Data Placement for Stripe Merging in Locally Repairable Codes | [Summary](/posts/readings/paper/infocom/infocom22-lrc) | LRC stripe merging, code conversion, LRC
ICDCS'21 | StripeMerge: Efficient Wide-Stripe Generation for Large-Scale Erasure-Coded Storage | [Summary](/posts/readings/paper/icdcs/icdcs21-stripemerge) | StripeMerge, wide stripe, code conversion
OSDI'20 | Pacemaker: avoiding HeART attacks in storage clusters with disk-adaptive redundancy | [Summary](/posts/readings/paper/osdi/osdi20-pacemaker) | PACEMAKER, redundancy transitioning, disk heterogeneity
SRDS'20 | Enabling I/O-Efficient Redundancy Transitioning in Erasure-Coded KV Stores via Elastic Reed-Solomon Codes | [Summary](/posts/readings/paper/srds/srds20-elastic-rs) | Elastic Reed-Solomon (ERS) codes, redundancy trasntioning
INFOCOM'20 | On the Optimal Repair-Scaling Trade-off in Locally Repairable Codes | [Summary](/posts/readings/paper/infocom/infocom20-lrc-tradeoff) | LRC Repair-Scaling Tradeoff, redundancy transitioning, LRC
IEEE Access'20 | Efficient Storage Scaling for MBR and MSR Codes | [Summary](/posts/readings/paper/ieeeaccess/ieeeaccess20-rc-scaling) | MSR codes, scaling
ITCS'20, TIT'22 | Convertible Codes: New Class of Codes for Efficient Conversion of Coded Data in Distributed Storage | [Summary](/posts/readings/paper/itcs/itcs20-convertible-codes) | Convertible Codes: I/O, code conversion
ISIT'20 | Access-optimal Linear MDS Convertible Codes for All Parameters | [Summary](/posts/readings/paper/isit/isit20-access-optimal-convertible-codes) | Access-optimal Convertible Codes
FAST'19 | Cluster storage systems gotta have HeART: improving storage efficiency by exploiting disk-reliability heterogeneity | [Summary](/posts/readings/paper/fast/fast19-heart) | HeART, disk heterogeneity, redundancy transitioning
ISIT'18 | Generalized Optimal Storage Scaling via Network Coding | [Summary](/posts/readings/paper/isit/isit18-nc-scaling) | Network coding, scaling
INFOCOM'18, TPDS'22 | Toward Optimal Storage Scaling via Network Coding: From Theory to Practice | [Summary](/posts/readings/paper/infocom/infocom18-ncscale) | NCScale, scaling, network coding
TPDS'16 | I/O-Efficient Scaling Schemes for Distributed Storage Systems with CRS Codes | [Link](http://ieeexplore.ieee.org/abstract/document/7347422/) | CRS, scaling
DSN'15, TPDS'17 | Enabling Efficient and Reliable Transition from Replication to Erasure Coding for Clustered File Systems | [Link](https://ieeexplore.ieee.org/document/7872497) | Replication to EC, redundancy transitioning
FAST'15 | A Tale of Two Erasure Codes in HDFS | [Summary](/posts/2020/09/paper-reading-twoec-fast15/) | HACFS, redundancy transitioning
TC'15 | Accelerate RDP RAID-6 Scaling by Reducing Disk I/Os and XOR Operations | [Link](http://ieeexplore.ieee.org/abstract/document/6642028/) | RAID, scaling
TPDS'14 | An Efficient Scaling Scheme for RS-Coded Storage Clusters | [Summary](/posts/readings/paper/tpds/tpds14-scalers) | Scale-RS, scaling
ICPP'12 | GSR: A Global Stripe-Based Redistribution Approach to Accelerate RAID-5 Scaling | [Link](https://ieeexplore.ieee.org/abstract/document/6337607/) | GSR, RAID, scaling (C. Wu)
FAST'11 | Accelerate RAID Scaling by Minimizing Data Migration | [Link](https://www.usenix.org/conference/fast11/fastscale-accelerate-raid-scaling-minimizing-data-migration) | FastScale, RAID, scaling
TOCS'1996 | The HP AutoRAID Hierarchical Storage System | [Link](https://ieeexplore.ieee.org/document/5264167) | AutoRAID, replication to RAID


#### Erasure Coding Reliability Analysis

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SRDS'17, TPDS'19 | SimEDC: A Simulator for the Reliability Analysis of Erasure-Coded Data Centers | [Link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/tpds19simedc.pdf) | SimEDC
HotStorage'10 | Mean time to meaningless: MTTDL, Markov models, and storage system reliability | [Link](https://www.usenix.org/legacy/event/hotstorage10/tech/full_papers/Greenan.pdf) | MTTDL Meaningless
OSDI'09 | Availability in Globally Distributed Storage Systems | [Summary](/posts/readings/paper/osdi/osdi09-availability) | Google Availability
I2TS'08 | When MTTDLs Are Not Good Enough: Providing Better Estimates of Disk Array Reliability  | [Link](https://www.cse.scu.edu/~tschwarz/Papers/i2ts08.pdf) | Calculation of MTTDL (1)
SNAPI'07| Outshining Mirrors: MTTDL of Fixed-Order SSPiRAL Layouts | [Link](http://www2.cs.uh.edu/~paris/MYPAPERS/Snapi07.pdf) | Calculation of MTTDL (2)


#### Techniques for Erasure Coding

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'23 | Explore Data Placement Algorithm for Balanced Recovery Load Distribution | [Summary](/posts/readings/paper/atc/atc23-repair-placement) | Recovery, data placement
IPDPS'23 | Boosting Multi-Block Repair in Cloud Storage Systems with Wide-Stripe Erasure Coding | [Summary](/posts/readings/paper/ipdps/ipdps23-multiple-repair) | Multiple repair, wide stripe
ICPP'23 | Toward Optimal Repair and Load Balance in Locally Repairable Codes | [Summary](/posts/readings/paper/icpp/icpp23-optimal-lrc) | LRC, repair, load balancing
ICDCS'22 | PivotRepair: Fast Pipelined Repair for Erasure-Coded Hot Storage | [Link](https://ieeexplore.ieee.org/document/9912193/) | repair
ICPP'22 | Exploiting Parallelism of Disk Failure Recovery via Partial Stripe Repair for an Erasure-Coded High-Density Storage Server | [Link](https://dl.acm.org/doi/abs/10.1145/3545008.3545014) | repair, high density storage
ICPP'22 | Repair-Optimal Data Placement for Locally Repairable Codes with Optimal Minimum Hamming Distance | [Summary](/posts/readings/paper/icpp/icpp22-optimal-lrc) | LRC, repair, data placement
ATC'21 | Boosting Full-Node Repair in Erasure-Coded Storage | [Summary](/posts/readings/paper/atc/atc21-repairboost) | RepairBoost, full-node recovery
SOSP'21 | Geometric Partitioning: Explore the Boundary of Optimal Erasure Code Repair | [Link](/posts/readings/paper/sosp/sosp21-geometric-partitioning) | Geometric Partitioning
FAST'21 | Exploiting Combined Locality for Wide-Stripe Erasure Coding in Distributed Storage | [Summary](/posts/readings/paper/fast/fast21-ecwide), [Summary (earlier)](/posts/2021/07/paper-reading-ecwide/) | ECWide, repair, LRC, wide stripe
ICPP'21 | Multi-level Forwarding and Scheduling Repair Technique in Heterogeneous Network for Erasure-coded Clusters | [Link](https://dl.acm.org/doi/abs/10.1145/3472456.3472494) | repair, heterogeneous
IWQoS'21 | EC-Scheduler: A Load-Balanced Scheduler to Accelerate the Straggler Recovery for Erasure Coded Storage Systems | [Summary](/posts/readings/paper/iwqos/iwqos21-ecscheduler) | repair, load balancing
IPDPS'20 | EC-Fusion: An Efficient Hybrid Erasure Coding Framework to Improve Both Application and Recovery Performance in Cloud Storage Systems | [Link](https://ieeexplore.ieee.org/document/9139819) | EC-Fusion, multiple erasure codes
HotStorage'20 | SelectiveEC: Selective Reconstruction in Erasure-coded Storage Systems | [Summary](/posts/2020/08/paper-reading-selectiveec-hotstorage20/) | SelectiveEC, load balancing
Eurosys'20 | RAIDP: replication with intra-disk parity | [Summary](/posts/2020/08/paper-reading-raidp-eurosys20/) | RAID-P
FAST'20 | CRaft: An Erasure-coding-supported Version of Raft for Reducing Storage Cost and Network Cost | [Link](https://www.usenix.org/conference/fast20/presentation/wang-zizhong) | CRaft
FAST'19 | Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques | [Summary](/posts/2020/08/paper-reading-ec-acceleration-fast19/) | repair acceleration
DSN'19 | Fast Predictive Repair in Erasure-Coded Storage | [Summary](/posts/2020/08/paper-reading-fpr-dsn19/) | FastPR, repair, parallelization
ICPP'19 | Fast Recovery Techniques for Erasure-coded Clusters in Non-uniform Traffic Network | [Link](https://dl.acm.org/doi/10.1145/3337821.3337831) | multiple failure repair
ATC'17 | Repair Pipelining for Erasure-Coded Storage | [Summary](/posts/2020/08/paper-reading-repair-pipelining-atc17/) | ECPipe, repair, parallelization
ATC'17 | PARIX: Speculative Partial Writes in Erasure-Coded Systems | [Link](https://www.usenix.org/conference/atc17/technical-sessions/presentation/li-huiba) | Parix
Eurosys'16 | Partial-Parallel-Repair (PPR): A Distributed Technique for Repairing Erasure Coded Storage | [Summary](/posts/2020/08/paper-reading-ppr-eurosys16/) | PPR, repair, parallelization
MSST'13 | CORE: Augmenting Regenerating-Coding-Based Recovery for Single and Concurrent Failures in Distributed Storage Systems | [Link](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/msst13.pdf) | CORE, repair, mutli-failure
SYSTOR'14 | Lazy Means Smart: Reducing Repair Bandwidth Costs in Erasure-coded Distributed Storage | [Link](https://dl.acm.org/doi/abs/10.1145/2611354.2611370) | Lazy recovery
TC'14 | Boosting Degraded Reads in Heterogeneous Erasure-Coded Storage Systems | [Summary](/posts/readings/paper/tc/tc14-degraded) | degraded read, heterogeneous network
FAST'14 | Parity Logging with Reserved Space: Towards Efﬁcient Updates and Recovery in Erasure-coded Clustered Storage | [Link](https://www.usenix.org/conference/fast14/technical-sessions/presentation/chan) | CodFS
MSST’12 | On the speedup of single-disk failure recovery in XOR-coded storage systems: Theory and practice | [Summary](/posts/2020/09/paper-reading-zhu-replace-recovery-msst12/) | Zhu, replace recovery algorithms for XOR based codes
FAST'12 | Rethinking Erasure Codes for Cloud File Systems: Minimizing I/O for Recovery and Degraded Reads | [Summary](/posts/2020/09/paper-reading-khan-fast12/) | Khan, RotatedRS, repair I/O improvement




#### Erasure-coded Systems

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
NSDI'22 | C2DN: How to Harness Erasure Codes at the Edge
for Efficient Content Delivery | [Summary](/posts/readings/paper/nsdi/nsdi22-c2dn) | C2DN
FAST'22 | Hydra : Resilient and Highly Available Remote Memory | [Link](https://www.usenix.org/conference/fast22/presentation/lee) | Hydra, RDMA
FAST'22 | DEPART: Replica Decoupling for Distributed Key-Value Storage | [Link](https://www.usenix.org/conference/fast22/presentation/zhang-qiang) | DEPART, distributed KVStore, EC
NSDI'20 | Near-Optimal Latency Versus Cost Tradeoffs in Geo-Distributed Storage | [Summary](/posts/2021/06/paper-reading-pando-nsdi20/) | PANDO, consensus, EC
SC'20 | INEC: Fast and Coherent In-Network Erasure Coding | [Link](https://ieeexplore.ieee.org/document/9355252) | INEC, RDMA
SC'19 | TriEC: tripartite graph based erasure coding NIC offload | [Link](https://dl.acm.org/doi/abs/10.1145/3295500.3356178) | TriEC, RDMA
SoCC'19 | Coupling Decentralized Key-Value Stores with Erasure Coding | [Summary](/posts/readings/paper/socc/socc19-echash) | ECHash, KVStore
HPDC'19 | UMR-EC: A Unified and Multi-Rail Erasure Coding Library for High-Performance Distributed Storage Systems | [Link](https://dl.acm.org/doi/abs/10.1145/3307681.3325406) | UMR-EC, RDMA
FAST'19 | OpenEC: Toward Unified and Configurable Erasure Coding Management in Distributed Storage Systems | [Summary](/posts/2020/08/paper-reading-openec-fast19/) | OpenEC
ICDCS'17 | High-Performance and Resilient Key-Value Store with Online Erasure Coding for Big Data Workloads | [Link](https://ieeexplore.ieee.org/document/7979997) | RDMA
ATC'17 | Giza: Erasure Coding Objects across Global Data Centers | [Link](https://www.usenix.org/conference/atc17/technical-sessions/presentation/chen-yu-lin) | Giza, consensus
FAST'16 | Efficient and Available In-memory KV-Store with Hybrid Erasure Coding and Replication | [Link](https://www.usenix.org/conference/fast16/technical-sessions/presentation/zhang-heng) | Cocytus, KVStore
OSDI'16 | EC-Cache: Load-Balanced, Low-Latency Cluster Caching with Online Erasure Coding | [Summary](/posts/2021/02/paper-reading-eccache-osdi16/) |  EC-Cache
OSDI'14 | Pelican: A Building Block for Exascale Cold Data Storage | [Summary](/posts/2021/06/paper-reading-pelican-osdi14/) | Pelican, cold DSS
FAST'12 | NCCloud: A Network-Coding-Based Storage System in a Cloud-of-Clouds | [Summary](/posts/2019/06/paper-reading-nccloud-fast12/) | NCCloud, network coding


#### Miscellaneous

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
IPTPS'02 |  Erasure coding vs. replication:a quantitative comparison | [Link](http://people.eecs.berkeley.edu/~kubitron/courses/cs252/handouts/papers/erasure_iptps.pdf) | EC vs replication


### Storage Systems and Cloud

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'19 | Dayu: Fast and Low-interference Data Recovery in Very-large Storage Systems | [Link](https://www.usenix.org/conference/atc19/presentation/wang-zhufan) | Dayu, recovery
SYSTOR'19 | Kurma: Secure Geo-Distributed Multi-Cloud Storage Gateways | [Summary](/posts/2021/02/paper-reading-kruma-systor19/) | Kurma
ATC'14 | SCFS: A Shared Cloud-backed File System | [Summary](/posts/2021/01/paper-reading-scfs-atc14/) | SCFS, Depsky extension
SoCC'14 | Hybris: Robust Hybrid Cloud Storage | [Summary](/posts/2021/02/paper-reading-hybris-socc14/) | Hybris
SOSP'13 | SPANStore: Cost-Effective Geo-Replicated Storage Spanning Multiple Cloud Services | [Summary](/posts/2021/02/paper-reading-spanstore-sosp13/) | SPANStore
OSDI'12 | Flat Datacenter Storage | [Link](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-75.pdf) | Flat Datacenter Storage
Eurosys'11 | DEPSKY: A High-Availability and Integrity Layer for Cloud Storage | [Summary](/posts/2019/07/paper-reading-depsky-eurosys11/) | Depsky
SoCC'10 | RACS: a case for cloud storage diversity | [Summary](/posts/2019/07/paper-reading-racs-socc10/) | RACS

### Blockchain

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
Bitcoin white paper | Bitcoin: A Peer-to-Peer Electronic Cash System | [Link](https://bitcoin.org/bitcoin.pdf) | Bitcoin white paper
Ethereum yellow paper | Ethereum: A secure decentralised generalised transaction ledger | [Link](https://ethereum.github.io/yellowpaper/paper.pdf) | Ethereum yellow paper
Github Repo | Self-maintained blockchain paper list | [Repo 1](https://github.com/jianyu-niu/blockchain_conference_paper), [Repo 2](https://github.com/decrypto-org/blockchain-papers) | -
HPCA'24 | Rapper: A Parameter-Aware Repair-in-Memory Accelerator for Blockchain Storage Platform | [Link](https://ieeexplore.ieee.org/document/10476464) | Blockchain, EC
ACM Computing Survey'24 | Scaling Blockchains with Error Correction Codes: A Survey on Coded Blockchains | [Link](https://dl.acm.org/doi/10.1145/3637224) | Blockchain, coding
TC'24 | BFT-DSN: A Byzantine Fault-Tolerant Decentralized Storage Network | [Link](https://ieeexplore.ieee.org/document/10436433) | BFT, EC
IOTJ'24 | TORR: A Lightweight Blockchain for Decentralized Federated Learning | [Link](https://ieeexplore.ieee.org/document/10189448/) | Blockchain, EC, AI
TKDE'23 | PartitionChain: A Scalable and Reliable Data Storage Strategy for Permissioned Blockchain | [Link](https://ieeexplore.ieee.org/document/9656652) | PartitionChain
TC'23 | Efficient Integrity Auditing Mechanism With Secure Deduplication for Blockchain Storage | [Link](https://ieeexplore.ieee.org/document/10050830) | Blockchain, security, deduplication
ICPADS'23 | DW-LRC: A Dynamic Wide-stripe LRC Codes for Blockchain Data Under Malicious Node Scenarios | [Link](https://ieeexplore.ieee.org/document/10476025) | Blockchain, EC, LRC
IOTJ'23 | On Min–Max Storage for Resource-Restricted Clients in Coded Blockchain Systems | [Link](https://ieeexplore.ieee.org/document/10130762) | Blockchain, coding
TDSC'22 | Enabling Secure and Efficient Decentralized Storage Auditing With Blockchain | [Link](https://ieeexplore.ieee.org/document/9436004/) | Blockchain, security, coding
ISIT'22 | Polar Coded Merkle Tree: Improved Detection of Data Availability Attacks in Blockchain Systems | [Link](https://ieeexplore.ieee.org/iel7/9834325/9834269/09834538.pdf) | Blockchain, Merkle tree, Coding
IOTJ'22 | Proof of Continuous Work for Reliable Data Storage Over Permissionless Blockchain | [Link](https://ieeexplore.ieee.org/document/9548672) | Permissionless blockchain, EC
COMNET'22 | Speeding up block propagation in Bitcoin network: Uncoded and coded designs | [Link](https://www.sciencedirect.com/science/article/pii/S1389128622000238) | Bitcoin, coding
TCOM'22 | Overcoming Data Availability Attacks in Blockchain Systems: Short Code-Length LDPC Code Design for Coded Merkle Tree | [Link](https://ieeexplore.ieee.org/document/9841605) | Blockchain, merkle tree, coding
SmartWorld'22 | A Lightweight Locally Repairable Code-based Storage Architecture for Blockchains | [Link](https://ieeexplore.ieee.org/document/10189448/) | Blockchain, coding, LRC
WCNC'22 | Secure and Private Fountain Code based Architecture for Blockchains | [Link](https://ieeexplore.ieee.org/document/9771862) | Blokchain, coding
IEEE S&P (Oakland)'21 | Red Belly: A Secure, Fair and Scalable Open Blockchain | [Link](https://ieeexplore.ieee.org/document/9519440/) | Red Belly
TIFS'21 | PolyShard: Coded Sharding Achieves Linearly Scaling Efficiency and Security Simultaneously | [Link](https://ieeexplore.ieee.org/iel7/9166581/9173928/09174305.pdf) | Polyshard, blockchain, sharding
TON'21 | Coding for Scalable Blockchains via Dynamic Distributed Storage | [Link](https://ieeexplore.ieee.org/document/9508769) | Blockchain, EC
TKDE'21 | Distributed Error Correction Coding Scheme for Low Storage Blockchain Systems | [Link](https://ieeexplore.ieee.org/document/9042862) | Erasure coding, blockchain
ISIT'21 | Low Latency Cross-Shard Transactions in Coded Blockchain | [Link](https://ieeexplore.ieee.org/iel7/9517708/9517709/09518047.pdf) | Blockchain, coding, sharding
ITW'21 | Communication-Efficient LDPC Code Design for Data Availability Oracle in Side Blockchains | [Link](https://dl.acm.org/doi/abs/10.1109/ITW48936.2021.9611473) | Blockchain, coding
ICDE'20 | BFT-Store: Storage Partition for Permissioned Blockchain via Erasure Coding | [Link](https://ieeexplore.ieee.org/document/9101675) | BFT-Store
SIGMOD'20 Demo | A Byzantine Fault Tolerant Storage for Permissioned Blockchain | [Link](https://dl.acm.org/doi/10.1145/3448016.3452744) | Erasure coding, permissioned blockchain
JPDC'20 | Blockchain-based verification framework for data integrity in edge-cloud storage | [Link](https://www.sciencedirect.com/science/article/pii/S0743731520303142) | Blockchain, verification, coding
ICDCS'20 | Towards Privacy-assured and Lightweight On-chain Auditing of Decentralized Storage | [Link](https://ieeexplore.ieee.org/document/9355771) | Blockchain, verification, auditing
Blockchain'20 | Secure Regenerating Codes for Reducing Storage and Bootstrap Costs in Sharded Blockchains | [Link](https://ieeexplore.ieee.org/document/9284685) | Blockchain, EC, regenerating codes
IOTJ'20 | Distributed Error Correction Coding Scheme for Low Storage Blockchain Systems | [Link](https://ieeexplore.ieee.org/document/9042862) | Erasure coding, blockchain
AFT'19 | SoK: Sharding on Blockchain | [Link](https://dl.acm.org/doi/10.1145/3318041.3355457) | Sharding
CCS'18 | RapidChain: Scaling Blockchain via Full Sharding | [Link](https://dl.acm.org/doi/10.1145/3243734.3243853) | RapidChain, blockchain, sharding
iTings'18 | Erasure code-based low storage blockchain node | [Link](https://ieeexplore.ieee.org/document/8726839) | (highly cited reference) Erasure coding, blockchain
TrustCom'18 | A Blockchain-based Decentralized Data Storage and Access Framework for PingER | [Link](https://ieeexplore.ieee.org/document/8456048) | Bitcoin, coding
ICPADS'18 | Blockchain Based Data Integrity Verification in P2P Cloud Storage | [Link](https://ieeexplore.ieee.org/document/8644863/) | Blockchain, verification, coding
PODC'07 | Verifying Distributed Erasure-Coded Data | [Link](https://dl.acm.org/doi/10.1145/1281100.1281122) | EC, verification
DSN'04 | Efficient Byzantine-tolerant erasure-coded storage | [Link](https://ieeexplore.ieee.org/document/1311884) | BFT, erasure coding




### Security

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
Systor'18 | How to Best Share a Big Secret | [Link](https://dl.acm.org/doi/10.1145/3211890.3211896) | Secret sharing
Communications of the ACM'1979 | How to Share a Secret | [Link](https://dl.acm.org/doi/10.1145/359168.359176) | Secret sharing


### Edge

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
HotEdge'20 | Sharing and Caring of Data at the Edge | [Summary](/posts/2021/02/paper-reading-sharing-hotedge20/) | Edge storage survey (including a list of papers, must read)
JPDC'20 | EdgeKV: Decentralized, scalable, and consistent storage for the edge | [Summary](/posts/2021/06/paper-reading-edgekv-jpdc20/) | EdgeKV


#### SEC (Symposium on Edge Computing) Paper List

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SEC’17 | EdgeCourier: An Edge-hosted Personal Service for Low-bandwidth Document Synchronization in Mobile Cloud Storage Services | --- | ---
SEC’17 | CloudPath: A Multi-Tier Cloud Computing Framework | --- | ---
SEC’17 | LAVEA: Latency-aware Video Analytics on Edge Computing Platform | --- | ---
SEC’17 | Fast Transparent Virtual Machine Migration in Distributed Edge Clouds | --- | ---
SEC’17 | A Vehicle-based Edge Computing Platform for Transit and Human Mobility Analytics | --- | ---
SEC’18 | VideoEdge: Processing Camera Streams using Hierarchical Clusters | --- | ---
SEC’18 | Extend Cloud to Edge with KubeEdge | --- | ---
SEC’19 | Sandpaper: mitigating performance interference in CDN edge proxies | --- | ---
SEC’19 | Real-time traffic estimation at vehicular edge nodes | --- | ---
SEC’19 | Infrastructure fault detection and prediction in edge cloud environments | --- | ---
SEC’19 | Why cloud applications are not ready for the edge (yet) | --- | ---



### Deduplication

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'15 | Toward Reliable, Secure, and Cost-Efficient Cloud Storage via Convergent Dispersal | [Summary](/posts/2019/06/paper-reading-cdstore/) | CDStore


### Consensus

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ATC'14 | In Search of an Understandable Consensus Algorithm | [Summary](/posts/2019/07/paper-reading-raft-atc14/) | Raft


### Stream Processing

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
ICDCS'20 | Toward Adaptive Disk Failure Prediction via Stream Mining | [Summary](/posts/2020/08/paper-reading-streamdfp-icdcs20/) | StreamDFP


### Graph Processing

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
OSDI'16 | Gemini: A Computation-Centric Distributed Graph Processing System | [Summary](/posts/2020/09/paper-reading-gemini-osdi16/) | Gemini
SIGMOD'19 | Nanosecond Indexing of Graph Data With Hash Maps and VLists | [Summary](/posts/2020/09/paper-reading-nanosecond-sigmod19/) | Nanosecond


### Scheduling

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SOSP'1973 | Polynomial Complete Scheduling Problems | [Summary](/posts/readings/paper/sosp/sosp1973-scheduling) | Scheduling proof
Communications of ACM'1974 | Scheduling independent tasks to reduce mean finishing time | [Summary](/posts/readings/paper/commacm/commacm1974-scheduling) | Scheduling algorithms
JACM'1976 | Exact and Approximate Algorithms for Scheduling Nonidentical Processors | [Summary](/posts/readings/paper/jacm/jacm1976-scheduling) | Scheduling algorithms
JACM'1977 | Heuristic Algorithms for Scheduling Independent Tasks on Nonidentical Processors | [Summary](/posts/readings/paper/jacm/jacm1977-scheduling) | Performance analysis on scheduling heuristics
MP'1990 | Approximation Algorithms for Scheduling Unrelated Parallel Machines | [Summary](/posts/readings/paper/mp/mp1990-scheduling) | Scheduling algorithms and proofs


### Graph Theory

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
JALG'06 | Semi-matchings for bipartite graphs and load balancing | [Summary](/posts/readings/paper/jalg/jalg05-semi-matching) | Semi-matching on unweighted bipartite
IPL'06 | An approximation algorithm for the load-balanced semi-matching problem in weighted bipartite graphs | [Summary](/posts/readings/paper/ipl/ipl06-semi-matching) | Semi-matching for jobs with identical processing times
IPL'09 | A note on "An approximation algorithm for the load-balanced semi-matching problem in weighted bipartite graphs" | [Summary](/posts/readings/paper/ipl/ipl09-semi-matching-correction) | Corrections of bounds for IPL'06
IPSJ'07 | Optimal Balanced Semi-Matchings for Weighted Bipartite Graphs | [Summary](/posts/readings/paper/ipsj/ipsj07-matching) | Optimal Semi-matching proof


### Networking

#### Software Defined Network (SDN)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
Book | Software-Defined-Networks: A Systems Approach | Reading notes: [Ch.1](/posts/readings/book/sdn-system/sdn-system-ch1), [Ch.2](/posts/readings/book/sdn-system/sdn-system-ch2), [Ch.3](/posts/readings/book/sdn-system/sdn-system-ch3), [Ch.4](/posts/readings/book/sdn-system/sdn-system-ch4), [Ch.5](/posts/readings/book/sdn-system/sdn-system-ch5), [Ch.6](/posts/readings/book/sdn-system/sdn-system-ch6), [Ch.7](/posts/readings/book/sdn-system/sdn-system-ch7), [Ch.8](/posts/readings/book/sdn-system/sdn-system-ch8) | SDN Book
White paper | Cisco SD-WAN white paper | [Link](https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/white-paper-listing.html) | Cisco SD-WAN
IEEE Communications Surveys & Tutorials'14 | A Survey of Software-Defined Networking: Past, Present, and Future of Programmable Networks | [Link](https://ieeexplore.ieee.org/document/6739370) | SDN Survey
ICCCN'21 | Software-Defined Wide Area Network (SD-WAN): Architecture, Advances and Opportunities | [Link](https://ieeexplore.ieee.org/document/8847124) | SD-WAN Survey
SIGCOMM'18 | B4: Experience with a Globally-Deployed Software Defined WAN | [Link](https://dl.acm.org/doi/10.1145/2534169.2486019) | B4
NSDI'14 | Network Virtualization in Multi-tenant Datacenters | [Link](https://www.usenix.org/conference/nsdi14/technical-sessions/presentation/koponen) | Network Virtualization
SIGCOMM'13 | Achieving High Utilization with Software-Driven WAN | [Link](https://conferences.sigcomm.org/sigcomm/2013/papers/sigcomm/p15.pdf) (Not done) | Software-Driven WAN
SIGCOMM'08 | OpenFlow: Enabling Innovation in Campus Networks | [Link](http://ccr.sigcomm.org/online/files/p69-v38n2n-mckeown.pdf) (Not done) | OpenFlow

#### Network Measurement

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
SIGCOMM'18 | SketchLearn: Relieving User Burdens in Approximate Measurement with Automated Statistical Inference | [Summary](/posts/2020/08/paper-reading-sketchlearn-sigcomm18/) | SketchLearn


### TOS (Transaction on Storage) Paper List

#### Erasure Coding (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'09 | GRID codes: Strip-based erasure codes with high fault tolerance for storage systems | [Link](https://dl.acm.org/doi/10.1145/1480439.1480444) | ---
TOS'12 | Generalized X-code: An efficient RAID-6 code for arbitrary size of disk array | [Link](https://dl.acm.org/doi/10.1145/2339118.2339121) | ---
TOS'13 | Exploiting Redundancies and Deferred Writes to Conserve Energy in Erasure-Coded Storage Clusters | [Link](https://doi.org/10.1145/2491472.2491473) | ---
TOS'13 | Pyramid Codes: Flexible Schemes to Trade Space for Access Efficiency in Reliable Data Storage Systems | [Link](https://doi.org/10.1145/2435204.2435207) | ---
TOS'14 | STAIR Codes: A General Family of Erasure Codes for Tolerating Device and Sector Failures | [Link](https://doi.org/10.1145/2658991) | ---
TOS'14 | Sector-Disk (SD) Erasure Codes for Mixed Failure Modes in RAID Systems | [Link](https://dl.acm.org/doi/10.1145/2560013) | ---
TOS'15 | Low-Complexity Implementation of RAID Based on Reed-Solomon Codes | [Link](https://dl.acm.org/doi/10.1145/2700308) | ---
TOS'17 | High-Performance General Functional Regenerating Codes with Near-Optimal Repair Bandwidth | [Link](https://dl.acm.org/doi/10.1145/3051122) | ---
TOS'17 | Optimal Repair Layering for Erasure-Coded Data Centers: From Theory to Practice | [Link](https://doi.org/10.1145/3149349) | ---
TOS'17 | Systematic Erasure Codes with Optimal Repair Bandwidth and Storage | [Link](https://doi.org/10.1145/3109479) | ---
TOS'20 | On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes | [Link](https://doi.org/10.1145/3381832) | ---
TOS'20 | Fast Erasure Coding for Data Storage: A Comprehensive Study of the Acceleration Techniques | [Link](https://doi.org/10.1145/3375554) | ---
TOS'20 | PBS: An Efficient Erasure-Coded Block Storage System Based on Speculative Partial Writes | [Link](https://doi.org/10.1145/3365839) | ---


#### RAID (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'05 | Improving storage system availability with D-GRAID | [Link](https://doi.org/10.1145/1063786.1063787) | ---
TOS'05 | Reliability and security of RAID storage systems and D2D archives using SATA disk drives | [Link](https://doi.org/10.1145/1044956.1044961) | ---
TOS'07 | PARAID: A gear-shifting power-aware RAID | [Link](https://dl.acm.org/doi/10.1145/1288783.1289721) | ---
TOS'08 | A new intra-disk redundancy scheme for high-reliability RAID storage systems in the presence of unrecoverable errors | [Link](https://dl.acm.org/doi/10.1145/1353452.1353453) | ---
TOS'09 | Higher reliability redundant disk arrays: Organization, operation, and coding | [Link](https://dl.acm.org/doi/10.1145/1629075.1629076) | ---
TOS'10 | Differential RAID: Rethinking RAID for SSD reliability | [Link](https://dl.acm.org/doi/10.1145/1807060.1807061) | ---
TOS'11 | A Hybrid Approach to Failed Disk Recovery Using RAID-6 Codes: Algorithms and Performance Evaluation | [Link](https://dl.acm.org/doi/10.1145/2027066.2027071) | ---
TOS'11 | Minimum density RAID-6 codes | [Link](https://doi.org/10.1145/1970338.1970341) | ---
TOS'11 | Online availability upgrades for parity-based RAIDs through supplementary parity augmentations | [Link](https://doi.org/10.1145/1970338.1970340) | ---
TOS'11 | Reducing Repair Traffic in P2P Backup Systems: Exact Regenerating Codes on Hierarchical Codes | [Link](https://doi.org/10.1145/2027066.2027070) | ---
TOS'11 | Disk Scrubbing Versus Intradisk Redundancy for RAID Storage Systems | [Link](https://doi.org/10.1145/1970348.1970350) | ---
TOS'14 | Beyond MTTDL: A Closed-Form RAID 6 Reliability Equation | [Link](https://doi.org/10.1145/2577386) | ---
TOS'15 | RAIDShield: Characterizing, Monitoring, and Proactively Protecting Against Disk Failures | [Link](https://doi.org/10.1145/2820615) | ---
TOS'15 | An Energy-Efficient and Reliable Storage Mechanism for Data-Intensive Academic Archive Systems | [Link](https://doi.org/10.1145/2720021) | ---
TOS'15 | Rebuttal to “Beyond MTTDL: A Closed-Form RAID-6 Reliability Equation” | [Link](https://doi.org/10.1145/2700311) | ---
TOS'16 | LoneStar RAID: Massive Array of Offline Disks for Archival Systems | [Link](https://doi.org/10.1145/2840810) | ---
TOS'16 | H-Scale: A Fast Approach to Scale Disk Arrays via Hybrid Stripe Deployment | [Link](https://dl.acm.org/doi/10.1145/2822895) | ---
TOS'19 | Determining Data Distribution for Large Disk Enclosures with 3-D Data Templates | [Link](https://doi.org/10.1145/3342858) | RAID+


#### Data Placement (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'14 | Random Slicing: Efficient and Scalable Data Placement for Large-Scale Storage Systems | [Link](https://doi.org/10.1145/2632230) | ---


#### Flash-memory (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'18 | An Analysis of Flash Page Reuse With WOM Codes | [Link](https://doi.org/10.1145/3177886) | ---


#### Backup (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'12 | Efficient cooperative backup with decentralized trust management | [Link](https://doi.org/10.1145/2339118.2339119) | ---


#### Storage System (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'05 | DISP: Practical, efficient, secure and fault-tolerant distributed data storage | [Link](https://doi.org/10.1145/1044956.1044960) | ---
TOS'09 | POTSHARDS—a secure, recoverable, long-term archival storage system | [Link](https://doi.org/10.1145/1534912.1534914) | ---
TOS'11 | PRESIDIO: A Framework for Efficient Archival Data Storage | [Link](https://doi.org/10.1145/1970348.1970351) | ---
TOS'13 | DepSky: Dependable and Secure Storage in a Cloud-of-Clouds | [Summary](/posts/2019/07/paper-reading-depsky-eurosys11/) | ---
TOS'17 | Hybris: Robust Hybrid Cloud Storage | [Summary](/posts/2021/02/paper-reading-racs-socc14/) | ---
TOS'17 | Redundancy Does Not Imply Fault Tolerance: Analysis of Distributed Storage Reactions to File-System Faults | [Link](https://dl.acm.org/doi/10.1145/3125497) | ---
TOS'19 | Liquid Cloud Storage | [Link](https://doi.org/10.1145/3281276) | ---
TOS'20 | The Case for Custom Storage Backends in Distributed Storage Systems | [Link](https://doi.org/10.1145/3386362) | ---


#### KV-Store (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'17 | Efficient and Available In-Memory KV-Store with Hybrid Erasure Coding and Replication | [Link](https://doi.org/10.1145/3129900) | ---


#### Benchmark (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'07 | Understanding disk failure rates: What does an MTTF of 1,000,000 hours mean to you? | [Link](https://doi.org/10.1145/1288783.1288785) | ---
TOS'08 | A nine year study of file system and storage benchmarking | [Link](https://dl.acm.org/doi/10.1145/1367829.1367831) | ---


#### Techniques (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'12 | Efficient software implementations of large finite fields GF(2n) for secure storage applications | [Link](https://doi.org/10.1145/2093139.2093141) | ---
TOS'16 | Tools for Predicting the Reliability of Large-Scale Storage Systems | [Link](https://doi.org/10.1145/2911987) | ---


#### File System (TOS)

Venue | Title | Link / Summary | Brief
:---: | :---: | :---: | :---:
TOS'14 | A Study of Linux File System Evolution | [Link](https://doi.org/10.1145/2560012) | ---
TOS'20 | Everyone Loves File: Oracle File Storage Service | [Link](https://doi.org/10.1145/3377877) | ---
