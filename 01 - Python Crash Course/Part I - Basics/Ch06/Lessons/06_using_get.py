print("Chapter 6:")
print("Exercise 6 - Using 'get()'")

alien_0 = {"color" : "green", "speed" : "slow"}

# This line would throw an error, because there is no key "points"
# print(alien_0["points"])

# The "get" method provides a default value in lieu of an error
point_value = alien_0.get("points", "No point value assigned")
print(point_value)

# You can omit the default value, in which case, Python will return "None"
point_value = alien_0.get("points")
print(point_value)
