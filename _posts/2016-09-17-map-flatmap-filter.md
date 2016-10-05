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

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 basic.scala %}

### Map

A *map* operation is used to transform the list. Here's the signature of map for the above list - 

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 map-function-syntax.scala %}

Let us understand the signature - 

1. The map function takes in another function f. f takes in an Int (an item of the list - one at a time) and returns B.

2. It returns a collection of type B (the transformed type).

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 map.scala %}

### FlatMap

A *flatMap* operation is nothing but a map operation followed by a flatten operation. *Flatten* collapses one level of nested structure.

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 map.scala %}
                                                               
Let us understand this signature - 

1. The function f takes in an Int and returns a Collection of type B.
2. This level of nested structure is collapsed to return a collection of type B.

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 flatmap.scala %}

1. Each and every operation in the flatMap returns a List.
2. The flatten operation collapses this level of list.

### Filter

A *Filter* operation is used to filter out values from a collection based on some property of the element in the collection. 

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 filter-func-def.scala %}

Let us understand this signature - 

1. The function p takes in an Int (each and every element in the collection) and returns a Boolean.
2. The filter function returns a list of Int, all the elements that returned *true* for that function.

{% gist kaushik88/00f3812f4b56751ad979ca1da99af738 filter.scala %}

**Final Note** - As can be seen, these operations execute on 1 value at a time and hence really easy to parallelize. As a result, they're commonly used in Scalding and Spark.