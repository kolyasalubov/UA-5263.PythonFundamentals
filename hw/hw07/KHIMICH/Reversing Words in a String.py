word = input()

def reverse(word):
  words = word.split()
  rev_words = words[::-1]
  result = " ".join(rev_words)
  return result


print(reverse(word))