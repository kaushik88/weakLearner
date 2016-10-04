---
layout: post
title: "Generics, SubTypes and SuperTypes"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about - 

1. How to define a Generic class and a Generic function.
2. How to restrict the type of the parameters being passed to a function.

### Generics

As in Java, classes and traits can have type parameters. Consider the example below,

class Pair[T, S](val first : T, val second : S)

The above line defines a class that has 2 parameters - first (of type T) and second (of type S). This is very useful as when you want to build a Pair object, now the 2 parameters could be of any type.

**Generic Functions**

def getMiddleElement[T](a : Array[T]) : T = a(a.length / 2)

What's happening above?

1. We've defined a generic function - a function of type T. 
2. It takes in a parameter *a* - an Array of type T.
3. It then returns the middle element. Hence the function return type is T.

**Bounds**

Consider the pair class that we've defined above but where both the elements are of the same type - 

class Pair[T](val first :T, val second :T) {
	def smaller = if (first.compareTo(second) < 0) first else second // Error
}

The function throws an error as you do not know if the type T has a compareTo method. In order to impose this restriction, you need T to be a sub-Type of Comparable[T]. What this means is that, Comparable must be a parent of T.

class Pair[T <: Comparable[T]](val first :T, val second :T) {
	def smaller = if (first.compareTo(second) < 0) first else second // Error
}

In a similar way, you can also define supertypes using the '>:' operator.

> T <: Lower >: Upper