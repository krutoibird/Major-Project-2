import pygame
from menu import main_menu, level_menu
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

state = "main_menu"

while True:
    if state == "main_menu":
        state = main_menu()

    elif state == "level_menu":
        state = level_menu()

    else:
        break

pygame.quit()

