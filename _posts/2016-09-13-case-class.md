---
layout: post
title: "Case Class"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

Case classes can be seen as plain and immutable data-holding objects that should exclusively depend on their constructor arguments.

{% gist kaushik88/3db738c1b63583a999bf6bad02538cde case-class.scala %}

When you define a case class, the following things happen automatically - 

1. Each of the constructor parameters are declared as a val and you've getters and setters for each of them.

2. An *apply* method is provided - this would let you create new objects using the *new* keyword.

3. Methods *toString*, *equals*, *copy* and *hashCode* are generated - this would help you serialization, deserialization, comparison and copying objects.

4. Case classes are also optimized for use in Pattern Matching.

All these benefits are seen in the sample code below - 

{% gist kaushik88/3db738c1b63583a999bf6bad02538cde case-class-benefits.scala %}