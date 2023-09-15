import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

print("Chapter 10:")
print("Exercise 3 - Work with File Contents\n")

pi_string = ""

with open(file_path) as file_object:
    for line in file_object:
        # Here we are using the content of the line to update our 'pi_string' variable
        # We have switched from rstrip() to strip() to remove the leading spaces as well after line 1
        pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
