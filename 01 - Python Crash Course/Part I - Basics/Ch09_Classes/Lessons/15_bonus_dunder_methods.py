from sm_utils import clear_terminal, pause

print("Chapter 9:")
print("Exercise 15 (Bonus) - Dunder Methods and Properties")

# So far, we have worked with one "magic" method: __init__

# These "magic" (or "dunder" - short for double-underscore) methods are built into Python classes.
# You can get a list of them for a given class using the following code: dir(<<class_name>>)

# For example, here are the dunder methods for int...
clear_terminal()
print(dir(int))
pause()

# ... and for string...
clear_terminal()
print(dir(str))
pause()

# Any of these can be overridden in your custom classes

# Some to pay attention to include:

# Initialization and Construction
# __new__       Called when a class is instantiated
# __init__      Constructor: called by __new__ when a class is instantiated
# __del__       Destructor

# Numeric
# __trunc__(self):      Implements behavior for math.trunc()
# __ceil__(self):       Implements behavior for math.ceil()
# __floor__(self):      Implements behavior for math.floor()
# __round__(self, n):   Implements behavior for the built-in round()
# __invert__(self):     Implements behavior for inversion using the ~ operator.
# __abs__(self):        Implements behavior for the built-in abs()
# __neg__(self):        Implements behavior for negation
# __pos__(self):        Implements behavior for unary positive 

# Arithmetic
# __add__(self, other):         Implements behavior for math.trunc()
# __sub__(self, other):         Implements behavior for math.ceil()
# __mul__(self, other):         Implements behavior for math.floor()
# __floordiv__(self, other):    Implements behavior for the built-in round()
# __div__(self, other):         Implements behavior for inversion using the ~ operator.
# __truediv__(self, other):     Implements behavior for the built-in abs()
# __mod__(self, other):         Implements behavior for negation
# __divmod__(self, other):      Implements behavior for unary positive 
# __pow__:                      Implements behavior for exponents using the ** operator.
# __lshift__(self, other):      Implements left bitwise shift using the << operator.
# __rshift__(self, other):      Implements right bitwise shift using the >> operator.
# __and__(self, other):         Implements bitwise and using the & operator.
# __or__(self, other):          Implements bitwise or using the | operator.
# __xor__(self, other):         Implements bitwise xor using the ^ operator.

# String Methods
# __str__(self):                Defines behavior for when str() is called on an instance of your class.
# __repr__(self):               Called by built-int repr() method to return a machine readable representation of a type.
# __unicode__(self):            This method to return an unicode string of a type.
# __format__(self, formatstr):  Return a new style of string.
# __hash__(self):               Return an integer, used for quick key comparison in dictionaries.
# __nonzero__(self):            Defines behavior for when bool() is called on an instance of your class. 
# __dir__(self):                This method to return a list of attributes of a class.
# __sizeof__(self):             It return the size of the object.

# Comparisons
# __eq__(self, other):  Defines behavior for the equality operator, ==.
# __ne__(self, other):  Defines behavior for the inequality operator, !=.
# __lt__(self, other):  Defines behavior for the less-than operator, <.
# __gt__(self, other):  Defines behavior for the greater-than operator, >.
# __le__(self, other):  Defines behavior for the less-than-or-equal-to operator, <=.
# __ge__(self, other):  Defines behavior for the greater-than-or-equal-to operator, >=.

# Here's an example of using a dunder override in a class
class Person(object):
    """Class to define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self) -> str:
        """Return a string representation of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"

clear_terminal()
someone = Person("john", "doe")
print(someone)
pause()

# There are also dunder properties that aren't methods
# For example, __doc__ returns the doc string for a method or class
clear_terminal()
print(Person.__doc__)
pause()

# One in particular to be aware of is __dict__, which returns a dictionary of the object members
clear_terminal()
print(someone.__dict__)

# Here are some of the dunder properties

# Classes
# __name__:         Stores class name
# __dict__:         Stores class attributes (see where attributes are stored)
# __module__:       Stores the name of the module they were defined in within
# __bases__:        Stores class base classes (see inheritance)
# __mro__:          Stores class method resolution order

# Functions
# __name__:         Function name
# __dict__:         Function attributes
# __module__:       Name of the module they were defined in within
# __defaults__:     Default argument values for positional args
# __kwdefaults__:   Default argument values for keyword args

# Modules
# __name__:         Module name
# __dict__:         Module attributes
# __file__:         File this module was loaded from (though some modules are missing this)

# All Objects
# __class__:        Class of the object attribute
# __dict__:         Object attributes
