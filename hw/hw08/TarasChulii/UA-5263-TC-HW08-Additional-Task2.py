import getpass
import re

def validation_password(password: str):
    if len(password) < 6:
        return f"The length of password should be more than 6 characters."

    if len(password) > 16:
        return f"The length of password should be less than 16 characters."

    if not re.search(r'[a-z]', password):
        return f"The password should contains at least one letter in lowercase."

    if not re.search(r'[A-Z]', password):
            return f"The password should contains at least one letter in uppercase."

    if not re.search(r'[0-9]', password):
            return f"The password should contains at least one digit."

    if not re.search(r'[$#@]', password):
            return f"The password should contains at least one special charcter from [$#@]."

    return f"Provided password successfully passed validation."

def main():
    print(validation_password(getpass.getpass("Enter your password: ")))

if __name__ == "__main__":
    main()