import pygame
import piece as p

#definition of the class responsible for the board and all behaviour of pieces inside it

class table: 	
	def __init__(self):
	#creator of the class table
		self.pieceEliminated = False
		self.comboPossible = False
		#the two variables above are used to indicate characteristics of one particular move
		
		#below is the creation of the board - the variable grid is a matrix that 
			#keeps all the information neeeded (which positions are occupied and what is the kind
			#of piece occupying it)
		self.size = 8
		self.grid = [[0 for x in range(self.size)] for y in range(self.size)]

		#below the initial conditions of the match are set
		for y in range(self.size):
			for x in range(self.size):
				if ((y % 2 == 0) and (x % 2 != 0)):
					if (y < 3):
						self.grid[x][y] = p.piece("white", False)
					elif (y > 4):
						self.grid[x][y] = p.piece("red", False)
				elif ((y % 2 != 0) and (x % 2 == 0)):
					if (y < 3):
						self.grid[x][y] = p.piece("white", False)
					elif (y > 4):
						self.grid[x][y] = p.piece("red", False)
	
	def drawTable(self, gameDisplay):
	#function responsible for drawing the board at each movement.
	#first it draws the checkered background and then it draws the pieces according to their
		#positions on the matrix grid
		pygame.draw.rect(gameDisplay, (255, 255, 255), (0,0,480,480), 0)
		for y in range(self.size):
			for x in range(self.size):
				#draws the background board
				if ((y % 2 == 0) and (x % 2 != 0)):
					pygame.draw.rect(gameDisplay, (0,0,0), (x*60, y*60, 60, 60), 0)
				elif ((y % 2 != 0) and (x % 2 == 0)):
					pygame.draw.rect(gameDisplay, (0,0,0), (x*60, y*60, 60, 60), 0)
				#drawing the pieces in the table		
				if self.grid[x][y] != 0:
					self.grid[x][y].drawPiece(gameDisplay, x, y)

	def isGameOver(self):
	#checks if the game is over by counting all the pieces in the table
	#if one color has no pieces, the match has ended
		redPieces = 0
		whitePieces = 0
		for y in range (self.size):
			for x in range (self.size):
				if self.grid[x][y] != 0:
					if self.grid[x][y].getColorTag() == "red":
						redPieces += 1
					elif (self.grid[x][y].getColorTag() == "white"):
						whitePieces += 1
		if ((redPieces == 0) or (whitePieces == 0)):
			return True
		else:
			return False

	def isValidMove(self, x, y, newX, newY, turn):
	#checks if a given move is valid and returns true if it is and false if it is not
	#if a move should eliminate a piece, it does so already
		auxX = x
		auxY = y
		foundPiece = False
		#first check: new position chosen by user is a "black" box
		if (newY % 2 == 0 and not(newX % 2 != 0)):
			return False
		if (newY % 2 != 0 and not(newX % 2 == 0)):
			return False
		#second check: new position is not already occupied by another piece
		if (self.grid[newX][newY] != 0):
			return False
		#from here on out, there are two possibilites
		#possibility 1: the piece the user is trying to move is not a king, therefore it can only
			#move one square at a time (except when eliminating opposing pieces) and it can only move forward
		#possibility 2: the piece the user is trying to move is a king, therefore it can move more than
			#one square at a time and it can move backwards
		if not (self.grid[x][y].isKing):
			#implementation of possibility 1
			if (newY > y):
				if (turn == 'red'):
					print("Move not possible.")
					return False
				print ("Piece going down.")
				if newX > x:
					print("Piece going right.")
					if (newX - x == 1) and (newY - y == 1) and (self.grid[newX][newY] == 0):
						print("Move possible!")
						return True
					elif (newX - x == 2) and (newY - y == 2) and (self.grid[newX-1][newY-1] != 0):
						if(self.grid[newX-1][newY-1].getColorTag() != turn):
							print("Move possible, piece eliminated!")
							self.grid[newX-1][newY-1] = 0
							self.pieceEliminated = True
							return True
						else:
							print("Move not possible.")
							return False
					else:
						print("Move not possible.")
						return False
				else:
					print("Piece going left.")
					if (x - newX == 1) and (newY - y == 1) and (self.grid[newX][newY] == 0):
						print("Move possible!")
						return True
					elif (x - newX == 2) and (newY - y == 2) and (self.grid[newX+1][newY-1] != 0):
						if (self.grid[newX+1][newY-1].getColorTag() != turn):
							print("Move possible, piece eliminated!")
							self.grid[newX+1][newY-1] = 0
							self.pieceEliminated = True
							return True
						else:
							print("Move not possible.")
					else:
						print("Move not possible.")
						return False
			else:
				if (turn == "white"):
					print("Move not possible.")
					return False
				print ("Piece going up.")
				if newX < x:
					print("Piece going left.")
					if (x - newX == 1) and (y - newY == 1) and (self.grid[newX][newY] == 0):
						print("Move possible!")
						return True
					elif (x - newX == 2) and (y - newY == 2) and (self.grid[newX+1][newY+1] != 0):
						if (self.grid[newX+1][newY+1] != turn):	
							print("Move possible, piece eliminated!")
							self.grid[newX+1][newY+1] = 0
							self.pieceEliminated = True
							return True
						else:
							print("Move not possible.")
							return False
					else: 
						print("Move not possible.")
						return False
				else:
					print("Piece going right.")
					if (newX - x == 1) and (y - newY == 1) and (self.grid[newX][newY] == 0):
						print("Move possible!")
						return True
					elif (newX - x == 2) and (y - newY == 2) and (self.grid[newX-1][newY+1] != 0):
						if (self.grid[newX-1][newY+1].getColorTag() != turn):
							print("Move possible, piece eliminated!")
							self.grid[newX-1][newY+1] = 0
							self.pieceEliminated = True
							return True
						else:
							print("Move not possible.")
							return False
					else:
						print("Move not possible.")
						return False

		else:
			#implementation of possibility 2
			if (newY > y):
				print ("Piece going down.")
				if newX > x:
					print("Piece going right.")
					while newY > auxY:
						auxY += 1
						auxX += 1
						if (self.grid[auxX][auxY] != 0):
							print("Found a piece of the color " + self.grid[auxX][auxY].getColorTag() + " on the way.")
							if (self.grid[auxX][auxY].getColorTag() == turn):
								print("The color of both pieces are the same")
								return False
							foundPiece = True
						if (foundPiece):
							if (self.grid[auxX+1][auxY+1] != 0):
								print("The space next to the piece on the trajectory is not empty.")
								return False
							else:
								auxY += 1
								auxX += 1
								if ((auxY == newY) and (auxX == newX)):
									print("Move possible, piece eliminated.")
									self.pieceEliminated = True
									self.grid[auxX-1][auxY-1] = 0
									return True
								else:
									print("Move incorrect.")
									return False
					print("Move possible.")
					return True					

				else:
					print("Piece going left.")
					while newY > auxY:
						auxY += 1
						auxX -= 1
						if (self.grid[auxX][auxY] != 0):
							print("Found a piece of the color " + self.grid[auxX][auxY].getColorTag() + " on the way.")
							if (self.grid[auxX][auxY].getColorTag() == turn):
								print("The color of both pieces are the same")
								return False
							foundPiece = True
						if (foundPiece):
							if (self.grid[auxX-1][auxY+1] != 0):
								print("The space next to the piece on the trajectory is not empty.")
								return False
							else:
								auxY += 1
								auxX -= 1
								if ((auxY == newY) and (auxX == newX)):
									print("Move possible, piece eliminated.")
									self.pieceEliminated = True
									self.grid[auxX+1][auxY-1] = 0
									return True
								else:
									print("Move incorrect.")
									return False
					print("Move possible.")
					return True								

			else:
				print ("Piece going up.")
				if newX < x:
					print("Piece going left.")
					while newY < auxY:
						auxY -= 1
						auxX -= 1
						if (self.grid[auxX][auxY] != 0):
							print("Found a piece of the color " + self.grid[auxX][auxY].getColorTag() + " on the way.")
							if (self.grid[auxX][auxY].getColorTag() == turn):
								print("The color of both pieces are the same")
								return False
							foundPiece = True
						if (foundPiece):
							if (self.grid[auxX-1][auxY-1] != 0):
								print("The space next to the piece on the trajectory is not empty.")
								return False
							else:
								auxY -= 1
								auxX -= 1
								if ((auxY == newY) and (auxX == newX)):
									print("Move possible, piece eliminated.")
									self.pieceEliminated = True
									self.grid[auxX+1][auxY+1] = 0
									return True
								else:
									print("Move incorrect.")
									return False
					print("Move possible.")
					return True				

				else:
					print("Piece going right.")
					while newY < auxY:
						auxY -= 1
						auxX += 1
						if (self.grid[auxX][auxY] != 0):
							print("Found a piece of the color " + self.grid[auxX][auxY].getColorTag() + " on the way.")
							if (self.grid[auxX][auxY].getColorTag() == turn):
								print("The color of both pieces are the same.")
								return False
							foundPiece = True
						if (foundPiece):
							if (self.grid[auxX+1][auxY-1] != 0):
								print("The space next to the piece on the trajectory is not empty.")
								return False
							else:
								auxY -= 1
								auxX += 1
								if ((auxY == newY) and (auxX == newX)):
									print("Move possible, piece eliminated.")
									self.pieceEliminated = True
									self.grid[auxX-1][auxY+1] = 0
									return True
								else:
									print("Move incorrect.")
									return False
					print("Move possible")
					return True


	def isComboPossible(self, gameDisplay, turn, x, y):
		#after a piece has eliminated an opposing piece, it might be able to do a "combo"
		#this function checks whether that's the case for a given situation and it basically
			#has two outpus: one is through the class variable comboPossible and the other is 
			#through an array, which informs what "kinds" of combos are possible (here, kind refers
			#to the direction of the combo) 
		print("Verifying possibility of combo.")
		comboType = [False, False, False, False]
		if (x > 0 and x < 7 and y > 0 and y < 7 and self.pieceEliminated):
			#find a way to store possibilities of combos
			if (self.grid[x-1][y-1] != 0 and self.grid[x-1][y-1].getColorTag() != turn):
				if (x >= 2 and y >= 2):
					if (self.grid[x-2][y-2] == 0):
						print("Possibility of type 1 combo found.")
						comboType[0] = True
			if (self.grid[x+1][y-1] != 0 and self.grid[x+1][y-1].getColorTag() != turn):
				if (x <= 5 and y >= 2):
					if (self.grid[x+2][y-2] == 0):
						print("Possibility of type 2 combo found.")
						comboType[1] = True
			if (self.grid[x+1][y+1] != 0 and self.grid[x+1][y+1].getColorTag() != turn):
				if (x <= 5 and y <= 5):
					if (self.grid[x+2][y+2] == 0):
						print("Possibility of type 3 combo found.")
						comboType[2] = True
			if (self.grid[x-1][y+1] != 0 and self.grid[x-1][y+1].getColorTag() != turn):
				if (x >= 2 and y <= 5):
					if (self.grid[x-2][y+2] == 0):
						print("Possibility of type 4 combo found")
						comboType[3] = True
		if (comboType == [False, False, False, False]):
			print("No combo possibility found.")
		return comboType

	def handleCombo(self, gameDisplay, comboType, x, y, xCombo, yCombo, turn):
		#if a combo is possible and the user chooses to do it, this function handles it
		#this function basically continues the movement of a piece, after it has already eliminated
			#an opposing piece in its "base movement"
		print("Entered function handleCombo!")
		choiceCombo = [False, False, False, False]
		comboType_aux = [False, False, False, False]
		validChoiceFound = False
		done = False
		if ((xCombo == x - 2) and (yCombo == y - 2)):
			print("Type 1 combo selected")
			choiceCombo[0] = True
			validChoiceFound = True
		elif ((xCombo == x + 2) and (yCombo == y - 2)):
			print("Type 2 combo selected")
			choiceCombo[1] = True
			validChoiceFound = True
		elif((xCombo == x + 2) and (yCombo == y + 2)):
			print("Type 3 combo selected")
			choiceCombo[2] = True
			validChoiceFound = True
		elif((xCombo == x - 2) and (yCombo == y + 2)):
			print("Type 4 combo selected")
			choiceCombo[3] = True
			validChoiceFound = True
		if validChoiceFound:
			if(choiceCombo[0] and comboType[0]):
				self.grid[xCombo][yCombo] = p.piece(turn, self.grid[x][y].getKing())
				self.grid[x][y] = 0
				self.grid[xCombo+1][yCombo+1] = 0
			elif(choiceCombo[1] and comboType[1]):
				self.grid[xCombo][yCombo] = p.piece(turn, self.grid[x][y].getKing())
				self.grid[x][y] = 0
				self.grid[xCombo-1][yCombo+1] = 0
			elif(choiceCombo[2] and comboType[2]):
				self.grid[xCombo][yCombo] = p.piece(turn, self.grid[x][y].getKing())
				self.grid[x][y] = 0
				self.grid[xCombo-1][yCombo-1] = 0
			elif(choiceCombo[3] and comboType[3]):
				self.grid[xCombo][yCombo] = p.piece(turn, self.grid[x][y].getKing())
				self.grid[x][y] = 0
				self.grid[xCombo+1][yCombo-1] = 0
			comboType_aux = self.isComboPossible(gameDisplay, turn, xCombo, yCombo)
			done = True
			self.crownAKing(xCombo, yCombo, turn)
		return comboType_aux

	def crownAKing(self, x, y, turn):
		#this function turns a regular piece into a "king" peace when it has reached the opposing
			#end of the table
		if (turn == "red"):
			if (y == 0):
				self.grid[x][y].setKing()
		else:
			if (y == 7):
				self.grid[x][y].setKing()


	def movePiece(self, gameDisplay, event, turn):
		#this function is called by main.py every time a use chooses a piece he wishes to move
		#it aggregates the functions drawTable(), isValidMove(), isComboPossible(), handleCombo()
			# and crownAKing()
		#it is the backbone of the game's functionality
		x = event.pos[0]//60
		y = event.pos[1]//60
		hasMoved = False
		if (self.grid[x][y] != 0):
			if (turn == self.grid[x][y].getColorTag()):
				pygame.draw.rect(gameDisplay, (255,0,0), (x*60, y*60, 60, 60), 2)
				pygame.display.update()
				done = False
				while not done:
					for event in pygame.event.get():
						if (event.type == pygame.QUIT):
							done = True
						if (event.type == pygame.KEYDOWN and event.key == 27):
							done = True
						if event.type == pygame.MOUSEBUTTONDOWN:
							newX = event.pos[0]//60
							newY = event.pos[1]//60
							if (newX == x) and (newY == y):
								done = True
							else:
								print("Trying to move a piece of the color: " + turn)
								self.pieceEliminated = False
								if (self.isValidMove(x, y, newX, newY, turn)):
									self.grid[newX][newY] = p.piece(turn, self.grid[x][y].getKing())
									self.grid[x][y] = 0
									self.crownAKing(newX, newY, turn)
									done = True
									hasMoved = True
									self.comboPossible = False
									comboType = self.isComboPossible(gameDisplay, turn, newX, newY)
									if not (comboType == [False, False, False, False]):
										self.comboPossible = True
		pygame.draw.rect(gameDisplay, (0,0,0), (x*60, y*60, 60, 60), 2)
		self.drawTable(gameDisplay)
		pygame.display.update()
		while self.comboPossible:
			if comboType[0]:
				pygame.draw.rect(gameDisplay, (255,0,0), ((newX-2)*60, (newY-2)*60, 60, 60), 2)
			if comboType[1]:
				pygame.draw.rect(gameDisplay, (255,0,0), ((newX+2)*60, (newY-2)*60, 60, 60), 2)
			if comboType[2]:
				pygame.draw.rect(gameDisplay, (255,0,0), ((newX+2)*60, (newY+2)*60, 60, 60), 2)
			if comboType[3]:
				pygame.draw.rect(gameDisplay, (255,0,0), ((newX-2)*60, (newY+2)*60, 60, 60), 2)
			pygame.display.update()	
			self.comboPossible = False
			done = False
			while not done:
				for event in pygame.event.get():
					if (event.type == pygame.QUIT):
						done = True
					if (event.type == pygame.KEYDOWN and event.key == 27):
						done = True
					if event.type == pygame.MOUSEBUTTONDOWN:
						xCombo = event.pos[0]//60
						yCombo = event.pos[1]//60
						comboType = self.handleCombo(gameDisplay, comboType, newX, newY, xCombo, yCombo, turn)
						if not (comboType == [False, False, False, False]):
							self.comboPossible = True
						print(self.comboPossible)
						self.drawTable(gameDisplay)
						pygame.display.update()
						newX = xCombo
						newY = yCombo
						done = True

		if not hasMoved:
			return turn
		else:
			if (turn == "red"):
				return "white"
			else:
				return "red"