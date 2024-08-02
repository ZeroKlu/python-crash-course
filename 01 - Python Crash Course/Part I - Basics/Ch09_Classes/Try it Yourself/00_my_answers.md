## Chapter 9 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 9 try-it-yourself exercises.

---

### Assignment 9.1 - Restaurant

Make a class called `Restaurant`. The `__init__()` method for `Restaurant` should store two attributes: a `restaurant_name` and a `cuisine_type`. Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open. Make an instance called `restaurant` from your class. Print the two attributes individually, and then call both methods.


Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant = Restaurant("the mad greek", "greek & indian food")
print(restaurant.name.title())
print(restaurant.cuisine.title())
restaurant.describe()
restaurant.open()
```

</details>
<br>

<details>
<summary>Output</summary>

```
The Mad Greek
Greek & Indian Food
The Mad Greek proudly serves Greek & Indian Food
The Mad Greek is open for business!
```

</details>

---

### Assignment 9.2 - Three Restaurants

Start with your class from Exercise 9.1. Create three different instances 
from the class, and call `describe_restaurant()` for each instance.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant_1 = Restaurant("The Mad Greek", "Greek & Indian food")
restaurant_2 = Restaurant("Charlie's Crab", "seafood")
restaurant_3 = Restaurant("The Brown Derby", "steak")

restaurant_1.describe()
restaurant_2.describe()
restaurant_3.describe()
```

</details>
<br>

<details>
<summary>Output</summary>

```
The Mad Greek proudly serves Greek & Indian Food!
Charlie'S Crab proudly serves Seafood!
The Brown Derby proudly serves Steak!
```

</details>

---

### Assignment 9.3 - Users

Make a class called `User`. Create two attributes called `first_name` and 
`last_name`, and then create several other attributes that are typically 
stored in a user profile. Make a method called `describe_user()` that prints 
a summary of the user's information. Make another method called
`greet_user()` that prints a personalized greeting to the user. Create 
several instances representing different users, and call both methods for 
each user.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class User:
    """Defines a user"""

    def __init__(self, first_name, last_name, location, profession):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.profession = profession

    def greet(self):
        """Greet the user"""
        print(
            f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(
            f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Location:   {self.location.title()}")
        print(f"Profession: {self.profession.title()}\n")


user_1 = User("scott", "mclean", location="dallas", profession="programmer")
user_1.greet()
user_1.describe()

user_2 = User("hillary", "taylor", location="twinsburg", profession="lawyer")
user_2.greet()
user_2.describe()

user_3 = User("jeremy", "mclean", location="columbus",
              profession="restaurant manager")
user_3.greet()
user_3.describe()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hello there, Scott Mclean
Name:       Scott Mclean
Location:   Dallas
Profession: Programmer

Hello there, Hillary Taylor
Name:       Hillary Taylor
Location:   Twinsburg
Profession: Lawyer

Hello there, Jeremy Mclean
Name:       Jeremy Mclean
Location:   Columbus
Profession: Restaurant Manager
```

</details>

---

### Assignment 9.4 - Number Served

Start with your program from Exercise 9.1. Add an attribute called 
`number_served` with a default value of 0. Create an instance called 
restaurant from this class. Print the number of customers the restaurant has 
served, and then change this value and print it again.

Add a method called `set_number_served()` that lets you set the number of 
customers that have been served. Call this method with a new number and print 
the value again.

Add a method called `increment_number_served()` that lets you increment the 
number of customers who've been served. Call this method with any number you 
like that could represent how many customers were served in, say, a day of 
business.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()} food!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")

    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")


restaurant = Restaurant("burger heaven", "american")
restaurant.describe()
restaurant.get_number_served()
restaurant.number_served = 10
restaurant.get_number_served()

restaurant.set_number_served(20)
restaurant.get_number_served()

restaurant.increment_number_served(5)
restaurant.get_number_served()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Burger Heaven proudly serves American food!
We have served 0 people today.

We have served 10 people today.

Set number served to 20
We have served 20 people today.

Incremented number served to 25
We have served 25 people today.
```

</details>

---

### Assignment 9.5 - Login Attempts

Add an attribute called `login_attempts` to your `User` class from Exercise 9.3. Write a method called `increment_login_attempts()` that increments the value of `login_attempts` by `1`. Write another method called `reset_login_attempts()` that resets the value of `login_attempts` to `0`.

Make an instance of the `User` class and call `increment_login_attempts()` several times. Print the value of `login_attempts` to make sure it was incremented properly, and then call `reset_login_attempts()`. Print `login_attempts` again to make sure it was reset to `0`.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class User:
    """Defines a user"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the number of login attempts"""
        print(f"Login Attempts: {self.login_attempts}")

user = User("john", "doe")
user.describe()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       John Doe
Username:   JDOE
Login Attempts: 0
Login Attempts: 1
Login Attempts: 2
Login Attempts: 0
```

</details>

---

### Assignment 9.6 - Ice Cream Stand

An ice cream stand is a specific kind of restaurant. Write a class called `IceCreamStand` that inherits from the `Restaurant` class you wrote in Exercise 9.1 or Exercise 9.4. Either version of the class will work; just pick the one you like better. Add an attribute called `flavors` that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of `IceCreamStand`, and call this method.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Restaurant Class</summary>

```python
class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")
        
    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")
```

</details>
<br>

<details>
<summary>IceCreamStand Class</summary>

```python
class IceCreamStand(Restaurant):
    """Defines an Ice Cream Stand as a subclass of Restaurant"""

    def __init__(self, name, cuisine, flavors=["chocolate", "vanilla", "strawberry"]):
        """Initialize a new instance of the IceCreamStand class"""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def list_flavors(self):
        """Print out a list of the available flavors"""
        print(f"\n{self.name.title()} has the following flavors available:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

    def add_flavor(self, flavor):
        """Add an item to the list of the available flavors"""
        if flavor not in self.flavors:
            self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """Remove an item from the list of the available flavors"""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_stand = IceCreamStand("Frosty Freeze", "ice cream", ["chocolate", "vanilla", "strawberry", "pistachio"])
my_stand.list_flavors()

my_stand.add_flavor("rocky road")
my_stand.list_flavors()

my_stand.remove_flavor("pistachio")
my_stand.list_flavors()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Pistachio

Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Pistachio
 - Rocky Road

Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Rocky Road
```

</details>

---

### Assignment 9.7 - Admin

An administrator is a special kind of user. Write a class called `Admin` that inherits from the `User` class you wrote in Exercise 9.3 or Exercise 9.5. Add an attribute, `privileges`, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called `show_privileges()` that lists the administrator's set of privileges. Create an instance of `Admin`, and call your method.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User Class</summary>

```python
class User:
    """Defines a User"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(
            f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(
            f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempts counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the login attempts counter"""
        print(f"Login Attempts: {self.login_attempts}\n")
```

</details>
<br>

<details>
<summary>Admin Class</summary>

```python
class Admin(User):
    """Define an Admin as a subclass of User"""

    def __init__(self, first_name, last_name, privileges=None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the user's privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_admin = Admin("jane", "smith")
my_admin.describe()
my_admin.show_privileges()

my_admin = Admin("bob", "jones", ["create", "delete"])
my_admin.describe()
my_admin.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Jane Smith
Username:   JSMITH

Privileges:
 - create
 - delete
 - modify
 - ban

Name:       Bob Jones
Username:   BJONES

Privileges:
 - create
 - delete
```

</details>

---

### Assignment 9.8 - Privileges

Write a separate `Privileges` class. The class should have one attribute, `privileges`, that stores a list of strings as described in Exercise 9.7. Move the `show_privileges()` method to this class.

Make a `Privileges` instance as an attribute in the `Admin` class. Create a new instance of `Admin` and use your method to show its privileges.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User Class</summary>

```python
class User:
    """Defines a User"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempts counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the login attempts counter"""
        print(f"Login Attempts: {self.login_attempts}\n")
```

</details>
<br>

<details>
<summary>Admin Class</summary>

```python
class Admin(User):
    """Define an Admin as a subclass of User"""

    def __init__(self, first_name, last_name, privileges = None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
```

</details>
<br>

<details>
<summary>Privileges Class</summary>

```python
class Privileges:
    """Defines a set of privileges"""

    def __init__(self, privileges = None):
        """Initialize a new instance of the Privileges class"""
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the user's privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_admin = Admin("jane", "smith")
my_admin.describe()
my_admin.privileges.show_privileges()

my_admin = Admin("bob", "jones", ["create", "delete"])
my_admin.describe()
my_admin.privileges.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Jane Smith
Username:   JSMITH

Privileges:
 - create
 - delete
 - modify
 - ban

Name:       Bob Jones
Username:   BJONES

Privileges:
 - create
 - delete
```

</details>

---

