import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
	#检测右键按下，并向右移动
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

	elif event.key == pygame.K_q:
		sys.exit()

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
			#按下按键
			if event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)

			#松开按键
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
	#redraw screen
	screen.fill(ai_settings.bg_color)

	#在飞船和外星人后面重回所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#draw ship
	ship.blitme()
	#draw aliens
	aliens.draw(screen)
	#flash screen
	pygame.display.flip()

def update_bullets(bullets):
	#删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))

def create_fleet(ai_settings, screen, aliens):
	'''创建外星人群'''
	#创建一个外星人，并计算一行可以容纳多少外星人
	#外星人间距为外星人宽度
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))

	#创建第一行外星人
	for alien_number in range(number_aliens_x):
		#创建一个外星人并将其加入当前行
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2*alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)
