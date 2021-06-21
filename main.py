import sys

import pygame

pygame.init()

# Path maker
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
	print('running in a PyInstaller bundle')
	path = sys._MEIPASS + '/'
else:
	print('running in a normal Python process')
	path = ''

# Global defines
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(path + 'assets/font/pixel.ttf', 20)
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game Window Creating
img_icon = pygame.image.load(path + 'assets/icon.ico')
img_icon = pygame.transform.scale(img_icon, (32, 32))

pygame.display.set_icon(img_icon)
pygame.display.set_caption("Game Title")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Sound class and Music loading
class SFX:
	pass


pygame.mixer.music.load(path + 'audio/music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0, 5000)

# Array image loading

# Image loading

# Color define
GREEN = (13, 179, 20)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Groups
group = pygame.sprite.Group()


# Classes
class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

	def update(self):
		pass

	def draw(self):
		pass


# Functions
def draw_text(text, color, x, y, rightalign=False, font=FONT):
	textimg = font.render(text, True, color)
	if rightalign:
		x = SCREEN_WIDTH - textimg.get_width() - x
	screen.blit(textimg, (x, y))


def draw_background():
	# screen.blit(img_background, (0, 0))
	screen.fill(GREEN)


# Object init

# Game Events
running = True

# Game Loop
while running:
	CLOCK.tick(FPS)

	# Event Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Logic Loop
	draw_background()

	# Display Update
	pygame.display.update()

pygame.quit()
