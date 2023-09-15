# One of the most important aspects of programming is handling errors (exceptions)

# In Python, this is done using try-except blocks with syntax as follows:
#
# try:
#     # code that could throw an exception
#     # the program should 'try' to execute this
# except:
#     # code to run if an exception occurs during the 'try' block's execution
# else:
#     # code to run if exception does not occur
# finally:
#     # code to run at the end whether or not an exception occurs

# Perform Lesson Tasks
print("Chapter 10:")
print("Exercise 8 - Handling a ZeroDivisionError\n")

try:
    # This line will throw an error
    print(5/0)
except ZeroDivisionError:
    # This code executes when a 'ZeroDivisionError' is thrown in the try block
    print("You can't divide by zero!")
