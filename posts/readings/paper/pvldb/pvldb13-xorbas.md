# Reading Notes: Xorbas PVLDB'13

Title: XORing Elephants: Novel Erasure Codes for Big Data

Conference (PVLDB'13): [Link](https://www.vldb.org/pvldb/vol6/p325-sathiamoorthy.pdf)

Journal (): [Link]()

## Summary

This paper introduces Xorbas, another LRC construction. With implementation over HDFS called HDFS-Xorbas, compared with RS, with 14% additional storage, the experiments show approximately 2 times disk repair I/O and repair network traffic. Compared with MDS code, it introduces logarithmic locality and distance asymptotically equal to that of MDS code.

## Main Contributions

* Xorbas (LRC) code constructions
    * Faster repair; higher reliability (for a better degraded read
      performance)

* Implementation in HDFS-RAID (called HDFS-Xorbas)

* Evaluation in AWS EC2 and Facebook local clusters.

## Details

* LRCs are codes that make the tradeoff between storage optimality and
  repair performance.

* Block locality. Block locality *r* means each block can be a function of r
  other blocks. For small locality codes, even n, k grow, we can still
  reconstruct the data by reading *r* blocks. MDS codes have *r* >= k. RS
  codes are MDS codes that have the smallest possible *r = k*.
    * LRCs are non-MDS codes, with logarithmic block locality compared with
      MDS code, tradeoff storage overhead to get repair speed and bandwidth
      efficiency.
    * Xorbas-LRCs have the optimal distance for the specified locality.

* Code constructions
    * An explicit construction of LRC(k,n-k,r) = (10,6,5)
    * Starts with RS(10,4)
    * Local parities for the local groups: the same as Azure-LRC
    * Add one more local parity for the parity groups (for the global parities
      and the local parities of the local groups)
    * The paper presents a randomized algorithm and a deterministic algorithm
      to find the coefficients for the local parities.
        * For HDFS-RAID, the coefficients can be simplified as all ones.
    * To save the storage for the additional parity for the parity group, the
      paper view this additional parity as an *implied parity block*, which is
      the XOR of the local parities of the *local groups* and the *parity
      group*.

* Implementation
    * Implement over HDFS-RAID
    * RAID-Node: Scan for files to be EC-ed. Reduce replication level from 3
      to one. Implemented as a MapReduce job.
        * BlockFixer: check for failures (lost / corrupted blocks).
          Implemented as a MapReduce job.
    * RS(10,4) is implemented under the ErasureCode component.
    * Xorbas is implemented over RS, which only adds local parities to the
      underlying RS code. 
    * Encoding: Xorbas calculates all parity blocks through its MapReduce
      encoder. All blocks are spread across the cluster according to Hadoop's
      configured block placement policy.
    * Decoding. It has two decoders, a light decoder for local repair
      functionalities when facing single block failure and a heavy decoder
      with RS repair functionalities when the light decoder fails. MapReduce
      also applies to decoding.

* Reliability Analysis.
    * Applying a standard Markov model for the analysis
    * It shows that it adds two 0's of reliability to the 3-way replication
      and RS(10,4). This is trivial, simply because it adds two more parities.

* Evaluation
    * Metrics: repair I/O (bytes read), repair bandwidth (Network Traffic) and
      Repair time (duration). The metrics are standard.

* Appendix
    * Theoretical proofs for the distance of Xorbas-LRCs through *entropy*.
    * Proving that Xorbas-LRCs have the optimal distance (minimum distance)
      for the specified locality.
    * Show the Xorbas-LRC constructions over RS(10,4), and prove the optimal distance.

## Strength

* Stats show that LRC introduces approximately 2 times disk repair I/O and repair traffic, with marginally suboptimal storage.

## Weakness

* The only difference between Azure-LRC and Xorbas is that it adds one local
  parity to the global parity group and additional local parities. The
  theoretical contribution is very limited.

* The construction is not shown to be general. More analysis can be conducted.