print("Chapter 8:")
print("Exercise 4 - Default Values")

# You can set default values
# Note: After a default value for one parameter, all later parameters in the function must have default values
def describe_pet_def(pet_name, animal_type="dog"):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# You can omit any arguments with default values
describe_pet_def("willie")
describe_pet_def(pet_name = "willie")

# If you pass a value it will override the default
describe_pet_def("harry", "hamster")
describe_pet_def(pet_name="harry", animal_type="hamster")
