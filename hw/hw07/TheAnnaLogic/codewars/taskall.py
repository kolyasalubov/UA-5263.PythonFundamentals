# Task 1: Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# Task 2: Find Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# Task 3: No yelling!
def filter_words(st):
    words = st.split()
    result = " ".join(words)
    return result.capitalize()


# Task 4: Convert a Number to a String!
def number_to_string(num: int) -> str:
    result = str(num)
    return result


# Task 5: Reversing Words in a String
def reverse(st):
    words = st.split()
    words = words[::-1]
    result = " ".join(words)
    return result


# Task 6: Reverse List Order
def reverse_list(l):
    result = l[::-1]
    return result


# Task 7: Multiples of 3 or 5
def solution(number):
    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Task 8: Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    if max_distance >= distance_to_pump:
        return True
    else:
        return False


# Task 9: Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# Task 10: Convert boolean values to strings 'Yes' or 'No'   
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


# Task 11: Counting sheep
def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item:
            count += 1
    return count


# Task 12: Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
    