# Reading Notes: OSDI'25 Stripeless

Title: Stripeless Data Placement for Erasure-Coded In-Memory Storage

Conference (OSDI'25):
[Link](https://www.usenix.org/conference/osdi25/presentation/gao)

Journal (): [Link]()

## Summary

This paper proposes an erasure-coded distributed in-memory KV-store called Nos
that adopts a "stripeless" redundancy scheme to achieve low latency and high
throughput compared with the baselines. Although it calls "stripeless" data
placement, the underlying idea is to hybrid replication and XOR-based
one-parity coding. It adopts a combinatorial data placement strategy called
SBIBD to ensure multi-node fault tolerance for primary-backups.

## Main Contributions

* Hybrids replication and XOR-based one-parity coding for in-memory KV-store.

* Implementation of Nos, an in-memory KV-store with the proposed stripeless
  data placement and achieves low latency and high throughput compared to the
  STOA baselines.

## Problem

* For fast in-memory KV-stores, EC operations with stripes brings overheads
  (in bandwidth and computation).
    * Intra-object (each obj will be split to k chunks): I/O fanout; not good
      for small objects
    * Inter-object (ensemble multiple objects to a single stripe): metadata
      overhead, memory consumptions
        * Static data placement (e.g., hashing): cannot adapt to dynamic
          workload changes
        * Dynamic data placement: centrally coordinated metadata service will
          be the performance bottleneck and leads to single-point-of-failure;
          such scheme also have high metadata overhead for small objs.

## Details

* Parameters (k, p)
  * k: number of blocks in a fault-tolerant group
  * p: number of tolerable blocks in a fault-tolerant group


## Strength

* Limited memory overhead (actually) compared with replication and EC-only
  schemes.

* Close-to-replication latency and throughputs for in-memory operations for
  YCSB workloads.

## Weakness

* Limited parameter settings for short k for erasure coding. Thus it has
  higher memory overhead than EC-only schemes

* Requires fast RDMA access (where the bandwidth is still the bottleneck)

* I expect to see the amortized costs (in blocks) of reconstructing any lost
  chunk for different values of k and p (although this may not be necessary
  for OSDI).

* It's necessary to provide the reliability analysis of different values of k
  and p between different schemes.

* It says split scheme has high I/O fanout and put significant overhead on the
  network. This may not be true, and high I/O fanout may be good for
  parallelization.