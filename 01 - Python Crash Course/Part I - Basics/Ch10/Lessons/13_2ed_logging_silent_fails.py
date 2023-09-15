import os

ROOT_DIR = os.path.dirname(__file__)
log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log")

"""Get the approximate word count from a file."""
def count_words(file_name):
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # Here, we are writing the error to a log file
        with open(log_path, "a") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
        # Now, the 'pass' is not as bad, because we dealt with the error
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.\n")

print("Chapter 10:")
print("Exercise 13 - Logging Silent Fails\n")
        
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "missing.txt"]
for file_name in file_names:
    count_words(file_name)
