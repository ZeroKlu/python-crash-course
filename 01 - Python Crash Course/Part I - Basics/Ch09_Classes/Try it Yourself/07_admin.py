"""Assignment 9.7"""

# Admin: An administrator is a special kind of user. Write a class
#        called `Admin` that inherits from the `User` class you wrote
#        in Exercise 9.3 or Exercise 9.5. Add an attribute, `privileges`,
#        that stores a list of strings like "can add post", "can delete
#        post", "can ban user", and so on. Write a method called
#        `show_privileges()` that lists the administrator's set of
#        privileges. Create an instance of `Admin`, and call your method.

print("Try-it-Yourself:")
print("Assignment 9.7")

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

class Admin(User):
    """Define an Admin as a subclass of User"""

    def __init__(self, first_name, last_name, privileges=None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        if privileges is None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the user's privileges"""
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

my_admin = Admin("jane", "smith")
my_admin.describe()
my_admin.show_privileges()

my_admin = Admin("bob", "jones", ["create", "delete"])
my_admin.describe()
my_admin.show_privileges()
