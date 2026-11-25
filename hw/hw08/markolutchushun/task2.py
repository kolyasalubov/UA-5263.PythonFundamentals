import areas

print("виберіть фігуру:")
print("1 - прямокутник")
print("2 - трикутник")
print("3 - коло")

choice = input("введіть: ")

if choice == "1":
    a = float(input("введіть сторну а: "))
    b = float(input("введіть сторну б: "))
    print("Площа прямокутника:", areas.rectangle_area(a, b))

elif choice == "2":
    a = float(input("Введіть основу a: "))
    h = float(input("Введіть висоту h: "))
    print("Площа трикутника:", areas.triangle_area(a, h))

elif choice == "3":
    r = float(input("Введіть радіус: "))
    print("Area:", areas.circle_area(r))

else:
    print("Неправильний вибір")

