print("Chapter 6:")
print("Exercise 8 - Looping Dictionary Items by Name")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# Taking advantage of multiple assignment (unpacking), you can iterate over the keys and values simultaneously
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite language is {value.title()}.")

print()

# Note: You can use meaningful variable names instead of "key" and "value"
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
