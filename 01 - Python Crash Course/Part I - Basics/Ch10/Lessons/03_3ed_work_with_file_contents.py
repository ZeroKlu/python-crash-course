from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files", debug=True)

print("Chapter 10:")
print("Exercise 3 - Work with File Contents\n")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text()

lines = text.splitlines()
for line in lines:
    # Here we are using the content of the line to update our 'pi_string' variable
    # We have switched from rstrip() to strip() to remove the leading spaces as well after line 1
    pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
