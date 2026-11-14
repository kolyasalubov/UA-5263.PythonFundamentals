"""Solutions for the 12 additional practical tasks."""

from math import hypot


def greet(name: str) -> str:
    """Return Jenny's special greeting for Johnny or a regular greeting."""
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the distance between two points, rounded to 2 decimal places."""
    return round(hypot(x2 - x1, y2 - y1), 2)


def filter_words(text: str) -> str:
    """Collapse whitespace and capitalize the first character of the text."""
    return " ".join(text.split()).capitalize()


def number_to_string(number: int | float) -> str:
    """Return the string representation of a number."""
    return str(number)


def reverse(text: str) -> str:
    """Return the words in reverse order, separated by single spaces."""
    return " ".join(text.split()[::-1])


def reverse_list(items: list) -> list:
    """Return a new list containing the items in reverse order."""
    return items[::-1]


def solution(number: int) -> int:
    """Return the sum of positive multiples of 3 or 5 below ``number``."""
    return sum(
        value
        for value in range(max(0, number))
        if value % 3 == 0 or value % 5 == 0
    )


def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    """Return True if the remaining fuel can cover the distance to the pump."""
    return mpg * fuel_left >= distance_to_pump


def are_you_playing_banjo(name: str) -> str:
    """Return the banjo message based on whether the name starts with R/r."""
    if name[:1].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


def bool_to_word(value: bool) -> str:
    """Return ``Yes`` for True and ``No`` for False."""
    return "Yes" if value else "No"


def count_sheeps(sheep: list[bool | None]) -> int:
    """Return the number of True values in the list."""
    return sheep.count(True)


def correct_tail(body: str, tail: str) -> bool:
    """Return True when ``body`` ends with ``tail``."""
    return body.endswith(tail)
