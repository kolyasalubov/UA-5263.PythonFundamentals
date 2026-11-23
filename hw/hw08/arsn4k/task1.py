import re

def check_password(password: str) -> str:
    """
    This function checks if the given password meets the following criteria:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character ($, #, @)
    - Length between 6 and 16 characters
    
    Args:
        password (str): input user's password

    Returns:
        str: validation message
    """
    checker = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$"
    result = bool(re.match(checker, password))

    if result:
        return "Your password is valid"
    return "Your password is invalid"

print(check_password("ABCabc123#"))         #valid
print(check_password("abc123"))             #invalid
print(check_password("aA1@bcdefghijklm"))   #invalid