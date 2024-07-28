print("Chapter 10:")
print("Exercise 8 - Working with Multiple Files\n")

# --- 2nd Edition Method ---

import os

ROOT_DIR = os.path.dirname(__file__)

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_words(file_name)

print()

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path

def count_file_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    except Exception as ex:
        print(ex)
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_file_words(file_name)
