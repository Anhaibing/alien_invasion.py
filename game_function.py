import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
	#检测右键按下，并向右移动
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		
def fire_bullet(ai_settings, screen, ship, bullets):
	#创建一颗子弹，将其加入大编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	#key & mouse event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			#按下按键
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)

			#松开按键
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	#redraw screen
	screen.fill(ai_settings.bg_color)

	#在飞船和外星人后面重回所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#draw ship
	ship.blitme()
	#flash screen
	pygame.display.flip()

def update_bullets(bullets):
	#删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))