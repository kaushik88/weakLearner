---
layout: post
title: "Higher Order Functions"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn 

1. How to treat functions as first class citizens.

Consider the following example, 

{% gist kaushik88/4ac3f98f2882937faf7f777a12447434 higher-order-functions.scala %}

Definitely, there is a pattern between sumInts and sumCubes. In fact, we're used to writing this as a mathematical expression - 

$$
\begin{align*}
  \sum_{x=a}^{b} f(x)
\end{align*}
$$

We can achieve the same abstraction in Scala, through the following sytax - 

{% gist kaushik88/4ac3f98f2882937faf7f777a12447434 higher-order-functions2.scala %}


Let us understand this function definition - 

1. sum takes in 3 parameters - a function, an Int and an Int.
2. The first parameter is a function which takes an Int and returns an Int.
3. This can be called like these - 

{% gist kaushik88/4ac3f98f2882937faf7f777a12447434 higher-order-functions-example.scala %}