# There are two types of programmers in the world: those who write buggy code and liars.
# Python provides the unittest module for building and executing tests of the code

import unittest

# Here is the function we'll be testing
def get_formatted_name(first, last, middle = ""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# To see a broken test case, we'll also test this one
def get_formatted_name_broken(first, last, middle):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def main():
    print("Chapter 11:\nExercise 1 - Testing a Function\n")
    unittest.main()

# Here, we create a class to test the function in 'name_function.py'
# This includes two "unit tests," each of which tests a single aspect of a function's behavior
# Combining several unit tests produces a "test case," which comprehensively tests the function
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        # This unit test calls the name function without a middle name
        formatted_name = get_formatted_name("janis", "joplin")
        # Uncomment the next line to see a failed test
        formatted_name = get_formatted_name_broken("janis", "joplin")
        # The "assert" method provides an expected value for comparison (if the function works)
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        # This unit test calls the name function with a middle name
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        # Uncommenting the next line will not fail testing, since a middle name is provided
        formatted_name = get_formatted_name_broken("wolfgang", "amadeus", "mozart")
        # The "assert" method provides an expected value for comparison (if the function works)
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

if __name__ == "__main__":
    main()
