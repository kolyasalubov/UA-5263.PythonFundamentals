import re

password = input("Введіть пароль: ")

if (
    6 < len(password) < 16
    and re.search("[a-z]", password)
    and re.search("[A-Z]", password)
    and re.search("[0-9]", password)
    and re.search("[@#$]", password)
):
    print("правильний пароль")
else:
    print("не правильний пароль")