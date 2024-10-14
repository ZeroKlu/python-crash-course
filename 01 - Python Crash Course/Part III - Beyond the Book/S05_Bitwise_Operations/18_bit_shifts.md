## Using Bit-Shifts (`<<` and`>>`)

A bit-shift operation literally shifts the bit values in a field a
specified number of positions to the left (`<<`) or right (`>>`).

---

### Right Bit-Shift is Division by Two

Right-shifting a value is equivalent to dividing the value by two to the 
power of the number of positions shifted:

`n >> p = n / 2 ** p`

So, if we have a value $n=128$, and bit-shift it to the right $3$ 
places, we get the value $128/2^3=16$

```python
x = 128
b = x >> 3
print(f"{x} >> 3 = {b}")
```

Output:

```
128 >> 3 = 16
```

Looking at that in binary, we have:

```
        1000 0000 (128)
        ^--⌄  (the 1 moves three places to the right)
>> 3    0001 0000  (16)
```

---

### Left Bit-Shift is Multiplication by Two

Left-shifting a value is equivalent to multiplying the value by two to the 
power of the number of positions shifted:

```n << p = n * 2ᵖ```

With our existing value ```n = 16```, if we shift to the left three places, 
we get the value ```16 * 2³ = 128```

```python
x = 16
b = x << 3
print(f"{x} << 3 = {b}")
```

```
        0001 0000  (16)
        ⌄--^  (the 1 moves three places to the left)
<< 3    1000 0000 (128)
```

---

### Overflow and Underflow Can Result in Data Loss

Assuming we're limited to 8-bits, what happens when we shift so that we
overflow a bit into the ninth place?

#### No Overflow In Python

Python integers grow dynamically, so as long as there is memory available,
we will not encounter overflow.

```python
# Overflow doesn't happen in Python
x = 64
b = x << 3
print(f"{x} << 3 = {b}")
```

Output:

```
64 << 3 = 512
```

Binary View:

```
         0100 0000  (64)
      ⌄---^  (the 1 moves three places to the left)
<< 3  10 0000 0000 (512)
```

The Python integer grows to support the extra bits required.

---

#### Overflow in Languages with Static-Size Integer Types

Let's take a look at integer overflow in C. We'll use an `unsigned char` type,
which is the equivalent of an 8-bit byte in C.

See [bit_shift_overflow.c](./18_bit_shift_overflow.c)

```c
#include <stdio.h>

int main() {
    unsigned char x, b;

    // Overflow
    x = 64;
    b = x << 3;
    printf("%d\n", b);

    return 0;
}
```

Output:

```
64 << 3 = 0
```

Binary View:

```
         0100 0000  (64)
      ⌄---^  (the 1 moves three places to the left)
<< 3  10 0000 0000 (512)
```

This would yield 256 if we had a ninth bit into which to shift. But, since
we only have 8 bits to consider, the bit containing the 1 is lost, and the
returned value is 0.

---

#### Underflow in Python

We can also lose information when we right shift past the ones place 
(underflow).

Unlike overflow, Python *is* vulnerable to underflow.

```python
x = 4
b = x >> 3
print(f"{x} >> 3 = {b}")
```

Output:

```
4 >> 3 = 0
```

Binary View:

```
        0000 0100    (4)
              ^---⌄  (the 1 moves three places to the left)
>> 3    0000 0000 1  (Undefined value - There is no zeros place)
```

---

#### Underflow in Languages with Static-Size Integer Types

For completeness, let's look at our C example for underflow as well

```c
#include <stdio.h>

int main() {
    unsigned char x, b;

    // Underflow
    x = 4;
    b = x >> 3;
    printf("%d >> 3 = %d\n", x, b);

    return 0;
}
```

Output:

```
4 >> 3 = 0
```

Binary View:

```
        0000 0100    (4)
              ^---⌄  (the 1 moves three places to the left)
>> 3    0000 0000 1  (Undefined value - There is no zeros place)
```

---

### A Simple Example: Iterating Over a BitFlag

In some scenarios, it's useful to check all the bits in a bit-flag value.

An easy approach to this is to use a bit-shift to cycle through each bit in
the ones place.

Let's imagine that we have a bit-flag enum for our program settings.

```python
from enum import IntFlag

class Settings(IntFlag):
    DebugMode = 1,
    InteractiveMode = 2,
    RememberSettings = 4,
    Optimize = 8
```

In a scenario where we want to check all of the settings, we can do something
like this:

See [iterate_flags.py](./18_iterate_flags.py)

```python
from random import randint

# -- SNIP --

settings = randint(0, 15)
print(f"With Settings: {settings}, the following bits are set:")
currentValue = 1
while settings > 0:
    if settings & 1: print(f"- {Settings(currentValue).name}")
    settings >>= 1
    currentValue <<= 1
```

Output:

```
With Settings: 15, the following bits are set:
- DebugMode
- InteractiveMode
- RememberSettings
- Optimize
```

Run this a few times to see different results when the random `settings`
value changes.

---
