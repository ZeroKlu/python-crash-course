## Two's Complement

Enter the solution that is implemented for numbers in modern computing: **two's complement**

Two's complement is just one's complement *plus one*.

---

### A Four-Bit Example

So with our known positive values (in our imaginary 4-bit integer):

* `0000` = 0
* `0001` = 1
* `0010` = 2
* `0011` = 3
* `0100` = 4
* `0101` = 5
* `0110` = 6
* `0111` = 7

---

The two's complement implementation for negatives would look like this:
* `0000` =  0
* `1111` = -1
* `1110` = -2
* `1101` = -3
* `1100` = -4
* `1011` = -5
* `1010` = -6
* `1001` = -7  
  ... which leaves a wasted bit, so
* `1000` = -8

... and this is why we have an extra negative value in integer data types

---

### Does This Really Work?

We can check ourselves by looking at the same examples we've been using:

---

### 1 - 1

```
      0001
    + 1111
    ------
 1 <- 0000
```

The previously lost carry bit doesn't matter any more, and we get the 
correct answer: ```1 - 1 = 0```

---

### 7 - 3

```
      0111
    + 1101
    ------
 1 <- 0100
```

Again, although we lose a carry bit, we end up with the right answer:
```7 - 3 = 4```

---

### Problem Solved!

Implementation of a two's complement negatives system ensures that we
always get the correct answer when performing binary addition with our
adder circuits, even if the signs don't match.

---

### Wait a minute! Now integer overflow makes sense too!

Now that we understand that the number system uses two's complement for
negatives, the overflow behavior we saw earlier makes sense.

If we go back to using an 8-bit integer, and look at our 127 + 1 problem:

```c
#include <stdio.h>

int main() {
                  //     ⌄--- remember, this is the sign bit
    char b = 127; // b = 0111 1111 =  127
    b++;          // b = 1000 0000 = -128
    printf("b = %i", b);

    return 0;
}
```

We can predict that this is the expected overflow behavior by doing the
binary addition:

```
  0111 1111
+ 0000 0001
-----------
  1000 0000
```

And we see the previously inexplicable behavior of ```127 + 1 = -128``` for
an 8-bit signed integer emerge as a result of overflowing into the sign 
bit.

---

### Verification

Just to verify that this is the expected behavior:

* 128 in binary is ```1000 0000```
* One's complement of that is ```0111 1111```
* Two's complement (one's complement plus one) then is ```1000 0000```

So ```-128``` is the expected result

---
