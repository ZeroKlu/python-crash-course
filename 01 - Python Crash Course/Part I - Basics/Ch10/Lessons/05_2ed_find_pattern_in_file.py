import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

print("Chapter 10:")
print("Exercise 5 - Read a File and Search for a Pattern\n")

pi_string = ""

with open(file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

# Get a pattern to search for in the file contents
birthday = input("Enter your birthday in the form MMDDYY:\n> ")

# Let's look to see if the string entered appears somewhere in pi_string
if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appears in the first million digits of pi.")
