def correct_tail(body, tail):
    sub = body[-len(tail):]
    return sub == tail

print(correct_tail("Fox", "x"))
print(correct_tail("Rhino", "o"))
print(correct_tail("Meerkat", "t"))
print(correct_tail("Emu", "u"))
print(correct_tail("Badger", "g"))
print(correct_tail("Giraffe", "ffe"))