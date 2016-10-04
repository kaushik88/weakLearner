---
layout: post
title: "Functional Programming"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about - 

1. The functional programming paradigm.

There are 2 main programming paradigms -

1. Imperative Paradigm
2. Functional Paradigm

Functional Paradigm is a style of building the structure and elements of computer programs — that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. The focus is more on a building functions from smaller building blocks (something like a LEGO). In contrast, imperative programming focuses on performing actions over time, meaning perform action1 followed by action2 etc. This means that in functional paradigm, there are no mutable variables, assignments, loops, and other control structures that are present in the imperative paradigm.

int i = 0;
i = 10; // Here 'i' is a mutable variable.

Functions in a Functional Programming language are first-class citizens. This means that - 

1. They can be defined anywhere (even inside other functions).
2. They can be passed as arguments and also returned from other functions.
3. There is a way to compose richer functions from simple function blocks.

### Why Immutables?

Mutables introduce non-determinism in parallel programming. Consider the following example - 

var x = 0
async {x = x + 1}
async {x = x + 2}

Depending on the order of execution, the output of this can either be a 0, 1 or 2.

However, strict functional languages don't have mutables. It can be thought of constructing the program over space (smaller building blocks) and parallel to time.

{% include figure.html path="blog/personal/space.png" alt="Space vs Time" %}
