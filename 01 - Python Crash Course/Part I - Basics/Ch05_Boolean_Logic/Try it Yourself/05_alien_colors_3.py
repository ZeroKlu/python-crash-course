# Assignment 5.5
# Alien Colors # 3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#                   • If the alien is green, print a message that the player earned 5 points.
#                   • If the alien is yellow, print a message that the player earned 10 points.
#                   • If the alien is red, print a message that the player earned 15 points.
#                   • Write three versions of this program, making sure each message is printed for the
#                     appropriate color alien.

print("Try-it-Yourself:")
print("Assignment 5.5")

alien_colors = ["green", "yellow", "red"]
for alien_color in alien_colors:
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        points = 0
    print(f"You earned {points} points!")
