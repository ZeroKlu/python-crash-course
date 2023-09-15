import os
ROOT_DIR = os.path.dirname(__file__)

# THe only change from our previous example is that now we are pointing to a larger file
file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

print("Chapter 10:")
print("Exercise 4 - Million Digit Pi\n")

pi_string = ""

with open(file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

# Since pi_string is a million digits long, let's just print out to 50 decimal places
print(pi_string[:53])
print(f"pi_string is {len(pi_string)} characters long.\n")
