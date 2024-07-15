## Ch 2 - Lesson 8: Arithmetic Operators

Python provides the standard set of arithmetic operators you find in most
programming languages, as well as a couple that are less common.

---

### Supported Arithmetic Operators

|||||
|-|-|-|-|
|Operator|Meaning|Example(s)|Notes|
|+|add|`3 + 2` -> `5`||
|-|subtract|`3 - 2` -> `1`||
|*|multiply|`3 * 2` -> `6`||
|/|divide|`3 / 2` -> `1.5`||
|||`4 / 2` -> `2.0`|Division always returns a float|
|**|exponent|`3 ** 2` -> `9`||
|//|integer division|`3 // 2` -> `1`|Drops the decimal part after dividing|
|%|modulo|`3 % 2` -> `1`|Remainder|
|||||

### Operator Precedence

OK - We're going to travel back in time to pre-algebra class...

Python adheres to the PEMDAS order of operations when performing arithmetic
operations.

This means that operations higher on the list below are performed before 
items lower on the list.

* [**P**]arentheses (and other grouping symbols)
* [**E**]xponents
* [**M**]ultiplication and [**D**]ivision
* [**A**]ddition and [**S**]ubtraction

Within the same precedence, operations are performed from left to right.

---

So, following PEMDAS precedence, consider the following operation:

`3 + 2 * 4`

Multiplication has a higher precedence than addition, so it is performed
first (`2 * 4` -> `8`), making the expression the same as:

`3 + 8` which yields `11`

---

However, if we include grouping, which has higher precedence than
multiplication, like this:

`(3 + 2) * 4`

The operation in parentheses is performed first (`3 + 2` -> `5`), making 
the expression the same as:

`5 * 4` which yields `20`

---

### A note on Python Integers

Integers in Python are not fixed-size like they are in other languages.
Because of this, the maximum value for a Python integer is limited only by 
the available system RAM.

---
