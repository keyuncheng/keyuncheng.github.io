# Reading Notes: ATC'21 ZNS

Title: ZNS: Avoiding the Block Interface Tax for
Flash-based SSDs

Conference (ATC'21): [Link](https://www.usenix.org/conference/atc21/presentation/bjorling)

Journal (): [Link]()

## Summary

This paper provides (1) empirical evaluation using a ZNS SSD and a
conventional block-based SSD in write-intensive worloads, (2) review of
ZNS interfaces, (3) ZNS support in Linux kernel and RocksDB, and (4)
implementation of a ZNS-based file system, to show the effectiveness of ZNS in
reducing write amplification (WA) and improving the performance.

## Main Contributions

This is a key paper to understand ZNS SSDs, by lifting the majority of FTL
functionalities to the host side (e.g., mapping), while keeping the
reliability mechanisms (e.g., ECC, bad block management) in SSD controller.
Another aspect is that ZNS SSDs only allows sequential writes within a zone,
which improves write amplification (WA) and overall performance.

## Details

## Strength

## Weakness

N/A