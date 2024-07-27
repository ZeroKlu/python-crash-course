print("Chapter 10:")
print("Exercise 1 - Read a File\n")

# --- 2nd Edition Method ---
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

file_object = open(file_path)
text = file_object.read()
print(text.rstrip(), "\n")
file_object.close()

with open(file_path) as file_object:
    text = file_object.read()
print(text.rstrip())

print()

# --- 3rd Edition Method ---
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")
path_object = Path(file_path)

text = path_object.read_text()
print(text.rstrip())
