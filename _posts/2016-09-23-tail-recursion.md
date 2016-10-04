---
layout: post
title: "Tail Recursion"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn to - 

1. Understand the different types of recursion.
2. Understand why tail recursion is more effecient.

Consider the following recursive function to compute the GCD.

def gcd(a : Int, b : Int) : Int = {
	if (b == 0) a else gcd (b, a % b)
}

Here's how the stack trace of this would look like - 

gcd(14, 21)
	-> gcd (21, 14 % 21)
	-> gcd (14, 7)
	-> gcd (7, 0)
	-> 7

Let us look at another type of recursion - factorial.

def factorial(num :Int) : Int = {
	if (n == 0) 1 else num * factorial(num - 1)
}

factorial(4)
	-> 4 * factorial(3)
	-> 4 * 3 * factorial(2)
	-> 4 * 3 * 2 * factorial(1)
	-> 4 * 3 * 2 * 1 * factorial(0)
	-> 24

What's the difference between the above 2 types of recursion. The expression in the factorial function grows as we go deeper in the recursion. However, for GCD the expression stays the same - it osciallates between one call to another.

> If the function calls itself as its last action, the function's stack frame could be reused. This is called *tail recursion*.

In tail recursion, the stack frame of the function could be reused and hence it could execute in constant stack space. JVM restrict the size of the stack frame to a couple of thousand and hence if you think that your function could have a lot of depth, it might be wise to re-implement it as tail-recursive.