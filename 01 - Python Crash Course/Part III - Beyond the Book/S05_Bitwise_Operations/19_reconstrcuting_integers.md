## Bit_Shift - Real-World Example: Reconstructing Integers

Bit-shifting can be very useful when we know that a byte represents some other
value.

### Scenario

You have an incoming data stream that you've read into a byte array.

You know that the incoming data represents 32-bit integer values and that 
within each set of four bytes, the least significant digits come first and the
most significant digits last.

You need to reconstruct the integer values from the byte array.

---

### Structure of the Data

Let's imagine that the array contains only one 32-bit integer, broken up into
four bytes:

```python
bytes = [ 0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001 ]
```

---

### First Byte is Easy

We know the first byte represents bits 0-7, so we can take it as-is.

```python
num = bytes[0] # 73
```

---

### Second Byte is Less So

The second byte, however, represents bits 8-15.

The value of ```0000_0010``` in isolation is 2, and we might naively decide
to add it to the value we've stored:

```python
# This won't work
num += bytes[1] # 75
```

---

### Fixing the Wrong Answer

But that value doesn't make sense. We know that bits 8-15 have values from 256
to 32,768. So, given that at least one of those bits is set, we can't possibly
have a result less than 256.

Instead, we need to multiply this byte by 256 to get the result we expect

```python
num += bytes[1] * 256 # 585
```

---

### Simplifying with Bit-Shift

And that will work, but we'd then have to multiply the third byte by 65,536 
and the fourth by 16,777,216.

Those numbers are pretty easy to remember, but the process would get more 
difficult as we started working with items that are larger than four bytes.

But since they are all powers of two, we can accomplish the same thing by 
bit-shifting:

|Byte|Low Bit|Shift|Value|
|:-:|:-:|:-:|-:|
|0|2⁰|none|1|
|1|2⁸|<< 8|256|
|2|2¹⁶|<< 16|65,536|
|3|2²⁴|<< 24|16,777,216|

We can modify the code to use the bit-shift like this:

```python
num += bytes[1] << 8 # 585
```

---

#### Looping Through the Bytes

So, a loop like this would handle each four-byte set:

```python
num = 0
for p in range(4):
    num += bytes[p] << (p * 8)
```

---

### The Whole Solution

I have included an example of this process.

See [](./19_reconstrcuting_integers.py)

```python
def reconstruct_integers(bytes: list[int], size: int=4) -> list[int]:
    assert len(bytes) % size == 0, "Invalid data!"

    num_units = len(bytes) // size

    integers = []

    for n in range(0, num_units * size, size):
        data = bytes[n:n+size]
        integers.append(reconstruct_integer(data, size))
    
    return integers

def reconstruct_integer(data: list[int], size: int=4) -> int:
    assert len(data) == size, "Invalid data!"

    num = 0

    for p in range(len(data)):
        num += data[p] << (p * 8)
    
    return num

def main() -> None:
    bytes = [
        0b0000_0000, 0b0000_0000, 0b0000_0000, 0b0000_0000,
        0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001,
        0b0001_0101, 0b1100_1101, 0b0101_1011, 0b0000_0111,
        0b1111_1111, 0b1111_1111, 0b1111_1111, 0b1111_1111
    ]
    values = reconstruct_integers(bytes)
    for value in values:
        out = f"{value:,}"
        print(f"{out:>13}")

if __name__ == "__main__":
    main()

```

Output:

```
            0
1,234,567,890
  123,456,789
4,294,967,295
```

Try putting in some different sets of bytes and see what your output looks 
like.

---
