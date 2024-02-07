import sys
input = sys.stdin.readline

def print_r(room):
	for row in room:
		print(row)
	print('--------------------')

height, width = map(int, input().strip().split(' '))
room = [list(map(int, input().strip().split(' '))) for _ in range(height)]

