import math


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)


def filter_words(st):
    return " ".join(st.split()).capitalize()


def number_to_string(num: int) -> str:
    return str(num)


def reverse(st: str) -> str:
    return " ".join(st.split()[::-1])


def filter_list(l):
    return [x for x in l if isinstance(x, int)]


def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / mpg <= fuel_left


def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    return name + " does not play banjo"


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count


def correct_tail(body, tail):
    return body[-1] == tail