---
title: "Paper Reading: StreamDFP ICDCS'20"
date: 2020-08-02
permalink: /posts/2020/08/paper-reading-streamdfp-icdcs20/
author_profile: false
excerpt: false
tags:
  - paper reading
  - storage
  - stream processing
  - disk failure prediction
---

Toward Adaptive Disk Failure Prediction via Stream Mining


Download
------
[ICDCS, 2020](https://www.cse.cuhk.edu.hk/~pclee/www/pubs/icdcs20.pdf)


Summary
------

This paper presents StreamDFP, a general stream mining framework for disk failure predition with concept-driven adaption.

Problems to solve:
1. Online labeling
2. Concept-drift aware training. The system should detect and adapt to concept drift in training.
3. General Prediction. Regression: likelihood the a new disk will fail. Classification: Whether a new disk will fail.


Details
------

1. Regards disk failure prediction as a stream processing/mining problem, which is online
2. Datasets: SMART datasets, including Backblaze dataset and Alibaba Cloud dataset.
3. Complete design, from disk logs to prediction. Python + Java, around 2000LoC.

- Concept Drift: the relationship between the input and output continuously changes over time. Which should be p(y_t|x_t). Solution: Change detection

4. Learning Algorithms. Commonlyused decision tree, ensemble learning algorithms are used.

5. Studied the concept drifts p(y_t|x_t) by measuring p(x_t) and p(y_t). Conclusion: the concept drift likely exists.

6. Architecture: 
- Python: feature extraction, buffering, online labeling, first phase downsampling. Output of processed data will be stored into a local file system.
- Java: Second phase downsampling, prediction model (incremental learning).


Strength
------

1. Enabling concept-drift adaption increases classification accuracy for different learning algorithms.

2. Online labeling improves the overall accuracy.

3. Compatibility of Regression and Classification.

4. Speed viable for pratical stream processing usage.

5. Validation in Alibaba Cloud dataset, which is large


Weakness
------

1. What's the advantage of StreamDFP compared with its related work[43] ORF? And what about the performance comparison between the two works? Speed and accuracy? ORF method focused on aging issue in online learning method, but this paper's work changes the perspective, it viewed the workflow as a data stream. What's the difference?

2. How about other datasets? Are those datasets available? (Needs to figure out)

<!-- refs -->
