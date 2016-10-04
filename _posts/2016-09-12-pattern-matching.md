---
layout: post
title: "Pattern Matching"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

What you'll learn in this blog post - 

1. Scala's response to Java's switch statement.
2. Pattern Matching for Options.
3. Exception Handling in Scala.

**Switch Statement**

Switch statement is a common way in C/C++/Java to match a given variable and have different behaviors for different values. This is a sample syntax - 

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 java-switch.java %}

There are a couple of limitations in this - 

1. *Switch* is a statement and not an expression. In the example above, we assign *monthString* to a value in every branch.

2. The Fall-Through Problem - You must explicitly have a break statement at the end of every branch, or you will fall through to the next branch.

Scala solves both the problems using Pattern Matching.

**Pattern Matching**

The same code above is simplified to the code below - 

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 pattern-match.scala %}

**Guards**

Guards enable you to add a condition to guard your default case. This makes the code much easier to read rather than nested switch statements or an if block within a switch branch in Java. Consider the example below - 

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 pattern-match-guards.scala %}

**Variables In Patterns**

In Scala, you can also have a variable following a case keyword. This is used in a couple of scenarios - 

1. When you want to use the value of the variable in the branch.
2. When you match for type. This is a preferred method when compared to *isInstanceOf* operator.

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 pattern-match-variables.scala %}

**Option Match**

In Scala, pattern matching is also used to get the value of an Option type. This is done through the code below - 

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 pattern-match-options.scala %}

**Exception Handling** 

Exception Handling in Scala is a lot similar to Java. It also follows a similar syntax as the Pattern Matching.

{% gist kaushik88/b8c2a3d2d1ced24e5e9a246e8598ecf3 pattern-match-try-catch.scala %}