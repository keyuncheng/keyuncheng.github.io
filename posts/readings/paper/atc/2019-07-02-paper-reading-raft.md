---
title: 'Paper Reading: RAFT'
date: 2019-07-02
permalink: /posts/2019/07/paper-reading-raft-atc14/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - cryptography
---

In Search of an Understandable Consensus Algorithm (RAFT)


Download
------
[ATC, 2014](https://web.stanford.edu/~ouster/cgi-bin/papers/raft-atc14)


Summary
------

This paper presents **Raft**, a simpler and more understandable consensus algorithm. Previously dominant **Paxos** protocol which is commonly taught has significant drawbacks: too difficult to understand and not able to provide a good foundation to build pratical implementations. Raft applied specific techniques to improve understandability including decomposition and state space reduction, and it has several novel features: strong leader, leader election and membership changes.



Details
------

Paxos Drawbacks
------

* Exceptionally difficult to understand, few people succeed to understand it.

* No widely agreed-upon algorithm for multi-Paxos, most for single-decree, but incomplete  descriptions for multi-Paxos. Multi-Paxos relies on a complex **single-decree decomposition**, and it use a simple symmetric peer-to-pear approach as its core, no leadearship form for its optimization.


Raft consensus Algorithm
------

**Recommend**: a [commic](http://thesecretlivesofdata.com/raft/) about Raft.


### Motivation


1. Problem decomposition

2. Simpify state spaces and eliminate nondeterministim


### Basics

* **NOTE**: Check the original paper for all examples and figures based on page limit.

* Single distinguished **leader** is elected to manage the replicated log (accepts log from client and replicates to **followers**). Data flows between leader to followers.


### Raft guarantee several properties

* Election: When leader fail, elect a new one.

* Leader append-only

* Log-matching to guarantee correctness

* Leader Completeness

* State Machine Safety


### Roles

* Followers: respond only

* Candidate: used to elect a new leader

* Leader: Replicate logs to followers

### Operations

RPC: RequestVotes(Candidate), AppendEntries(Leader)

* Heartbeat-like operation (such as AppendEntries with no log entries)


### Leader Election

1. All server starts as followers

2. No communication from leader: election timeout, begin election.

3. A candidate wins with majority votes.

4. For the case that no candidate wins: Raft use randomized election timeouts to ensure that split votes are rare (the probability to happen for the second time) and resolved quickly.

* Several corner cases for ranking system (initially the authors applied)


### Log replication

1. Client request command

2.  Leader append to its own log (new entry)

3. Leader issues AppendEntries to all Followers

4. Only if it's safe (the majority of Followers respond and safely replicated), Leader apply the entry to state machine, return result to client

* **NOTE**: If any follower fails, Leader retries AppendEntries indefinitely

A lot of details in maintaining Leader and Followers log consistency (consistency check for missing entries).


### Safety issues

1. Election restriction

2. Committing entries from previous terms

3. ...


Strength
------

Adiditional to its completeness as a protocol with guarantee on safety, consistency, it's

1. Understandable

2. More applicable for implementation


Weakness
------

1. Single Leader configuration may be a bottleneck for large scale system, unable for load balance

2. Fixed way of communication

3. For the case that all candidates split votes, it may be a problem that the randomness causes latency (though finally one candidate will win the election).


<!-- refs -->
