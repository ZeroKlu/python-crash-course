# Assignment 6.8
# Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary,
#       include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
#       Next, loop through your list and as you do, print everything you know about each pet.

print("Try-it-Yourself:")
print("Assignment 6.8")

charlie = {
    "animal": "dog",
    "owner": "talia",
}

orville = {
    "animal": "guinea pig",
    "owner": "scott",
}

bronte = {
    "animal": "cat",
    "owner": "melissa",
}

pets = [charlie, orville, bronte]
for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
