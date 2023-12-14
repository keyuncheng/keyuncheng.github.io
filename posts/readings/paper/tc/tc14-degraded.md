# Reading Notes: TC'14 Degraded Read

Title: Boosting Degraded Reads in Heterogeneous Erasure-Coded Storage Systems

Conference (): [Link]()

Journal (TC): [Link](https://ieeexplore.ieee.org/document/6911949)

## Summary

This paper considers applying a greedy algorithm to solve the problem with
multiple degraded reads for distributed storage systems under heterogeneous
network settings. The optimization goal is to find a solution with minimum
total degraded read time to read all failed blocks. The coding scheme is based
on XOR-based array codes (CRS, Libe8tion, STAR) where the encoding and
decoding matrix are pre-calculated in advance.

## Main Contributions

## Details

## Strength

## Weakness

* As discussed in their future work (5), d is a very important parameter to
   evaluate.
* General scalar coding schemes like RS codes and Azure-LRC are not considered
  in this paper. It would be better to evaluate these codes.
