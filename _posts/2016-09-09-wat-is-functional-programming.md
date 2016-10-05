---
layout: post
title: "Functional Programming"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about the functional programming paradigm.

There are 2 main programming paradigms -

1. Imperative Paradigm
2. Functional Paradigm

Most of us learn Programming the Imperative (C, C++, Java, Python) way. We have learnt to think of programs as a list of commands executed over time. We're used to having mutable variables, loops, assignment and control statements. 

Functional Paradigm is a style of building the structure and elements of computer programs — that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It focuses on computing results rather performing actions (imperative). It is more about evaluation of expressions rather than execution of commands (imperative). This means that in functional paradigm, there are no mutable variables, assignments, loops, and other control structures.

Functions in a Functional Programming language are first-class citizens. This means that - 

1. They can be defined anywhere (even inside other functions).
2. They can be passed as arguments and also returned from other functions.
3. There is a way to compose richer functions from simple function blocks.

### Why Immutables?

In order to truly understand the power of immutables, consider programming in a parallel or multi-threaded environment. **Mutables introduce non-determinism**. Consider the following example - 

var x = 0 <br/>
async {x = x + 1} <br/>
async {x = x + 2} <br/>

Depending on the order of execution, the output of this can either be a 0, 1 or 2. A lot of the imperative languages have tried to stem this problem by introducing synchronization, locks etc. However, strict functional languages have solved it by removing mutables altogether. There was this nice analogy by Martin Odersky at OSCON in 2011 - 

{% include figure.html path="blog/personal/space.png" alt="Space vs Time" %}

Imperative programming languages can be thought of performing a sequence of actions over time whereas functional programming languages can be thought of building functions over space (parallel to time). In the series of next blog posts, you'll learn about Scala - a language that although is not strictly functional, bridges the gap between Imperative and Functional.