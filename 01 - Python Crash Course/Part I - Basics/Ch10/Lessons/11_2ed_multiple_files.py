import os

ROOT_DIR = os.path.dirname(__file__)

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        # Note: A couple of the Project Gutenberg files require us to specify the character encoding
        with open(file_path, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        # This prevents the script from crashing when a file is not found
        print(f"Sorry, the file {file_name} does not exist.\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.\n")

print("Chapter 10:")
print("Exercise 11 - Working with Multiple Files\n")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_words(file_name)
