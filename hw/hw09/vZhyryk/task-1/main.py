from random import randint

secretNumber = randint(1, 100)
tries = 10
attempt = 1

while attempt <= tries:
    try:
        guess = int(input(f"Спроба {attempt}/{tries}. Введи число: "))
    except ValueError:
        print("Введи нормальне число!")
        continue

    if guess == secretNumber:
        print("Вітаю, ти вгадав!")
        break
    elif guess < secretNumber:
        print("Загадане число більше")
    else:
        print("Загадане число менше")
    attempt += 1
else:
    print(f"Спроби закінчились. Було загадано {secretNumber}")
