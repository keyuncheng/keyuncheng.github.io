# Reading Notes: FAST'23 Uniform Cauchy LRC

Title: Practical Design Considerations for Wide Locally Recoverable Codes (LRCs)

Conference (FAST'23): [Link](https://www.usenix.org/conference/fast23/presentation/kadekodi)

Journal (): [Link]()

## Summary

This paper compares different LRC constructions from a practical perspective,
including the average data repair cost, average repair cost (including the
global parities, which is more friendly for full-LRCs that can support local
repair for global parities), and MTTDL. It proposes a construction called
Uniform Cauchy LRC (which is very close to ATC'18) which can repair more
failure patterns than the prior constructions in **multiple failures** where
the number of failures is larger than the code distance. The comparisons are
based on theoretical analysis and Monte-Carlo simulation experiments.

## Main Contributions

* Compares state-of-the-art LRC constructions for wide stripes, including
  Azure-LRC, Azure-LRC+1, Optimal Cauchy LRC (Xorbas)

* Reliability analysis using observed failures (via Monte Carlo simulations)

* Analyze the theoretical properties of Optimal distance LRCs and MR-LRCs with
  maximal recovery property (not necessarily distance optimal)

* Propose Uniform Cauchy LRC, a sub-optimal distance LRC that can tolerate
  more failure patterns with the number of failures larger than the distance,
  with a tradeoff of smaller code distance than the Optimal Cauchy LRCs.

## Details

* Optimal-LRC: very close to ATC'18

* Uniform Cauchy LRC: the coefficients of global parities are the same as Optimal-LRC; the
  coefficients of local parities changed.

* One useful information: analyzing the multiple failure patterns in practice,
  which suggests that multiple failures appear more common than shorter codes.
  Supporting the multiple failures (especially on the system performance) for
  wide-LRCs needs more research.

## Strength

## Weakness

* The construction is almost the same as Optimal-LRC proposed in ATC'18, which
  makes the novelty very limited. The only difference is that the new
  construction can repair more failure patterns for multiple failures beyond
  the code distance. By the way, it makes the code distance lower than the
  original Optimal-LRC (ATC'18). Overall, I think the theoretical construction
  is very limited.

* It only contains theoretical analysis. No real-world experiments are
  conducted.