---
layout: post
title: "Var-Val-Def"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

**Val**

A *val* is a way of declaring immutables in Scala. Hence, when you declare a *val*, you've to initialize it.

{% gist kaushik88/7ea61e62fb4404366af59fb5a1c8967f %}

A few notes on *val* - 

1. A val is more easier to read and understand as it is always initialized at the time of declaration. 

2. A val is more safer - you don't have to worry if some other part of your code is changing it. This becomes even more important in multi-threaded systems.

3. Due to the functional nature of Scala and also due to Pattern Matching, I believe *val*s are more commonly used than *var*s.

4. A val is similar to the **final** keyword in Java - so although you cannot change the value of a *val*, you should be able to change the state of a val object.

**Var**

A *var* is a way of declaring mutables (or variables) in Scala.

{% gist kaushik88/ec286ee0966acda650d08167e681411a %}

A few notes on vars - 

1. The main drawbacks of val is that for some scenarios, it is not intuitive to use vals. It would be a lot easier to use vars. 

Consider the following example, to note this difference

{% gist kaushik88/6b3179655abc4cfad384a24ba73eaa66 %}

**def**

In Scala, *def* is a way to define a function. More about functions in this gist - 

{% gist kaushik88/296e85f7c8b6eadd742bac47577535f2 %}