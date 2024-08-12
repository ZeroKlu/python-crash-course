## One's Complement

Another option that was looked at in early computer design was to implement
negative numbers as the ***one's complement*** of their positive 
counterparts.

One's complement is simply the binary complement (opposite value for each 
bit) of the positive value.

---

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

The one's complement implementation would look like this:

* `1111` = -0
* `1110` = -1
* `1101` = -2
* `1100` = -3
* `1011` = -4
* `1010` = -5
* `1001` = -6
* `1000` = -7

---

### OK - So what's wrong with this one?

We still have the problem of both positive and negative zeroes.

Addition is also still a problem, though less so than in the previous example.

Let's look at the same examples we saw in the previous topic:

---

### 1 - 1

```
  0001
+ 1110
------
  1111
```

This gives a result of ```1 - 1 = -0```, which isn't perfect (because what
even is -0?), but if we add 1 to the result:

```
      1111
    + 0001
    ------
 1 <- 0000  *lost (overflowed) carry bit here
```

We end up with the expected value of ```0```

---

### 7 - 3

```
      0111
    + 1100
    ------
 1 <- 0011
```

Which gives ```7 - 3 = 3```, which is wrong, but again if we add 1 (which
we can think of as wrapping the lost carry bit)...

```
      0011
    + 0001
    ------
      0100
```

We get the right answer of ```7 - 3 = 4```

---

### So Close!

This business of wrapping the lost carry bit doesn't make sense without 
extra hardware (and extra memory, since we don't have a fifth bit to hold 
it in).

So, how do we address the problem of getting results that are off by one?
And is there a way to get rid of that pesky negative zero?

---
