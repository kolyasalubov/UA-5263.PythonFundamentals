from password_validator import is_valid_password


def main() -> None:
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == "__main__":
    main()
