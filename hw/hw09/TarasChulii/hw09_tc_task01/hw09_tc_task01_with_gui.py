
import pygame
from random import randint

# Constants
WIDTH, HEIGHT = 600, 200
BG_COLOR = (114, 157, 224)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ATTEMPTS_COUNT = 10
MIN_NUMBER = 1
MAX_NUMBER = 100


def check_choice(number, goal):
    if number < goal:
        return f"{number} is less than expected", BLACK, False

    if number > goal:
        return f"{number} is greater than expected", BLACK, False

    return f"Congratulations! You WIN! Goal: {goal}", GREEN, True


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Taras Chulii - HW09 - Task01 - Number Guessing Game")

    icon = pygame.image.load("./images/octopus_6420766.png")
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)

    # Game initialization
    goal = randint(MIN_NUMBER, MAX_NUMBER)

    input_text = ""
    attempts_count = 0

    game_finished = False
    game_won = False

    result = ""
    result_color = BLACK

    title = font.render(f"Guess a whole number from {MIN_NUMBER} to {MAX_NUMBER}", True, BLACK)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif not game_finished:

                    if event.key == pygame.K_RETURN:

                        if input_text:
                            number = int(input_text)

                            if MIN_NUMBER <= number <= MAX_NUMBER:

                                attempts_count += 1

                                result, result_color, game_won = check_choice(number, goal)

                                input_text = ""

                                if game_won or attempts_count >= ATTEMPTS_COUNT:
                                    game_finished = True

                                    if not game_won:
                                        result = (
                                            f"You LOSE! Goal was {goal}"
                                        )
                                        result_color = RED

                            else:
                                result = "Number must be between 1 and 100"
                                result_color = RED
                                input_text = ""

                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]

                    elif event.unicode.isdigit():
                        if len(input_text) < len(str(MAX_NUMBER)):
                            input_text += event.unicode

        # Rendering
        screen.fill(BG_COLOR)

        attempts_left = ATTEMPTS_COUNT - attempts_count

        screen.blit(title, (10, 10))

        if not game_finished:

            text_input = font.render(f"Enter number: {input_text}", True, BLACK)

            text_attempts = font.render(f"Attempts left: {attempts_left}", True, BLACK)

            screen.blit(text_input, (10, 40))
            screen.blit(text_attempts, (10, 70))

        text_result = font.render(result, True, result_color)
        screen.blit(text_result, (10, 110))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
