# Reading Notes: LRC Regenerating Codes

Title: Codes With Local Regeneration and Erasure Correction

Conference (): [Link]()

Journal (TIT'14): [Link](https://ieeexplore.ieee.org/document/6846301)

## Summary

This paper extends the concept of LRC to codes with multiple local parities,
and introduces local MSR codes and MBR codes, such that the local repair
bandwidth is minimized, and the code is optimal with respect to the minimum distance.

## Main Contributions

* Prove the optimal code (minimum) distance of LRCs with multiple local
  parities (II.A (4)). Pyramid codes falls into this category.

* Uniform Rank Accumulation (URA): the code posessing the URA property if
any subsets of columns have equal ranks (rank accumulation profiles). Any
MDS vector codes is a URA code is MSR code and vice versa.

* Two LRCs with local regeneration is proposed
    * The first one (V.B) assumes all local codes have the same coding
      coefficients (G_L), and the same copy of global parities (Q_delta)
    * The second one (V.C) follows a Pyramid code like spliting of local
      parity blocks (Q_1 to Q_m)

## Details

* There exists a lot of proofs I didn't go into details, including
    * The proof of optimal distance for local MSR / MBR codes
    * Existence of local MSR codes with all symbol locality (only proof the
      existence, without concerning about the field size)
    * Constructions of MBR codes

I would go back when needed.

## Strength

* The first formal work on LRCs with local regeneration.

## Weakness