# Reading Notes: FAST'19 HeART

Title: Cluster storage systems gotta have HeART: improving storage efficiency
by exploiting disk-reliability heterogeneity

Conference (FAST'19):
[link](https://www.usenix.org/conference/fast19/presentation/kadekodi)

Journal (): [link]()

## Summary

This paper introduces HeART, an online tuning tools for redundancy transition
by observations of disk reliability status. HeART significantly reduces the #
of disks (storage savings) with the same reliability levels (MTTDL) compared
with one-scheme-for-all and replications.

## Main Contributions

## Details

* Goal: reduce storage overhead by replacing one-fits-all schemes with
  adaptive redundancy rate
    * The reason why AFR comes into play

* Analysis of AFR
    * Bathtub curves of AFR for six disk models are shown

* How to use AFRs?
    * HeART groups disks with similar AFRs and a tailor-made scheme for
      different groups
        * Heterogeneous AFRs
    * How to measure disk reliability? MTTDL
        * One interesting thing: multiple redundancy schemes can achieve same
          MTTDL, but long schemes (high k) with high reconstruction costs -
          there is a tradeoff how to select redundancy schemes?

* Challenges that HeART try to addresses:
    * Online redundancy transition for different groups
        * time required, I/O (not considered)
    * Accurately detects AFRs for different groups
        * How to filter out abnormal AFRs?

* Designs
    * Online change point (bathtub point change significantly) detection
        * Should use prior information about HDDs at start
        * Standard sliding-window based change point detector
        * Periodically trigger point detection
    * Abnormally detection of reliability data stream from HeART (to filter
      out the abnormal data): use RRCF algorithm (I didn't look into detail)

* Evaluation
    * Over Blackbaze dataset of 6 disk groups
    * Mostly focus on the functionalities
        * Identify the useful life periods -> MTTDL
        * How HeART suggests the coding schemes with best storage savings?
            * Start from (9,6) -> depend on disk AFRs among groups -> also
              short codes (like (24, 20) and (21, 17))
    * Sensitivity analysis
        * how the system judges the flat period of disk groups?
        * AFR buffer: the period (or padding called in the paper) added after
          the infancy of a disk life (in the baththub curve)
            * Larger buffer size: conservative for the low part of AFR

## Strength

* Probably the first system work on the disk AFR analysis (I don't see others
  for now)
    * which gives strong evidence for the **motivation of redundancy
      transition**: disk failure rate highly varies and the baththub curve
      suggests that **we can adapt the redundancy rates with convertible
      codes**

* HeART can suggest how to adapt the redundancy scheme with init code (9,6)
    * It's based on the analysis disk's real status (AFR) instead of man-made

* The designs are mostly non-system
    * Based on reliability analysis (MTTDL)

## Weakness

* What's the role of HeART in real systems? This paper suggests that the
  approach is online, but didn't show the exact performance of HeART in real
  systems as a reliability adaptor.