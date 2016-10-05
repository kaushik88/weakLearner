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

{% gist kaushik88/7901d9b9c4ec39488e4448f617cf406d implicit-functions.scala %}

In this example, I’ve defined an implicit function that takes in an integer and returns a string. This enables me to use all functions of String (target type) on Integers (source type). Note that, the Scala compiler wouldn’t convert all Integers to Strings and would convert them only if the code wouldn’t compile in the first place.


### Implicit Parameters

Consider the example where you want to define a function which needs to take in a value and needs to pretty print it with the currency symbol. Instead of passing the currency symbol every time, you can define a function which takes in an implicit variable of type Currency. When the function printAmount() is called, an implicit variable of type Currency is needed for it to compile successfully.

{% gist kaushik88/7901d9b9c4ec39488e4448f617cf406d implicit-parameters.scala %}