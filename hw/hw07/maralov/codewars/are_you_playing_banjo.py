# Are You Playing Banjo?


def are_you_playing_banjo(name):
    if name[0] in "Rr":
        return name + " plays banjo"
    return name + " does not play banjo"


print(are_you_playing_banjo("martin"))  # "martin does not play banjo"
print(are_you_playing_banjo("Rikke"))  # "Rikke plays banjo"
print(are_you_playing_banjo("bravo"))  # "bravo does not play banjo"
print(are_you_playing_banjo("rolf"))  # "rolf plays banjo"
