---
title: "Paper Reading: NCCloud"
date: 2019-06-30
permalink: /posts/2019/06/paper-reading-nccloud-fast12/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - fault tolerance
---

NCCloud: A Network-Coding-Based Storage System in a Cloud-of-Clouds


Download
------
[ToC, 2013](https://appsrv.cse.cuhk.edu.hk/~pclee/www/pubs/tc13nccloud.pdf)

[FAST, 2012](http://www.cse.cuhk.edu.hk/~pclee/www/pubs/fast12.pdf)


Summary
------

This paper presents a proxy-based storage system called NCCloud, which is built on top of a network-coding-based storage scheme called FMSR. Compared with traditional RAID-6 (Reed Solomon Codes), NCCloud can save repair traffic by close to 50% when $n$ is large. While other regenerating code like EMSR code keeps the same storage size as in RAID-6 codes but saves repair traffic, it still requires storage nodes to perform encoding during repair. FMSR codes achieves the same repair traffic but relax the encoding requirement of storage nodes, so it 's portable to any cloud storage service which only need to support the standard read/write functionalities. However, FMSR codes are non-systematic and are acceptible for long-term archival applications, where the read frequency is typically low.


Details
------

An example
------

![fig1][fig1]

#### "Fig1: example of repair operation in RAID-6, EMSR, FMSR codes with $n = 4$ and $k = 2$"

Fig 1 illustrates the repair operation **single node failure** for different codes. In this example, a file in size $M$ are stored in $n = 4$ nodes and allows $k = 2$ node failure at most. Corresponding statistics are listed in the following table. 

| Codes  | Chunk Size    | Total Storage Size | Repair Traffic | Other Requirements |
|:------:|:-------------:|:------------------:|:--------------:|:------------------:|
| RS     | $M / 2$       | 2M                 | M              |                    |
| EMSR   | $M / 4$       | 2M                 | 0.75M          | Encoding in Storage Nodes |
| FMSR   | $M / 4$       | 2M                 | 0.75M          |                    |


Implementation
------

* Regenerate code chunks that are not necessarily identical to those originally stored in the failed node

* Two phase checking scheme

### Upload

1. devide file $F$ into $k(n-k)$ equal-size **native chunks** = $F_i$

2. encode **native chunks** to $n(n-k)$ equal-size **code chunks** = $P_i$

3. let **EM** = $[a_{i,j}]$ be $n(n-k) * k(n-k)$ encoding matrix. Row vector in size $k(n-k)$ of **EM** is called *encoding coefficient vector (ECV)*

4. $P_i = \sum_{j=1}^{k(n-k)} a_{i,j}F_j$, product of ECV_i and all the native chunks $F_1$ ... $F_{k(n-k)}$.

5. Whole **EM** is stored in a metadata object then replicated to all storage nodes.

6. Many ways to construct **EM**, as long as it passes two-phase checking.


### Download

1. select any $k$ of $n$ storage nodes, download $k(n-k)$ **code chunks**.

2. ECVs form a $k(n-k) * k(n-k)$ matrix $EM_{repair}$.

3. If the MDS property is maintained, $EM_{repair}^{-1}$ exists.

4. **native chunks** can be recovered by using all downloaded **code chunks** by $F = EM_{repair}^{-1}P$.


### Repair

1. Ensure the MDS property still holds  even after **iterative repairs**.

2. Two phase-checking scheme: suppose $(r-1)^{th}$ repair successful, then in $(r)^{th}$ repair, we first check if the new set of chunks in all storage nodes satisfies the MDS property in $(r)^{th}$ repair, then check if the MDS property still holds in $(r+1)^{th}$ repair.

3. repair steps

* Step 1: Download **EM** from one node.

* Step 2: Select one ECV from each of the $n - 1$ surviving nodes, which means randomly select one chunk from all (n-k) chunks in each storage nodes.

* Step 3: Generate repair matrix randomly. 

* Step 4: Compute the ECVs for the new code chunks and reproduce a new encoding matrix $EM^{\'}$.

* Step 5: check if both MDS and rMDS are satisfied for $EM^{\'}$. If either one fails, return to Step 2. Note that overhead doesnot depend on the chunk size, since only deal with ECVs.

* Step 6: Download actual chunk data and regenerate new chunk data. We proceed to download the $n - 1$ chunks that correspond to the selected ECVs in Step 2 from the n - 1 surviving nodes. Wrong selection of ECVs may violate the MDS property thus fail in recovery.

### Analysis

Some analysis of two-phase checking and system reliability, including an counter example, simulations.

### Discussion

* Generalization of FMSR codes for concurrent node failures

* Different metrics other than MTTDL

* Degraded reads

Strength
------

* Double fault-tolerance

* Save repair traffic (up to 50% for large n)

* Thin-cloud interface


Weakness
------

* Large overhead of encode/decode operations. Two-phase checking causes generating new code chunks.

* Non-systematic, not a good choice for frequent read(modify) operation. Partial read requires complete file download.



<!-- refs -->

[fig1]: /images/2019-06-30-paper-reading-nccloud/fig1.jpg "fig1"