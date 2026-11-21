from random import randint

number = randint(1, 100)
tries = 10

for i in range(1, tries + 1):
    guess = int(input(f"Try {i} of {tries}. Enter a number from 1 to 100: "))

    if guess == number:
        print(f"Congratulations! You guessed the number {number} in {i} tries!")
        break
    elif guess < number:
        print("The number is greater")
    else:
        print("The number is less")
else:
    print(f"You have used all {tries} tries. The number was {number}")