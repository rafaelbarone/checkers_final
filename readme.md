**CHECKERS!**

The code in this repository implements a basic game of checkers for two players using pygame for graphics

Important: pygame must be installed for the game to be executed

The basic rules are:

	- The table has 8x8 white and black boxes

	- There are white and red pieces, which can only move about the black boxes

	- The objective of the game is to eliminate all opposing pieces

	- In the beginning of the game, all pieces are considered "regular", which means they can only move forward on the table (with the exception of combos - will be explained later) and one block at a time

	- When a piece reaches the opposing end of the table, it becomes a "king" piece, which meants it can now also move backwards on the table and more than one block at a time

	- When a piece moves over an opposing piece, occupying a vacant block after it, it eliminates that opposing piece

	- When a piece has eliminated an opposing piece, it might get the chance to make a "combo", which is to eliminate another piece in one of the adjacent blocks (providing it has space to do so - the block after the opposing piece is vacant)


The game is implemented in three files:

	- piece.py: basic file responsible for implementing the class "piece", which is responsible for drawing individual pieces and holding the information for a given piece (color and wether that piece is a king or not)

	- table.py: most important file, responsible for the board and for all the behaviour of the game, please check the file and its comments for more information

	- main.py: responsible for setting up the game and for running the game loop
	
	
How to play:
	
	- The game starts with the red pieces
	
	- Select a piece by clicking on it (its box will be highlighted in red), unselect by pressing "esc" or clicking on it again
	
	- With a piece selected, move it by clicking on another box, if the move is possible, the piece will move immediately and, unless a combo is possible, this player's turn will end
	
	- If, after eliminating a piece, a combo is possible, a box will be highlighted in red to show the player that they may move their piece again. If they do not wish to do the combo, pressing "esc" will end the turn
