def age_parity(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return "even" if age % 2 == 0 else "odd"


def main():
    try:
        age = int(input("Enter your age: "))
        parity = age_parity(age)
    except ValueError as error:
        print(f"Invalid age: {error}")
    else:
        print(f"Your age is {parity}.")


if __name__ == "__main__":
    main()
