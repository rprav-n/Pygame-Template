# Pymunk for physics
# PIL for image manipulation
# Sockets for multiplayer
# Perlin-noise for random worlds

# Pygame template
import pygame
import os


# Settings
WIN_WIDTH = 380
WIN_HEIGHT = 600
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
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Sprite Groups
all_sprites = pygame.sprite.Group()


# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    dt = clock.tick(FPS) / 1000
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

