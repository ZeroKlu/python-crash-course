from relative_paths import get_path
from pathlib import Path

print("Chapter 10:")
print("Exercise 2 - Read a File Line-by-Line\n")

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text()

# Split the text into lines
lines = text.splitlines()
for line in lines:
    # Now we can perform work on each line as we encounter it
    # We still use the rstrip() function to remove the newline characters at the ends of the lines
    print(line.rstrip())
