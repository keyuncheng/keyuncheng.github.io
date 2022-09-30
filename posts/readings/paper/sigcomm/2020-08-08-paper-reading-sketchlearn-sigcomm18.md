---
title: "Paper Reading: Sketchlearn SIGCOMM'18"
date: 2020-08-09
permalink: /posts/2020/08/paper-reading-sketchlearn-sigcomm18/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - stream processing
---

SketchLearn: Relieving User Burdens in Approximate Measurement with Automated Statistical Inference


Download
------
[SIGCOMM, 2018](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/sigcomm18.pdf)


Summary
------

Approximate network measurements trade accuracy to saves resources, but requires intensive manual effort to learn the appropriate tradeoff. Sketchlearn, a sketch-based network measurement framework, learns statistical properties from the resources to eliminates the resource traffic conflicts.


Details
------

Problems behind: Due to conpetition of network traffics with limited resources (resource conflicts), measurement errors occurs. Sufficient resources must be guaranteed in approximate measurements. A tight binding of resource configurations (resource params) and accuracy parameters exists in approximate measurements.

Current approach: approximate measurements.
Limitations: Hard to quantify stats (expected errors, threshholds), hard to find theoretical bounds, hard to examine correctness. Not understand: Hard to define flowkeys

Design requirements: fast (real-time, per-packet processing), resource saving (memory), generalization


Proposed approach: Sketch-based measurement framework. It draws the resource conflicts by building a multi-level sketches. The sketch tracks the frequencies of flow records at bit-level, so the multi-sketch forms a multi-level Gaussian.

* Multi-level sketch for per-bit tracking.
* Separation of large/small flows. Large flows are extracted from sketches, while residual counters for small flows.
* Model inference: needs configs for multi-sketch. Param-free (expected errors, thresholds params, other configs)
* Error measurement for individual flows


Model learning (needs to look in detail): Theory about model inference. Large flow extraction replies on this.
* Various traffic stats: heavy hitters, heavy changers. Cardinality and per flow frequencies are calculated.


Implementation: Software/hardware data plane and control plane. Flows are updated with each incoming packet.



Strength
------

* General framework for various network traffics.
* Automated statistical inferences based on multi-sketch relies on multi-level Gaussians.
* Free of custom params like threshold params, accuracy params(expected errors) are required, so user burdens on configurations are minimized.



Weakness
------


<!-- refs -->
