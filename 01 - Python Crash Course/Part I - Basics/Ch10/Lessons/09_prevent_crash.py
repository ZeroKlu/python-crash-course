# Handling exceptions can be used to prevent a crash
# i.e.: After handling an exception, the program can continue to execute

# Perform Lesson Tasks
print("Chapter 10:")
print("Exercise 9 - Using Error Handling to Prevent a Crash\n")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:\n> ")
    if first_number == 'q':
        break
    second_number = input("Second number:\n> ")
    if second_number == 'q':
        break

    # Here, we are using a 'try' to allow the loop to continue after a ZeroDivisionError
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
