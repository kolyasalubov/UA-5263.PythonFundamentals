def count_chars(text):
    result = {}
    for i in text:
        result[i] = result.get(i, 0) + 1
    return result


if __name__ == "__main__":
    print(count_chars("Cucumber")) 