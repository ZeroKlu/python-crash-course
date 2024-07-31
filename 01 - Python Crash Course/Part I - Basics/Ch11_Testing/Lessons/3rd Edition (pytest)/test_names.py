# There are two types of programmers in the world: those who write buggy code and liars.
# Python provides the pytest library for building and executing tests of the code

# Make sure to navigate to this folder in the terminal before running the pytest command
# Note: The filename must start with 'test_' to be picked up by pytest

from name_function import get_formatted_name, get_formatted_name_broken

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"

# Uncomment the test below to see a failed test
# def test_first_last_name_on_broken_function():
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name_broken("janis", "joplin")
#     assert formatted_name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"

def test_first_last_middle_name_on_broken_function():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name_broken("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"

# To perform testing:
#
# 1. Navigate to the folder where this script is in your terminal
# 2. Run the following command in the terminal
#    pytest
# 3. Verify your results
#    - Green dots '.' following the filename indicate passed tests
#    - Failed tests are indicated by a red 'F' and are followed by an error description


