print("Chapter 10:")
print("Exercise 10 - Handling a FileNotFoundError\n")

# --- 2nd Edition Method ---

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "alice_missing.txt")

file_name = file_path.split("\\")[-1]

try:
    with open(file_path, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    print(f"Found file: {file_name}")

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path

file_path = get_path("alice_missing.txt", "Files")
file_name = file_path.split("\\")[-1]

try:
    file = Path(file_name)
    contents = file.read_text()
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    print(f"Found file: {file_name}")
