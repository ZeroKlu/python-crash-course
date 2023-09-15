import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "alice_missing.txt")

file_name = file_path.split("\\")[-1]

print("Chapter 10:")
print("Exercise 10 - Handling a FileNotFoundError\n")

# Note: The 'try' block should surround code for specific functionality, not all of the code
try:
    with open(file_path, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    # By default, split() splits the string into an array on spaces ' '.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")
