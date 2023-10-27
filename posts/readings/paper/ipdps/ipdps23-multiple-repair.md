# Reading Notes: IPDPS'23 multiple repair

Title: Boosting Multi-Block Repair in Cloud Storage Systems with Wide-Stripe
Erasure Coding

Conference (IPDPS'23): [Link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10177413)

Journal (): [Link]()

## Summary

This paper combines the idea of centralized repair (collect data for repair at
a specific node) and independent repair (repair pipelining) to solve the
multiple repair problem in a heterogeneous network setting, under the
wide-stripe setting. Evaluation under the heterogeneous network settings
demonstrates the effectiveness of the combination.

## Main Contributions

* Propose a theoretical model to combine the centralized repair and
  independent repair, such their repair time are equal.

* Extend to hierarchical settings and multiple node repair problem.

* System implementation based on OpenEC

## Details

* Modeling for multiple block repair with **RS codes**
    * Centralized repair downloads k blocks to a node and distribute the
      repaired blocks to the new nodes
    * Independent repair uploads and downloads x blocks at each node and
      repair in parallel (same as repair pipelining)
    * A block can be physically divided into two parts, where for each part we
      adopt one repair approach (either centralized or independent)
    * Thus, the modeling can be used to calculate the tradeoff point, such
      that the time for centralized repair and independent repair are the same
        * By solving a linear equation
    * It considers the heterogeneous network setting, where the bandwidth
      between nodes are different (assume they are known in advance)
    * Based on the modeling (with given coding parameters, network bandwidth
  (upload and download) for each node, block size, etc.), we find the point
  where both of these two approaches takes the same time to finish

* Extension to hierarchical setting
    * Only focus on cross-rack network bandwidth

* Multi-node repair
    * Assign the repair on different nodes via a combination of LFS
      (frequency) or LRS (recently) approach

* Evaluation
    * Generates the heterogeneous network settings
    * Settings
       * Over EC2 with **88** nodes, 10Gbps network, 2vCPU, 8GiB memory


## Strength

* Combines both approaches

## Weakness

* Design (it's good enough for a rank B paper)
    * Trivially combines both existing two approaches
    * Wide-stripe is not the focus

* Evaluation
    * To me it has many problems
    * The network setting is called a dataset, but I would consider it as an
      list of upload and download bandwidth. I can't find the dataset on the
      code repo
    * The redundancy is high (e.g., (64, 25)), I would not call it
      wide-stripes
    * Figure 8 has many typos
    * For exp6, the time breakdown is not reasonable
        * The operations performed are in parallel, thus we cannot directly
          count the time by separating the two sub-blocks