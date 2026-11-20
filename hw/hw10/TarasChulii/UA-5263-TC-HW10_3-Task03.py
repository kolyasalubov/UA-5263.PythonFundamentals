class Employee():

    """Class representing an employee with name and salary."""

    total_employees = 0
    MIN_SALARY = int(1000)

    def __init__(self, name, salary):
        self.name = name.capitalize()
        self.salary = salary
        type(self).total_employees += 1

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.MIN_SALARY:
            raise ValueError(f"Invalid salary value for {self.name}. Minimal salary is {Employee.MIN_SALARY}")
        self.__salary = salary

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    def get_employee_info(self):
        return f"{self.name} has salary : {self.salary}"


def self_test():

    employees = []

    for name, salary in [("John", 2000),
                         ("Jane", 3000),
                         ("test_incorrect_salary", 900) ]:
    
        try:
            employees.append(Employee(name, salary))
        except (ValueError) as error: 
            print(f"Error: {error}")

    print(f"\nTotal employees count is: {Employee.get_total_employees()}")

    for employee in employees:
        print(employee.get_employee_info())

    print("\nClass information:")
    print(f"Base class: {Employee.__base__}")
    print(f"Class name: {Employee.__name__}")
    print(f"Module name: {Employee.__module__}")
    print(f"Documentation: {Employee.__doc__}")
    print(f"Class namespace: {Employee.__dict__}")



if __name__ == "__main__":
    self_test()