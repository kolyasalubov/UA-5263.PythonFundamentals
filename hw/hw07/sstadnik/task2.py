def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def triangle_area(base, height):
    """Return the area of a triangle."""
    return base * height / 2


def circle_area(radius):
    """Return the area of a circle."""
    return 3.14 * radius ** 2


def main():
    """Ask the user for a figure and print its area."""
    print('1 - rectangle')
    print('2 - triangle')
    print('3 - circle')
    choice = input('Choose a figure (1/2/3): ')

    if choice == '1':
        width = float(input('Width: '))
        height = float(input('Height: '))
        print('Area:', rectangle_area(width, height))
    elif choice == '2':
        base = float(input('Base: '))
        height = float(input('Height: '))
        print('Area:', triangle_area(base, height))
    elif choice == '3':
        radius = float(input('Radius: '))
        print('Area:', circle_area(radius))
    else:
        print('Unknown choice.')

main()
