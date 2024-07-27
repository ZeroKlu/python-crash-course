import os

ROOT_DIR = os.path.dirname(__file__)

"""Get the approximate word count from a file."""
def count_words(file_name):
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
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
        
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "missing.txt"]
for file_name in file_names:
    count_words(file_name)
