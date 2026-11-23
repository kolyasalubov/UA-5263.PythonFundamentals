# No yelling!


def filter_words(st):
    return " ".join(st.split()).capitalize()


print(filter_words("HELLO world!"))  # "Hello world!"
print(filter_words("This will not pass "))  # "This will not pass"
print(filter_words("NOW THIS is a VERY EXCITING test!"))  # Now this is a very exciting test!
