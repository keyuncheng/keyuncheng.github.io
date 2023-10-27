# Reading Notes: ICPP'22 Repair placement for Optimal-LRC

Title: Repair-Optimal Data Placement for Locally Repairable Codes with Optimal
Minimum Hamming Distance

Conference (ICPP'22): [Link](https://dl.acm.org/doi/abs/10.1145/3545008.3545038)

Journal (): [Link]()

## Summary

This paper studies redundancy transition for a specific LRC construction,
Optimal-LRC, which is proven to have optimal minimum hamming distance. It
first prove flat placement and random placement incur high cross-cluster
repair bandwidth.  It proposes an optimal data placement to minimize the
cross-cluster repair bandwidth, by placing the block groups to a minimum
number of clusters, subject to a single cluster fault tolerance.
Implementation is based on Memcached.

## Main Contributions

* Propose an optimal data placement in terms of cross-cluster repair traffic
 over clustered data storage with Optimal-LRC.

* Prototype atop Memcached with the implementation of Optimal-LRC (which is
  new and now **opensourced**).

* Extensive experiments show that optimal data placement reduces the degraded
  read time over flat and random placement by up to 86.2% and 69.2%, reduces
  the full-node repair time by up to 7.7x and 5.6x.

## Details

* Difference between Optimal-LRC and Azure-LRC, Xorbas, ...
    * All groups can be locally repaired within groups.
    * In theory: minimum hamming distance.
    * Extended idea in this work: single-cluster fault tolerance

* Challenges:
    * Random placement has limited repair performance improvement over flat
      placement (with one example for illustration)
    * Inefficient to **directly apply** the techniques for Azure-LRC, as the
      construction and fault-tolerance semantics are different.

* Design
    * Data placement to minimize DRC and NRC (single block and single node
      repair cost)
    * Key idea:
        * Place every d - 1 blocks of each group to a seperate cluster, so as
          to minimize the number of clusters spanned by each group.
        * It's guaranteed to minimize DRC and NRC.
        * The algorithm is very straightforward, limiting the number of blocks
          within d - 1 (d is the hamming distance) (that's the reason why
          AzureLRC is not directly applicable here).
    * It then design single block repair algorithm
        * Introduce a concept: helper cluster, for localized repair
        * Helper cluster does the cross-cluster network transmission, while
          the cluster with the failed block does the decoding.

* Implementation
    * I didn't look into the details. It's based on Memcached, and centralized
      (or proxy based).

* Evaluation
    * Over local cluster and based on HDD like NCS testbed 1.
    * they compare **4 constructions** of LRC (Azure, Azure+1, Xorbas and
      Optimal-LRC), like ATC'18
    * parameters supported: from k = 8 to k = 12; d = 3 to d = 5

## Strength

* Significant performance improvement for single block and full-node repair
  compared with flat and random placement.

* The design is very simple and straightforward, and to me it's tailor made
  for Optimal-LRC, which has a fixed group size and all based on hamming
  distance.

## Weakness
