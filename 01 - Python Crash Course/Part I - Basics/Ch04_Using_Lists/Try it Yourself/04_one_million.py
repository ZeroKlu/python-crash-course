"""Assignment 4.4"""

# One Million: Make a list of the numbers from one to one million,
#              and then use a for loop to print the numbers.
#              (If the output is taking too long, stop it by pressing
#               CTRL-C or by closing the output window.)

print("Try-it-Yourself:")
print("Assignment 4.4")

million = list(range(1, 1_000_001))

# I'm cheating, since we don't cover slices until later in the chapter
for num in million[:5] + million[-5:]:
    print(num)

# Uncomment this block to see all the numbers print
# for num in million:
#     print(num)
