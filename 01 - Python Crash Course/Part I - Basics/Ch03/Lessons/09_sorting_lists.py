print("Chapter 3:")
print("Exercise 9 - Sorting Lists")

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

# You can sort the list itself (which is permanent)
cars.sort()
print(cars)

# You can also sort in reverse order
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
# You can sort your results in the moment without actually modifying the list
print(sorted(cars))
print(cars)

# You can reverse the order of the unsorted list
cars.reverse()
print(cars)

# You can get the length of a list using the len() function
print(f"There are {len(cars)} items in the cars list.")
