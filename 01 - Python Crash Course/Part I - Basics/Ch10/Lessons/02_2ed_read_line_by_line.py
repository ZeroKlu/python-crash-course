import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

print("Chapter 10:")
print("Exercise 2 - Read a File Line-by-Line\n")

with open(file_path) as file_object:
    # The file_object is already a list of its lines, so we can simply act on them instead of storing a new list
    for line in file_object:
        # Now we can perform work on each line as we encounter it
        # We still use the rstrip() function to remove the newline characters at the ends of the lines
        print(line.rstrip())

# We could also get the lines manually, like this:
with open(file_path) as file_object:
    # Explicitly store the lines in a list
    lines = file_object.readlines()
# This allows us to work with the lines outside of the with block (after the file is closed)
for line in lines:
    print(line.rstrip())
