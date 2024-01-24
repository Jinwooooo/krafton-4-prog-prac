import sys
from collections import deque

input = sys.stdin.readline

def print_g(box):
	for tray in box:
		for row in tray:
			print(row)
		print('---------------------')
	print('*********************')

def get_tomato_init_idx(graph, size):
	tomato_arr = []

	for i in range(size[2]):
		for j in range(size[1]):
			for k in range(size[0]):
				if graph[i][j][k] == 1:
					tomato_arr.append((i,j,k))

	return tomato_arr

def get_tomato_status(graph, size):
	max_tomato = size[0] * size[1] * size[2]
	curr_tomato = sum(list(map(lambda tray: sum(map(sum, tray)), box)))
	if max_tomato == curr_tomato:
		return True
	else:
		return False

def bfs_box(graph, size):
	
	visited = [[[False for _ in range(size[2])] for _ in range(size[1])]] * size[0]
	queue = deque([])

	# inserting all initial tomato position in queue
	for tomato_coord in get_tomato_init_idx(graph, size):
		queue.append(tomato_coord)

	dz = [1,-1,0,0,0,0]
	dy = [0,0,1,-1,0,0]
	dx = [0,0,0,0,1,-1]

	while queue:
		node = queue.popleft()

		for i in range(6):
			nz = z + dz[i]
			ny = y + dy[i]
			nx = x + dx[i]

			if ((0 <= nx < size[2]) and (0 <= ny < size[1]) and 
				(0 <= nz < size[0]) and graph[nz][ny][nx] != -1 and
				graph[nz][ny][nx] == 0:)
				graph[nz][ny][nx] = 1
				queue.append((nx, ny, nz))


x, y, z = map(int, input().strip().split(' '))
size = [x,y,z]
box = []
for _ in range(z):
	tray = []
	for _ in range(y):
		tray.append(list(map(int, input().strip().split(' '))))
	box.append(tray)



print_g(box)