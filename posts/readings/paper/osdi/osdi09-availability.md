# Reading Notes: OSDI'09 Google Availability

Title: Availability in Globally Distributed Storage Systems

Conference (OSDI'09): [Link](https://www.usenix.org/conference/osdi10/availability-globally-distributed-storage-systems)

Journal (): [Link]()

## Summary

* The paper is an analysis based on Google on the failures and availability,
  reliability of geo-distributed storage systems. For the reliability
  analysis, it focuses on the MTTDL.

## Main Contributions

* Measure (quantify) and **analyze** the availability (in different
  components) for distributed storage systems

* Modeling the data availability
    * Markov Model

* Multi-cell replication scheme
    * Show the importance of cluster-wide failure events

## Details

* Reasons of disk and node availability (Chapter 2)

* Measurement of availability
    * Average availability
    * MTTF

* Numbers
    * Disk AFR: 2% - 4%
    * Node failures: 1min - 1 hour (Figure 2)
        * Major reason: planned reboots; others: node restarts and unplanned
          reboots
        * Node failures contributes significantly to data availability

* Correlated failures
    * Failure bursts
    * 37% of failures from multiple failures within 2 mins are correlated
    * Propose a measurement called **rack affinity**

* Fault tolerant schemes
    * Replication
    * Erasure Coding
    * System admins may do rate-limiting for node failure recovery
    * Rack-aware policy will in general increase the stripe MTTF

* Simulation of expected availability
    * Simulate all possible stripes and simulate failure events
        * The simulation results is close to the actual events
        * It suggests the effectiveness of simulating failures with synthetic data 
    * I think the design is not clear

* Markov Modeling of Stripe Availability
    * A flexible model
    * Canonical markov modeling
        * Independent failures
        * Exponential distribution
            * FAST'07 points out that Weibull distribution is better
            * Some studies ay that mpm=hp,pgemeoty pf recovery rate and
              failure events have a much smaller events than the size of the
              event
    * Construction
        * Computation of failure rate: averaging the probability from all
          failure events, such that a random failure event will affect (fail)s
          a subset of chunks from all available chunks
          * Single chunk recovery rate is fixed: assume that the recovery rate
            does not depend on the total number of unavailable chunks in the
            cell
          * Only model **serial recovery** to gain more conservative estimates
            of stripe availability
        * This section really needs an example, but the paper doesn't provide
          it
    * Extension to multi-cell replication
        * The design needs more elaboration
    * Evaluation shows the MTTF from Markov model predicts the same magnitude
      as the measured MTTF
    * Reducing recovery time is effective when correlated failures are few.
      This suggests we can improve availability by improving the recovery
      performance
        * When correlated failures are considered, even a 90% reduction in
          recovery time results in only a 6% reduction in availability
        * This suggests that if we don't consider correlated failures, we are
          **overestimating** the reliability (MTTF)
    * Improving the reliability of disk (LSE rate and disk failure rate) does
      not significantly improve the data availability
    * Replication across data centers greatly improves availability (MTTF)
        * This is obvious

## Strength

* The statistics from industry are useful

## Weakness

* This paper focuses on the analysis of failures and causes, but does not have
  many theoretical and system level insights

* The theoretical parts are too high level, and needs more elaboration
    * Markov modeling and MTTDL
    * Modeling of multiple failures