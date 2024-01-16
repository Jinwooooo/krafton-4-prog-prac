def partition_matrix(matrix):
    n = len(matrix)
    
    if n % 2 != 0:
        raise ValueError("Matrix dimensions should be even for partitioning")

    mid = n // 2

    # Extracting four submatrices
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]

    return top_left, top_right, bottom_left, bottom_right

# Example usage
n = 4
original_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = partition_matrix(original_matrix)

print("Top Left Matrix:")
for row in result[0]:
    print(row)

print("\nTop Right Matrix:")
for row in result[1]:
    print(row)

print("\nBottom Left Matrix:")
for row in result[2]:
    print(row)

print("\nBottom Right Matrix:")
for row in result[3]:
    print(row)


# import sys

# def prettify(mat):
# 	for row in mat:
# 		print(row)

# def create_board(n):
# 	board = []
# 	for _ in range(n):
# 	    row = []
# 	    for _ in range(n):
# 	        row.append(0)
# 	    board.append(row)

# 	return board

# def place_piece(board, n, pos):
# 	x, y = pos
# 	board[x][y] = -1

# 	return board

# def chk_validity(board, n, pos):
# 	x, y = pos

# 	# vertical
# 	for i in range(n):
# 		if board[x][i] == -1:
# 			return False

# 	# LU diag
# 	for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 		if board[i][j] == -1:
# 			return False

# 	# RU diag
# 	for i, j in zip(range(x, -1, -1), range(y, n, 1)):
# 		if board[i][j] == -1:
# 			return False

# 	# # vertical
# 	# for i in range(n):
# 	# 	if board[x][i] == -1:
# 	# 		return False

# 	# # LU diag
# 	# for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 	# 	if board[i][j] == -1:
# 	# 		return False

# 	# # LL diag
# 	# for i, j in zip(range(x, n, 1), range(y, -1, -1)):
# 	# 	if board[i][j] == -1:
# 	# 		return False

# 	return True


# n = 4
# pos = [0,0]
# board = create_board(n)

# print(chk_validity(board, n, pos))

# p2_arr = []
# for i in range(n):
# 	for j in range(n):
# 		p2_arr.append([i,j])

# for _ in range(n*n):
# 	for p2_tup in p2_arr:
# 		if(chk_validity(board, n, p2_tup) == True):
# 			place_piece(board, n, p2_tup)

# 	print('--------------')
# 	prettify(board)

# 	if sum(sum(board,[])) == -n:
# 		succ_place += 1

# 	board = create_board(n)
# 	p2_arr = p2_arr[1:]

# print(succ_place)

# temp_pos_s = [[0,0], [1,0], [1,1], [1,2], [2,0], [2,1], [3,0], [3,1], [3,2], [3,3]]
# temp_pos_s = [[0,1], [1,0], [1,1], [1,2], [1,3], [2,0], [3,0], [3,1], [3,2]]

# for temp_pos in temp_pos_s:
# 	if (chk_validity(board, n, temp_pos) == True):
# 		print("--- ... marking board ... ---")
# 		place_piece(board, n, temp_pos)
# 	else:
# 		print("--- ! ---")
# 		print("cannot place object in ", temp_pos, " position")
# 		print("--- ! ---")

# 	prettify(board)




# def chk_vert_validity(board, n, pos):
# 	x, y = pos

# 	# vertical
# 	for i in range(n):
# 		if board[i][y] == -1:
# 			return False

# 	return True

# def chk_hori_validity(board, n, pos):
# 	x, y = pos

# 	# horizontal
# 	for j in range(n):
# 		if board[x][j] == -1:
# 			return False

# 	return True

# def chk_diag_validity(board, n, pos):
# 	x, y = pos

# 	# LU
# 	for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# RU
# 	for i, j in zip(range(x, -1, -1), range(y, n, 1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# LL
# 	for i, j in zip(range(x, n, 1), range(y, -1, -1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# RL
# 	for i, j in zip(range(x, n, 1), range(y, n, 1)):
# 		if board[i][j] == -1:
# 			return False

# 	return True