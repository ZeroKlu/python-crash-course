print("Chapter 3:")
print("Exercise 7 - Popping an Item from a List")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

# You can remove the last item from the list and capture its value to use immediately
popped_motorcycle = motorcycles.pop()
print(f"I popped '{popped_motorcycle}'...")
print(f"{len(motorcycles)} elements")
print(motorcycles)

# You can specify what location to pop
popped_motorcycle = motorcycles.pop(1)
print(f"I popped '{popped_motorcycle}'...")
print(f"{len(motorcycles)} elements")
print(motorcycles)
