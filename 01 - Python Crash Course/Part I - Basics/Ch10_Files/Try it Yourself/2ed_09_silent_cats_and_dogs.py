# Assignment 10.9
# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

import os

ROOT_DIR = os.path.dirname(__file__)
log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log.txt")

print("Try-it-Yourself:")
print("Assignment 10.9\n")

def read_file(file_name):
    """Read the selected file"""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path) as f:
            content = f.read()
    except FileNotFoundError:
        with open(log_path, "a") as l:
            l.write(f"Missing File:\n{file_path}\n\n")
        pass
    else:
        print(f"{file_name}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
