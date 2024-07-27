from relative_paths import get_path
from pathlib import Path

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        # This will simply ignore the error and continue processing
        pass
        # WARNING: This is extremely risky, as you will neither be handling nor recording errors
        #          This can result in unexpected issues in downstream code
        #          You WILL be required to justify this on code reviews
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.\n")

print("Chapter 10:")
print("Exercise 12 - Failing Silently\n")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_words(file_name)
