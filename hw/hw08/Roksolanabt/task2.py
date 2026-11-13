import re


def check_password(password):
    errors = []
    if not re.search(r"[a-z]", password):
        errors.append("at least 1 lowercase letter [a-z]")
    if not re.search(r"[A-Z]", password):
        errors.append("at least 1 uppercase letter [A-Z]")
    if not re.search(r"[0-9]", password):
        errors.append("at least 1 digit [0-9]")
    if not re.search(r"[$#@]", password):
        errors.append("at least 1 special character from [$#@]")
    if len(password) < 6:
        errors.append("minimum length 6")
    if len(password) > 16:
        errors.append("maximum length 16")
    return errors


def main():
    password = input("Enter a password: ")
    errors = check_password(password)
    if not errors:
        print("Valid password")
    else:
        print("Invalid password. Requirements not met:")
        for error in errors:
            print(" -", error)


if __name__ == "__main__":
    main()