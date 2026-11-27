# Counting sheep...


def count_sheeps(sheep):
    return sum(sheep)


sheep = [True, True, True, False, True, True, True, True,
         True, False, True, False, True, False, False, True,
         True, True, True, True, False, False, True, True]
print(count_sheeps(sheep))  # 17
