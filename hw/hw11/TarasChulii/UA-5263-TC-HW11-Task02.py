"""
Task02
Write a program that analyzes the entered number and, depending on the number, gives
the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.
"""

DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

while True:
    try:
        number = int(input("Enter day number (1-7): "))
        if number not in DAYS:
            raise ValueError("Day number must be between 1 and 7.")
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print(DAYS[number])
        break