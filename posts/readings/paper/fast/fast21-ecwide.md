# Reading Notes: FAST'21 ECWide

Title: Exploiting Combined Locality for Wide-Stripe Erasure Coding in Distributed Storage

Conference (FAST'21): [Link](https://www.usenix.org/conference/fast21/presentation/hu)

Journal (): [Link]()

## Summary

This paper proposes combined locality (parity locality and topological
locality) to solve the wide-stripe repair problem in a clustered storage
system. It studies the tradeoff between storage overhead and cross-rack repair
bandwidth for different schemes. It also proposes practical designs to
addresses the single-chunk and full node repair, encoding and update problems.  

## Main Contributions

* Combine parity locality (local parity chunks) and topological locality
  (chunk placements in clustered settings) to reduce cross-rack
  repair bandwidth.

* Parallel encoding and local update schemes to reduce cross-rack transfers

* Implementation (raw and Memcached-based)

## Details

* Problem
    * Repair overhead: increase linearly with k
    * Encoding: increase (not linearly) with k
    * Update: high update penalty of all parity chunks for MDS codes

* Existing works
    * Parity locality: LRCs
        * Problem: high redundancy, caused by small group size
        * Setting: one node in a rack; fault tolerance: tolerates the same
          number of node and rack failures
    * Topological locality
        * No local parity chunks
        * Reducing the rack level fault tolerance for localized repair
          operations. Existing studies focus on minimizing the cross-cluster
          repair bandwidth
        * The overall repair bandwidth is reduced via inner-rack local
          computations
        * The minimum redundancy is preserved, but the cross-rack bandwidth is
          still high (through optimal)

* Idea: combining both locality with limited # of racks and limited # of local
  parity chunks
    * Tradeoff both cross-rack bandwidth and storage overhead for repair

* Design
    * Objective: given the specified node fault tolerance f (any f failures),
      and single rack fault tolerance, redundancy threshold gamma, k,
      determine the parameters that minimizes the cross-rack repair bandwidth
    * Parameters: (n, k, z, r), where z is the # of racks, r is the # of
      cross-rack chunks
    * Focus: single failure repair
    * Parameter choices: choose LRC constructions to make sure c = f, where c
      is the # of blocks in a rack, subject to the single rack fault tolerance
        * Adding linear dependency on given fault tolerance does not improve
          fault tolerance
    * The paper argues that for wide stripes, the overhead for global parity
      blocks is low for node repair, as there are only a very small fractions
      global parity blocks in a node

    * Construction of Combined Locality
        * Given k the maximum allowed redundancy, fault tolerance f, find
          available (r, z) pairs, and r_min with smallest single chunk repair
          bandwidth
        * Based on r_min, minimize the cross-rack repair bandwidth
            * Find n based on r_min
            * put one local parity block and the local groups in (r+1)/c
              racks. Thus, single rack fault tolerance is preserved.
    * Tradeoff analysis
        * tradeoff-between redundancy and cross-rack repair bandwidth under
          the same k and f
    * MTTDL

## Strength

## Weakness

* Is the selection of Azure-LRC general for any (n,k,r)? In Table 3, only a
  specific parameter set is chosen (16, 10, 5), but it looks unfair for
  Optimal-LRC and Azure-LRC+1, because the # of data + global parity blocks
  are uneven. Maybe this is the general case for any (n,k,r) but I'm not sure.