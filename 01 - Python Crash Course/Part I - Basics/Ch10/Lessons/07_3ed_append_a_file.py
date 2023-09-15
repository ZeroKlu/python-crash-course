from relative_paths import get_path
from pathlib import Path

file_path = get_path("programming.txt", "Files")

file = Path(file_path)

print("Chapter 10:")
print("Exercise 7 - Append to a File\n")

# First, let's check what the file already contains
print(file.read_text())

content = "I also love finding meaning in large datasets.\n"
content +="I love creating apps that can run in a browser.\n"

# To append, we need to use a similar method to what we did in the 2nd edition code
# The difference, is that we don't need to pass a filename, since our Path object already has that
with file.open("a") as f:
    f.write(content)

# Finally, let's check that the file has been appended
print(file.read_text())
