# Reading Notes: TKDE'23 PartitionChain

Title: PartitionChain: A Scalable and Reliable Data Storage Strategy for Permissioned Blockchain

Conference (TKDE'23): [Link](https://ieeexplore.ieee.org/document/9656652)

Journal (): [Link]()

## Summary

This work proposes PartitionChain to address BFT-Store's problem, where the
computation overhead and network transmission overhead are high for blockchain
initialization and re-encoding. In addition, it enhances security, as
BFT-Store does not implement the security check (e.g., measuring malicious
behaviors).

## Main Contributions

## Details

For this paper, I merely focus on the storage overhead reduction

* Data partitioning: PartitionChain applies inner-block coding, where each
  block needs to be divided into pieces and perform encoding.
    * The benefit: for decoding, it only needs to retrieve the pieces for the
      block itself, rather than other blocks.
    * The drawback: decoding is required for ALL blocks.

* Protocol: also PBFT + RS code

* Encoding: similar to BFT-Store, but the coding is performed on a per-block
  basis; it also applies CLAS(Certificate Aggregate Signature) to enhance
  security for BFT.

* Decoding: it's also similar to BFT-Store.  It needs election of a leader
  that's likely to be honest, and it will decode the block by retrieving valid
  pieces (from both honest and malicious nodes) of original blocks.

* Scaling: in my opinion, the scaling process for data re-encoding is the same
  as BFT-Store. The difference is the data verification process (in other
  words, PartitionChain verifies the data integrity of the original block
  before scaling).

* Benefits of PartitionChain over BFT-Store
    * Computation overhead reduction for decoding: as it limits the size of
      the chunk, and no cross-coding is performed, then the amount of data for
      decoding a block is definitely reduced.
    * The re-initialization overhead of PartitionChain is reduced from BFT-Store

## Strength

* PartitionChain out-performs over BFT-Store mainly from the security aspect 

* The re-initialization overhead of PartitionChain is reduced from BFT-Store,
  as some nodes doe snot need to re-encode all data

## Weakness

* I think the evaluation is not sufficient, and the comparisions between
  PartitionChain and BFT-Store are not fair.  Especially, the
  encoding/decoding throughput is on a per-block basis, that is to say,
  cross-coding must be of higher network transmission overhead inner-block
  coding.  However, the drawback of inner-block coding, is that whenever a
  block is generated, coding needs to be performed immediately, which also
  incur significant computation/network overhead. Instead, cross-coding is
  performed on a per-batch basis, where blocks are grouped together and coded