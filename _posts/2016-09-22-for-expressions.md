---
layout: post
title: "For Expressions"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about - 

1. An easy-to-read alternative to higher order functions like map, flatMap and filter.
2. Easily handle combinatorics.

While *map*, *filter* and *flatMap* are powerful paradigms, sometimes they could get harder to read, especially while dealing with nested higher order functions. In order to deal with this, we have for-expressions. Despite similar syntax to for-loops in Java, for-expressions are different in the fact that it is an expression which builds from the output of each of the iteration.

Consider the following example - 

{% gist kaushik88/89c1724b36d8321a317234539a60d542 nested-map.scala %}

As can be seen, this is hard to understand. Hence, Scala came up with for-expressions.

{% gist kaushik88/89c1724b36d8321a317234539a60d542 for-expressions.scala %}

As you can see above, this is much easier to read!!

