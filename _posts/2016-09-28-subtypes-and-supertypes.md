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

{% gist kaushik88/879ed8185f81d085364450e2c93132e3 pair.scala %}

The above code defines a class that has 2 parameters - first (of type T) and second (of type S). This is very useful as when you want to build a Pair object, now the 2 parameters could be of any type.

**Generic Functions**

{% gist kaushik88/879ed8185f81d085364450e2c93132e3 middleElement.scala %}

What's happening above?

1. We've defined a generic function - a function of type T. 
2. It takes in a parameter *a* - an Array of type T.
3. It then returns the middle element. Hence the function return type is T.

**Bounds**

Consider the pair class in the example above but where both the elements are of the same type - 

{% gist kaushik88/879ed8185f81d085364450e2c93132e3 bounds1.scala %}

The function throws an error as you do not know if the type T has a compareTo method. In order to impose this restriction, you need T to be a sub-Type of Comparable[T]. What this means is that, Comparable must be a parent of T.

{% gist kaushik88/879ed8185f81d085364450e2c93132e3 bound2.scala %}

In a similar way, you can also define supertypes using the '>:' operator. More specifically, you could combine both the subType and superType this way - 

{% gist kaushik88/879ed8185f81d085364450e2c93132e3 bound3.scala %}