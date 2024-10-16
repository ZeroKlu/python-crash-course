"""Chapter 5: Lesson 3"""

print("Chapter 5:")
print("Exercise 3 - Handling Multiple Conditions")

# Using logical operators, you can check more than one condition in an if statement

# Logical "and"
#  p | and | q
# -------------
#  T |  T  | T    * Only true when both conditions are true
#  T |  F  | F
#  F |  F  | T
#  F |  F  | F
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 21
print(age_0 >= 21 and age_1 >= 21)

# Logical "not"
#  not |  p
# -----------
#   T  |  F
#   F  |  T
print(age_0 >= 21 and not age_1 < 21)

# Logical "or"
#  p | or  | q
# -------------
#  T |  T  | T
#  T |  T  | F
#  F |  T  | T
#  F |  F  | F    * Only false when both conditions are false
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# In boolean logic, there is also the concept of "xor" (exclusive or)
#  p | or  | q
# -------------
#  T |  F  | T
#  T |  T  | F    * Only true when exactly one of the conditions is true
#  F |  T  | T    * Only true when exactly one of the conditions is true
#  F |  F  | F

# Python does not provide an operator for xor, but you can simulate it by combining and and or operators
p = True
q = False

# There are multiple ways to express xor
p_xor_q = (p or q) and not (p and q)
print(f"{p} XOR {q} = {p_xor_q}")

p_xor_q = (p and not q) or (q and not p)
print(f"{p} XOR {q} = {p_xor_q}")
