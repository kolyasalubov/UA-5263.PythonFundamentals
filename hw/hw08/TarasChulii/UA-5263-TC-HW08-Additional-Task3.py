import tc_area

def print_selected_choice(choice):
    print(f"You have selected {(choice).capitalize()}")


available_choice = ["rectangle", "triangle", "circle", "exit"]
print("Please choose square of which figure would you like to calculate?")

while True:
    print(f"You have the following options {available_choice}")
    choice = (input("Please enter your choice: ")).lower()
    match choice:
        case "rectangle":
            print_selected_choice(choice)
            width, height = map(float, input("Please enter Width and Height, separated by comma: ").split(","))
            print(f"Area of {choice.capitalize()} with Width({width}) and Height({height}) is {tc_area.area_of_rectangle(width, height)}")
        case "triangle":
            print_selected_choice(choice)
            a, b, c = map(float, input("Please enter length of each side of Triangle, separated by comma: ").split(","))
            print(f"Area of {choice.capitalize()} with sides length A({a}), B({b}) and C({c}) is {tc_area.area_of_triangle(a, b, c)}")
        case "circle":
            print_selected_choice(choice)
            radius = float(input("Please enter Radius of Circle: "))
            print(f"Area of {choice.capitalize()} with radius({radius}) is {tc_area.area_of_circle(radius)}")
        case "exit":
            print_selected_choice(choice)
            break
        case _:
           print(f"Invalid choice, please repeat !!!")        
