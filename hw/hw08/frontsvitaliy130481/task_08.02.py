import re

password = input("Enter password to validate: ")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"
if re.match(pattern, password):
  print("Valid Password")
else:
  print("Invalid Password")