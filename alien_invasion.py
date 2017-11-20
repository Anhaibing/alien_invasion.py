import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
	#pygame init
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	#set title
	pygame.display.set_caption("Alien Invasion")

	#make a ship
	ship = Ship(screen)

	#cycle
	while True:
		#exit event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#redraw screen
		screen.fill(ai_settings.bg_color)
		#draw ship
		ship.blitme()
		#flash screen
		pygame.display.flip()

run_game()