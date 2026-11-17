def count_characters(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
input_str = "hello"
print(count_characters(input_str))

