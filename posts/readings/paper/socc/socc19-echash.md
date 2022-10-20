# Reading Notes: SoCC'19 ECHash

Title: Coupling Decentralized Key-Value Stores with Erasure Coding

Conference (SoCC'19): [link](https://dl.acm.org/doi/10.1145/3357223.3362713)

Journal (): [link]()

## Summary

When consistent hashing is combined with erasure coding and applied to
decentralized KV-Store, there exists high parity updates and cannot handle
degraded read caused by scaling. This paper introduces introduces an erasure
coding model FragEC, which incur no parity update for storage scaling for
decentralized KV-Store. It addresses the degraded read issue by combining
consistent hashing. It then implements ECHash, an in-memory KVStore based on
memcached. Experiment shows that ECHash achieves better scaling performance
than baseline erasure coding implementation over memcached.

## Main Contributions

* FragEC, or fragmented erasure coding: one data chunk can be divided into
  sub-chunks and can mapped to multiple nodes (for consistent hashing with
  multiple rings).

* Design consistent hashing based on multiple hash rings, which partition
  nodes into multiple isolated zones. One hash ring corresponds to one zone.

* Improve node repair performance over baseline approach by supporting the
  repair of sub-chunks.

## Details

* Background
    * Consistent hashing: reduce the re-hashing overhead when scaling.
        * Problem of consistent hashing: load imbalance.
    * Scaling
        * Vertical scaling: add resources to each node
        * Horizontal scaling: add nodes
    * Scenario: (n, k) remains unchanged!

* Setting
    * number of storage nodes increases / decreases -> (scale down or scale
      up)

* FragEC
    * TBD

## Strength

## Weakness