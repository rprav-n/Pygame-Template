# Pygame template
import pygame
import os

# Set up assets / folders
game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder,"assets")


# Settings
WIDTH = 800
HEIGHT = 600
TITLE = "My Game"
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Intialize
pygame.init()
pygame.mixer.init() # For sound or music
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.image = pygame.image.load(os.path.join(assets_folder, "player.png")).convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5
    
    def update(self):
        self.rect.x += 8
        self.rect.y += self.y_speed
        if self.rect.left >= WIDTH:
            self.rect.right = 0
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5


p = Player()
all_sprites.add(p)
        
# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # clock.tick_busy_loop(FPS)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Game
    all_sprites.update()

    # Draw / Render
    screen.fill(RED)
    all_sprites.draw(screen)
    
    # *after* drawing everything flip the display
    pygame.display.flip() # or pygame.display.update()
    

pygame.quit()

