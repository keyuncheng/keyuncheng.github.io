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

## Details

* The detailed constructions of different LRC constructions are TBD.

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