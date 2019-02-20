import pygame

#definition of the class responsible for the pieces in the board (white or red)

#pieces can become "kings" by reaching the opposing end of the table

class piece:
	def __init__(self, color, king):
	#creator of the class piece
		if (color == "red"):
			self.color = (255, 0, 0)
			self.colorTag = "red"
		else:
			self.color = (255, 255, 255)
			self.colorTag = "white"
		self.radius = 25
		if (king):
			self.isKing = True
		else:
			self.isKing = False

	def drawPiece(self, gameDisplay, x, y):
	#function responsible for drawing the pieces in the table 
		if (self.isKing):
			pygame.draw.circle(gameDisplay, self.color, (x*60 + 30, y*60 + 30), self.radius, 0)
			pygame.draw.circle(gameDisplay, (255, 255, 0), (x*60 + 30, y*60 + 30), self.radius//2, 2)
		else:
			pygame.draw.circle(gameDisplay, self.color, (x*60 + 30, y*60 + 30), self.radius, 0)

	def setKing(self):
	#function responsible for turning a regular piece into a "king" piece
		if not (self.isKing):
			self.isKing = True

	def getKing(self):
	#checks whether a piece is a king or not
		return self.isKing

	def getColorTag(self):
	#checks the color of the piece
		return self.colorTag