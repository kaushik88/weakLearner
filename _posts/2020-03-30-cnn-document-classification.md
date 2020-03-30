---
layout: post
mathjax: true
title: "Convolutional Neural Networks for Sentence Classification"
tags:
- Classification
categories:
- Applied
thumbnail_path: blog/personal/classification.jpeg
---

[Paper Link](https://arxiv.org/pdf/1408.5882.pdf)

### Introduction

- A simple CNN with little hyperparameter tuning and static vectors achieves excellent results on multiple benchmarks.

### Architecture

{% include figure.html path="blog/personal/cnn_class_result.png" alt="CNN Classification Architecture" %}

- Convolution applied over words - different kernels/filters for different ngrams.
- Apply pooling over time.
- Use dropout.

**CNN-multichannel**

- A model with two sets of word vectors. Each set of vectors is treated as a ‘channel’ and each filter is applied to both channels, but gradients are backpropagated only through one of the channels.
- Hence the model is able to fine-tune one set of vectors while keeping the other static. Both channels are initialized with word2vec.

### Results

{% include figure.html path="blog/personal/cnn_archi.png" alt="CNN Classification Results" %}
