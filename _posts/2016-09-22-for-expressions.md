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

val nums : List[Int] 		= List(1,2,3,4,5)
val pairsWithEvenSums : List[(Int, Int)] = nums flatMap (num1 => nums map (num2 => (num1, num2))) filter (pair => (pair._1 + pair._2) %2 == 0)

// List((1,1), (1,3), (1,5), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), (5,1), (5,3), (5,5))

As can be seen, this is hard to understand. Hence, Scala came up with for-expressions.

for ( seq ) yield expr

for {
	num1 <- nums				// Generator
	num2 <- nums				// Generator
	sum = num1 + num2			// Definition
	if sum % 2 == 0				// Filter
} yield (num1, num2)

As you can see above, this is much easier to read!!

