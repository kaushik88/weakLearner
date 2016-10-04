---
layout: post
title: "Var-Val-Def"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

What you'll learn in this blog post - 

1. How to declare immutables and variables in Scala.
2. How to define functions in Scala.

**Val**

A *val* is a way of declaring immutables in Scala. By *immutable*, I mean that the value of a variable cannot be modified or changed after the declaration. As a result of this constraint, you've to initialize a *val* when you declare it.

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f val.scala %}

A few notes on *val* - 

1. A val is more easier to read and understand as it is always initialized at the time of declaration. 

2. A val is more safer - you don't have to worry if some other part of your code is changing it. This becomes even more important in multi-threaded systems.

3. Due to the functional nature of Scala and also due to Pattern Matching, I believe *val*s are more commonly used than *var*s.

4. Although you cannot change the value of a *val*, you should be able to change the state of a val object.

**Var**

A *var* is a way of declaring mutables (or variables) in Scala.

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f var.scala %}

A few notes on vars - 

1. The main drawbacks of val is that for some scenarios, it is not intuitive to use vals. It would be a lot easier to use vars. 

Consider the following example, to note this difference

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f var-val.scala %}

**def**

In Scala, *def* is a way to define a function. More about functions in this gist - 

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f def.scala %}

One of the useful features of functions in Scala is that the arguments can take default values. Here's how you can define them - 

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f default-arguments.scala %}