---
title: "Paper Reading: RS code theory SIAM'1960"
date: 2021-06-13
permalink: /posts/2021/06/paper-reading-rs-siam1960/
author_profile: false
excerpt: false
tags:
  - Code
---

Polynomial Codes Over Certain Finite Fields


Download
------
[SIAM, 1960](https://epubs.siam.org/doi/pdf/10.1137/0108018)


Summary
------

This paper presents the theory of RS code



Details
------

K: a finite field (|K| can be arbitrary large, |K| >= 2)

* K can be represented by V_n(Z_2)
  * how? Construct beta_k = (a_k, a_k+1, ..., a_k+n), an n-dimension vector, where a_k, an element in Z_2 is picked from a cyclic group of K.
  * How to fund such a_k? Find an irriducible f(x) in Z_2(alpha), where alpha is the root of f(x).
  * Use the formula f(x) a_n+k + c1 * a_n+k-1 ... + c_n * a_0 + k = 0 to construct the cyclic a_k. a_k has period 2^n - 1.
  * Finally, we got beta_k.
  * Define **the multiplication rule** (Note that beta satisfy the algebraic equations satisfied by corresponding elements in K):
    * beta_k = beta^k
  * K = {0, beta, beta^1, beta^2, ...beta^2^n-2, 1}, |K| = 2^n. It means that all elements in K are represented by beta_k. We can find any element in K by checking the beta_k table.
  * this is the finite field we are discussing in the paper

* Code: a mapping between V_m(K) to V_n(K)

* RS code: a mapping between V_m(K) to V_2^n(V_n(Z_2))
  * Input: a m-dimensional vector (b_0, b_2, ..., b_m-1), where b_k is picked from K
  * Output: (P(0), P(beta), P(beta^2), ..., P(beta^2^n-2), P(1))
  * Such code tolerates (2^n - m - 1) / 2 errors

* How to define P(x)?
  * easy. P(x) = b_0 + b_1 * x + b_2 * x^2 ... + b_m-1 * x^m-1. b_k is exactly the input of code
  * actually, b_k can be represented by beta_i, since beta_i represents all elements in K.

* What is P(beta^k)?
  * Also easy. replace x in P(x) with beta^k. As b_k are replacible by checking the beta_k table. P(beta^k) must be be able to be represented by a polynomial of beta

* Check the code example in the paper. Input b_i are represented by an m-bit array of alpha_i (or, beta_i, it doesn't matter), beta_i are represented by a V_3(Z_2), a 3-bit array.
  * The code translates a m-bit array in Z_2(alpha) to 2^n-bit array in Z_2(alpha), and it tolerates up to (2^n - m - 1) / 2 bit errors.


Strength
------

Top-1 theory paper to beginners of EC

Weakness
------

N/A




<!-- refs -->

