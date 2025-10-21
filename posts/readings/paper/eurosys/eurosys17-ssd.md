# Reading Notes: EuroSys'17 SSD

Title: The Unwritten Contract of Solid State Drives

Conference (EuroSys'17):
[Link](https://dl.acm.org/doi/10.1145/3064176.3064187)

Journal (): [Link]()

## Summary

This paper investigates how file systems should adapt to fully realize the
potentials of SSDs. It also provides an SSD analysis tool WiseSee and a
simulation tool WiscSim to help file system researchers to evaluate their
designs on SSDs.  The analysis helps SSD and application developers to fully
understand the behaviors of SSDs and how to optimize their usage.

## Main Contributions

## Details


SSD users should follow five main rules:

* (Request Scale rule) SSD clients should issue large requests or many
  outstanding requests
    * Log-structured structures are preferred
* (Locality rule) To reduce translation-cache misses in FTLs, SSDs should be
  accessed with locality.
* (Aligned Sequentiality rule) To reduce the cost of converting page-level to
  block-level mappings in hybrid-mapping FTLs, clients of SSDs should start
  writing at the aligned beginning of a block boundary and write sequentially.
* (Grouping By Death Time rule) To reduce the cost of garbage collection, SSD
  clients should group writes by the likely death time of data.
* (Uniform Data Lifetime rule) To reduce the cost of wear-leveling, SSD
  clients should create data with similar lifetimes.


* To achieve high performance in such an environment, one must
carefully study the workloads of clients and the reactions of SSDs

* Observation \#5: Linux buffered I/O implementation limits request scale.
  This is because Linux buffered read implementation splits and serializes
  requests before sending to the block layer and subsequently the SSD.  In
both buffered read() and mmap(), only a small request is sent to the SSD at a
time, which cannot exploit the full capability of the SSD.
    * In contrast, The direct I/O implementation sends application requests in
whole to the block layer. Then, the block layer splits the large requests into
smaller ones before sending them to the SSD.

* Observation #8 (FS): Delaying and merging slow non-data operations could
boost immediate performance
## Strength

## Weakness