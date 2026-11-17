from math import hypot


def greet(name: str) -> str:
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return round(hypot(x2 - x1, y2 - y1), 2)


def filter_words(text: str) -> str:
    return " ".join(text.split()).capitalize()


def number_to_string(number: int | float) -> str:
    return str(number)


def reverse(text: str) -> str:
    return " ".join(text.split()[::-1])


def reverse_list(items: list) -> list:
    return items[::-1]


def solution(number: int) -> int:
    return sum(
        value
        for value in range(max(0, number))
        if value % 3 == 0 or value % 5 == 0
    )


def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    return mpg * fuel_left >= distance_to_pump


def are_you_playing_banjo(name: str) -> str:
    if name[:1].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


def bool_to_word(value: bool) -> str:
    return "Yes" if value else "No"


def count_sheeps(sheep: list[bool | None]) -> int:
    return sheep.count(True)


def correct_tail(body: str, tail: str) -> bool:
    return body.endswith(tail)
