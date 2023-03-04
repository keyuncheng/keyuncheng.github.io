---
title: "Paper Reading: Grid codes TOS'09"
date: 2020-10-15
permalink: /posts/2020/10/paper-reading-grid-codes-tos09/
author_profile: false
excerpt: false
tags:
  - erasure coding
---

GRID codes: Strip-based erasure codes with high fault tolerance for storage systems


Download
------
[TOS, 2009](https://dl.acm.org/doi/10.1145/1480439.1480444)


Summary
------

In Grid codes, the stripes are arranged into multi-dimensional (in 2 dims as shown in paper) grids. Grid code is constructed by the matched code.



Details
------

1. Matched code: all the row substripes should be encoded by the same erasure code, and all the column substripes should also be encoded by the same erasure code. Moreover, the code chosen for all the row substripes should match with that for all the column substripes.

2. Code construction
* Two matched code (row and column) choice: XOR-based MDS code (EVENODD, STAR, X-code). They can be both horizontal code / vertical code or mixed.
* Refer to the stripe layout in page 10, 11, 12. 

3. Data reconstruction
* An iterative reconstruction algorithm: reconstruct row sub-stripes and column sub-stripes by corresponding horizontal / vertical codes respectively.

4. Grid code Features
* High Fault tolerance: t = (t_1 + 1) * ... * (t_m + 1) - 1, m stands for the code i
* High storage efficiency. Storage efficiency increases with stripe size
* **Optimal Small-Write Performance**. It's not discussed in detail.
* Fast reconstruction. Only need to read the sub-stripes from the t erased strips.

5. Restrictions
* stripe size of row code and column code should be equal, n_row = n_col

6. Comparison with other codes
* Refer to table in page 19. Significantly high fault tolerance

Strength
------

1. High fault tolerance

2. can be fully XOR based

3. Fast recovery, since in reconstruction, only need to read t sub-stripes related to the t strips



Weakness
------

1. Storage efficiency is not optimal, due to the mixture of codes

2. Code construction speed is not discussed





<!-- refs -->