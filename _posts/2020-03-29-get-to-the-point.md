---
layout: post
mathjax: true
title: "Get To The Point: Summarization with Pointer-Generator Networks"
tags:
- NLG
categories:
- Applied
thumbnail_path: blog/personal/chatbot.png
---

[Paper Link](https://arxiv.org/pdf/1704.04368.pdf)

### Introduction

- Two shortcomings of abstractive text summarization - factual inconsistency and repetitive text.
- we use a hybrid pointer-generator network that can copy words from the source text via pointing.
- we use coverage to keep track of what has been summarized, which discourages repetition.

### Architecture

**Baseline**

- Bahdanau attention over the document hidden states.
- Calculate P_vocab by having a dense layer and then downward projection layer to vocab size and then softmax.

**Pointer Generator Network**

- p_gen = W [h't; s_t; x_t] + b
- p_word = p_gen * p_vocab + (1-p_gen) * a_it

**Coverage Mechanism**

- In our coverage model, we maintain a coverage vector ct, which is the sum of attention distributions over all previous decoder timesteps.
- c_t = sum(a_it)
- While calculating attention, they also use c_t.
- Also introduce coverage loss, which minimizes sigma(a_it * c_it). This makes sure that the same words in the document are not attended to again and again.

### Results

{% include figure.html path="blog/personal/gttp_result.png" alt="Get To The Point Results" %}