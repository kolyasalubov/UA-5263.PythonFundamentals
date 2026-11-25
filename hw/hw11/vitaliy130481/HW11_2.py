def get_day_of_week(number):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            raise ValueError("Number must be between 1 and 7.")

if __name__ == "__main__":
    try:
        day_number = int(input("Enter a number (1-7): "))
        print(get_day_of_week(day_number))
    except ValueError as e:
        print(f"Invalid input: {e}")