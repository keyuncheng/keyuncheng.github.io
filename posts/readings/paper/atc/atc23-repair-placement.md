# Reading Notes: ATC'23 repair data placement

Title: Explore Data Placement Algorithm for Balanced Recovery Load Distribution

Conference (ATC'23): [Link](https://www.usenix.org/conference/atc23/presentation/shan)

Journal (): [Link]()

## Summary

This paper formulates the EC full-node recovery load balancing problem with a
weighted repair load graph, and proves that solving the problem (finding an
optimal data placement with minimum recovery load) is NP-hard by reducing the
problem to a maximum independent set problem in polynomial time. It then
proposes a greedy algorithm to generate data placement with balanced recovery
load distribution. Evaluation compares the greedy data placement versus the
random data placement and shows the effectiveness of the solutions.

## Main Contributions

## Details

* Problem
    * Parallel full-node recovery does not imply fast recovery
    * Load imbalance cannot be addressed by random data placement, which also
      increases the risk of data loss without careful scheduling
    * Fine-grained data unit (e.g., sub-packetization) increases the metadata
      overhead

* Solution
    * Formulates the recovery load minimization problem as selecting a set of
      nodes to minimize the weight in the recovery load graph
        * Prove that it's NP-hard by reducing to maximum independent set
          problem
    * Proposes a greedy algorithm to generate data placement without
      fine-grained data unit, and addresses the repair load balancing problem.

* Notations
    * N: # of nodes
    * (n, k, r): EC parameters
    * W: repair load matrix
    * S: # of placement groups (stripes). I will use placement group and
      stripe interchangeably.
    * P_i: the i-th placement group; P_i,j, the j-th block in the i-th
      placement group. The value of P_i,j represents the node id where P_i,j
      stores.
    * Index(P_i, k) = j, if P_i,j = k (stored in the k-th node (out of N))
    * G = (V, E): Recovery load graph, with N nodes
        * E_i,j: the recovery load from node i to node j, **if node i fails**
        *E_i,j is summed up with the recovery load for each of S stripes, that
        sends from node j to node i
        (equation 1).  
    * \[i \in P\]: node i is in the placement group P

* Definitions
    * Node: single disk or machine
    * Placement group: I understand it as stripe (it's not clearly defined in
      the paper)
    * Repair load matrix
        * RS and LRC: n * n matrix, edge weight = 1
        * When the # of parities r > 1, there are multiple possible repair
          matrices, and thus we can choose any one of them.
        * Target for single placement group
    * Repair load graph: summing up the repair load for each placement group

* Assumption
    * Each placement group has the same amount of data
    * **ONLY one stripe will be incoming as new data**

* Problem: Consider **when we add one more stripe into the system**. Our goal
  is to construct an array of P (of size n), where all elements are in V
  (nodes), where the maximum weight of any edge that belongs to the edge set
  is mimimized. (Definition 2)
    * Physical meaning: When we add one more stripe to the system, we want to
      select n nodes to place the new stripe (of n blocks), such that the
      maximum full-node recovery load is minimized (is one) among all N nodes,
      after adding the new stripe. 

* Reducing the problem to finding the maximum independent set problem
    * From a graph G, find at least n nodes (from N) such that there are no
      edges connecting any two nodes.
    * The key idea of the proof: a maximum independent set of n nodes
      comprises nodes that are not connected, thus the edges are with weight
      0. After adding the new stripe, the maximum weight of any edge in this
      independent set becomes 1 (from 0 to 1 with one more block), which is
      minimized.

* Solution: a greedy heuristic to place the new stripe.
    * Input: current recovery load graph
    * Output: n nodes to place the stripe, where the recovery load is the
      smallest possible
    * Algorithm sketch:
        * It iteratively finds n nodes from N nodes.
            * First, randomly select the first node with the smallest weight
            (connecting to the neighbors)
            * Next, filter out invalid nodes (violating fault tolerance)
            * Third: find nodes that can satisfy uniform distribution
            * Fourth: find nodes with the currently smallest weight

* Redistribution of data upon full-node recovery
    * Propose a greedy heuristic (Algorithm 2), which is very similar to
      Algorithm 1
    * Algorithm 2 is repeatedly called to place data for each stripe

* **When new data comes, Algorithm 1 is repeatedly called for each new stripe
  to reduce the maximum load of full-node recovery**

* Discussion: how to handle the situation when new nodes are added (instead of
  new stripes)
    * Limit the number of nodes selected from the new nodes to place the new
      data

* Evaluation
    * The design shows a more random data placement, and smaller variance on
      load distribution
    * The design shows that the system is capable to reduce the variance of
      load distribution upon new disks added
    * The design shows significantly reduced full-node recovery time
    * Performance:
        * Implementation: based on RCStor (SOSP'23 Geometric Partitioning)
        * Evaluate RS, LRC and Clay code
        * Homogeneous network settings
        * Evaluation shows that the placement algorithm significantly reduces
          the full-node recovery time versus the random data placement algorithm

## Strength

* The paper considers an iterative algorithm to generate data placement to
  reduce the full-node recovery time. The problem formulation is interesting,
  although not easy to understand at the beginning. It assumes data are added
  to the system iteratively. Based on the assumption, it designs placement
  algorithm to place each of the new stripe, such that the data are as evenly
  distributed as possible, while the maximum recovery load is reduced. It
  formulates the problem and prove the NP-hardness of the problem. 

## Weakness

* The most important weakness is that the recovery load matrix for each stripe
  is fixed. Even though it's OK for RS code (with n - k = 1) and Clay code
  (with d = n - 1), in general, it's not reasonable for a lot of codes, where
  there are numerous repair load matrices. The assumption is that it picks one
  of the candidate repair load matrices, and uses it for all stripes. Actually
  this assumption overlooks the MDS property, where collecting any k of n
  blocks are able to reconstruct the data.

* It considers the data are iteratively added to the system. Whether the
  algorithm is capable of adjusting existing data placement to a recovery load
  -balanced placement worth exploring.