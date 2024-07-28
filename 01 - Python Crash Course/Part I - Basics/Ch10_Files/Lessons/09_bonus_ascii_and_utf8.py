print("Chapter 10:")
print("Exercise 8 - Working with Multiple Files\n")

# --- 2nd Edition Method ---

import os

ROOT_DIR = os.path.dirname(__file__)
file_name = "moby_dick.txt"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path, encoding="utf-8") as f:
    contents = f.read()
    print(len(contents))

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path

file_name = "moby_dick.txt"
file_path = get_path(file_name, "Files")
file = Path(file_path)
contents = file.read_text(encoding="utf-8")
print(len(contents))
