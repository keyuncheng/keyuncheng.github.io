# Reading Notes: INFOCOM'22 LRC Repair-Scaling Tradeoff

Title: On the Optimal Repair-Scaling Trade-off in Locally Repairable Codes

Conference (INFOCOM'20): [Link](https://ieeexplore.ieee.org/document/9155417)

Journal (TPDS'22): [Link](https://ieeexplore.ieee.org/document/9448455)

## Summary

This paper analyzes the optimal repair-scaling tradeoff of Azure's LRC in
clustered (racked) storage systems. It designs placement strategies for LRC on
the optimal repair-scaling tradeoff curve. Numerical analysis and experiments
shows both the repair and scaling performance improvement over conventional
placement schemes.

## Main Contributions

* Presents the optimal tradeoff under clustered storage systems for LRC

* Presents the algorithm to generate the placement for optimal tradeoff

## Details

* Scenario
    * Clustered storage systems

* Terminologies
    * Upcoding and downcoding
        * corresponds to scaling **down** and **up**, respectively
    * network core: clustered are interconnected by a network core, and shares
      the bw
    * core cluster: (for upcoding) starting at the minimum scaling bw

* Goal
    * minimize cross cluster bw
    * In-cluster bw is considered 0

* Restrictions: MDS property
    * No more than g + i failures are allowed that spans i local groups
    * How to prove: swapping (like the original Azure's LRC paper)

* Placement
    * Placement of local parities plays the most important role in such case
    * Generating the optimal trade-off curve: starting from the minimal
      scaling bw, then move the local parities from the core cluster to the
      other clusters
        * This approach increases the cross-cluster bandwidth (scaling); but
          decreases the repair scaling bandwidth

* Algorithm design (mainly focuses on upcoding)
    * The algorithm summarizes the approach along the trade-off line
    * first: place parity blocks to minimize upcoding cost
    * next: place data blocks to minimize repair cost given minimal upcoding
      cost
        * There is a proof of lowerbound of repairing cost given a fixed
          upcoding cost
    * then: relocating the local parities to generate the scaling-repair
      tradeoff

* Downcoding: gives brief analysis
    * The journal version extended downcoding formally

* Example used for illustration: (k,l,g,cluster) = (12,2,2,7)
    * 12 data blocks are placed at different clusters
    * 2 core clusters stores the parities initially
    
* Evaluation
    * Numerical analysis
        * 8 sets of parameters
        * compare the placemnt of optimal scaling / optimal repairing with
          flat placement
    * Evaluation
        * local cluster (1Gbps, HDD)
        * performance analysis, block size, bandwidth

## Strength

## Weakness

* Focuses on single failure

* Limited parameters spaces: the parameters can only vary for local parities,
  or the # of local groups, as the paper only considers the case when k is
  divisible # of local groups before and after scaling

* Experiment settings: network bandwidth is considered 1Gbps only