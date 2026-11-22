class Employee:
    """Employee with name and salary."""

    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print(f"Total number of employees: {cls.count}")


# TEST:
if __name__ == "__main__":
    emp1 = Employee("Olena", 3000)
    emp2 = Employee("Andriy", 3500)

    emp1.display_employee()
    emp2.display_employee()
    Employee.display_count()

    print("\n--- Class Metadata ---")
    print("Base classes (__base__):", Employee.__base__)
    print("Class namespace (__dict__):", Employee.__dict__)
    print("Class name (__name__):", Employee.__name__)
    print("Module name (__module__):", Employee.__module__)
    print("Documentation (__doc__):", Employee.__doc__)