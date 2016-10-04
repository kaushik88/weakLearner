---
layout: post
title: "Reduce, Fold and FoldLeft"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about - 

1. The basic understanding of reduce, fold and foldLeft.
2. The subtle difference between the 3 of them.

In order to explain these 3 functions, let us take a list of integers - 

val oddNumbers :List[Int] = List(1,3,5,7,9,11,13)

### Reduce

For a list of Integers, here's how the signature of reduce is defined - 

def reduce[A1 >: Int](op: (A1, A1) => A1): A1

Let us now understand this signature : 

1. reduce is a function that now operates on type A1 that is a *supertype* of type Int.
2. reduce takes in a function as a parameter which itself takes in 2 parameters of type A1 and also has a return type of A1.
3. The reduce function returns of type A1.

Consider the following example - 

	/**
	* A simple function which takes in 2 integers and returns the sum of the 2 integers.
	* @param number1 
	* @param number2
	* @return 
	*/

	def additionReduce(number1: Int, number2: Int) : Int = {
		number1 + number2
	}

	oddNumbers.reduce{additionReduce}

So, what's happening above - 
	1. I've defined a function addition which adds 2 numbers.
	2. The reduce function takes this function as a parameter to reduce the list of integers to an integer.

### Fold

For the same example above, here's how the signature of fold is defined - 

def fold[A1 >: Int](z: A1)(op: (A1, A1) => A1): A1

Let us now understand this signature : 

1. Like reduce, fold is a function that now operates on type A1 that is a *super-type* of type Int.
2. Unlike reduce, fold takes in 2 parameters - an integer (starting value) and a function (similar to reduce).
3. The fold function's return type is also A1.

	def additionFold(accumulator: Int, number: Int) : Int = {
			accumulator + number
		}
	oddNumbers.fold(0)(additionFold)

So, what's happening above - 
	1. The starting value for fold is now 0.
	2. The fold now takes in (0, 1) and the addition function is performed.
	3. The return value of that function and the second value in the list is now passed to the function again.
	4. This continues to happen till we've processed all the elements in the list.

### FoldLeft

override def foldLeft[B](z: B)(op: (B, Int) => B): B

Let us now understand this signature : 

1. foldLeft takes in 2 parameters - an object of type B (has no relation to Int), and a function. The function takes in 2 parameters, 1 of type B and 1 of type Int.
2. The function and foldLeft returns an object of type B.

oddNumbers.fold(0)(additionFold)

### Reduce/Fold vs FoldLeft

* The Big Big difference between Reduce/Fold and FoldLeft is that the former can be implemented in parallel but foldLeft cannot be implemented in parallel (as the order of execution is fixed). As a result, reduce/fold only accepts an operation that is both commutative and associative. As a result, it is common to see *reduce* functions in MapReduce paradigms like Scalding and also in Spark.

* The primary difference between reduce/fold and foldLeft is the order in which the fold operation iterates through the collection. In foldLeft, it starts on the left side—the first item—and iterates to the right. Fold/Reduce goes in no particular order.

* FoldLeft is more powerful than Fold in terms of the types it can support. You can use foldLeft on a list of integers to do some complicated operation and return an object. However, in fold/reduce you can only return a superType of Int.

### Reduce vs Fold

There is only a subtle difference between reduce and fold.

1. Reduce requires the operator to be both commutative and associative whereas fold requires the operator to be associate only.

2. As a result of this, fold requires a start value whereas reduce doesn't require one.
