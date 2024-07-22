print("Chapter 7:")
print("Exercise 9 - Removing List Items")

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    # Since the remove() function only removes the first occurrence, a loop lets us remove all occurrences
    pets.remove("cat")
    print(len(pets))
    
print(pets)
