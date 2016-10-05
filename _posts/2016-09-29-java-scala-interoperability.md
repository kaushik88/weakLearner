---
layout: post
title: "Java To Scala Interoperability"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post you'll learn about - 

1. How to work with Java's collections in Scala.

This blog post will use the *JavaConverters* to convert from Scala Collections to Java Collections and vice-versa.

Here's the conversion table - 

1. Iterator               <=>     java.util.Iterator
2. Iterator               <=>     java.util.Enumeration
3. Iterable               <=>     java.lang.Iterable
4. Iterable               <=>     java.util.Collection
5. mutable.Buffer         <=>     java.util.List
6. mutable.Set            <=>     java.util.Set
7. mutable.Map            <=>     java.util.Map
8. mutable.ConcurrentMap  <=>     java.util.concurrent.ConcurrentMap

{% gist kaushik88/c62c5706973cd69d5857b94cecff0051 j2s.scala %}