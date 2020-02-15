---
layout: post
mathjax: true
title: "Neural Machine Translation of Rare Words with Subword Units"
tags:
- Tokenization
categories:
- Applied
thumbnail_path: blog/personal/deepl.png
---

[Paper Link](https://arxiv.org/pdf/1508.07909.pdf)

### Architecture

- Initialize the symbol vocabulary with all the characters plus a special '.' character.
- Iteratively count all symbol pairs and merge the top pair ('A', 'B') to form a new symbol ('AB').
- Each merge operation produces a new symbol (in our case 'AB').
- The number of merge operations is the only hyper-parameter.
- The final vocabulary size is equal to number of symbols in the initial vocabulary plus the number of merge symbols.

{% include figure.html path="blog/personal/bpe_algo.png" alt="BPE Algorithm" %}