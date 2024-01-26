import sys
from collections import deque

input = sys.stdin.readline

# debugging purposes
def print_g(land):
	print('-------------')
	for row in land:
		print(row)
	print('-------------')

def bfs_house(land, row, col, n):
	house_ctr = 1
	queue = deque([(row, col)])
	land[row][col] = 0

	drow = [1,-1,0,0]
	dcol = [0,0,1,-1]

	while queue:
		row, col = queue.popleft()

		for i in range(4):
			nrow = row + drow[i]
			ncol = col + dcol[i]

			# avoiding list out of bound
			if (nrow < 0 or nrow >= n or ncol < 0 or ncol >= n):
				continue
			# avoiding already visited
			elif land[nrow][ncol] == 0:
				continue
			else:
				land[nrow][ncol] = 0
				queue.append((nrow, ncol))
				house_ctr += 1

	return land, house_ctr

n = int(input())
land = []
for _ in range(n):
	land.append(list(map(int, input().strip())))

output_arr = []

# doing BFS everytime there is a non visited house cluster
for row in range(n):
	for col in range(n):
		if land[row][col] == 1:
			land, house_ctr = bfs_house(land, row, col, n)
			output_arr.append(house_ctr)

# BJ wanted output format
print(len(output_arr))
output_arr.sort()
for a in output_arr:
	print(a)
