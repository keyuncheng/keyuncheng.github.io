# Reading Notes: TIT'12 LRC

Title: On the Locality of Codeword Symbols

Conference (): [Link]()

Journal (TIT'12): [Link](https://ieeexplore.ieee.org/document/6259860)

## Summary

## Main Contributions

## Details

* It focuses the systematic LRCs where each group have one local parity
  blocks. Especially, the global parities have hamming weight equals to *k*.

* Structure Theorem. For any systematic LRCS with information locality
  (locality for data blocks *r*) and code distance *d*, prove the lower bound
  of number of parity blocks *n - k*, where *n >= k + ceil(k/n) + d - 2*.
  basic Pyramid codes matches the lower bound.
    * I didn't go into the details of the proof.

* Canonical codes
    * Data blocks are divisible by *r*, where *k | r*, and each is assigned
      with a local parity block. Global parity blocks have hamming weight *k*.
        * Example: Pyramid codes
    * Theorem: let d < r + 3. Any systematic code with locality *r* is
      systematic code. The physical meaning is that, when code distance is
      less than r + 3, which means that the local group size is sufficiently
      large, then the code is canonical and thus optimal in distance.
    * Provides an lower bound and upper bound for the locality of **parity blocks**

* Non-canonical codes
    * Existance proof of all-symbol locality, given the sufficiently large
      field size

* Maximally Recoverable codes
    * Cannot have small field size 

## Strength

## Weakness