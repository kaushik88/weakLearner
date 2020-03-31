---
layout: post
mathjax: true
title: "A Structured Self-Attentive Sentence Embedding"
tags:
- Classification
categories:
- Applied
thumbnail_path: blog/personal/classification.jpeg
---

[Paper Link](https://arxiv.org/pdf/1703.03130.pdf)

### Introduction

### Architecture

{% include figure.html path="blog/personal/csa_archi.png" alt="Self Attention Architecture" %}

H = hidden states of Bi-LSTM (N*2u)
a = softmax(V_s2 * tanh(W_s1 * H^T))

where the dimensionality of a is n.

But we might need multiple such vectors, lets say r and hence we set 

A = softmax(W_s2 * tanh(W_s1 * H^T))

where the dimensionality of A is r*n

M = AH (r * 2u)

### Results

{% include figure.html path="blog/personal/csa_results.png" alt="Self Attention Results" %}