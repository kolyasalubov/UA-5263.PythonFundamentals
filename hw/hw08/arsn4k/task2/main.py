import  areas_operations as ao
import menu

def main():
    """
    This function operates other functions and lets user enter sides
    """
    choice = menu.show_menu()

    if choice == 1:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"Area = {ao.calculate_area_of_rectangle(width, height)}")
    
    elif choice == 2:
        side_a = float(input("Enter side A: "))
        height = float(input("Enter height: "))
        print(f"Area = {ao.calculate_area_of_triangle(side_a, height)}")
    
    elif choice == 3:
        radius = float(input("Enter radius: "))
        print(f"Area = {ao.calculate_area_of_circle(radius)}")

    elif choice == 4:
        print("Exiting...")
    
    else:
        print("Wrong choice")

main()
