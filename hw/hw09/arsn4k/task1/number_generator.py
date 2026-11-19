import pygame
import random

pygame.init()

DISPLAY_HEIGHT = 850
DISPLAY_WIDTH = 650
SCREEN_COLOR = (196, 163, 163)


screen = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_WIDTH))
clock = pygame.time.Clock()
pygame.display.set_caption("Guess the number")

title_font = pygame.font.Font(None, 64)
title = title_font.render("Guess the number!", True, (64, 64, 64))

middle_label = pygame.font.Font(None, 50)
label = middle_label.render("Guess a number between 1 and 100.", True, (255,255,255))

attempts_counter = 10
attempts_text_font = pygame.font.Font(None, 35)

input_font = pygame.font.Font(None, 32)
input_text = ''

button_font = pygame.font.Font(None, 30)
button_text = button_font.render("GUESS", True, (0, 0, 0))

button_surface = pygame.Surface((150,50))
button_text_rect = button_text.get_rect(center=(button_surface.get_width() / 2,
                                                button_surface.get_height() / 2))

button_rect = pygame.Rect(350, 250, 150, 100)

input_box = pygame.Rect(225, 180, 400, 50)
active = False

random_number = random.randint(1, 100)
print(random_number)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        if attempts_counter > 0:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = True
                if button_rect.collidepoint(event.pos):
                    if int(input_text) == random_number:
                        print("You won")
                    elif int(input_text) != random_number and attempts_counter != 0:
                        attempts_counter -= 1
                    elif attempts_counter == 0:
                        print("You lost")
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(input_text)
                        input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
    
    screen.fill(SCREEN_COLOR)

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 850, 64))

    screen.blit(title, title.get_rect(center=(425,30)))
    screen.blit(label, label.get_rect(center=(425, 150)))
    attempts_text = attempts_text_font.render(f"Your attempts: {attempts_counter}", True, (255,255,255))
    screen.blit(attempts_text, attempts_text.get_rect(center=(120, 100)))

    txt_surface = input_font.render(input_text, True, (255, 255, 255))
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, (64,64,64), input_box, width=3, border_radius=10)


    button_surface.blit(button_text, button_text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))
    pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 150, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()