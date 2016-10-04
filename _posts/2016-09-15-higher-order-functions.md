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

def sumInts(a : Int, b : Int) : Int = {
	if (a > b) 0 else a + sumInts(a+1, b)
}

def cube(x : Int) : Int = x * x * x

def sumCubes(a: Int, b : Int) : Int = {
	if (a > b) 0 else cube(a) + sumCubes(a+1, b)
}

Definitely, there is a pattern between sumInts and sumCubes. In fact, we're used to writing this as a mathematical expression - 

Sum f(x) from a to b.

We can achieve the same abstraction in Scala, through the following sytax - 

def sum(f : Int => Int, a : Int, b : Int) : Int = {
	if (a > b ) else f(a) + sum(a+1, b)
}

Let us understand this function definition - 

1. sum takes in 3 parameters - a function, an Int and an Int.
2. The first parameter is a function which takes an Int and returns an Int.
3. This can be called like these - 

sum(cube, 2, 5)	
sum( x => x * x * x, 2, 5)		// Anonymous Functions