print("Chapter 8:")
print("Exercise 3 - Positional Versus Keyword Arguments")

def describe_pet(animal_type, pet_name):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional arguments are passed in the same order they appear in the function signature
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# Passing arguments in the wrong order will result in unexpected behavior
describe_pet("harry", "hamster")

# For keyword arguments, you can overlook the order by indicating in the call which argument is which
# The names must exactly match the parameter names in the function definition
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

# By default, all arguments are required. Omitting one (like the below) will result in an error
# describe_pet("augie")

# You should not assume that you can store the output of a function
message1, message2 = describe_pet("cat", "reginald"), describe_pet("fish", "bubbles")
# We'll discuss return values a couple of lessons later. For now, note that this returns 'None None'.
print("\n", message1, message2)
