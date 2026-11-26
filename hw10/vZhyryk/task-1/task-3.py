class Employee:
    """Employee with a name and a salary; counts all created employees."""
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_count(self):
        print(f"Total employees: {Employee.count}")

    def display_employee(self):
        print(f"{self.name} has salary: {self.salary}")


emp1 = Employee("Ada", 5000)
emp2 = Employee("Ivan", 4200)

emp1.display_employee()
emp2.display_employee()
emp1.display_count()

print("__base__:", Employee.__base__)
print("__dict__:", Employee.__dict__)
print("__name__:", Employee.__name__)
print("__module__:", Employee.__module__)
print("__doc__:", Employee.__doc__)