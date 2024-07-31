# Assignment 11.3
# Employee: Write a class called Employee. The __init__() method should take in a first name, a last name,
#           and an annual salary, and store each of these as attributes. Write a method called give_raise()
#           that adds $ 5,000 to the annual salary by default but also accepts a different raise amount.
#
#           Write a test case for Employee. Write two test methods, test_give_default_raise() and
#           test_give_custom_raise(). Use the setUp() method so you don’t have to create a new employee
#           instance in each test method. Run your test case, and make sure both tests pass.

import unittest

class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def show_details(self):
        print(f"{self.first_name} {self.last_name} - Salary : ${self.annual_salary}".title())

    def give_raise(self, amount = 5000):
        self.annual_salary += amount

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("joe", "coder", 50_000)

    def test_raise_default(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55_000)

    def test_raise_default(self):
        self.employee.give_raise(10_000)
        # Note: This test uses the value from setUp and does not include the increment from the previous unit test
        self.assertEqual(self.employee.annual_salary, 60_000)

def main():
    print("Try-it-Yourself:n\Assignment 11.3\n")
    unittest.main()

if __name__ == "__main__":
    main()