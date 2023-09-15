# Assignment 10.9
# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

from relative_paths import get_path
from pathlib import Path

log_path = get_path("missing_files.log.txt", "Files")
log_file = Path(log_path)

print("Try-it-Yourself:")
print("Assignment 10.9\n")

def read_file(file_name):
    """Read the selected file"""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        content = file.read_text()
    except FileNotFoundError:
        with log_file.open("a") as l:
            l.write(f"Missing File:\n{file_path}\n\n")
        pass
    else:
        print(f"{file_name}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
