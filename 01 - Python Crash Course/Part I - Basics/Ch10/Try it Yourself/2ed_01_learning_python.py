# Assignment 10.1
# Learning Python: Open a blank file in your text editor and write a few lines summarizing what
#                  you’ve learned about Python so far. Start each line with the phrase 'In Python you can...'
#                  Save the file as learning_python.txt in the same directory as your exercises from this
#                  chapter. Write a program that reads the file and prints what you wrote three times. Print
#                  the contents once by reading in the entire file, once by looping over the file object, and
#                  once by storing the lines in a list and then working with them outside the with block.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "T.10.01.learning_python.txt")

print("Try-it-Yourself:")
print("Assignment 10.1\n")

# Read and print entire file
with open(file_path) as file:
    result = file.read()
    print(result.rstrip())

print()
    
# Print line-by-line
with open(file_path) as file:
    for line in file:
        print(line.rstrip())

print()

# Store as a list
# Read and print entire file
with open(file_path) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
