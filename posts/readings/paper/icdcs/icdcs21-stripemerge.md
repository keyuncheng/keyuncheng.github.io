# Reading Notes: ICDCS'21 StripeMerge

Title: StripeMerge: Efficient Wide-Stripe Generation for Large-Scale
Erasure-Coded Storage.

Conference (ICDCS'21): [link](https://ieeexplore.ieee.org/document/9546417)

Journal (): [link]()

## Summary

This paper introduce StripeMerge, a solution to combine two narrow RS coded
stripes with same (n, k) into a wide stripe with (2k + ). It introduces the
idea of perfect matching, with which the merging bandwidth is 0. It then
argues that the computation cost of finding a perfect matching solution is
expensive, and introduces two alternatives heuristics of matching algorithm
for practicality. The experiments with both simulation and EC2 experiments
show that StripeMerge significant outperforms NCScale for various (n, k)
settings.

## Main Contributions

1. The first work to generate wide stripe generation problem.

2. Design two practical heuristics to generate wide stripe by merging stripes.

3. experiments of both simulation and prototype show the effectiveness of
   StripeMerge, by outperforming NCScale by a large margin.

## Details

* The key idea of this paper, is to formulate the stripe merging problem as a
  bipartite matching problem, with the end points being the chunk placement.

* StripeMerge-P significantly reduces the running time of StripeMerge-G by
  categorizing the # of overlapped parity chunks into groups.

## Strength

* It's a great idea to formulate the stripe merging problem as a bipartite
  matching problem and improve it with heuristics.

* Experiments. The experiments are well designed (e.g. running time analysis
  and memory consumptions in the simulation).

## Weakness

* Parameter spaces. It can support (n, k) -> (n + k, 2k) only. Generating a
  real wide stripe with a narrow stripe (e.g. from (n, k) -> (n + 9k, 10k))
  requires recursively applying of stripe merging. It remains unexplored.