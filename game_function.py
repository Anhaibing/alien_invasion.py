import sys
import pygame

def check_events(ship):
	#key & mouse event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			#按下按键
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#检测右键按下，并向右移动
					ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					ship.moving_left = True

			#松开按键
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					ship.moving_left = False

def update_screen(ai_settings, screen, ship):
	#redraw screen
		screen.fill(ai_settings.bg_color)
		#draw ship
		ship.blitme()
		#flash screen
		pygame.display.flip()