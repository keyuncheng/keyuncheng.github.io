---
title: "Paper Reading: Optimal LRC TIT'14"
date: 2020-09-19
permalink: /posts/2020/09/paper-reading-optimal-lrc-tit14/
author_profile: false
excerpt: false
tags:
  - erasure coding
  - LRC
---

A family of optimal locally recoverable codes


Download
------
[Trans. of Information Theory, 2014](https://arxiv.org/pdf/1311.3284.pdf)


Summary
------

This paper introduces the optimal LRC, with the property that with a given (n, k, r), it attains the maximum possible value of the distance. The recovery can be done for all n with r blocks only.



Details
------

1. Code construction. Assume k is divisible by r, and n is divisible by r + 1.
	* Good polynomial. g(a) = g(b) for any a and b in the field partition, and it's a constant for g(a) and g(b).
	* in simple: encoding polynomial is constructed with r g(x)'s, the data block; decoding requires r symbols oppositely.

2. Code distance of Optimal-LRC has an upper bound.

3. The paper shows several (7) examples, (n, k, r) = (9, 4, 2); 2 for (12, 6, 3), one is with minimal distance d = 6, another is using the addictive group of the field; and a example (28, k, 13). Here, k <= nr / (r +1)

4. The implementation of optimal LRC codes can be in systematic forms.

5. Product codes compared with addictive codes.

6. Parallel recovery for local groups are introduced.



Strength
------

1. All single symbol failure can be repaired locally with r symbols.

2. It's a natural generalization of RS code, taking locality into account.

3. Examples are given for code construction.


Weakness
------

1. This paper is hard to read, with almost all formulas, proofs.

2. No implementation available, though it's been implemented in ATC'18 paper (they don't release yet).


<!-- refs -->