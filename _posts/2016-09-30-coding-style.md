---
layout: post
title: "Coding Style"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about - 

> Coding Style for better readability.

**1. Use Pattern Matching for Collection functions like map, filter, flatMap** - 

val numbers : List[Int] = List(1,2,3)
val squares : List[Int] = numbers.map(n => n * n)	// bad naming and no data types
val squares : List[Int]	= numbers.map{case number :Int => number * number}	// pattern matching syntax makes it more readble.

**2. Avoid return statements when possible**

In scala, return statements are optional and hence should be avoided when possible.

**3. Avoid using variables or vars**

> Make your variables immutable, unless there's a good reason not to.
