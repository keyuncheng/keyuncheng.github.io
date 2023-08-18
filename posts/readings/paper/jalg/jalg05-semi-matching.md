# Reading Notes: JALG'05 Semi-matching for bipartite graphs

Title: Semi-matchings for bipartite graphs and load balancing

Conference (): [Link]()

Journal (Journal of Algorithms 2005):
[Link](https://doi.org/10.1016/j.jalgor.2005.01.003)

## Summary

This paper formulates the semi-matching problem for bipartite graphs, with the
focus on unweighted bipartite graphs (edge with weight = 1). It gives
theoretical proofs of the properties of semi-matching, and relates it to
load-balancing. Finally, it provides two algorithms to compute optimal
semi-matching for unweighted bipartite graph. The first algorithm is based on
modified Hungarian, while the second one is based on cost-reducing paths.

## Main Contributions

* Formulates the semi-matching problem

* Relates semi-matching with load-balancing, and optimization objectives to
  unweighted graphs

* Theoretical proofs for unweighted bipartite graphs

* Two algorithms to find optimal semi-matching

## Details

* Optimization objective: mean finish time
    * The paper proves that this objective also optimizes Lp-norm

* It relates to scheduling unrelated machines

* A-sm1: based on modified Hungarian
    * Complexity: O(UE)

* A-sm2: based on cost-reducing paths

## Strength

## Weakness

* Scheduling unrelated parallel machines is a weighted version of the results
  in this paper; However, this paper focuses on unweighted bipartite graphs;