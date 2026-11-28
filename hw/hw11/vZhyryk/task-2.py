DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class InvalidWeekDayError(Exception):
    def __init__(self, data):
        super().__init__(data)
        self.data = data


def match_number_week_days(num):
    try:
        return handle_week_day(num)
    except ValueError:
        return "Value is not a number"
    except InvalidWeekDayError as e:
        return e.data


def handle_week_day(num):
    number = int(num)
    if number > 7 or number < 1:
        raise InvalidWeekDayError("Invalid week day")
    return DAYS[number - 1]


print(match_number_week_days(input("Enter week day as a number: ")))
