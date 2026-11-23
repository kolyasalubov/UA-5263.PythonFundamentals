#I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(pow((x2 - x1) ** 2 + (y2 - y1) ** 2 ,0.5) ,2)

#III. No yelling!
def filter_words(st):
    return " ".join(st.lower().capitalize().split())

#IV. Convert a Number to a String
def number_to_string(num : int) -> str:
    return str(num)

#V. Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])

#VI. Reverse List Order
def reverse_list(l):
    return l[::-1]

#VII. Multiples of 3 or 5
def solution(number):
    
    result = []
        
    for num in range(number):
        if num % 3 == 0:
            result.append(num)
        if num % 5 == 0:
            result.append(num)
    
    return sum(set(result))

#VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    return False

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return f"Yes"
    return f"No"

#XI. Counting sheep
def count_sheeps(sheeps):
    return sum(sheep for sheep in sheeps)

#XII. Is this my tail?
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False