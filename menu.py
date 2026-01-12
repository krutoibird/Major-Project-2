import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Apple Worm Menu")
clock = pygame.time.Clock()

#MAIN MENU

menu_background = pygame.image.load("major_project/image/real_background.png").convert()
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

button_start = pygame.image.load("major_project/image/real_start.png").convert_alpha()
button_start = pygame.transform.scale(button_start, (240, 120))
start_button_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))
hover_start_size = (int(240 * 1.15), int(120 * 1.15))

#LEVEL MENU

level_menu_bg = pygame.image.load("major_project/image/real_level_background.png").convert()
level_menu_bg = pygame.transform.scale(level_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

level_size = (120, 120)
hover_level_size = (int(120 * 1.15), int(120 * 1.15))
button_gap = 50
total_levels = 5

# Back button
back_button = pygame.image.load(
    "major_project/image/real_back_game start_menu_button.png"
).convert_alpha()
back_button_rect = back_button.get_rect(
    topleft=(50, SCREEN_HEIGHT // 2 - back_button.get_height() // 2)
)
hover_back_size = (
    int(back_button.get_width() * 1.15),
    int(back_button.get_height() * 1.15)
)

# Level buttons
level1_button = pygame.transform.scale(
    pygame.image.load("major_project/image/1level_button.png").convert_alpha(),
    level_size
)
level2_button = pygame.transform.scale(
    pygame.image.load("major_project/image/2level_button.png").convert_alpha(),
    level_size
)
level3_button = pygame.transform.scale(
    pygame.image.load("major_project/image/3level_button.png").convert_alpha(),
    level_size
)
level4_button = pygame.transform.scale(
    pygame.image.load("major_project/image/4level_button.png").convert_alpha(),
    level_size
)
level5_button = pygame.transform.scale(
    pygame.image.load("major_project/image/5level_button.png").convert_alpha(),
    level_size
)

start_x = SCREEN_WIDTH // 2 - (level_size[0] * total_levels + button_gap * (total_levels - 1)) // 2
start_y = SCREEN_HEIGHT // 2 - 200

level1_rect = level1_button.get_rect(topleft=(start_x, start_y))
level2_rect = level2_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 1, start_y))
level3_rect = level3_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 2, start_y))
level4_rect = level4_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 3, start_y))
level5_rect = level5_button.get_rect(topleft=(start_x + (level_size[0] + button_gap) * 4, start_y))

#MAIN MENU FUNCTION
def main_menu():
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse):
                    return "level_menu"

        screen.blit(menu_background, (0, 0))

        if start_button_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(button_start, hover_start_size)
            rect = enlarged.get_rect(center=start_button_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(button_start, start_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

#LEVEL MENU FUNCTION
def level_menu():
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button_rect.collidepoint(mouse):
                    return "main_menu"

                if level1_rect.collidepoint(mouse):
                    return run_level(1)

                if level2_rect.collidepoint(mouse):
                    return run_level(2)

                if level3_rect.collidepoint(mouse):
                    return run_level(3)

                if level4_rect.collidepoint(mouse):
                    return run_level(4)

                if level5_rect.collidepoint(mouse):
                    return run_level(5)

        screen.blit(level_menu_bg, (0, 0))

        def draw_button(img, rect):
            if rect.collidepoint(mouse):
                enlarged = pygame.transform.scale(img, hover_level_size)
                r = enlarged.get_rect(center=rect.center)
                screen.blit(enlarged, r)
            else:
                screen.blit(img, rect)

        draw_button(level1_button, level1_rect)
        draw_button(level2_button, level2_rect)
        draw_button(level3_button, level3_rect)
        draw_button(level4_button, level4_rect)
        draw_button(level5_button, level5_rect)

        if back_button_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(back_button, hover_back_size)
            rect = enlarged.get_rect(center=back_button_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(back_button, back_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

#RUN LEVEL
def run_level(level_number):
    from game import Game

    while True:
        game = Game(level=level_number)
        game.run()

        if game.restart:
            continue  
        break

    return "level_menu"
