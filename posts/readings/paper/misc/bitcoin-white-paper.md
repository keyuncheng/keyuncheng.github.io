# Reading Notes: Bitcoin White Paper

Title: Bitcoin: A Peer-to-Peer Electronic Cash System

Conference (): [Link](https://bitcoin.org/bitcoin.pdf)

Journal (): [Link]()

## Summary

This paper proposes bitcoin, a peer-to-peer electronic cash system (often
referred to blockchain). The system is designed to allow online payments
through decentralized consensus (i.e., without a trusted third-party to verify
transactions).  The key problem is to address the double spending problem in
p2p network.


## Main Contributions

* Propose blockchain

* Use chained hashing with timestamps and Proof-of-Work to solve double spending problem

## Details

* Timestamp server (to address double spending): a hash is computed by
  combining the timestamp of a block and the block itself.  The hash is
  broadcast to peered nodes for verification. It ensures that the block (with
  transactions) is enforced to be generated after the previous blocks.

* Proof-of-Work: use CPU power to scan (enumerate) for a value, such that the
  hash of the block filled with the scanned value starts with a certain number
  of 0s.  The verification of PoW is simple, but the enumeration process is
  very difficult (with a exponential complexity of the # of zeros)

* Some strategy to reclaim space: pruning on the Merkle tree

## Strength

The first work of blockchain-based decentralized p2p E-cash system

## Weakness

Known issues: expensive in computation power for the miners