# Reading Notes: SRDS'22 XHR-Code

Title: XHR-Code: An Efficient Wide Stripe Erasure Code to Reduce Cross-Rack Overhead in Cloud Storage Systems

Conference (SRDS'22): [Link](https://ieeexplore.ieee.org/document/9996847/)

Journal (): [Link]()

## Summary

This paper proposes XHR-Code to address the multiple failures repair overhead
from ECWide, which applies Azure-LRC under the wide-stripe hierarchical
settings. It adds an intermediate layer of locality encoded by Hitchhiker
between the XOR local parities and global parities. It also controls the
storage overhead by enlarging the local group size, while keeping the number
of racks small. Experiments shows its effectiveness.

## Main Contributions

## Details

## Strength

* The Hitchhiker local parity encodes the data blocks **horizontally** from
  the rack level, which is new.

## Weakness

* Overall, this paper has limited design novelty, which starts from
  ECWide, and adds a layer of local parity blocks similar to pyramid codes
  with three levels of hierarchy

* The design has many typos and makes the reading very difficult to
  understand. Also, the design is not accurately described especially for the
  Hitchhiker layer. What should be the number of rack groups? How many racks
  should one rack group contain? From the figures, it looks that every rack
  group has exactly *z - 1* racks; however, the texts are not described
  clearly. Thus, the exact configurations appeared in the evaluation cannot be
  fully understood.
  
* For XHR-Code itself, how it makes the tradeoff between storage overhead,
  single parity block repair bandwidth, and multiple parity block repair
  bandwidth is not clear. Given the same storage overhead, if we add
  additional local parity blocks to protect the rack level fault tolerance,
  the number of racks is reduced, however, the local group size also becomes
  larger. Thus, the single parity block repair performance will also be
  degraded. This is not discussed in the paper.