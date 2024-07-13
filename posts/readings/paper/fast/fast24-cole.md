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
      storage overhead and degraded write performance 

## Details

* Merkle Patricia Tree
    * A combination of a Merkle tree (hash-based tree for integrity
      verification) and Patricia trie (very similar to Radix Tree, where the
      storage overhead is further reduced)
    * The problem is that MPT has a high storage overhead due to the
      duplicated index structure (Fig. 1) for multiple block states.
        * The index structure cannot be removed as blockchain needs to support
          provenance queries
    * Data structure for indexing the Ethereum transactions and states.
    * Supported query types:
        * Get(): get the latest state from the input address
        * Put(): insert the state with the value of the input address to the
          current block
        * ProvQuery(): get history results for an input range of blocks
        * VerifyProv(): verify through hashing that the results returned by
          ProvQuery() are valid.

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

* Column-based storage
    * Keys are compound keys (address, block_height)； compound keys are
      represented by 64 bit big numbers
    * Values are contiguously stored in the same level for the same address
      (sorted by block height); hence, the MPT's storage overhead is reduced
      (from internal nodes)
    * To retrieve a value, COLE searches the MBTree first and then go to disk
      level with learned indexes 

* LSM-tree structure
    * First level: Merkle B+Tree
    * Next levels: on Disk with learned index

* Write flow
    * Insertion of a state kv pair for the latest block
        * The write flow is very similar to LSM-tree write operation, where
          the compound key (address, block height) is first write to in-memory
          L0 layer (MBTree), then flush to disk in subsequent on-disk levels
          when the previous levels are full (refer to Fig. 4)
    * Index construction
        * Using a learned model referred from PGM-index
            * It's a linear model based on convex hulls, where the disk page
              sizes are model parameters (such that the models are generated
              in a disk-friendly manner)
            * Given a linear model, COLE can predict the location of the
              compound key's position in a file
            * The state's compound key and position are treated as the
              location on a 2-D plane
            * The model updates the convex hulls on the 2-D plane in a
              streaming-based manner; the learned model builds minimal
              parallelogram based on the convex hull for prediction
            * For each layer (memory and disk), an index file based on learned
              index are created
    * Merkle file construction
        * The Merkle file only includes the value files, but not the index
          files 
        * The Merkle files are generated in parallel for all layers and stored
         in multiple Merkle files to increase the write throughput
    * A discussion
        * COLE does not support blockchain forking and designed to work with
          non-forking blockchains
            * Ethereum by default adopts a fork-based design, when multiple
              miners has done over the same set of transactions and broadcast
              over the networks
    * To address the write stall problem for write operation (due to the
      recursive merge operation in Algorithm 1), it proposes an async merge
      algorithm
        * Reason: some straggler nodes can be out-of-sync
        * High level idea: two stages of checkpoints, (1) start; (2) commit
        * Ensure that (1) is sync across nodes
* Read flow
    * Optimization technique: apply bloom filter to both MBTree (memory) and
      Learned indexes (disk) search the keys
    * Get query: very similar to LSM-tree get (in memory with MBTree -> on
      disk with learned index)
    * Provenance Query: Similar to MPT, but without the learned index (as they
      are not constructed with index files)

* Evaluation
    * Single machine; SmallBank for account transfers; YCSB for KVStore
      get/put operations

## Strength

* A natural combination of Learned index + LSM-Tree + Blockchain states

## Weakness