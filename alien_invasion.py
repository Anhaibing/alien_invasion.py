import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
	#pygame init
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	#set title
	pygame.display.set_caption("Alien Invasion")

	#make a ship
	ship = Ship(ai_settings, screen)

	#创建一个用于存储子弹的编组
	bullets = Group()

	#cycle
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()