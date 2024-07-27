# Assignment 10.8
# Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first
#                file and three names of dogs in the second file. Write a program that tries to read these
#                files and print the contents of the file to the screen. Wrap your code in a try-except block
#                to catch the FileNotFound error, and print a friendly message if a file is missing. Move one
#                of the files to a different location on your system, and make sure the code in the except
#                block executes properly.

from relative_paths import get_path
from pathlib import Path

print("Try-it-Yourself:")
print("Assignment 10.8\n")

def read_file(file_name):
    """Read the selected file"""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        content = file.read_text()
    except FileNotFoundError:
        print(f"File [{file_name}] not found!\n")
    else:
        print(f"{file_name}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
