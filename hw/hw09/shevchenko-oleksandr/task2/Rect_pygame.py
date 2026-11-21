import pygame


FPS = 60
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)


def main():
    pygame.init()
    game_display = pygame.display.set_mode(
        (WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE
    )
    pygame.display.set_caption("Move the rectangle")
    clock = pygame.time.Clock()
    coord_x = 50
    coord_y = 50
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen_width, screen_height = game_display.get_size()
        rectangle_width = min(WIDTH_RECTANGLE, screen_width)
        rectangle_height = min(HEIGHT_RECTANGLE, screen_height)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            coord_x -= DELTA_STEP
        if keys[pygame.K_RIGHT]:
            coord_x += DELTA_STEP
        if keys[pygame.K_UP]:
            coord_y -= DELTA_STEP
        if keys[pygame.K_DOWN]:
            coord_y += DELTA_STEP

        coord_x = max(0, min(coord_x, screen_width - rectangle_width))
        coord_y = max(0, min(coord_y, screen_height - rectangle_height))

        game_display.fill(BLACK_COLOR)
        pygame.draw.rect(
            game_display,
            RED_COLOR,
            (coord_x, coord_y, rectangle_width, rectangle_height),
        )
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
