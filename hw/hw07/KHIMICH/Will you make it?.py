def fuel(distance, mpg, fuel_left):
  distance_to_run = fuel_left * mpg

  if distance_to_run >= distance:
    return True
  else:
    return False


print(fuel(50, 25, 2))