#better solution
def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


def filter_words(st):
    return " ".join(st.split()).capitalize()


def number_to_string(num : int) -> str:
    return str(num)


def reverse(st):
    return " ".join(st.split()[::-1])


def reverse_list(l):
    return l[::-1]


def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 ==0)
  
  
  
  def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (fuel_left * mpg >=distance_to_pump)


def are_you_playing_banjo(name):
    return (f'{name} plays banjo' if name[0].lower()=='r' else f'{name} does not play banjo')


def bool_to_word(boolean):
    return ('Yes' if boolean == 1 else 'No')



def count_sheeps(sheep):
    return sum(1 for i in sheep if i==True)
 


def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False
    
#better solution
def correct_tail(body, tail):
    return body.endswith(tail)