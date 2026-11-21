num = input("Введіть число: ")

def reverse(num):
  number = num.split(" ")
  rev_num = number[::-1]
  result = " ".join(rev_num)
  return result

print(reverse(num))