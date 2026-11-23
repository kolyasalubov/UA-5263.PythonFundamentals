# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

def greet_v2(name):
    return f"Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    distance = pow((x2-x1)**2 + (y2-y1)**2, 0.5)
    return round(distance, 2)


# III. No yelling!
def filter_words(st):
    st = st.split()
    output = str()
    output = output.join(_ + " "for _ in st).capitalize().strip()
    return output

def filter_words_v2(st):
    return " ".join(st.split()).capitalize()


# IV. Convert a Number to a String
def number_to_string(num : int) -> str:
    return f"{num}"


# V. Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])


# VI. Reverse List Order
def reverse_list(l):
    return l[::-1]


# VII. Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

 
# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"

are_you_playing_banjo_v2 = lambda name: f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
bool_to_word = lambda boolean: "Yes" if bool(boolean) else "No"


# XI. Counting sheep
def count_sheeps(sheeps_array):
    sum = 0
    for i in sheeps_array:
        if i == True:
            sum += 1
        else:
            sum += 0
    return sum


# XII. Is this my tail?
def correct_tail(body: str, tail: str) -> bool:
    if body.endswith(tail):
        return True
    return False

correct_tail_v2 = lambda body, tail: True if body[-1] == tail else False
