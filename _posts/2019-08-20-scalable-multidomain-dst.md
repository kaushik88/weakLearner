---
layout: post
mathjax: true
title: "Scalable Multi-Domain Dialogue State Tracking"
tags:
- Dialog
categories:
- Research
thumbnail_path: blog/personal/chatbot.png
---

[Paper Link](https://arxiv.org/pdf/1712.10224.pdf)

### Overview

- The language understanding module outputs are used to delexicalize the user utterances, which are processed by the DST for feature extraction.
- We then integrate a separate candidate generation step that estimates a set of slot value candidates using the local conversation context, as well as possibly external knowledge sources.
- DST operates only on these candidates, resulting in an approach scalable to large and rich datasets.

### Architecture

- Model the dialogue state as a joint distribution across all slots and make a simplifying assumption of factoring the joint distribution as a product of a distribution for each slot.

**Candidate Set**

- Candidate set for a slot is defined as the set of values of that slot, along with the scores.
- Let $$ {C_s}^t $$ be the candidate set for a turn t of a slot s. $$ {C_s}^0 is empty for every slot. Limit $$ | {C_s}^t | $$ to K.
- Take the candidates for a slot from user utterance, then system utterances and then from the past conversation based on scores (in decreasing order) until you hit K.

**State Representation**

- To $$ {C_s}^t $$, we add 2 values - null and don't care. This is the total set of possible values a slot can take.
- We also PAD to keep K constant.

**Model Description**

{% include figure.html path="blog/personal/scalablemultidomain-archi.png" alt="Scalable Multi-Domain DST Architecture" %}

- DST is a discriminative model which takes the candidate set for each slot and assigns a score to each of them.
- Feature Extraction
	- 3 types of features - utterance, slot and candidate.
	- Delexicalization - substituting all the values of slot s with some function delex(s). Just the slot values and not slot names.
	- Delexicalized utterance passed through 2-layers of BiLstm and we take the final hidden layer as the utterance representation.
- Utterance related features
	- User Utterance and System Utterance.
	- User dialog act and System dialog act (global ones 'greetings' and 'negate' only).
- Slot related features
	- Relevant to a particular slot and are common across all candidates for the slot.
	- Features - Binary vectors indicating the presence of slot specific dialog act (request or deny) for both user and system. Also include scores of null and don't care in the previous turn.
- Candidate related features
	- Features - Binary vectors indicating the presence of candidate specific dialog act (inform, modify) and the score of candidate in prev turn.
	- Also use the utterance feature from the LSTM.


### Results

| Paper | Accuracy on DSTC2 |
|-------|----|-----|
| This paper | 0.703 |
| Rule-based Baseline | 0.619 |
