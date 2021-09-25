#CS/2017/038
import pygame, sys
import numpy as np
from tkinter import messagebox as mb

pygame.init()

width = 600
height = 600
lineWidth = 15
winLineWidth = 15
rows = 3
columns = 3
squareSize = 200
circleRadius = 60
circleWidth = 15
crossWidth = 25
spaces = 55
bgColor = (70 ,70 , 170)
lineColor = (30, 30, 90)
circleColor = (204, 48, 0)
crossColor = (172, 90, 0)

screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption( 'CS/2017/038-TIC TAC TOE' )
screen.fill( bgColor )

board = np.zeros( (rows, columns) )

def drawLines():
	pygame.draw.line( screen, lineColor, (0, squareSize), (width, squareSize), lineWidth )
	pygame.draw.line( screen, lineColor, (0, 2 * squareSize), (width, 2 * squareSize), lineWidth )
	pygame.draw.line( screen, lineColor, (squareSize, 0), (squareSize, height), lineWidth )
	pygame.draw.line( screen, lineColor, (2 * squareSize, 0), (2 * squareSize, height), lineWidth )

def drawFigures():
	for row in range(rows):
		for col in range(columns):
			if board[row][col] == 1:
				pygame.draw.circle( screen, circleColor, (int( col * squareSize + squareSize//2 ), int( row * squareSize + squareSize//2 )), circleRadius, circleWidth )
			elif board[row][col] == 2:
				pygame.draw.line( screen, crossColor, (col * squareSize + spaces, row * squareSize + squareSize - spaces), (col * squareSize + squareSize - spaces, row * squareSize + spaces), crossWidth )	
				pygame.draw.line( screen, crossColor, (col * squareSize + spaces, row * squareSize + spaces), (col * squareSize + squareSize - spaces, row * squareSize + squareSize - spaces), crossWidth )

def markSquire(row, col, player):
	board[row][col] = player

def availableSquire(row, col):
	return board[row][col] == 0

def isboardfull():
	for row in range(rows):
		for col in range(columns):
			if board[row][col] == 0:
				return False

	return True

def message():
	mb.showinfo("Success!","Game Over")

def checkwin(player):
	for col in range(columns):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			verticalWinningLine(col, player)
			message()
			return True

	for row in range(rows):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			horizondalWinningLine(row, player)
			message()
			return True

	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		assendingDiagonal(player)
		message()
		return True

	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		decendingDiagonal(player)
		message()
		return True

def verticalWinningLine(col, player):
	posX = col * squareSize + squareSize//2

	if player == 1:
		color = circleColor
	elif player == 2:
		color = crossColor
		pygame.display.set_caption( 'Congratulation Cross is the Winner!' )

	pygame.draw.line( screen, color, (posX, 15), (posX, height - 15), lineWidth )

def horizondalWinningLine(row, player):
	posY = row * squareSize + squareSize//2

	if player == 1:
		color = circleColor
		pygame.display.set_caption( 'Congratulation Circle is the Winner!' )
	elif player == 2:
		color = crossColor
		pygame.display.set_caption( 'Congratulation Cross is the Winner!' )

	pygame.draw.line( screen, color, (15, posY), (width - 15, posY), winLineWidth )

def assendingDiagonal(player):
	if player == 1:
		color = circleColor
		pygame.display.set_caption( 'Congratulation Circle is the Winner!' )
	elif player == 2:
		color = crossColor
		pygame.display.set_caption( 'Congratulation Cross is the Winner!' )

	pygame.draw.line( screen, color, (15, height - 15), (width - 15, 15), winLineWidth )

def decendingDiagonal(player):
	if player == 1:
		color = circleColor
		pygame.display.set_caption( 'Congratulation Circle is the Winner!' )
	elif player == 2:
		color = crossColor
		pygame.display.set_caption( 'Congratulation Cross is the Winner!' )

	pygame.draw.line( screen, color, (15, 15), (width - 15, height - 15), winLineWidth )

def restart():
	screen.fill( bgColor )
	drawLines()
	for row in range(rows):
		for col in range(columns):
			board[row][col] = 0

drawLines()

player = 1
gameOver = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

			mouseX = event.pos[0]
			mouseY = event.pos[1]

			rowClicked = int(mouseY // squareSize)
			colClicked = int(mouseX // squareSize)

			if availableSquire( rowClicked, colClicked ):

				markSquire( rowClicked, colClicked, player )
				if checkwin( player ):
					gameOver = True
				player = player % 2 + 1

				drawFigures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				gameOver = False

	pygame.display.update()