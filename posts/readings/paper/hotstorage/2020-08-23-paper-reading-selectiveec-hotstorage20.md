---
title: "Paper Reading: SelectiveEC HotStorage'20"
date: 2020-08-23
permalink: /posts/2020/08/paper-reading-selectiveec-hotstorage20/
author_profile: false
excerpt: false
tags:
  - Erasure Coding
---


SelectiveEC: Selective Reconstruction in Erasure-coded Storage Systems


Download
------
[HotStorage, 2020](https://www.usenix.org/system/files/hotstorage20_paper_xu.pdf)


Summary
------

This paper introduces a balanced reconstruction scheduling module SelectiveEC for erasure coding, to solve the skewed load in recovery batches. Compared with random stripe reconstruction, SelectiveEC improves the  recovery process by averagely bigger than 97%. 



Details
------


Background: Random selection of source and replacement makes the repair traffic skewed/unbalanced, thus slows down the recovery. Even high-speed network like InfiniteBand speeds up the recovery process, it induces higher costs.

1. Problem 1: Network transmission time is amplified for *k* times because it has to retrieve k chunks. Chunks transmission time take up to 85.23%, and increase as *k* goes up.

2. Problem 2: Though data chunks are randomly distributed, it's hard to reach load balance with limited number of chunks.

3. Problem 3: Non-uniform data layout.

Approach: 

1. Introduced a bipartite graph to define the degree of parallelism (DRP). Reconstruction is described by linking replacement node and chunk node. DRP = number of failed chunk processed in a timeslot. If all degree of nodes are the same, it achieves load balancing. Maximum of DRP can't be reached with large k.

2. SelectiveEC to improve the load balance of single node failure. Two optimization techs: dynamic, and manual. Dynamic: it dynamically selects reconstruction tasks to batches to make them balanced.

How to do: 

1. Construct a bipartite for the repair task. Finding a k-regular graph is NP-hard,  do it with max flow to find a near optimal solution of the graph. If a flow is saturated, it's a k-regular graph, thus load balanced. 

2. Then update the flow by replacing the min degree nodes with reconstruction tasks, to make it balanced. Finally, a (near) saturated flow can be get.

Note: Do this for source nodes and reconstruction nodes.



Strength
------

1. By using the bipartite to simulate the recovery process, SelectiveEC improves DRP (dynmaic repair paralleling) by up to 106%.




Weakness
------


1. This paper only compares with the randomly reconstruction. It uses max flow as the scheduler, how about other baselines of chunk recovery scheduling? Greedy approach or other dynamic approaches? What's the computation cost of the scheduler?

2. It improves the performance when the transmission is the bottleneck. What if it's not? Will it then introduces additional overhead?

3. Only DRP (degree of recovery parallelism) is analyzed by cumulative probability density function. How about the recovery speed?




<!-- refs -->