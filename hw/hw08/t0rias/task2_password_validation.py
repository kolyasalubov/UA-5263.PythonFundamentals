import re

PASSWORD_PATTERN = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'

RULES = [
    (r'.*[a-z]', 'at least 1 lowercase letter [a-z]'),
    (r'.*[A-Z]', 'at least 1 uppercase letter [A-Z]'),
    (r'.*[0-9]', 'at least 1 number [0-9]'),
    (r'.*[$#@]', 'at least 1 character from [$#@]'),
    (r'.{6}', 'minimum length 6 characters'),
    (r'.{0,16}$', 'maximum length 16 characters'),
]

def is_valid_password(password: str) -> bool:
    """Return True if the password satisfies all validation rules."""
    return re.match(PASSWORD_PATTERN, password) is not None

def get_errors(password: str) -> list[str]:
    """Return a list of rules the password does not satisfy."""
    errors = []
    for pattern, message in RULES:
        if re.match(pattern, password) is None:
            errors.append(message)
    return errors

if __name__ == '__main__':
    user_password = input('Enter password: ')

    if is_valid_password(user_password):
        print('Valid password')
    else:
        print('Invalid password. Failed checks:')
        for error in get_errors(user_password):
            print(f'  - {error}')