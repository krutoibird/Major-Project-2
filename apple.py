from settings import TILE_SIZE

class Apple:
    def __init__(self, game, position):
        self.game = game
        self.position = position
        self.active = True

    def draw(self):
        if not self.active:
            return

        gx, gy = self.position
        px = gx * TILE_SIZE
        py = gy * TILE_SIZE

        self.game.screen.blit(self.game.apple_img, (px, py))
