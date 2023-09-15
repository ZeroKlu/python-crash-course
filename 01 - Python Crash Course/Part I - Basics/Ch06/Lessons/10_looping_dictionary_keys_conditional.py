print("Chapter 6:")
print("Exercise 10 - Looping Dictionary Keys for Conditional Handling")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# Getting a list of keys is useful when there is a condition to be met
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

print()

# The opposite direction of comparison is also viable
people = ["phil", "sarah", "erin", "jen", "edward"]
for person in people:
    if person not in favorite_languages.keys():
        print(f"{person.title()}, please take the languages poll.")
