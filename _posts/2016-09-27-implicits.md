---
layout: post
title: "Implicits"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn - 

1. Implicit Functions
2. Implicit Parameters

### Implicit Functions

Implicit functions take a single parameter and are automatically called (if in scope or is defined in the companion object of the target type) on the source type variable if there is a type mis-match. For example, consider the following example —

object TypeConversion {
	implicit def ito(a :Int) :String = {
		a.toString
	}
}

/* 
Example 1- 
	In this example, The Scala Compiler first checks fif there is a concat() method for Integers. If there is no such method, it checks if there is an implicit method that takes an Integer as a parameter
*/
val thirtyFour :String = 3.concat(4)

/*
Example 2- 
	In this example, the Scala compiler doesn't do an implicit conversion from Integer to String as the expression is a valid expression
*/
val thirtySix :Int = 3 * 12

In this example, I’ve defined an implicit function that takes in an integer and returns a string. This enables me to use all functions of String (target type) on Integers (source type). Note that, the Scala compiler wouldn’t convert all Integers to Strings and would convert them only if the code wouldn’t compile in the first place.


### Implicit Parameters

Consider the example where you want to define a function which needs to take in a value and needs to pretty print it with the currency symbol. Instead of passing the currency symbol every time, you can define a function which takes in an implicit variable of type Currency. When the function printAmount() is called, an implicit variable of type Currency is needed for it to compile successfully.

case class Currency(symbol :String)

object TypeParameters {
	def printAmount(amount :Double)(implicit currency :Currency) = {
		println(currency.symbol + amount)
	}
}

object Dollar {
	implicit val dollarCurrency = Currency("$")

	def printDollar(value :Dollar) = {
		TypeParameters.printAmount(value)
	}
}