import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "programming.txt")

print("Chapter 10:")
print("Exercise 7 - Append to a File\n")

# First, let's check what the file already contains
with open(file_path, "r") as file_object:
    print(file_object.read())

with open(file_path, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Let's verify that we appended to the existing file
with open(file_path, "r") as file_object:
    print(file_object.read())
