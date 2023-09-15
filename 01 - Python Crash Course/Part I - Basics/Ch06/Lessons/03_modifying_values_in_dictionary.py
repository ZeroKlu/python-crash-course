print("Chapter 6:")
print("Exercise 3 - Modifying Values in a Dictionary")

alien_0 = {"color" : "green", "points" : 5}
print(f"The alien is {alien_0['color']}")

# changing a value is just like adding a new one, except you specify a key that already exists
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}")
    
# Here's the book example for a real-world (game) scenario
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal x-position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New x-position:      {alien_0['x_position']}")
