import pygame
pygame.init()


screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Game Menu")
clock = pygame.time.Clock()

menu_background = pygame.image.load("major_project/image/Good_background.png").convert()
menu_background = pygame.transform.scale(menu_background, (1366, 768))

button_start = pygame.image.load("major_project/image/start.png").convert_alpha()
button_start_hover = pygame.image.load("major_project/image/start_behide.png").convert_alpha()

scale_width = 0.7
scale_height = 0.2
narrow_factor = 0.85

new_width = int(button_start.get_width() * scale_width * narrow_factor)
new_height = int(button_start.get_height() * scale_height)

button_start = pygame.transform.scale(button_start, (new_width, new_height))
button_start_hover = pygame.transform.scale(button_start_hover, (new_width, new_height))

start_button_rect = button_start.get_rect(center=(1050, 420))


#MENU LOOP
menu_running = True
while menu_running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(mouse_pos):
                print("Start Game!")
                menu_running = False

    screen.blit(menu_background, (0, 0))

    if start_button_rect.collidepoint(mouse_pos):
        screen.blit(button_start_hover, start_button_rect)
    else:
        screen.blit(button_start, start_button_rect)

    pygame.display.flip()
    clock.tick(60)





# WRAP YOUR WORM GAME CODE INTO A FUNCTION
def run_worm_game():
    import pygame
    pygame.init()

# Variable I'll need later

    SCREEN_WIDTH = 1366
    SCREEN_HEIGHT = 768
    TILE_SIZE = 40

# Took it from tech with tim to set up total distance that can be moved and size of my snake moving or whatever is moving bruh

    GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
    GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

    FPS = 60

    class Game:
        def __init__(self):
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Bullshit I've been coding for hours now")

# Random sky image/Will change later

            self.background_img = pygame.transform.scale(
                pygame.image.load("major_project/image/Sky.png").convert(),
                (SCREEN_WIDTH, SCREEN_HEIGHT)
            )

#Resize all of my images so they fit in my tile movement logic

            self.block_img = pygame.transform.scale(
                pygame.image.load("major_project/image/Terre.png").convert(),
                (TILE_SIZE, TILE_SIZE)
            )

            self.apple_img = pygame.transform.scale(
                pygame.image.load("major_project/image/Apple.png").convert_alpha(),
                (TILE_SIZE, TILE_SIZE)
            )

            self.head_img = pygame.transform.scale(
                pygame.image.load("major_project/image/wormhead.png").convert_alpha(),
                (TILE_SIZE, TILE_SIZE)
            )

            self.body_img = pygame.transform.scale(
                pygame.image.load("major_project/image/wormbody.png").convert_alpha(),
                (TILE_SIZE, TILE_SIZE)
            )

#Objects I will use later on in the game

            self.level = Level(self)
            self.worm = Worm(self)

 #Two tests for apple to see if worm gets bigger/ if not change this part of the code

            apple_y = GRID_HEIGHT - 2 #Just so apple is above where I place blocks
            self.apples = [
                Apple(self, (8, apple_y)),
                Apple(self, (12, apple_y))
            ]

            self.clock = pygame.time.Clock()
            self.running = True

#How I process movement in the game/No prohibitions yet

        def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

#making sure it moves tile by tile

                    if event.key in (pygame.K_w, pygame.K_UP):
                        self.worm.try_move((0, -1))
                    elif event.key in (pygame.K_s, pygame.K_DOWN):
                        self.worm.try_move((0, 1))
                    elif event.key in (pygame.K_a, pygame.K_LEFT):
                        self.worm.try_move((-1, 0))
                    elif event.key in (pygame.K_d, pygame.K_RIGHT):
                        self.worm.try_move((1, 0))

 #ptting it all on the screen (thank you reddit for the base oop suggestions)

        def draw(self):
            # Background
            self.screen.blit(self.background_img, (0, 0))
            # Ground
            self.level.draw()
            # Apples
            for apple in self.apples:
                apple.draw()
            # Worm 
            self.worm.draw()

            pygame.display.flip()
            # Main loop
        def run(self):
            while self.running:
                self.handle_events()
                self.worm.apply_gravity()
                self.draw()
                self.clock.tick(FPS)
    # setting up da roads
    class Level:
        def __init__(self, game):
            self.game = game
            #whole last row gonna be ground for now
            self.blocks = []
            ground_y = GRID_HEIGHT - 1

            for x in range(GRID_WIDTH):
                self.blocks.append((x, ground_y))

# testing if this is a block

        def is_block(self, tile):
            return tile in self.blocks

        def draw(self):
            for gx, gy in self.blocks:
                px = gx * TILE_SIZE
                py = gy * TILE_SIZE
                self.game.screen.blit(self.game.block_img, (px, py))

#Apple class

    class Apple:
        # How it appears/disappea
        def __init__(self, game, position):
            self.game = game
            self.position = position
            self.active = True

        def draw(self):
            if not self.active:
                return
            gx, gy = self.position
            self.game.screen.blit(self.game.apple_img, (gx * TILE_SIZE, gy * TILE_SIZE))
# worm movement logic and gravity
    class Worm:
        def __init__(self, game):
            self.game = game
# throwing him in the sky (the worm) XD
            start_x = 3
            start_y = 1

            self.segments = [
                (start_x, start_y),
                (start_x - 1, start_y),
                (start_x - 2, start_y)
            ]

            self.direction = (1, 0)
            self.grow_amount = 0

            self.gravity_counter = 0
            self.gravity_delay = 10

        def head(self):
            return self.segments[0]

        def set_direction(self, direction):
            self.direction = direction

        def try_move(self, direction):
            self.set_direction(direction)
            dx, dy = self.direction

            hx, hy = self.head()
            new_head = (hx + dx, hy + dy)

            if not (0 <= new_head[0] < GRID_WIDTH): return
            if not (0 <= new_head[1] < GRID_HEIGHT): return
            if self.game.level.is_block(new_head): return
            if new_head in self.segments: return

            self._move_to(new_head)

        def apply_gravity(self):
            self.gravity_counter += 1
            if self.gravity_counter < self.gravity_delay:
                return
            self.gravity_counter = 0
# Logic for worm stan on only one block and rest of body can move freely horizontallly
            supported = False

            for (sx, sy) in self.segments:
                below = (sx, sy + 1)

                if below[1] >= GRID_HEIGHT:
                    supported = True
                    break

                if self.game.level.is_block(below):
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
                    self.grow(2)

        def grow(self, amount):
            self.grow_amount += amount

        def draw(self):
            hx, hy = self.segments[0]
            self.game.screen.blit(self.game.head_img, (hx * TILE_SIZE, hy * TILE_SIZE))

            for gx, gy in self.segments[1:]:
                self.game.screen.blit(self.game.body_img, (gx * TILE_SIZE, gy * TILE_SIZE))
#Start the bullshit game
    game = Game()
    game.run()
    pygame.quit()



run_worm_game()
