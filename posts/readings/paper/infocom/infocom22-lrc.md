# Reading Notes: INFOCOM'22 Scaling for LRC

Title: Optimal Data Placement for Stripe Merging in Locally Repairable Codes.

Conference (INFOCOM'22): [link](https://ieeexplore.ieee.org/document/9796704/)

Journal (): [link]()

## Summary

This paper studies redundancy transition for LRC, especially, merging multiple
small LRC stripes to a large stripe. It first shows that random placement
introduces high transition bandwidth, and propose two specific placement for
two specific merge regimes, named aggregated merging and dispersed merging.
They are provenly minimizing the cross-cluster scaling bandwidth, while
preserving the repair bandwidth.

## Main Contributions

* Formally prove that the random placement introduces high transition
  bandwidth.

* Introduce two specific data placements for aggregated merging and dispersed
  merging, to minimize cross-cluster scaling bandwidth.

## Details

* aggregated merging: fix (1) the number of global parities; (2) group size,
  merge the data and local parities

* dispersed merging: fix (1) the storage redundancy and (2) group size, which
  is the initial n - k, and final n - k

* Challenges: the merging bandwidth for two types of merging is high;
  specifically, the relocation bandwidth is high for aggregated merging; the
  recalculation bandwidth is high for dispersed merging, as it needs to
  calculate more parities.

* Proof: 5 propositions to prove the issues for the two problems

* Design:
    * Key idea: control the number of blocks to be placed in the same cluster,
      or the number of clusters for a stripe and placement.

    * Algorithms and tradeoff analysis: recalculation cost and migration cost
      for aggregated and dispersed merging represents the two extremes.

    * Optimality: any random placement can be converted into prescribed
      placement.
        * Prove the lower bound of cross-cluster transition bandwidth of x
          small LRC stripes.

## Strength

* The parameter spaces supported is larger than INFOCOM'20. The two prescribed
  placements are achievable, which means they can converted from any
  placements.

* Extensive experiments
    * wide parameter selection, from k = 4 to k = 20.

## Weakness

N/A for now