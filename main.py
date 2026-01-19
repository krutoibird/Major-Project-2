
import pygame
from menu import main_menu, run_level, level_menu
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

state = "main_menu"

while True:

    if state == "main_menu":
        state = run_main_menu(screen, clock)

    elif state == "level_select":
        choice = run_level_select(screen, clock)
        if choice == "main_menu":
            state = "main_menu"
        else:
            game = Game(level=choice)
            result = game.run()
            state = result

    else:
        pygame.quit()
        break
