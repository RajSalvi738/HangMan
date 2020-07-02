import pygame
import os
import math
import random

#display setup
pygame.init()
WIN_WIDTH, WIN_HEIGHT = 800, 500
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Hangman Game")

#font
FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

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
words = ['HELLO', 'DEVELOPER', 'PYGAME', 'GITHUB']
word = random.choice(words)
guessed = []

#main loop
FPS = 60
clock = pygame.time.Clock()
run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw():
	win.fill(WHITE)

	#drawing title
	text = TITLE_FONT.render("HANGMAN", 1, BLACK)
	win.blit(text, (WIN_WIDTH/2 - text.get_width()/2, 20))

	#drawing word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "

	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text, (400, 200))

	#drawing buttons
	for letter in letters:
		x, y, alphabet, is_visible = letter
		if is_visible:
			pygame.draw.circle(win, BLACK, (x, y), BUTTON_RADIUS, 3)
			text = FONT.render(alphabet, 1, BLACK)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()

def display_message(message):
	pygame.time.delay(1000)
	win.fill(WHITE)
	text = WORD_FONT.render(message, 1, BLACK)
	win.blit(text, (WIN_WIDTH/2 - text.get_width()/2, WIN_HEIGHT/2 - text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(3000)


while run:
	clock.tick(FPS)

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
						letter[3] = False
						guessed.append(alphabet)
						if alphabet not in word:
							hangman_status += 1

	draw()

	is_won = True
	for letter in word:
		if letter not in guessed:
			is_won = False
			break

	if is_won:
		display_message("You WON!")
		break

	if hangman_status == 6:
		display_message("You LOST!")
		break

pygame.quit()
