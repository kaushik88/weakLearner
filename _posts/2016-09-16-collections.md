---
layout: post
title: "Collections"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

In this blog post, you'll learn about immutable collections - 

1. Lists
2. Vectors
3. Arrays

At the top of the hierarchy, we've **Iterable**. Iterable has 3 children - **Sequence**, **Set** and **Map**. **List**, **Range** and **Vector**  are sub-classes of Sequence.

### Lists

Here's how you declare a list - 

{% gist kaushik88/57ee2ac8b3bb663dd1461e5241a49597 list-declaration.scala %}

So when we declare a list of Strings called fruits, the language allocates 3 cells for fruits - the first cell for apples, the second cell for oranges and the third cell for bananas. The first cell has a pointer to the second cell and the second cell has a pointer to the third cell. The third cell has a pointer to *Nil*.

**Nil** is an empty list. You can construct a list using the :: (cons) operator.

{% gist kaushik88/57ee2ac8b3bb663dd1461e5241a49597 list-construction.scala %}

Lists are optimized for recursive operations and do not perform well for random access. In the above example, the 3 cells (apples, oranges and bananas) could potentially be randomly located in memory.

### Vectors

Vectors are essentially represented as very, very shallow trees. 

1. When a Vector has less than 32 elements, then this is equivalent to an Array of 32 elements (contiguous data).

2. When the size of the Vector goes beyond 32 elements, then in the first level we've 32 pointers. Each of the pointer points to a Vector (size 32) in the second level. So this is 2^10 elements.

3. When the size of the Vector goes beyond 2<sup>10</sup>, then the depth of the tree becomes 3 where the inner levels are just pointers to the actual elements in the leaf node.

4. The read time is of the complexity O(log <sub>32</sub> N)

Vectors are really good for bulk operations (map, reduce, fold etc) but then are not optimized for head and tail operations.

### Ranges

Ranges are stored compactly in Scala - all we need is to store 3 parameters (start, end and step value). It is also easy to construct ranges in Scala - 

{% gist kaushik88/57ee2ac8b3bb663dd1461e5241a49597 range.scala %}

