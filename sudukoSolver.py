
sudoku =[ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def solve(board, s):
	if s == 'yes':
		print(" ")
		printBoard(board)
	find = findEmpty(board)
	if not find:
		return True
	else:
		row, col = find

	for i in range(1,10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve(board, s):
				return True

			board[row][col] = 0

	return False

def valid(board, num, pos):
	# check row 
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False
	# check column
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# check box
	box_x = pos[1] // 3
	box_y = pos[0] // 3 

	for i in range(box_y * 3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True

def printBoard(board):
	print ("- - - - - - - - - - - - -")

	for i in range(len(board)):
		if i%3 == 0 and i != 0:
			print ("- - - - - - - - - - - - -")


		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end='') 

			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ", end='') 

	print ("- - - - - - - - - - - - -")

def findEmpty(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return (i,j) # row, col

	return None 

printBoard(sudoku)
solve(sudoku, 'yes')
print('')
printBoard(sudoku)
