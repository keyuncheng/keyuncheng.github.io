# Reading Notes: paper

Title: Practical Byzantine fault tolerance

Conference (OSDI'1999): [Link](https://dl.acm.org/doi/10.5555/296806.296824)

Journal (): [Link]()

## Summary

This paper describes the PBFT consensus algorithm that solves the BFT problem
with practicality consideration (efficient and simple in implementation).

## Main Contributions

## Details

It's a replication-based consensus algorithm that replicates data with *3f +
1* copies, and tolerates at most *f* faulty replicas.

Algorithm sketch:

* Client request
    * Send to Primary node
    * If the Primary node has no response, then broadcast to all backup nodes
* Pre-prepare phase (by primary node)
    * The Primary node receives request from Client and broadcast pre-prepare
      message to all backup nodes for verification. The message has a time
      order
    * Purpose: In order to tolerate faulty primary node
* Prepare (by all backup nodes)
    * Backup node checks and validates the pre-prepare message from the
      primary node. It can verify that the Primary node is valid
    * Backup node also validates the message and broadcast a prepare message
      to Primary node and all other Backup nodes
* Commit
    * When all Backup nodes all agree on *f + 1* prepare messages, it replies
      to the Client with the result (true or false)
* Result
    * Client must receive *f+1* SAME replies to validate the results (whether
      true or false). It make sure the majority of nodes agree on the same results


## Strength

## Weakness