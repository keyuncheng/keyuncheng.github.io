# Reading Notes: FAST'24 COLE

Title: COLE: A Column-based Learned Storage for Blockchain Systems

Conference (FAST'24): [Link](https://www.usenix.org/conference/fast24/presentation/zhang-ce)

Journal (): [Link]()

## Summary

COLE is a blockchain-based storage that leverages learned index and LSM-tree
to reduce the storage overhead introduced by Merkle Patricia Trie (MPT).  It
puts the values of blockchain states in a column-based manner, where the
values with the same address (sorted by block ids) are sequentially stored to
reduce the write overhead.  Compared with the MPT based Ethereum-based
blockchain with KV-store storage backend, COLE achieves significant storage
saving while having a better throughput.

## Main Contributions

* It leverages learned index and LSM tree to reduce the storage overhead for
  indexing incurred by MPT.
    * Directly applying Learned indexing to Merkle Tree introduces even higher
      storage overhead. 

## Details

(Partially done)

* Merkle Patricia Tree
    * A combination of a Merkle tree (hash-based tree for integrity
      verification) and Patricia trie (very similar to Radix Tree, where the
      storage overhead is further reduced)
    * The problem is that MPT has a high storage overhead due to the
      duplicated index structure (Fig. 1) for multiple block states.
        * The index structure cannot be removed as blockchain needs to support
          provenance queries
    * Data structure for indexing the Ethereum transactions and states.

* Idea: 
    * Learned index can reduce the storage costs and query times in database
    storage (compared with the conventional B+ tree that has O(logf_n) depth)
  and O(n/f) nodes for indexing.
    * LSM tree are used to reduce the write overhead of the learned index. By
      following the column-based DB design, COLE sequentially appends the
      latest state values to the same state address for faster provenance
      enquiry results.
    * The first level (with the latest block states) are stored in the first
      level of LSM tree; the latter levels are compacted to the disk (called
      disk levels) through async compaction to reduce the write latency.

* Write flow (Partial)
    * Insertion of a state kv pair for the latest block
        * Using a stream-based manner (Fig. 4); where the old state are
          flushed from memory to disk through compaction
        * The write flow is very similar to LSM-tree write operation, where
          the compound key (address, block height) is first write to in-memory
          L0 layer, then flush to disk in subsequent layers when the previous
          layers are full
        * Question: blockchain's write frequency is about one block per
            10s, what's the performance overhead in reality?
    * Index construction
        * Using a linear model called PGM-index to reduce the I/O cost for
          read operation
            * Note: I did not understand how to model over the compound keys
              with the help of convex hull
            * Question: will blockchain's write overhead affects model
              training?
    * Merkle tree construction (as file)
        * Streamingly generate the merkle files, but in a concurrent way: all
          layers are consequently write to multiple merkle files to increase
          the write throughput, due to the independence of different Merkle
          Hash Tree layers (I need to validate whether this assumption is true)
    * A discussion
        * COLE does not support blockchain forking and designed to work with
          non-forking blockchains
            * Ethereum by default adopts a fork-based design, when multiple
              miners has done over the same set of transactions and broadcast
              over the networks
    * To address the write stall problem for write operation (due to the
      recursive merge operation in Algorithm 1), it proposes an async merge
      algorithm
        * Details: TBD
        * Question: any consistency issue?
* Read flow (TBD)

## Strength

## Weakness