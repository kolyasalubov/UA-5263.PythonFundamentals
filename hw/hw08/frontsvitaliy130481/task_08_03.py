from geometry import get_circle_area, get_rectangle_area, get_triangle_area

choice = input("Enter shape (rectangle/triangle/circle): ").strip().lower()

if choice == "rectangle":
  a = float(input("Side a: "))
  b = float(input("Side b: "))
  print(f"Rectangle area: {get_rectangle_area(a, b)}")

elif choice == "triangle":
  a = float(input("Base a: "))
  h = float(input("Height h: "))
  print(f"Triangle area: {get_triangle_area(a, h)}")

elif choice == "circle":
  r = float(input("Radius r: "))
  print(f"Circle area: {get_circle_area(r)}")

else:
  print("Unknown shape entered!")