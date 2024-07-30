print("Chapter 10:")
print("Exercise 10 - Failing Silently\n")

# --- 2nd Edition Method ---

import os

ROOT_DIR = os.path.dirname(__file__)

"""Get the approximate word count from a file."""
def count_words(file_name):
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "missing.txt"]
for file_name in file_names:
    count_words(file_name)

print()

log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log")

"""Get the approximate word count from a file."""
def log_words(file_name):
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        with open(log_path, "a") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "missing.txt"]
for file_name in file_names:
    count_words(file_name)

print()

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_words(file_name)

print()

log_path = get_path("missing_files.log", "Files")
log_file = Path(log_path)

def log_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        with log_file.open("a") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    log_words(file_name)
