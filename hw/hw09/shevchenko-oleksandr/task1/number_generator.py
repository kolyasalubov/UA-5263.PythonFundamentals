import random


def main():
    secret_number = random.randint(1, 100)
    attempts_left = 10

    print("Guess the number from 1 to 100. You have 10 attempts.")

    while attempts_left > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Enter a number from 1 to 100.")
            continue

        attempts_left -= 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {10 - attempts_left} attempt(s).")
            return

        if attempts_left == 0:
            break

        if guess < secret_number:
            print(f"The number is higher. Attempts left: {attempts_left}.")
        else:
            print(f"The number is lower. Attempts left: {attempts_left}.")

    print(f"No attempts left. The number was {secret_number}.")


if __name__ == "__main__":
    main()
