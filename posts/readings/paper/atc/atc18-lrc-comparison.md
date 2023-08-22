# Reading Notes: LRC Comparison ATC'18

Title: On Fault Tolerance, Locality, and Optimality in Locally Repairable Codes

Conference (ATC'18): [Link](https://www.usenix.org/conference/atc18/presentation/kolosov)

Journal (TOS'20): [Link](https://dl.acm.org/doi/10.1145/3381832)

## Summary

This paper conducts a theoretical comparison between different LRC
constructions, including Azure-LRC, Azure-LRC+1, Xorbas-LRC and Optimal-LRC with two
metrics: ARC (average repair cost) and NRC (normalized repair cost). The
results show the tradeoff for these codes and how the codes optimize their
objectives. This paper analyzes these codes in Ceph via AWS EC2 experiments.
The experiments show that the prediction of recovery (number of blocks to be
repaired) is accurate, and the prediction provides a good estimate of the time
required for reconstruction. It also proves that NRC provides a good estimate
of the LRC constructions.

## Main Contributions

* Theoretical comparison between LRCs

* Implementation in Ceph, including the Optimal-LRCs

* Evaluation in EC2

## Details

* Motivation: directly comparing the costs and benefits of different LRC
  constructions is *nontrivial*, as these codes have different tradeoffs
  between storage overhead, recovery costs and degraded read performances.
  Furthermore, these codes with different parameters have different locality
  semantics. How to choose the optimal codes under different scenarios is
  non-trivial.
  
* Codes for comparison
    * Azure-LRC
    * Azure-LRC+1
    * Xorbas-LRC
    * Optimal-LRC

* LRCs
    * data-LRCs. Azure LRC and Pyramid codes are data-LRCs. Only the data block and local parities can be repaired locally. Global parities should be repaired with k blocks.
    * full-LRCs. Xorbas, Optimal-LRC are full-LRCs. The glocal parities can be repaired locally as well. Optimal-LRC requires n mod (r + 1) != 1. The storage overhead is slightly higher, and the code minimum distance is higher than data-LRCs. Gophan has provided an upper bound for the full-LRC code minimum distance, and shows that Optimal-LRC achieves this upper bound.

* Problems
    * The comparison between code constructions is not straightforward.
    * r (the local group size - 1) is not appropriate as a metric for the repair
    locality, because it's not fair for data-LRCs.

* Metrics
    * Use *d* (minimum code distance) to measure the fault tolerance
        * Why not MTTDL? Needs to construct a Markov Reliability model for
          each set of coding parameters, and this model does not always yields
          an analytic closed-form equation.
    * ARC (appeared in ATC'12 Azure-LRC), which averages the number of blocks
      to collect for different single block failures. ARC does not take into
      account the higher overhead of some of these codes, which implies that
      more blocks will have to be repaired in the event of a node failure
      (e.g., global parities for Azure-LRC). ARC is also not appropriate for
      modeling the degraded reads.
    * NRC. NRC = ARC * n / k. The cost of repairing the parity blocks is
      amortized over the *k* **data blocks**, instead of all *n* blocks.
    * Average degraded read cost, as repairing data blocks only.

* (Continue here)

4. Codes being compared
  * Xorbas (only in theoretical analysis, not in experiments)
  * Azure-LRC
  * Azure-LRC+1. Adding one local parity to the global parities, calculated by XORing all global parities. Can be directly appied to Azure-LRC and Pyramid codes.
  * Optimal-LRC. The author proposed a new code construction for all admissible parameters. It's discussed in another paper (Optimal LRC codes for all lenghts n ≤ q) from him.

5. Theoretical Comparison
  * For the same (n, k,r), there is always one full-LRC with a lower NRC than that of Azure-LRC. However, in most settings, the reduction in NRC is coupled with a reduction in d.
  * Adding a local parity to global parity always reduces the repair cost, with additional storage overhead.
  * Azure-LRC and Optimal-LRC are most flexible in (n, k).

6. Experimental Comparison
  * In Ceph. It is the only open-source distributed storage system that implements LRCs as part of its main distribution. LRC as a plugin in Ceph.
  * Optimal-LRC implementation. They implemented Optimal-LRC in Ceph, but haven't release the source code yet.
  * For a given (n, k,r) combination, both ARC and NRC can predict which code will incur the the highest and lowest repair costs. At the same time, they are both inaccurate in their prediction of the actual repair cost.
  * Their results show that the reduction in the amount of data read for repair does not directly translate to a reduction in repair time. This is the result of additional bottlenecks in the system. Overall, the full-LRCs achieves the greatest reduction in repair time.
  * This paper also compares the results for LRCs in different zones, with local groups in each zone, and repaired locally. Data-LRCs and full-LRCs are expected to achieve the highest benefit in large-scale deployments, where sufficient I/O parallelism can be achieved within a single zone


## Strength

1. This paper tries to analyse all existing LRCs with proposed metrics in theoretical ways, and shows that LRC reduces the repair cost in real setup.

## Weakness

N/A for this paper. It's more a comparison.