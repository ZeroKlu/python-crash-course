print("Chapter 10:")
print("Exercise 5 - Write a File\n")

# --- 2nd Edition Method ---

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "programming.txt")

with open(file_path, "w") as file:
    file.write("I love programming!\n")
    file.write("I love creating new games!\n")

with open(file_path, "r") as file:
    print(file.read())

def write_line(file_object, text):
    file_object.write(f"{text}\n")
    
with open(file_path, "w") as file:
    write_line(file, "I love coding!")
    write_line(file, "I love creating new applications!")

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(file_path, "r") as file_object:
    print(file_object.read())

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path

file_path = get_path("programming.txt", "Files")

file = Path(file_path)

file.write_text("I love programming!\n")

print(file.read_text())

def write_line(path_object, text):
    path_object.write_text(f"{text}\n")

content = """I love programming!
I love creating new games.
I also love working with data."""

write_line(file, content)

print(file.read_text())

content = "I also love finding meaning in large datasets.\n"
content +="I love creating apps that can run in a browser.\n"

with file.open("a") as f:
    f.write(content)

print(file.read_text())
