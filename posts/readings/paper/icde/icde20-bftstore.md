
# Reading Notes: ICDE'20 BFT-Store

Title: BFT-Store: Storage Partition for Permissioned Blockchain via Erasure Coding

Conference (ICDE'20): [Link](http://ieeexplore.ieee.org/document/9101675)

Journal (): [Link]()

## Summary

This paper propose BFT-Store, an EC-based permissioned blockchain system to
reduce the storage overhead over the traditional replication-based blockchain.
It integrates EC and PBFT (Practical BFT for permissioned blockchain)
consensus algorithm. It also considers scaling in blockchain with a
re-encoding based approach.

## Main Contributions

## Details

* Challenges
    * When n = 3f + 1, how to ensure at least 2f + 1 honest nodes will receive
      valid EC chunks?
    * How to scale the blockchain when nodes join or leave?
    * How to ensure data read performance when data are erasure-coded?

* Design
    * Cross-block coding with RS(k,m) = (n - 2f, 2f): each set of n - 2f data
      blocks are grouped to generate 2f parity blocks, which collectively form
      a coding group; 
        * Reason to choose (n - 2f, 2f): to ensure BFT (based on PBFT
          protocol)
    * BFT-Store hybrids EC with replication to ensure data read performance,
      at the cost of higher storage overhead (but still lower than full
      replication)
        * Each block is replicated for *c* copies, and distributed to a
          specific set of nodes
        * For *N* nodes, the overall storage overhead is reduced from O(N) to
          O(c) (the paper says the storage overhead is reduced to O(1), but I
          think this is wrong)
    * Encoding:
        * On each node:
            * Collect n - 2f data blocks
            * Encode to generate 2f parity blocks
            * It ensures that each block is replicated for c times in a coding
              group
    * Read:
        * Step 1: Check if a local systematic read is feasible (the block is
          replicated in its local storage) 
        * Step 2: Check if other honest (available) nodes store the
          (systematic) block
        * Step 3: Perform decoding: broadcast data read to n-f nodes and
          retrieve n - 2f blocks (it tolerates f Byzantine failed nodes) to
          perform decoding
    * **Scaling**
        * Note: the workflow described in the paper is unclear and has
          techinical errors. Here, I describe the flow on my understanding
        * Overall: BFT-Store performs a re-encoding based approach for scaling
        * Assume additional nodes are added to the storage system, where there
          are *n'* new nodes, and it tolerates *f'* BFT failures.
        * Step 1: Leader node (selected in a round-robin fashion) sends a
          **decode** message to all other backup nodes storing EC data
        * Step 2: Backup nodes send chunk-set messages to the Leader node for
          decoding. The chunk-set messages **include ALL** the locally stored
          chunks.
        * Step 3: 
            * 3-1: For each coding group, the Leader node collects n - 2f
          blocks and performs decoding to recover the original n - 2f data
          blocks.
            * 3-2: It sends a collection of new n'-2f blocks to all n' - 1
              backup nodes to perform (n' - 2f', 2f') encoding
        * Step 4: 
            * 4-1: Leader sends re-encode message to all Backup nodes (which
          chunks to collect)
            * 4-2: Each Backup node performs encoding based on the new set of
              blocks and deletes its originally stored data from the orignal
              coding scheme.
        * Step 5: Each Backup node sends re-encoding-finish message to Leader
        * It ensures that the blocks remains available during scaling operations

* Implementation
    * It implements over Tendermint (PBFT-based protocol for consensus)

* Evaluation
    * For each data point, it assumes a fix set of nodes (and does not vary
      the number of nodes at run-time)
    * It compares storage savings with full-replication based scheme
    * It compares read latency with full-replication based scheme


## Strength

* First work to integrate EC and PBFT consensus for permissioned blockchain

* The work clearly describes the encoding and decoding operation, and it's
  clear and it can reduces the storage overhead from O(n) to O(c)

## Weakness

* The design of scaling is unclear and have technical errors
    * First, the decoding of **ALL** stripes is performed on **one elected
      leader node**. It's a centralized approach and it's definitely the
      performance bottleneck.
        * All backup nodes send the locally stored blocks to the leader node
          to perform decoding. As each block is replicated for *c* times, then
          the leader node will receive *c* times of stripes and the
          performance must be bad
        * **BFT-Store does NOT evaluate the scaling performance** (e.g, what
          is the scaling performance overhead when the number of nodes is
          **increased/decreased at run-time**)
    * Second, how the data blocks of newly generated stripes of (n' - 2f',
      2f') are placed is not described. It assumes that all original blocks of
      the previously coded blocks are **removed**, and all new stripes are
      generated from scratch. It means that after scaling, **ALL data** are
      written to BFT-Store from scratch. It must have a bad performance.