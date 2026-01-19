import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Apple Worm Menu")
clock = pygame.time.Clock()

# MAIN MENU
menu_background = pygame.image.load("major_project/image/real_background.png").convert()
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

button_start = pygame.image.load("major_project/image/real_start.png").convert_alpha()
button_start = pygame.transform.scale(button_start, (240, 120))
start_button_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))
hover_start_size = (int(240 * 1.15), int(120 * 1.15))

# LEVEL MENU
level_menu_bg = pygame.image.load("major_project/image/real_level_background.png").convert()
level_menu_bg = pygame.transform.scale(level_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

level_size = (120, 120)
hover_level_size = (int(120 * 1.15), int(120 * 1.15))
button_gap = 50
total_levels_first_row = 5
total_levels_second_row = 5 

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

# Level buttons 1~10
level_buttons = []
for i in range(1, 11):
    img = pygame.image.load(f"major_project/image/{i}level_button.png").convert_alpha()
    level_buttons.append(pygame.transform.scale(img, level_size))


start_x_first = SCREEN_WIDTH // 2 - (level_size[0] * total_levels_first_row + button_gap * (total_levels_first_row - 1)) // 2
start_y_first = SCREEN_HEIGHT // 2 - 200

level_rects = []

for i in range(5):
    rect = level_buttons[i].get_rect(topleft=(start_x_first + i * (level_size[0] + button_gap), start_y_first))
    level_rects.append(rect)


start_y_second = start_y_first + level_size[1] + 20
total_width_second_row = level_size[0] * total_levels_second_row + button_gap * (total_levels_second_row - 1)
start_x_second = SCREEN_WIDTH // 2 - total_width_second_row // 2

for i in range(5, 10):
    rect = level_buttons[i].get_rect(topleft=(start_x_second + (i - 5) * (level_size[0] + button_gap), start_y_second))
    level_rects.append(rect)

# MAIN MENU FUNCTION
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

# LEVEL MENU FUNCTION
def level_menu():
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse):
                    return "main_menu"
                
                for i, rect in enumerate(level_rects):
                    if rect.collidepoint(mouse):
                        return run_level(i + 1)

        screen.blit(level_menu_bg, (0, 0))

        
        for i, rect in enumerate(level_rects):
            img = level_buttons[i]
            if rect.collidepoint(mouse):
                enlarged = pygame.transform.scale(img, hover_level_size)
                r = enlarged.get_rect(center=rect.center)
                screen.blit(enlarged, r)
            else:
                screen.blit(img, rect)

        # Back button
        if back_button_rect.collidepoint(mouse):
            enlarged = pygame.transform.scale(back_button, hover_back_size)
            rect = enlarged.get_rect(center=back_button_rect.center)
            screen.blit(enlarged, rect)
        else:
            screen.blit(back_button, back_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

# RUN LEVEL
def run_level(level_number):
    from game import Game

    while True:
        game = Game(level=level_number)
        game.run()

        if game.restart:
            continue
        break

    return "level_menu"
