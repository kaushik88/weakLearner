---
layout: post
mathjax: true
title: "Named Entity Recognition with Bidirectional LSTM-CNNs"
tags:
- NER
categories:
- Research
thumbnail_path: blog/personal/ner.jpeg
---

[Paper Link](https://arxiv.org/pdf/1511.08308.pdf)

### Overview

- The core idea from this paper (looking back) is the use of Lexicons.

### Architecture

{% include figure.html path="blog/personal/ner_lstm_cnn.png" alt="NER using LSTM and CNN" %}

- For each lexicon category, we match every n-gram (up to the length of the longest lexicon entry) against entries in the lexicon.
- A match is successful when the n-gram matches the prefix or suffix of an entry and is at least half the length of
the entry. (Discard matches with <= 2 words).
- Prefer exact matches over partial matches, and then longer matches over shorter matches, and finally earlier matches in the sentence over later matches.
- All matches are case insensitive.

{% include figure.html path="blog/personal/ner_lexicon.png" alt="Using Lexicons in NER" %}

### Results

{% include figure.html path="blog/personal/ner_lexicon_result.png" alt="Using Lexicons in NER" %}