print("Chapter 8:")
print("Exercise 10 - Passing an Arbitrary Amount of Keyword Arguments")

# For an arbitrary number of keyword arguments, the parameter name is preceded by a double-asterisk
# This will be received as a dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # Since **user_info is a dictionary, we can just add keys for our positional arguments
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location = "princeton", field = "physics")
print(user_profile)
