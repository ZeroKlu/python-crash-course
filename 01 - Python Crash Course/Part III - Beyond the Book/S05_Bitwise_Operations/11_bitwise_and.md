## Using Bitwise AND (`&`)

The bitwise AND operator (`&`) is used to compare two values and return
only the intersection of their set (`1`) bits.

At each binary position (i), the result of the operation is equivalent to
multiplying the bits together and can be expressed as follows.

`(a & b)ᵢ = aᵢ × bᵢ`

Since 1 × 1 is 1, and any number n × 0 is 0, we can see that this matches
the bitwise truth table we laid out for this operator, where a 1 is 
returned only in bit positions where both of the compared values contain 1.

| b1 | & | b2 |
|:---|:-:|---:|
| 1  | 1 |  1 |
| 1  | 0 |  0 |
| 0  | 0 |  1 |
| 0  | 0 |  0 |

---

### Example

Consider this scenario:

```
    a = 10011100₂ = 156₁₀
    b = 00110100₂ =  52₁₀
a & b = 00010100₂ =  20₁₀
```

Only the positions where the bit is 1 in both a and b return a 1 from the
`&` operation.

As long as we understand that what's being compared are the individual
bits, we can express the values in any base with the same results

See [bitwise_and.py](./11_bitwise_and.md)

```python
a = 0b10011100 # 156
b = 0b00110100 # 52
print(f"{bin(a & b)[2:]:>08}") # --> 00010100 (20)

x = 156
y = 52
print(x & y) # --> 20
```

Output:

```
00010100
20
```

---

### A Simple Example: Checking for an Even Number ###

There are many places where it's useful to check if a number is odd or even.

#### Using Modulo

Typically, most of us have been taught to do that using a modulo (or remainder)
computation like this:

See [even_numbers.py](./11_even_numbers.py)

```python
def is_even(n: int) -> bool:
    return not n % 2
```

---

### Using Bitwise AND

Another approach would be to perform a bitwise check on the ones-place bit.

See [even_numbers.py](./11_even_numbers.py)

```python
def is_even(n: int) -> bool:
    return not n & 1
```

Let's imagine checking the number 42

```
  0010_1010  (42)
& 0000_0001  ( 1)
-----------
  0000_0000  ( 0)
```

Since no position has ones in both numbers, the result is zero (even)

or 73...

```
  0010_1001  (73)
& 0000_0001  ( 1)
-----------
  0000_0001  ( 1)
```

The ones place has ones in both numbers, as it must for an odd number, 
since ```2⁰ = 1``` is the only odd power of two, so the result is one (odd)

---

The bitwise comparison is inherently faster than a modulo computation, 
because division is a cumbersome process in a computer.

Of course, in modern programming languages, the compilers are optimized for
well-known scenarios like this one, so ```n % 2``` will compile to the same
assembly language instructions as ```n & 1```, which means that there 
isn't a  practical reason to choose one over the other.

---
