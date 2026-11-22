import re

def validate_password():
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$"
    password = input("Enter a password: ")
    return print(bool(re.match(pattern, password)))

validate_password()
