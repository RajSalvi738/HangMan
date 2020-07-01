import pygame
import os

#display setup
pygame.init()
WIN_WIDTH, WIN_HEIGHT = 800, 500
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Hangman Game")

#load the images
images = []
for img in os.listdir('images/'):
	image = pygame.image.load('images/' + img)
	images.append(image)

#game variables
hangman_status = 0

#main loop
FPS = 60
clock = pygame.time.Clock()
run = True
WHITE = (255, 255, 255)

while run:
	clock.tick(FPS)

	win.fill(WHITE)
	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			print(mouse_pos)

pygame.quit()
