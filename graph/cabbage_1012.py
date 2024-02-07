import sys
from collections import deque
input = sys.stdin.readline

# debug purposes
def print_field(field):
	for row in field:
		print(row)
	print('----------------')

def bfs_field(field, coord, width, length):
	q = deque([(coord[0], coord[1])])
	field[coord[0]][coord[1]] = 0

	while q:
		row, col = q.popleft()

		drow = [1,-1,0,0]
		dcol = [0,0,1,-1]

		for i in range(4):
			nrow = row + drow[i]
			ncol = col + dcol[i]
			
			if nrow < 0 or nrow >= length or ncol < 0 or ncol >= width:
				continue
			elif field[nrow][ncol] == 0:
				continue
			else:
				q.append((nrow, ncol))
				field[nrow][ncol] = 0

	return field


for _ in range(int(input())):
	width, length, no_cab = map(int, input().strip().split(' '))
	field = [[0 for _ in range(width)] for _ in range(length)]
	for _ in range(no_cab):
		col, row = map(int, input().strip().split(' '))
		field[row][col] = 1

	bug_ctr = 0
	for i in range(length):
		for j in range(width):
			if field[i][j] == 1:
				field = bfs_field(field, (i, j), width, length)
				bug_ctr += 1
	print(bug_ctr)
