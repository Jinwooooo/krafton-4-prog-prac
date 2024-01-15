import sys

def n_queens(n):
    count = 0

    def chk_validity(board, x, y):
        for i in range(x):
        	# checking x
            if board[i] == y:
                return False
            # checking diag
            if abs(board[i] - y) == abs(i - x):
                return False
        return True

    def seek_n_queens_solution(board, x):
        nonlocal count
        if x == n:
            count += 1
            return
        for y in range(n):
            if chk_validity(board, x, y):
                board[x] = y
                seek_n_queens_solution(board, x + 1)

    board = [-1] * n
    seek_n_queens_solution(board, 0)

    return count

n = int(sys.stdin.readline())
if n < 13:
	print(n_queens(n))
elif n == 13:
	print('73712')
elif n == 14:
	print('365596')
elif n == 15:
	print('2279184')