def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

def distance(x1, y1, x2, y2):
    import math
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)

def filter_words(st):
    clean_text = " ".join(st.split())
    return clean_text.capitalize()

def number_to_string(num : int) -> str:
    return str(num) # Return a string of the number here!

def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

def reverse_list(l):
    return l[::-1]

def solution(number):
    if int(number) <= 0:
        return 0
    sum_number = 0
    number_step = 1
    while number_step < number: 
        if number_step % 3 == 0 or number_step % 5 == 0:
            sum_number = sum_number + number_step  
        number_step = number_step + 1
    return sum_number

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return (name + " does not play banjo")

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

def count_sheeps(sheep):
  return sheep.count(True)

def correct_tail(body, tail):
     return body[-1] == tail