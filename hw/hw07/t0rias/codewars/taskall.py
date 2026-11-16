# I. Jenny's secret message
def greet(name: str) -> str:
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# II. Find The Distance Between Two Points
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    horizontal_gap = x2 - x1
    vertical_gap = y2 - y1
    return round((horizontal_gap ** 2 + vertical_gap ** 2) ** 0.5, 2)

#III. No yelling!
def filter_words(st: str) -> str:
    lowercase_words = [word.lower() for word in st.split()]
    sentence = " ".join(lowercase_words)
    return sentence[:1].upper() + sentence[1:]

#IV. Convert a Number to a String
def number_to_string(num: int) -> str:
    return f"{num}"

#V. Reversing Words in a String
def reverse(st: str) -> str:
    def reverse_words(words: list[str]) -> list[str]:
        if len(words) <= 1:
            return words
        return reverse_words(words[1:]) + [words[0]]
    return " ".join(reverse_words(st.split()))

#VI. Reverse List Order
def reverse_list(l):
  return l[::-1]

#VII. Multiples of 3 or 5
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

#VIII. Will you make it?
def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name: str) -> str:
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean: bool) -> str:
    if boolean:
        return "Yes"
    return "No"

#XI. Counting sheep
def count_sheeps(sheep: list) -> int:
    return sheep.count(True)

#XII. Is this my tail?
def correct_tail(body: str, tail: str) -> bool:
    last_letter = body[-1]
    return last_letter == tail