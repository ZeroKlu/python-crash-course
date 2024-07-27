from relative_paths import get_path
from pathlib import Path

log_path = get_path("missing_files.log", "Files")
log_file = Path(log_path)

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        # Here, we are writing the error to a log file
        with log_file.open("a") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
        # Now, the 'pass' is not as bad, because we dealt with the error
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.\n")

print("Chapter 10:")
print("Exercise 12 - Failing Silently\n")
        
file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    count_words(file_name)
