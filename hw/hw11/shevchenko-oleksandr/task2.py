WEEKDAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def weekday_for_number(number):
    if number not in WEEKDAYS:
        raise ValueError("Enter a number from 1 to 7.")

    return WEEKDAYS[number]


def main():
    try:
        number = int(input("Enter a day number (1-7): "))
        weekday = weekday_for_number(number)
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print(weekday)


if __name__ == "__main__":
    main()
