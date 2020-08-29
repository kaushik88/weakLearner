---
layout: post
mathjax: true
title: "ArcFace: Additive Angular Margin Loss for Deep Face Recognition"
tags:
- Loss
categories:
- Applied
thumbnail_path: blog/personal/embedding.png
---

[Paper Link](https://arxiv.org/pdf/1801.07698.pdf)

### Introduction

- Centre loss penalises the distance between the deep features and their corresponding class centers in Euclidean space to achieve intra-class compactness.
- SphereFace assumes the linear transformation matrix in the last fully connected layer can be used as a representation of the class centers in an angular space and pensalises the angles between the deep features and their corresponding weights in a multiplicative way.
- ArcFace is an additive angular margin loss.

### Architecture

{% include figure.html path="blog/personal/arcface_archi.png" alt="Architecture for ArcFace Loss" %}

**Softmax Loss**

{% include figure.html path="blog/personal/softmax_loss.png" alt="Softmax Loss" %}

- Softmax loss doesn't enforce higher similarity for intra-class samples and diversity for inter-class samples. (See figure below)

**ArcFace Loss**

- We change W.x as ||W|| ||x|| cos\theta and set bias as 0.
- If we normalize W as a unit vector, then ||W|| becomes 1.
- We also normalize x and scale it to s.

{% include figure.html path="blog/personal/arcface_loss.png" alt="ArcFace Loss" %}

### Results

{% include figure.html path="blog/personal/arcface_results.png" alt="Results for ArcFace Loss" %}

