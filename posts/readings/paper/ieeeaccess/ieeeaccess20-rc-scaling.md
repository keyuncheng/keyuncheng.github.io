# Reading Notes: IEEE Access'20 Regenerating code scaling

Title: Efficient Storage Scaling for MBR and MSR Codes

Conference (IEEE Access): [Link](https://ieeexplore.ieee.org/document/9076623)

Journal (): [Link]()

## Summary

This paper explores storage scaling of regenerating codes, specifically, E-MBR
and Butterfly codes, as two representative codes of MBR and MSR codes. It
focus on reducing the scaling bandwidth with the characteristics of code
constructions. It also provides efficient scaling methods for these two
specific codes, respectively. Experiments show that the scaling bandwidth can
be reduced by up to 75% and 43.8% comparing with the centralized scaling
method respectively.

## Main Contributions

* It explores the scaling problem for explicit constructions of MSR and MBR
  codes.

* The scaling bandwidth is proven to be optimal for E-MBR (not for Butterfly)

* It provides a lower bound of scaling bandwidth of Butterfly

* The implementation is shown to have significant scaling performance
  improvement over conventional centralized scaling.

## Details

* E-MBR
    * d = n - 1
    * Most important characteristics: All the blocks of each node have
      duplicates across the other nodes
    * The scaling improvement comes from reducing the migration with the
      duplicated sub-blocks
    * The paper analyzes the cases for n - k = 1 and 2, respectively

* Butterfly
    * Butterfly's encoding (constructing the parity blocks) is a recursive
      process of encoding with a smaller k's code instance
    * Utilizing the old parity blocks to avoid re-encoding of them (as the
      construction is recursive), so as to reduce the scaling bandwidth

* The idea of distributed scaling comes from INFOCOM'18, Hu for RS codes.

## Strength

* Probably one of the earliest works on scaling for regenerating codes

* One significant contribution is to prove the lower bounds for both E-MBR and
  Butterfly code (one specific construction of MBR and MSR);

## Weakness

* I'm curious about the reason why Butterfly can't meet the lower bound of
  scaling bandwidth, as it's not elaborated in the paper. The E-MBR scaling
  bandwidth is easier to understand, and the lower bound can be met naturally.

* Currently, n - k is limited to at most 2. It's not very general. (n,k) is
  going up to at most (6,4), which is also limited. Is it because the
  performance in distributed scaling is not as expected in theory?

* A more general class of codes can be explored.