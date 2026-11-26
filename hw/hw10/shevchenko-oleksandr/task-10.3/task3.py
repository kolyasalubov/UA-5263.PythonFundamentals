class Employee:
    """Stores an employee's name and salary and tracks the employee count."""

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.total_employees}")

    def display_info(self):
        print(f"Name: {self.name}; salary: {self.salary:g}")


def display_class_info():
    print(f"Base class: {Employee.__base__}")
    print(f"Class namespace: {Employee.__dict__}")
    print(f"Class name: {Employee.__name__}")
    print(f"Module name: {Employee.__module__}")
    print(f"Documentation: {Employee.__doc__}")


def main():
    employees = [
        Employee("John", 2500),
        Employee("Jane", 3200),
    ]

    Employee.display_total_employees()
    for employee in employees:
        employee.display_info()

    display_class_info()


if __name__ == "__main__":
    main()
