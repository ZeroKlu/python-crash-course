print("Chapter 6:")
print("Exercise 12 - Looping Dictionary Values")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

# Sometimes you want only the values (for example, when obtaining anonymous stats)
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# You might use a similar process for counting responses for statistical analysis
counts = {}
for language in favorite_languages.values():
    if language in counts.keys():
        counts[language] += 1
    else:
        counts[language] = 1

print("\nThe following languages have been mentioned:")
for lang in sorted(counts.keys()):
    # Note the use of the trinary logical operator here:        tru_val if condition else false_val
    print(f"{lang.title()}: {counts[lang]} time{('' if counts[lang] == 1 else 's')}")
