import sys
from collections import deque

input = sys.stdin.readline

def print_g(box):
	print('*********************')
	for tray in box:
		for row in tray:
			print(row)
		print('---------------------')
	print('*********************')

def init_tbox(graph, size):
	coord_arr = []
	visited = [[[False for _ in range(size[0])] for _ in range(size[1])] for _ in range(size[2])]

	for i in range(size[2]):
		for j in range(size[1]):
			for k in range(size[0]):
				if graph[i][j][k] == 1:
					coord_arr.append((k,j,i))
					visited[i][j][k] = True

	return coord_arr, visited

def bfs_tbox(graph, size):
	queue = deque([])

	# inserting all initial tomato position in queue
	coord_arr, visited = init_tbox(graph, size)
	for coord_val in coord_arr:
		queue.append(coord_val)

	dz = [1,-1,0,0,0,0]
	dy = [0,0,1,-1,0,0]
	dx = [0,0,0,0,1,-1]

	while queue:
		x, y, z = queue.popleft()

		for i in range(6):
			nz = z + dz[i]
			ny = y + dy[i]
			nx = x + dx[i]

			if (nx < 0 or nx >= size[0] or ny < 0 or ny >= size[1] or
				nz < 0 or nz >= size[2]):
				continue

			if graph[nz][ny][nx] == 0 and visited[nz][ny][nx] == False:
				visited[nz][ny][nx] = True
				graph[nz][ny][nx] = graph[z][y][x] + 1
				queue.append((nx, ny, nz))

	return graph

# getting input values
x, y, z = map(int, input().strip().split(' '))
size = [x,y,z]
box = []
for _ in range(z):
	tray = []
	for _ in range(y):
		tray.append(list(map(int, input().strip().split(' '))))
	box.append(tray)

iter_box = bfs_tbox(box, size)

# if any 0 remain after bfs, not possible for fully ripe
for tray in iter_box:
	for row in tray:
		for slot in row:
			if slot == 0:
				print(-1)
				exit(0)

req_day = max(list(map(lambda plane: max(map(max, plane)), iter_box)))
print(req_day - 1)


