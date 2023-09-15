import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "programming.txt")

print("Chapter 10:")
print("Exercise 6 - Write a File\n")

# When we open a file, we can specify the file open mode with the following values:
#  - 'r'     read           (open the file as read-only) * This is the default mode if the argument is omitted
#  - 'w'     write          (open the file as write-only - any existing data will be replaced)
#  - 'a'     append         (open the file and write to the end - any existing data will be retained)
#  - 'r+'    read/write     (open the file to both read and write)
with open(file_path, "w") as file_object:
    # Python does not contain a write_line method, so you must include your own new-line characters
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games!\n")
    # Note: Only strings can be written to file, so numerical data must be converted first

# Let's verify that we wrote the file
with open(file_path, "r") as file_object:
    print(file_object.read())

# A workaround for appending new-line characters would be to create a function
def write_line(file_object, text):
    file_object.write(f"{text}\n")
    
with open(file_path, "w") as file_object:
    # Python does not contain a write_line method, so you must include your own new-line characters
    write_line(file_object, "I love coding!")
    write_line(file_object, "I love creating new applications!")

# Let's verify that we wrote the file again
with open(file_path, "r") as file_object:
    print(file_object.read())
