"""
Task01
Write a program that prompts the user to enter their age, and then displays a
message stating whether the age is even or odd. The program must provide the ability
to enter a negative number, and in this case generate an exception. The master code
should call a function that processes the information entered.
"""
class NegativeValueError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

def input_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise NegativeValueError("Age should be positive.")
        except ValueError:
            print("Entered not an integer value.")
        except NegativeValueError as e:
            print(e)
        else:
            break

    return age

def check_parity(number):
    return "even" if number % 2 == 0 else "odd"

def main():
    age = input_age()
    pariry = check_parity(age)

    print(f"Your age is {age}. It is {pariry}.")


if __name__ == "__main__":
    main()
