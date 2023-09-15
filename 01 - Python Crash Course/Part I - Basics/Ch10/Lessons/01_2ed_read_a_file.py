# Note: I have added the code labeled "# Manual relative path method" below to be able to access files in
#         a separate folder (via relative path) when executing in Visual Studio
#       The book discusses file paths as well, but it does not cover how to consistently access relative paths

import os

# Perform Lesson Tasks
print("Chapter 10:")
print("Exercise 1 - Read a File\n")

# Manual relative path method
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

# Here we are actually opening the file
# Note: Using the 'with' keyword will ensure that we release the file after reading it
#       This is similar to the C# 'using' keyword
with open(file_path) as file_object:
    # Store all lines of text in a list
    text = file_object.read()

# if we did not use the 'with' keyword, the code above would look like this:
# file_object = open(file_path)
# text = file_object.read()
# file_object.close()

# This is risky, because any error between open() and close() would leave the file locked in the OS

# rstrip() is used here to prevent printing a blank line at the end of the file
print(text.rstrip())
