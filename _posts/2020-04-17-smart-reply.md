---
layout: post
mathjax: true
title: "Efficient Natural Language Response Suggestion for Smart Reply"
tags:
- Dialog
categories:
- Applied
thumbnail_path: blog/personal/chatbot.png
---

[Paper Link](https://arxiv.org/pdf/1705.00652.pdf)

### Introduction

- Smart Reply Dual Encoder architecture for GMail-like applications.

### Architecture

{% include figure.html path="blog/personal/sr_archi.png" alt="Smart Reply Overall Architecture" %}

**Dual Encoder**

- Dual encoder architecture with shared weights across the message and response.

**Batch Negatives**

- Instead of choosing negatives for every batch and minimize log loss.

**Response Biasing**

- The negatives would largely include popular labels.
- Offset this by having language model based probability of a label (pre-computed) to combine this with the dual encoder score.

### Results

{% include figure.html path="blog/personal/sr_results.png" alt="Results in Smart Reply" %}
