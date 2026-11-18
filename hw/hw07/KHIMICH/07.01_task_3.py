word = input("Input Word: ")
def calc(text):
  char_count = {}
  for char in text:
    char_count[char] = char_count.get(char, 0) + 1
  return char_count

result = calc(word)
print(result)