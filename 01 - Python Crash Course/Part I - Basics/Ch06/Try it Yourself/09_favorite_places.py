# Assignment 6.9
# Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the
#                  dictionary, and store one to three favorite places for each person. To make this exercise
#                  a bit more interesting, ask some friends to name a few of their favorite places. Loop through
#                  the dictionary, and print each person’s name and their favorite places.

print("Try-it-Yourself:")
print("Assignment 6.9")

favorite_places = {
    "scott": ["ireland", "spain", "mexico"],
    "matt": ["puerto rico"],
    "pat": ["minnesota", "scotland"],
}

for name in favorite_places.keys():
    print(f"\n{name.title()}'s favorite places include:")
    for place in favorite_places[name]:
        print(f"\t{place.title()}")
