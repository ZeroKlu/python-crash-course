print("Chapter 6:")
print("Exercise 5 - Using Dictionaries to Group Similar Objects")

# Where the previous examples showed multiple properties of one object,
#   a dictionary can also store one property across multiple objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    # Though bad practice in some languages, Python recommends a trailing comma for easy adding of lines
    "phil": "python",
}

language = favorite_languages["phil"].title()
print(f"Phil's favorite language is {language}.")
