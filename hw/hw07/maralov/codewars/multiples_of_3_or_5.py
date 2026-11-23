# Multiples of 3 or 5


def solution(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(solution(10))  # 23
print(solution(16))  # 60
print(solution(3))  # 0
print(solution(-5))  # 0
