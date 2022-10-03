# Reading Notes: OSDI'20 Pacemaker

PACEMAKER: Avoiding HeART attacks in storage clusters with disk-adaptive
redundancy

## Summary

This paper presents Pacemaker to reduce the transition overload (in our
context, redundancy transition overhead instead) in large scale clusters by
proactively (1) organizing data layouts, (2) initializing transitions without
affecting redundancy. It first analyzes traces from millions of disks from
large production cluster to show that transition overload strongly blocks the
cluster's performance. Pacemaker is integrated to HDFS and experiments from
production clusters show that the transition overhead significantly reduces to
no more than 5% while providing storage savings for 14% to 20%.

## Main Contributions

## Details

* Problem settings (almost the same as redundancy transition)
    * Disk failure rates highly vary among storage clusters -> conservative
      redundancy (MTTDL analysis)
        * high reconstruction cost for wide stripes with the same redundancy
    * AFR (Annual disk Failure Rate) has to be learned from observations
    * Transition overload is high (from previous work HeART)
        * Overwhelming burst of urgent transition I/O -> periods of 100%
          bandwidth

* Existing studies
    * Reactive approach: exists a period of time that the data is unprotected

* Pacemaker address transition overload issue by
    * proactively organize stripe layouts
    * proactively ("savely") initializing transitions without hurting the
      redundancy
    * integrate to HDFS to demonstrate the feasibility

* Designs
    * To meet redundancy constraints:
        * Dgroup (same makes/models, fixed) and Rgroup (same redundancy
          schemes and placement restrictions)
        * Allows disks transition from Rgroups
    * To meet I/O constraints
        * Reconstruction I/O
        * Transition I/O (most important)
            * Peak I/O limitation

    * Proactive-transition-initiator
        * using AFR curves (rates) and learn the rate to determine the time to
          transit
            * Disk health monotoring service and AFR curve learners
            * Special handling for trickle disks and step disks
        * Rgroup planner: which group should be transition to with constraints
          (redundancy, predefined I/O constraints)
            * Rgroup creation and purging: meets system required placement
              restrictions
        * Rate-limitor: limit the transition rate

    * Transition-executors
        * transition by emptying disk (simply moving contents to other disks),
          for small # of disks
        * Recalculating parities: **redundancy transition techniques**(what we
          are focusing on)

* Implementation on HDFS
    * Feasibility and low implementation overhead

## Strength

* Improve from HeART: improve the transition overhead **from system's
  perspective**
    * Strong proof by real data from large clusters and disks
    * Problem clear and strong reasoning (analysis of disk failure rates, peak
      I/Os)
    * How they solve problems from system's perspective (given how to
      transition with codes in theory)
        * Limit transition I/O with Rgroups, monitoring disk health, rate
          limiting, etc.
    * Strong evidence from experiments: 4 clusters
        * Proof of concept from HDFS

## Weakness

* This paper mostly focus on how to solve transition overhead almost from
  system's perspective. It's really a good paper to read. The underlying
  assumption is the transition overhead is addressed from theory perspective.
  They didn't talk about it in this paper. How to select the codes in Sec. 5.3
  may worth mentioning.

* The experiment results are mostly based on simluation with cluster logs. I'm
  interested how the proactive approach will perform in real clusters. 