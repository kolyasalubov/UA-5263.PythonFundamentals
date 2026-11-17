def is_valid_password(password: str) -> bool:
    return (
        6 <= len(password) <= 16
        and any("a" <= char <= "z" for char in password)
        and any("A" <= char <= "Z" for char in password)
        and any("0" <= char <= "9" for char in password)
        and any(char in "$#@" for char in password)
    )


def main() -> None:
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == "__main__":
    main()
