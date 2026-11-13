import math

def area_of_rectangle(width: float , height: float) -> float:
    """This function calculates square of rectangle."""
    
    return round(float(width * height), 2)

def area_of_triangle(a: float , b: float, c: float) -> float:
    """This function calculates square of triangle."""
    p = (a + b + c) / 2

    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)

def area_of_circle(radius: float) -> float:
    """This function calculates square of circle."""
        
    return round(math.pi * math.pow(radius, 2), 2)

def main():
    print(area_of_rectangle(2, 3))
    print(area_of_triangle(3, 4, 5))
    print(area_of_circle(10))

if __name__ == "__main__":
    main()