---
layout: post
mathjax: true
title: "Dialog Context Language Modeling With Recurrent Neural Networks"
tags:
- Dialog
categories:
- Research
thumbnail_path: blog/personal/chatbot.png
---

[Paper Link](http://150.162.46.34:8080/icassp2017/pdfs/0005715.pdf)

### Overview

- The goal is to encode the context for Language Modeling.
- Design RNN based contextual language models that specially track the interactions between speakers in a dialog.
- Modeling utterances in a dialog as a sequence of inputs might not well capture the pauses, turntaking, and grounding phenomena in a dialog.

**Background**

- [Mikolov et al](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/rnn_ctxt.pdf) proposed a topic conditioned RNNLM by introducing a contextual real valued vector (LDA of preceding text) to the RNN hidden state.
- [Lin et al](https://www.cs.cmu.edu/~ark/EMNLP-2015/proceedings/EMNLP/pdf/EMNLP106.pdf) proposed using Hierarchical RNN for document modeling.

However all these methods focused on applying context by encoding preceding text without considering interactions in dialogs.

### Architecture

**Context Dependent RNNLM**

Let D = (U_1, U_2, ... U_K) be a dialog with K turns and involve 2 speakers. In this case, turn is just the utterance of a single speaker and could involve multiple messages. The *k*th turn U_k = (w_1, w_2, ..., w_{T_K}) is represented as a sequence of T_k words.

$$
\begin{align*}
P (U_k | U_{less_than_k}) = \prod_{t=1}^{T_k} P ({w_t}^{U_k} | {w_{less_than_t}}^{U_k}, U_{less_than_k})
\end{align*}
$$


{% include figure.html path="blog/personal/dialogRNN.png" alt="Dialog RNN" %}

- In the above model, we append a context representation to the input to RNN (as opposed to the hidden state).

**Context Representations**

- Strip sentence boundaries, run an RNN and use the final hidden state as the context (DRNNLM). 
- Alternatively, the last RNN hidden state is fed to the RNN hidden state of the target utterance at each time step (CCDCLM).

However, the above 2 methods treat dialog history as a sequence of inputs, without modeling dialog interactions. In order to deal with this, the paper proposes 2 different architectures - 

{% include figure.html path="blog/personal/dialogRNN2.png" alt="Interactive Dialog Context LM" %}

In the above model, we define the context and initial hidden state as follows - $$ c = {h_{T_{k-1}}}^{U_{k-1}} $$ and $$ {h_0}^{U_k} = {h_{T_{k-2}}}^{U_{k-2}} $$

{% include figure.html path="blog/personal/dialogRNN3.png" alt="External State Interactive Dialog Context LM" %}

In the above model, we have an external RNN to encode the respresentation from 1 turn to another.

### Results

| Model | K=1 | K=2 | K=3 | K=5 |
|-------|----|-----|
| RNNLM | 60.4 | - | - | - |
| DRNNLM | - | 60.1 | 58.6 | 59.1 |
| CCDCLM | - | 63.9 | 61.4 | 62.2 |
| IDCLM | - | - | 58.8 | 58.6 | 
| ESIDCLM | - | - | 58.4 | 58.5 |