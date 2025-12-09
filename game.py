import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GRID_HEIGHT
from block import Block
from worm import Worm
from apple import Apple

class Game:
    def __init__(self, level=1):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bullshit I've been coding for hours now")

        # Load images
        self.background_img = pygame.transform.scale(
            pygame.image.load("assets/gameplay/Sky.png").convert(),
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        self.block_img = pygame.transform.scale(
            pygame.image.load("assets/gameplay/Terre.png").convert(),
            (60, 60)
        )

        self.apple_img = pygame.transform.scale(
            pygame.image.load("assets/gameplay/Apple.png").convert_alpha(),
            (60, 60)
        )

        self.head_img = pygame.transform.scale(
            pygame.image.load("assets/gameplay/wormhead.png").convert_alpha(),
            (60, 60)
        )

        self.body_img = pygame.transform.scale(
            pygame.image.load("assets/gameplay/wormbody.png").convert_alpha(),
            (60, 60)
        )
      
        self.block = Block(self)

        self.worm = Worm(self)

        apple_y = GRID_HEIGHT - 2
        self.apples = [
            Apple(self, (8, apple_y)),
            Apple(self, (12, apple_y))
        ]

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key in (pygame.K_w, pygame.K_UP):
                    self.worm.try_move((0, -1))
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self.worm.try_move((0, 1))
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self.worm.try_move((-1, 0))
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.worm.try_move((1, 0))

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
            self.draw()
            self.clock.tick(FPS)
