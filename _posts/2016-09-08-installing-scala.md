---
layout: post
title: "Scala - Getting Started"
tags:
- Scala
categories:
- Code
thumbnail_path: blog/personal/scala-logo.png
---

This is the first post in a series of blog post on **Scala**. In this post, we'll go over setting up Scala on a Mac. I believe the process must be similar for other Operating Systems as well.

#### 1. Download Scala binaries from [here](http://www.scala-lang.org/download/)

Download the tar in Option 1 from the image below.

{% include figure.html path="blog/personal/scala-howTo.png" alt="Scala Download" %}

#### 2. Unpack it

- tar zxvf fileNameHere.tgz

#### 3. Change your PATH variable

- SCALA_HOME = /path/to/scala
- PATH = $PATH:/$SCALA_HOME/bin

#### 4. Start REPL

Since Scala is an interpretive language (it is also compile-able), you can try it out using a REPL (Read-Eval-Print-Loop). This is an easy way to quickly try out a function or a logic in your mind. Just type scala on the command-line - 

- scala

Let me know if this works for you!