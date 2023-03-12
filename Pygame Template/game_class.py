# Pygame template
import pygame

# Settings
WIDTH = 360
HEIGHT = 480
TITLE = "My Game"
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game:
	def __init__(self): # Initialize game window, etc
		self.running = True
		pygame.init()
		pygame.mixer.init() # For sound or music
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
	
	def new(self): # Start a new game
		self.all_sprites = pygame.sprite.Group()
		self.run()
		
	def run(self): # Game loop
		self.playing = True
		while self.playing:
			# Keep loop running at the right speed
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
	
	def update(self): # Game loop - update
		self.all_sprites.update()
	
	def events(self): # Game loop - events
		# Process input (events)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
	
	def draw(self): # Game loop - draw
		self.screen.fill(RED)
		self.all_sprites.draw(self.screen)
		# *after* drawing everything flip the display
		pygame.display.flip() # or pygame.display.update()
	
	def show_start_screen(self):
		pass
	
	def show_game_over_screen(self):
		pass
		
		
g = Game()
g.show_start_screen()

while g.running:
	g.new()
	g.show_game_over_screen()
		
		
pygame.quit()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	