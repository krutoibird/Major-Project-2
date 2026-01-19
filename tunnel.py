import pygame
from settings import TILE_SIZE


class Tunnel:
    def __init__(self, game, position):
        self.game = game
        self.position = position

    def draw(self):
        gx, gy = self.position
        px = gx * TILE_SIZE
        py = gy * TILE_SIZE

        center = (px + TILE_SIZE // 2, py + TILE_SIZE // 2)
        pygame.draw.circle(self.game.screen, (0, 0, 0), center, TILE_SIZE // 3)