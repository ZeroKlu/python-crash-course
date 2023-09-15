print("Chapter 3:")
print("Exercise 5 - Inserting an Item in a List")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

# You can insert an item at a specific location by specifying the index of the item you're adding
# The rest of the list will renumber accordingly
motorcycles.insert(3, "ducati")
print(f"{len(motorcycles)} elements")
print(motorcycles[4])
print(motorcycles)
