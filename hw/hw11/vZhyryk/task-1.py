class NegativeValueError(Exception):
    def __init__(self, data):
        super().__init__(data)
        self.data = data

def check_odd_even(val):
    try:
        return handle_age(val)
    except ValueError:
        return "You entered not a number."
    except NegativeValueError as e:
        return e.data

def handle_age(val):
    age = int(val)
    if age < 0:
        raise NegativeValueError("Age cannot be lower than 0")
    if age % 2 == 0:
        return "Entered number is even"
    return "Entered number is odd"

print(check_odd_even(input("Enter your age: ")))