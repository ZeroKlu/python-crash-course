print("Chapter 6:")
print("Exercise 11 - Sorting Dictionary Keys")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# Like any list, you can sort the keys to get the results in order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
