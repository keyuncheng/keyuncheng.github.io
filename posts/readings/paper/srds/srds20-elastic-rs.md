# Reading Notes: SRDS'20 Elastic RS

Title: Enabling I/O-Efficient Redundancy Transitioning in Erasure-Coded KV
Stores via Elastic Reed-Solomon Codes

Conference (SRDS'20): [link](https://ieeexplore.ieee.org/document/9252042)

Journal (): [link]()

## Summary

* Main idea
    * Mitigate the I/O overhead for parity blocks update during redundancy
      transitioning
        * Target code: RS
        * Target scenario: KV store (with hot and cold data for high and low
          redundancy)
    * Approach: increasing the overlapping data blocks
    * Baseline method: Stretched RS code (SRS)
    * Key difference and improvement over SRS
        * Logically distributes data blocks in a row-major order
        * Construction of encoding matrix (to increase the number of
          overlapping blocks)

## Main Contributions

## Details

* By design, ET targets at alpha >= 2;
    * For RS-ET, it builds atop multiple sub-stripes of RS
    * The concept of row-major stripes and sub-stripes of ET are the same
* ET targets at repair and currently single failure repair
    * The same redundancy as RS
* Open questions:
    * Do we need to consider repair for such scenario (KV store)?
        * One possibility is considering the scenario like (A tale of two
          erasure codes, FAST’15), using two code schemes, one for repair
          performance (ET can come into play) and another for storage overhead
    * When will the transition be like for codes with alpha >= 2?
        * For example, for RS-ET(9,6,3) to RS(14,10,4); what’s the logical
          target sub-packetizaiton (most likely 12, the LCM and we can start
          with the same approach as in Elastic RS, increasing the overlap
          sub-blocks
        * For RS-ET, need to figure out how much of I/O overhead during
          transitioning comes from pairwise coupling of ET
            * RS-ET needs to maintain the systematic layout
    * What’s the target (n, k, w) to choose for redundancy transitioning?

## Strength

## Weakness