# Assignment 11-3
# Employee: Write a class called Employee. The __init__() method should take in a first name, a last name,
#           and an annual salary, and store each of these as attributes. Write a method called give_raise()
#           that adds $5,000 to the annual salary by default but also accepts a different raise amount.
# 
#           Write a test file for Employee with two test functions, test_give_default_raise() and
#           test_give_custom_raise(). Write your tests once without using a fixture, and make sure they both pass.
#           Then write a fixture so you don’t have to create a new employee instance in each test function.
#           Run the tests again, and make sure both tests still pass.

class Employee():
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def __str__(self):
        """Return a representation of the employee as a string."""
        print(f"{self.first_name} {self.last_name} - Salary : ${self.annual_salary}".title())

    def give_raise(self, amount=5000):
        """Increase the employee's salary"""
        self.annual_salary += amount
