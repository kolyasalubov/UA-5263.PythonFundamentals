def count_sheeps(sheep):
  total = 0
  for i in sheep:
    if i == True:
      total += 1
  return total

count = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
print(count_sheeps(count))