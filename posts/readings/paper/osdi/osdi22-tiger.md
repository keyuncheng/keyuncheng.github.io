# Reading Notes: OSDI'22 Tiger

Title: Tiger: disk-adaptive redundancy without placement restrictions

Conference (OSDI'22):
[Link](https://www.usenix.org/conference/osdi22/presentation/kadekodi)

Journal (): [Link]()

## Summary

This paper follows up the prior designs (i.e. HeART and Pacemaker), and
considers the problems of data placement in disk-adaptive redundancy systems.
Previous works (Pacemaker) partitions is sub-cluster based, forcing the
erasure coded stripes to be resided in sub-clusters with homogeneous failure
rates. To reduce the failure rate in such setting, Tiger proposes eclectic
stripe, which resides in possibly diverse failure rate stripes to avoid the
placement constraints. This approach shows improved storage savings, peak I/O
during transition in the evaluation.

## Main Contributions

* Eclectic stripe
    * The logical stripes are placed across disks with dynamic AFRs.
        * In conventional (no disk adaptive) settings, Eclectic stripes
          follows the default, that's encoding across different disks models.
    * The redundancy scheme is dynamically chosen based on the actual disk AFR
      for every logical stripes.
        * This approach improves the risk diversity. (How's the distribution
          of actual stripe redundancy scheme?)
    * A new approximate MTTDL calculation to simplify the originial expensive
      MTTDL calculation with 2-4x speed up and preserving accuracy over 95%
        * The main idea is to reduce the computation complexity
            * Original MTTDL calculation requires solving a system of
              equations with diverse disk AFR rates, thus not directly
              applicable to eclectic stripes
                * Computation cost is very high (several seconds for a single
                  set of redundancy schemes)
            * The new MTTDL calculation utilizes Poission-binomial
              distribution for the approximation
                * The formula eliminates the AFR! (didn't really understand
                  the theory yet)
                * computation time reduces to milliseconds
    * Eclectic volumes
        * Multiple logical eclectic stripes may resides in the same physical
          disk, increasing the diversity

## Details

1. Problem
    * Pacemaker's design requires the disks with very closed ages (or, the
      Rgroups) to be erasure-coded. This increases the risk of such system
      undergoes unanticipated homogeneous failures. There is no diversity in
      stripe placement.
    * Placemaker's design requires the sub-clusters (or Rgroups) with
      sufficiently large sizes, like thousands of disks. It's not suitable for
      common DC settings.
    * Rgroups with very large sizes results in a large batch of
      "step-deployed" disks to suffer from simultaneous AFR changes, thus the
      system need to handle the burst I/O of redundancy transition.

## Strength

* Experiments shows
    * The placement diversity is significantly improved from Pacemaker (core
      of the design purpose)
        * How to measure? Viable disk candidates to erasure coding schemes
    * The risk diversity is significantly improved from PaceMaker with the
      same traces in Pacemaker (Google and Blackblaze).
        * How to measure? Risk-diversity (0-1): The percentage of disks that's
          applicable to a specified erasure coding scheme.
    
## Weakness

* What's the performance impact of metadata overhead with Eclectic stripe for
  large clusters? Although with the eclectic volume desing, this paper still
  follows the centralized approach for the controller, now all logical stripes
  contains various AFRs, I wonder what's the overhead the metadata management.