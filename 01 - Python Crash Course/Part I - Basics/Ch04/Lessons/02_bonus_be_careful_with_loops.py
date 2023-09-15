print("Chapter 4:")
print("Exercise 2 - Be Careful with Loops")

# Beware!
# It's tempting to modify a list while iterating across it, but that will break things... for example:
numbers = [1, 2, 3, 4, 5]

input("Try to predict the results of the next loop. Press enter to continue after your prediction...")

for number in numbers:
    n = numbers.index(number)
    print(numbers.pop(n))
# You might be surprised that this only prints 1, 3, and 5
# That's because on the first iteration, we pop numbers[0], which re-indexes the entire list [2, 3, 4, 5]
# But the Python iterator doesn't know about the change (it was created when we started the loop)
# So it just moves on to numbers[1], which is now the 3. Then it pops numbers[1] leaving [2, 4, 5]
# Finally the third iteration moves to numbers[2], which is now the value 5
# No error is thrown, because the iterator halts upon reaching the end of the list
# We just get an unexpected result

# Moral: NEVER modify the collection you are looping over!
# Foreshadowing: We'll see a way to empty the list in a loop without problems in Lesson 07.04
