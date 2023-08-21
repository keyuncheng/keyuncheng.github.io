# Reading Notes: Azure-LRC

Title: Erasure Coding in Windows Azure Storage

Conference (ATC'12): [Link](https://www.usenix.org/conference/atc12/technical-sessions/presentation/huang)

Journal (): [Link]()

## Summary

This paper introduces Windows's Azure Local Reconstruction Codes (Azure's
LRCs). LRC reduces the number of erasure coding fragments that need to be read
when reconstructing the failed data fragments, while still keeping the storage
overhead low. The construction is based on local groups, each of which encodes
partial data fragments.

## Main Contributions

## Details

* WAS originally stores in 3-way replication, until the data reaches a certain
  size, WAS will perform erasure coding on the data. Erasure coding is lazily
  performed in the background.

* Problems: reconstruction takes a long time at the node to read data.

* Azure's LRCs have *k* data fragments, *l* local groups, and *r* global
   parities. *n* total number of fragments, where *n = k + l + r*.
    * Storage overhead: *1 + (l + r) / k*.
    * The repair reads fewer data fragments by reading from local groups. But
   it introduces more storage overhead, as it stores more local parity
   fragments.
    * Single fragment failure in a local group: it reads *l* fragments
      (including *l - 1* data fragments and one parity fragment).

* Azure's LRCs are not MDS codes, where not all multiple failure patterns are
   recoverable. For example, for (6,2,2) Azure's LRCs, if there are four
   failures, where 3 data fragments and one parity fragment are all failed,
   the data are not recoverable, since the remaining parity fragments can't be
   used to reconstruct the remaining 3 data fragments.

* Azure's LRCs achieves *Maximally Recoverable Property*, which can recover
   information-theoretically decodable failure patterns. To elaborate, it
   tolerates (r + 1) failures, but it can not tolerate arbitrary *(l + r)*
   failures. For example, (6,2,2) Azure's LRCs can tolerate arbitrary 3
   fragments failure, and it allows all local groups where each group has one
   single node failure; but it cannot tolerate arbitrary four failures.

* Goal of Azure's LRC: how to design coding equations to decode all the
  information-theoretically decodable failure patterns.
    * LRC coding equations: XOR for local parities; RS for global parities
    * Discuss decodable cases of four failures (not all). The other cases are
      skipped.
    * Comparing the Pyramid codes, Azure's LRCs have smaller finite field
      sizes.
    * An easy method to detect whether the failure pattern is decodable: swap
      the local parity fragment to the failed data fragment, and see whether
      there are more than *r* failures for the **data + global parities**. If
      yes, then the failure pattern is not decodable. 

* Reliability Analysis
    * Markov Reliability Model: the modeling is augmented from standard
      modeling, as LRCs have non-decodable failures. The modeling assumes
      failures are independent.
        * Extension of the modeling to correlated failures: check OSDI'10 (GFS)
    * Average single failure repair rate
    * multiple repair rate: They make an assumption: in practice, the repair
      rates for multiple failures (beyond single failures) are dominated by
      the time taken to detect failure and trigger repair. Thus they set the
      as 1/T, where T is the time to detect and trigger repair.
    * Average repair cost (in number of fragments)
    * Decodability ratio: the ratio of decodable failure patterns to all
      enumerated failure patterns.
    * Storage Overhead vs Reconstruction Cost (Figure. 4): there exists a
      tradeoff between the storage overhead and the reconstruction cost.
    * Azure reports the number of fault domains as 20.
    * Comparisons: LRC lower bound curve vs RS lower bound curve for fault
      domain <= 20
        * LRC achieves higher cost and performance trade-off than RS.
    * Comparisons: LRC vs other code constructions: HoVer, Stepped
      Combination, Weaver and RS codes

* WAS chooses LRC (12, 2, 2) as the example under the 20 fault domains.
    * EC is implemented in the stream layer after the blocks are sealed.


## Strength

1. LRC saves significant I/Os and bandwidth during reconstruction when compared to RS.

## Weakness

1. LRCs are non-MDS codes. Additional storage overhead is introduced for the same fault tolerance.

2. LRC is optimized for reconstructing data fragments but not (global) parity fragments. In terms of parity reconstruction, Weaver codes, HoVer codes and Stepped Combination codes can be more efficient.