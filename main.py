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

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#load the images
images = []
for img in os.listdir('images/'):
	image = pygame.image.load('images/' + img)
	images.append(image)


def draw(win, hangman_status, letters, word, guessed, BUTTON_RADIUS):
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

def button(BUTTON_RADIUS, BUTTON_GAP):
	letters = []
	startX = round((WIN_WIDTH - (BUTTON_RADIUS * 2 + BUTTON_GAP) * 13) / 2)
	startY = 400
	A = 65

	for i in range(26):
		x = startX + BUTTON_GAP * 2 + ((BUTTON_RADIUS * 2 + BUTTON_GAP) * (i % 13))
		y = startY + ((i // 13) * (BUTTON_GAP + BUTTON_RADIUS * 2))
		letters.append([x, y, chr(A + i), True])

	return letters

def choose_word(words):
	return random.choice(words)

def main(win):
	FPS = 60
	clock = pygame.time.Clock()
	run = True
	hangman_status = 0

	BUTTON_RADIUS = 20
	BUTTON_GAP = 15

	words = ['HELLO', 'DEVELOPER', 'PYGAME', 'GITHUB']	
	guessed = []

	word = choose_word(words)

	letters = button(BUTTON_RADIUS, BUTTON_GAP)

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

		draw(win, hangman_status, letters, word, guessed, BUTTON_RADIUS)

		is_won = True
		for letter in word:
			if letter not in guessed:
				is_won = False
				break

		if is_won:
			display_message("You WON!")
			hangman_status = 0
			guessed = []
			word = random.choice
			run = False

		if hangman_status == 6:
			display_message("You LOST!")
			run = False

def main_menu(win):
	run = True
	while run:
		win.fill(WHITE)
		text = WORD_FONT.render("Press Any Key To Play", 1, BLACK)
		win.blit(text, (WIN_WIDTH/2 - text.get_width()/2, WIN_HEIGHT/2 - text.get_height()/2))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				main(win)

	pygame.display.quit()

main_menu(win)
