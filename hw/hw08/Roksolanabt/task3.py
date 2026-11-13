import areas

def main():
    print("Which figure's area do you want to calculate?")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")
    choice = input("Your choice: ").strip()

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print(f"Area of the rectangle: {areas.rectangle_area(a, b)}")
    elif choice == "2":
        h = float(input("Enter height h: "))
        a = float(input("Enter base a: "))
        print(f"Area of the triangle: {areas.triangle_area(h, a)}")
    elif choice == "3":
        r = float(input("Enter radius r: "))
        print(f"Area of the circle: {areas.circle_area(r)}")
    else:
        print("Unknown choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()

