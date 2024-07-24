from sm_utils import clear_terminal, pause

print("Chapter 9:")
print("Exercise 14 (Bonus) - Properties")

# In a class, a property is just like an attribute, except the property is a function, 
#  while the attributes are just public variables

class Person(object):
    """Class to define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        # first_name and last_name are attributes of the class
        self.first_name = first_name
        self.last_name = last_name
    
    # Full-Name is a property of the class, which wi indicate using the @property decorator
    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"

clear_terminal()
someone = Person("john", "doe")
print(someone.first_name)
print(someone.last_name)
print(someone.full_name) # You access a property the same way as an attribute
pause()

# You can also use name mangling to conceal your attributes and expose them using properties
# This is called encapsulation

class Human(object):
    """Class to define a human"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the human class"""
        # first_name and last_name are attributes of the class
        self.__first_name = first_name
        self.__last_name = last_name
    
    @property
    def first_name(self):
        """Return the first name of the person"""
        return self.__first_name.title()
    
    @property
    def last_name(self):
        """Return the last name of the person"""
        return self.__last_name.title()

    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"

clear_terminal()
someone_else = Human("john", "doe")
print(someone_else.first_name)
print(someone_else.last_name)
print(someone_else.full_name)
