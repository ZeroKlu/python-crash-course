# Assignment 10.8
# Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first
#                file and three names of dogs in the second file. Write a program that tries to read these
#                files and print the contents of the file to the screen. Wrap your code in a try-except block
#                to catch the FileNotFound error, and print a friendly message if a file is missing. Move one
#                of the files to a different location on your system, and make sure the code in the except
#                block executes properly.

import os

ROOT_DIR = os.path.dirname(__file__)

print("Try-it-Yourself:")
print("Assignment 10.8\n")

def read_file(file_name):
    """Read the selected file"""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\nFile [{file_name}] not found!\n")
    else:
        print(f"\n{file_name}:")
        print(content.rstrip())

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
