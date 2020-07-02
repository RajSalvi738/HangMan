import pygame
import os
import math

#display setup
pygame.init()
WIN_WIDTH, WIN_HEIGHT = 800, 500
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Hangman Game")

#font
FONT = pygame.font.SysFont('comicsans', 40)

#load the images
images = []
for img in os.listdir('images/'):
	image = pygame.image.load('images/' + img)
	images.append(image)

#button
BUTTON_RADIUS = 20
BUTTON_GAP = 15
letters = []
startX = round((WIN_WIDTH - (BUTTON_RADIUS * 2 + BUTTON_GAP) * 13) / 2)
startY = 400
A = 65

for i in range(26):
	x = startX + BUTTON_GAP * 2 + ((BUTTON_RADIUS * 2 + BUTTON_GAP) * (i % 13))
	y = startY + ((i // 13) * (BUTTON_GAP + BUTTON_RADIUS * 2))
	letters.append([x, y, chr(A + i), True])

#game variables
hangman_status = 0

#main loop
FPS = 60
clock = pygame.time.Clock()
run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw():
	win.fill(WHITE)

	for letter in letters:
		x, y, alphabet, is_visible = letter
		if is_visible:
			pygame.draw.circle(win, BLACK, (x, y), BUTTON_RADIUS, 3)
			text = FONT.render(alphabet, 1, BLACK)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()


while run:
	clock.tick(FPS)

	draw()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			for letter in letters:
				x, y, alphabet, is_visible = letter
				if is_visible:
					distance = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
					if distance < BUTTON_RADIUS:
						print(alphabet)
						letter[3] = False

pygame.quit()
