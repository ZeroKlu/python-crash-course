print("Chapter 6:")
print("Exercise 9 - Looping Dictionary Keys")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# if you only need to get the keys, there is a property for that as well
for name in favorite_languages.keys():
    print(name.title())

print()

# The keys are the default return as well, so this accomplishes the same thing
for name in favorite_languages:
    print(name.title())
