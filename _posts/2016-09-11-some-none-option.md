---
layout: post
title: "Some-None-Option"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

What you'll learn in this blog post - 

1. Scala's response to Java's mistake of creating null.

If you've ever worked in Java, you definitely know about the *NullPointerException*. A NullPointerException occurs when you try to access an object (without handling the null case), but then it was a *null*. NullPointerExceptions are really common in Java and one reason for this is that there is no way for a developer to communicate to either self or another developer that the value for an object is **Optional**.

Scala tries to solve the problem by providing a type for representing optional values, i.e. values that may be present or not: the Option[A] trait. Option[A] is a container for an optional value of type A. If the value of type A is present, the Option[A] is an instance of Some[A], containing the present value of type A. If the value is absent, the Option[A] is the object None.

{% gist kaushik88/b58b47620c123ce25126643a4ffaed67 options.scala %}

Options are also used in pattern matching (we'll cover about this in the next blog post). We'll also look at a more cleaner way of handling None when we learn about **FlatMap**.