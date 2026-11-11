def calc_letters(input : str) -> dir:
    res = {}
    for idx in range(len(input)):
        res[input[idx]] = idx
    return res

val = input()

print(calc_letters(val))