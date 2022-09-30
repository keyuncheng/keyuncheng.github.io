---
title: "Paper Reading: NC for Storage TIT'10"
date: 2020-08-15
permalink: /posts/2020/08/paper-reading-ncstorage-tit10/
author_profile: false
excerpt: false
tags:
  - storage
  - network coding
  - distributed system
  - regenerating codes
---

Network Coding for Distributed Storage Systems

(Revised June 15, 2021)

Download
------
[Trans. of Information Theory, 2010](https://users.ece.utexas.edu/~dimakis/RC_Journal.pdf)


Summary
------

This paper builds the theory of using network coding on erasure coded storage. It introduces regenrating codes, which transmits **a function of erasure coded fragments** from the surviving nodes for repairing. The paper shows that regenerating codes reduces repair bandwidth with a linear increase of storage overhead (MBR) or retains the same storage overhead (MSR) as traditional EC. This paper shows the tradeoff between repair bandwidth and storage overhead by solving a min-flow problem over a pre-defined information flow graph. It also shows the possibility of adopting regenerating codes for less frequently read data.



Details
------

1. Problems: In distributed storage, high repair traffic for traditional EC. E.g. for (n, k) = (4, 2), at least 2 copies of coded data should be collected by the new node. Access to these coded data is not avoidable.

2. Approach: Regenerating code achieves optimal storage and repair bandwidth tradeoff curve.

3. Background: Erasure coding, network coding, distributed storage system

The information flow is analyzed by information flow graph. It consists of data source, storage nodes, data collectors. The nodes are active/inactive for each timeslot. The graph is dynamic and allows new nodes to join. For (n, k) = (4, 2), the minimum cut shows that at least 0.5 times data is required. 

Storage bandwidth tradeoff. For each set of params for a distribute EC storage systems, we marked it as (n, k, d, a, g), d = number of information from survivors, a = data size, g = min data size required for repair.

3.1 Code repair can be achieved iff. the underlying information graph has sufficiently large min-cuts.
	* Minimum of storage point is: (M / k, Md / k(d - k + 1))

3.2 Minimum-Storage Regenerating (MSR) Codes and Minimum-Bandwidth Regenerating (MBR) Codes
	* For MSR code, the core point is let the newcomer to communicate more than k nodes. For each node, a factor of (n - 1) / (n - k) of the data are required.
	* For the MBR code, it's considered no longer optimal in terns of the reliability for given redundancy.

4. Evaluation
	* Model. f: the fraction of nodes fails per-unit time; a: the probability that a node trasient fails.
	* The probability of a file's unavailability is calculated for all ECs.
	* Estimation of f an a in practice are done with traces. f and a are derived from the traces.

	* Comparison between MSR, MBR and Hybrid of them: MSR offers slightly lower maintenance bandwidth and storage. Disadvantage of MBR: constructing the file requires communication with all n - 1 nodes.

5. Conclusion: a theoretical framework (information flow graph) to determine the information required for repair in districuted EC storage, and the tradeoff between storage and repair bandwidth.



Strength
------




Weakness
------

Regenrating codes are more applicable for less frequently read data (e.g. cold archive, backup, etc.), but not for hot data, since the read cost is much higher than replication. Even for MBR codes, the newly introduced storage overhead may be an issue.


<!-- refs -->