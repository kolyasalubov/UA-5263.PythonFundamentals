from random import randint


def play_guess_number(min_value: int = 1, max_value: int = 100, max_attempts: int = 10) -> None:
	secret_number = randint(min_value, max_value)
	attempts_used = 0

	print(f"Я загадав число від {min_value} до {max_value}. У тебе є {max_attempts} спроб!")

	while attempts_used < max_attempts:
		user_input = input(f"Спроба {attempts_used + 1}/{max_attempts}. Введи число: ")

		try:
			guess = int(user_input)
		except ValueError:
			print("Будь ласка, введи коректне ціле число.")
			continue

		attempts_used += 1

		if guess == secret_number:
			print(f"Вітаю! Ти вгадав число {secret_number} за {attempts_used} спроб!")
			return
		elif secret_number > guess:
			print("Загадане число більше за твоє.")
		else:
			print("Загадане число менше за твоє.")

	print(f" Спроби закінчилися! Я загадав число {secret_number}.")


if __name__ == "__main__":
	play_guess_number()
