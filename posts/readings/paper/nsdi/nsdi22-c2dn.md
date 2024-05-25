# Reading Notes: NSDI'22 C2DN

Title: C2DN: How to Harness Erasure Codes at the Edge
for Efficient Content Delivery

Conference (NSDI'22): [Link](https://www.usenix.org/conference/nsdi22/presentation/yang-juncheng)

Journal (): [Link]()

## Summary

C2DN proposes a data placement scheme for erasure coding blocks in CDN servers
to address the write imbalance problem incurred by replication.  The key
design models the data placement problem with a maximum flow problem for write
load balancing for erasure-coded blocks.  It further hybrids replication and
erasure coding in CDN servers to reduce cache miss ratio.  Experiments show
that the design can reduce the cache miss ratio and improve the write load
balance in CDN servers.

## Main Contributions

* It considers applying erasure coding in CDN servers to address the write
imbalance problem incurred by replication.

* It models a maximum flow problem to balance the write load for erasure-coded
  blocks.

* It implements the scheme over a real-world CDN system and shows that it can
  reduce the cache miss ratio and improve the write load balance.

## Details

* Trace analysis
    * The trace analysis from real-word CDN clusters (10 serveres) shows that
      (i) Node failures are common and are mostly transient (ii) the write
      load (replication-based) is more imbalanced; (iii) replication based CDN
      cannot remove cache miss spike
    * Note: The definition of node failures in CDN is more strict than the
      traditional definition of node failures in distributed systems.  For
      example, if a node does not meet the SLA, it is considered a failure and
      should be removed from consistent hashing.
* Design
    * Naive design by employing EC into CDN (directly replacing replication)
    also has the write load imbalance problem
        * Read 1 chunk from local cache and K + P - 1 chunks from other servers
        * Can reduce the average byte miss ratio (shown via experiments)
        * Problem: Cache partial hits, where less than K chunks are cached in
          the stripe (partial hit can lead to higher cache miss latency);
          cache partial hit become more frequent during server unavailability
    * Parity load balance via solving max flow problem
        * Every time an server unavailability is detected, it needs to do
          parity rebalancing
        * Heuristic: put parity chunks in least loaded servers
        * Proof: when LRU cache size goes larger, when a chunk is in cache,
          the probability of another chunk of the same stripe is also in cache
          approaches to 1.
* System
    * It employs multiple caching schemes
        * DRAM cache
        * local metadata cache for fast lookup
        * Hybriding replication and EC
    * Hybriding replication and EC
        * replciation for small objs; EC for large objects (when the object
          size is larger than 128 KB)
    * Delayed fetch of sub-chunks (a hand-crafted delayed 20% wait time for
      stragglers, such that parity chunks will be read)


## Strength
    * Good writing
        * Trace-driven analysis to show the write load imbalance problem in CDN
## Weakness
    * The design of CDN is not novel. It is a straightforward application
      of erasure coding in CDN servers, even with the design of parity balancing heuristic.
    * It does not have a good reduction of cache miss ratio without unavailability (only 6.4% on object miss ratio). It simply says that erasure coding takes effects on large objects, but it's not elaborated in the evaluation. A breakdown is needed.
        * Note that the major improvement is that it address cache miss ratio **with** node unavailibility
    * I would like to see the analysis of cache partial hits in the experiments. It's the main problem addressed by C2DN, but there is only very few explanations in the experiments