print("Chapter 5:")
print("Exercise 7 - Bitwise Operations")

import sys

# Although the book does not spend time on this topic, understanding bitwise operators is very useful for
# a Python developer.

# First, we need to understand a little about binary
# In the binary, or base-2 number system, there are only two digits, 0 and 1

# In our standard base-10 (decimal) system, we have the typical digits, 0 through 9
# As you traverse a number from right to left, each position represents ten times the previous one
#   So, if you have this base-10 number:      255
#       There are five 1s, five 10s, and two 100s

# In binary, as we traverse a number from left to right, each position represents two times the previous one
#   So, if you have this binary number:      11111111
#       There is one 1, one 2, one 4, one 8, one 16, one 32, one 64, and one 128
#       You might notice that the sum of these is 255 (the max value of a single 8-bit byte)
#       So, 11111111 binary is equivalent to 255 in decimal
#       Likewise, 00000000 binary is equivalent to 0 decimal

# Because there are exactly two possible values in each binary digit (and because under the covers all
#   numbers in a computer are stored as binary), it's almost inevitable that people would decide to use
#   individual binary digits to store boolean values (imagine 1 = TRUE and 0 = FALSE)

# This is useful, because in Python, a boolean value takes up one byte, but by using each bit, you can store
#   eight times as many boolean properties in the same space. This is the fundamental concept behind a bitflag.

# Let's simplify and only use 4 bits in an example.

# We have a value of 1001 binary, which is the equivalent of 8 + 0 + 0 + 1 = 9
my_settings = 9
signed_integer = -10
  
# Adding 1<<32 to convert signed to
# unsigned integer
unsigned_integer = signed_integer+(1 << 32)
print(unsigned_integer)

# If we want to check if the setting in the 8s place is on, we can perform a binary operation to check it
# The binary AND operator (&) checks each bit in two numbers and sets a third one where bits are set to 1
#   only if they are 1 in both of the numbers being compared

# We'll make a value of 1000 binary (8 decimal), because we only want to check the 8s place.
my_comparison = 8

# Since & only returns 1 when both digits in a place are 1s, we know it will return 0 in the 1s, 2s, and 4s
# So, if the 8s place is set in the original number (we know it is set in the comparison), then we'll get back
#   a value of 1000 (or 8)

# Breaking it down in our example
#   my_settings:        1001
#   my_comparison:      1000
#   bitwise AND (&):    1000 (because only the 8s place has 1s in both rows) -> returns 8

# So, we can use our existing knowledge of boolean logic like this:
if (my_settings & my_comparison) == my_comparison:
    print("\nThe 8s setting is enabled\n")
else:
    print("\nThe 8s setting is NOT enabled\n")

# A real-world application of using a bitflag with binary & is checking if a specific product license is enabled

# ----------------------

# Of course, there is a bitwise OR operator (|) as well.
# Bitwise OR returns a 1 in each place where at least one of the numbers has a 1 in that place

# So, with our existing numbers, we'd see this:

#   my_settings:        1001
#   my_comparison:      1000
#   bitwise OR (|):     1001 (because both the 1s place and the 8s place have at least one 1) -> returns 9

# We might imagine an OR scenario where we're checking user permissions when a user is in two groups
# In a least-restrictive system, the user would receive the combination of both permission sets

my_permissions = my_settings | my_comparison

for i in [2 ** x for x in range(4)]:
    if my_permissions & i == i:
        print(f"The user has permission {i}")
        # We expect to see permissions 1 and 8

# ----------------------

# For bitwise operations, we have an XOR (^) operator that only sets a place to 1
#   only if exactly one number has a 1 in that place

# So, with our existing numbers, we'd see this:

#   my_settings:        1001
#   my_comparison:      1000
#   bitwise XOR (^):    0001 (because only the 1s place has exactly one 1) -> returns 1

my_xor = my_settings ^ my_comparison
print(f"\n{my_settings} XOR {my_comparison} = {my_xor}")

# Bitwise XOR was used in early (but not very secure) cryptographic systems because it's
#   reversible if you have the key (and the key is the same length in bits as your text)

# So, after out first XOR, we'd see this:
#   my_xor:             0001
#   my_comparison:      1000
#   bitwise XOR (^):    1001 (because both the 1s and 8s places have exactly one 1) -> returns 9

# Note how XORing the result with the same comparison gives us back the original settings value of 9
print(f"{my_xor} XOR {my_comparison} = {my_xor ^ my_comparison}")

# ----------------------

# Bitwise NOT (~) swaps each bit in a value

# If I look at the original settings value

#   my_settings:        1001
#   bitwise NOT (~):    0110    ->      should return 6

print(f"\n{~my_settings}\n")

# Actually returns -10.. Why?

# There's a lot going on here...
# In computers we usually represent numbers using 32 bits,
# so binary representation of 9 is (....0000 1001)[32 bits]

# Bitwise negation (NOT) is a 1's complement of the number (reverses every bit)
# This generates an intermediate result of (....1111 0110)

# But the leftmost bit of an integer is a sign bit, and when it gets reversed,
#   that makes the number negative, and negative numbers are represented as 2's complement,
#   which is the result of 1's complement plus 1
# This makes the end result (....0000 1001) + 1 = (...0000 1010) = 10
# But, with the sign-bit set, we end up with -10

# Moral: Be super careful using bitwise NOT unless you have a deep understanding of
#        1's and 2's complements and how they relate to integers in the computer

# ----------------------

# Bit-shifting is the last of the bitwise operators.
# This is no longer a logical computation but instead an arithmetic one

# When you bit-shift a number it literally moves all of the bits over in the specified direction.

# What's cool about this is that you can easily double or halve a number, because shifting one bit
#   to the left (<<) multiplies by two and to the right (>>) divides by two.

# So with this value (0010 = 2)...
x = 2

# If I bit-shift one place to the left (0100 = 4)...
x = x << 1
print(x, "\n")

# And then if I shift it back to the right two places (0001 = 1)...
x = x >> 2
print(x, "\n")

# But here's where you have to be careful. If you shift past the end, you lose the bits that overflow
# So, 0001 shifted to the right becomes 0000 (0) not 0.5
x = x >> 1
print(x, "\n")

# The same thing can happen when you shift too far to the left.
# You can shift into the sign bit and mess up you value entirely.

# Moral: Be careful of overflow when bit-shifting
