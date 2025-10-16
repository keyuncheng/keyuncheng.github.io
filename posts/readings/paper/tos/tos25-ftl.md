# Reading Notes: HyTorC

Title: HyTorC: Hybrid Address Translation for SSDs supporting Compression

Conference (TOS'25): [Link](https://dl.acm.org/doi/pdf/10.1145/3767335)

Journal (): [Link]()

## Summary

This paper proposes a hybrid FTL scheme based on block and page mapping. The
key idea is to embed the logical page mapping into logical block mapping,
where the block mapping gradually evolves from block-level to page-level
mapping.  It then applies compression on both data and FTL metadata to further
reduce the FTL memory overhead.

## Main Contributions

## Details

* Logical block descriptors (LBDs): each LBD contains a pointer to a
  physical block and an availability bitmap to indicate which pages in block
  mapping mode or page mapping mode. It then adds compression bitmap to record
  the compression status of each page.

* The mappings will be compressed (optionally) by using RLE (Run-Length
  Encoding) to further reduce the memory overhead.

## Strength

* The memory overhead is reduced compared with page-level mapping FTL, DFTL,
  SFTL and leaFTL (ASPLOS'23).

* The additional access overhead is comparatively limited compared to other baselines.

## Weakness

* Why consider SSDs with compression only?

* Why consider 4KB page size and 1024 pages per block only? Any other
  configurations?

* There is no evaluation on the FTL metadata compression ratio.

* I will suggest to evaluate the compression overhead to show that the
  overhead is limited.