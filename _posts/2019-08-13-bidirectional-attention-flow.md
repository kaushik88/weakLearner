---
layout: post
mathjax: true
title: "Bi-directional Attention Flow for Machine Comprehension"
tags:
- Seq2Seq
categories:
- Research
thumbnail_path: blog/personal/machine-translation-robot.png
---

[Paper Link](https://arxiv.org/pdf/1611.01603.pdf)

### Overview

- The motivation is that attention should flow both ways (from context to question and from question to context).

### Architecture

{% include figure.html path="blog/personal/bidaf.png" alt="Bidirectional Attention Flow for Machine Comprehension" %}

- The core idea behind the paper is on the Bi-directional attention layer between the context (decoder) and the question (encoder). 

Assume we've the context hidden states $$ c_1,....,c_N \in \mathbb{R}^{2h} $$ and question hidden states $$ q_1,....,q_M \in \mathbb{R}^{2h} $$. We compute the similarity matrix **S** $$ \in \mathbb{R}^{NxM} which contains a similarity score S<sub>ij</sub> for each pair of (c<sub>i</sub>, q<sub>j</sub>) where 

$$
\begin{align*}
 	S_{ij} = {w^T}_sim [c_i; q_j; c_i \circ q_j] \in R
\end{align*}
$$

**Context-to-Question Attention (C2Q)**

We take a row-wise softmax of **S** to obtain the attention distributions $$ \alpha^i $$ which is used to take a weighted sum of the quesiton hidden states $$ q_j $$ yielding C2Q attention output **a_i**.

$$
\begin{align*}
 	\alpha^i = softmax(S_i;) \in \mathbb{R}^M
\end{align*}
$$

$$
\begin{align*}
 	**a**_i = \sigma_{j=1}^{M} \alpha_j^iq_j \in \mathbb{R}^2h
\end{align*}
$$

**Question-To-Context Attention (Q2C)**

Similarly, we take a column-wise softmax of **S** to obtain the attention distributions $$ \beta $$ which is used to take a weighted sum of the context hidden states $$ c_i $$ yielding C2Q attention output **c\textsinglequote**.

**Bi-directional Attention Flow**

$$
\begin{align*}
 	b_i = [c_i; **a**_i; c_i \circ **a**_i; c_i \circ c\textsinglequote_i ]
\end{align*}
$$

### Results

| Paper | EM | F1 |
|-------|----|-----|------|
| Dynamic Co-attention Networks | 66.2 | 75.9 |
| BiDaf| 67.7 | 77.3 |
| No char embedding| 65 | 74.4 |
| No C2Q Attention| 57.2 | 67.7 |
| No Q2C Attention| 63.6 | 73.7 |