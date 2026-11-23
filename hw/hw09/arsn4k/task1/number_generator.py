import pygame
import random

pygame.init()

DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 380
SCREEN_COLOR = (255, 255, 255)
TITLE_FONT_COLOR = (35, 43, 56)

program_icon = pygame.image.load(".\images\icon.jpg")
pygame.display.set_icon(program_icon)

screen = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_WIDTH), False)
clock = pygame.time.Clock()
pygame.display.set_caption("Guess the number")

title_font = pygame.font.SysFont(name="swiss721black", size=26, bold=False)

title = title_font.render("GUESS THE NUMBER!", True, TITLE_FONT_COLOR)

middle_label = pygame.font.SysFont(name="microsofttaile", size=26, bold=True)
label = middle_label.render("Guess a number between 1 and 100", True, TITLE_FONT_COLOR)

attempts_counter = 10
attempts_text_font = pygame.font.SysFont(name="microsoftyaheiui", size=20, bold=False)
feedback_text = ""

button_font = pygame.font.SysFont(name="arial", size=26, bold=True)
button_text = button_font.render("GUESS", True, (255, 255, 255))
button_rect = pygame.Rect(235, 200, 150, 50)
button_color = (76, 96, 122)

input_font = pygame.font.SysFont(name="Arial", size=24, bold=False)
input_text = '1234'
input_box = pygame.Rect(80, 130, 460, 52)
input_box_color = (0,0,0)
active = False
button_is_active = False

random_number = random.randint(1, 100)
print(random_number)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            active = input_box.collidepoint(event.pos)

            if button_rect.collidepoint(event.pos):
                button_is_active = True
                
                if input_text.isdigit():
                    if int(input_text) == random_number:
                        feedback_text = f"Congratulations, you guessed, the number is {random_number} "
                        attempts_text = attempts_text_font.render(f"{feedback_text}", True, (1,1,1))
                        screen.blit(attempts_text, attempts_text.get_rect(center=(300, 330)))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        flag = False
                    elif int(input_text) != random_number and attempts_counter != 0:
                        attempts_counter -= 1
                        feedback_text = f"You didn't guess the number, attempts left: {attempts_counter}"

                    elif attempts_counter == 0:
                        feedback_text = f"You lost, the number was: {random_number}"
                        attempts_text = attempts_text_font.render(f"{feedback_text}", True, (1,1,1))
                        screen.blit(attempts_text, attempts_text.get_rect(center=(300, 330)))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        flag = False
                else:
                    feedback_text = "Enter valid number"

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            button_is_active = False
        button_color = (59, 76, 99) if button_is_active else (76,96,122)      
        input_box_color = (1,1,1) if active else (100, 116, 139)   
                    
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
    screen.fill(SCREEN_COLOR)
    header_background = pygame.draw.rect(screen, (249, 250, 251), (0, 0, 600, 65))
    header_divider_line = pygame.draw.line(screen, (200, 203, 204), start_pos=(0,65), end_pos=(600,65), width=2)
    screen.blit(title, title.get_rect(center=(320, 32.5)))
    screen.blit(label, label.get_rect(center=(320, 100)))

    pygame.draw.rect(screen, input_box_color, input_box, width=3, border_radius=15)
    txt_surface = input_font.render(input_text, True, (1,1,1))
    screen.blit(txt_surface, (input_box.x+10, input_box.y+10))
    
    pygame.draw.rect(screen, button_color, button_rect, border_radius=100)
    screen.blit(button_text, (button_rect.x + 38, button_rect.y + 10))
    
    attempts_text = attempts_text_font.render(f"{feedback_text}", True, (1,1,1))
    screen.blit(attempts_text, attempts_text.get_rect(center=(300, 300)))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()