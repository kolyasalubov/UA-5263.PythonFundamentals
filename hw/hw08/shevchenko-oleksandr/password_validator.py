def is_valid_password(password: str) -> bool:
    return (
        6 <= len(password) <= 16
        and any("a" <= char <= "z" for char in password)
        and any("A" <= char <= "Z" for char in password)
        and any("0" <= char <= "9" for char in password)
        and any(char in "$#@" for char in password)
    )
