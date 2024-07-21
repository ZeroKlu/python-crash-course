print("Chapter 6:")
print("Exercise 13 - Enforcing Uniqueness when Looping Dictionary Values")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

# You could enforce uniqueness using a second list
mentioned = []
for language in favorite_languages.values():
    if language not in mentioned:
        mentioned.append(language)
print("\nThe following languages have been mentioned:")
for language in mentioned:
    print(language.title())

# But there is also a built-in mechanism set() for reporting only unique values
# By casting the list as a set, we eliminate duplicates
# Note: Sets do not maintain order, so the order these print may be different
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Note: You can create a set explicitly
languages = {"python", "ruby", "python", "c"}
print(languages)
