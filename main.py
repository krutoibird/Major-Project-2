
import pygame
from menu import run_main_menu, run_level_select
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

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
            # start chosen level
            game = Game(level=choice)  # We can choose levels now
            game.run()
            state = "main_menu"

    else:
        pygame.quit()
        break
