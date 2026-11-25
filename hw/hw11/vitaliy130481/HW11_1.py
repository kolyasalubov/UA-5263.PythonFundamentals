class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    return "Your age is odd." if age % 2 else "Your age is even."


if __name__ == "__main__":
    try:
        user_age = int(input("Enter your age: "))
        print(check_age(user_age))
    except NegativeAgeError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid integer.")