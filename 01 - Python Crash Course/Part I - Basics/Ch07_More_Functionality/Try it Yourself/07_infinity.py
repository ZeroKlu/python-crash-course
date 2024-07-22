# Assignment 7.7
# Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window
#           displaying the output.)

print("Try-it-Yourself:")
print("Assignment 7.7")

print("See code file for infinite loop...")
# Uncomment the below to run an infinite loop
# num = 1
# while num <= 10:
#     print(num)
#
# The fix for this loop is to remember to increment the number
num = 1
while num <= 10:
    print(num)
    # This line ensure's the loop will end
    num += 1
