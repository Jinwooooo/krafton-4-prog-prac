import sys
from collections import deque
input = sys.stdin.readline

def init_shark(mat, visit, height, width):
	coord = []

	for row in range(height):
		for col in range(width):
			if mat[row][col] == 1:
				mat[row][col] = 0
				visit[row][col] = True
				coord.append((row, col, 0))

	return mat, visit, coord

def bfs_shark(mat, visit, coord, height, width):
	move_list = [[1,0],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[0,1],[1,1]]
	q = deque([(row, col, dist) for row, col, dist in coord])

	while q:
		row, col, dist = q.popleft()

		for drow, dcol in move_list:
			nrow = row + drow
			ncol = col + dcol

			if 0 <= nrow < height and 0 <= ncol < width:
				if not visit[nrow][ncol]:
					ndist = dist + 1
					mat[nrow][ncol] = ndist
					visit[nrow][ncol] = True
					q.append((nrow, ncol, ndist))

	return mat

height, width = map(int, input().strip().split(' '))
mat = [list(map(int, input().strip().split(' '))) for _ in range(height)]
visit = [[False for _ in range(width)] for _ in range(height)]

mat, visit, coord = init_shark(mat, visit, height, width)
mat = bfs_shark(mat, visit, coord, height, width)

max_dist = 0
for row in mat:
	max_dist = max(max_dist, max(row))

if max_dist == 0:
	print(1)
else:
	print(max_dist)


