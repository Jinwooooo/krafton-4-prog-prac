def solve_n_queens(n):
    # 가능한 모든 솔루션의 수를 저장할 변수
    count = 0

    # 유효한 퀸 배치를 확인하는 함수
    def is_valid(board, row, col):
        # 같은 열에 퀸이 있는지 확인
        for i in range(row):
            if board[i] == col:
                return False
            # 대각선에 퀸이 있는지 확인
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    # 백트래킹 함수
    def backtrack(board, row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    # 초기 체스판 생성
    board = [-1] * n
    backtrack(board, 0)

    return count

n = 5  # N-퀸 문제에서의 N 값 (체스판 크기)
solution_count = solve_n_queens(n)
print(solution_count)
	
# This code is contributed by guptapratik


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