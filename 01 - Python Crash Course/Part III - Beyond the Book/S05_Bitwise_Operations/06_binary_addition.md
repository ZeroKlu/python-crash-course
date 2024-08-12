## Binary Addition

In order to understand how binary representations of integers work,
it's useful to first take a look at the way binary addition is handled
by a computer.

---

### The Binary Adder

A binary adder (at its core) is a circuit. Optimally, all that circuit 
should do is:

1. Take in two bits `A` & `B` (plus a carry bit `C`)
2. Add them together where
```
           A   B   Sum Carry
        a. 0 + 0 =  0    0
        b. 0 + 1 =  1    0
        c. 1 + 0 =  1    0
        d. 1 + 1 =  0    1
```
3. Return the output and pass the carry bit (if needed) to the next bit adder

---

Such a circuit looks sort of like this:

```
      A & B are the input bits, and C is the carry
     ┌──────────────────────────────────────────────────────────────────────────────────┐
     │                          Full Adder                                              │
     │    ┌──────────────────┐              ┌──────────────────┐                        │
 A───│───>│             SUM  │───A ^ B──────│             SUM  │───(A ^ B) ^ C──────────│───> Sum
     │    │ Half Adder       │              │ Half Adder       │                        │
 B───│───>│            CARRY │───A & B──┐ ┌─│            CARRY │───C & (A ^ B)─┐        │
     │    └──────────────────┘          │ │ └──────────────────┘               │ ┌────┐ │
 Cin─│──────────────────────────────────│─┘                                    └─│    │ │
     │                                  │                                        │ ≥1 │─│───> Cout
     │                                  └────────────────────────────────────────│    │ │
     │                                                                           └────┘ │
     └──────────────────────────────────────────────────────────────────────────────────┘
```

---

### Addition with the Adder Circuit

Looking at the behavior of the circuit, we can see that there are eight 
possible scenarios to account for:

|   A   |   B   |  Cin  |       |   S   | Cout  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|   0   |   0   |   0   |       |   0   |   0   |
|   0   |   0   |   1   |       |   1   |   0   |
|   0   |   1   |   0   |       |   1   |   0   |
|   0   |   1   |   1   |       |   0   |   1   |
|   1   |   0   |   0   |       |   1   |   0   |
|   1   |   0   |   1   |       |   0   |   1   |
|   1   |   1   |   0   |       |   0   |   1   |
|   1   |   1   |   1   |       |   1   |   1   |

---

Let's examine the case where `A = 1`, `B = 1`, and `Cin = 0`

This is equivalent to adding `1 + 1` with no previous carry coming in.

* `A` & `B` enter the first half-adder
    * Both are 1s, so:
        * SUM (S₁) = `A XOR B` = `1 XOR 1` = `0`
        * CARRY (C₁) = `A AND B` = `1 AND 1` = `1`
* S₁ and Cin enter the second half-adder
    * Both are 0s, so:
        * SUM (S) = `S₁ XOR Cin` = `0 XOR 0` = `0`
        * CARRY (C₂) = `S₁ AND Cin` = `0 AND 0` = `0`
* S is 0, so the output sum is `0`
* C₁ + C₂ = `1 + 0` = 1, and since `1 ≥ 1`, `Cout = 1`

So, binary 1 + 1 = 0, with a carry (to the next place) of 1

```
  0000 0001
+ 0000 0001
  ---------
          ⌄--- S
  0000 0010
         ^--- C
```

Hence 1 + 1 = 2 (or rather `10` in binary)

---

### Negatives in a Binary Adder

Looking at its minimal implementation, a circuit like this is not
designed to know the difference between positive and negative numbers.
All it does is add binary digits (and track the carry bit).

But, since there is no subtraction circuit, computers add negatives in
order to handle subtraction as an operation.

Because of that, we need a system of numbering in which the results from
the adder circuit are consistent for positive and negative numbers without 
requiring a different circuit for negative numbers (or subtraction).

We know that we can use a specific bit for the sign, but how do we create a
binary numbering system where the results are consistent?

The next topics will explain that...

---
