from random import randint

secretNumber = randint(1, 100)
tries = 10

for attempt in range(1, tries + 1):
    try:
        guess = int(input(f"Спроба {attempt}/{tries}. Введи число: "))

        if guess == secretNumber:
            print("Вітаю, ти вгадав!")
            break
        elif guess < secretNumber:
            print("Загадане число більше")
        else:
            print("Загадане число менше")
    except ValueError:
        print("Введи нормальне число!")
else:
    print(f"Спроби закінчились. Було загадано {secretNumber}")
