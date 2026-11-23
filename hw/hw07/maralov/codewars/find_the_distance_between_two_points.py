# Simple: Find The Distance Between Two Points
import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


print(distance(1, 1, 0, 0))  # 1.41
print(distance(0, 0, 3, 4))  # 5.0
