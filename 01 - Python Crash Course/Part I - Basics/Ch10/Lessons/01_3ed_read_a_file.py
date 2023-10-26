# Note: I have added the code labeled "# Module-based relative path method" below to be able to access files in
#         a separate folder (via relative path) when executing in Visual Studio
#       The book discusses file paths as well, but it does not cover how to consistently access relative paths

from relative_paths import get_path
from pathlib import Path

print("Chapter 10:")
print("Exercise 1 - Read a File\n")

# Module-based relative path method
file_path = get_path("pi_digits.txt", "Files")

# Here we are actually opening the file
# Create a path object
path_object = Path(file_path)
# Read in the file contents as text
text = path_object.read_text()

# rstrip() is used here to prevent printing a blank line at the end of the file
print(text.rstrip())
