---
layout: post
title: "Map, FlatMap and Filter"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll read about - 

1. Some basic operations on collections - Map, FlatMap and Filter (Duh!)

We'll be working with a list of Ints : 

val numbers : List[Int] = List(1,2,3,4,5,6,7,8,9,10)

### Map

A *map* operation is used to transform the list. Here's the signature of map for the above list - 

def map[B](f: Int => B): scala.collection.TraversableOnce[B]

Let us understand the signature - 

1. The map function takes in another function f. f takes in an Int (an item of the list - one at a time) and returns B.

2. It returns a collection of type B (the transformed type).

val squareNumbers : List[Int] = numbers.map{case number :Int => number * number}
// List(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

### FlatMap

A *flatMap* operation is nothing but a map operation followed by a flatten operation. *Flatten* collapses one level of nested structure.

def flatMap[B](f: Int => scala.collection.GenTraversableOnce[B]): scala.collection.TraversableOnce[B]                                                               
Let us understand this signature - 

1. The function f takes in an Int and returns a Collection of type B.
2. This level of nested structure is collapsed to return a collection of type B.

val squaresAndCubes :List[Int] = numbers.flatMap{case number :Int => List(number * number, number * number * number)}
// List(1, 1, 4, 8, 9, 27, 16, 64, 25, 125, 36, 216, 49, 343, 64, 512, 81, 729, 100, 1000)

1. Each and every operation in the flatMap returns a List.
2. The flatten operation collapses this level of list.

### Filter

A *Filter* operation is used to filter out values from a collection based on some property of the element in the collection. 

   def filter(p: Int => Boolean): List[Int]

Let us understand this signature - 

1. The function p takes in an Int (each and every element in the collection) and returns a Boolean.
2. The filter function returns a list of Int, all the elements that returned *true* for that function.

val oddNumbers : List[Int] = numbers.filter{case number :Int => number % 2 == 1}
// List(1, 3, 5, 7, 9) 

**Final Note** - As can be seen, these operations execute on 1 value at a time and hence really easy to parallelize. As a result, they're commonly used in Scalding and Spark.