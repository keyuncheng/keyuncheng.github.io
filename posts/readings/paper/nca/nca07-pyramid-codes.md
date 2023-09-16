# Reading Notes: NCA'07 Pyramid Codes

Title: Pyramid Codes: Flexible Schemes to Trade Space for Access Efficiency in Reliable Data Storage Systems

Conference (NCA'07): [Link](https://ieeexplore.ieee.org/document/4276609)

Journal (TOS'13): [Link](https://doi.org/10.1145/2435204.2435207)

## Summary

This paper proposes Pyramid Codes, the coding scheme before the formal study
of LRC. The goal of Pyramid codes is to trade storage overhead (higher than
MDS codes) for degraded read efficiency.

## Main Contributions

* Propose Pyramid codes to trade storage overhead for degraded read
  efficiency.

* (Informally) Study the maximally recoverable property (decode all
  information-decodable failure patterns).

## Details

* Basic Pyramid Codes
    * The code is systematic
    * Basic Construction
        * Construction
            * Step 1: Start from MDS(k, x + y) code, where there are *k* data
              blocks and *x + y* parity blocks
            * Step 2: Keep *y* parity blocks as global parity blocks. Suppose
              there are *l* local groups. It breaks *x* parity blocks into
              *xl* local parity blocks. Each group has *x* local parity
              blocks, where the row of the coefficient matrix corresponding to
              the local parity blocks has non-zero entries for the elements in
              the local group.
            * In total, it has *xl + y* parity blocks
        * Property: it tolerates arbitrary x + y failures; it's not Maximally Recoverable
    * It studies the decodability of all erasure patterns. There are some
      failure patterns (larger than the total number of parity blocks) that
      cannot be recoverable.

* Decodability (Recoverability)
    * Tanner graph (bipartite graph)
        * Left nodes: data blocks
        * Right: parity blocks
        * Edges: if a data block participates in the computation of parity
          blocks
            * A simplified graph: failed data blocks + available parity blocks
    * Examine by maximum matching
        * If the bipartite graph has a maximum (full-size) matching, then it
          is recoverable
    * Necessary condition for recoverability
        * Proved use a contradiction with Bipartite graph and minimum cover
          set
        
* Generalized Pyramid Codes
    * All blocks are local parity blocks, which means each parity block only
      covers a subset of data blocks
    * It's Maximally Recoverable
    * Field size: Comb(n, k - 1), guaranteed to be searchable
        * The proof is skipped
    * The decodability is solvable by maximum matching
    * Decoding function
        * Needs to be searched for EVERY single erasure pattern, including
          single block recovery and multiple block recovery
            * The search algorithm is through bipartite matching
    * Have stronger decodability than the basic Pyramid Codes, due to its
      flexible configurations
        * Don't have any global parity blocks

## Strength

## Weakness

* The field size of both basic and generalized pyramic codes is very high,
  which makes it not practical to implement (as claimed in ATC'12)

* The storage overhead of generalized pyramid codes is also high, considering
  the horizontal and vertical parity settings