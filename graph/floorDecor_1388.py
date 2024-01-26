import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# debugging purposes
def print_g(floor):
	print('-------------')
	for row in floor:
		print(row)
	print('-------------')

def dfs_floor(floor, row, col, mrows, mcols):
	dmove = [1,-1]

	if floor[row][col] == '|':
		floor[row][col] = True
		for i in range(2):
			nrow = row + dmove[i]

			# avoiding list out of bound
			if (nrow < 0 or nrow >= mrows):
				continue 

			# if connected parts found, go deeper
			if floor[nrow][col] == '|':
				dfs_floor(floor, nrow, col, mrows, mcols)
	elif floor[row][col] == '-':
		floor[row][col] = True
		for i in range(2):
			ncol = col + dmove[i]

			if (ncol < 0 or ncol >= mcols):
				continue

			if floor[row][ncol] == '-':
				dfs_floor(floor, row, ncol, mrows, mcols)

	return floor

# initializing
mrows, mcols = map(int, input().strip().split(' '))
floor = []
for _ in range(mrows):
	floor.append(list(input().strip()))
result = 0

# traversing the whole matrix
for row in range(mrows):
	for col in range(mcols):
		if type(floor[row][col]) == str:
			floor = dfs_floor(floor, row, col, mrows, mcols)
			result += 1

print(result)
