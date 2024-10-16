"""Assignment 6.6"""

print("Chapter 6:")
print("Exercise 6 - Using 'get()'")

alien = {"color" : "green", "speed" : "slow"}

# This line would throw an error, because there is no key "points"
# print(alien["points"])

point_value = alien.get("points", "No point value assigned")
print(point_value)

point_value = alien.get("points")
print(point_value)
