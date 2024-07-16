print("Chapter 4:")
print("Exercise 6 - Slicing Lists")

players = ["charles", "martina", "michael", "florence", "eli"]

# You can access a portion (slice) of a list all at the same time
print(players[0:3])
print(players[1:4])

# If you omit an argument, the slice goes all the way to the omitted end of the list
print(players[:4])
print(players[2:])
print(players[-3:])

# You can loop across a slice (since even a subset of a list is a list)
print("Here are the first 3 players on my team")
for player in players[:3]: print(player)

# You can specify the increment with a third argument
# Here, I'll print every other player
print(players[::2])

# Using a negative increment, you can slice in reverse order from the end
print(players[::-2])

# BONUS
# Even though a string is not technically a list, we can use slicing on a string
# This gives us a really elegant way to reverse a string using the -1 increment
name = "Scott"
print(name[::-1])
