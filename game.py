import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from block import Block
from worm import Worm
from apple import Apple
from level_1 import LEVEL_1_MAP

class Game:
    def __init__(self, level=1):
        pygame.init()

        self.level = level
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Apple Worm")

        IMG = "major_project/image/"

        self.background_img = pygame.transform.scale(
            pygame.image.load(IMG + "Sky.png").convert(),
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.block_img = pygame.transform.scale(
            pygame.image.load(IMG + "Terre.png").convert(),
            (60, 60)
        )
        self.apple_img = pygame.transform.scale(
            pygame.image.load(IMG + "Apple.png").convert_alpha(),
            (60, 60)
        )
        self.head_img = pygame.transform.scale(
            pygame.image.load(IMG + "wormhead.png").convert_alpha(),
            (60, 60)
        )
        self.body_img = pygame.transform.scale(
            pygame.image.load(IMG + "wormbody.png").convert_alpha(),
            (60, 60)
        )

        self.clock = pygame.time.Clock()
        self.running = True
        self.win = False

        self.load_level()

    
    def load_level(self):
        self.apples = []
        self.block = Block(self)
        self.block.blocks = []

        worm_start = None

        for y, row in enumerate(LEVEL_1_MAP):
            for x, cell in enumerate(row):
                if cell == "#":
                    self.block.blocks.append((x, y))
                elif cell == "W":
                    worm_start = (x, y)
                elif cell == "O":
                    self.apples.append(Apple(self, (x, y)))

        self.worm = Worm(self, worm_start)

   
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                
                if event.key == pygame.K_r:
                    self.load_level()

                if event.key in (pygame.K_w, pygame.K_UP):
                    self.worm.try_move((0, -1))
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self.worm.try_move((0, 1))
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self.worm.try_move((-1, 0))
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.worm.try_move((1, 0))

    
    def check_win(self):
        for apple in self.apples:
            if apple.active:
                return
        self.win = True
        self.running = False

   
    def draw(self):
        self.screen.blit(self.background_img, (0, 0))
        self.block.draw()
        for apple in self.apples:
            apple.draw()
        self.worm.draw()
        pygame.display.update()

   
    def run(self):
        while self.running:
            self.handle_events()
            self.worm.apply_gravity()
            self.check_win()
            self.draw()
            self.clock.tick(FPS)
