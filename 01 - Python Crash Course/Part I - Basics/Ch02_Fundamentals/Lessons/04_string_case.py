"""Chapter 2: Lesson 4"""

print("Chapter 2:")
print("Exercise 4 - Manipulating String Case")

name = "ada lovelace"
# Print in Title Case
print(f"Title Case: {name.title()}")

# Print in UPPER CASE
print(f"UPPER CASE: {name.upper()}")

# Print in lower case
print(f"lower case: {name.lower()}")

# Print in sentence case
print(f"Sentence case: {name.capitalize()}")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
