# ACCESSING RELATIVE PATHS

# There are two different types of file paths to be aware of
# Absolute Path: complete path to the target file, typically starting with a drive letter, UNC, or URL
# Relative Path: path to the target file relative to the location of the script calling it

# In visual studio, when you execute a Python script, the starting directory for a relative path is the
#   directory you have navigated to in your terminal instance.

# You can target a file properly by making sure that the terminal is in a location where it is available

# Alternately, you can come up with a method to obtain the location of the script and start from there


# Here is my method for accessing a file at a relative path
# -------------------- RELATIVE PATHS - METHOD 1 --------------------
# 1. Import the OS library
import os

# 2. Obtain the directory where the script is executing
ROOT_DIR = os.path.dirname(__file__)
print(f"Root directory is:          \"{ROOT_DIR}\"")

# 3. Create the path to the file to be opened
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")
print(f"File path (manual) is:      \"{file_path}\"")



# I have created a module (relative_paths.py) that handles steps 1-3 (above) for you, like the below example:
# -------------------- RELATIVE PATHS - METHOD 2 --------------------
# 1. Import the relative_paths module
from relative_paths import get_path

# 2. Get the file path
file_path = get_path("pi_digits.txt", "Files")
print(f"File path (from module) is: \"{file_path}\"\n")


# READING A FILE

# In the second edition of the textbook, the method for reading the file looks like this
# -------------------- READ FILE - 2nd EDITION METHOD --------------------
with open(file_path) as file:
    text = file.read()
    print(text.rstrip())


print("-----")


# In the 3rd edition, the book presents a new (simpler) methodology for the file interaction
# -------------------- READ FILE - 3nd EDITION METHOD --------------------
from pathlib import Path

file = Path(file_path)
contents = file.read_text()
print(contents.rstrip())


# Throughout the lessons, you'll find each lesson with files repeated twice, once with "2ed" in the filename for
#   the 2nd edition code sample and once with "3ed" in the filename for the 3rd edition code sample

# In the 2nd edition samples, I will manually handle relative paths using the os library
# In the 3rd edition samples, I will handle relative paths using the relative_paths.py module
