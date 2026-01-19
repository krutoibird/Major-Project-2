import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from block import Block
from worm import Worm
from apple import Apple

from level_1 import LEVEL_1_MAP
from level_2 import LEVEL_2_MAP
from level_3 import LEVEL_3_MAP
from level_4 import LEVEL_4_MAP
from level_5 import LEVEL_5_MAP
from level_6 import LEVEL_6_MAP


LEVELS = {
    1: LEVEL_1_MAP,
    2: LEVEL_2_MAP,
    3: LEVEL_3_MAP,
    4: LEVEL_4_MAP,
    5: LEVEL_5_MAP,
    6: LEVEL_6_MAP,
}


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
        self.hole_img = pygame.transform.scale(
            pygame.image.load(IMG + "hole.png").convert_alpha(),
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

       
        self.restart = False

        self.load_level()

    def load_level(self):
        self.apples = []
        self.holes = []   #$
        self.voids = []   #?
        self.block = Block(self)
        self.block.blocks = []

        worm_start = None
        level_map = LEVELS[self.level]

        for y, row in enumerate(level_map):
            for x, cell in enumerate(row):
                if cell == "#":
                    self.block.blocks.append((x, y))
                elif cell == "W":
                    worm_start = (x, y)
                elif cell == "O":
                    self.apples.append(Apple(self, (x, y)))
                elif cell == "$":
                    self.holes.append((x, y))
                elif cell == "?":
                    self.voids.append((x, y))

        if worm_start is None:
            raise ValueError(f"LEVEL {self.level} Not W")

        self.worm = Worm(self, worm_start)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.restart = False

            if event.type == pygame.KEYDOWN:

                
                if event.key == pygame.K_q:
                    self.running = False
                    self.restart = False

                
                if event.key == pygame.K_r:
                    self.restart = True
                    self.running = False

                if event.key in (pygame.K_w, pygame.K_UP):
                    self.worm.try_move((0, -1))
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self.worm.try_move((0, 1))
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self.worm.try_move((-1, 0))
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.worm.try_move((1, 0))

    def check_hole(self):
        head_x, head_y = self.worm.segments[0]

        if (head_x, head_y) in self.holes:
            
            self.running = False
            self.restart = False

    def check_void(self):
        
        for segment in self.worm.segments:
            if segment in self.voids:
                
                self.running = False
                self.restart = True
                return

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))

        self.block.draw()

       
        for x, y in self.holes:
            self.screen.blit(self.hole_img, (x * 60, y * 60))

        for apple in self.apples:
            apple.draw()

        self.worm.draw()
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.worm.apply_gravity()
            self.check_void()   
            self.check_hole()   
            self.draw()
            self.clock.tick(FPS)

