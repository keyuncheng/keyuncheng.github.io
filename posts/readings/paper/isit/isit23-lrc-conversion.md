# Reading Notes: ISIT'23 LRC Conversion

Title: Locally Repairable Convertible Codes:
Erasure Codes for Efficient Repair and Conversion

Conference (ISIT'23 extended version): [Link](http://www.cs.cmu.edu/~rvinayak/papers/LRC_conversion_ISIT2023_extension.pdf)

Journal (): [Link]()

## Summary

This paper proposes a piggybacking framework over LRC codes to reduce the LRC
conversion bandwidth by re-encoding. It focuses on changing *k* and *g*, and
considers both split and merge conversions. Theoretical studies shows that the
conversion bandwidth can be reduced by 17.89%.

## Main Contributions

## Details

* Coding scheme
    * LRC with optimal code distance with local parity groups of size *r+1*,
      global parities *g*. Each local group have *l* local parity block.
    * Underlying RS code: Vandermonde-based RS code

* Piggybacking framework
    * Encode useful information of a part of symbols to certain coded symbols

* Parameter
    * (k,g,r,l) -> (k',g',r',l'), while r and l keeps the same

* Goal
    * Reduce the number of symbols **read** (as the number of writes are fixed)

* Motivating example
    * Example 1 (merge): 12 -> 8 -> **7 + 1/3**
    * Example 2 (split): 12 -> 5 + 1/3 -> **5**

* Detail
    * Step 1: Base code construction: pyramid code
    * Step 2: Design of piggybacks
        * Some extra information is stored in the local parity blocks and
          global parity blocks
    * To achieve the bandwidth reduction, the number of global parities
      **needs to be changed**
        * Additionally, for the merging case, the bandwidth reduction is
          possible only when the number of global parity blocks decreases
        * Additionally, for the split case, the bandwidth reduction is
          possible only when the number of global parity blocks decreases
        * In short, the conversion utilizes the local parity blocks
          piggybacked with extra information to reduce the conversion bandwidth

## Strength

## Weakness

* It only considers when the number of local parity blocks is unchanged

* The theoretical improvement is very limited (although it's made general),
  considering the applicable parameters (# of global parities needs to
  increase for both merge and split regime)

* The design is **very difficult** to understand
    * Six different types of sub-packets mixed in one plot, making it hard to
      figure out the exact conversion bandwidth for the conversion
    * For the split conversion, each local group reads different portions of
      sub-packets. Can't find a general algorithm to describe the procedure.

* It's not clear the exact sub-packetization required
    * For the merge regime, is it two (as divided into two parts)?
    * For the split regime, is it four (as divided into four parts)?