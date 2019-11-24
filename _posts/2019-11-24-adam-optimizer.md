---
layout: post
mathjax: true
title: "Adam Optimizer"
tags:
- Deep Learning
categories:
- Research
thumbnail_path: blog/personal/deepl.png
---

[Paper Link](https://arxiv.org/pdf/1412.6980.pdf)

### Architecture

Adam realizes the benefits of both AdaGrad and RMSProp.

- **Adaptive Gradient Algorithm (AdaGrad)** that maintains a per-parameter learning rate that improves performance on problems with sparse gradients (e.g. natural language and computer vision problems).

- **Root Mean Square Propagation (RMSProp)** that also maintains per-parameter learning rates that are adapted based on the average of recent magnitudes of the gradients for the weight (e.g. how quickly it is changing). This means the algorithm does well on online and non-stationary problems (e.g. noisy).

### Results

{% include figure.html path="blog/personal/adam_result.png" alt="Results of Adam Optimizer" %}