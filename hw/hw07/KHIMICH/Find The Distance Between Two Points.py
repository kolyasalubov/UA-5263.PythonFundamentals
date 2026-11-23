import math

def distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  return round(result, 2)

print(distance((0, 0), (3, 4)))  # Виведе 5.0