import pygame
import table as t
import piece as p
from tkinter import messagebox  

#this file is responsible for the set-up of the match (creating the display and the table)
#it is also responsible for the functionalities of the "game loop" while the match is running

gameDisplay = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Checkers!")
clock = pygame.time.Clock()

print("Setting up game...")

table = t.table()
table.drawTable(gameDisplay)
turn = "red"

pygame.display.update()

crashed = False
gameOver = False

print("Game started!")

#game loop
while not crashed and not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			turn = table.movePiece(gameDisplay, event, turn)

	if table.isGameOver():
		gameOver = True
		print("Game over!")
		messagebox.showinfo("Game over!", "Color " + turn + " wins!")
 
	clock.tick(60)