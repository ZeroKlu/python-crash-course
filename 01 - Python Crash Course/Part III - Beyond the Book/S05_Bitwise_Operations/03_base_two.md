## Base 2 (Binary)

Remember our rule:

Starting from the rightmost position and traversing right-to-left, the 
place values are `bᵖ` where `b` is the base and `p` is the position relative 
to the rightmost number (how many digits away).

---

### Position Values

Following the same logic we saw in base 10, in base 2, the position 
values are just powers of two instead of ten (although I will express 
their values as base 10 here for convenience):

* 2⁰ = 1
* 2¹ = 2
* 2² = 4
* 2³ = 8
* 2⁴ = 16
* 2⁵ = 32
* 2⁶ = 64
* 2⁷ = 128
* and so on

This means in our binary byte we have the following places:

|      |      |      |      |      |      |      |      |      |
|------|------|------|------|------|------|------|------|------|
|  ... | 128s |  64s |  32s |  16s |  8s  |  4s  |  2s  |  1s  |

---

### Computed Values

Reading binary numbers is similar to decimal: the sum of the non-zero 
position values.

So:

* 0000 0000 = **0**
* 0000 0001 = **1** (1 * 1)
* 0000 0010 = **2** (1 * 2) + (0 * 1)
* 0000 0011 = **3** (1 * 2) + (1 * 1)
* ...
* 1111 1111 = **255** (128 + 64 + 32 + 16 + 8 + 4 + 2 + 1)

That means that there are 256 possible values available in an 8-bit 
byte, which makes perfect sense, since 2⁸ = 256

And for an unsigned 8-bit integer, these values range from 0 to 255

---
