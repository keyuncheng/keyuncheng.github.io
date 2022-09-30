---
title: 'Erasure Coding Basic Concepts'
date: 2021-07-18
permalink: /posts/2021/07/blogs-ec-basic-concepts/
author_profile: false
excerpt: false
tags:
  - erasure coding
  - basics
---


Must-know erasure coding concepts for beginners 

Finite Field
------

* field
    * operators: addition, multiplication
    * implementation: checkout [Clemenson's note](https://people.cs.clemson.edu/~westall/851/rs-code.pdf) on implementation of these two parameters
    * multiplication by checking log-table and log-inverse
    * fast multiplication on powers of 2

* prime
    * prime ideal

* polynomial
    * minimal polynomial
    * irreducible polynomial
    * generator polynomial

* conversion of a finite field to binary polynomials
    * differential equation
    * how to to find the irreducible polynomial
    * how the generator polynomial is constructed

* related codes
    * linear code
    * cyclic code
    * BCH code
    * Reed-Solomon code
    * bit-matrix code
    * array code

* systmatic code and non-systematic code construction

* online coding / offline coding