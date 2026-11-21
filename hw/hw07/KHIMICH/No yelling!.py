word = input()

def filter_words(word):
    st1 = word.capitalize()
    st2 = " ".join(st1.split())
    return st2
print(filter_words(word))