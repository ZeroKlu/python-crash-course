from relative_paths import get_path
from pathlib import Path

# THe only change from our previous example is that now we are pointing to a larger file
file_path = get_path("pi_million_digits.txt", "Files", debug=True)

print("Chapter 10:")
print("Exercise 3 - Work with File Contents\n")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text()

lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

# Get a pattern to search for in the file contents
birthday = input("Enter your birthday in the form MMDDYY:\n> ")

# Let's look to see if the string entered appears somewhere in pi_string
if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appears in the first million digits of pi.")
