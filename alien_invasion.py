import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#pygame init
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	#set title
	pygame.display.set_caption("Alien Invasion")

	#创建一个飞船，一个用于存储子弹的编组，一个用于存储外星人的编组
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings, screen, aliens)

	#cycle for game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()