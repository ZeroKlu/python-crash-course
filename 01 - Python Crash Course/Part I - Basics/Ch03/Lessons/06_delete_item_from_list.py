print("Chapter 3:")
print("Exercise 6 - Deleting an Item from a List")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

# You can delete an item at a specified location
# The rest of the list will renumber accordingly
del motorcycles[2]
print(f"{len(motorcycles)} elements")
print(motorcycles[2])
print(motorcycles)
