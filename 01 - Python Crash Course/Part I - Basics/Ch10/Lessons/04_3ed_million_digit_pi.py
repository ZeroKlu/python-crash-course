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

# Since pi_string is a million digits long, let's just print out to 50 decimal places
print(pi_string[:53])
print(f"pi_string is {len(pi_string)} characters long.\n")
