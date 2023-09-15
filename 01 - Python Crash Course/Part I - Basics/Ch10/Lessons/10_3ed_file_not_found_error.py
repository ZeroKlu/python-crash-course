from relative_paths import get_path
from pathlib import Path

file_path = get_path("alice_missing.txt", "Files")
file_name = file_path.split("\\")[-1]

print("Chapter 10:")
print("Exercise 10 - Handling a FileNotFoundError\n")

# Note: The 'try' block should surround code for specific functionality, not all of the code
try:
    file = Path(file_name)
    contents = file.read_text()
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    # By default, split() splits the string into an array on spaces ' '.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")
