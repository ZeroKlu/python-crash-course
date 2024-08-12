## A Bit about Integers

> *"I see what you did there..."*  
> &nbsp;&nbsp;~Literally Everyone

A byte is comprised of 8 bits, each of which can be a one or a zero. 
Binary (base 2) is the basis of bitwise computation.

In most programming languages, the default integer type is four bytes 
(32 bits) long, but for simplicity, we'll work with 8-bit integers in 
this lesson.

---

### Position Values

In all of our numbering systems, the position values (1's place, e.g.) 
are computable. Starting from the rightmost position and traversing 
right-to-left, the place values are `bᵖ` where `b` is the base and `p` is 
the position relative to the rightmost number (how many digits away).

---

So, for any numbering system, the place values look like this.

|    |    |    |    |    |
|----|----|----|----|----|
| ...| b³ | b² | b¹ | b⁰ |

---

And reading the value of a number, where `d` is the digit in a given 
place, looks like this (sum of each digit times its position value):

|          |          |          |          |          |
|----------|----------|----------|----------|----------|
|    ...   | + d * b³ | + d * b² | + d * b¹ | + d * b⁰ |

---
