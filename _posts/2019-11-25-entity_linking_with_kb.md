---
layout: post
mathjax: true
title: "Entity Linking with a Knowledge Base: Issues, Techniques and Solutions"
tags:
- NER
categories:
- Research
thumbnail_path: blog/personal/ner.jpeg
---

[Paper Link](http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/TKDE14-entitylinking.pdf)

### Overview

- Many KBs - Wikipedia, DBpedia, YAGO, Freebase, KnowItAll, ReadTheWeb and Probase.
- 2 main challenges - name variations (partial names, aliases, abbreviations, and alternate spellings) and entity ambiguity.
- It is possible that some entity mention in text does not have its corresponding entity record in the given
knowledge base. We define this kind of mentions as unlinkable mentions and give NIL as a special label denoting *unlinkable*.
- Usually NER before entity linking.
- Similar to coreference resolution (without an external KB) and Word Sense Disambiguation (WSD).
- 3 sub-problems in Entity Linking - **Candidate Entity Generation**, **Candidate Entity Ranking** and **Unlinkable Mention Prediction**.

### Architecture

**Candidate Entity Generation**

1. Named Dictionary Based Techniques - ⟨key, value⟩ mapping where key is entity and value is the canonical entity. From wiki, *entity pages*, *redirect pages*, *disambiguation pages*, **bold phrases in first paragraphs** and **hyperlinks**. Now we can use exact/partial match on the key for a given mention.

2. Surface Form Expansion - This is mostly for acronym expansion and includes heuristic based methods and supervised learning methods (SVM which emits a score given an (acronym, candidate) pair).

3. Search Engine Based Techniques - Google APIs and Wikipedia search engines.

**Candidate Entity Ranking**

Features for this can be broadly classified into Context Independent (doesn't depend on where the mention occurs - examples include mention text, entity popularity and entity type) and Context Dependent (bag of words and concept vector).

{% include figure.html path="blog/personal/entity_ranking.png" alt="Entity Ranking" %}

Ranking methods include binary ranking and LTR in supervised ranking and IR based ranking in unsupervised ranking.

**Unlinkable Mention Prediction** - Binary classification problem - given a (mention, top Entity) train a binary classifier to predict whether the top entity is not linked to the mention. An alternate approach is to add 'NIL' as a candidate to entity ranking problem and take a softmax over (N+1) entities.