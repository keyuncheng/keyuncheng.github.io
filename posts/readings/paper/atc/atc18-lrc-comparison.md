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

* Motivation 
    * directly comparing the costs and benefits of different LRC constructions
      is *nontrivial*, as these codes have different tradeoffs between storage
      overhead, recovery costs and degraded read performances. Furthermore,
      these codes with different parameters have different locality semantics.
      How to choose the optimal codes under different scenarios is
      non-trivial.
  
* Codes for comparison
    * Azure-LRC
    * Azure-LRC+1
    * Xorbas-LRC
    * Optimal-LRC

* Types of LRCs
    * data-LRCs. Azure LRC and Pyramid codes are data-LRCs. Only the data block and local parities can be repaired locally. Global parities should be repaired with *k* blocks.
    * full-LRCs. Xorbas, Optimal-LRC are full-LRCs. The glocal parities can be
      repaired locally as well. Optimal-LRC requires *n mod (r + 1) != 1*. The
      storage overhead is slightly higher, and the code minimum distance is
      higher than data-LRCs. Gophan has provided an upper bound for the
      full-LRC code minimum distance, and shows that Optimal-LRC achieves this
      upper bound.

* Problems
    * The comparison between code constructions is not straightforward.
    * *r* (the local group size - 1) is not appropriate as a metric for the repair
    locality, because it's not fair for data-LRCs.

* Metrics
    * Use *d* (minimum code distance) to measure the fault tolerance
        * Why not MTTDL? Needs to construct a Markov Reliability model for
          each set of coding parameters, and this model does not always yields
          an analytic closed-form equation.
    * ARC (appeared in ATC'12 Azure-LRC), which averages the number of blocks
      to collect for different combinations of single block failures. ARC does
      not take into account the higher overhead (in *n*, but not in *k*) of
      some of these codes, which implies that more blocks will have to be
      repaired in the event of a node failure (e.g., global parities for
      Azure-LRC). ARC is also not appropriate for modeling the degraded read
      (but how about full node recovery?).
    * NRC. NRC = ARC * *n / k*. The cost of repairing the parity blocks is
      amortized over the *k* **data blocks**, instead of all *n* blocks.
    * Average degraded read cost, as repairing data blocks only.
    * Storage overhead *n / k*
    * *rd*-ratio (*NRC/d*), showing the tradeoff between repair cost and fault
      tolerance. For the same fault tolerance *d*, the lower *rd*-ratio is
      better.

* Details of codes to be compared
    * Azure-LRC. The last local group which contains *k mod r* data blocks is
      also assigned with one local parity. Need to make sure that *k + l < n*.
      This extension is general for most of the *(n,k,r)* parameters.
    * Azure-LRC+1. Add one local parity to the global parities, calculated by
      XORing all global parities (the difference from Xorbas is that it
      doesn't linearly combine the local parities). It's a naive extension of
      Azure-LRC and Pyramid codes.
    * Xorbas-LRC. The same as VLDB'13.
    * Optimal-LRC. 

* Codes being compared
    * Xorbas (only in theoretical analysis, not in experiments)
    * Azure-LRC
    * Azure-LRC+1. Adding one local parity to the global parities, calculated
      by XORing all global parities. Can be directly applied to Azure-LRC and
      Pyramid codes.
    * Optimal-LRC. The authors propose a new construction based on the
      original Optimal-LRC construction (TIT'14), which is generally
      applicable to parameters *n mod (r+1) != 1*. The encoding coefficients
      are different from the original Optimal-LRC construction (see Appendix).
      The new construction attains the largest possible minimum distance; and
      is the first optimal construction for all possible parameters.

* Theoretical analysis
    * Repair cost (Fig. 7)
        * Some parameters are not feasible for some code constructions under
          the same *(n,k,r)*
        * For the same *(n,k,r)*, the degraded read costs are almost the same
        * Increasing *r* increases the degraded read costs and NRCs.
    * Code distance (Fig. 8)
        * Increase *d* mush either increase *n* or *r*.
        *  For the same *(n,k,r)*, there is always one full-LRC with a lower
           NRC than that of Azure-LRC. However, in most settings, the
           reduction in NRC is coupled with a reduction in the code distance
           *d* (reasonable).
    * Comparing *(n,k,r)* Azure-LRC and *(n+1,k,r)* full-LRCs (Azure-LRC+1,
      Optimal-LRC), which adds one local parity over the global parities.
        * Reduction in NRC and *d*, at the cost of increasing storage overhead
    * Optimal-LRC does not always achieve optimal NRC (Fig. 10)
        * Reason: Optimal-LRC is designed to accommodate the global parities
          with data blocks in the same local group; when there exists only a
          few global parities (much smaller than *r*), the local group size
          increases (because of the constraints of *k* and *r*)
    * A metric to model the tradeoff between the repair cost and fault
      tolerance: *rd*-ratio (*NRC / d*) (Fig. 11)
        * The code achieving the lowest *rd*-ration is not necessarily a
          full-LRC.
        * When fixing *n* and *k*, different codes that achieve the minimal
          *rd*-ratio have different *n* and *r* (reasonable).
            * When fixing *n* and *k*, we can find an available *r*, where the
              Optimal-LRC achieves the lowest *rd*-ratio among all codes
        * Generalization of *rd*-ratio: *NRC / d^x*. Physical meaning?
            * Goal: tune the weight of *d* according to the system's tradeoff
              between durability (reliability?) and repair cost.
            * Optimal-LRC wins for almost all (but one) cases, indicating a
              better allocation of local parities.
        * Given a target fault tolerance threshold *d*, find feasible
          *(n,k,r)* for different codes.
            * Azure-LRC and Optimal-LRC are most flexible in *(n,k,r)*, as
              they can find feasible coding parameters.
    * Multiple failures for higher redundancy codes (Fig. 14 where *n >= 2k*)      
        * The case is less common, and it's possible that the **local repair
          may be worse than the global repair**
        * Appeared in the **distributed and peer-to-peer settings**
          (multiple concurrent failures are common)
        * In this case, the definitions of ARC and NRC need to be adapted to a
          weighted version of multiple failures, instead of just considering
          single failures 

* Experimental Comparison 
    * Codes compared
        * RS, Azure-LRC, Azure-LRC+1, Optimal-LRC
        * Xorbas is not implemented, as the coding parameters are not
          explicitly provided in the VLDB'13 paper except *(16,10,5)*; Plus
          Ceph doesn't support the local recovery for the global parity group
          from other local groups
    * System
        * Use Ceph. It is the only open-source distributed storage system that
          implements LRCs as part of its main distribution. Besides, Ceph
          supports online coding instead of replication first, then performs
          EC in the background.
            * Use Jerasure for coding, LRC Plugin implemented in Ceph for
              Azure-LRC and Azure-LRC+1.
            * It also discusses some implementation issues in Ceph: redundant
              data read; sub-optimal replacement OSDs (collision and handling
              with *straw2* algorithm)
        * Ceph doesn't support local repair by default. Degraded read needs to
          retrieve *k* blocks.
        * Original optimal-LRC implementation. They provide the constructions
          and coefficients
        * Deployment: 20 nodes, each node has two OSDs: 40 OSDs.
    * Metric: full-node recovery for single node
    * For a given (n,k,r) combination, both ARC and NRC can predict which
      code will incur the highest and lowest repair costs. At the same time,
      they are both inaccurate in their prediction of the actual repair cost.
    * Their results show that the reduction in the amount of data read for
      repair does not directly translate to a reduction in repair time. This
      is the result of additional bottlenecks in the system. Overall, the
      full-LRCs achieve the greatest reduction in repair time.
        * The I/O bandwidth utilized by RS and LRCs are different, RS has a
          higher utilization; for LRCs, the system may not saturate the
          storage devices (**No breakdown**)
    * It compares the results for LRCs in different zones (geographically
      different places), with local groups in each zone, and repaired locally.
      LRCs are expected to achieve the highest benefit in large-scale
      deployments, where sufficient I/O parallelism can be achieved within a
      single zone.
        * Why not use Optimal-LRC in the experiment for full-LRC?


## Strength

* Theoretical contributions
    * Metrics for comparison
        * NRC
        * *rd*-ratio
    * A more general optimal-LRC construction than TIT'14 (the construction is
      based on it)

* System contributions
    * Modification of LRC plugin (Azure-LRC and Azure-LRC+1)
    * Optimal-LRC implementation
    * Ceph's implementation support
    * Extensive evaluation over EC2
    

## Weakness

* There are some confusing settings in the evaluation, such as the parameter
settings and code selection
    * Some parameters and codes are chosen without explanation (e.g., the Zone
    experiment, why not use Optimal-LRC?)
    * The Ceph system performance has no breakdown.
    * It is better to use plots for the results instead of using the tables
