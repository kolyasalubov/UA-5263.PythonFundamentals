from random import randint

number = randint(1, 100)
guessed = False

print('I picked a number from 1 to 100. You have 10 tries.')

for attempt in range(1, 11):
    guess = int(input('Enter a number: '))
    if guess == number:
        print('Congratulations! You guessed the number.')
        guessed = True
        break
    if number > guess:
        print('The number is greater than yours.')
    else:
        print('The number is less than yours.')

if not guessed:
    print('You have used all 10 attempts and did not guess the number.')
    print('The number was', number)
