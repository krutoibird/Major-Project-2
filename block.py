from settings import TILE_SIZE, GRID_WIDTH, GRID_HEIGHT

class Block:
    def __init__(self, game):
        self.game = game
        self.blocks = []

        ground_y = GRID_HEIGHT - 3

        for x in range(GRID_WIDTH):
            self.blocks.append((x, ground_y))

    def is_block(self, tile):
        return tile in self.blocks

    def draw(self):
        for gx, gy in self.blocks:
            px = gx * TILE_SIZE
            py = gy * TILE_SIZE
            self.game.screen.blit(self.game.block_img, (px, py))
