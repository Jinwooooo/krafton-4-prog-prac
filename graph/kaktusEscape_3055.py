import sys
from collections import deque

input = sys.stdin.readline

def print_g(maze):
	print('----------------')
	for row in maze:
		print(row)
	print('----------------')

def init_kaktus(maze, mrows, mcols):
	queue = deque([])

	for row in range(mrows):
		for col in range(mcols):
			if maze[row][col] == 'S':
				queue.append((row, col))
			elif maze[row][col] == 'D':
				ext_coord = (row, col)

	# water must be inserted into q before player, or water spreads first
	for row in range(mrows):
		for col in range(mcols):
			if maze[row][col] == '*':
				queue.append((row, col))

	return queue, ext_coord

def dfs_kaktus(maze, mrows, mcols):
	queue, ext_coord = init_kaktus(maze, mrows, mcols)
	distance = [[0 for _ in range(mcols)] for _ in range(mrows)]

	drow = [1,-1,0,0]
	dcol = [0,0,1,-1]

	while queue:
		row, col = queue.popleft()

		# if player has arrived at 'D' coordinates
		if maze[ext_coord[0]][ext_coord[1]] == 'S':
			return distance[ext_coord[0]][ext_coord[1]]

		for i in range(4):
			nrow = row + drow[i]
			ncol = col + dcol[i]

			if 0 <= ncol < mcols and 0 <= nrow < mrows:
				if maze[row][col] == 'S' and (maze[nrow][ncol] == '.' or maze[nrow][ncol] == 'D'):
					maze[nrow][ncol] = 'S'
					distance[nrow][ncol] = distance[row][col] + 1
					queue.append((nrow, ncol))
				elif maze[row][col] == '*' and (maze[nrow][ncol] == '.' or maze[nrow][ncol] == 'S'):
					maze[nrow][ncol] = '*'
					queue.append((nrow, ncol))

		# simulation chk
		# print(queue)
		# print_g(distance)
		# print_g(maze)
	return "KAKTUS"

mrows, mcols = map(int, input().strip().split(' '))
maze = []
for _ in range(mrows):
	maze.append(list(map(str, input().strip())))

print(dfs_kaktus(maze, mrows, mcols))

