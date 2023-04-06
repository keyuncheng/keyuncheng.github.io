# Reading Notes: IWQoS'21 EC-Scheduler

Title: EC-Scheduler: A Load-Balanced Scheduler to Accelerate the Straggler
Recovery for Erasure Coded Storage Systems.

Conference (IWQoS 2021): [link](https://ieeexplore.ieee.org/document/9521280)

Journal (): [link]()

## Summary

This paper motivates the problem of straggler in EC recovery, and propose a
balanced scheduling algorithm called EC-Scheduler straggler recovery. It
dynamically analyzes the workload on the nodes to guarantee the parallelism
and recovery load balance.

## Main Contributions

* It models straggler recovery problem
    * Models least expected completion time with the consideration of
      heterogenity of storage nodes, with an 2x-approximation solution

* It design a dynamic adaption module with similar approach (least expected
  completion time)


## Details

* Motivation
    * Straggler problem
        * imbalanced access by upper layer applications, which incurs
      heterogenity to the system.
        * Disk level heterogenity: caused by storage devices
        * Node offline
    * Existing work
        * Partial coding operations: PPR, ECPipe
        * graph based problem: Fast-PR, Selective-EC
        * Integer programming: ECStore
    * Problem of existing work
        * FastPR: without considering heterogenity
        * Selective-EC: without considering heterogenity, and no dynamic load
          adaptation
        * EC-Store: models chunk level parallelism, not for node level
          parallelism

* Design
    * repair scenarios: hot-standby and scattered repair
    * least expected completion time algorithm: 
        * Greedily assign tasks to nodes with least expected completion time
    * Model the I/O for each node independently
        * It only considers and tries to minimize the **read time** (NP-hard)
            * Start from least task time first, and then change to expected
              completion time
    * Dynamic load perceiver: exponential moving average

* Evaluation
    * Compare with random repair, FastPR, ECStore
    * argue that repair algorithms focused on optimizing network transmission
      does not apply to their focus
    * Simulation based on 4 public traces

* Evaluation
    * Propose imbalance factor lambda: lmax / (lmax - lavg)

## Strength

* Scheduling problem

## Weakness

* The modeling from a repair problem to a scheduling problem is not described
  in detail

* No system architecture provided: only centralized design based on Redis
  described in text

* The assumption that the modeling on recovery time considers **read only** is
  not rigorous, as network transmission is the bottleneck in most cases

* The design is relatively trivial: a simple scheduling problem

* The improvement shown in evaluation is limited (Table V and IV), and the
  parameters ranges are small 