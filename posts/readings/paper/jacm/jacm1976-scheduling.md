# Reading Notes: Scheduling Unrelated Parallel Machines

Title: Exact and Approximate Algorithms for Scheduling Nonidentical Processors

Conference (): [Link]()

Journal (Journal of the ACM, 1976):
[Link](https://dl.acm.org/doi/abs/10.1145/321941.321951)

## Summary

This paper summarizes the exact and approximate algorithms for general
scheduling independent parallel machine problem, mainly focusing on some
objectives: (1) minimize maximum finish time, (2) minimize mean finish time,
(3) minimize weighted mean flow time. It also presents exact algorithms
(dynamic programming) and approximation algorithms for the above mentioned
problems.

## Main Contributions

* Provides exact and approximation solutions to scheduling unrelated machines
  problem. The DP solutions are of great importance.

## Details

* Algorithms for scheduling unrelated machines
    * Analogy: partition of tasks into disjoint ordered sets
    * Measures: (1) maximum finish time, (2) mean finish time, (3) weighted
      finish time
    * Complexity
        * (1) NP-complete
            * Proof: reducing to 3-satisfiability problem
        * (2) polynomial
            * Shortest-processing-time-first algorithm provides an optimal
              solution
        * (3) NP-complete

* Optimization goal: minimize maximum finish time
    * Exact algorithm: dynamic algorithm
        * Use a 2-processor example to illustrate
        * (1) enumerate the search space by searching from the bottom
        * (2) encode and store current possible (cannot be improved) solutions
          in memory
        * Analogy: branch-and-bound tree
        * Complexity: O(min(nF, 2^n))
        * Generalization to m-processors is straignt forward
    * Approximation algorithm
        * Epsilon-approximation algorithms, **with epsilon as input**
        * The algorithm follows a strategy for solving knapsack problem by
          approximation; very complicated
        * An example of 2-tuple
            * Key idea: (1) divide the task times into sets; (2) generate
              sumsets (3) update the tuples in sumsets to figure out the
              possible division sets

* Optimization goal: minimize mean finish time
    * Exact algorithm
        * Reducing to a min-cost-flow problem
        * core idea: copy the jobs for m times

* Optimization goal: minimize weighted mean finish time
    * Exact algorithm
        * Example: 2-processors as example
        * Core idea: merging the second coordinates of 3-tuples
    * Approximation algorithm
        * Similar structure as approximation algorithm for 2-processor maximum
          finish time

* See the summary of complexity of algorithms proposed at the end of the paper

## Strength

N/A

## Weakness

N/A