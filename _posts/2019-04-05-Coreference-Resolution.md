---
layout: post
mathjax: true
title: "Coreference Resolution"
tags:
- NLP
categories:
- Research
thumbnail_path: blog/personal/coref.png
---


**Problem**

The task of Coreference Resolution is to identify all mentions that refer to the same real world entity. Consider the following example - 

> Barack Obama nominated Hillary Rodham Clinton as his secretary of state on Monday. He chose her because she had foreign affairs experience as former First Lady.

*Barack Obama*, *he* and *his* all refer to **Obama** (Entity).  <br/>
*Hillary Rodham Clinton*, *secretary of state*, *her*, *she* and *First Lady* all refer to **Hillary Clinton**. <br/>

**Datasets**

OntoNotes 5.0 is the biggest coreference dataset out there - it has around 3000 documents labeled by humans. You can download the dataset from LDC [here](https://catalog.ldc.upenn.edu/LDC2013T19). Conll has annotated the dataset and you can find the annotated dataset and scripts to merge them [here](http://conll.cemantix.org/2012/data.html).


**Metrics & SotA**

- MUC
- CEAF
- LEA
- B-CUBED
	* For each mention, compute a precision and recall.
	* Average the individual Ps and Rs
- BLANC

Often report F1 over these metrics.

| Paper | F1 Score |
|------|------|
| Wiseman et al (2015)| 63.3|
| Clark & Manning (2016)| 65.4|
| Lee et al (2017) | 67.2 |

<br/>

**Key Resources**

[1] - 2018 Stanford NLP Lecture - [Slides](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/lectures/lecture13.pdf) <br/>
[2] - HuggingFace Demo and Github repository - [Github](https://github.com/huggingface/neuralcoref/tree/master/neuralcoref) <br/>
[3] - Learning Anaphoricity and Antecedent Ranking Features for Coreference Resolution - [Paper](http://people.seas.harvard.edu/~srush/acl15.pdf) <br/>
[4] - Improving Coreference Resolution by Learning Entity-Level Distributed Representations - [Paper](https://nlp.stanford.edu/pubs/clark2016improving.pdf) <br/>

### Theory

**Winograd Schema**

If you think this is an easy task, consider the following 2 examples - 

> She poured water from the pitcher into the cup until it was full/empty. <br/> <br/>
> The trophy would not fit in the suitcase because it was too big/small.

In each of the above 2 examples, the coreference would change based on a single world. Also, there is a lot of common knowledge (not written in books) that goes into these resolution. These are called Winograd Schema and was recently proposed as an alternative to Turing Test.

**Applications**

- Document Understanding 
- Machine Translation
- Dialog Systems

**Anaphora**

Anaphora is a kind of reference where one term in the document (anaphor) refers to another term term (antecedent).

> Barack Obama said he would sign the bill.

**Bridging Anaphora**

> We went to see a concert last night. The tickets were really expensive.

Insert-Venn Diagram


### Ranking

Coreference resolution can be broadly divided into 2 steps - 

- Detect the mentions
	- easier
	- can be nested
- Cluster the mentions
	- harder
	- multiple ways (see below)

**Mention Detection**

Mention is a span of text referring to some entity. There are 3 kinds of mentions - 

1. Pronouns
	- Part of Speech Tagger 
2. Named Entities
	- NER
3. Noun Phrases
	- Constituency Parser

**Mention Clustering Models**

There are 3 kinds of coref models - 

1. Mention Pair
2. Mention Ranking
3. Mention Clustering

**Mention Pair**

In the Mention Pair model, we train a binary classifier that predicts if a pair of mentions are coreferent. <br/>

At the train time, we minimize a standard cross entropy loss - 

- Assume, we've N mentions in the model <br/>
- y<sub>ij</sub> if mentions m<sub>i</sub> and m<sub>j</sub> are coreferent, -1 otherwise

$$
\begin{align*}
  J = - \sum_{i=2}^{N} \sum_{j=1}^{i} y_{\text{ij}} log p(m_j, m_i)
\end{align*}
$$

- i -> iterates through the mentions
- j -> iterate through candidate antecedents

At the test time, we pick some threshold (say 0.5) and add coreference links between all positives.

Disadvantages

1. Could easily ball up and all form 1 big cluster.
2. Most of the mentions only have 1 antecedent, but we predict all of them

**Mention Ranking**

In the Mention Ranking model, we assign each mention to its highest scoring candidate antecedent. We also have a dummy NA mention that allows the model to decline linking the current mention to anything.

$$
\begin{align*}
  J = - \sum_{i=2}^{N} -log \sum_{j=1}^{i-1} (y_{\text{ij} == 1}) p(m_j, m_i)
\end{align*}
$$

**Model Architectures**

1. Non-Neural Statistical Classifier
2. Feed-Forward Neural Network
	a. Embeddings, distance, document genre, speaker information.
3. LSTMs and Attention


### HuggingFace Coref Implementation

The HuggingFace Coref Implementation is very similar to this [paper](https://nlp.stanford.edu/pubs/clark2016improving.pdf) by Clark and Manning.

