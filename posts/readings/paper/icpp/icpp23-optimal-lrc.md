# Reading Notes: ICPP'22 Repair placement for Optimal-LRC

Title: Toward Optimal Repair and Load Balance in Locally Repairable Codes

Conference (ICPP'23): [Link](https://dl.acm.org/doi/10.1145/3605573.3605635)

Journal (): [Link]()

## Summary

* For optimal-LRC in clustered storage systems, propose (1) a data partition
  scheme and (2) a node selection scheme to reduce cross-rack repair bandwidth
  and load balance.


## Main Contributions



## Details

* Scenario
    * Clustered storage
    * Azure-LRC, k is divisible by # of local groups

* Problem
    * data partitioning affects the cross-cluster network traffic
    * node selection can affect load balance

* Challenge
    * random data placement causes high cross-rack repair bandwidth
        * Specifically, it focuses on repairing the global parity block
          problem for ECWide

* Motivation: Minimize # of clusters for each group and blocks
    * Data and global parity blocks span less clusters, the cross-rack BW for
      repairing global parity block can be reduced (trivial)
    * Under careful partitioning, the cross-rack BW can be reduced to optimal
      for single and global repair
    * Random node and cluster selection incur storage and network load
      imbalance
        * Considering the access frequency: local parity blocks are more
          commonly accessed
        * Put hot data in less loaded nodes to improve load balance
        * Considering the heterogeneity of clusters and nodes (new nodes and
          new clusters are with higher storage capacity)

* Design
    * Metrics
        * Storage load and bias
        * Network load and bias
    * Physical meaning: to measure the load imbalance (I think the description
      is not clear)
    * Partitioning
        * DRC and NRC are both minimized under single cluster fault tolerance
    * Node selection: select proper nodes in clusters for load balance
        * Measure the potential load of each partition and for each block

## Strength

* Propose a rack and node placement scheme for Azure-LRC for reducing the
  cross-rack bandwidth and load balancing

## Weakness

* In numerical analysis, there is no hotness related analysis for design
  2 (node selection). The design idea is too high level and needs further
  elaboration
  
* The baseline is very trivial. Needs comparative study versus existing
  placement schemes, for example, ECWide.
