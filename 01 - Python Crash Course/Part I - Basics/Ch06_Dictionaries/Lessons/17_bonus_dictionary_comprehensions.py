# Like lists, you can use comprehensions to populate dictionaries

# We have a scenario where we want to combine two lists into a dictionary
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]

# We could do this with a loop
dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]
print(dictionary)

# But this loop (just like with lists), could be simplified with a comprehension
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)

# Recall that we can produce a list of tuples with the zip() function
# We can use a dictionary comprehension on the result of the zip
dictionary = {key: value for (key, value) in zip(keys, values)}
print(dictionary)

# And of course, we can filter the results with conditions
odd_dictionary = {key: value for (key, value) in zip(keys, values) if value % 2 == 1}
print(odd_dictionary)
