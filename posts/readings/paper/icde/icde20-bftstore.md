
# Reading Notes: ICDE'20 BFT-Store

Title: BFT-Store: Storage Partition for Permissioned Blockchain via Erasure Coding

Conference (ICDE'20): [Link](http://ieeexplore.ieee.org/document/9101675)

Journal (): [Link]()

## Summary

This paper propose BFT-Store, an EC-based permissioned blockchain system to
reduce the storage overhead over the traditional replication-based blockchain.
It integrates EC and BFT consensus to reduce the storage overhead. It also
considers scaling in blockchain with a re-encoding based approach.

## Main Contributions

## Details

Challenges
* When n = 3f + 1, how to ensure 2f + 1 honest nodes have received valid EC
  chunks.

* How to scale the blockchain when more nodes join.

* How to ensure data read performance with all data erasure-coded

* Design
    * Cross-block coding: group n - 2f data blocks as a coding group and
      perform coding; each node preserves a unique chunk and hash values for
      verification
    * Coding scheme: (k,m) = (n-2f, 2f) RS code to ensure BFT
    * Replication-based EC to ensure data read performance, at the cost of
      higher storage overhead (but still lower then full replication)
    * Encoding: It places each set of replicated n - 2f blocks are placed
      across multiple honest nodes, to ensure decoding with n - 2f honest
      nodes (chunks)
    * Read: (1) check if systematic read for the block is available (with the
      replicated blocks); (2) otherwise, use EC to decode unavailable block
    * Scaling
        * It's a re-encoding based approach for BFT
        * Leader sends decode message to all nodes
        * Backup nodes send chunk-set messages to the leader (without chunk
          yet)
        * Leader sends re-encode message to Backup nodes (which chunks to
          collect), and performs decoding
        * Backup sends coding-finish message to Leader
        * During re-encoding, the blockchain remains available when some
          blocks are in the process of encoding-decoding

* Implementation
    * It implements over Tendermint (PBFT-based protocol for consensus)

* Evaluation
    * It compares storage savings with full-replication based scheme
    * It compares read latency with full-replication based scheme


## Strength

* First work to integrate EC and BFT consensus for permissioned blockchain

## Weakness

* The design of scaling is not clear
    * How the blocks are en-coded and replicated (based on its write flow) is
      not described clearly
    * Figure 2 is too high level and does not elaborate on how newly generated
      data and parity blocks are placed

* Evaluation
    * It does not evaluate how the storage overhead and write/read latency
      varies when more nodes join on-the-fly (this is when re-encoding is
      triggered)