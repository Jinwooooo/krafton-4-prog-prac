import sys
from collections import deque

def bfs_maze(maze, rows, cols):
	queue = deque([])
	queue.append([0, 0])

	dy = [-1, 1, 0, 0]
	dx = [0, 0, -1, 1]

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			xx = x + dx[i]
			yy = y + dy[i]

			if 0 <= xx < rows and 0 <= yy < cols and maze[xx][yy] == 1:
				queue.append([xx, yy])
				maze[xx][yy] = maze[x][y] + 1

	return maze[rows-1][cols-1]

rows, cols = map(int, sys.stdin.readline().strip().split(' '))
maze = []
for _ in range(rows):
	maze.append(list(map(int, sys.stdin.readline().strip())))

print(bfs_maze(maze, rows, cols))
