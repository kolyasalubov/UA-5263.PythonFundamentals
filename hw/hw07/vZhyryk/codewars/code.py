# # ------------Task 1-------------

def greet(name : str) -> str:
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# # ------------Task 2-------------

import math
def distance(x1 : int, y1 : int, x2 : int, y2 : int) -> float:
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)

# ------------Task 3-------------

def filter_words(st: str) -> str:
    return " ".join(st.split()).capitalize()

# ------------Task 4-------------

def number_to_string(num : int) -> str:
    return f"{num}"

# ------------Task 5-------------

def reverse(st : str) -> str:
    val = st.split()
    val.reverse()
    return " ".join(val)

# ------------Task 6-------------

def reverse_list(l : list[int]) -> list[int]:
    l.reverse()
    return l

# ------------Task 7-------------

def solution(number : int) -> int:
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# ------------Task 8-------------

def zero_fuel(distance_to_pump : int, mpg : int, fuel_left : int) -> bool:
    return distance_to_pump <= mpg * fuel_left

# ------------Task 9-------------

def are_you_playing_banjo(name : str) -> str:
    return f"{name} plays banjo" if name.lower()[0] == 'r' else f"{name} does not play banjo"

# ------------Task 10------------

def bool_to_word(boolean : bool) -> str:
    return "Yes" if boolean else "No"

# ------------Task 11------------

def count_sheeps(sheep : list[bool]):
    return sheep.count(True)

# ------------Task 12------------

def correct_tail(body, tail):
     return body[-1] == tail