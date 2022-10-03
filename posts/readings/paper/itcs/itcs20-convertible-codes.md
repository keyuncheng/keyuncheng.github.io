# Reading Notes: ITCS'20 Convertible Codes

## Summary
This paper proposes convertible codes to mitigate the redundancy transition
overhead. It first formalizes the notion of code conversion, then introduces
the convertible codes to mitigate the code conversion costs. Specifically,
convertible codes can minimize the number of node access. It presents a
special class of convertible codes in the merge regime (k' is a multiple of k
after transition), and two special classes of codes: optimal access
convertible codes for all parameters (with high field size); and optimal
access convertible codes for a broad range of parameters.

## Main Contributions

* Formally analyze the problem of "redundancy transition" (considering the
  disk failure rate)
    * High redundancy - waste of resources
    * Low redundancy - prone to data loss

* Formalize the notion of code conversion
    * constructing codes with lcm(k, k') # of stripes

* It present the lower bound of the access cost (# of node access), or the
  notion of access-optimal

* It presents a set of MDS convertible codes in the merge regime that
  satisfies access-optimal property for a certain field size, and the explicit
  code construction (with the generator matrix) with proof.

* For the Hankel-I and Hankel-II construction with low field size (high and
  low field size), I need more time to understand.

## Strength

* This paper motivates the problem of code conversion with disk failure rate
  change and it's reasonable (referring to PACEMAKER, the disk failure rate
  significantly varies from makes/models).

* Convertible codes focuses on optimizing the # of node accesses, which is a
  reasonable optimization goal over the baseline (re-encoding from scratch).

* It presents an explicit construction over the merge regime, thus is
  practical.

## Weakness

* The paper writes "reducing the number of accesses also reduces disk IO,
  network bandwidth and CPU consumed". This is not formally proved. Although
  the paper claims the access-optimality, but the I/Os and (merge) bandwidths
  are not formally proven reducing.

* Generality: It considers the construction over merge regime. What's the
  difference between merge regime and others? We may have the same redundancy
  (n - k), but different ks, and how to select k is not discussed in the
  context. Can the idea of merge regime (which is comparatively
  straightforward) be applied to the non-merge regime?