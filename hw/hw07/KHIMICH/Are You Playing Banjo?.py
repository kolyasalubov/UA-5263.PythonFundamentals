name = input("Say your name: ")
def play(name):
    if "r" in name or "R" in name:
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
print(play(name))