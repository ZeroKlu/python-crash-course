from dataclasses import dataclass

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott", "McLean", 53, "Dallas")
print(emp.__dataclass_fields__)
