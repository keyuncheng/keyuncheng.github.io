# Reading Notes: paper

Title: Dynamic-EC: an efficient dynamic erasure coding method for permissioned blockchain systems

Conference (Frontiers of Computer Science'24): [Link](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-023-3209-3)

Journal (): [Link]()

## Summary

This paper designs a erasure-coding based permission blockchain system.  It
reduces the storage overhead from prior works (BFT-Store, ICDE'20,
PartitionChain, TKDE'23) by trading off the fault tolerance.  Its motivation
is that prior works always tolerate *f* malicious nodes, and use a fixed
erasure coding scheme that tolerates *f* malicious nodes.  In reality, there
are not as many malicious nodes as *f*, where in most cases, there are only a
very small number of nodes, such that it can use another erasure code with
lower storage overhead for further storage saving.  Dynamic-EC measure the
number of malicious nodes and risky nodes based on a heuristic algorithm, and
select a erasure coding scheme to encode the data.  Experiments show that it
can reduce the storage overhead over BFT-Store and PermissionChain.

## Main Contributions

In my understanding, the only difference between Dynamic-EC and PartitionChain
is the algorithm for voting the malicious nodes, such that the malicious nodes
can be removed from the system. It also adds another set of nodes called
"risky nodes", meaning that these nodes can also be categorized unavailable
(but they will not be removed from the system).

## Details

* Heuristic algorithm for voting the malicious nodes and risky nodes
    * In the heuristic, malicious nodes (that can conduct malicious attacks)
      has a higher weight than risky nodes (unresponsive nodes)
    * After running the heuristic, all nodes are categorized into three
      categories: normal nodes, risky nodes, and malicious nodes. Malicious
      nodes will be removed; risky nodes will not be removed but without
      placing any data until they are responsive.
        * The number of malicious nodes is always no larger than *f*,
          sometimes only one or two.

* EC algorithm
    * Almost the same as PartitionChain: in-block coding.

* Data placement algorithm
    * It places the data by following PBFT algorithm to ensure that the data
      are placed across normal nodes to ensure the fault tolerance.

* Evaluation
    * They consider the **best case** for Dynamic-EC, where almost all nodes
      are considered normal, hence the data are coded in low redundancy codes
      than the one in BFT-Store and PermissionChain, such that the storage
      overhead can be reduced.

## Strength

## Weakness

* I don't agree with the problem proposed by this paper, which to me is an
  artificial problem. It says that the number of malicious nodes can be
  smaller than *f*, then it can use a lower redundancy code for encoding.
  However, in reality, the number of malicious nodes varies and it's possible
  that the number goes up to *f*. The design is actually trading-off fault
  tolerance for storage savings.  However, we don't want to trade-off fault
  tolerance for storage savings, as fault tolerance (i.e., the # of tolerated
  failures) is often a required metric in practice. If the data are already
  encoded in lower redundancy codes with fault tolerance lower than *f* (e.g.,
  1 or 2), then the data are not recoverable even if the number of malicious
  nodes is smaller than *f* (e.g., 3), which leads to data loss.

* The experiments does not cover the "Dynamic" in encoding, such that the data
  is encoded in a fixed coding scheme (although it has lower redundancy than
  BFT-Store).  Once the data are written to disk, the fault tolerance is
  fixed. It does not apply any redundancy transitioning to other coding
  schemes, based on the current measured number of malicious nodes (it's main
  design). It means that Dynamic-EC may store data with multiple coding
  schemes when the number of failures varies from time to time. This is not
  evaluated in the experiments. And I don't think this is a correct design, as
  mixing multiple coding schemes does not guarantee the system can tolerate
  the maximum number of malicious nodes.