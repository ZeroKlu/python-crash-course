## An Intuitive (but Wrong) Implementation of Negative Integers

For these illustrations, we'll simplify beyond what the computer uses
and imagine a 4-bit integer type.

Since this is a signed integer, we'll use the rightmost bit (the 8s
place) as our sign bit.

---

That means that for our positive values, we have the following set:

* `0000` = 0
* `0001` = 1
* `0010` = 2
* `0011` = 3
* `0100` = 4
* `0101` = 5
* `0110` = 6
* `0111` = 7

---

If we implement negative numbers intuitively, we'd assume that all of the
binary digits would be the same as the positive numbers, with only the sign
bit flipped, like this:

* `1000` = -0
* `1001` = -1
* `1010` = -2
* `1011` = -3
* `1100` = -4
* `1101` = -5
* `1110` = -6
* `1111` = -7

---

### What's wrong with that?

This approach introduces two major flaws:

1. There are two different values for zero
    * This is wasteful, since there is no mathematical difference between
      0 and -0
    * It also results in the possibility that adding zero could flip the
      sign on the number it's being added to.

2. The way the adder circuit works, we would get incorrect answers, so this
   would necessitate a more complicated circuit, affecting performance.
    * Imagine the scenario where we're adding 1 + -1 (see below)
        * The result (see table in previous topic) of adding two 1s is 2
        * It doesn't matter what we do with the sign bit, because 1 - 1 = 
          0, not 2 or -2

---

### Adding Our Invalid Negatives

Recall that ```0 - 1``` is the same as ```0 + -1``` so let's look at the
result of that (using our intuitive system) in binary addition

1 (as 4-bit binary) is 0001

-1 (as 4-bit binary) is 1001

```
  0001
+ 1001
  ----
  1010
```

So according to our system, 1 - 1 = -2

---

### Overflowing into the Sign Bit

Other numbers can lose a carry bit and flip the sign.

Consider ```7 - 3``` or ```7 + -3```

7 = 0111

-3 = 1011

```
  0111
+ 1011
  ----
  0010
```

So according to our system, 7 - 3 = 2

---

### What Now?

So, this solution is clearly not going to work. The next idea is...

---
