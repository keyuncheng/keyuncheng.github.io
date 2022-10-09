# Reading Notes: INFOCOM'18 NCScale

Title: Toward Optimal Storage Scaling via Network Coding: From Theory to
Practice

Conference (INFOCOM'18): [link](https://ieeexplore.ieee.org/document/8485961)

Journal (TON'21): [link](https://dl.acm.org/doi/abs/10.1109/TNET.2021.3106394)

## Summary

This paper shows the optimal tradeoff of storage scaling with network coding,
and the minimal scaling bandwidth. It also introduces NCScale, a system
realizing NC based scaling. Experiments shows that NCScale improves the
scaling performance of Scale-RS by up to 50%.

## Main Contributions

* Optimal scaling bandwidth is formally proven

## Details

* Formalize scaling with network coding
    * Example: (3,2,1) transition: Scale-RS needs 8 blocks, including 4 for
      data and 4 for parity; NC requires only 4 blocks, requiring only 2 for
      data and 2 for parity, leveraging the XOR property.

* Prove the optimal scaling bandwidth with information flow graph
    * The overall proof structure follows TIT'10
    * I didn't dig in to the proof in detail

* NCScale
    * Highlights: NCScale achieves the minimal scaling bandwidth when n - k =
      1
        * Main idea: the parity block can be locally computed (without
          transfer over the network)
        * Example: (3,2,1)
    * Non-optimal scaling bandwidth
        * Example (4,2,2)
        * Need to transfer one parity block for scaling
    * Shows the **actual scaling bandwidth** (promising!)
    * The algorithm of NCScale can be abstracted as 
        * Compute: compute new parity blocks (which may need additional block
          transfer from other storage nodes)
        * Send
        * Delete (obsolete blocks)

## Strength

* The evaluation shows NCScale consistently outperforms prior ScaleRS, 

## Weakness

* For redundancy transition, scale down is also another important part,
  considering the actual disk failure changes. A more conservative approach in
  reliability may need to be applied.

* The experiment settings are conducted with small (n,k) (up to (9,6) with 3
  parities) and low network bandwidth (up to 2Gbps, network bottleneck, send
  time dominates the complete workflow)

* I'm thinking what's the underlying reason that NCScale cannot match the
  lower bound (optimal scaling bandwidth) for large n - k, and how we can
  improve from here.