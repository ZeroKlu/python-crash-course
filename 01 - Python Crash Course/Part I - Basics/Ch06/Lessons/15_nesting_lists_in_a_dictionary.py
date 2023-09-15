print("Chapter 6:")
print("Exercise 15 - Nesting Lists in a Dictionary")

# When it makes sense as part of an object's description, consider using a list as a value
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

# This can be especially useful with multiple objects
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "Haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
