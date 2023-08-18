# Reading Notes: TPDS'14 Scale-RS

Title: Scale-RS: An Efficient Scaling Scheme for RS-Coded Storage Clusters

Conference (): [Link]()

Journal (TPDS'14): [Link](https://ieeexplore.ieee.org/document/6819450)

## Summary

This paper introduces Scale-RS, a scaling scheme for distributed erasure coded
storage systems. By scaling, it first transposes the data from the existing
storage nodes to newly added storage nodes (migration), and update parity
blocks by calculating parity delta blocks from the existing data nodes to
minimize data movement (parity update). New incoming data are automatically
added to the updated storage clusters and encoded with the updated redundancy
scheme. Trace-driven analysis and experiments show that Scale-RS achieves the
best read performance among all scaling approaches(no-migration, and data
migration only without parity update).

## Main Contributions

* introduce Scale-RS with three major features
    * Uniform data distribution. By uniform, it means that either old and new
      stripes are encoded with the new (scaled) redundancy scheme.
    * Minimize the data movement for data block relocation
    * Reduced parity block update by calculating the parity delta blocks

## Details

* Baseline: No-data migration and data migration only without parity update
    * No-data migration: data blocks / chunks are not moved. New incoming data
      chunks results in parity update for each stripe.
    * Data migration only without parity update: data blocks are first
      migrated (redistributed), such that the newly added storage nodes will
      also have relocated data blocks. Parity blocks are updated like no-data
      migration.

* Problem of the baseline approaches:
    * No-data migration: load imbalance due to non-uniform distribution of I/O
      among all data chunks (both old and new)
    * Both approaches suffer from higher update penalty, as they need to read
      more data blocks for parity update.

* Scale-RS: split data migration and parity update into two stages, and allow
  parity to be updated for old data stripes. Newly added data are
  automatically encoded with the new redundancy scheme.
  
  * It divide the scaling into the following steps
    * Relocate data blocks. It follows a transposed move pattern, which is,
      filling an old stripe with new redundancy scheme requires data movement
      from **one data node** only.
    * Parity update: The data node responsible for data relocation also needs
      to calculate parity delta blocks, and transfer to the parity node for
      parity update. All old data nodes are able to participate in the process
    * After above steps, old data and parity blocks are all updated.
    * Now newly added data are automatically encoded with new redundancy
      scheme.

* System related design
    * Write aggregation: merge multiple single block request to a larger block
      request (make read write sequential)
    * Decoupling parity update from data migration.
        * Can migrate data at first. Only after the parity blocks are all
          updated, a stripe is considered as finished scaling.
    * Deferred update
        * In parity nodes, it buffers incoming data blocks from other storage
          nodes for scaling by caching old stripes in memory. Then it can read
          multiple parity blocks in a sequential manner.

## Strength

* uniform I/O across storage nodes
    * minimized data movement for **data relocation**
* Reduced I/O for parity updates

## Weakness

* The parity update overhead is not breakdown in detail. **Dedicated parity
  nodes** are considered with the highest network and I/O overheads.

* No analysis / experiments for the system related optimizations