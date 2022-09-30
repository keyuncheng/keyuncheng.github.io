---
title: "Paper Reading: RACS"
date: 2019-07-01
permalink: /posts/2019/07/paper-reading-racs-socc10/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - vendor lock-in
---

RACS: a case for cloud storage diversity


Download
------
[SoCC, 2010](http://www.cs.cornell.edu/~hweather/publications/racs-socc2010.pdf)


Summary
------

This paper presents RACS, a proxy that transparently spreads the storage load over many storage providers. Stripping user data across multiple providers can allow customers to avoid vendor lock-in, reduce the cost of switching providers, and better tolerate provider outages or failures. RACS incorporates erasure coding rather than replication to tolerate provider failures.


Details
------

* providers charges with bandwidth in/out, requests and hosting the actual data, and compete aggresively on price, thus expensive to switch from one provider to another.

* replicate data to multiple providers has high storage and bandwith cost.

* RACS assumes a minimal storage interface (`put, get, delete, list`)

* Outages and economic failures are considered and distinguished.

* RACS decreases the prohibitive costs of such failures and vendors lock-in.

* RACS stripe data accross multiple providers using erasure codes, and retrives chunks from surviving nodes to recover loss data when node failure occurs.

* This paper implements RACS and REST interfaces for different storage providers. for multiple proxy, they use ZooKeeper to implement synchronization.




Strength
------

* Avoid vendor lock-in

* Provide fault torlerance for both storage nodes and proxy (multiple proxy)

* Proxy-based transparent interface to client

* Saving costs compared with replication


Weakness
------

* Transient failures are not considered (in future work)

* Relatively simple prototype implementation.