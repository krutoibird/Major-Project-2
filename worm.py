from settings import TILE_SIZE, GRID_WIDTH, GRID_HEIGHT

class Worm:
    def __init__(self, game, start_pos):
        self.game = game

        start_x, start_y = start_pos

        
        self.segments = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y),
        ]

        self.direction = (1, 0)
        self.grow_amount = 0

        self.gravity_counter = 0
        self.gravity_delay = 10

    def head(self):
        return self.segments[0]

    def try_move(self, direction):
        dx, dy = direction
        hx, hy = self.head()
        new_head = (hx + dx, hy + dy)

        
        if not (0 <= new_head[0] < GRID_WIDTH):
            return
        if not (0 <= new_head[1] < GRID_HEIGHT):
            return

        
        if self.game.block.is_block(new_head):
            return

        
        if new_head in self.segments:
            return

        self._move_to(new_head)

    def apply_gravity(self):
        self.gravity_counter += 1
        if self.gravity_counter < self.gravity_delay:
            return
        self.gravity_counter = 0

        
        supported = False
        for (x, y) in self.segments:
            below = (x, y + 1)
            if below[1] >= GRID_HEIGHT or self.game.block.is_block(below):
                supported = True
                break

        if supported:
            return

        hx, hy = self.head()
        new_head = (hx, hy + 1)

        if new_head in self.segments:
            return

        self._move_to(new_head)

    def _move_to(self, new_head):
        self.segments.insert(0, new_head)

        if self.grow_amount > 0:
            self.grow_amount -= 1
        else:
            self.segments.pop()

        
        for apple in self.game.apples:
            if apple.active and apple.position == new_head:
                apple.active = False
                self.grow(1)

    def grow(self, amount):
        self.grow_amount += amount

    def draw(self):
        hx, hy = self.segments[0]
        self.game.screen.blit(
            self.game.head_img,
            (hx * TILE_SIZE, hy * TILE_SIZE)
        )

        for x, y in self.segments[1:]:
            self.game.screen.blit(
                self.game.body_img,
                (x * TILE_SIZE, y * TILE_SIZE)
            )
#2
