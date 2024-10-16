"""Assignment 6.6"""

# Polling: Use the code in favorite_languages.py
#     • Make a list of people who should take the favorite languages poll.
#       Include some names that are already in the dictionary and some that
#       are not.
#     • Loop through the list of people who should take the poll. If they
#       have already taken the poll, print a message thanking them for
#       responding. If they have not yet taken the poll, print a
#       message inviting them to take the poll.

print("Try-it-Yourself:")
print("Assignment 6.6")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people = ["jen", "sarah", "adam", "edward", "eleanor", "phil"]
for name in people:
    # if name in favorite_languages.keys():
    if name in favorite_languages:
        print(f"Hi {name.title()}! Thanks for taking the poll.")
    else:
        print(f"Hi {name.title()}, please take the poll.")
