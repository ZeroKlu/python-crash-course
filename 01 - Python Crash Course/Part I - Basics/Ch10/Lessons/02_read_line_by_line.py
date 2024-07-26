print("Chapter 10:")
print("Exercise 2 - Read a File Line-by-Line\n")

# --- 2nd Edition Method ---
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print()

# --- 3rd Edition Method ---
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text()

lines = text.splitlines()
for line in lines:
    print(line.rstrip())
