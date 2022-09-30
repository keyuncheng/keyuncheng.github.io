---
title: 'Paper Reading: CDStore'
date: 2019-08-05
permalink: /posts/2019/06/paper-reading-cdstore/
author_profile: false
excerpt: false
tags:
  - paper reading
  - cloud storage
  - security
  - reliability
---

CDStore: Toward Reliable, Secure, and Cost-Efficient Cloud Storage via
Convergent Dispersal


Download
------
[ATC, 2015](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/atc15.pdf)


Summary
------

This paper presents CDStore, a client-server based multi-cloud storage solution with reliability, security and cost-efficiency guarantees. CDStore adopts two-stage deduplication which builds on **Convergence Dispersal** by using deterministic content-derived hashes as inputs to secret sharing, and it can achieve both bandwidth and storage savings and be robust against side-channel attacks.


Details
------

1. Convergence Dispersal, AONT-RS, CAONT-RS
    * OAEP-based AONT to improve performance on speed
    * Replace random inputs with deterministic hashes to allow deduplication
    * Due to randomness, secret-sharing prohibits deduplication
    * **CD** Replace random input with deterministic hash, thus allows deduplication
    * Stronger hash key can be applied to mitigate brute-force attacks
    * Exps shows that CAONT-RS generates despersed data faster than AONT-RS based instantiation

2. Two-stage deduplication
    * inter-users, intra-users dedup
    * dedup greately reduces storage overhead in some cases
    * (n, k, r) settings, (n, k) determines fault torlerance degree, (k, r) determines confidentiality degree
    * can avoid side-channel attacks by making dedup patterns independent accross users' uploads. At least (n - r) uncompromized

3. Fault Torlerance on Client and Server
    * offloading metadata management to server side 

4. Implementation
    * Metadata offloading (file metadata, share metadata are distributed to all servers)
    * Index management
    * Multi-thread Optimization in secret encoding/decoding

4. Microbenchmarks for reference



Strength
------

1. Two-stage deduplication
    * Achieve both bandwidth and storage savings
    * Robust against side-channel attacks

2. **Convergence Dispersal** + AONT + Reed-Solomon code ensures security


Weakness
------

1. Strong attack models (Byzantine faults) are not considered

2. Assume protected Client-Server connection (attacks like eavesdropping doesn't work)

3. Encoding in client side (requires computation effort)

4. GC and compression are not considered

5. Load Balance (multi-VM (server) per cloud)

6. Consistency

<!-- refs -->
