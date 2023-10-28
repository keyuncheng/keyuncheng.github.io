# Reading Notes: ATC'21 RepairBoost

Title: Boosting Full-Node Repair in Erasure-Coded Storage

Conference (ATC'21): [Link](https://www.usenix.org/conference/atc21/presentation/lin)

Journal (): [Link]()

## Summary

This paper proposes a repair scheduling scheme called RepairBoost to solve the
single full-node repair problem (1) load-balance the upload / download traffic
across different storage nodes; (2) parallelize the repair of multiple
independent blocks from different stripes to fully utilize the network
bandwidth at each time slots. It further propose extensions to multiple node
repair and heterogeneous network settings. Experiments over EC2 shows the
effectiveness of the proposed repair scheme.

## Main Contributions

* Modeling and algorithm
    * Step 1: Characterize repair solutions (algorithms) via Directly Acyclic
      Graphs (DAG) called RDAG
        * See the example of RDAG for PPR in Figure 6.
        * Difference with ECDAG (FAST'19 OpenEC): the vertices models the
          nodes, the edges models the dependencies on linear combinations
    * Step 2: Load balancing by assigning the vertices of multiple RDAGs
      corresponding multiple blocks (from independent stripes) to physical
      nodes
        * Core of the assigment algorithm: sorting the intermediate vertices
          by the number of blocks to upload / download, and do a balance
          assignment
            * Basiclly it's a greedy algorithm
    * Step 3: Scheduling the repair operations
        * Constructing multiple maximum flows, and reducing the sizes of
          multiple RDAGs simutaneously
        * Repeat the process until all vertices are handled (i.e., all leaf,
          intermediate and final blocks are assigned to corresponding nodes in
          a scheduled way)
* Extensions
    * Multi-node repair scheduling
        * Repair each node individually
        * Prioritize the stripes with more blocks to repair, or with popularly
          accessed chunks
    * Heterogeneous environment
        * deduce the time to upload / download a chunk first
            * Make sure that the upload / download speed for a chunk is almost
              similar (this is a little weird)
        * Sort and choose the links by the available bandwidth first
    * Adaptation to network conditions
        * Monitor the run-time network bandwidth, and proactively adjust the
          repair solutions of the next sub-processes
* Implementation
    * Standalone + HDFS integration (similar to OpenEC)
* Evaluation
    * AWS EC2 Deployment: similar to OpenEC with 17 instances\
    * Coding schemes: RS code, LRC and Butterfly codes
    * Repair algorithms: conventional, PPR and ECPipe


## Details

## Strength

* A novel modeling to characterize the repair solutions for full-node repair,
  which load-balances the repair load and effectively parallelizes the repair
  process for single blocks from multiple stripes

* Implementation and extensive evaluation

## Weakness

* I doubt about the complexity when it models the codes with
  sub-packetization, which by nature have more complicated linear dependencies
  of repair (decoding) operations (e.g., Clay codes). From my understanding,
  the modeling will be much more complicated.
    * I cannot find the repair performance regenerating codes (Bufferfly codes
      for example). It only shows the load balancing degree.
    * What's the overhead when doing the scheduling of the repair operations?