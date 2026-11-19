def calc_letters(input : str) -> dict:
    res = {}
    for idx in range(len(input)):
        try:
            res[input[idx]] = res[input[idx]] + 1
        except KeyError:
            res[input[idx]] = 1
    return res

val = input()

print(calc_letters(val))
