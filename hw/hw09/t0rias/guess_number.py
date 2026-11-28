from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10
"""Ask the user for a number until a valid value in range is entered."""
def read_guess(attempt):
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS}. Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"The number must be between {MIN_NUMBER} and {MAX_NUMBER}.")
            continue
        return guess

def main():
    secret = randint(MIN_NUMBER, MAX_NUMBER)
    print(f"I'm thinking of a number from {MIN_NUMBER} to {MAX_NUMBER}. "
          f"You have {MAX_ATTEMPTS} attempts.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = read_guess(attempt)

        if guess == secret:
            print(f"Congratulations! You guessed the number on attempt {attempt}.")
            return
        if guess < secret:
            print("The secret number is greater.")
        else:
            print("The secret number is less.")

    print(f"You've used all {MAX_ATTEMPTS} attempts. The number was {secret}.")

if __name__ == "__main__":
    main()